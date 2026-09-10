# Node plan — B_MCP — stdio MCP

> Parent: [EXECUTION_GRAPH.md](../../EXECUTION_GRAPH.md)

| Field | Value |
|-------|-------|
| **Node id** | `B_MCP` |
| **Job** | Stateless stdio tools `list_workflows` and `run_workflow`; never wait |
| **Wave** | 4 |
| **Depends on** | B_NODES `node_id_list` |
| **Write paths** | `src/electrical_engineer/mcp/**`, `tests/integration/test_mcp.py` |
| **Read paths** | ARCHITECTURE §8, CLI run entry |
| **subagent_type** | generalPurpose |
| **Model** | `composer-2.5` |
| **Isolation** | `mcp/` only |

---

## Objective

`electrical-engineer mcp` speaks MCP stdio. `list_workflows` returns catalog ids. `run_workflow` starts a run and returns short JSON + artifact paths. If a gate would wait: fail closed with structured error + `ui_url` or `electrical-engineer ui --run <id>`. Host UI is not allow-all. No sessions, no `resume_*`.

## Non-goals

- HTTP/SSE MCP
- A second prompt loop inside MCP

## Contract

**Input:** `{ "node_id_list": [] }`

**Output:** `{ "mcp_tools": ["list_workflows","run_workflow"], "waits": false }`

## Commits

| # | Commit | Gate |
|---|--------|------|
| 20 | `feat(mcp): list_workflows + run_workflow` | protocol test |
| 21 | `test(mcp): fail-closed on gate` | no hang |

## Do not

- Sleep waiting for a human
- Implement HTTP transport

## Return to graph

Tools list, tests, failures.
