"""Registered EE activity nodes. Bodies fail closed except label/summary."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

from electrical_engineer.unchecked import UNCHECKED

Activity = Callable[[dict[str, Any], dict[str, Any]], dict[str, Any]]

REGISTRY: dict[str, Activity] = {}


def register(name: str) -> Callable[[Activity], Activity]:
    def wrap(fn: Activity) -> Activity:
        REGISTRY[name] = fn
        return fn

    return wrap


@register("label-unchecked")
def label_unchecked(_spec: dict[str, Any], inputs: dict[str, Any]) -> dict[str, Any]:
    return {"unchecked": True, "token": UNCHECKED, "inputs": inputs}


@register("write-run-summary")
def write_run_summary(_spec: dict[str, Any], inputs: dict[str, Any]) -> dict[str, Any]:
    unchecked = any(
        isinstance(v, dict) and (v.get("unchecked") or v.get("token") == UNCHECKED)
        for v in inputs.values()
    )
    return {
        "recipe_id": _spec.get("recipe_id", ""),
        "unchecked": unchecked,
        "token": UNCHECKED if unchecked else None,
        "paths": [],
    }


def get(name: str) -> Activity:
    if name not in REGISTRY:
        raise KeyError(name)
    return REGISTRY[name]


def names() -> list[str]:
    return sorted(REGISTRY)
