# Electrical Engineer

> Full internals (every package, file map, how the repo runs): [Extensive README](docs/EXTENSIVE.md)

**Electrical Engineer** is an Apache-2.0 **undergraduate EE co-solver**. It runs named YAML workflows so a student (or a host agent) can retrieve, check, and explain coursework with simulators when they exist, and with the exact token **unchecked** when they do not.

> **Electrical Engineer is a local CLI + persistent localhost UI you can run today.** It is not Electric Pi, not a Cordis/DSH agent loop, and not a PyPI release or BYOK cloud.
> Primary interface: `electrical-engineer`.
> Invariant: **unverified numbers use the exact token `unchecked`** — never a silent fake SPICE pass.

```text
$ uv run electrical-engineer --help
usage: electrical-engineer [-h] [--version]
                           {run,workflows,mcp,eval,ui,rag,memory} ...
```

```text
$ uv run electrical-engineer eval --pack circuits
PASS divider-dc-01 recipe=solve-circuit-problem
1/1 passed
```

Trials: [`docs/planning/T1_TRIALS.md`](docs/planning/T1_TRIALS.md). Boot log: [`docs/planning/R1_BOOT.md`](docs/planning/R1_BOOT.md). Honest holes: [`docs/CANNOT_DO.md`](docs/CANNOT_DO.md).

## Why it exists

Undergraduate electrical engineering is mostly circuits, signals, machines, power, and control — not chatbot fluency. This repo is the H3 harness from [`docs/PID.md`](docs/PID.md): a branded CLI wrapping portable skills and stdio MCP, with a FastAPI + React workspace bound to **127.0.0.1**. Hosts (Cursor, Claude Code, OpenAI) own the LLM loop; the CLI can also talk to a local OpenAI-compatible daemon when `EE_LOCAL_LLM_URL` is set.

## Core techniques

- **Named YAML DAGs.** Recipes under `workflows/` run in-process (`repair_max`, 16-node cap). Limit: the router never invents a graph; unmatched work uses `unmatched-cosolver` and stays unchecked.
- **Label-unchecked.** If ngspice, python-control, or pandapower is missing, the run fails closed with token `unchecked`. Limit: a checked number requires a tool or a numeric check, not a fluent paragraph.
- **Localhost slot UI.** FastAPI on `127.0.0.1:8765`, Vite React slots, DESIGN-coinbase tokens (Inter + JetBrains Mono — **not** Coinbase fonts or wordmark). Limit: no WAN bind, no agent loop in the browser, library SVG/PNG only.
- **stdio MCP.** `list_workflows` / `run_workflow`. Photo, compose, and control-diagram ids fail closed with a `ui_url`. Limit: MCP never waits on a human.
- **Thin RAG facade.** Book/chapter/folder/domain filters; empty retrieval is visible. Spike picked **bm25** until LightRAG 1.5 has numbers on a licensed chapter. Limit: no commercial PDFs in git.

## Visual system

White canvas, scarce `#0052ff` pill CTAs, `unchecked` as a badge-pill. Tokens live in `ui/src/tokens.css` from [`docs/design/DESIGN-coinbase.md`](docs/design/DESIGN-coinbase.md). We do not ship Coinbase Display/Sans/Mono/Icons.

## Get started

```text
uv sync --extra dev
uv run electrical-engineer workflows
uv run electrical-engineer run solve-circuit-problem
EE_NO_BROWSER=1 uv run electrical-engineer ui
uv run electrical-engineer mcp
uv run electrical-engineer eval --pack circuits
./scripts/validate.sh
```

Put a `problem.json` in the working directory for numeric tasks (see `eval/gold/circuits/divider-dc-01/fixtures/problem.json`).

Host adapters: [`docs/hosts/README.md`](docs/hosts/README.md).

## What it achieves (honest)

Reproduced on this tree (T1): divider `Vout=5.0` checked; unmatched and injection stay `unchecked`; MCP photo does not hang; UI binds loopback; control artifacts exist but say `python-control missing` when the library is absent. MATLAB is optional and not in CI.

## License

Apache-2.0. See [`LICENSE`](LICENSE).
