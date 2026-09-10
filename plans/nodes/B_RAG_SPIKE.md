# Node plan — B_RAG_SPIKE — RAG spike

> Parent: [EXECUTION_GRAPH.md](../../EXECUTION_GRAPH.md)

| Field | Value |
|-------|-------|
| **Node id** | `B_RAG_SPIKE` |
| **Job** | Measure LightRAG 1.5 (RAG-Anything path) vs Docling-thin vs BM25+dense; wrap the winner; do not lock before numbers |
| **Wave** | 5 |
| **Depends on** | B_NODES `retrieve_port` |
| **Write paths** | `src/electrical_engineer/rag/**`, `research/notes/rag-spike-2026-09.md`, `tests/unit/test_rag_filters.py` |
| **Read paths** | ADR-0004, `research/synthesis/rag-stack-recommendation.md`, HKUDS LightRAG v1.5 notes |
| **subagent_type** | generalPurpose |
| **Model** | `cursor-grok-4.6-high` |
| **Isolation** | `rag/` + spike note |

---

## Objective

Quality then speed. Spike on **one licence-clean owned chapter** (not a commercial book). Engines: (1) LightRAG ≥1.5 MinerU multimodal (RAG-Anything merged; standalone RAG-Anything is unmaintained), (2) Docling + thin index, (3) BM25+dense files. Record precision@small-budget, citation book/chapter/page, filter `book_id`/`chapter_id`/`folder_tag`/`domain_tag`, empty-retrieval visible. EE facade always owns metadata. Optional local patches live under our package, not a silent fork in git of the whole upstream. **Winner chosen only after the note has numbers.** Inventory CLI `rag add|list|tag`. Untrusted ingest.

## Non-goals

- Shipping commercial PDFs
- Microsoft GraphRAG as primary
- Locking engine in A1 (already deferred here)

## Contract

**Input:** `{ "retrieve_port": true }`

**Output:** `{ "rag_facade": true, "engine": "lightrag15|docling|bm25|deferred", "filters": true, "spike_note": "path" }`

## Commits

| # | Commit | Gate |
|---|--------|------|
| 38 | `docs(rag): spike protocol + corpus rules` | no commercial PDF |
| 39 | `feat(rag): facade + inventory CLI` | `rag list` |
| 40 | `feat(rag): retrieve-passage filters` | empty visible |
| 41 | `docs(rag): spike results + engine pick` | numbers in note |

## Do not

- Decide the engine in commit 38
- Commit book binaries

## Return to graph

`engine`, `spike_note`, failures.
