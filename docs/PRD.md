# Product Requirements Document — Electrical Engineer

**Status:** Proposed (2026-09-12). Supersedes Accepted D0 (2026-09-10) pending owner review.  
**Date:** 2026-09-12  
**Licence of this product’s code:** Apache License 2.0  
**Identity:** [`PID.md`](PID.md) (still Accepted until the PID commit of this pass).  
**This pass does not implement MCP/skill code.** As-built vs target is explicit in §4.

---

## 1. Thesis, name, licence

**Thesis.** Electrical Engineer is an Apache-2.0, forever-open-source undergraduate electrical-engineering **lab**: a **domain kernel** that wraps a rented frontier agent loop (Cursor, Claude Code, Codex, ChatGPT desktop) so the student gets a checked assignment — method, numbers, viva — without us becoming a new harness. A branded **local CLI** and **persistent localhost UI** are a complete path with no AI host. Named YAML recipes attach physics; they are not the chat brain. The product checks numbers with simulators when it can and labels unverified numbers with the exact token **unchecked**. It is shaped by **real UG coursework** at Indian and global institutes. GATE is an eval instrument, not the product bound. PG, civil, and mechanical are out of the public promise.

| Field | Requirement |
|-------|-------------|
| Name | Electrical Engineer |
| Repo | `Electrical-Engineer` |
| CLI | `electrical-engineer` (`run`, `workflows`, `mcp`, `eval`, `ui`, `rag`, `memory`) |
| UI | Persistent localhost workspace on `127.0.0.1` (critical surface) |
| Public category | **lab** (undergraduate electrical-engineering lab) |
| Internal class | **domain kernel** (host owns the loop; we own engines, skills, gates) |
| Mode | Co-solver (full working + answer + evidence, or exact token `unchecked`) |
| Licence | Apache-2.0 for *our* code; textbooks never redistributed in git |
| Commercial | Forever OSS in this repo; no paid tier |
| Geography | India first; global UG EE must not be a thin afterthought |

Rejected public nickname: “Agentic UG EE Studio”. “Bench” is not the public noun (EEBench.org; physical instrument benches).

## 2. Users and non-users

**Users (v1).** UG EE / EEE students, India first, including colleges without MATLAB-fluent TAs. Global UG students taking equivalent cores. Self-learners on the same UG cores. GATE/IES aspirants may use exam-style items; that does not make this a GATE-only product.

**Non-users (v1).** Faculty/TA product features. PG as a promised audience. Working plant / protection / tape-out engineers as the identity.

**Never.** Civil, mechanical, or manufacturing students as this product. Live PLC / plant actuation.

## 3. Goals, non-goals, v1 vs later

### Goals

- Help UG students finish **and understand** EE assignments: correct enough to use, explained enough for a viva, **visible** in a local UI.
- Run **locally** as a CLI without requiring any AI host; fully offline when a local model is configured; spice/control/load-flow with **no** model.
- Also run **inside** Cursor, Claude Code, Codex, and **ChatGPT desktop** under the same kernel contract (skills + MCP + CLI). ChatGPT **web** is not a host.
- Spend the host on method, viva, and missing-data interview. Clamp numbers, invented spice DAGs, and photo confirm in the kernel.
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
- ChatGPT web, Claude Desktop, GitHub Copilot, Gemini CLI as v1 hosts.
- Claiming ChatGPT Chat has Cursor-class repo editing.

### v1 vs later

| Now (public promise) | Later (same repo, unpublished until promised) |
|----------------------|-----------------------------------------------|
| UG coursework **lab** (domain kernel) | Optional `--profile` for PG; not advertised |
| H3 CLI + MCP + **persistent localhost UI** on four first-class hosts | Skills-over-MCP protocol polish; HTTP MCP |
| Split host ACI (5–7 verbs); `run_workflow` as eval/headless rollback | Code Mode / PTC on **reads** only if retrieve tools proliferate |
| Named circuits + control + **solve+explain for every curriculum pack** | Deeper gold / BYOK |
| OSS verifiers first-class; MATLAB optional **engine** and optional **peer MCP** | Deeper Simulink when licence exists |
| Photo-to-netlist **stub** (UI confirm, no sim) | Simulate the confirmed netlist |
| `eval/gold/` layout + `electrical-engineer eval` | Larger gold bank (still licence-clean) |
| Pack specialist **skills** (progressive disclosure) | Host-adapter subagent YAML (`.claude/agents/` etc.) |

