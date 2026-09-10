"""Registered EE activity nodes. Bodies fail closed except label/summary."""

from __future__ import annotations

import json
from collections.abc import Callable, Mapping
from pathlib import Path
from typing import Any

from electrical_engineer.unchecked import UNCHECKED

Activity = Callable[[dict[str, Any], dict[str, Any]], dict[str, Any]]

REGISTRY: dict[str, Activity] = {}


def register(name: str) -> Callable[[Activity], Activity]:
    def wrap(fn: Activity) -> Activity:
        REGISTRY[name] = fn
        return fn

    return wrap


def _walk_checked(inputs: Mapping[str, Any]) -> bool:
    for v in inputs.values():
        if not isinstance(v, dict):
            continue
        if v.get("ok") is True and not v.get("unchecked"):
            return True
        nested = v.get("inputs")
        if isinstance(nested, dict) and _walk_checked(nested):
            return True
    return False


@register("label-unchecked")
def label_unchecked(_spec: dict[str, Any], inputs: dict[str, Any]) -> dict[str, Any]:
    if _walk_checked(inputs):
        value = None
        for v in inputs.values():
            if isinstance(v, dict) and v.get("value") is not None:
                value = v.get("value")
        return {"unchecked": False, "token": None, "value": value, "inputs": inputs}
    return {"unchecked": True, "token": UNCHECKED, "inputs": inputs}


@register("write-run-summary")
def write_run_summary(_spec: dict[str, Any], inputs: dict[str, Any]) -> dict[str, Any]:
    checked = _walk_checked(inputs)
    value = None
    paths: list[str] = []
    for v in inputs.values():
        if not isinstance(v, dict):
            continue
        if v.get("value") is not None:
            value = v.get("value")
        paths.extend(v.get("paths") or [])
    out = {
        "recipe_id": _spec.get("recipe_id", ""),
        "unchecked": not checked,
        "token": None if checked else UNCHECKED,
        "value": value,
        "paths": paths,
    }
    run_dir = _spec.get("run_dir")
    if run_dir:
        Path(run_dir, "summary.json").write_text(json.dumps(out, indent=2))
        out["paths"] = [*paths, str(Path(run_dir) / "summary.json")]
    return out


def get(name: str) -> Activity:
    if name not in REGISTRY:
        raise KeyError(name)
    return REGISTRY[name]


def names() -> list[str]:
    return sorted(REGISTRY)
