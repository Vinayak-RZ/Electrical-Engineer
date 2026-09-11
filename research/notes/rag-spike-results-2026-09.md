# RAG spike results (2026-09-11)

Protocol: [`rag-spike-2026-09.md`](rag-spike-2026-09.md). Licence-clean Kuphaldt DC excerpts (CC-BY), not a commercial book.

## Environment

| Engine | Import | Notes |
|--------|--------|-------|
| LightRAG ≥1.5 | **missing** (`No module named 'lightrag'`) | Not measured |
| Docling | **missing** | Not measured |
| rank_bm25 | unused | Token-overlap stand-in in `retrieve.py` |
| EE facade | present | `electrical_engineer.rag.retrieve` |

## Numbers (k=3, Kuphaldt Vol I seed)

| Query / filter | Top hit | empty | precision@1 |
|----------------|---------|-------|-------------|
| Ohm's law / voltage current resistance, `book_id=kuphaldt-dc` | chapter 2 | false | 1.0 |
| Kirchhoff Voltage Law / divider, `book_id=kuphaldt-dc` | chapter 6 | false | 1.0 |
| `book_id=kuphaldt-dc, chapter_id=99` | none | **true** | n/a |
| Perturbed numeric 24 V / 8 Ω via `explain-circuits` | ch 2 + `value=3.0` | false | 1.0 |

Citation metadata is owned by the facade (`book_id` / `chapter_id` / `page`). Passages never flip gates.

## Engine pick

**bm25** (token overlap + filters). LightRAG 1.5 and Docling stay deferred until those packages are in the env. Do not vendor RAG-Anything.

`docs/CANNOT_DO.md` already has CD-RAG-ANYTHING.