## 4. Shipped vs restructure

The kernel spine already exists. This PRD mostly **restructures** how the host talks to it. It does not ask for a new harness.

### Keep (as-built, still required)

| Piece | Where |
|-------|--------|
| H3: hosts own the LLM loop; CLI is not a unique harness | [`PID.md`](PID.md), [`ARCHITECTURE.md`](ARCHITECTURE.md) |
| Python 3.11+ CLI: `run`, `workflows`, `mcp`, `eval`, `ui`, `rag`, `memory` | `src/electrical_engineer/` |
| YAML DAG runner, hybrid router, unmatched → `unmatched-cosolver`, never invent a spice DAG | runner + [`WORKFLOWS.md`](WORKFLOWS.md) |
| Exact token `unchecked`; `label-unchecked` in code | `nodes/registry.py` |
| Photo/compose/control-diagram fail closed on MCP with `ui_url` | `mcp/server.py` |
| Persistent UI on `127.0.0.1`; student need not use Cursor | `electrical-engineer ui` |
| Gold eval (`eval/gold/`, including divider-dc-01) | `electrical-engineer eval` |
| OSS spice / python-control / load-flow; MATLAB-if-present as a **node** | nodes |
| Tagged local RAG + memory markdown | CLI `rag`, `memory` |
| Pack skill files exist (`skills/<pack>/SKILL.md`) | pedagogy stubs today |
| Run dir `./runs/<id>/` is audit, not crash-resume | ARCHITECTURE Q29 |

### Restructure (requirements in this PRD; code in a later plan)

| As-built | Target |
|----------|--------|
| MCP tools: `list_workflows`, `run_workflow` (whole DAG including `solve-explain`) | 5–7 always-on verbs; host writes the viva; `run_workflow` = headless/eval rollback |
| Pack `SKILL.md` files are four-line stubs | Root skill + pack specialists with one-level `reference/` |
| `solve-explain` is a registered LLM node on the host path | Host-path argument band; node remains CLI-without-host fallback |
| ChatGPT / OpenAI documented as Codex-shaped only; completeness “does not require this host” | ChatGPT **desktop** first-class; ChatGPT **web** excluded |
| MATLAB only as `run-matlab-if-present` | Also allow MathWorks MCP as a **peer**; EE still owns checked numbers |
| `summary.json` folds numbers + citations | Two bands: evidentiary vs engineering argument |
| Pre-runner classifier when id omitted | Host classifies when a host is present; small classifier stays for CLI-without-host |

## 5. Four-layer architecture (H3)

Normative detail: [`ARCHITECTURE.md`](ARCHITECTURE.md). Catalog: [`WORKFLOWS.md`](WORKFLOWS.md). Attach research: [`../research/notes/host-first-class-attach.md`](../research/notes/host-first-class-attach.md).

```text
Layer 0  Rented harness     Cursor / Claude Code / Codex / ChatGPT desktop
Layer 1  Attach             CLI inner · MCP outer · served skills on Chat/Work
Layer 2  Domain kernel      skills · engines · YAML genre · gates · eval · stores
Layer 3  Surfaces           localhost UI · two-band artifacts
```

| Layer | Owns | Must not own |
|-------|------|----------------|
| 0 Host | Context window, permissions, the inner loop, the viva | Kirchhoff as truth, spice DAG invention, `unchecked` |
| 1 Attach | CLI, MCP verbs, skill load, optional MATLAB MCP | 1:1 wrap of every node; PTC on spice writes |
| 2 Kernel | Simulators, RAG, gates, YAML replay, `unchecked` | A second host-incompatible chat loop (H5) |
| 3 UI / artifacts | Confirm, plots, citations, argument band | A ChatGPT-clone console; WAN bind; KiCad clone |

