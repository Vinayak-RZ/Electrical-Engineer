"""Hybrid router: explicit id skips classify; 0.15 asks; else unmatched."""

from __future__ import annotations

from dataclasses import dataclass

UNMATCHED = "unmatched-cosolver"
ASK_DELTA = 0.15


@dataclass(frozen=True)
class Route:
    recipe_id: str | None
    kind: str  # explicit | classified | ask | unmatched


def route(
    explicit_id: str | None,
    scores: list[tuple[str, float]] | None = None,
) -> Route:
    if explicit_id:
        return Route(explicit_id, "explicit")
    ranked = sorted(scores or [], key=lambda x: -x[1])
    if not ranked or ranked[0][1] <= 0:
        return Route(UNMATCHED, "unmatched")
    if len(ranked) >= 2 and ranked[0][1] - ranked[1][1] < ASK_DELTA:
        return Route(None, "ask")
    return Route(ranked[0][0], "classified")
