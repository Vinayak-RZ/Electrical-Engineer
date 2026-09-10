"""Deterministic in-process YAML DAG FSM. No LLM calls here."""

from __future__ import annotations

from collections.abc import Callable, Mapping
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from typing import Any

DEFAULT_TIMEOUT_S = 120
MAX_TIMEOUT_S = 600
MAX_PARENT_NODES = 16

Activity = Callable[[dict[str, Any], dict[str, Any]], dict[str, Any]]


class RunnerError(Exception):
    pass


@dataclass(frozen=True)
class NodeSpec:
    id: str
    activity: str
    needs: tuple[str, ...] = ()
    optional: bool = False
    timeout_s: int = DEFAULT_TIMEOUT_S
    extras: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class Recipe:
    id: str
    nodes: dict[str, NodeSpec]


def parse_recipe(data: Mapping[str, Any]) -> Recipe:
    rid = str(data["id"])
    raw_nodes = data.get("nodes") or {}
    nodes: dict[str, NodeSpec] = {}
    for nid, body in raw_nodes.items():
        timeout = int(body.get("timeout_s", DEFAULT_TIMEOUT_S))
        timeout = min(timeout, MAX_TIMEOUT_S)
        timeout = max(timeout, 1)
        needs = tuple(body.get("needs") or [])
        skip = {"activity", "needs", "optional", "timeout_s"}
        extras = {k: v for k, v in body.items() if k not in skip}
        nodes[str(nid)] = NodeSpec(
            id=str(nid),
            activity=str(body["activity"]),
            needs=needs,
            optional=bool(body.get("optional", False)),
            timeout_s=timeout,
            extras=extras,
        )
    if len(nodes) > MAX_PARENT_NODES:
        raise RunnerError(f"parent cap {MAX_PARENT_NODES} nodes")
    recipe = Recipe(id=rid, nodes=nodes)
    _assert_acyclic(recipe)
    return recipe


def _assert_acyclic(recipe: Recipe) -> None:
    temp: set[str] = set()
    seen: set[str] = set()

    def visit(nid: str) -> None:
        if nid in seen:
            return
        if nid in temp:
            raise RunnerError("cycle")
        temp.add(nid)
        for dep in recipe.nodes[nid].needs:
            if dep not in recipe.nodes:
                raise RunnerError(f"unknown need {dep}")
            visit(dep)
        temp.remove(nid)
        seen.add(nid)

    for nid in recipe.nodes:
        visit(nid)


def ready_ids(recipe: Recipe, completed: Mapping[str, Any]) -> list[str]:
    ready: list[str] = []
    for nid, spec in recipe.nodes.items():
        if nid in completed:
            continue
        if all(n in completed for n in spec.needs):
            ready.append(nid)
    return sorted(ready)


def run_fsm(
    recipe: Recipe,
    activities: Mapping[str, Activity],
) -> dict[str, dict[str, Any]]:
    """Run until done or failed. Ready nodes may overlap; start order is sorted id."""
    completed: dict[str, dict[str, Any]] = {}
    while len(completed) < len(recipe.nodes):
        batch = ready_ids(recipe, completed)
        if not batch:
            raise RunnerError("blocked")
        start_order = list(batch)
        with ThreadPoolExecutor(max_workers=max(1, len(batch))) as pool:
            futs = {}
            for nid in start_order:
                spec = recipe.nodes[nid]
                fn = activities.get(spec.activity)
                if fn is None:
                    raise RunnerError(f"unknown activity {spec.activity}")
                inputs = {dep: completed[dep] for dep in spec.needs}
                futs[pool.submit(_call, fn, spec, inputs)] = nid
            for fut in as_completed(futs):
                nid = futs[fut]
                completed[nid] = fut.result()
    return completed


def _call(fn: Activity, spec: NodeSpec, inputs: dict[str, Any]) -> dict[str, Any]:
    payload = {"id": spec.id, "optional": spec.optional, **spec.extras}
    out = fn(payload, inputs)
    if not isinstance(out, dict):
        raise RunnerError(f"{spec.id} must return dict")
    return out
