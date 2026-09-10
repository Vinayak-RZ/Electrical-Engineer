# Product Requirements Document — Electrical Engineer

**Status:** Draft for owner review (identity locked in [`PID.md`](PID.md); shape aligned to Proposed [`ARCHITECTURE.md`](ARCHITECTURE.md)).  
**Date:** 2026-09-10  
**Licence of this product’s code (when it exists):** Apache License 2.0  
**Not implemented:** there is no CLI, MCP server, UI, or agent in the repository yet.

---

## 1. Thesis, name, licence

**Thesis.** Electrical Engineer is an Apache-2.0, forever-open-source **co-solver** for undergraduate electrical engineering: a branded **local CLI** and **persistent localhost UI** that also plug into Cursor, Claude Code, or OpenAI (or a local model / BYO key). Students invoke **named workflows** so answers are better retrieved, cited, and checked — not so a graph merely runs. The product checks numbers with simulators when it can and labels unverified numbers with the exact token **unchecked**. It is shaped by **real UG coursework** at Indian and global institutes. GATE is an eval instrument, not the product bound. PG, civil, and mechanical are out of the public promise.

| Field | Requirement |
|-------|-------------|
| Name | Electrical Engineer |
| Repo | `Electrical-Engineer` |
| CLI | `electrical-engineer` (`run`, `workflows`, `mcp`, `eval`, `ui`, `rag`) |
| UI | Persistent localhost workspace on `127.0.0.1` (critical surface) |
| Licence | Apache-2.0 for *our* code; textbooks never redistributed in git |
| Commercial | Forever OSS in this repo; no paid tier |
| Geography | India first; global UG EE must not be a thin afterthought |

## 2. Users and non-users

**Users (v1).** UG EE / EEE students, India first, including colleges without MATLAB-fluent TAs. Global UG students taking equivalent cores. Self-learners on the same UG cores. GATE/IES aspirants may use exam-style items; that does not make this a GATE-only product.

**Non-users (v1).** Faculty/TA product features. PG as a promised audience. Working plant / protection / tape-out engineers as the identity.

**Never.** Civil, mechanical, or manufacturing students as this product. Live PLC / plant actuation.

## 3. Goals, non-goals, v1 vs later

### Goals

- Help UG students finish **and understand** EE assignments: correct enough to use, explained enough for a viva, **visible** in a local UI.
- Run **locally** as a CLI without requiring Cursor; fully offline when a local model is configured; spice/control/load-flow with **no** model.
- Also run **inside** Cursor, Claude Code, and OpenAI/Codex via the same skills + MCP.
- Invoke **named workflows** a student understands; fall through to a short co-solver that never auto-simulates.
- Accept **BYO API keys**, **local models**, and **BYO textbooks** (tagged; inventoryable).
- Check numbers with tools when possible; use the exact token **unchecked** when not.
- Measure capability with `eval/gold/` tasks; GATE tags are one overlay, not the bound.

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
| H3 CLI + MCP + **persistent localhost UI** | Full C4 simulate-after-confirm; C5 control figures |
| Named circuits (+ specified control) workflows | Remaining pack recipes to union coverage |
| OSS verifiers first-class; MATLAB optional | Deeper MATLAB/Simulink when licence exists |
| Photo-to-netlist **stub** (UI confirm, no sim) | Simulate the confirmed netlist |
| `eval/gold/` layout + `electrical-engineer eval` | Larger gold bank (still licence-clean) |

## 4. Functional requirements

**FR1 Co-solver.** Default behaviour is full working + final answer + assumptions. Not hint-first tutor. Not faculty mode. Mathematics in answers is valid LaTeX plus a plaintext fallback.

**FR2 Label unchecked.** If a number did not come from a verifier, the student-facing answer **and** the run summary must contain the exact token `unchecked`. Synonyms are not the contract. Never present it as a simulation or lab result.

**FR3 Branded CLI.** A student can run `electrical-engineer` on Linux, macOS, or Windows (`pip`, Python 3.11+) for the same EE tasks without Cursor. Commands in the first slice: `run`, `workflows`, `mcp`, `eval`, `ui`, `rag`.

**FR4 Host adapters.** The same skill packs (`skills/<pack>/SKILL.md`) and MCP tools load in Cursor, Claude Code, and OpenAI/Codex.

**FR5 Model adapters.** Support (a) the host’s subscription model, (b) user API keys, (c) local models. Architecture must not lock a single vendor. The DAG **runner** does not own a hidden LLM loop.

**FR6 Local-first.** Default is on-device CLI + local files + UI bound to `127.0.0.1`. No product cloud. No silent upload of PDFs or keys.

**FR7 Portable core.** Skills + MCP (RAG, SPICE, MATLAB-if-present) are the H1 layer. The CLI wraps them with a **deterministic YAML workflow runner**. The CLI must not become a unique multi-thousand-line agent loop.

