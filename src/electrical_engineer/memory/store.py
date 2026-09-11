"""Capped untrusted markdown memory."""

from __future__ import annotations

from pathlib import Path

CAP = 32768
EXCERPT = 800


def project_memory(root: Path) -> Path:
    d = root / ".electrical-engineer" / "memory"
    d.mkdir(parents=True, exist_ok=True)
    return d


def user_memory() -> Path:
    d = Path.home() / ".local" / "share" / "electrical-engineer" / "memory"
    d.mkdir(parents=True, exist_ok=True)
    return d


def write_capped(path: Path, text: str) -> str:
    if len(text.encode()) <= CAP:
        path.write_text(text)
        return text
    summary = text[: EXCERPT * 2] + "\n\n[summarised: over 32KiB cap]\n"
    path.write_text(summary)
    return summary


def excerpt(path: Path) -> str:
    data = path.read_text() if path.is_file() else ""
    return data[:EXCERPT]


def list_files(root: Path) -> list[Path]:
    return sorted(p for p in root.glob("*.md") if p.is_file())
