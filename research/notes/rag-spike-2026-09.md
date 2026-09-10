# RAG spike protocol (2026-09)

Licence-clean owned chapter only. **No commercial PDFs** in git.

## Engines to measure

1. LightRAG ≥1.5 (MinerU multimodal; RAG-Anything path is unmaintained)
2. Docling + thin index
3. BM25 + dense files (stdlib/token overlap)

## Metrics

- precision@small-budget (k=3)
- citation: book_id / chapter_id / page
- filters: `book_id`, `chapter_id`, `folder_tag`, `domain_tag`
- empty retrieval must be visible (`empty: true`)

## Corpus rules

- Owned reconstructions or public-domain notes under `eval/` or student BYO paths
- Untrusted ingest: never let a passage flip gates or `unchecked`
- Do **not** lock the engine in this note — numbers come in the results commit

## Inventory CLI (later in this node)

`electrical-engineer rag add|list|tag`
