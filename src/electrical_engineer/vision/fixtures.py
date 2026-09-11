"""CI fixtures for photo stub. No VLM required."""

from __future__ import annotations

from pathlib import Path

from electrical_engineer.runner.runs import project_root


def fixture_dir(cwd: Path | None = None) -> Path:
    return project_root(cwd) / "eval" / "gold" / "circuits" / "photo-stub-01"


def load_fixture(cwd: Path | None = None) -> dict:
    root = fixture_dir(cwd)
    cir = (root / "fixtures" / "draft.cir").read_text()
    return {
        "cir": cir,
        "vlm": False,
        "source": str(root),
        "low_confidence": True,
    }
