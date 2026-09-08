# Running RAG-Anything locally on the GitHub Release path

## Purpose

Map how RAG-Anything can run **entirely on the user’s machine** without contradicting the already-researched install: package on disk, embedding packs from a GitHub Release, local vector store (Chroma default), MCP tools, optional local LLM.

## Findings

Claim | Evidence (URL or ledger ID) | Confidence
--- | --- | ---
RAG-Anything can bind LLM, vision, and embeddings to Ollama, LM Studio, or vLLM instead of OpenAI | https://github.com/HKUDS/RAG-Anything/blob/main/env.example ; examples/ollama_integration_example.py ; examples/lmstudio_integration_example.py ; docs/vllm_integration.md | high
Ollama chat can use the OpenAI-compatible `/v1` helper; embeddings should use Ollama’s native `/api/embed` | https://github.com/HKUDS/RAG-Anything/blob/main/examples/ollama_integration_example.py | high
Fully offline LightRAG init still needs a local `tiktoken` cache (`TIKTOKEN_CACHE_DIR`) | https://github.com/HKUDS/RAG-Anything/blob/main/docs/offline_setup.md | high
MinerU weights download on first parse unless pre-cached; first-run needs network or a vendor cache in the Release | https://github.com/HKUDS/RAG-Anything/blob/main/README.md (MinerU model source) | high
GitHub Release assets must stay under 2 GiB each | https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases | high
Planned EE runtime is **Chroma (or sqlite-vec) packs**, not LightRAG’s default file store | `notes/local-package-and-embedding-release.md` | high
Shipping LightRAG `working_dir` as a Release is possible but couples every client to LightRAG versions and extract-model IDs | LightRAG persistence + this note’s architecture | med

### Two local profiles (do not mix casually)

The GitHub Release idea and RAG-Anything’s native store are different products. Treat them as two profiles.

```text
Profile A — runtime (what students/users run)
  package install
    → download ee-corpus-embeddings-vX.zip (SHA-256)
    → load Chroma / sqlite-vec
    → MCP search_ee_corpus / get_passage / cite
    → optional Ollama chat
    → MATLAB/SPICE verify (unchanged)

Profile B — curator / BYO ingest (what builds packs, or indexes a user’s own PDFs)
  RAG-Anything + MinerU/Docling
    → local Ollama (chat + embed + optional VLM)
    → typed content_list (text / table / equation / figure)
    → export chunks + metadata + vectors
    → zip domain packs for GitHub Release
    → optional LightRAG graph kept only on the curator machine
```

**Default product path remains Profile A.** Profile B is how we *make* packs and how BYO-PDF ingest can work on a machine that can afford MinerU.

### Local model wiring (Profile B)

Official Ollama example (defaults):

| Role | Suggested local model | Notes |
|------|------------------------|-------|
| Chat / graph extract | `llama3.2` or a stronger 8B+ instruct | Graph quality is the ceiling; small models invent entities |
| Embeddings | `nomic-embed-text` (768-d) or `bge-m3` (1024-d, `env.example`) | **Must match** the id used to build and consume a pack |
| Vision | Not enabled in the official Ollama sample | For figures: Qwen2.5-VL / Llama 3.2 Vision / MiniCPM-V via LM Studio or Ollama |

`env.example` already documents `LLM_BINDING=ollama` and `EMBEDDING_BINDING=ollama`. For a GitHub-release-friendly laptop, prefer:

- CPU-only curator: `parser=docling`, equations on, images **off** (captions = figure caption text only).
- GPU curator: `parser=mineru`, equations on, images on with a local VLM.

That matches the official Ollama example turning `enable_image_processing=False` — they already treat local vision as optional.

### Offline / air-gap checklist

Needed **before** the machine leaves the network (or bundled as extra Release assets, each &lt;2 GiB):

1. `tiktoken_cache/` via `scripts/create_tiktoken_cache.py` (`docs/offline_setup.md`).
2. MinerU / Docling model weights (Hugging Face cache or MinerU’s documented model source).
3. Ollama models pulled once (`ollama pull …`) or GGUF files for llama.cpp / LM Studio.
4. Embedding model files identical to the pack’s `model_id`.
5. Python wheels if pip is blocked (optional vendor wheelhouse).

None of these belong in git. They belong in **separate Release assets** or a documented first-run download with checksums.

### How RAG-Anything fits the existing Release design

