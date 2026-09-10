# DECISIONS

ADR seeds from the research phase, plus owner-accepted product locks (2026-09-09). Status values: `proposed` | `accepted` | `superseded`.

Research memo [`research/synthesis/recommendation.md`](research/synthesis/recommendation.md) remains **historical advice**. Product identity is [`docs/PID.md`](docs/PID.md) (Accepted). Requirements: [`docs/PRD.md`](docs/PRD.md).

---

## ADR-0001 — Harness base

- **Status:** accepted (product lock 2026-09-09)
- **Context:** Need a place to run EE skills, RAG, and verifiers while remaining usable from Cursor, Claude Code, and OpenAI, and also as a local CLI without those hosts.
- **Decision:** **H3** — branded CLI (`electrical-engineer`) wrapping portable skills + MCP + local RAG (**H1 layer**). The CLI is glue, ug policy, co-solver defaults, and an eval runner. It must not grow a unique agent loop (that would be H5).
- **Historical research advice:** O1 / H2 (package-first, optional Pi package) scored highest in `recommendation.md`. That advice is **superseded as the product choice**. Do not treat O1 as the locked harness.
- **Consequences:** Skills + MCP stay portable; three model paths (host subscription, BYO key, local LLM); H3 falsifier = CLI diverges from hosts.
- **Alternatives:** H1 skills-only (no branded CLI); H2 optional Pi package; **H4** Electric Pi fork (rejected); **H5** greenfield harness (rejected).
- **Sources:** owner P0; `docs/PID.md`; `docs/PRD.md`; scoring history in `research/synthesis/option-scoring.md`

---

## ADR-0002 — Knowledge grounding (RAG spine)

- **Status:** proposed
- **Context:** Undergrad EE knowledge is dense with formulae and worked examples; model priors alone are insufficient.
- **Decision:** Ground concepts via **BYO textbook RAG** (MCP tools + structure-aware hybrid retrieval); use skills for pedagogy; never commit commercial book text.
- **Consequences:** Ingestion quality becomes a core engineering problem; licence-safe by default.
- **Alternatives:** Skills-only; fine-tune; redistributed corpus (rejected).
- **Sources:** `research/notes/ee-corpus-and-licensing.md`, `research/notes/rag-*.md`

---

## ADR-0003 — Verification tier

- **Status:** proposed
- **Context:** Numeric EE answers must not be invented.
- **Decision:** **MATLAB/Simulink MCP when a licence is present**; OSS SPICE/Python stack is **first-class** otherwise (P1 default in the PRD, not a PID lock).
- **Consequences:** Mixed-licence audience. Unverified numbers are **labelled unchecked** — they are allowed, but must never be presented as simulation or lab results. (Research-era “refuse unverified simulation” is replaced by this label policy.)
- **Alternatives:** OSS-only; MATLAB-only; hard-refuse any number without a tool.
- **Sources:** `research/notes/matlab-simulink-surface.md`, `research/notes/open-source-verification.md`

---

## ADR-0004 — Multimodal RAG ingest engine

- **Status:** proposed
- **Context:** EE textbooks mix text, equations, tables, figures, and multi-column layout; text-only RAG fails. User flagged [RAG-Anything](https://github.com/HKUDS/RAG-Anything) as a candidate all-in-one stack.
- **Decision:** Use **RAG-Anything (MinerU default) as the ingest + index engine** behind a portable **EE RAG MCP server**; distribute via **GitHub Releases** as an installable sidecar with local Ollama/LM Studio backends. Do **not** adopt it as the agent harness or skip the MCP wrapper.
- **Consequences:** Heavy Python/MinerU dependency chain; user-local index and BYO PDFs; spike on one owned EE chapter required before `accepted`. Fallback: MinerU/Docling + thin custom MCP if spike fails.
- **Alternatives:** Thin MinerU+MCP only; Docling+LlamaIndex; VLM-only chunking; commercial parsers; Microsoft GraphRAG as primary spine.
- **Sources:** `research/notes/rag-anything-evaluation.md`, `research/synthesis/rag-stack-recommendation.md`, `research/notes/rag-parsing-formulae-figures.md`, `research/notes/rag-agent-integration.md`

---

## ADR-0005 — UG coursework bound, GATE as eval, single repo

- **Status:** accepted (product lock 2026-09-09; supersedes the research-era “UG/PG + later fork” wording)
- **Context:** The project needs a public definition of success that matches a student-first vision without claiming a shipped agent, and without competing with licence-locked plant-floor or EDA copilots.
- **Decision:** Public promise = **union of representative UG EE programmes** (Indian institutes + global institutes). See `docs/curriculum-map.md`. **GATE EE is an eval overlay / capability check**, not the syllabus bound. **PG is not a public promise.** **One git repository only** — later unpublished `--profile` flags may exist; do not fork UG vs lab. C1–C8 remain the success bar; C8 is not a student UX promise. Reliability = tools own numbers **or** the output says **unchecked**; vision drafts are not truth until the student confirms.
- **Consequences:** Eval may tag GATE sections; missing a taught UG core is a product gap even if GATE omits it. No second repo. README must not promise PG or a research fork as the public line.
- **Alternatives:** GATE-only bound (rejected); public PG promise (rejected); two-repo UG-freeze vs lab fork (rejected).
- **Sources:** owner P0; `docs/PID.md`; `docs/curriculum-map.md`; `docs/PRD.md`; historical `research/notes/ee-task-taxonomy-draft.md`

---

## ADR-0006 — Apache-2.0, forever OSS, co-solver default

- **Status:** accepted (product lock 2026-09-09)
- **Context:** Licence, commercial model, and default student interaction were OPEN in the research PID draft.
- **Decision:** *Our* code is **Apache License 2.0**. This repository is **forever OSS**; no paid tier here. Default student mode is **co-solver** (full working + answer + assumptions). No faculty/TA/LMS features in v1. Civil, mechanical, and manufacturing are never this product.
- **Consequences:** `LICENSE` is Apache-2.0. Hosted paid tutors are out of this repo’s promise. Integrity is “show the work”; institutions own cheating policy.
- **Alternatives:** MIT; AGPL; dual-licence paid tier; tutor-default; faculty v1.
- **Sources:** owner P0; `LICENSE`; `docs/PID.md`; `docs/PRD.md`
