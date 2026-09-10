# Gate 0 — Research, then questions

**Status:** Blocking. Graph-engineering forbids compiling nawab §19, `EXECUTION_GRAPH.md`, or `plans/nodes/*.md` until the questions in this file are answered.  
**Date:** 2026-09-10  
**Skill:** [graph-engineering](../../.cursor/skills/graph-engineering/SKILL.md) Gate 0 + [nawab-plans](../../.cursor/skills/nawab-plans/SKILL.md) project profile  
**Base:** `main` @ `b6564a7` (fetched 2026-09-10)

This is **not** an approved implementation plan and **does not** authorize product code.

After answers: lead compiles nawab §0–§18 (project profile) into [`IMPLEMENTATION_PLAN.md`](../../IMPLEMENTATION_PLAN.md), then §19 + [`EXECUTION_GRAPH.md`](../../EXECUTION_GRAPH.md) + linked node plans. Approving **that** graph starts execution immediately.

---

## 1. Research findings (repo state)

Greenfield product workspace. **No** `pyproject.toml`, `src/`, `packages/`, `.specify/`, CLI, MCP server, UI, or eval runner. Authority is documentation only.

| Layer | State | Path |
|-------|-------|------|
| Identity | **Accepted** | [`docs/PID.md`](../PID.md) |
| Requirements | **Draft** — owner review still open | [`docs/PRD.md`](../PRD.md) |
| Architecture | **Proposed** | [`docs/ARCHITECTURE.md`](../ARCHITECTURE.md) |
| Workflow catalog | **Proposed** (ids renamable until first CLI) | [`docs/WORKFLOWS.md`](../WORKFLOWS.md) |
| UG bound | Done | [`docs/curriculum-map.md`](../curriculum-map.md) |
| ADRs | 0001/0005/0006 accepted; 0002–0004 and **0007** proposed | [`DECISIONS.md`](../../DECISIONS.md) |
| Architecture Q&A | Q1–Q64 frozen for the Proposed draft | [`research/notes/architecture-qa-gate.md`](../../research/notes/architecture-qa-gate.md) |
| Eval layout | Folders specified; **zero gold items** | [`eval/gold/README.md`](../../eval/gold/README.md) |
| Prior plan | Research-phase only; forbids product nawab until PRD accept | [`IMPLEMENTATION_PLAN.md`](../../IMPLEMENTATION_PLAN.md) |
| Licence | Apache-2.0 | `LICENSE` |

Locked P0 (do not reopen): H3 branded CLI wrapping portable skills + MCP + local RAG; not H4/H5; Apache-2.0; forever OSS; India-first global UG; GATE is eval overlay; co-solver default; exact token `unchecked`; one repo; no faculty v1; no civil/mechanical; no commercial PDFs in git; UI on `127.0.0.1`; YAML DAG runner; hosts own the main LLM loop.

Skills loaded for this gate: `nawab-plans` (project), `graph-engineering`, `ponytail`, `frontend-architecture`, `backend-architecture`, `agentic-system-design`, `system-design-tradeoffs`, `speckit.mdc`. **Not** graphify — that maps a codebase; this repo has no product code to cluster.

---

## 2. What “entire product” can mean (must pick)

The user asked for an end-to-end plan that **builds the entire product**. The PRD splits **now** vs **later**. Compiling one graph that pretends they are the same size would either under-build or explode the commit matrix.

| Option | Ships in this graph | Out of this graph |
|--------|---------------------|-------------------|
| **A — PRD v1 public promise** | CLI (`run`, `workflows`, `mcp`, `eval`, `ui`, `rag`); YAML runner + gates; persistent UI; circuits named recipes; unmatched-cosolver; control **specified**, implement after circuits; C4 photo **stub**; C5 catalog stub; `eval/gold/` + thin runner; tagged RAG; memory; host skill docs | C4 simulate-after-confirm; remaining pack solve/simulate DAGs; HTTP MCP; crash-resume; PG profile |
| **B — PRD v1 + later rows in one phased graph** | Everything in A, then later waves: C4 sim, C5 implement, remaining `explain-*` packs, larger gold bank | H4/H5, faculty, plant PLC, second repo, copyrighted books in git |
| **C — curriculum-map union as v1** | Solve/simulate/design DAGs for all 10 packs in the first ship | Same never-list as B |

