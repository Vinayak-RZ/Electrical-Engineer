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

## 7. Curriculum and capabilities

**Bound.** The public promise is the **union of representative UG EE / EEE programmes** (Indian institutes first, global institutes first-class). Source of truth: [`curriculum-map.md`](curriculum-map.md). A question is in-scope if it is normal coursework in that union (assignment, lab numerical, diagram, exam-style), not only if it appears on GATE.

**GATE is not the bound.** GATE EE section tags are an **eval overlay**: a convenient check that we can see capability. Do not drop a programme core because GATE weights it lightly. Do not skip a taught lab genre because GATE omitted it. Extra GATE trick items that programmes do not teach are optional eval spice, not the syllabus.

**Packs in the public promise** (see the map for institute citations): circuits, signals, electronics, machines, power (study-level), control, power electronics, measurements, UG EM/fields, maths for EE. Labs attached to those cores are in-scope as assignment/lab-report genre, not a separate product.

**Out of the bound:** civil, mechanical, manufacturing. **Out of the public promise:** PG-only courses. Expansion stays in this repo via packs + unpublished later profiles — never a second git repo.

### C1–C8 mapped to v1 vs later

IDs match `README.md`. Claimable bar: on a published UG task set, with tools on, match gold **or label unchecked**. Fluent wrong numbers presented as checked fail the product.

| ID | Capability | v1 (proposed P1) | Later (same repo) |
|----|------------|------------------|-------------------|
| C1 | Solve EE questions correctly | Gold match **or label unchecked** on enabled packs. Silent invention is a fail. | Remaining packs to union coverage |
| C2 | Explain, not only answer | Assumptions, laws, steps a viva can probe | Same, richer citation when RAG is in |
| C3 | Assignment genres | Solve, derive, design-to-spec, simulate (when a tool exists), review, explain, lab-style report — **text + tools** on first packs | Same genres on remaining packs |
| C4 | Circuit diagrams | **P1** — not required to ship the first CLI slice | Photo/screenshot → draft netlist → student-confirmed schematic → simulate |
| C5 | Control-system diagrams | After C4 | Block diagrams / figures with the same edit-then-simulate gate |
| C6 | Reliability contract | Tool evidence with numbers; **unchecked** when unverified; no fabricated simulation | Same |
| C7 | Student-first and open | Apache-2.0, local-first CLI, OSS verifiers first-class, MATLAB if present | Same |
| C8 | Limit-finding | **Not a student UX promise.** Public eval of evidence vs unvalidated-claim rate may live in-repo | Unpublished PG profile; no second fork |

**P1 depth default (not locked):** circuits first, then control. Other packs remain in the product bound; they are not “out of Electrical Engineer.”

---

## 8. Reliability, integrity, exam-item legal policy

### Reliability

- Tools own checked numbers (ngspice / Python stack; MATLAB if present).
- If a number did not come from a verifier, the output must say **unchecked**. Never present it as a simulation, lab result, or load-flow.
- Diagrams (when in a slice) are **drafts** until the student confirms topology.
- Low-confidence OCR/vision is flagged. Saying what was not checked is success.

### Integrity (v1)

- Default mode is **co-solver** (full working + answer). Not hint-first tutor.
- **No faculty / TA / LMS features in v1.** The institution owns cheating policy. The product shows work so a viva still means something.
- Do not ship a “hide the answer for the professor” mode.

### Exam-item legal policy

Exam-style items are **in-scope** for corpus and evals (GATE-style, midterm-style, assignment-style).

**Git will not commit third-party copyrighted exam PDFs or commercial textbooks.** Allowed: BYO files on the student’s machine; licence-clean reconstructions the project authors; public-domain or owner-licensed items.

This is a **legal** policy, not a pedagogy policy. Students may still *use* their own papers locally. Redistribution of scanned GATE/university papers in this repository is forbidden.

---

## 9. Non-functional requirements

| NFR | Requirement |
|-----|-------------|
| Local-first | Default path is on-device CLI + local files. No product cloud. No silent upload of PDFs, keys, or student work. |
| Licence | Apache License 2.0 for *our* code. Forever OSS in this repo; no paid tier. Textbooks never redistributed in git. |
| Single repo | One git repository. UG is the public profile. PG, if ever, is an unpublished `--profile`, not a fork. |
| Portable core | Skills + MCP must load in CLI and in Cursor / Claude Code / OpenAI. CLI must stay a thin wrapper (glue, ug policy, eval). |
| H3 falsifier | If the CLI grows a unique agent loop hosts cannot share, stop — that is H5. |
| India-first, globally competent | Copy, examples, and packs must not treat non-Indian UG EE as an afterthought. |
| Secrets | API keys via environment / host secret stores only. |

---

## 10. Open P1 defaults (proposed, not locked)

Owner may override at PRD review. Until then, implementers treat these as **working defaults**, not PID locks.

| Topic | Proposed default | Owner review |
|-------|------------------|--------------|
| MATLAB vs OSS | MATLAB if present; OSS (ngspice / Python) first-class otherwise | - [ ] Accept  - [ ] Override: ____ |
| RAG | Local vector store; BYO PDFs; no commercial books in git (aligns with ADR-0002) | - [ ] Accept  - [ ] Override: ____ |
| v1 slice | C1–C3, C6–C7 first; C4 diagrams P1; C5 after C4; C8 not a student UX promise | - [ ] Accept  - [ ] Override: ____ |
| First pack depth | Circuits first, then control | - [ ] Accept  - [ ] Override: ____ |

**PRD status:** Draft until the owner says “PRD accepted” (or lists edits). Identity (P0) is already accepted in [`PID.md`](PID.md).

---

## 11. Out of scope

Never this product (not “later in another repo”):

- **H4** Electric Pi hard-fork as the product.
- **H5** Greenfield unique agent harness.
- **Civil, mechanical, manufacturing** packs or identity.
- **Plant-floor / live PLC / protection actuation.**
- **Second git repo** (UG-freeze fork vs lab fork).
- **Faculty LMS**, tutor-default as the public mode, paid hosting in this repo.
- **Shipping copyrighted textbooks or third-party exam PDFs** in git.
- Replacing MATLAB, KiCad, or professional EDA.

PG is not a public promise. Optional unpublished profile may exist later in **this** repo only.

---

## Related artifacts

| Doc | Role |
|-----|------|
| [`PID.md`](PID.md) | Accepted identity |
| [`PID_DECISION_SHEET.md`](PID_DECISION_SHEET.md) | P0 answers; P1 proposed |
| [`curriculum-map.md`](curriculum-map.md) | UG bound |
| [`../DECISIONS.md`](../DECISIONS.md) | ADRs |
| [`ARCHITECTURE.md`](ARCHITECTURE.md) | Technical architecture (**Proposed**) |
| [`../research/synthesis/recommendation.md`](../research/synthesis/recommendation.md) | Historical O1 *advice*; product chose H3 |

---

## Owner review checkpoint

This PRD is **not accepted** until the owner says so. Confirm or override:

- [ ] Thesis, H3 CLI, Apache-2.0, forever OSS, India-first global UG
- [ ] GATE is eval only; bound = [`curriculum-map.md`](curriculum-map.md)
- [ ] Co-solver default; **unchecked** labels; no faculty v1
- [ ] Exam-style in-scope; **no** third-party copyrighted PDFs in git
- [ ] P1 defaults in §10 (MATLAB/OSS, RAG, C1–C7 slice, circuits-then-control)
- [ ] **PRD accepted** — or listed edits

Do not start an implementation nawab plan until this checkpoint is closed.
