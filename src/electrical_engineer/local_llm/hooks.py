"""Optional local-LLM hooks. Hosts skip this path."""

from __future__ import annotations

from electrical_engineer.local_llm.client import complete
from electrical_engineer.router.hybrid import route


def classify_scores(text: str) -> list[tuple[str, float]] | None:
    out = complete(f"classify:{text[:200]}")
    if out.get("skipped"):
        return None
    return [(str(out.get("text") or "unmatched-cosolver"), 0.5)]


def solve_explain_hook(prompt: str) -> dict:
    out = complete(prompt)
    if out.get("skipped"):
        return {"used_local_llm": False, "skipped": True}
    return {"used_local_llm": True, "text": out.get("text"), "skipped": False}


def route_with_llm(explicit_id: str | None, text: str | None = None):
    scores = classify_scores(text or "") if text and not explicit_id else None
    return route(explicit_id, scores)
