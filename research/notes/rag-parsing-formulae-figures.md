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
| **PyMuPDF (fitz)** | Fast text+blocks, positions, TOC/page maps | No real formula extraction; maths become pictures or broken linear text | Good geometry baseline |
| **Docling** | Layout + tables; typed document with page/bbox provenance (MIT) | Formula quality weaker than science-specialized stacks on dense math | Strong structure/provenance default |
| **MinerU** | Formulas → LaTeX; tables → HTML; multi-column / OCR path | Heavier stack; watch current licence terms | Strong LaTeX-emitting candidate |
| **Marker** | High-throughput Markdown/JSON; optional LLM cleanup | Formula fidelity without LLM pass is uneven; check model-weight terms | Throughput candidate |
| **Unstructured** | Element types include Formula/Table/FigureCaption | Formula typed but not a full LaTeX reconstructor | Useful pipeline glue |
| **VLM captioners** | Circuit/Bode figure descriptions | Costly; may invent topology | Optional secondary caption only |

Practical pipeline lean: **PyMuPDF for TOC/page maps → MinerU or Docling for body → keep page crops for figures.**

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
- [Docling paper](https://arxiv.org/abs/2408.09869) — retrieved 2026-09-07 — reliability: paper
- [MinerU paper](https://arxiv.org/abs/2409.18839) — retrieved 2026-09-07 — reliability: paper
- [PyMuPDF formula limitation discussion](https://github.com/pymupdf/pymupdf4llm/discussions/390) — retrieved 2026-09-07 — reliability: primary
- [agentic-system-design skill](.cursor/skills/agentic-system-design/SKILL.md) — retrieved 2026-09-07 — reliability: primary (S3)

## Confidence

Overall confidence for this note: med

Direction (layout + formula awareness) is high confidence; specific tool ranking needs a measured spike on real EE PDFs.