| Planned EE piece | RAG-Anything native | Recommended join |
|------------------|---------------------|------------------|
| GitHub Release zip | LightRAG `working_dir` directory | **Export** chunks+vectors+metadata to the planned zip; do not ship raw `working_dir` in v1 |
| Chroma default | LightRAG nano/file or Milvus/Qdrant/PG | Adapter at export time; runtime stays Chroma/sqlite-vec |
| Hybrid BM25 + dense | Graph + dense (lexical is secondary) | Keep BM25/FTS5 at runtime; graph is curator-side or P1 |
| MCP tools | Python `aquery` API | Thin MCP wrapper around the **store**, not around the whole library |
| BYO PDF | `process_document_complete` | Call RAG-Anything only in ingest mode |
| Citations (book, chapter, page) | `page_idx` on content_list items | Map into existing metadata schema (`doc_id`, `chapter`, `page_start`, `chunk_type`) |
| MATLAB verify | None | Keep outside RAG entirely |

### What a Release pack should contain if we use RAG-Anything to build it

Reuse the previous pack table; add fields RAG-Anything already emits:

- `chunk_id`, `doc_id`, `title`, `licence_tag`, `domain_tag`
- `chapter` / `section` if we can recover them (PyMuPDF TOC overlay — parser plugin)
- `page_start`, `page_idx`
- `chunk_type` ∈ {prose, equation, example, figure, table}
- `latex` when type is equation
- `img_relpath` optional (figures as **separate** image assets, or omit to shrink the zip)
- `text` (generation context) — still a rights question (see open questions on the local-pack note)
- `embedding` vector + `embedding_model_id` + `embedding_dim`
- `pack_version`

**Do not** put original PDFs in the zip. **Do not** put MinerU weights in the same zip as book chunks (size + licence clarity).

### Hardware reality (local-first)

| Machine | Realistic Profile B | Realistic Profile A |
|---------|---------------------|---------------------|
| 16 GB RAM, CPU only | Docling + small embed + no VLM; graph extract will be slow | Chroma query + 8B Ollama chat is plausible |
| 16–24 GB + modest GPU | MinerU + 8B extract + optional 3B–7B VLM | Same as above; no ingest needed |
| Curator workstation | Full MinerU + stronger extract/VLM to **build** packs | N/A |

“Entirely local” for **query** does not require RAG-Anything on the query path. “Entirely local” for **BYO ingest** does.

### Licence notes for a shipped package

- RAG-Anything: MIT.
- LightRAG: confirm current MIT-family terms at pin time (`lightrag-hku<1.5`).
- MinerU: Apache-2.0 **plus** extra terms (online-service attribution; separate commercial licence only above 100M MAU or USD 20M monthly revenue). Fine for this project’s scale; still attribute if we ever offer a hosted ingest.
- Docling: MIT — cleaner default if MinerU extras become awkward.
- Embedding/VLM weights: each model’s own terms (often research-only or use-restricted). Pin and document.

## Open questions

- Host of the Release repo (this repo vs a private corpus repo) — still open from the local-pack note.
- Whether figure **images** ship in the pack or only captions (size vs circuit-figure utility).
- Minimum local extract model that does not trash equation entities.

## Sources

- [local-package-and-embedding-release.md](local-package-and-embedding-release.md) — retrieved 2026-09-08 — reliability: primary
- [RAG-Anything env.example](https://github.com/HKUDS/RAG-Anything/blob/main/env.example) — retrieved 2026-09-08 — reliability: primary
- [Ollama integration example](https://github.com/HKUDS/RAG-Anything/blob/main/examples/ollama_integration_example.py) — retrieved 2026-09-08 — reliability: primary
- [LM Studio integration example](https://github.com/HKUDS/RAG-Anything/blob/main/examples/lmstudio_integration_example.py) — retrieved 2026-09-08 — reliability: primary
- [vLLM integration doc](https://github.com/HKUDS/RAG-Anything/blob/main/docs/vllm_integration.md) — retrieved 2026-09-08 — reliability: primary
- [offline_setup.md](https://github.com/HKUDS/RAG-Anything/blob/main/docs/offline_setup.md) — retrieved 2026-09-08 — reliability: primary
- [GitHub About releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases) — retrieved 2026-09-08 — reliability: primary (S33)
- [MinerU Open Source License](https://github.com/opendatalab/MinerU/blob/master/LICENSE.md) — retrieved 2026-09-08 — reliability: primary
- [agentic-system-design](../../.cursor/skills/agentic-system-design/SKILL.md) — retrieved 2026-09-08 — reliability: primary (S3)

## Confidence

Overall confidence for this note: high

Local bindings and the 2 GiB Release limit are documented. The export-adapter (LightRAG store → Chroma zip) is a design join, not a shipped tool; a later spike would confirm it is boring rather than heroic.
