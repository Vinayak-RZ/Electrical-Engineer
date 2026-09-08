# Phase completion — RAG-Anything stack research

## Completed work

Evaluated HKUDS/RAG-Anything against Electrical-Engineer’s document type (mixed textbooks) and the already-proposed local GitHub Release + Chroma runtime. Recorded features, implementation, local-run mapping, and a proposed ingest-only decision (ADR-0004).

## Files modified

- Added `research/notes/rag-anything-evaluation.md`
- Added `research/notes/rag-anything-local-releases.md`
- Added `research/synthesis/rag-stack-recommendation.md`
- Updated `DECISIONS.md` (ADR-0002 clarification + ADR-0004)
- Updated registers: `research/DECISION_REGISTER.md`, `research/question-bank.md`, `research/source-ledger.md`
- Updated maps: `research/README.md`, `docs/EXTENSIVE.md`, `PROGRESS.md`, `IMPLEMENTATION_PLAN.md`, `research/synthesis/recommendation.md`

## Architectural changes

None in product code (none exists). Research stance: RAG-Anything is the ingest/enrichment library, not the student runtime.

## Validation performed

`./scripts/research/validate-research.sh --full`

## Known issues

- No owned-chapter spike; EE-specific quality is unmeasured.
- Agent Patterns Catalog MCP was unreachable (MCP-PENDING).
- Export adapter (LightRAG/`content_list` → Chroma zip) is designed, not built.

## Next phase objectives

Wait for acceptance of ADR-0004. If accepted, a later implementation plan can schedule the owned-chapter ingest spike. No product scaffold from this phase.

### What you learned (this phase)

- **Concept:** Dual-graph multimodal RAG — tables/equations/figures become graph entities, not flattened text.
- **Pattern:** Separate **curator ingest** (heavy, RAG-Anything) from **runtime packs** (thin, Chroma + MCP).
- **Trade-off:** Best library for the document type is not the same as the best local-first product architecture.
