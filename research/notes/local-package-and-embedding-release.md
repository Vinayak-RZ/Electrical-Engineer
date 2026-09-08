# Local package and GitHub embeddings release

## Purpose

Research a **fully local** Electrical-Engineer install path: a user-installed package/plugin that downloads a prebuilt textbook **embedding pack** from a GitHub Release into a local vector store (Chroma or similar), then answers EE questions offline (aside from optional MATLAB).

## Findings

Claim | Evidence (URL) | Confidence
--- | --- | ---
GitHub Releases allow binary assets; **each file must be under 2 GiB**; no limit on total release size or bandwidth | https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases | high
Embedded vector stores (no server) fit local agents: **sqlite-vec**, **Chroma**, **LanceDB** | https://dreaming.press/posts/sqlite-vec-vs-lancedb-vs-chroma-embedded-vector-store-solo-builder.html | high
sqlite-vec + FTS5 is strong for personal corpora &lt;~50–100k chunks (single file, hybrid BM25) | https://github.com/NousResearch/hermes-agent/issues/844 | med
Chroma is the fastest DX for Python RAG prototypes; LanceDB better when data outgrows RAM or needs versioning | https://dreaming.press/posts/chroma-vs-lancedb.html | med
Shipping **embeddings is not the same as shipping PDFs**, but it is **not automatically copyright-safe**; rights depend on what the publisher licence allows | copyright doctrine + prior corpus note stance | med
A local package that downloads a pinned Release asset at setup matches the user workflow (curated licensed books → embed offline → publish pack → install pulls pack) | this note’s architecture sketch | high

### Product shape (local-first)

```text
User machine
  ├── electrical-engineer package (Pi package / CLI / Cursor skill host)
  ├── local LLM runtime (optional: Ollama / llama.cpp) OR API key if user allows
  ├── local vector store (Chroma or sqlite-vec / LanceDB)
  ├── embedding pack (downloaded once from GitHub Release)
  └── MATLAB/Simulink MCP (optional; needs local licence) OR OSS SPICE fallback
```

Setup flow:

1. User installs the package (`pi install …` / `npm` / `pip` — exact host undecided).
2. Setup command downloads `ee-corpus-embeddings-vX.zip` from a **GitHub Release** (checksum verified).
3. Unpack into local store (Chroma collection or sqlite-vec DB).
4. Agent tools call `search_ee_corpus` against that local store only.

### Embedding-pack release design

| Concern | Recommendation |
|---------|----------------|
| What to ship | Chunk text (or hashed ids) + vectors + metadata (book, chapter, page, licence tag) — **not** original PDF binaries |
| Size | Split packs by domain (circuits / power / control / machines) so each asset stays &lt;2 GiB |
| Integrity | SHA-256 in release notes; setup refuses mismatch |
| Versioning | Semantic pack versions; agent records pack version in answers for reproducibility |
| Updates | `ee-corpus update` pulls newer Release; keep old pack until confirmed |

### Vector DB choice (local)

| Store | Best when | Caution |
|-------|-----------|---------|
| **Chroma** | Fastest to wire in Python; user asked for it; good up to memory-sized corpora | Directory-based; hybrid BM25 weaker natively |
| **sqlite-vec** | Single-file portability + FTS5 hybrid; undergrad-scale packs | Brute-force KNN ceiling |
| **LanceDB** | Larger packs, disk-based ANN, versioning | Slightly heavier mental model |

**Lean for v1 research stance:** support **Chroma as default** (matches user intent) with an optional **sqlite-vec** profile for single-file portability. Revisit LanceDB if packs exceed RAM.

### Rights and ethics (must stay explicit)

- You (the pack curator) must have licences that allow **creating and redistributing derived embedding indexes** of those books. Many textbook licences allow personal use but **forbid redistribution of content or derivatives** — embeddings can still be contested as derivatives.
- Safer packaging: release only packs built from books you clearly control; publish a **manifest of titles/editions** without shipping PDFs; document that end users are not receiving the books themselves.
- Keep OER/CC-BY material in a separate public seed pack if desired.

### Local models vs MATLAB

- “Entirely local” for **chat + RAG** ⇒ local LLM (Ollama etc.) + local embeddings + local vector DB.
- “Entirely local” for **Simulink sims** ⇒ local MATLAB licence still required; otherwise fall back to local ngspice/python-control (see open-source verification note).

## Open questions

- Exact package host (Pi package vs Cursor plugin vs standalone CLI) under a hard local-only constraint.
- Who hosts the Release repo (main Electrical-Engineer vs private corpus repo)?
- Embedding model choice (must ship the **same** model id used to build the pack, or pack is useless).
- Whether chunk **text** is included in the release (better RAG answers) or only vectors + opaque ids (weaker generation, slightly less content exposure).

## Sources

- [GitHub About releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases) — retrieved 2026-09-08 — reliability: primary
- [sqlite-vec vs LanceDB vs Chroma](https://dreaming.press/posts/sqlite-vec-vs-lancedb-vs-chroma-embedded-vector-store-solo-builder.html) — retrieved 2026-09-08 — reliability: secondary
- [Chroma vs LanceDB](https://dreaming.press/posts/chroma-vs-lancedb.html) — retrieved 2026-09-08 — reliability: secondary
- [Hermes knowledgebase RAG discussion](https://github.com/NousResearch/hermes-agent/issues/844) — retrieved 2026-09-08 — reliability: secondary
- [ee-corpus-and-licensing.md](ee-corpus-and-licensing.md) — retrieved 2026-09-08 — reliability: primary
- [pi-feasibility.md](pi-feasibility.md) — retrieved 2026-09-08 — reliability: primary

## Confidence

Overall confidence for this note: high

Architecture fit is clear. Copyright risk on redistributed embeddings remains medium until licence text for each book is reviewed.
