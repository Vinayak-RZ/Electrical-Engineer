# Product Identity Document (PID) — Electrical Engineer

**Status:** Accepted (P0 locks, 2026-09-09). P1 items remain **proposed** until PRD review.  
**Date:** 2026-09-09  
**Requirements authority after this:** [`PRD.md`](PRD.md)

This document is the locked product identity. Trade-off *history* lives in git; agents must not reopen H1–H5, licence, or UG vs PG without a new owner decision.

---

## 1. Thesis

Electrical Engineer is an Apache-2.0, forever-open-source **co-solver** for undergraduate electrical engineering: a branded **local CLI** that also plugs into Cursor, Claude Code, or OpenAI (or a local model / BYO key), checks numbers with simulators when it can and **labels** numbers it did not check, and is shaped by **real UG coursework** at Indian and global institutes. GATE is an eval instrument, not the product bound. PG, civil, and mechanical are out of the public promise.

## 2. Identity (locked)

| Field | Value |
|-------|--------|
| Public name | Electrical Engineer |
| GitHub repo | `Electrical-Engineer` |
| CLI (default) | `electrical-engineer` |
| Category | UG EE co-solver with simulators and host adapters |
| Geography | India first; must not be weak for global UG EE |
| Licence (our code) | Apache License 2.0 |
| Commercial | Forever OSS in this repo; no paid tier |
| Locality | Local-first CLI; optional Cursor / Claude Code / OpenAI; BYO API key; local models |
| Harness | **H3** — branded CLI wrapping portable skills + MCP + local RAG (H1 layer). Not a Pi fork (H4). Not a greenfield harness (H5). |
| Repo copies | **One repo only** |
| Default mode | Co-solver (full working + answer + evidence or unchecked label) |
| Unverified numbers | Allowed if **labelled unchecked**; never presented as simulation |
| Faculty / TA | None in v1 |
| PG | Not a public promise |
| Civil / mechanical / manufacturing | Never in this product |

**Is:** a student-facing, open, checkable UG electrical-engineering co-solver.  
**Is not:** Siemens Eigen, MATLAB Copilot, Cadence Cerebrus, a plant-floor controller, a faculty LMS, a GATE-only drill app, or a general coding agent with “also do circuits.”  
**Invariant:** tools own checked numbers; unchecked numbers are labelled; diagrams (when in scope) are drafts until the student confirms; no commercial textbooks in git.

## 3. Who it is for

**Primary:** UG electrical engineering students — India first, including colleges without a MATLAB-fluent TA — who have assignments, labs, and diagrams in circuits, machines, power, control, signals, and electronics. Global UG EE must remain first-class, not an afterthought.

**In v1 as users, not as extra products:** GATE/IES aspirants may use exam-style questions (eval + BYO). Self-learners taking UG-equivalent courses are welcome.

**Not in v1:** faculty/TA features, PG promise, working plant engineers, civil/mechanical students.

**Never:** control-room operators, live PLC writes, tape-out analog as the product identity.

## 4. Bound: UG coursework, not GATE

Public promise = **union of representative UG EE programmes** (Indian institutes + global institutes). See [`curriculum-map.md`](curriculum-map.md).

GATE EE is a **capability check / eval overlay**, not the ceiling and not the only syllabus.

Expansion stays cheap without a second repo: domain packs + unpublished later profiles. Do not put the UG limit inside SPICE or the RAG index.

```text
Host adapter     CLI / MCP / Cursor / Claude Code / OpenAI skills
Policy profile   ug-coursework (public) | later unpublished
Domain packs     circuits | control | power | machines | …
Tool adapters    MATLAB-if-present | ngspice | pandapower | …
Eval suites      pack × profile; GATE overlay on UG tasks
```

## 5. Success bar (C1–C8)

Same IDs as `README.md`. v1 vs later is in the PRD (P1 proposed: C1–C3 and C6–C7 first; C4 then C5; C8 not a student UX promise).

Claimable bar: on a published UG task set, with tools on, match gold **or label unchecked**. Fluent wrong numbers presented as checked fail the product.

## 6. H3 shape (locked)

```text
Student
  ├─ electrical-engineer CLI (branded, local, policy here)
  └─ Cursor / Claude Code / OpenAI (same skills + MCP)
           │
     skills + MCP (RAG, spice, matlab)
           │
     models: host subscription | BYO API key | local LLM
           │
     verifiers: OSS first-class; MATLAB if present
```

The CLI is a **thin wrapper** (glue, ug profile, co-solver defaults, eval runner). It must not grow into a unique agent loop (H5). Hosts keep their own loops; we supply skills, tools, and policy the CLI also applies.

## 7. Trust (locked)

| Topic | Stance |
|-------|--------|
| Unverified numbers | Label **unchecked**; never call them simulation |
| Diagrams | Draft until student confirms |
| Integrity | Co-solver default; institution owns cheating policy; no faculty mode in v1 |
| Student data | Local by default; no silent upload |
| Plant / PLC write | Out of product |
| Copyright | No commercial PDFs in git; BYO or licensed embedding packs |
| Exam items | Exam-style tasks in-scope; **no** third-party copyrighted PDFs committed; BYO allowed |

## 8. Non-goals

- H4 (Electric Pi fork) and H5 (greenfield harness)
- Second git repo / UG-freeze fork
- PG as a public promise
- Civil, mechanical, manufacturing
- Faculty LMS, paid product, plant-floor copilots
- Replacing MATLAB or KiCad
- Shipping copyrighted textbooks or live exam PDFs in git

## 9. P1 proposed (not locked — PRD review)

| Topic | Proposed |
|-------|----------|
| MATLAB vs OSS | MATLAB if present; OSS first-class otherwise |
| RAG | Local vector store; BYO PDFs; no commercial books in git |
| v1 slice | C1–C3, C6–C7 P0; C4 P1; C5 after C4 |
| First pack | Circuits first, then control |

## 10. Related artifacts

| Doc | Role |
|-----|------|
| [`PRD.md`](PRD.md) | Requirements |
| [`PID_DECISION_SHEET.md`](PID_DECISION_SHEET.md) | Answer trace |
| [`curriculum-map.md`](curriculum-map.md) | UG bound |
| [`../research/synthesis/recommendation.md`](../research/synthesis/recommendation.md) | Historical O1 *advice*; product chose H3 |
| [`../DECISIONS.md`](../DECISIONS.md) | ADRs |

## Sources

- Owner P0 answers (2026-09-09) — reliability: primary
- [`PID_DECISION_SHEET.md`](PID_DECISION_SHEET.md) — reliability: primary
- Research notes under `research/` — reliability: primary

## Confidence

Overall confidence that **P0 identity is locked:** high.
P1 defaults remain owner-reviewable.
