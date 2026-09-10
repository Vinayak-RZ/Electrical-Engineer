# Project overview

## Purpose

**Electrical-Engineer** is an Apache-2.0 workspace for a **UG electrical engineering co-solver**: a branded local CLI (`electrical-engineer`) plus a **persistent localhost UI**, also usable from Cursor, Claude Code, or OpenAI. Named workflows make retrieval, citations, and verified numbers better. It checks numbers with simulators when it can, and labels unverified numbers with the exact token **unchecked**. GATE is an eval instrument, not the bound. PG, civil, and mechanical are out of the public promise.

The project is also an experiment: how far current AI can go on **core engineering** (not only software), and where it still fails.

## System overview (today)

Greenfield / research-complete; **PID accepted**; **PRD draft**; **architecture Proposed**. There is no shipped agent. Authority:

- Identity: [`docs/PID.md`](docs/PID.md)
- Requirements: [`docs/PRD.md`](docs/PRD.md)
- Architecture (Proposed): [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)
- Workflows (Proposed): [`docs/WORKFLOWS.md`](docs/WORKFLOWS.md)
- UG bound: [`docs/curriculum-map.md`](docs/curriculum-map.md)
- Research history: [`research/`](research/)
- Success-bar capabilities: [`README.md`](README.md)
- Internals map: [`docs/EXTENSIVE.md`](docs/EXTENSIVE.md)

## High-level architecture (intended, not implemented)

```
Student
  ├─ electrical-engineer CLI  (H3: YAML DAG runner, policy, eval)
  ├─ persistent localhost UI  (127.0.0.1; shared understanding)
  └─ Cursor / Claude Code / OpenAI
           ↓
     EE skill packs + MCP (H1 layer)
           ↓
     models: host | BYOK | local
           ↓
     verifiers: OSS first-class; MATLAB if present
           ↓
     Explanation + evidence  |  or labelled unchecked
```

Named YAML recipes; router never invents a DAG. Diagram ingest (stub): vision → draft netlist → **UI confirm** → stop (sim later).

## Constraints

- Apache-2.0; forever OSS in this repo; no paid tier.
- No commercial textbook PDFs or third-party exam PDFs in git.
- No fabricated simulation numbers; unverified values use the exact token **unchecked**.
- Local-first; no product cloud; UI binds to `127.0.0.1`.
- Named YAML workflows; router never invents a DAG.
- UG coursework public promise; one repo; PG not advertised.
- Academic integrity is the institution’s policy; default mode is co-solver.

## Sources of truth

- Identity / requirements: `docs/PID.md`, `docs/PRD.md`
- Architecture / workflows (Proposed): `docs/ARCHITECTURE.md`, `docs/WORKFLOWS.md`
- Capabilities / vision: `README.md`
- Landscape research: `research/notes/ai-core-engineering-landscape.md`
- Historical build advice (not the harness lock): `research/synthesis/recommendation.md`
- ADRs: `DECISIONS.md` (ADR-0001 = H3)
- Live phase status: `PROGRESS.md`