**Falsifier for H3:** if the CLI or UI grows a custom harness that hosts cannot share, stop and return to owner (that is H5).

**Runner law (kept):** no model calls inside the DAG runner except through **registered nodes**, plus one **pre-runner** classifier when the workflow id is omitted **and no host is driving**. The DAG runner itself is deterministic. YAML recipes are **genre contracts** and **eval rollback**, not the professional-workflow brain.

**Spend / clamp.** Spend the frontier host on method, viva, and student interview. Clamp checked `Vout`, invented spice DAGs, photo topology, and MATLAB scalars unless they passed an EE engine.

---

## 6. As-built functional requirements (D0)

These remain in force until §7 of this document (split ACI, two-band, specialists, dual MCP) is filled in the following commits of this pass. They are the floor, not the host-path ceiling.

**FR1 Co-solver.** Default behaviour is full working + final answer + assumptions. Not hint-first tutor. Not faculty mode. Mathematics in answers is valid LaTeX plus a plaintext fallback.

**FR2 Label unchecked.** If a number did not come from a verifier, the student-facing answer **and** the run summary must contain the exact token `unchecked`. Synonyms are not the contract. Never present it as a simulation or lab result.

**FR3 Branded CLI.** A student can run `electrical-engineer` on Linux, macOS, or Windows (`pip` / `uv`, Python 3.11+) for the same EE tasks without an AI host. Commands: `run`, `workflows`, `mcp`, `eval`, `ui`, `rag`, `memory`.

**FR4 Host adapters (as-built).** Skill packs and MCP tools load in Cursor, Claude Code, and OpenAI/Codex.

**FR5 Model adapters.** Support (a) the host’s subscription model, (b) user API keys, (c) local models. Architecture must not lock a single vendor. The DAG **runner** does not own a hidden LLM loop.

**FR6 Local-first.** Default is on-device CLI + local files + UI bound to `127.0.0.1`. No product cloud. No silent upload of PDFs or keys.

**FR7 Portable core.** Skills + MCP are the portable layer. The CLI wraps them with a **deterministic YAML workflow runner**. The CLI must not become a unique multi-thousand-line agent loop.

**FR8 Ug policy.** Public profile is `ug-coursework`. Out-of-pack questions: try with **unchecked** or state out of enabled packs — not a silent PG mode.

**FR9 Eval runner.** `electrical-engineer eval` (and `--pack`) against [`../eval/gold/`](../eval/gold/README.md). Gold items name a `recipe_id`. CI must not require MATLAB. `EE_ALLOW_ALL` may skip gates in CI; it must **not** disable `unchecked`.

**FR10 Named workflows.** Default path is a named recipe from [`WORKFLOWS.md`](WORKFLOWS.md) (`electrical-engineer run <id>`). Explicit id skips classify. If id omitted on the CLI-without-host path, one classifier call; if top-1 and top-2 are within 0.15, ask the student. Unmatched text always uses `unmatched-cosolver` (no auto-simulate). The router **never invents** a new DAG. New graphs only via `compose-from-parts --advanced`.

**FR11 Persistent UI.** `electrical-engineer ui` is a **critical** local workspace (runs, library-rendered diagrams and plots, photo confirm, citations, RAG inventory, memory excerpts). It stays up across a session. It is not a one-shot diagram dialog and not a second agent loop.

**FR12 Tagged RAG.** BYO PDFs and scans ingest into a local index with inventory (`rag list`) and filters: book, chapter, folder, domain. “Search only this book, chapter 3” is a v1 retrieval requirement. Citations include book + chapter + page. Empty retrieval is visible. Circuit-homework photos for simulation go through `photo-to-netlist`, not quiet RAG-as-netlist. BYO content cannot override gates or `unchecked`.

