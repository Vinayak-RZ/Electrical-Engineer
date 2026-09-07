# Option scoring (O1–O4)

## Purpose

Score four build paths for an electrical-engineering agentic system on fixed criteria, using evidence from WS-A–D notes.

## Scoring scale

1 = poor fit · 3 = acceptable · 5 = strong fit. Scores are research judgements, not commitments.

### Criteria

1. Time-to-insight (how fast we learn if the bet works)
2. Cross-agent reuse (Claude / Cursor / Codex / Pi)
3. RAG fit (textbook corpus)
4. Verification fit (MATLAB + OSS)
5. Maintenance cost (lower cost = higher score)
6. Differentiation
7. Licence risk (lower risk = higher score)
8. Exit cost if the bet fails (lower lock-in = higher score)

## Findings

### Options

| ID | Path |
|----|------|
| O1 | Pi **package** (extensions + skills) plus portable MCP servers |
| O2 | Pi **hard fork** branded as EE agent |
| O3 | **Thin meta-layer**: EE RAG MCP + skill packs only; no harness ownership |
| O4 | **Custom harness** greenfield |

### Matrix

| Criterion | O1 | O2 | O3 | O4 | One-line justification |
|-----------|----|----|----|----|------------------------|
| Time-to-insight | 5 | 2 | 5 | 1 | Packages/MCP spike fastest; fork/custom burn calendar on plumbing |
| Cross-agent reuse | 4 | 2 | 5 | 2 | O3 maximal; O1 still portable via MCP/skills; fork/custom trap users |
| RAG fit | 5 | 5 | 5 | 5 | All can host RAG; Pi documents context RAG; MCP works everywhere |
| Verification fit | 4 | 4 | 5 | 4 | Official MATLAB MCP already targets common hosts; Pi needs MCP bridge |
| Maintenance | 4 | 2 | 5 | 1 | Thin layer lightest; fork/custom track upstream forever |
| Differentiation | 3 | 5 | 2 | 4 | Fork gives brand CLI; thin layer looks like “just MCP” |
| Licence risk | 5 | 5 | 5 | 5 | Equal if BYO corpus; harness choice does not change book rights |
| Exit cost | 4 | 2 | 5 | 1 | Skills/MCP survive host change; custom dies with the repo |

**Totals:** O3 **37** · O1 **34** · O2 **27** · O4 **23**

### Interpretation

- **O3** wins on portability and maintenance but under-delivers a cohesive “Electrical Engineer agent” experience.
- **O1** is close behind and adds a Pi-native wiring story without owning a fork.
- **O2/O4** only win if branded single-binary UX outweighs maintenance — not supported by current evidence.

## Open questions

- Whether a light branded CLI wrapper over O3 (without forking Pi) closes the differentiation gap.
- User fork appetite may force O2 despite scores.

## Sources

- [pi-feasibility.md](../notes/pi-feasibility.md) — retrieved 2026-09-07 — reliability: primary
- [harness-landscape.md](../notes/harness-landscape.md) — retrieved 2026-09-07 — reliability: primary
- [rag-agent-integration.md](../notes/rag-agent-integration.md) — retrieved 2026-09-07 — reliability: primary
- [matlab-simulink-surface.md](../notes/matlab-simulink-surface.md) — retrieved 2026-09-07 — reliability: primary
- [ee-corpus-and-licensing.md](../notes/ee-corpus-and-licensing.md) — retrieved 2026-09-07 — reliability: primary

## Confidence

Overall confidence for this note: high

Relative ordering is stable under ±1 perturbations on differentiation; only a hard “must own the binary” constraint flips O2 above O1.
