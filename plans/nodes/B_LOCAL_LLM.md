# Node plan — B_LOCAL_LLM — Local LLM adapter

> Parent: [EXECUTION_GRAPH.md](../../EXECUTION_GRAPH.md)

| Field | Value |
|-------|-------|
| **Node id** | `B_LOCAL_LLM` |
| **Job** | OpenAI-compatible local client for classifier + solve-explain on the CLI path |
| **Wave** | 6 |
| **Depends on** | B_CORE `solve_explain_port` |
| **Write paths** | `src/electrical_engineer/local_llm/**`, `tests/unit/test_local_llm.py` |
| **Read paths** | ARCHITECTURE model paths |
| **subagent_type** | generalPurpose |
| **Model** | `cursor-grok-4.6-high` |
| **Isolation** | `local_llm/` |

---

## Objective

CLI local-model path talks to a user-run OpenAI-compatible server (Ollama / LM Studio / vLLM). Used for the pre-runner classifier and `solve-explain` only. Hosts (Cursor/Claude/OpenAI) skip this and use their own loop. Missing daemon: clear skip, deterministic nodes still run. **No BYOK** in this graph. Do not pin a vendor model name as the product.

## Non-goals

- Cloud API keys
- Fine-tunes
- Image generation

## Contract

**Input:** `{ "solve_explain_port": true }`

**Output:** `{ "local_llm": true, "byok": false, "skip_if_missing": true }`

## Commits

| # | Commit | Gate |
|---|--------|------|
| 44 | `feat(llm): openai-compat local client` | skip-if-missing test |
| 45 | `feat(llm): classifier + solve-explain hook` | no call when unset |

## Do not

- Hard-require a daemon in CI
- Add Anthropic/OpenAI cloud keys

## Return to graph

`local_llm`, tests, failures.