Default if you skip: **A**, because that is the PRD “Now” column. You asked for “entire product,” so **B** is the other honest reading.

---

## 3. Preview — not compiled (lifecycle + likely nodes)

This is the shape Gate 0 will compile **after** answers. No node-plan files exist yet. No §19. Do not treat this as approval to run.

### Lifecycle coverage

| Stage | Likely node(s) | Notes |
|-------|----------------|-------|
| Research + questions | R0 | This document. Lead only. |
| Docs-in | D0 | PRD/architecture accept recorded; gaps listed; Spec Kit constitution **if** you choose it |
| Architecture | A1 | ADR-0007 accept; package layout; typed ports prose; UI architecture note |
| Design / UI UX | U1 | Required — persistent UI is critical. Information architecture, states, a11y. Not a KiCad clone |
| Build | B* fan-out | See workstreams. Disjoint write paths |
| Integrate | M1 | Wire CLI ↔ runner ↔ UI ↔ MCP ↔ skills. Barrier |
| Evaluate | E1 | pytest + gold items + injection pack + `unchecked` contract |
| Run | R1 | **Boot** `electrical-engineer --help`, `ui`, one named recipe, MCP stdio. Not unit tests alone |
| Trials | T1 | Happy, empty RAG, unmatched+unchecked, gate fail-closed, injection, photo-stub confirm-no-sim |
| Docs-out | D1 | README + extensive + host adapter docs **after** it runs |

### Likely workstreams (disjoint paths)

| ID | Owns | Parallel with |
|----|------|----------------|
| WS-CORE | `src/electrical_engineer/` runner, CLI, gates, run-dir, router | after A1 |
| WS-NODES | registered Python activities (spice, control, unchecked, summary) | WS-CORE contracts |
| WS-WF | `workflows/<pack>/*.yaml` + `skills/<pack>/SKILL.md` | WS-NODES ids |
| WS-UI | localhost viewer (`127.0.0.1`) | WS-CORE run JSON + artifact paths |
| WS-MCP | stdio `list_workflows`, `run_workflow` | WS-CORE |
| WS-RAG | ingest/index sidecar + `rag` CLI | can trail CORE; inventory is P0 for C2 |
| WS-EVAL | `eval/gold/` items + `electrical-engineer eval` | after first recipes exist |
| WS-HOST | Cursor / Claude Code / OpenAI adapter docs | after skills exist |

### Preview topology (real edges only)

```text
R0 (this gate)
  → D0 + A1          (parallel: docs-in does not write src/)
  → U1 // B-CORE     (U1 needs A1 contracts; B-CORE needs A1 layout)
  → B-NODES // B-UI // B-MCP   (after CORE publishes run JSON + CLI entry)
  → B-WF // B-RAG              (after node ids + ports exist)
  → M1 barrier
  → E1 → R1 → T1 → D1
```

Fake edges cut: UI does not wait on RAG inventory to render a run dir; MCP does not wait on gold items; host docs do not wait on photo stub.

### Model policy (from this request; confirm in Q18)

| Tier | Use | Cursor slug |
|------|-----|-------------|
| Judge / build / architecture / UI / runner / eval design | **Grok 4.6** | `cursor-grok-4.6-high` |
| Extract, classify, inventory, scaffolding, docs-sync | **Composer 2.5** | `composer-2.5` (or `composer-2.5-fast` if you pick speed) |
| Lead git, gates, PR, merge plumbing | Lead session | `inherit` |

Lead still owns every commit. Subagents do not commit. One nawab §9 row per commit.

---

## 4. Gaps that block compile (not already locked)

Architecture Q&A closed runner/FSM/gates/MCP/UI-role/`unchecked`. These remain **unspecified** and would be guessed if we compiled now:

1. PRD / architecture **accept** (docs still say draft / Proposed).
2. P1 PRD §10 checkboxes (MATLAB/OSS, RAG tags, v1 slice, circuits-then-control, orchestrator).
3. **UI implementation stack** (Python templates vs JS SPA). Architecture says “thin viewer,” not React/HTMX.
4. **RAG-Anything** still proposed (ADR-0004); spike never approved (PROGRESS Phase S skipped).
5. **Packaging** (uv/pip, src layout, console script name).
6. **Local LLM / BYOK** adapter: OpenAI-compatible only vs Ollama vs both.
7. **Photo stub vision** backend (host vision vs local VLM vs stubbed fixtures first).
8. **Spec Kit** `.specify/` missing; greenfield usually wants constitution → specify before code.
9. **Commit budget** (nawab requires asking before §9).
10. Scope of “entire product” (section 2).
11. Whether **control pack implementation** is in this graph or a later graph after circuits ships.
12. Gold-set **size** (architecture: do not design a 200-task bank).
13. Workflow **id freeze** (WORKFLOWS.md: renamable until first CLI).

