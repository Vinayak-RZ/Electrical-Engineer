# DECISIONS

ADR seeds from the research phase. Status values: `proposed` | `accepted` | `superseded`.

---

## ADR-0001 — Harness base

- **Status:** proposed
- **Context:** Need a place to run EE skills, RAG, and MATLAB tools while remaining usable from multiple agent hosts.
- **Decision:** Prefer **O1 package-first hybrid** (portable MCP + skills, optional Pi package). Avoid hard-fork (O2) and greenfield harness (O4) unless falsifiers hit.
- **Consequences:** Faster experiments; must maintain MCP/skill quality; Pi MCP bridge may be needed.
- **Alternatives:** O2 Pi fork; O3 thin layer only; O4 custom harness.
- **Sources:** `research/notes/pi-feasibility.md`, `research/synthesis/option-scoring.md`, `research/synthesis/recommendation.md`

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
- **Decision:** **MATLAB/Simulink MCP as intended primary verifier**; OSS SPICE/Python stack as documented fallback.
- **Consequences:** Licence dependency for full fidelity; policy to refuse unverified “simulation” claims.
- **Alternatives:** OSS-primary; simulation optional.
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

## ADR-0005 — UG-bounded success bar and later research fork

- **Status:** proposed
- **Context:** The project needs a public definition of “we succeeded” that matches a student-first vision (solve + explain + diagrams + reliability) without claiming a shipped agent, and without competing with licence-locked plant-floor or EDA copilots.
- **Decision:** Publish a **verified capability list** (C1–C8) at the top of `README.md` as the success bar. Keep the public product **UG/PG-coursework bounded**. Use a later **fork or parallel track** to explore PG/operational/analog-search limits. Reliability = tools own numbers; vision drafts are not truth until edited.
- **Consequences:** Eval design must eventually instantiate C1–C8; marketing language that implies a finished tutor is forbidden until those evals exist. The landscape note is the evidence that this bar matches how core-engineering AI actually works in 2025–2026.
- **Alternatives:** Exam-score-only bar; “any question, no refuse path”; plant-floor industrial scope; closed-source student app.
- **Sources:** `research/notes/ai-core-engineering-landscape.md`, `research/notes/ee-task-taxonomy-draft.md`, `research/notes/capability-eval-design.md`, `README.md`
