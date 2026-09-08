# Recommendation memo

## Purpose

Recommend what to build next for Electrical-Engineer after the research phase. This memo is **not** a product requirements document.

## Recommendation

**Primary path: O1 — Pi package-first hybrid, with O3 portability as the backbone, refined for local-first operation.**

Build (when a later implementation phase starts):

1. **Portable EE skill packs** (circuits, power, control, machines; tutor/co-solver/reviewer modes).
2. **Local textbook RAG**: curator builds embedding packs from licensed books; publish packs as **GitHub Release assets**; setup downloads into a **local vector store** (Chroma default; sqlite-vec optional). No commercial PDFs in git.
3. **Verification wiring** to MathWorks MATLAB/Simulink MCP when licensed, plus a documented OSS fallback (SPICE MCP, pandapower/python-control/sympy).
4. An optional **Pi package** that installs EE defaults, local RAG tools, and an MCP bridge — without hard-forking Pi.
5. **Circuit vision path**: photo/screenshot → draft netlist → **editable schematic UI** → Simulink (or ngspice) simulation only after user confirmation.

**Runner-up: O3 alone** (skills + MCP only, no Pi package) if Pi’s missing built-in MCP becomes a time sink.

**Not recommended now: O2 hard fork or O4 custom harness** — higher maintenance without improving RAG or MATLAB access.

## Why this path

- Matches the intended **fully local** install: package on the machine, embeddings on disk, vector DB local — only MATLAB remains licence-gated when used.
- Pi documents RAG via extensions and invites packages; a fork is unnecessary for the niche bet ([pi.dev](https://pi.dev/)).
- User priority is working with other agents; MCP + skills travel to Claude Code, Cursor, and Codex.
- MathWorks already ships MATLAB MCP toward those hosts.
- **Curated embedding Releases** (not PDF redistribution) fit the user’s licence-and-publish workflow; rights review per title remains mandatory.
- Photo → schematic needs a **UI edit gate**; Simulink is the preferred sim backend when present, with ngspice as local fallback.

## First spike list (later, only with explicit approval)

1. Stub local RAG MCP: load a tiny Chroma/sqlite-vec fixture; measure citation round-trip offline.
2. Prototype Release download + checksum into a local Chroma collection (empty or toy vectors).
3. Formula-preserving parse of **one owned** EE chapter (metrics only; no corpus commit).
4. MATLAB MCP smoke: evaluate a trivial expression if a licence exists; optional Linear Circuit Wizard / netlist path probe.
5. Photo → draft netlist → render-in-UI round-trip on **one clean textbook schematic** (no sim claim without edit).
6. Probe Pi MCP-via-extension path for package feasibility.

## Open questions (≥5)

1. Confirm textbook rights for **redistributing embedding packs** (owned titles + licence text review).
2. Confirm MATLAB/Simulink toolbox availability on your machines.
3. Is a branded CLI experience important enough to revisit a soft fork?
4. Local multimodal model for circuit photos, or allow optional cloud vision (conflicts with “entirely local”)?
5. Which SPICE MCP to standardize on for the OSS tier?
6. How large an initial gold-task set per GATE section?
7. Should PG/research-intern genres be first-class in the first implementation slice?
8. Embed chunk **text** in Release packs vs vectors + opaque ids only?

## What this memo does NOT decide

- Product requirements, personas-as-specs, or launch metrics.
- Exact tech stack versions or monorepo layout.
- Whether to train or fine-tune a model.
- Branding, pricing, or full standalone app UI (schematic UI is a research path, not a shipped product).
- Acceptance of ADR seeds (they remain `proposed` until you accept them).

## Confidence

Overall confidence for this memo: high

Falsifier: if extension/MCP packaging on Pi repeatedly fails, drop to pure O3; if you mandate a single branded binary, re-score O2; if embedding redistribution is legally blocked for the intended titles, fall back to BYO-only ingest on the user’s machine.

## Sources

- [option-scoring.md](option-scoring.md) — retrieved 2026-09-07 — reliability: primary
- [pi-feasibility.md](../notes/pi-feasibility.md) — retrieved 2026-09-07 — reliability: primary
- [rag-agent-integration.md](../notes/rag-agent-integration.md) — retrieved 2026-09-07 — reliability: primary
- [ee-corpus-and-licensing.md](../notes/ee-corpus-and-licensing.md) — retrieved 2026-09-07 — reliability: primary
- [matlab-simulink-surface.md](../notes/matlab-simulink-surface.md) — retrieved 2026-09-07 — reliability: primary
- [open-source-verification.md](../notes/open-source-verification.md) — retrieved 2026-09-07 — reliability: primary
- [ee-task-taxonomy-draft.md](../notes/ee-task-taxonomy-draft.md) — retrieved 2026-09-07 — reliability: primary
- [local-package-and-embedding-release.md](../notes/local-package-and-embedding-release.md) — retrieved 2026-09-08 — reliability: primary
- [photo-to-schematic-to-simulink.md](../notes/photo-to-schematic-to-simulink.md) — retrieved 2026-09-08 — reliability: primary
