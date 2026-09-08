# RAG-Anything: features, implementation, and EE fit

## Purpose

Evaluate [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) as a candidate for Electrical-Engineer textbook RAG. Answer whether it is the best option for mixed EE documents (prose, multi-column layout, tables, circuit figures, equations), how its features are actually implemented, and how it compares to alternatives already researched in this repo.

## Findings

Claim | Evidence (URL or ledger ID) | Confidence
--- | --- | ---
RAG-Anything is an all-in-one multimodal RAG library built on LightRAG, targeting PDFs that mix text, images, tables, and equations | https://github.com/HKUDS/RAG-Anything ; https://arxiv.org/abs/2510.12323 | high
Default parse path is MinerU; Docling and PaddleOCR are swappable backends | https://github.com/HKUDS/RAG-Anything/blob/main/README.md ; `raganything/parser.py` | high
Retrieval is LightRAG hybrid: vector similarity plus knowledge-graph traversal, with modality-aware ranking | https://arxiv.org/abs/2510.12323 §2.2–2.3 ; https://github.com/HKUDS/LightRAG | high
Paper reports 63.4% DocBench and 42.8% MMLongBench vs LightRAG 58.4% / 38.9%; multimodal subset on DocBench 76.3% vs LightRAG 59.7% | https://arxiv.org/abs/2510.12323 Tables 2–3 | high
Gains grow on long documents (DocBench 101+ pages: 68.2–68.8% vs MMGraphRAG ~55%) | https://arxiv.org/abs/2510.12323 §3.2 | high
Ablation: chunk-only 60.0%, no reranker 62.4%, full 63.4% — graph does most of the work | https://arxiv.org/abs/2510.12323 Table 4 | high
Library is MIT; depends on LightRAG (`lightrag-hku<1.5`) and `mineru[core]>=3.4.1` | https://github.com/HKUDS/RAG-Anything/blob/main/LICENSE ; https://github.com/HKUDS/RAG-Anything/blob/main/pyproject.toml | high
MinerU (required parse default) uses a custom Apache-2.0-based licence with attribution and huge-scale commercial thresholds | https://github.com/opendatalab/MinerU/blob/master/LICENSE.md | high
Official examples default to OpenAI GPT-4o / text-embedding-3-large; local Ollama/LM Studio/vLLM are supported but not the happy path | https://github.com/HKUDS/RAG-Anything/blob/main/examples/ollama_integration_example.py ; `env.example` | high
Official Ollama example **disables image processing** and uses chat + embed only | https://github.com/HKUDS/RAG-Anything/blob/main/examples/ollama_integration_example.py | high
Storage is LightRAG’s own KV/vector/graph files (optional Neo4j, Postgres, Milvus, Qdrant) — not the Chroma packs already planned here | https://github.com/HKUDS/RAG-Anything/blob/main/env.example ; `notes/local-package-and-embedding-release.md` | high
Benchmarks are academic / financial / legal DQA, not EE textbooks; no measured EE formula or circuit-schematic eval | https://arxiv.org/abs/2510.12323 §3 ; `notes/rag-eval-methodology.md` | high

### What it is (and is not)

RAG-Anything (PyPI `raganything`, v1.4.1 at research time) is a **Python library**, not a complete EE agent. It wraps:

1. A **document parser** (MinerU / Docling / PaddleOCR).
2. **Modality processors** that turn images, tables, and equations into text descriptions plus LightRAG entities.
3. **LightRAG** for chunking, entity/relation extraction, vector index, and hybrid query.
4. Optional **VLM-enhanced query** that re-attaches original images at generation time.

It does **not** provide MCP tools, EE citation policy, MATLAB/SPICE verification, GitHub Release pack download, or a Chroma-shaped runtime. Those remain Electrical-Engineer work.

### Main features and how they are implemented

Pipeline the README and paper agree on: **parse → categorize → modality analysis → dual knowledge graph → hybrid retrieve → synthesize**.

#### 1. Document parsing

**Feature.** High-fidelity extract of PDFs, Office files, and images into a typed `content_list`.

**Implementation.** `raganything/parser.py` (~125k) plus `mineru_content.py`. `RAGAnythingConfig.parser` selects `mineru` (default), `docling`, or `paddleocr`. MinerU emits blocks typed as text / image / table / equation with page index and local image paths. Office files need LibreOffice on PATH. Callers can skip parse entirely via `insert_content_list` (useful if we keep PyMuPDF TOC maps from the existing parse note).

This is the same MinerU/Docling lean already recorded in `rag-parsing-formulae-figures.md`. RAG-Anything is the orchestration, not a new parser.

