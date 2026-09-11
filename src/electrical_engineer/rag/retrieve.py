"""Thin retrieve facade. Empty is visible. Engine chosen after spike numbers."""

from __future__ import annotations

from pathlib import Path

from electrical_engineer.rag.inventory import load_inventory, rag_root


def retrieve(filters: dict | None = None, *, cwd: Path | None = None) -> dict:
    filters = {k: v for k, v in (filters or {}).items() if v}
    items = load_inventory(cwd)
    hits = []
    for rec in items:
        if any(rec.get(k) != v for k, v in filters.items()):
            continue
        text = ""
        p = Path(rec["path"])
        if not p.is_absolute():
            p = rag_root(cwd) / rec["path"]
        if p.is_file():
            text = p.read_text()[:800]
        hits.append({**rec, "text": text})
    hits = hits[:3]
    return {"passages": hits, "empty": len(hits) == 0, "filters": filters, "engine": "bm25"}
