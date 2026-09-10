# Node plan — B_CORE — Runner + CLI

> Parent: [EXECUTION_GRAPH.md](../../EXECUTION_GRAPH.md)

| Field | Value |
|-------|-------|
| **Node id** | `B_CORE` |
| **Job** | Deterministic YAML DAG FSM, gates, run dirs, hybrid router, CLI surface |
| **Wave** | 2 |
| **Depends on** | B_PKG `pkg` |
| **Write paths** | `src/electrical_engineer/cli/**`, `runner/**`, `gates/**`, `router/**`, `runs` gitignore already, `tests/unit/test_runner*.py`, `tests/unit/test_gates*.py`, `tests/unit/test_unchecked*.py` |
| **Read paths** | `docs/ARCHITECTURE.md` §§4–8, 13 |
| **subagent_type** | generalPurpose |
| **Model** | `cursor-grok-4.6-high` |
| **Isolation** | sole writer of runner/cli/gates/router |

---

## Objective

In-process YAML runner: ready nodes concurrent, start order sorted id, 16-node parent cap on compose later, timeouts 2min/10min ceiling, no crash-resume, run id `{suffix}-{utc}`. Gates TOML most-restrictive, max 2 interrupts, `EE_ALLOW_ALL` does not disable `unchecked`. Router: explicit id skips classify; else one classifier call; 0.15 ask; else unmatched. CLI commands exist (may stub ui/rag/eval/memory until later nodes). Runner makes **no** model calls except through registered nodes + pre-runner classifier.

## Non-goals

- Implementing spice/RAG/UI bodies
- LangGraph
- Hidden agent loop (H5)

## Contract

**Input:** `{ "pkg": true }`

**Output:** `{ "run_json_schema": { "summary_fields": ["recipe_id","unchecked","paths"] }, "cli_commands": ["run","workflows","mcp","eval","ui","rag","memory"] }`

## Commits

| # | Commit | Gate |
|---|--------|------|
| 9 | `feat(runner): YAML DAG FSM` | unit FSM |
| 10 | `feat(gates): toml most-restrictive` | interrupt-3 aborts |
| 11 | `feat(runs): id + isolation dirs` | path test |
| 12 | `feat(router): hybrid classify + unmatched` | 0.15 test |
| 13 | `feat(cli): command surface` | `--help` |
| 14 | `test: unchecked exact token` | synonym fails |

## Do not

- Call an LLM inside the FSM
- Bind a web server here (B_UI)

## Return to graph

`run_json_schema`, tests run, failures.
