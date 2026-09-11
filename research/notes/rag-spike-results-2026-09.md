# RAG spike results (2026-09-10)

Protocol: [`rag-spike-2026-09.md`](rag-spike-2026-09.md). One licence-clean owned note, not a commercial book.

## Environment

| Engine | Import | Notes |
|--------|--------|-------|
| LightRAG ≥1.5 | **missing** (`No module named 'lightrag'`) | Not measured |
| Docling | **missing** | Not measured |
| rank_bm25 | **missing** | Not used |
| EE facade | present | `electrical_engineer.rag.retrieve` |

## Numbers (k=3, owned `ch1.md` “KVL around a loop.”)

| Query / filter | Hits | empty | precision@3 |
|----------------|------|-------|-------------|
| `book_id=own, chapter_id=1` | 1 | false | 1.0 (only in-filter file) |
| `book_id=own, chapter_id=99` | 0 | **true** | n/a (empty visible) |
| no inventory | 0 | **true** | n/a |

Citation metadata is owned by the facade (`book_id` / `chapter_id` / `folder_tag` / `domain_tag`). Passages never flip gates.

## Engine pick

**bm25** (thin file+filter facade). LightRAG 1.5 and Docling stay deferred until a licensed chapter can be ingested and the same table is re-run. Do not vendor RAG-Anything.

`docs/CANNOT_DO.md` already has CD-RAG-ANYTHING.