#### 2. Adaptive content decomposition

**Feature.** Split a document into coherent units without flattening columns or merging sidebars into body text.

**Implementation.** Delegated to MinerU/Docling layout models. RAG-Anything then routes each typed block. Hierarchy is preserved as `belongs_to` edges later, not as a separate EE chapter/example schema.

#### 3. Visual content analyzer

**Feature.** Caption figures and extract spatial / hierarchical relations (panels, axes, legends).

**Implementation.** `raganything/modalprocessors.py` (`ImageModalProcessor`). A vision model (`vision_model_func`, GPT-4o in the README) receives the crop plus nearby context (`CONTEXT_WINDOW` / page mode from `docs/context_aware_processing.md`). Output is a retrieval-oriented description plus an entity summary. The original image is kept so VLM query can dereference it (`query.py`, paper §2.4).

Risk for EE: VLMs invent circuit topology. Existing stance still holds — treat figures as **searchable artifacts**, do not trust a caption as a netlist (`photo-to-schematic-to-simulink.md`).

#### 4. Structured data interpreter

**Feature.** Tables stay tables: headers, cells, units, trends.

**Implementation.** `TableModalProcessor` in `modalprocessors.py`. Table HTML/structure from the parser is passed to the LLM with a table-analysis prompt (`prompt.py` / paper Figure 8). Graph edges such as row-of / column-of / unit-of are the paper’s explanation for beating “table as paragraph” baselines (DocBench finance case).

This is the strongest match to EE machine-test tables and per-unit examples.

#### 5. Mathematical expression parser

**Feature.** Equations as LaTeX plus conceptual mapping.

**Implementation.** `EquationModalProcessor`. MinerU already emits LaTeX; the processor asks the LLM to explain variables, assumptions, and neighbouring formulae (`prompt.py` / paper Figure 9). `omml_extractor.py` handles Word OMML maths. Config flag: `enable_equation_processing`.

This is why the library is interesting for EE. It is still LLM interpretation on top of MinerU LaTeX — not a CAS, and not MATLAB.

#### 6. Dual-graph index (the core algorithm)

**Feature.** Multimodal knowledge graph + text knowledge graph, fused by entity name.

**Implementation (paper §2.2, code via LightRAG):**

- Non-text units become multimodal anchor nodes `v_j^mm`.
- An LLM writes a chunk description and an entity summary for each unit, using a local neighbourhood window δ.
- LightRAG extractor `R(·)` pulls intra-chunk entities/relations; each is linked with `belongs_to` to the multimodal anchor.
- Text chunks go through ordinary LightRAG GraphRAG-style NER + relations.
- Graphs merge on entity-name alignment.
- Dense embeddings are stored for entities, relations, and chunks → index I = (G, T).

This is **many LLM calls per page**. Quality tracks the extract model. GPT-4o-mini in the paper; a local 8B model will be cheaper and noisier.

#### 7. Hybrid / modality-aware retrieval

**Feature.** Combine graph hops with vector search; boost figures/tables/equations when the query says so.

**Implementation.** LightRAG modes (`naive`, `local`, `global`, `hybrid`) plus RAG-Anything ranking in `query.py`. Paper: structural candidate set C_stru (keyword → entity → neighbourhood) ∪ semantic top-k C_seman, then multi-signal fusion (graph importance, cosine, inferred modality). `aquery_with_multimodal` lets the user inject a table or LaTeX snippet as extra query context.

This is a stronger version of the hybrid dense+BM25 + optional concept-graph already sketched in `rag-chunking-and-retrieval.md`. It is **not** BM25 unless LightRAG/storage is configured for lexical search; the paper’s “structural” path is graph/keyword, not FTS5.

#### 8. VLM-enhanced query

**Feature.** After retrieval, feed original images into a vision model with the text context.

**Implementation.** `query.py` dereferences `img_path` for visual hits and calls `vision_model_func`. Disabled if no vision function is wired (the official Ollama example).

#### 9. Other features (lower EE priority)

| Feature | Implementation | EE need |
|---------|----------------|---------|
| Audio | `modalprocessors_audio.py` + faster-whisper | Low (lecture recordings later) |
| Video | scene detect + VLM + Whisper | Low |
| Batch folder ingest | `batch.py` / `batch_parser.py` | Useful for curator-side pack builds |
| Enhanced Markdown | `enhanced_markdown.py` | Nice-to-have export |
| Parser plugin registry | `register_parser` in `__init__.py` | Lets us keep PyMuPDF TOC |
| Offline tiktoken cache | `docs/offline_setup.md` | Required for air-gapped Release installs |

