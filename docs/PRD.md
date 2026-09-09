# Product Requirements Document — Electrical Engineer

**Status:** Draft for owner review (identity locked in [`PID.md`](PID.md); P1 items proposed).  
**Date:** 2026-09-09  
**Licence of this product’s code (when it exists):** Apache License 2.0  
**Not implemented:** there is no CLI, MCP server, or agent in the repository yet.

---

## 1. Thesis, name, licence

**Thesis.** Electrical Engineer is an Apache-2.0, forever-open-source **co-solver** for undergraduate electrical engineering: a branded **local CLI** that also plugs into Cursor, Claude Code, or OpenAI (or a local model / BYO key), checks numbers with simulators when it can and **labels** numbers it did not check, and is shaped by **real UG coursework** at Indian and global institutes. GATE is an eval instrument, not the product bound. PG, civil, and mechanical are out of the public promise.

| Field | Requirement |
|-------|-------------|
| Name | Electrical Engineer |
| Repo | `Electrical-Engineer` |
| CLI | `electrical-engineer` |
| Licence | Apache-2.0 for *our* code; textbooks never redistributed in git |
| Commercial | Forever OSS in this repo; no paid tier |
| Geography | India first; global UG EE must not be a thin afterthought |

## 2. Users and non-users

**Users (v1).** UG EE / EEE students, India first, including colleges without MATLAB-fluent TAs. Global UG students taking equivalent cores. Self-learners on the same UG cores. GATE/IES aspirants may use exam-style items; that does not make this a GATE-only product.

**Non-users (v1).** Faculty/TA product features. PG as a promised audience. Working plant / protection / tape-out engineers as the identity.

**Never.** Civil, mechanical, or manufacturing students as this product. Live PLC / plant actuation.

## 3. Goals, non-goals, v1 vs later

### Goals

- Help UG students finish **and understand** EE assignments: correct enough to use, explained enough for a viva.
- Run **locally** as a CLI without requiring Cursor.
- Also run **inside** Cursor, Claude Code, and OpenAI/Codex via the same skills + MCP.
- Accept **BYO API keys** and **local models**.
- Check numbers with tools when possible; **label unchecked** when not.
- Measure capability with evals; GATE tags are one overlay, not the bound.

### Non-goals

- Electric Pi (H4) or a from-scratch agent harness (H5).
- Second git repo.
- PG public promise.
- Faculty LMS, tutor-default, paid hosting.
- Civil / mechanical / manufacturing packs.
- Shipping copyrighted textbooks or third-party exam PDFs in git.
- Replacing MATLAB, KiCad, or professional EDA.

### v1 vs later

| Now (public promise) | Later (same repo, unpublished until promised) |
|----------------------|-----------------------------------------------|
| UG coursework co-solver | Optional `--profile` for PG; not advertised |
| H3 CLI + host adapters | Schematic UI when C4 is pulled into a slice |
| OSS verifiers first-class | Deeper MATLAB/Simulink when licence exists |
| Circuits-then-control depth (P1 default) | Remaining packs to union coverage |

## 4. Functional requirements

**FR1 Co-solver.** Default behaviour is full working + final answer + assumptions. Not hint-first tutor. Not faculty mode.

**FR2 Label unchecked.** If a number did not come from a verifier, the output must say **unchecked** (or equivalent). Never present it as a simulation or lab result.

**FR3 Branded CLI.** A student can run `electrical-engineer` on their machine for the same EE tasks without Cursor.

**FR4 Host adapters.** The same skill packs and MCP tools load in Cursor, Claude Code, and OpenAI/Codex.

**FR5 Model adapters.** Support (a) the host’s subscription model, (b) user API keys, (c) local models. Architecture must not lock a single vendor.

**FR6 Local-first.** Default is on-device CLI + local files. No product cloud. No silent upload of PDFs or keys.

**FR7 Portable core.** Skills + MCP (RAG, SPICE, MATLAB-if-present) are the H1 layer. The CLI wraps them. The CLI must not become a unique multi-thousand-line agent loop.

**FR8 Ug policy.** Public profile is `ug-coursework`. Out-of-pack questions: try with **unchecked** label or state out of enabled packs — not a silent PG mode.

**FR9 Eval runner.** A way to run gold tasks against the CLI (needed or C1/C6 are slogans).

## 5. H3 architecture

```text
Student
  ├─ electrical-engineer CLI  ← policy, glue, eval
  └─ Cursor / Claude Code / OpenAI
           │
     EE skill packs + MCP servers
           │
     models: host | BYOK | local
           │
     verifiers: ngspice / python stack; MATLAB if present
```

| Layer | Owns | Must not own |
|-------|------|----------------|
| CLI | Defaults (co-solver, ug, unchecked labels), install, eval | A second model loop that diverges from hosts |
| Skills | Pedagogy, workflows | Secrets, copyrighted books |
| MCP | RAG, simulators | The product identity |
| Hosts | Their own agent loops | Our textbook corpus |

**Falsifier for H3:** if the CLI grows a custom harness that hosts cannot share, stop and return to owner (that is H5).

## 6. Hosts and models

| Path | Requirement |
|------|-------------|
| Local CLI | Works with a configured local model **or** BYO key |
| Cursor | Skills + MCP documented |
| Claude Code | Skills + MCP documented |
| OpenAI / Codex | Skills + MCP documented |
| No Cursor | Still a complete v1 path via CLI |

P1 proposed (not locked): MATLAB if present else OSS first-class; local RAG with BYO PDFs.

---

*Curriculum, C1–C8 mapping, reliability, NFRs, and P1 checkboxes follow in the next PRD revision in this plan.*
