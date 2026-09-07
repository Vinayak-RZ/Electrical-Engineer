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
