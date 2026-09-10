# Node plan — B_NODES — Activity registry

> Parent: [EXECUTION_GRAPH.md](../../EXECUTION_GRAPH.md)

| Field | Value |
|-------|-------|
| **Node id** | `B_NODES` |
| **Job** | Register Python activities; research UG EE steps; keep cannot-do honest |
| **Wave** | 3 |
| **Depends on** | B_CORE `run_json_schema` |
| **Write paths** | `src/electrical_engineer/nodes/**`, `docs/CANNOT_DO.md`, `tests/unit/test_registry.py` |
| **Read paths** | `docs/ARCHITECTURE.md` §15, `docs/WORKFLOWS.md` §2, `docs/curriculum-map.md`, `research/notes/ee-task-taxonomy-draft.md` |
| **subagent_type** | generalPurpose (explore first if needed) |
| **Model** | `cursor-grok-4.6-high` |
| **Isolation** | sole writer of `nodes/` |

---

## Objective

Registry of activities: `retrieve-passage`, `check-numeric`, `run-spice`, `run-python-control`, `run-matlab-if-present`, `run-load-flow`, `ask-human`, `label-unchecked`, `write-run-summary`, `solve-explain`, photo stages, `run-recipe`. Bodies may be stubs that fail closed except `label-unchecked` and `write-run-summary` which must work. After web/curriculum research, extra EE steps are either registered or listed in `docs/CANNOT_DO.md` (live protection actuation, tape-out analog, MATLAB-only Simulink plants, etc.).

## Non-goals

- Full ngspice quality (can stub until circuits recipes need it)
- Inventing workflows in the registry

## Contract

**Input:** `{ "run_json_schema": {} }`

**Output:** `{ "node_id_list": ["string"], "cannot_do": ["string"] }`

## Commits

| # | Commit | Gate |
|---|--------|------|
| 15 | `feat(nodes): registry + label-unchecked` | registry test |
| 16 | `feat(nodes): spice control loadflow seams` | missing-tool fail clear |
| 17 | `feat(nodes): photo stage stubs` | ports exist |
| 18 | `docs: cannot-do seed from research` | file non-empty |

## Do not

- Auto-attach `run-spice` to unmatched
- Pretend MATLAB exists in CI

## Return to graph

`node_id_list`, `cannot_do`, failures.
