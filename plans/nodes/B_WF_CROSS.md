# Node plan — B_WF_CROSS — Unmatched + compose

> Parent: [EXECUTION_GRAPH.md](../../EXECUTION_GRAPH.md)

| Field | Value |
|-------|-------|
| **Node id** | `B_WF_CROSS` |
| **Job** | Ship `unmatched-cosolver` and `compose-from-parts --advanced` |
| **Wave** | 4 |
| **Depends on** | B_NODES `node_id_list` |
| **Write paths** | `workflows/_cross/**`, `skills/_cross/**`, `src/electrical_engineer/compose/**`, `tests/unit/test_compose.py` |
| **Read paths** | WORKFLOWS §§3–4, ARCHITECTURE §6 |
| **subagent_type** | generalPurpose |
| **Model** | `cursor-grok-4.6-high` |
| **Isolation** | `_cross` + `compose/` |

---

## Objective

`unmatched-cosolver` YAML: optional retrieve → solve-explain → label-unchecked → summary. **No** spice/matlab/load-flow on this path. `compose-from-parts --advanced`: typed ports, ≤16 nodes / ≤24 edges, cycle detect, may emit `run-recipe`, gate = ask. Invalid graphs fail closed before spice. Router must not take this path because a prompt was interesting.

## Non-goals

- Pack-specific recipes (later nodes)
- Inventing DAGs in the router

## Contract

**Input:** `{ "node_id_list": [] }`

**Output:** `{ "recipe_ports": ["Text","Passages","Netlist","Numeric","Summary"], "compose": true, "unmatched_no_sim": true }`

## Commits

| # | Commit | Gate |
|---|--------|------|
| 23 | `feat(wf): unmatched-cosolver` | no sim nodes in YAML |
| 24 | `feat(compose): advanced 16/24` | over-cap rejects |

## Do not

- Auto-simulate unmatched
- Wait in MCP for compose ask (fail closed)

## Return to graph

Recipe ids, tests, failures.
