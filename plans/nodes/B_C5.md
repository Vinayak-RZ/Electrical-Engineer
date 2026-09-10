# Node plan — B_C5 — Control diagram stub

> Parent: [EXECUTION_GRAPH.md](../../EXECUTION_GRAPH.md)

| Field | Value |
|-------|-------|
| **Node id** | `B_C5` |
| **Job** | `control-diagram-to-model`: figure → structured model → UI confirm → no silent sim |
| **Wave** | 8 |
| **Depends on** | B_PHOTO pattern + B_WF_CONTROL |
| **Write paths** | `workflows/control/control-diagram-to-model.yaml`, vision hooks if shared, tests |
| **Read paths** | WORKFLOWS C5 |
| **subagent_type** | generalPurpose |
| **Model** | `cursor-grok-4.6-high` |
| **Isolation** | that workflow |

---

## Objective

Do **not** drop this catalog row. Same spirit as photo stub: multimodal understand a block-diagram or Bode screenshot, draft a model JSON, one UI confirm, stop (or later simulate only after confirm if a control sim node exists). No silent sim.

## Non-goals

- Full Simulink import
- Image generation of diagrams

## Contract

**Input:** `{ "control_done": true }`

**Output:** `{ "c5_stub": true, "silent_sim": false }`

## Commits

| # | Commit | Gate |
|---|--------|------|
| 59 | `feat(wf): control-diagram-to-model stub` | confirm required |

## Do not

- Drop the workflow id
- Auto-run python-control on unconfirmed models

## Return to graph

`c5_stub`, failures.