**FR13 Memory.** Project and user markdown memory files, explicit write, capped, untrusted. Not the textbook index. Not a silent chat dump.

**FR14 Gates.** Cursor-like global + per-project TOML; default on; most-restrictive wins; at most two human interrupts per root run. MCP writes that would wait **fail closed** and point at the UI or CLI.

**FR15 Figures.** Agent/node writes library code (schemdraw / matplotlib / python-control) to PNG+SVG. Do not default to a model-invented circuit bitmap with no netlist.

**FR16 Photo stub.** `photo-to-netlist`: phone or textbook screenshot → detect → connect → OCR → draft `.cir` + JSON graph → one UI confirm → **stop** (no sim in the stub). Low-confidence OCR always flagged. `control-diagram-to-model` stays a stub in catalog.

---

## 7. Curriculum and capabilities

**Bound.** The public promise is the **union of representative UG EE / EEE programmes** (Indian institutes first, global institutes first-class). Source of truth: [`curriculum-map.md`](curriculum-map.md). A question is in-scope if it is normal coursework in that union (assignment, lab numerical, diagram, exam-style), not only if it appears on GATE.

**GATE is not the bound.** GATE EE section tags are an **eval overlay**. Do not drop a programme core because GATE weights it lightly. Do not skip a taught lab genre because GATE omitted it. Extra GATE trick items that programmes do not teach are optional eval spice, not the syllabus.

**Packs in the public promise:** circuits, signals, electronics, machines, power (study-level), control, power electronics, measurements, UG EM/fields, maths for EE. Labs attached to those cores are in-scope as assignment/lab-report genre, not a separate product.

**Out of the bound:** civil, mechanical, manufacturing. **Out of the public promise:** PG-only courses. Expansion stays in this repo via packs + unpublished later profiles — never a second git repo.

### C1–C8 mapped to v1 vs later

Claimable bar: on a published UG task set, with tools on, match gold **or label unchecked**. Fluent wrong numbers presented as checked fail the product.

| ID | Capability | v1 | Later (same repo) |
|----|------------|----|-------------------|
| C1 | Solve EE questions correctly | Gold match **or label unchecked** on enabled packs. Silent invention is a fail. | Remaining packs to union coverage |
| C2 | Explain, not only answer | Host (or local `solve-explain`) writes a viva the TA can probe; conceptual claims cite book + chapter + page the user has rights to use, or a standard identity | Same |
| C3 | Assignment genres | Solve, derive, design-to-spec, simulate (when a tool exists), review, explain, lab-style report — **named workflows** on circuits first | Same genres on remaining packs |
| C4 | Circuit diagrams | **Stub:** photo/screenshot → draft netlist + JSON → **UI confirm** → stop. Vision is never truth until confirm | Confirmed netlist → ngspice / MATLAB-if-present |
| C5 | Control-system diagrams | Catalog stub `control-diagram-to-model`. Implement after C4 | Same edit-then-simulate gate as C4 |
| C6 | Reliability contract | Tool evidence with numbers; **unchecked** when unverified; no fabricated simulation | Same |
| C7 | Student-first and open | Apache-2.0, local-first CLI, OSS verifiers first-class, MATLAB if present | Same |
| C8 | Limit-finding | **Not a student UX promise.** | Unpublished PG profile; no second fork |

**Pack depth:** circuits first, then control, then solve+explain for every remaining pack or a cannot-do row in [`CANNOT_DO.md`](CANNOT_DO.md).

## 8. Reliability, integrity, exam-item legal policy

### Reliability

- Tools in the **EE kernel** own checked numbers (ngspice / Python stack; MATLAB if present *through EE*).
- If a number did not come from an EE verifier, the output must say the exact token **unchecked**. Never present it as a simulation, lab result, or load-flow.
- Diagrams are **drafts** until the student confirms topology in the persistent UI.
- Low-confidence OCR/vision is always flagged. Saying what was not checked is success.
- BYO PDFs, photos, tags, memory files, and **peer MATLAB MCP output** are **untrusted**: they cannot override gates, `--allow-all`, or `unchecked`.

