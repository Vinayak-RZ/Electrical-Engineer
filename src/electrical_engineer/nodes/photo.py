"""Photo-to-netlist stages. Confirm does not simulate."""

from __future__ import annotations

from typing import Any

from electrical_engineer.nodes.registry import register


@register("detect-components")
def detect_components(_spec: dict[str, Any], inputs: dict[str, Any]) -> dict[str, Any]:
    return {"components": [], "confidence": 0.0, "low_confidence": True, **inputs}


@register("connect-wires")
def connect_wires(_spec: dict[str, Any], inputs: dict[str, Any]) -> dict[str, Any]:
    return {"wires": [], **inputs}


@register("ocr-labels")
def ocr_labels(_spec: dict[str, Any], inputs: dict[str, Any]) -> dict[str, Any]:
    return {"labels": [], "low_confidence": True, **inputs}


@register("draft-netlist")
def draft_netlist(_spec: dict[str, Any], inputs: dict[str, Any]) -> dict[str, Any]:
    return {"cir": "* draft\n", "graph": {"nodes": [], "edges": []}, **inputs}


@register("confirm-topology")
def confirm_topology(_spec: dict[str, Any], inputs: dict[str, Any]) -> dict[str, Any]:
    return {"confirmed": False, "simulate": False, **inputs}


@register("retrieve-passage")
def retrieve_passage(_spec: dict[str, Any], inputs: dict[str, Any]) -> dict[str, Any]:
    return {"passages": [], "empty": True}


@register("solve-explain")
def solve_explain(_spec: dict[str, Any], inputs: dict[str, Any]) -> dict[str, Any]:
    return {"text": "unchecked", "unchecked": True}


@register("ask-human")
def ask_human(_spec: dict[str, Any], inputs: dict[str, Any]) -> dict[str, Any]:
    return {"asked": True, "waiting": True}


@register("run-recipe")
def run_recipe(_spec: dict[str, Any], inputs: dict[str, Any]) -> dict[str, Any]:
    return {"child": inputs.get("recipe_id"), "paths": []}
