# PDF parsing, formulae, and figures for EE RAG

## Purpose

Identify how to extract EE textbooks without destroying equations, multi-column layout, tables, or circuit figures.

## Findings

Claim | Evidence (URL) | Confidence
--- | --- | ---
Technical-doc RAG fails when PDFs are flattened; layout-aware and formula-aware parsing matter | https://aclanthology.org/2026.rag4reports-1.4.pdf | high
Enterprise RAG guidance stresses multimodal/layout reality (figures, tables, not “text only”) | https://www.redhat.com/en/resources/engineering-rag-enterprise-ebook | med
EE PDFs uniquely stress **equations**, **phasor/circuit diagrams**, and **worked numerical examples** spanning pages | domain reasoning; OpenFOAM-style technical RAG analogy | med

### Tool comparison (≥4)

| Tool | Strength | Weakness for EE | Notes |
|------|----------|-----------------|-------|
| **PyMuPDF (fitz)** | Fast text+blocks, positions | Formulae often become broken Unicode; limited structure | Good baseline / coordinates |
| **Marker** | Formula-preserving markdown-oriented parse (cited in technical RAG work) | Heavier; quality varies by PDF producer | Strong candidate for books |
| **Docling** | Structured doc conversion, tables | Need EE-specific eval | Emerging stack |
| **Unstructured** | Broad connectors, element types | Easy to over-chunk; maths uneven | Useful for pipelines |
| **Nougat / VLM captioners** | Math/figure understanding | Costly; may hallucinate glyphs | Optional second pass for figures |

### Formula strategies

1. Prefer parsers that emit **LaTeX or MathML** when possible.
2. If only images of equations exist, store **image + optional VLM caption**, never pretend OCR certainty.
3. Keep **surrounding sentence context** with each formula chunk (assumptions live in prose).

### Figures and tables

- Link figure image ↔ caption ↔ nearest section heading.
- Circuit schematics: treat as **visual artifacts** with caption text searchable; do not invent netlists from drawings in v1 research scope.
- Tables (machine test data, per-unit examples): preserve as tables, not paragraph soup.

### Failure modes

- Two-column pages read in wrong order.
- Sidebars merged into main narrative.
- Minus signs / overbars lost in OCR.
- Example “Solution” separated from problem statement by a page break.

## Open questions

- Head-to-head Marker vs Docling on one legally owned EE chapter (Phase S spike candidate).
- Whether VLM captioning is worth cost for circuit figures vs caption-only search.

## Sources

- [Decompose, Retrieve, Cite (RAG4Reports)](https://aclanthology.org/2026.rag4reports-1.4.pdf) — retrieved 2026-09-07 — reliability: paper (S16)
- [Engineering RAG for the enterprise (Red Hat)](https://www.redhat.com/en/resources/engineering-rag-enterprise-ebook) — retrieved 2026-09-07 — reliability: vendor (S23)
- [agentic-system-design skill](.cursor/skills/agentic-system-design/SKILL.md) — retrieved 2026-09-07 — reliability: primary (S3)

## Confidence

Overall confidence for this note: med

Direction (layout + formula awareness) is high confidence; specific tool ranking needs a measured spike on real EE PDFs.
