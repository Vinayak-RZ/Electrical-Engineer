# Node plan — B_WF_CIRCUITS — Circuits recipes

> Parent: [EXECUTION_GRAPH.md](../../EXECUTION_GRAPH.md)

| Field | Value |
|-------|-------|
| **Node id** | `B_WF_CIRCUITS` |
| **Job** | Named circuits YAML + skill: solve, derive, simulate, review, explain |
| **Wave** | 5 |
| **Depends on** | B_WF_CROSS `recipe_ports` |
| **Write paths** | `workflows/circuits/**`, `skills/circuits/**`, `tests/integration/test_circuits_wf.py` |
| **Read paths** | WORKFLOWS §1 circuits, ARCHITECTURE figures |
| **subagent_type** | generalPurpose |
| **Model** | `cursor-grok-4.6-high` |
| **Isolation** | `circuits` pack only |

---

## Objective

Recipes: `solve-circuit-problem`, `derive-circuit`, `simulate-circuit` (`run-spice`, `repair_max: 2`), `review-circuit-solution`, `explain-circuits`. Skill `skills/circuits/SKILL.md` pedagogy only (no secrets). Numbers from sympy/spice or `unchecked`. Figures via schemdraw/matplotlib to PNG+SVG in the run dir.

## Non-goals

- Photo pipeline (B_PHOTO)
- Other packs

## Contract

**Input:** `{ "recipe_ports": [] }`

**Output:** `{ "circuits_done": true, "recipe_ids": [] }`

## Commits

| # | Commit | Gate |
|---|--------|------|
| 33 | `feat(wf): solve-circuit-problem` | YAML loads |
| 34 | `feat(wf): derive + check-numeric` | sympy path |
| 35 | `feat(wf): simulate-circuit repair_max 2` | exhaust → unchecked |
| 36 | `feat(wf): review + explain-circuits` | skill exists |
| 37 | `test(wf): circuits integration` | one run dir |

## Do not

- Fake spice success
- Commit textbook PDFs

## Return to graph

`recipe_ids`, tests, failures.