### Comparison (honest, not a feature tour)

| Option | Strength for EE textbooks | Weakness vs this project |
|--------|---------------------------|--------------------------|
| **RAG-Anything + LightRAG** | Best packaged multimodal ingest; equations/tables first-class; long-doc graph | Heavy LLM extract; LightRAG store ≠ Chroma packs; no MCP/verify; local VLM optional |
| **Custom parse + Chroma packs (current plan)** | Matches GitHub Release + local-first already accepted; thin runtime | We own formula/table wiring; no dual-graph unless we add it |
| **Docling / MinerU alone + LlamaIndex** | Modular; easier to emit our metadata schema | More assembly; weaker out-of-box graph |
| **ColPali / ColQwen (page-as-image)** | Strong on circuit drawings without OCR | Weak symbolic equation search; GPU; hard to ship as text+vector Release packs |
| **RAGFlow** | Productized layout RAG | Heavier app, less library-shaped, licence/ops cost |
| **LightRAG text-only** | Lighter graph RAG | Paper itself shows it loses ~16 points on multimodal DocBench |

### Fit verdict

RAG-Anything is the **best off-the-shelf library for the document type** (mixed technical PDFs). It is **not** the best *product architecture* if we swallow it whole: that would discard the GitHub Release → local Chroma → MCP design already proposed, and it would ship a GPU-ish ingest stack to every student laptop.

**Recommended use:** curator-side (and optional BYO-ingest) engine. Export structure-aware chunks — and only then embeddings — into the planned Release packs. Keep LightRAG graph as an optional P1 overlay, not the v1 runtime. Full local-run mapping is in `rag-anything-local-releases.md`. Stack choice is in `synthesis/rag-stack-recommendation.md`.

### Failure modes the paper already admits (relevant to EE)

- Text-centric retrieval bias even when the query asks for a figure (Appendix A.5).
- Rigid spatial scan; merged-cell tables still fail all methods.
- VLMs can misread panel/axis structure.

Add EE-specific failures from `rag-eval-methodology.md`: wrong formula variant, dropped assumptions, unit slip. Those are **not** measured on DocBench.

## Open questions

- How much of the paper’s graph gain survives a local 8B extract model on one owned EE chapter.
- Whether we export LightRAG working_dir snapshots as a Release asset, or only Chroma/sqlite-vec packs.
- Docling-default vs MinerU-default for CPU-only curator machines.

## Sources

- [RAG-Anything repository](https://github.com/HKUDS/RAG-Anything) — retrieved 2026-09-08 — reliability: primary
- [RAG-Anything technical report (arXiv:2510.12323)](https://arxiv.org/abs/2510.12323) — retrieved 2026-09-08 — reliability: paper
- [RAG-Anything pyproject.toml](https://github.com/HKUDS/RAG-Anything/blob/main/pyproject.toml) — retrieved 2026-09-08 — reliability: primary
- [RAG-Anything MIT licence](https://github.com/HKUDS/RAG-Anything/blob/main/LICENSE) — retrieved 2026-09-08 — reliability: primary
- [Ollama integration example](https://github.com/HKUDS/RAG-Anything/blob/main/examples/ollama_integration_example.py) — retrieved 2026-09-08 — reliability: primary
- [offline_setup.md](https://github.com/HKUDS/RAG-Anything/blob/main/docs/offline_setup.md) — retrieved 2026-09-08 — reliability: primary
- [env.example](https://github.com/HKUDS/RAG-Anything/blob/main/env.example) — retrieved 2026-09-08 — reliability: primary
- [MinerU Open Source License](https://github.com/opendatalab/MinerU/blob/master/LICENSE.md) — retrieved 2026-09-08 — reliability: primary
- [LightRAG](https://github.com/HKUDS/LightRAG) — retrieved 2026-09-08 — reliability: primary
- [rag-parsing-formulae-figures.md](rag-parsing-formulae-figures.md) — retrieved 2026-09-08 — reliability: primary
- [rag-chunking-and-retrieval.md](rag-chunking-and-retrieval.md) — retrieved 2026-09-08 — reliability: primary
- [local-package-and-embedding-release.md](local-package-and-embedding-release.md) — retrieved 2026-09-08 — reliability: primary
- [agentic-system-design](../../.cursor/skills/agentic-system-design/SKILL.md) — retrieved 2026-09-08 — reliability: primary (S3)

## Confidence

Overall confidence for this note: high

Repository layout, licences, and paper tables are primary sources. EE-specific quality is unmeasured until a later owned-chapter spike; that is the main thing that would lower or raise the ingest-layer recommendation.
