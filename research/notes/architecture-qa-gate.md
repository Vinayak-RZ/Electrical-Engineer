# Architecture Q&A gate (locks + working assumptions)

## Purpose

Record every post-research architecture question, the trade-off, and the answer used to write `docs/ARCHITECTURE.md` and `docs/WORKFLOWS.md`. Owner locks from the architecture questionnaire are **accepted**. Remaining items are **working assumptions** (same class as PRD P1): implementers use them; the owner may override at architecture review. This note is not a shipped CLI.

## Findings

Claim | Evidence | Confidence
--- | --- | ---
Owner already locked hybrid router, light DAG+FSM, DSH paradigm-only, photo stub, Cursor-like gates, per-run files, CLI + stateless MCP, extensive catalog | architecture questionnaire in the tech-architecture plan; `docs/PID.md` H3 | high
Language, runner library vs custom, compose strictness, catalog freeze, child-recipes, and resume policy were still open after Phase A research | `spatiotemporal-composability.md`; `light-dag-fsm-and-language.md`; `ee-workflow-catalog-draft.md` | high
Cloud/agent-patterns MCP was unreachable in this environment, so pattern IDs stay MCP-PENDING | `research/README.md` | high

### Owner locks (accepted — do not reopen without a new owner decision)

| Topic | Lock |
|-------|------|
| Router | Hybrid: named workflows for known intents; unmatched text uses a short co-solver path and must **label unchecked** numerics |
| Engine | Not LangGraph. Light DAG + FSM. Modular nodes. Predefined workflows **and** dynamic composition |
| Inspiration | DeepSeek Harness / Cordis spatiotemporal composability as **paradigm only**. Do not fork DSH (that would be H4/H5) |
| Photo | Stub contract in this architecture pass (C4 still P1). Text-solve + simulate specified in full |
| HITL | Cursor-like global + per-project gates; default **on**; at most **1–2** interrupts per workflow; allow-all globally or per-run |
| State | Per-run files on disk. No database. No Temporal cluster |
| Invoke | CLI-core `electrical-engineer run <workflow>` + optional **stateless stdio MCP** (`list_workflows`, `run_workflow`) |
| Catalog | Extensive, names a student can understand |
| Product | H3 thin CLI; one repo; co-solver; Apache-2.0; UG bound |

### Working assumptions (proposed — architecture review)

Each row: context, options, trade-off, **assumption used in the docs**.

#### A1 Language

**Context.** EE numerics are Python-first (ngspice/PySpice, python-control, RAG, MATLAB Engine). Fast CLIs in 2026 are often Rust.

**Option L1 — Python-only.** Same process for CLI, runner, nodes. Pros: one install; lab language in India; MATLAB/ngspice bindings exist. Cons: heavier RAM; slower CLI startup than a Rust binary.

**Option L2 — Rust CLI + Python workers.** Pros: single static CLI binary; easier sandbox per node. Cons: two languages; student must still have Python for spice/RAG; H3 surface grows.

**Option L3 — TypeScript CLI.** Pros: easy MCP. Cons: rhymes with DSH; extra Node toolchain.

**Assumption:** **L1 Python-only.** H3 is glue, not a coding-agent binary race. Revisit L2 only if CLI install/startup becomes the eval bottleneck.

**Override:** PRIORITY = SPEED (then L2) or SIMPLICITY (keep L1).

#### A2 Runner

**Context.** Owner wants DAG + FSM, not LangGraph, not a Temporal server.

**Option A — Custom in-process DAG + tiny FSM.** Toposort; states for running / waiting-human / failed / done. Pros: smallest; we own fail-closed. Cons: we maintain it.

**Option B — YAML recipes + tiny runner.** Pros: readable on disk. Cons: second schema to keep honest; JSON already needed for the run directory.

**Option C — Python functions as recipes.** Pros: natural branches. Cons: catalog is not browsable by non-dev students; evals harder to diff.

**Option D — Embed Treadle/Ordius/Tasked.** Pros: someone else’s DAG. Cons: second product; several assume SQLite (conflicts with files-only).

**Assumption:** **A with JSON recipes** (catalog + `runs/<id>/dag.json` share one shape). No YAML. Code is allowed **inside** a node, not as the published catalog format.

**Override:** PRIORITY = QUALITY of student-readable recipes (then add YAML as a sugar over the same JSON).

#### A3 Dynamic composition allowlist

**Context.** Unconstrained stitch becomes a unique agent graph (H5-shaped).

**Option loose — any registered node, any edge.** Pros: flexible. Cons: garbage types; hard to eval.