---

## 5. Trade-off blocks (answer with a letter or PRIORITY)

### Trade-off: persistent UI stack

**Option A:** Python-only (Starlette or FastAPI + Jinja + HTMX, library SVG/PNG). — Pros: one runtime, stays H3 glue, Windows/macOS/Linux via pip, hard to grow a second agent loop. Cons: less interactive topology editing; custom JS still needed for graph confirm.  
**Option B:** FastAPI JSON API + Vite/React SPA. — Pros: richer workspace, existing frontend-architecture skill. Cons: two toolchains, H5-falsifier risk if the SPA grows a brain, heavier install for students without Node.  
**Default if you skip:** A (ponytail + H3 falsifier).  
**Override:** PRIORITY = SIMPLICITY | QUALITY | SPEED

### Trade-off: RAG engine

**Option A:** Spike RAG-Anything (MinerU) on one owned chapter **before** wiring `retrieve-passage` (ADR-0004). — Pros: matches Proposed architecture; fail closed to Docling fallback. Cons: heavy deps; Phase S was skipped once.  
**Option B:** Ship a thin local index (files + BM25 + optional embeddings) that already supports book/chapter/folder filters; keep RAG-Anything behind a seam. — Pros: CLI/eval can ship; citations work. Cons: diverges from Proposed until a later swap.  
**Option C:** Block all recipes that need RAG until the spike passes; ship unmatched-cosolver + spice without retrieve. — Pros: honest. Cons: C2 citations fail the public promise.  
**Default if you skip:** A, because architecture says do not silently replace RAG-Anything.  
**Override:** PRIORITY = QUALITY | SPEED | SIMPLICITY

### Trade-off: spec artifacts

**Option A:** Spec Kit Phase 0 (`constitution` → `specify` → `plan` → `tasks`) **inside** D0/A1, then graph build waves. — Pros: greenfield rule in AGENTS.md; converge later. Cons: duplicates nawab if we also write a 18-section plan.  
**Option B:** Nawab + graph-engineering only; no `.specify/` this pass. — Pros: one execution contract. Cons: skips the repo’s stated greenfield path.  
**Default if you skip:** A, collapsed: constitution + specify only (not a second task dump that fights §9).  
**Override:** PRIORITY = CONSISTENCY | SPEED | SIMPLICITY

### Trade-off: photo-stub vision

**Option A:** Real vision nodes calling the configured host/BYO/local VLM; UI confirm; stop (no sim).  
**Option B:** Fixture-first stub (checked-in licence-clean images + deterministic detect/OCR fakes) so eval/CI do not need a vision model; real vision behind the same ports.  
**Default if you skip:** B for CI + A for interactive CLI when a vision model is configured.  
**Override:** PRIORITY = QUALITY | COST | SIMPLICITY

---

## 6. Questions (one list)

Reply by number. `skip` uses the stated default. Must-answer items have **no** silent default except where marked.

### Must-answer (blocks compile)

