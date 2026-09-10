# Node plan — B_HOST — Host adapter docs

> Parent: [EXECUTION_GRAPH.md](../../EXECUTION_GRAPH.md)

| Field | Value |
|-------|-------|
| **Node id** | `B_HOST` |
| **Job** | Document Cursor, Claude Code, and OpenAI/Codex skills + MCP install |
| **Wave** | 8 |
| **Depends on** | B_MCP `mcp_tools` |
| **Write paths** | `docs/hosts/README.md`, `docs/hosts/cursor.md`, `docs/hosts/claude-code.md`, `docs/hosts/openai.md` |
| **Read paths** | skills paths, MCP command |
| **subagent_type** | generalPurpose |
| **Model** | `composer-2.5` |
| **Isolation** | `docs/hosts/` |

---

## Objective

Docs-only: copy/symlink `skills/<pack>/SKILL.md` and point stdio at `electrical-engineer mcp`. Students need not use Cursor; hosts are first-class among several. No `init-host` helper (ponytail).

## Non-goals

- Shipping host binaries
- Making Cursor the only path

## Contract

**Input:** `{ "mcp_tools": [] }`

**Output:** `{ "host_docs": true }`

## Commits

| # | Commit | Gate |
|---|--------|------|
| 60 | `docs(hosts): cursor claude openai adapters` | three files |

## Do not

- Write product code
- Require Cursor for v1 completeness

## Return to graph

Paths, failures.
