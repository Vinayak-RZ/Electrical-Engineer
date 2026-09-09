# Project overview

## Purpose

**Electrical-Engineer** is an open-source workspace to design — and later build — an agent that can do undergraduate (then postgraduate) electrical-engineering work: solve assignment-style questions correctly, explain them, ingest circuit and control diagrams, and verify numbers with simulators rather than invent them.

The project is also an experiment: how far current AI can go on **core engineering** (not only software), and where it still fails.

## System overview (today)

Greenfield / research-complete. There is no shipped agent. Authority for “what to build” lives under [`research/`](research/). The human pitch and **success-bar capabilities** live at the top of [`README.md`](README.md). Internals map: [`docs/EXTENSIVE.md`](docs/EXTENSIVE.md).

## High-level architecture (intended, not implemented)

```
Student question / diagram
        ↓
Harness (portable skills + MCP, optional Pi package)
        ↓
Local textbook RAG (BYO / licensed embedding pack)
        ↓
Verifier (MATLAB/Simulink MCP preferred; SPICE/Python fallback)
        ↓
Explanation + evidence  |  or explicit refusal
```

Diagram ingest: vision → draft netlist → **student-edited schematic** → simulate.

## Constraints

- No commercial textbook PDFs in git.
- No fabricated simulation numbers.
- Open source; local-first path required.
- UG-bounded public promise; harder PG/limit-finding work is a later fork.
- Academic integrity is the institution’s policy; the product still shows work.

## Sources of truth

- Capabilities / vision: `README.md`
- Landscape research: `research/notes/ai-core-engineering-landscape.md`
- Build recommendation: `research/synthesis/recommendation.md`
- ADR seeds: `DECISIONS.md`
- Live phase status: `PROGRESS.md`
