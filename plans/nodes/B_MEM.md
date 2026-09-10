# Node plan — B_MEM — Memory CLI

> Parent: [EXECUTION_GRAPH.md](../../EXECUTION_GRAPH.md)

| Field | Value |
|-------|-------|
| **Node id** | `B_MEM` |
| **Job** | Capped untrusted markdown memory + `electrical-engineer memory` |
| **Wave** | 4 |
| **Depends on** | B_CORE `run_dirs` / CLI surface |
| **Write paths** | `src/electrical_engineer/memory/**`, `tests/unit/test_memory.py` |
| **Read paths** | ARCHITECTURE §11 |
| **subagent_type** | generalPurpose |
| **Model** | `composer-2.5` |
| **Isolation** | `memory/` only |

---

## Objective

Project memory `.electrical-engineer/memory/`; user memory `~/.local/share/electrical-engineer/memory/`. One concern per file. 32 KiB cap → summarise, do not grow. Context: paths + ≤800 char excerpt. Explicit CLI: list/read/write helpers. Untrusted: cannot override gates or `unchecked`. Not the RAG index.

## Non-goals

- Silent append every turn
- Vector memory

## Contract

**Input:** `{ "cli_commands": [] }`

**Output:** `{ "memory_cli": true, "cap_bytes": 32768 }`

## Commits

| # | Commit | Gate |
|---|--------|------|
| 22 | `feat(memory): dirs + CLI + cap` | over-cap summarises |

## Do not

- Write outside the two memory roots
- Treat memory as textbook corpus

## Return to graph

Commands, tests, failures.
