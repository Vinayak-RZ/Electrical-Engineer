"""Discover checked-in YAML recipes."""

from __future__ import annotations

from pathlib import Path

import yaml

from electrical_engineer.runner.fsm import Recipe, parse_recipe
from electrical_engineer.runner.runs import project_root


def workflows_root(cwd: Path | None = None) -> Path:
    return project_root(cwd) / "workflows"


def list_workflow_ids(cwd: Path | None = None) -> list[str]:
    root = workflows_root(cwd)
    if not root.is_dir():
        return []
    ids: list[str] = []
    for path in sorted(root.glob("**/*.yaml")):
        data = yaml.safe_load(path.read_text()) or {}
        ids.append(str(data.get("id") or path.stem))
    return ids


def load_recipe(recipe_id: str, cwd: Path | None = None) -> Recipe:
    root = workflows_root(cwd)
    for path in root.glob("**/*.yaml"):
        data = yaml.safe_load(path.read_text()) or {}
        if str(data.get("id") or path.stem) == recipe_id:
            return parse_recipe(data)
    raise FileNotFoundError(recipe_id)
