# Node plan — B_WF_CONTROL — Control recipes

> Parent: [EXECUTION_GRAPH.md](../../EXECUTION_GRAPH.md)

| Field | Value |
|-------|-------|
| **Node id** | `B_WF_CONTROL` |
| **Job** | `solve-control-problem` + `explain-control` with python-control plots |
| **Wave** | 6 |
| **Depends on** | B_WF_CIRCUITS `circuits_done` |
| **Write paths** | `workflows/control/**`, `skills/control/**`, `tests/integration/test_control_wf.py` |
| **Read paths** | WORKFLOWS control rows |
| **subagent_type** | generalPurpose |
| **Model** | `cursor-grok-4.6-high` |
| **Isolation** | `control` pack except C5 file |

---

## Objective

Classical control solve (TF, poles, step, Bode, root locus) via `run-python-control`; MATLAB-if-present optional and gated. Explain workflow cites + library plots (not invented PNGs). Export PNG+SVG.

## Non-goals

- `control-diagram-to-model` (B_C5)
- Simulink plants (cannot-do unless OSS equivalent)

## Contract

**Input:** `{ "circuits_done": true }`

**Output:** `{ "control_done": true, "recipe_ids": ["solve-control-problem","explain-control"] }`

## Commits

| # | Commit | Gate |
|---|--------|------|
| 42 | `feat(wf): solve-control-problem` | python-control |
| 43 | `feat(wf): explain-control plots` | svg+png in run dir |

## Do not

- Invent Bode bitmaps
- Require MATLAB in CI

## Return to graph

Recipe ids, tests, failures.
