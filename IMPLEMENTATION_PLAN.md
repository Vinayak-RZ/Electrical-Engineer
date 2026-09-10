# IMPLEMENTATION_PLAN

## Current contract (2026-09-10) — Proposed technical architecture

**Do not start CLI, MCP, skills, UI, or eval-runner implementation until the owner accepts [`docs/PRD.md`](docs/PRD.md) and a new implementation nawab plan is approved.** Architecture docs are **Proposed** (owner review), not an implementation license.

| Field | Contract |
|-------|----------|
| Identity | [`docs/PID.md`](docs/PID.md) **Accepted** |
| Requirements | [`docs/PRD.md`](docs/PRD.md) draft for owner review |
| Architecture | [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) **Proposed** |
| Workflows | [`docs/WORKFLOWS.md`](docs/WORKFLOWS.md) **Proposed** |
| Q&A locks | [`research/notes/architecture-qa-gate.md`](research/notes/architecture-qa-gate.md) |
| ADR | 0007 **proposed** (orchestrator, gates, UI, eval) |
| Eval layout | [`eval/gold/`](eval/gold/README.md) specified; no gold items yet |
| Harness | **H3** — deterministic YAML DAG runner; hosts own the main LLM loop |

The previous identity+PRD contract follows and remains in force.

---

## Current contract (2026-09-09) — product identity + PRD

**Do not start CLI, MCP, skills, or eval gold-set implementation until the owner accepts [`docs/PRD.md`](docs/PRD.md) and a new implementation nawab plan is approved.**

| Field | Contract |
|-------|----------|
| Identity | [`docs/PID.md`](docs/PID.md) **Accepted** |
| Requirements | [`docs/PRD.md`](docs/PRD.md) draft for owner review (P1 proposed) |
| Harness | **H3** branded CLI wrapping portable H1 (skills + MCP + local RAG). Not H4, not H5. |
| Licence | Apache-2.0; forever OSS; no paid tier |
| Bound | UG programmes India + global ([`docs/curriculum-map.md`](docs/curriculum-map.md)); GATE = eval overlay only |
| Repo | One repository; PG not a public promise |
| Default mode | Co-solver; unverified numbers labelled **unchecked** |
| Faculty | None in v1 |
| ADRs | 0001, 0005, 0006 **accepted**; 0002–0004 still proposed (P1) |

The historical research-phase note follows. It is **not** the current product decision (research O1/H2 was advice; the owner chose H3).

---

# IMPLEMENTATION_PLAN — research phase (historical)

This repository’s completed execution contract for the **research-only** phase is the
approved nawab plan carried out on branch `cursor/ee-research-phase-7e0c`.

**Delivered artifacts live under:**

- [`research/`](research/) — notes, registers, synthesis
- [`PROGRESS.md`](PROGRESS.md) — phase status
- [`DECISIONS.md`](DECISIONS.md) — ADR seeds (`proposed`)
- [`PHASE_N_COMPLETION.md`](PHASE_N_COMPLETION.md) — hardening record
- [`README.md`](README.md) / [`docs/EXTENSIVE.md`](docs/EXTENSIVE.md) — compilations

**Also delivered (2026-09-08 landscape pass):**

- [`research/notes/ai-core-engineering-landscape.md`](research/notes/ai-core-engineering-landscape.md) — AI progress in EE, manufacturing, civil; education and reliability implications
- Root [`README.md`](README.md) — target capabilities C1–C8 as the published success bar
- ADR-0005 seed (later accepted as UG coursework bound + single repo; wording originally proposed a research fork)

**Also delivered (2026-09-09 PID draft, later accepted):**

- [`docs/PID.md`](docs/PID.md) — product identity (Accepted after P0 locks)
- [`docs/PID_DECISION_SHEET.md`](docs/PID_DECISION_SHEET.md) — owner questions (P0 answered; P1 proposed)

**Next (after this historical phase):** owner accepted PID; PRD is the remaining human gate. See the **Current contract** block at the top of this file.
Do not start product implementation until that PRD is accepted and a new plan is approved.
