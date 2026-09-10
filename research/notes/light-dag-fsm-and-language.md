# Light DAG/FSM runners and language options

## Purpose

Compare light DAG + FSM execution (no LangGraph, no Temporal cluster) and languages that fit a local EE CLI whose heavy work is SPICE, control, RAG, and MATLAB-if-present.

## Findings

Claim | Evidence (URL) | Confidence
--- | --- | ---
Owner lock: not LangGraph; light DAG + FSM; modular nodes; files as run state | this plan’s owner answers | high
Static DAGs fit **known pipelines** (photo stub → netlist → gate → sim). Graphs struggle when the next step is data-dependent (tool list from an LLM, saga-style undo) | https://temporal.io/blog/the-fallacy-of-the-graph-why-your-next-workflow-should-be-code-not-a-diagram | high
Fateev’s “use code, not a diagram” is about **dynamic agents + durable cloud**. Electrical Engineer’s **named homework recipes** are closer to the exception he allows: static graphs for simple pipelines | same essay | high
A **tiny in-process runner** (topological sort + a few FSM states: running, waiting-for-human, failed, done) matches local-first file durability better than Treadle/Ordius/Tasked as a second product | https://github.com/billosys/treadle ; https://github.com/Wintersta7e/ordius ; https://tasked.dev/ | med
Python owns the EE numeric ecosystem (PySpice/ngspice, python-control, sympy, pandapower, RAG stacks) | `research/notes/open-source-verification.md` | high
Rust shows up in fast single-binary coding CLIs (Codex-class). Agent-loop latency is usually **model prefill**, not the orchestrator, unless the runner does heavy CPU | https://github.com/AnnenkovLabs/jig survey claims; https://sanketdaru.com/blog/python-vs-rust-ai-agents/ | med
TypeScript is DSH’s home language. Using it for *our* loop would rhyme with forking a coding harness | https://deepseek.com/harness/en/ | high
Go is a fine CLI language and a poor home for PySpice/RAG without cgo/subprocesses | ecosystem knowledge | med

### Engine options (all in-process; no extra server)

| Option | What it is | Fits EE recipes | Fits dynamic stitch | Cost |
|--------|------------|-----------------|---------------------|------|
| A. Custom DAG + FSM | Toposort nodes; states for gate/retry | Yes | Stitch = emit a DAG JSON into the run dir | Smallest; we own it |
| B. YAML recipes + tiny runner | Checked-in YAML; same runner | Yes, readable | Same as A | Extra YAML schema to keep honest |
| C. Code recipes | Python functions calling allowlisted nodes | Excellent for branches | Natural `if` / loops | Harder for non-dev catalog browsing |
| D. Embed Treadle/Ordius/Tasked | Rust libraries / binaries | Possible | Product-shaped | Second product; SQLite (owner said files, not DB) |
| E. LangGraph / Temporal | Rejected / cluster | Overkill | Yes | H5-shaped or not local-first |

**Working bias to ask, not freeze:** A or A+B. Use a **small FSM** only for gates (wait / allow / deny), not a second workflow language. Dynamic composition writes a DAG into `runs/<id>/dag.json` and the same runner executes it. Code (C) remains valid *inside* a node.

Owner also asked for DAG-like architecture **and** dynamic composition. That pair is: **DAG as the *executed* object**, **code or a stitcher as the *author***. Do not require students to draw graphs. Do not require a cloud durable engine to get files-on-disk resume (re-run remaining nodes by reading the run dir).

### Language options

| Option | CLI / runner | Nodes (spice, RAG, control) | Trade-off |
|--------|----------------|------------------------------|-----------|
| L1 Python-only | Click/typer CLI | Same process | Fastest to ship H3; one install; heavier RAM |
| L2 Rust CLI + Python workers | clap binary; exec Python per node or long-lived worker | Python | Fast CLI, sandboxable workers; two languages |
| L3 TypeScript CLI | node | Python subprocess | Easy MCP; DSH-shaped; Node on student machines |
| L4 Go CLI + Python | similar to L2 | Python | Fewer EE examples than Rust/Python |

MATLAB Engine and ngspice bindings are **Python-first**. A Rust-only EE core would reimplement that poorly. L1 vs L2 is the real choice. L3 is the one most likely to grow into H5.

Student machines in India: Python is already the lab language. A second Rust toolchain is a real install cost unless we ship a single binary that **bundles** or **calls** a venv.

## Open questions

- Custom runner vs YAML-on-disk recipes vs Python function recipes (or mix)?
- L1 Python-only vs L2 Rust CLI + Python nodes?
- Resume-after-crash: re-read run directory node outputs, or always restart the recipe?

## Sources

- [The fallacy of the graph (Temporal blog)](https://temporal.io/blog/the-fallacy-of-the-graph-why-your-next-workflow-should-be-code-not-a-diagram) — retrieved 2026-09-10 — reliability: vendor
- [Treadle](https://github.com/billosys/treadle) — retrieved 2026-09-10 — reliability: primary
- [Ordius](https://github.com/Wintersta7e/ordius) — retrieved 2026-09-10 — reliability: primary
- [Tasked](https://tasked.dev/) — retrieved 2026-09-10 — reliability: vendor
- [Python vs Rust for AI agents](https://sanketdaru.com/blog/python-vs-rust-ai-agents/) — retrieved 2026-09-10 — reliability: secondary
- [open-source-verification.md](open-source-verification.md) — retrieved 2026-09-10 — reliability: primary
- [DeepSeek Harness](https://deepseek.com/harness/en/) — retrieved 2026-09-10 — reliability: vendor

## Confidence

Overall confidence for this note: high on “do not adopt LangGraph/Temporal/DSH”; medium on L1 vs L2 until install/eval friction is weighed by the owner.