**Option typed — registered node ids + typed artifact ports; reject unknown edges before run.** Pros: fail closed. Cons: compose-from-parts cannot invent new node types.

**Assumption:** **Typed ports.** Invalid graphs fail closed. Stitch writes a one-shot DAG into the run directory; the same runner executes it.

#### A4 Child recipes

**Context.** Temporal: activities vs child workflows; “when in doubt, use an Activity.”

**Option child — a node may `run` another named recipe.** Pros: photo-then-sim reuse. Cons: nested lifecycles; closer to a unique loop.

**Option nodes-only — recipes compose nodes; nodes do not call recipes.** Pros: one execution model. Cons: shared tails are duplicated in catalog JSON (small).

**Assumption:** **Nodes-only** in this architecture. Shared tails are repeated in recipe JSON or extracted later as a node, not a child workflow.

#### A5 Catalog freeze

**Context.** Draft ids/titles in `ee-workflow-catalog-draft.md` are extensive.

**Option collapse explain-* into one `explain-ee-concept --pack`.** Pros: fewer recipes. Cons: less student-readable; less extensive.

**Option keep per-pack titles.** Pros: matches “names a student can understand.” Cons: more rows.

**Assumption:** **Keep per-pack explain-\*** and the draft ids/titles. `list-workflows` is CLI/MCP discovery, not a runnable recipe.

#### A6 v1 specify vs later implement

**Context.** P1 depth default is circuits then control. Architecture should still name the union.

**Assumption:** **Specify** every catalog row in `docs/WORKFLOWS.md`. Mark **implement-later** for packs beyond circuits-first (and for all **stub** rows). Specification is not a claim that the CLI exists.

#### A7 Gate policy files

**Context.** Cursor-like global + per-project; default on; allow-all globally or per-run.

**Assumption:**

- Global: `~/.config/electrical-engineer/gates.toml`
- Per-project: `.electrical-engineer/gates.toml` (project wins on the same key)
- Per-run: `electrical-engineer run … --allow-all`
- Default: gates **on**. Max **1–2** `ask-human` nodes per workflow. Photo stub uses one confirm. Simulate-as-checked does not require a second interrupt unless the recipe writes files outside the run directory.

#### A8 Unmatched intent

**Assumption:** Recipe `unmatched-cosolver`: optional `retrieve-passage` → `solve-explain` → `label-unchecked` if any numeric claim lacks a verifier artifact → `write-run-summary`. No `run-spice` unless the student (or router) selected a simulate workflow. Never present invented numbers as simulation.

#### A9 Photo stub

**Assumption:** `photo-to-circuit-netlist` is **contract-only**: detect → connect → OCR → draft netlist file → `ask-human` confirm. No schematic UI. No checked simulation from the stub. Vision output is a **draft**. C4 UI remains P1.

#### A10 Resume

**Assumption:** Crash resume **re-reads the run directory**. Nodes with a successful `nodes/<id>/out.json` are skipped. There is no database WAL. A dirty/failed node is retried. `--restart` (later CLI) would ignore existing outs.

#### A11 MCP surface

**Assumption:** Stateless stdio MCP exposes **only** `list_workflows` and `run_workflow` (owner lock). No session id. No resources. Hosts keep their loops.

#### A12 Context window

**Assumption:** Always inject a **skill index** (id + one-line). On an EE task, inject the matching `SKILL.md`. After each node, inject a short JSON summary plus **artifact paths**, not file bodies. Never dump SPICE traces, RAG index dumps, or full conversation logs into the model context.

## Open questions

None remaining for the architecture **draft**. Owner review may override A1–A12. PRD accept is still a separate checkpoint.

## Sources

- [PID](../../docs/PID.md) — retrieved 2026-09-10 — reliability: primary
- [PRD](../../docs/PRD.md) — retrieved 2026-09-10 — reliability: primary
- [spatiotemporal-composability.md](spatiotemporal-composability.md) — retrieved 2026-09-10 — reliability: primary
- [light-dag-fsm-and-language.md](light-dag-fsm-and-language.md) — retrieved 2026-09-10 — reliability: primary
- [ee-workflow-catalog-draft.md](ee-workflow-catalog-draft.md) — retrieved 2026-09-10 — reliability: primary
- [photo-to-schematic-to-simulink.md](photo-to-schematic-to-simulink.md) — retrieved 2026-09-10 — reliability: primary
- Owner architecture questionnaire (hybrid router, DAG+FSM, gates, CLI/MCP, files, catalog) — retrieved 2026-09-10 — reliability: primary

## Confidence

Overall confidence for this note: high on owner locks; medium on A1 (language) until the owner confirms L1 at architecture review.