**FR8 Ug policy.** Public profile is `ug-coursework`. Out-of-pack questions: try with **unchecked** or state out of enabled packs — not a silent PG mode.

**FR9 Eval runner.** `electrical-engineer eval` (and `--pack`) against [`../eval/gold/`](../eval/gold/README.md). Gold items name a `recipe_id`. CI must not require MATLAB. `EE_ALLOW_ALL` may skip gates in CI; it must **not** disable `unchecked`.

**FR10 Named workflows.** Default path is a named recipe from [`WORKFLOWS.md`](WORKFLOWS.md) (`electrical-engineer run <id>`). Explicit id skips classify. If id omitted, one classifier call; if top-1 and top-2 are within 0.15, ask the student. Unmatched text always uses `unmatched-cosolver` (no auto-simulate). The router **never invents** a new DAG. New graphs only via `compose-from-parts --advanced`.

**FR11 Persistent UI.** `electrical-engineer ui` is a **critical** local workspace (runs, library-rendered diagrams and plots, photo confirm, citations, RAG inventory, memory excerpts). It stays up across a session. It is not a one-shot diagram dialog and not a second agent loop.

**FR12 Tagged RAG.** BYO PDFs and scans ingest into a local index with inventory (`rag list`) and filters: book, chapter, folder, domain. “Search only this book, chapter 3” is a v1 retrieval requirement. Citations include book + chapter + page. Empty retrieval is visible. Circuit-homework photos for simulation go through `photo-to-netlist`, not quiet RAG-as-netlist. BYO content cannot override gates or `unchecked`.

**FR13 Memory.** Project and user markdown memory files, explicit write, capped, untrusted. Not the textbook index. Not a silent chat dump.

**FR14 Gates.** Cursor-like global + per-project TOML; default on; most-restrictive wins; at most two human interrupts per root run. MCP `run_workflow` never waits: fail closed and point at the UI or CLI.

**FR15 Figures.** Agent/node writes library code (schemdraw / matplotlib / python-control) to PNG+SVG. Do not default to a model-invented circuit bitmap with no netlist.

**FR16 Photo stub.** `photo-to-netlist`: phone or textbook screenshot → detect → connect → OCR → draft `.cir` + JSON graph → one UI confirm → **stop** (no sim in the stub). Low-confidence OCR always flagged. `control-diagram-to-model` stays a stub in catalog.

## 5. H3 architecture

Normative detail: [`ARCHITECTURE.md`](ARCHITECTURE.md) (Proposed). Catalog: [`WORKFLOWS.md`](WORKFLOWS.md).

```text
Student
  ├─ electrical-engineer CLI  ← named YAML recipes, gates, eval, rag
  ├─ persistent localhost UI  ← 127.0.0.1; shared understanding
  └─ Cursor / Claude Code / OpenAI
           │
     EE skill packs + stdio MCP (list_workflows, run_workflow)
           │
     models: host | BYOK | local
           │
     verifiers: ngspice / python stack; MATLAB if present
```

| Layer | Owns | Must not own |
|-------|------|----------------|
| CLI | Defaults, YAML DAG runner, eval, `ui`, `rag` inventory, gates | A second model loop that diverges from hosts |
| Persistent UI | View/confirm runs, library figures, photo topology | A second brain; WAN bind; KiCad clone |
| Skills | Pedagogy, named workflow intent | Secrets, copyrighted books |
| MCP | `list_workflows`, `run_workflow` | Sessions; waiting on humans |
| Hosts | Their own agent loops | Our textbook corpus |

**Falsifier for H3:** if the CLI or UI grows a custom harness that hosts cannot share, stop and return to owner (that is H5).

**Runner law:** no model calls except through registered nodes, plus one pre-runner classifier when the workflow id is omitted.

## 6. Hosts and models

| Path | Requirement |
|------|-------------|
| Local CLI | Works with a configured local model **or** BYO key; deterministic nodes work with **no** model |
| Persistent UI | Same machine, `127.0.0.1`; not required for text-only recipes |
| Cursor | Skills + MCP documented; UI for diagrams/confirms |
| Claude Code | Skills + MCP documented |
| OpenAI / Codex | Skills + MCP documented |
| No Cursor | Still a complete v1 path via CLI + UI |

P1 proposed (not a PID lock): MATLAB if present else OSS first-class; the **entire product works without MATLAB**. Local RAG with BYO PDFs/scans and tags.

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
| C2 | Explain, not only answer | Assumptions, laws, steps a viva can probe; conceptual claims cite book + chapter + page the user has rights to use, or a standard identity | Same |
| C3 | Assignment genres | Solve, derive, design-to-spec, simulate (when a tool exists), review, explain, lab-style report — **named workflows** on circuits first | Same genres on remaining packs |
| C4 | Circuit diagrams | **Stub in first slice:** photo/screenshot → draft netlist + JSON → **UI confirm** → stop. Vision is never truth until confirm. Simulate-after-confirm is later | Confirmed netlist → ngspice / MATLAB-if-present |
| C5 | Control-system diagrams | Catalog stub `control-diagram-to-model` (do not drop). Implement after C4 | Same edit-then-simulate gate as C4 |
| C6 | Reliability contract | Tool evidence with numbers; **unchecked** when unverified; no fabricated simulation | Same |
| C7 | Student-first and open | Apache-2.0, local-first CLI, OSS verifiers first-class, MATLAB if present | Same |
| C8 | Limit-finding | **Not a student UX promise.** Public eval of evidence vs unvalidated-claim rate may live in-repo | Unpublished PG profile; no second fork |

