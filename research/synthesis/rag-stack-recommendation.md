# RAG stack recommendation (RAG-Anything decision)

## Purpose

Decide whether Electrical-Engineer should adopt [RAG-Anything](https://github.com/HKUDS/RAG-Anything) as its RAG system, given mixed EE documents and the local GitHub Release + Chroma path already proposed. This memo is **not** a product requirements document.

## Recommendation

**Adopt RAG-Anything as the curator-side (and optional BYO) ingest + multimodal enrichment library. Do not adopt it as the entire runtime.**

Keep the already-proposed product spine:

1. Curator (or user BYO) runs layout-aware ingest.
2. Publish **embedding packs** as GitHub Release assets (no PDFs in git).
3. Local package downloads packs into **Chroma** (sqlite-vec optional).
4. Agent hosts call **MCP** tools (`search_ee_corpus`, `get_passage`, `cite`).
5. Numbers still go to MATLAB/Simulink or OSS sim — never to the RAG library.

What RAG-Anything replaces in that spine: the vague “MinerU or Docling then we invent processors” gap. What it does **not** replace: Release packaging, Chroma, MCP, citations, or verification.

**Runner-up if RAG-Anything’s LightRAG extract is too costly locally:** keep MinerU/Docling parse + our structure-aware chunks, skip the dual-graph until a measured spike says the graph is worth the LLM bill.

**Not recommended:** replace the local pack runtime with a full LightRAG `working_dir` on every laptop; ColPali-only retrieval; RAGFlow-as-the-product.

## Why this is not “just use the all-in-one”

The document type *is* RAG-Anything’s target: interleaved text, figures, tables, equations, long PDFs. The paper’s multimodal and long-doc gains are real (DocBench overall 63.4% vs LightRAG 58.4%; multimodal subset 76.3% vs 59.7%; 101+ page gap vs MMGraphRAG about 13 points). That answers “is this class of system the right idea?” — **yes**.

It does **not** answer “should this repo become a RAG-Anything app?” Three project constraints say no:

- **Local GitHub Release runtime** is already specified as Chroma/sqlite-vec packs (`local-package-and-embedding-release.md`). LightRAG’s store is a different artifact.
- **Portable MCP + skills** is the harness bet (ADR-0001 / D4). RAG-Anything is a Python `aquery` API.
- **EE correctness** still needs formula-variant eval and a simulator. RAG-Anything synthesizes answers; it does not verify them.

Ponytail read: take the library for the hard parse/enrichment, keep the thin local query path we already designed.

## Trade-off: library vs whole stack

**Decision:** Where RAG-Anything sits.

**Option A:** Whole-stack — LightRAG store + `aquery` is the product RAG.
Pros: fastest path to multimodal query; one vendor brain.
Cons: abandons Chroma packs; ships heavy ingest deps to every user; graph extract quality locked to a large LLM; weaker MCP story.

**Option B:** Ingest-layer — RAG-Anything builds `content_list` + captions/LaTeX; we export packs.
Pros: preserves local-first Release design; query path stays small; we own citations/metadata.
Cons: we write an exporter; lose query-time dual-graph unless we add it later.

**Default:** Option B because PRIORITY = SIMPLICITY + CONSISTENCY with D9/Q16.

**Override:** Set PRIORITY = QUALITY and accept LightRAG-on-disk if a later owned-chapter spike shows the graph is mandatory and pack export drops too much.

## Alternatives (short)

| Option | When it would win |
|--------|-------------------|
| Custom Docling/MinerU only | If RAG-Anything pins or licences become painful |
| ColPali / page-as-image | If circuit *drawings* dominate and we drop symbolic equation search |
| RAGFlow | If we wanted a hosted document UI more than a library |
| LightRAG text-only | If the corpus were plain markdown (it is not) |

MCP-PENDING: Agent Patterns Catalog was not queryable here; no catalog recipe id is claimed.

## First spike list (later, only with explicit approval)

1. Ingest **one owned** EE chapter through RAG-Anything (MinerU, equations on, images off) with local Ollama; score equation/table/page survival vs Docling-only.
2. Export that chapter to a toy Chroma fixture; confirm MCP citation round-trip still works.
3. Repeat with images on + a local VLM; measure caption hallucination on one circuit figure (no netlist claim).

## What this memo does NOT decide

- Product requirements or launch metrics.
- Exact model names/versions to pin in a Release.
- Whether chunk text is included in public packs (still a rights question).
- Acceptance of ADR seeds (they stay `proposed` until you accept them).

## Confidence

Overall confidence for this memo: high

Falsifier: if the owned-chapter spike shows MinerU+processors add nothing over Docling chunks, drop back to parse-only. If embedding-pack rights fail, BYO ingest can still use RAG-Anything on the user’s machine only.

## Sources

- [rag-anything-evaluation.md](../notes/rag-anything-evaluation.md) — retrieved 2026-09-08 — reliability: primary
- [rag-anything-local-releases.md](../notes/rag-anything-local-releases.md) — retrieved 2026-09-08 — reliability: primary
- [local-package-and-embedding-release.md](../notes/local-package-and-embedding-release.md) — retrieved 2026-09-08 — reliability: primary
- [recommendation.md](recommendation.md) — retrieved 2026-09-08 — reliability: primary
- [RAG-Anything paper](https://arxiv.org/abs/2510.12323) — retrieved 2026-09-08 — reliability: paper
- [system-design-tradeoffs skill](../../.cursor/skills/system-design-tradeoffs/SKILL.md) — retrieved 2026-09-08 — reliability: primary
