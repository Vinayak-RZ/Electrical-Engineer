"""Run a named YAML recipe into an isolated run dir."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import electrical_engineer.nodes  # noqa: F401  register activities
from electrical_engineer.catalog import load_recipe
from electrical_engineer.nodes.registry import REGISTRY
from electrical_engineer.runner.fsm import run_fsm
from electrical_engineer.runner.runs import create_run_dir, new_run_id, node_dir, project_root
from electrical_engineer.unchecked import UNCHECKED


def execute(
    recipe_id: str,
    *,
    cwd: Path | None = None,
    run_root: Path | None = None,
    problem: dict[str, Any] | None = None,
    allow_all: bool = False,
) -> dict[str, Any]:
    del allow_all  # gates still apply inside nodes; EE_ALLOW_ALL is env-only
    root = project_root(cwd)
    recipe = load_recipe(recipe_id, cwd)
    run_id = new_run_id()
    run_dir = create_run_dir(run_root or root, run_id)
    if problem:
        (run_dir / "problem.json").write_text(json.dumps(problem))
    elif (Path.cwd() / "problem.json").is_file():
        problem = json.loads((Path.cwd() / "problem.json").read_text())
        (run_dir / "problem.json").write_text(json.dumps(problem))

    def wrap(fn):
        def inner(spec: dict[str, Any], inputs: dict[str, Any]) -> dict[str, Any]:
            payload = {
                **spec,
                "run_dir": str(run_dir),
                "recipe_id": recipe.id,
                "problem": problem or {},
            }
            out = fn(payload, inputs)
            nd = node_dir(run_dir, spec["id"])
            (nd / "out.json").write_text(json.dumps(out, default=str))
            return out

        return inner

    completed = run_fsm(recipe, {name: wrap(fn) for name, fn in REGISTRY.items()})
    summary_node = completed.get("summary") or next(reversed(completed.values()))
    payload = {
        "recipe_id": recipe.id,
        "run_id": run_id,
        "unchecked": bool(summary_node.get("unchecked")),
        "token": summary_node.get("token"),
        "value": summary_node.get("value"),
        "paths": summary_node.get("paths") or [],
        "nodes": {
            k: {"unchecked": v.get("unchecked"), "ok": v.get("ok")} for k, v in completed.items()
        },
    }
    if payload["unchecked"] and payload.get("token") is None:
        payload["token"] = UNCHECKED
    if not payload["unchecked"]:
        for v in completed.values():
            if isinstance(v, dict) and v.get("value") is not None:
                payload["value"] = v.get("value")
    (run_dir / "summary.json").write_text(json.dumps(payload, indent=2))
    return {"run_id": run_id, "run_dir": str(run_dir), "summary": payload}
