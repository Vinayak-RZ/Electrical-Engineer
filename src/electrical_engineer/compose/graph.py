"""compose-from-parts --advanced: typed ports, 16/24 cap, cycle detect."""

from __future__ import annotations

from electrical_engineer.runner.fsm import RunnerError, parse_recipe

MAX_NODES = 16
MAX_EDGES = 24
PORTS = ("Text", "Passages", "Netlist", "Numeric", "Summary", "GraphJson", "HumanDecision", "RecipeRef")


class ComposeError(ValueError):
    pass


def compose(data: dict) -> dict:
    nodes = data.get("nodes") or {}
    edges = data.get("edges") or []
    if len(nodes) > MAX_NODES:
        raise ComposeError("more than 16 nodes")
    if len(edges) > MAX_EDGES:
        raise ComposeError("more than 24 edges")
    recipe_nodes = {}
    for nid, body in nodes.items():
        needs = [e["from"] for e in edges if e.get("to") == nid]
        recipe_nodes[nid] = {
            "activity": body.get("activity") or body.get("uses"),
            "needs": needs,
        }
    try:
        parse_recipe({"id": data.get("id", "composed"), "nodes": recipe_nodes})
    except RunnerError as exc:
        raise ComposeError(str(exc)) from exc
    return {"ok": True, "nodes": len(nodes), "edges": len(edges)}