### Integrity (v1)

- Default mode is **co-solver** (full working + answer). Not hint-first tutor.
- **No faculty / TA / LMS features in v1.** The institution owns cheating policy. The product shows work so a viva still means something.
- Do not ship a “hide the answer for the professor” mode.

### Exam-item legal policy

Exam-style items are **in-scope** for corpus and evals (GATE-style, midterm-style, assignment-style).

**Git will not commit third-party copyrighted exam PDFs or commercial textbooks.** Allowed: BYO files on the student’s machine; licence-clean reconstructions the project authors; public-domain or owner-licensed items.

This is a **legal** policy, not a pedagogy policy. Students may still *use* their own papers locally. Redistribution of scanned GATE/university papers in this repository is forbidden.

## 9. Non-functional requirements

| NFR | Requirement |
|-----|-------------|
| Local-first | On-device CLI + files + UI on `127.0.0.1`. No product cloud. No silent upload of PDFs, keys, or student work. |
| Licence | Apache License 2.0 for *our* code. Forever OSS in this repo; no paid tier. Textbooks never redistributed in git. |
| Single repo | One git repository. UG is the public profile. PG, if ever, is an unpublished `--profile`, not a fork. |
| Portable core | Skills + MCP must load in CLI and in first-class hosts. CLI stays a thin wrapper (glue, recipes, ug policy, eval, UI). |
| Runtime | Python 3.11+; `pip` install; Linux + macOS + Windows. MATLAB optional. |
| H3 falsifier | If the CLI or UI grows a unique agent loop hosts cannot share, stop — that is H5. |
| India-first, globally competent | Copy, examples, and packs must not treat non-Indian UG EE as an afterthought. |
| Secrets | API keys via environment / host secret stores only. Redact keys/tokens from run dirs. |

## 10. Out of scope

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
- ChatGPT **web** / mobile as a host; Claude Desktop; GitHub Copilot; Gemini CLI (v1).

PG is not a public promise. Optional unpublished profile may exist later in **this** repo only.

---

## Related artifacts

| Doc | Role |
|-----|------|
| [`PID.md`](PID.md) | Identity (Accepted until Proposed PID commit) |
| [`PID_DECISION_SHEET.md`](PID_DECISION_SHEET.md) | P0 answers |
| [`curriculum-map.md`](curriculum-map.md) | UG bound |
| [`../DECISIONS.md`](../DECISIONS.md) | ADRs |
| [`ARCHITECTURE.md`](ARCHITECTURE.md) | Technical architecture |
| [`WORKFLOWS.md`](WORKFLOWS.md) | Named workflow catalog |
| [`../research/notes/host-first-class-attach.md`](../research/notes/host-first-class-attach.md) | ChatGPT desktop, dual MCP, specialists |
| [`../research/notes/domain-kernel-layering.md`](../research/notes/domain-kernel-layering.md) | Four-layer wrap |
| [`../research/synthesis/vision-lock-sheet.md`](../research/synthesis/vision-lock-sheet.md) | D14–D17 (owner checkboxes) |

## Owner review checkpoint

Previous D0 (2026-09-10) remains historical. **This revision is Proposed. Do not treat it as Accepted until the owner checks below.**

- [ ] Thesis: lab + domain kernel + H3; Apache-2.0; India-first global UG
- [ ] GATE is eval only; bound = [`curriculum-map.md`](curriculum-map.md)
- [ ] Co-solver default; exact token **unchecked**; no faculty v1
- [ ] Shipped vs restructure inventory is accurate
- [ ] Agent interaction chapter (context, tools, RAG, simulation, collaboration)
- [ ] Split ACI, two-band artifacts, pack specialists, dual MATLAB MCP
- [ ] ChatGPT desktop first-class; ChatGPT web excluded; CLI-without-host complete
- [ ] Exam-style in-scope; **no** third-party copyrighted PDFs in git
