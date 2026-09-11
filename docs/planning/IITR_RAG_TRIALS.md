# IITR RAG + explain trials (2026-09-11)

Seed: Kuphaldt *Lessons in Electric Circuits* Vol I excerpts (CC-BY) under `eval/fixtures/oer/`.

| # | Scenario | Result | Evidence |
|---|----------|--------|----------|
| 1 | Syllabus scan → catalog | **PASS** NEP PCC EEC-* + 2022 suggested books | `research/notes/iitr-ee-book-catalog.md` |
| 2 | Retrieve Ohm's-law query (values changed 24 V / 8 Ω) | **PASS** top hit `kuphaldt-dc` chapter 2 | `tests/unit/test_rag_oer_seed.py`; `eval --pack rag-retrieval` |
| 3 | Retrieve KVL / divider query | **PASS** top hit chapter 6 | same |
| 4 | Wrong chapter filter | **PASS** `empty: true` | `chapter_id=99` |
| 5 | `explain-circuits` perturbed Ohm | **PASS** `value=3.0` and citation ch 2 | `eval/gold/rag-retrieval/ohms-perturbed` |
| 6 | `explain-circuits` KVL viva (no numeric) | **PASS** token `unchecked`, citation ch 6 | `eval/gold/explain/kvl-viva` |
| 7 | Unmatched numeric without verifier | **PASS** `unchecked` (existing gold) | `eval/gold/unmatched/open-ended-01` |
| 8 | Injection cannot flip `unchecked` | **PASS** | `eval/gold/injection/flip-gates-01` |

No commercial PDFs in git. Remaining IITR titles: [`docs/rag-byo.md`](../rag-byo.md).
