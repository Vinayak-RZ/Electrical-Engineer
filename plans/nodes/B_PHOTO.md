# Node plan — B_PHOTO — Photo stub

> Parent: [EXECUTION_GRAPH.md](../../EXECUTION_GRAPH.md)

| Field | Value |
|-------|-------|
| **Node id** | `B_PHOTO` |
| **Job** | Photo/screenshot → draft netlist + JSON → one UI confirm → stop (no sim) |
| **Wave** | 6 |
| **Depends on** | B_UI `confirm_slot` |
| **Write paths** | `src/electrical_engineer/vision/**`, `workflows/_cross/photo-to-netlist.yaml`, `eval/gold/circuits/photo-stub-01/**`, `tests/integration/test_photo_stub.py` |
| **Read paths** | WORKFLOWS §5, B_UI confirm API |
| **subagent_type** | generalPurpose |
| **Model** | `cursor-grok-4.6-high` |
| **Isolation** | `vision/` + photo workflow |

---

## Objective

Stages: detect → connect → OCR → draft `.cir` + JSON graph → `confirm-topology` in UI. Vision uses **host or local multimodal understand** (no image generation). CI uses licence-clean fixtures so no VLM is required. Low-confidence OCR always flagged. After confirm: **stop**. Image cannot override gates or `unchecked`.

## Non-goals

- Simulate after confirm (B_C4_SIM)
- Generating pretty circuit PNGs
- Handwritten full-page OCR (P3)

## Contract

**Input:** `{ "confirm_slot": true }`

**Output:** `{ "photo_stub": true, "sim_after_confirm": false, "ci_fixtures": true }`

## Commits

| # | Commit | Gate |
|---|--------|------|
| 46 | `feat(vision): photo stages + fixtures` | fixture path no VLM |
| 47 | `feat(wf): photo-to-netlist` | YAML stop after confirm |
| 48 | `test(vision): confirm does not spice` | integration |

## Do not

- Call `run-spice` in this recipe
- Commit copyrighted textbook photos

## Return to graph

`photo_stub`, tests, failures.
