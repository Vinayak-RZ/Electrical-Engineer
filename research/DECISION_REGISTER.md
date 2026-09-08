# Decision register

Stances for this research phase. Status: `open` | `leaning` | `proposed` | `deferred`.

| ID | Decision | Options | Stance | Decide-by phase | Notes |
|----|----------|---------|--------|-----------------|-------|
| D1 | Harness base | O1–O4 | **proposed: O1 hybrid** | Phase E | ADR-0001 |
| D2 | Knowledge grounding | priors / skills / RAG / fine-tune | **proposed: RAG + skills + tool verify** | Phase B/E | ADR-0002 |
| D3 | Corpus rights | owned / library / OER / BYO | **leaning: curator-licensed embedding packs + BYO** | CP-1 | Embeddings release ≠ PDF redistribute; still needs licence review |
| D4 | RAG insertion | MCP / middleware / multi-hop | **proposed: MCP + multi-hop skills** | Phase B | Local store behind MCP |
| D5 | Primary verifier | MATLAB / OSS / hybrid | **proposed: MATLAB primary, OSS fallback** | Phase C | ADR-0003; CP-2 |
| D6 | Distribution | sealed app / multi-agent | **proposed: local package + multi-host skills** | Phase A | Local-first install |
| D7 | Capability framing | exams / task genres | **proposed: task genres × verification** | Phase D | |
| D8 | Recommended build path | O1–O4 | **proposed: O1 (runner-up O3)** | Phase E | `synthesis/recommendation.md` |
| D9 | Vector store | Chroma / sqlite-vec / LanceDB | **leaning: Chroma default, sqlite-vec optional** | 2026-09-08 | `notes/local-package-and-embedding-release.md` |
| D10 | Circuit vision pipeline | VLM-only / structured detect+netlist / hybrid | **leaning: structured netlist + UI edit gate** | 2026-09-08 | `notes/photo-to-schematic-to-simulink.md` |
| D11 | Multimodal RAG engine | RAG-Anything / thin MinerU+MCP / commercial | **proposed: RAG-Anything behind MCP** | Spike gate | ADR-0004; `rag-stack-recommendation.md` |

## Sources

- `research/synthesis/recommendation.md` — retrieved 2026-09-07 — reliability: primary
- `DECISIONS.md` ADR seeds — retrieved 2026-09-07 — reliability: primary

## Confidence

Overall confidence for this register: high

`proposed` stances await your acceptance; `deferred` await CP-1/CP-2.
