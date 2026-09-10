# Node plan — B_C4_SIM — Sim after confirm

> Parent: [EXECUTION_GRAPH.md](../../EXECUTION_GRAPH.md)

| Field | Value |
|-------|-------|
| **Node id** | `B_C4_SIM` |
| **Job** | After student-confirmed netlist, allow `run-spice` — never from unmatched |
| **Wave** | 8 |
| **Depends on** | B_WF_PACKS `pack_recipes` + B_PHOTO stub |
| **Write paths** | `workflows/circuits/simulate-after-confirm.yaml` (or extend photo recipe **after** confirm only), tests |
| **Read paths** | PRD C4 later row |
| **subagent_type** | generalPurpose |
| **Model** | `cursor-grok-4.6-high` |
| **Isolation** | that workflow + tests |

---

## Objective

A named recipe runs spice **only** if `confirm-topology` already wrote a confirmed flag in the run dir. Unmatched and unconfirmed photos still cannot simulate.

## Non-goals

- Auto-sim from “looks like a netlist”
- MATLAB-only plants

## Contract

**Input:** `{ "photo_stub": true }`

**Output:** `{ "confirmed_sim": true }`

## Commits

| # | Commit | Gate |
|---|--------|------|
| 57 | `feat(wf): simulate-after-confirm` | unconfirmed rejected |
| 58 | `test(wf): unmatched still no spice` | integration |

## Do not

- Attach spice to unmatched-cosolver

## Return to graph

`confirmed_sim`, tests, failures.