1. **PRD.** Accept [`docs/PRD.md`](../PRD.md) as-is, list edits, or reject? (PRD §11 checkpoint is still unchecked.)
2. **Architecture.** Accept [`docs/ARCHITECTURE.md`](../ARCHITECTURE.md), [`docs/WORKFLOWS.md`](../WORKFLOWS.md), and ADR-0007, list edits, or reject?
3. **P1 defaults (PRD §10).** Accept all five rows (MATLAB-if-present/OSS-first-class; tagged local RAG; v1 = C1–C3 + C6–C7 + UI + eval + C4 stub + C5 catalog stub; circuits then control; YAML DAG orchestrator), or list overrides?
4. **Entire product (section 2).** A, B, or C?
5. **Commit budget** for the compiled §9 matrix? Nawab default for greenfield is **25–50+**. Pick a number or range (example: `40` or `32–40`). Hard requirement once set.
6. **UI stack.** Trade-off A (Python+HTMX) or B (React SPA)?
7. **RAG.** Trade-off A (RAG-Anything spike first), B (thin index now, seam for later), or C (no retrieve until spike)?
8. **Spec Kit.** Trade-off A (constitution+specify in D0) or B (nawab+graph only)?
9. **Photo vision.** Trade-off A, B, or the combined default (fixtures in CI, real vision when configured)?
10. **Control pack in this graph?** Implement `solve-control-problem` / `explain-control` in this one-shot after circuits, or only specify YAML/skills and leave implementation for a later graph?
11. **`compose-from-parts --advanced`.** Ship in this graph (gate=ask, 16/24 cap), or catalog + fail-closed stub until later?
12. **Local LLM / BYOK.** Required adapters in v1: (a) OpenAI-compatible HTTP only, (b) that plus Ollama, (c) host-subscription path only for LLM nodes (CLI deterministic nodes work with no model). Which?
13. **Packaging.** (a) `uv` + hatchling `src/` layout + `pip install -e .`, (b) plain setuptools/pip, (c) no preference (lead picks a). Default if skip: **a**.
14. **Workflow ids.** Freeze the current `WORKFLOWS.md` ids in this plan, or keep them renamable through first CLI commit (Q47)?
15. **Gold-set size for E1.** Proposed: **8–12** licence-clean items (circuits + unmatched + ≥2 injection). Accept, or give another number?
16. **Branch strategy.** Single feature branch for the whole graph (`cursor/…-eb74`), or per-workstream branches merged by the lead?
17. **Approval implication.** Graph-engineering: approving the compiled plan **starts execution immediately**. Confirm that, or require a second “go” after the graph is written?

### Optional (defaults if skipped)

18. **Cheap model slug.** Composer 2.5 as `composer-2.5` or `composer-2.5-fast`? Default: `composer-2.5`.
19. **Judge model slug.** `cursor-grok-4.6-high` vs `cursor-grok-4.6-medium`? Default: **high**.
20. **CI OS.** Ubuntu-only first, or Ubuntu + Windows + macOS? Default: **Ubuntu** in GitHub Actions; document Windows/macOS as supported, test later.
21. **Figure libraries.** schemdraw + matplotlib + python-control only, or also lcapy? Default: **first three**; lcapy later.
22. **Load-flow in v1.** Register `run-load-flow` (pandapower) now even if no named power recipe, or defer the node? Default: **register the node**, no named power DAG until option B/C in Q4.
23. **Python version ceiling.** 3.11+ as written, or also test 3.12/3.13? Default: **3.11 and 3.12** in CI.
24. **Public PyPI in this graph?** Default: **no** — git/editable install only until T1 is green.
25. **Host skill install.** Document copy/symlink into Cursor/Claude/Codex, or ship an `electrical-engineer init-host` helper? Default: **docs only** (ponytail).
26. **Eval `--pack`.** Implement `--pack circuits` in this graph? Default: **yes**.
27. **Memory CLI.** Explicit `memory` command vs only recipe nodes writing the two dirs? Default: **nodes + documented paths**, no extra top-level command (FR3 command list does not include `memory`).
28. **Auto-open UI.** Architecture: CLI auto-opens browser on visual gates. Allow `EE_NO_BROWSER=1` for CI? Default: **yes**.

---

## 7. After you answer

Lead will, in one follow-up (no product code until the compiled graph is approved unless Q17 says run-on-approve):

1. Record accepts/overrides in `DECISIONS.md` / PRD / architecture checkpoints.
2. Write full nawab **project** §0–§18 into `IMPLEMENTATION_PLAN.md` (commit matrix sized to Q5).
3. Compile `EXECUTION_GRAPH.md` + `plans/nodes/<id>.md` for every lifecycle node (links required).
4. Fill nawab §19. Stop for **graph approval** unless Q17 = start immediately.

Ponytail intensity: **full**. No LangGraph, Temporal, H4/H5, faculty LMS, or copyrighted PDFs.

---

## 8. Explicit non-compile

The following do **not** exist yet, by skill law:

- `EXECUTION_GRAPH.md`
- `plans/nodes/*.md`
- A filled nawab §9 commit matrix
- Product `src/`
