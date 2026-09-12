# Domain-system recommendation (WS-G)

## Purpose

Advise the owner on product *class*, *name*, and *orchestrator split* after comparing OpenMontage-class systems with locked EE constraints. This memo is not a product requirements document. Historical harness advice remains [`recommendation.md`](recommendation.md) (O1 Pi package). This memo does not reopen H4/H5.

## Recommendation

**Class.** Electrical Engineer is a **harness-native domain system** — the same class as OpenMontage, not an MCP, CLI, plugin, skill pack, or harness.

**Vertical.** An undergraduate electrical-engineering **lab** that inhabits Claude Code, Codex, and Cursor, with a local CLI for students who do not use those hosts.

**Names (pair).**

- Product name: **Electrical Engineer** (keep PID Q1; do not rename the CLI or repo).
- Public category: **lab**.
- Internal class: harness-native domain system.
- Mode: **co-solver** (full working + answer + evidence, or the exact token `unchecked`).

Rejected: “Agentic UG EE Studio” (jargon, acronym soup, video metaphor).

**Architecture.** Topology **C (hybrid)**. The host coding agent plans, explains, and reviews. Python owns simulators, RAG, gates, eval, and the localhost workspace. Named YAML recipes stay **genre contracts** for attaching physics. The router still never invents a spice DAG. Unmatched never auto-simulates. Photo confirm is not SPICE. H3 falsifier unchanged: the CLI must not grow a unique loop hosts cannot share.

**Analog.** OpenMontage turns a coding assistant into a video production studio. Electrical Engineer turns a coding assistant into an undergraduate electrical-engineering lab. Physics is the difference: OpenMontage can put method in markdown; EE puts method in skills *and* numbers in code (ChemCrow / Karajan pattern).

**Marketing.** GitHub one-liner: Electrical Engineer is an Apache-2.0 lab for undergraduate electrical engineering. It sits on Claude Code, Codex, or Cursor, checks numbers with simulators when it can, and labels the rest `unchecked`. GTM: host clubs (Claude Builder Club exists at IIT Madras), divider eval as the demo, GATE remains an eval overlay.

## Why this path

- OpenMontage, anything2explainer, and Karajan prove the class: inhabit the frontier harness; supply pipelines, tools, QC, artifacts.
- Anthropic’s workflow vs agent split matches EE: simulation attachment is a workflow; explanation is an agent. Topology B (today’s public identity) fights the host. Topology A (markdown-only control plane) cannot own Kirchhoff.
- This repo already has the skeleton (YAML, nodes, MCP, UI, eval). The gap is identity plus host-teachable skills, not a new harness.
- Keeping Electrical Engineer avoids collisions (EEBench.org, CircuitLab, Fuse, NI Workbench) and rename cost.
- “Lab” is what UG students already call the place this product analogizes. “Bench” collides with atopile’s agent benchmark and with physical instrument benches (cannot-do).

## What this memo does not decide

- PID/PRD/ARCHITECTURE/README text. That is a later docs pass after the vision lock sheet.
- Skill-pack depth, JSON artifact schemas, or a tool-registry rewrite.
- Dropping the YAML runner, crash-resume, BYOK, HTTP MCP, or PyPI.
- PG, faculty, plant-floor, or a second git repo.

## Open questions

- Owner accept/reject on the lock sheet (name, lab, topology C).
- How much of a named recipe the host may narrate versus `electrical-engineer run <id>` executing the DAG (implementation detail after lock).

## Sources

- [`research/notes/domain-system-architecture-patterns.md`](../notes/domain-system-architecture-patterns.md) — retrieved 2026-09-12 — reliability: primary
- [`research/notes/similar-agentic-domain-systems.md`](../notes/similar-agentic-domain-systems.md) — retrieved 2026-09-12 — reliability: primary
- [`research/notes/naming-and-positioning.md`](../notes/naming-and-positioning.md) — retrieved 2026-09-12 — reliability: primary
- [`research/notes/student-gtm-ug-ee.md`](../notes/student-gtm-ug-ee.md) — retrieved 2026-09-12 — reliability: primary
- [`docs/PID.md`](../../docs/PID.md) — retrieved 2026-09-12 — reliability: primary
- [`research/synthesis/recommendation.md`](recommendation.md) — retrieved 2026-09-12 — reliability: primary (historical O1; not this decision)

## Confidence

Overall confidence for this memo: high

Class and hybrid split rest on primary READMEs plus this repo’s runner law. The name pair is a judgment with collision evidence; an owner who wants a coined brand can reject D14 without rejecting C.
