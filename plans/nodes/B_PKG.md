# Node plan — B_PKG — Package + CI

> Parent: [EXECUTION_GRAPH.md](../../EXECUTION_GRAPH.md)

| Field | Value |
|-------|-------|
| **Node id** | `B_PKG` |
| **Job** | Make an installable empty package and Ubuntu CI that can fail |
| **Wave** | 1 |
| **Depends on** | A1 `layout_contract` |
| **Write paths** | `pyproject.toml`, `uv.lock` (if used), `src/electrical_engineer/__init__.py`, `src/electrical_engineer/py.typed`, `tests/test_import.py`, `.github/workflows/ci.yml`, `scripts/validate.sh`, `.gitignore` (`runs/`, `ui/dist/`) |
| **Read paths** | `LICENSE`, A1 layout |
| **subagent_type** | generalPurpose |
| **Model** | `composer-2.5` |
| **Isolation** | no other writer on pyproject this wave |

---

## Objective

`uv` + hatchling `src/` layout; console script reserved (`electrical-engineer` can be a stub `--help`). Ubuntu GitHub Actions: ruff + pytest. `scripts/validate.sh` calls those. No PyPI publish.

## Non-goals

- Runner, UI, RAG
- Windows/macOS CI

## Contract

**Input:** `{ "layout_contract": {} }`

**Output:** `{ "pkg": true, "ci": "ubuntu", "validate_sh": true }`

## Commits

| # | Commit | Gate |
|---|--------|------|
| 7 | `chore: uv hatchling src layout` | `uv run python -c "import electrical_engineer"` |
| 8 | `ci: ubuntu lint pytest` | workflow file valid |

## Do not

- Add FastAPI/React yet
- Pin a RAG engine

## Return to graph

Files touched, commands that passed, failures.
