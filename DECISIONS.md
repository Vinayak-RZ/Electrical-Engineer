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
- **Decision:** Ground concepts via **local textbook RAG** (curator/BYO ingest → GitHub Release packs or on-machine index; MCP tools + structure-aware hybrid retrieval); use skills for pedagogy; never commit commercial book text.
- **Consequences:** Ingestion quality becomes a core engineering problem; licence-safe by default. Ingest library choice is ADR-0004.
- **Alternatives:** Skills-only; fine-tune; redistributed PDF corpus (rejected).
- **Sources:** `research/notes/ee-corpus-and-licensing.md`, `research/notes/rag-*.md`, `research/notes/local-package-and-embedding-release.md`

---

## ADR-0003 — Verification tier

- **Status:** proposed
- **Context:** Numeric EE answers must not be invented.
- **Decision:** **MATLAB/Simulink MCP as intended primary verifier**; OSS SPICE/Python stack as documented fallback.
- **Consequences:** Licence dependency for full fidelity; policy to refuse unverified “simulation” claims.
- **Alternatives:** OSS-primary; simulation optional.
- **Sources:** `research/notes/matlab-simulink-surface.md`, `research/notes/open-source-verification.md`

---

## ADR-0004 — RAG library (RAG-Anything)

- **Status:** proposed
- **Context:** EE textbooks are multimodal (prose, multi-column layout, tables, circuit figures, equations). HKUDS/RAG-Anything is an all-in-one multimodal RAG library on LightRAG+MinerU that targets exactly that document class. The project already proposed a local-first runtime: GitHub Release embedding packs into Chroma (or sqlite-vec), queried via MCP.
- **Decision:** Use **RAG-Anything as the curator-side and optional BYO ingest/enrichment engine**. Export structure-aware chunks + embeddings into the planned Release packs. Do **not** make LightRAG’s `working_dir` the default student runtime. Keep MATLAB/OSS verification outside RAG.
- **Consequences:** We own a thin export adapter (content_list → pack schema). Query path stays small and offline. Dual-graph retrieval is optional P1. MinerU’s extra licence terms apply if MinerU is the default parser (Docling remains the CPU/licence-simpler fallback).
- **Alternatives:** (A) Whole-stack RAG-Anything/LightRAG on every laptop — rejected for store mismatch and weight. (B) Parse-only Docling/MinerU with no RAG-Anything — runner-up if a later owned-chapter spike shows processors add nothing. (C) ColPali page-as-image — rejected as pack/runtime default (weak symbolic maths). (D) RAGFlow as product — rejected (app, not library).
- **Sources:** `research/notes/rag-anything-evaluation.md`, `research/notes/rag-anything-local-releases.md`, `research/synthesis/rag-stack-recommendation.md`, `research/notes/local-package-and-embedding-release.md`
