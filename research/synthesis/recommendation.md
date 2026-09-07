# Recommendation memo

## Purpose

Recommend what to build next for Electrical-Engineer after the research phase. This memo is **not** a product requirements document.

## Recommendation

**Primary path: O1 — Pi package-first hybrid, with O3 portability as the backbone.**

Build (when a later implementation phase starts):

1. **Portable EE skill packs** (circuits, power, control, machines; tutor/co-solver/reviewer modes).
2. **EE textbook RAG as an MCP server** with BYO-PDF (+ optional OER), structure-aware chunking, hybrid retrieval, and citations.
3. **Verification wiring** to MathWorks MATLAB/Simulink MCP when licensed, plus a documented OSS fallback (SPICE MCP, pandapower/python-control/sympy).
4. An optional **Pi package** that installs EE defaults, RAG context helpers, and an MCP bridge — without hard-forking Pi.

**Runner-up: O3 alone** (skills + MCP only, no Pi package) if Pi’s missing built-in MCP becomes a time sink.

**Not recommended now: O2 hard fork or O4 custom harness** — higher maintenance without improving RAG or MATLAB access.

## Why this path

- Pi documents RAG via extensions and invites packages; a fork is unnecessary for the niche bet ([pi.dev](https://pi.dev/)).
- User priority is working with other agents; MCP + skills travel to Claude Code, Cursor, and Codex.
- MathWorks already ships MATLAB MCP toward those hosts.
- BYO textbook corpus avoids redistributing commercial PDFs.

## First spike list (later, only with explicit approval)

1. Attach a stub RAG MCP tool to Claude/Cursor; measure citation round-trip.
2. Formula-preserving parse of **one owned** EE chapter (metrics only; no corpus commit).
3. MATLAB MCP smoke: evaluate a trivial expression if a licence exists.
4. Probe Pi MCP-via-extension path for package feasibility.

## Open questions (≥5)

1. Confirm textbook rights model beyond BYO default (owned titles list?).
2. Confirm MATLAB/Simulink toolbox availability on your machines.
3. Is a branded CLI experience important enough to revisit a soft fork?
4. Local/offline embeddings required for privacy, or API-hosted fine?
5. Which SPICE MCP to standardize on for the OSS tier?
6. How large an initial gold-task set per GATE section?
7. Should PG/research-intern genres be first-class in the first implementation slice?

## What this memo does NOT decide

- Product requirements, personas-as-specs, or launch metrics.
- Exact tech stack versions or monorepo layout.
- Whether to train or fine-tune a model.
- Branding, pricing, or standalone app UI.
- Acceptance of ADR seeds (they remain `proposed` until you accept them).

## Confidence

Overall confidence for this memo: high

Falsifier: if extension/MCP packaging on Pi repeatedly fails, drop to pure O3; if you mandate a single branded binary, re-score O2.

## Sources

- [option-scoring.md](option-scoring.md) — retrieved 2026-09-07 — reliability: primary
- [pi-feasibility.md](../notes/pi-feasibility.md) — retrieved 2026-09-07 — reliability: primary
- [rag-agent-integration.md](../notes/rag-agent-integration.md) — retrieved 2026-09-07 — reliability: primary
- [ee-corpus-and-licensing.md](../notes/ee-corpus-and-licensing.md) — retrieved 2026-09-07 — reliability: primary
- [matlab-simulink-surface.md](../notes/matlab-simulink-surface.md) — retrieved 2026-09-07 — reliability: primary
- [open-source-verification.md](../notes/open-source-verification.md) — retrieved 2026-09-07 — reliability: primary
- [ee-task-taxonomy-draft.md](../notes/ee-task-taxonomy-draft.md) — retrieved 2026-09-07 — reliability: primary
