# Node plan — B_WF_PACKS — Remaining packs

> Parent: [EXECUTION_GRAPH.md](../../EXECUTION_GRAPH.md)

| Field | Value |
|-------|-------|
| **Node id** | `B_WF_PACKS` |
| **Job** | solve + explain YAML and skills for every remaining curriculum pack |
| **Wave** | 7 |
| **Depends on** | B_WF_CONTROL `control_done` |
| **Write paths** | `workflows/{signals,machines,power,electronics,measurements,em,power_electronics,maths}/**`, `skills/` same packs, `docs/CANNOT_DO.md`, one gold or cannot-do per pack |
| **Read paths** | `docs/curriculum-map.md`, WORKFLOWS catalog after D0 |
| **subagent_type** | generalPurpose |
| **Model** | `cursor-grok-4.6-high` |
| **Isolation** | those pack dirs only; sequential commits |

---

## Objective

For signals, machines, power, electronics, measurements, EM/fields, power electronics, maths-for-ee: ship `solve-<pack>` and `explain-<pack>` (ids may be improved, still renamable). Each pack: SKILL.md + YAML using registered nodes. If a solve cannot be verified with OSS tools, add a **cannot-do** row rather than a fake gold pass. Breadth over fake depth.

## Non-goals

- PG-only courses
- Civil/mechanical
- Full design/simulate DAG for every pack this wave (solve+explain is the bar; extra simulate only if a node already exists — e.g. load-flow for power)

## Contract

**Input:** `{ "control_done": true }`

**Output:** `{ "pack_recipes": {}, "cannot_do_added": [] }`

## Commits

| # | Commit | Gate |
|---|--------|------|
| 49 | `feat(wf): signals solve+explain` | YAML or cannot-do |
| 50 | `feat(wf): machines solve+explain` | same |
| 51 | `feat(wf): power solve+explain` | load-flow optional |
| 52 | `feat(wf): electronics solve+explain` | same |
| 53 | `feat(wf): measurements solve+explain` | same |
| 54 | `feat(wf): em solve+explain` | same |
| 55 | `feat(wf): power-electronics solve+explain` | same |
| 56 | `feat(wf): maths-for-ee solve+explain` | sympy |

## Do not

- One mega-commit for all packs
- Silent invention marked as checked

## Return to graph

`pack_recipes`, `cannot_do_added`, failures.
