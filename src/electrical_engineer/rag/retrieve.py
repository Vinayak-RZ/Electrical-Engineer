"""Thin retrieve facade. Empty is visible. Engine chosen after spike numbers."""

from __future__ import annotations

import re
from pathlib import Path

from electrical_engineer.rag.inventory import listed_inventory, rag_root
from electrical_engineer.runner.runs import project_root

PASSAGE_CHARS = 1500


def _tokens(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def _read_text(rec: dict, cwd: Path | None) -> str:
    raw = rec.get("path") or ""
    p = Path(raw)
    if not p.is_absolute():
        root = project_root(cwd)
        for cand in (root / raw, rag_root(cwd) / raw):
            if cand.is_file():
                p = cand
                break
    if p.is_file():
        return p.read_text(errors="replace")
    return ""


def retrieve(
    filters: dict | None = None,
    *,
    query: str = "",
    cwd: Path | None = None,
) -> dict:
    filters = {k: v for k, v in (filters or {}).items() if v}
    hits = []
    qtok = _tokens(query) if query else set()
    for rec in listed_inventory(cwd):
        if any(rec.get(k) != v for k, v in filters.items()):
            continue
        text = _read_text(rec, cwd)
        score = len(qtok & _tokens(text)) if qtok else 1
        if qtok and score == 0:
            continue
        snippet = text[:PASSAGE_CHARS]
        hits.append(
            {
                **rec,
                "text": snippet,
                "score": score,
                "page": rec.get("page"),
            }
        )
    hits.sort(key=lambda h: (-int(h["score"]), str(h.get("chapter_id") or "")))
    hits = hits[:3]
    return {"passages": hits, "empty": len(hits) == 0, "filters": filters, "engine": "bm25"}
