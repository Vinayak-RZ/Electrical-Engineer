# Chunking, metadata, and hybrid retrieval

## Purpose

Map retrieval design choices for EE textbooks once text is parsed: how to chunk, label, and search so symbols and worked examples survive.

## Findings

Claim | Evidence (URL) | Confidence
--- | --- | ---
Fixed-size token chunks sever methods from results in technical docs; structure-aware chunking is preferred | https://aclanthology.org/2026.rag4reports-1.4.pdf | high
Hybrid dense + lexical retrieval helps when queries and documents use different surface forms (acronyms, symbols) | https://www.redhat.com/en/resources/engineering-rag-enterprise-ebook | med
Parent–child (small chunks for recall, large parents for context) is a standard mitigation for context loss | common RAG engineering practice; data-engineering RAG literature | med

### Structure-aware chunk units (EE)

| Unit | Retrieve for | Keep together |
|------|--------------|---------------|
| Section | Concept definitions | Heading + prose + key equations |
| Worked example | Homework-like queries | Problem statement + solution steps |
| Theorem / identity box | Formula lookup | Statement + assumptions + variable definitions |
| Figure+caption | Diagram questions | Image ref + caption + nearby prose |

### Metadata schema (draft)

```text
doc_id, title, authors, edition, licence_tag,
domain_tag ∈ {circuits, machines, power, control, power_electronics, signals, em, measurements, other},
chapter, section, page_start, page_end,
chunk_type ∈ {prose, equation, example, figure, table},
prerequisite_ids[] (optional concept-graph edges)
```

### Hybrid retrieval

- **Dense** embeddings for semantic “explain synchronous reactance” queries.
- **BM25 / lexical** for `Ybus`, `SPWM`, `Routh-Hurwitz`, device part numbers, equation tags.
- Fuse with RRF or a cross-encoder rerank when latency allows.

### Concept-graph option (P1)

Nodes = EE concepts; edges = prerequisite / “used-in-example”. Helps multi-hop (“need phasors before power flow”). Treat as optional overlay, not v1 blocker.

### What we would measure later

Recall@k on section-anchored gold questions; citation page accuracy; formula-variant confusion rate.

## Open questions

- Embedding model choice (general vs code/math-specialized) for equation-heavy text.
- Whether per-domain sub-indices beat one global index.

## Sources

- [RAG4Reports technical-doc RAG](https://aclanthology.org/2026.rag4reports-1.4.pdf) — retrieved 2026-09-07 — reliability: paper (S16)
- [Engineering RAG for the enterprise](https://www.redhat.com/en/resources/engineering-rag-enterprise-ebook) — retrieved 2026-09-07 — reliability: vendor (S23)
- [agentic-system-design skill](.cursor/skills/agentic-system-design/SKILL.md) — retrieved 2026-09-07 — reliability: primary (S3)

## Confidence

Overall confidence for this note: med

Structure-aware + hybrid is well supported; exact schema fields will evolve during a later implementation phase.