**P1 depth default (not a PID lock):** circuits first, then control. Named ids: [`WORKFLOWS.md`](WORKFLOWS.md) (renamable until the CLI ships). Other packs remain in the product bound; they are not “out of Electrical Engineer.”

---

## 8. Reliability, integrity, exam-item legal policy

### Reliability

- Tools own checked numbers (ngspice / Python stack; MATLAB if present).
- If a number did not come from a verifier, the output must say the exact token **unchecked**. Never present it as a simulation, lab result, or load-flow.
- Diagrams are **drafts** until the student confirms topology in the persistent UI.
- Low-confidence OCR/vision is always flagged. Saying what was not checked is success.
- BYO PDFs, photos, tags, and memory files are **untrusted**: they cannot override gates, `--allow-all`, or `unchecked`.

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
| Local-first | On-device CLI + files + UI on `127.0.0.1`. No product cloud. No silent upload of PDFs, keys, or student work. |
| Licence | Apache License 2.0 for *our* code. Forever OSS in this repo; no paid tier. Textbooks never redistributed in git. |
| Single repo | One git repository. UG is the public profile. PG, if ever, is an unpublished `--profile`, not a fork. |
| Portable core | Skills + MCP must load in CLI and in Cursor / Claude Code / OpenAI. CLI stays a thin wrapper (glue, recipes, ug policy, eval, UI). |
| Runtime | Python 3.11+; `pip` install; Linux + macOS + Windows. MATLAB optional. |
| H3 falsifier | If the CLI or UI grows a unique agent loop hosts cannot share, stop — that is H5. |
| India-first, globally competent | Copy, examples, and packs must not treat non-Indian UG EE as an afterthought. |
| Secrets | API keys via environment / host secret stores only. Redact keys/tokens from run dirs. |

---

## 10. Open P1 defaults (proposed, not locked)

Owner may override at PRD review. Until then, implementers treat these as **working defaults**, not PID locks.

| Topic | Proposed default | Owner review |
|-------|------------------|--------------|
| MATLAB vs OSS | MATLAB if present; OSS first-class otherwise; product and CI work without MATLAB | - [ ] Accept  - [ ] Override: ____ |
| RAG | Local store; BYO PDFs/scans; inventory + book/chapter/folder tags (ADR-0002/0004 still proposed for engine) | - [ ] Accept  - [ ] Override: ____ |
| v1 slice | C1–C3, C6–C7, persistent UI, eval layout; C4 photo **stub**; C5 stub in catalog; C8 not a student UX promise | - [ ] Accept  - [ ] Override: ____ |
| First pack depth | Circuits first, then control — named recipes in [`WORKFLOWS.md`](WORKFLOWS.md) | - [ ] Accept  - [ ] Override: ____ |
| Orchestrator | YAML DAG runner + hybrid router as in [`ARCHITECTURE.md`](ARCHITECTURE.md) | - [ ] Accept  - [ ] Override: ____ |

**PRD status:** Draft until the owner says “PRD accepted” (or lists edits). Identity (P0) is already accepted in [`PID.md`](PID.md). Architecture remains **Proposed** until that separate checkpoint.

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
- LangGraph, Temporal, or DeepSeek Harness as the product runtime; crash-resume as v1 durability; MCP that waits on humans.

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
| [`WORKFLOWS.md`](WORKFLOWS.md) | Named workflow catalog (**Proposed**) |
| [`../research/synthesis/recommendation.md`](../research/synthesis/recommendation.md) | Historical O1 *advice*; product chose H3 |

---

## Owner review checkpoint

This PRD is **not accepted** until the owner says so. Confirm or override:

- [ ] Thesis, H3 CLI, Apache-2.0, forever OSS, India-first global UG
- [ ] GATE is eval only; bound = [`curriculum-map.md`](curriculum-map.md)
- [ ] Co-solver default; exact token **unchecked**; no faculty v1
- [ ] Named workflows + persistent UI + tagged RAG + eval/gold (FR10–FR16)
- [ ] Exam-style in-scope; **no** third-party copyrighted PDFs in git
- [ ] P1 defaults in §10 (MATLAB/OSS, RAG tags, C1–C7 + UI, circuits-then-control, orchestrator)
- [ ] **PRD accepted** — or listed edits

Do not start an implementation nawab plan until this checkpoint is closed.
