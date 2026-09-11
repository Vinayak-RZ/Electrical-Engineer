"""RAG inventory. Untrusted ingest; metadata owned by EE."""

from __future__ import annotations

import json
from pathlib import Path

from electrical_engineer.runner.runs import project_root


def rag_root(cwd: Path | None = None) -> Path:
    d = project_root(cwd) / ".electrical-engineer" / "rag"
    d.mkdir(parents=True, exist_ok=True)
    return d


def inventory_path(cwd: Path | None = None) -> Path:
    return rag_root(cwd) / "inventory.json"


def load_inventory(cwd: Path | None = None) -> list[dict]:
    path = inventory_path(cwd)
    if not path.is_file():
        return []
    return json.loads(path.read_text())


def save_inventory(items: list[dict], cwd: Path | None = None) -> None:
    inventory_path(cwd).write_text(json.dumps(items, indent=2))


def add_doc(path: str, *, tags: dict | None = None, cwd: Path | None = None) -> dict:
    items = load_inventory(cwd)
    rec = {
        "path": path,
        "book_id": (tags or {}).get("book_id"),
        "chapter_id": (tags or {}).get("chapter_id"),
        "folder_tag": (tags or {}).get("folder_tag"),
        "domain_tag": (tags or {}).get("domain_tag"),
        "untrusted": True,
    }
    items.append(rec)
    save_inventory(items, cwd)
    return rec


def tag_doc(path: str, tags: dict, cwd: Path | None = None) -> dict | None:
    items = load_inventory(cwd)
    for rec in items:
        if rec.get("path") == path:
            rec.update({k: v for k, v in tags.items() if v is not None})
            save_inventory(items, cwd)
            return rec
    return None
