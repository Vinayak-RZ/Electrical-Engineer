# Question bank

Every open research question for this phase. Status: `open` | `answered` | `deferred`.

| ID | Question | Owner WS | Status | Answer / deferral pointer |
|----|----------|----------|--------|---------------------------|
| Q1 | Is a Pi **package** enough for EE specialization, or is a **fork** required? | WS-A | answered | Package-first hybrid; fork only if extension APIs fail — `notes/pi-feasibility.md` |
| Q2 | Can RAG plug into Pi without forking? | WS-A | answered | Yes — Pi documents dynamic context RAG via extensions — `notes/harness-landscape.md` |
| Q3 | How portable are Pi skills to Claude Code / Codex / Cursor? | WS-A | answered | Skill formats converging; treat MCP+skills as portable core — `notes/harness-landscape.md` |
| Q4 | Which EE textbooks can we legally index? | WS-B | deferred | Intended: curator-licensed **embedding packs**; until licence review, **BYO + OER** — `notes/ee-corpus-and-licensing.md`, `notes/local-package-and-embedding-release.md` |
| Q5 | How should formulae and circuit figures be preserved? | WS-B | answered | Layout/formula-aware parse; LaTeX/MathML preferred; figures via caption+image — `notes/rag-parsing-formulae-figures.md` |
| Q6 | What chunking/retrieval design fits EE? | WS-B | answered | Structure-aware + parent-child + hybrid dense/BM25 — `notes/rag-chunking-and-retrieval.md` |
| Q7 | Should RAG enter as MCP, middleware, or multi-hop? | WS-B | answered | MCP portable core + skill multi-hop; optional Pi middleware — `notes/rag-agent-integration.md` |
| Q8 | How do we evaluate EE RAG? | WS-B | answered | Retrieval/faithfulness/citation/EE failure taxonomy + 20 case titles — `notes/rag-eval-methodology.md` |
| Q9 | Is MATLAB/Simulink the primary verifier? | WS-C | deferred | Intended primary; CP-2 licence pending — `notes/matlab-simulink-surface.md` |
| Q10 | What OSS verification covers which domains? | WS-C | answered | Coverage matrix in `notes/open-source-verification.md` |
| Q11 | What task genres define undergrad-EE-capable? | WS-D | answered | Seven genres × GATE sections — `notes/ee-task-taxonomy-draft.md` |
| Q12 | How to measure capability without a PRD? | WS-D | answered | Rubrics + verified/judgement split — `notes/capability-eval-design.md` |
| Q13 | Among O1–O4, which path? | WS-E | answered | O1 hybrid; runner-up O3 — `synthesis/recommendation.md` |
| Q14 | Local/offline models first-class? | WS-E | answered | Yes — local-first package + local vector store; API optional — `notes/local-package-and-embedding-release.md` |
| Q15 | Map PG/PhD genres now? | WS-D | deferred | Light stretch map only; undergrad primary |
| Q16 | Ship curated embeddings via GitHub Release into local Chroma? | WS-B | answered | Feasible; Chroma default; split packs &lt;2 GiB; licence review required — `notes/local-package-and-embedding-release.md` |
| Q17 | Photo of circuit → editable UI → Simulink sim? | WS-C | answered | Feasible via netlist intermediate + UI gate; Simulink/SPICE backends — `notes/photo-to-schematic-to-simulink.md` |
| Q18 | How far has AI come in core engineering (EE, manufacturing, civil), and what success bar should this OSS student project claim? | WS-D | answered | Tool-using verify loops are the real progress; UG-bounded tutor + later research fork — `notes/ai-core-engineering-landscape.md`, root `README.md` |
| Q19 | Steal Cordis/DSH spatiotemporal composability how, without forking DSH? | WS-A | answered | Paradigm only: node plugins in space, DAG recipes in time; do not run Cordis/DSH — `notes/spatiotemporal-composability.md` |
| Q20 | Map Temporal child-workflow vs activity without a Temporal cluster? | WS-A | answered | Node = activity; `run-recipe` = nested named YAML (depth ≤ 3, cycle check) — `notes/architecture-qa-gate.md` |
| Q21 | Light DAG vs FSM vs code-as-workflow vs embeddable library? | WS-A | answered | Custom in-process DAG + tiny FSM; YAML recipes; Python node functions; not LangGraph/Temporal/Treadle — `notes/architecture-qa-gate.md` |
| Q22 | CLI/runner language: Python-only vs Rust/Go CLI + Python nodes? | WS-A | answered | Python 3.11+ CLI/runner/nodes via pip this pass; Go/Rust CLI skin later allowed — `notes/architecture-qa-gate.md` |
| Q23 | How strict is dynamic-compose allowlisting? | WS-A | answered | Typed ports + 16 nodes / 24 edges; only `compose-from-parts`; fail closed — `notes/architecture-qa-gate.md` |
| Q24 | Freeze catalog ids and human titles? | WS-D | answered | Author `docs/WORKFLOWS.md` from owner list; ids renamable until CLI ships; do not freeze the research draft as API — `notes/architecture-qa-gate.md` |
| Q25 | Collapse per-pack explain-* into one workflow? | WS-D | answered | Keep per-pack explain titles — `notes/architecture-qa-gate.md` |
| Q26 | Gate policy file shape (global vs project, allow-all)? | WS-A | answered | Global + project TOML; most-restrictive wins; file + `EE_ALLOW_ALL` + `--allow-all` — `notes/architecture-qa-gate.md` |
| Q27 | Unmatched-intent path details? | WS-A | answered | Always `unmatched-cosolver`; no auto-simulate; exact token `unchecked` — `notes/architecture-qa-gate.md` |
| Q28 | Photo stub contract (C4 still P1)? | WS-C | answered | Detect → connect → OCR → draft netlist → persistent UI confirm; `.cir` + JSON; no sim after confirm — `notes/architecture-qa-gate.md` |
| Q29 | Resume-after-crash via run-dir vs always restart? | WS-A | answered | No crash-resume. Run dir is audit only. New run after process death — `notes/architecture-qa-gate.md` |
| Q30 | May a node invoke another named recipe (child)? | WS-A | answered | Yes: `run-recipe`, max depth 3, cycles rejected — `notes/architecture-qa-gate.md` |

## Sources

- Research notes under `research/notes/` and `research/synthesis/` — retrieved 2026-09-07 — reliability: primary
- User instructions — retrieved 2026-09-07 — reliability: primary

## Confidence

Overall confidence for this register: high

Deferred rows wait on user CP-1/CP-2 or later product choices.
