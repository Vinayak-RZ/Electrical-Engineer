# RAG–agent integration patterns

## Purpose

Decide how textbook retrieval should enter an agent loop relative to skills and numerical verification tools.

## Findings

Claim | Evidence (URL) | Confidence
--- | --- | ---
Agentic design separates context/RAG, tools, orchestrator, and guardrails | `.cursor/skills/agentic-system-design/SKILL.md` | high
Pi can implement RAG as **dynamic context** without forking | https://pi.dev/ | high
MCP is the portable tool surface for hosts that already speak MCP (Claude, Cursor, Codex, MATLAB’s own server) | https://github.com/matlab/matlab-mcp-server ; https://pi.dev/ | high
Harness survey notes coding agents rarely use vector retrieval for *code*; EE textbook RAG is a different corpus problem | https://arxiv.org/abs/2609.00006 | med

### Pattern options

| Pattern | How it works | Pros | Cons |
|---------|--------------|------|------|
| **A. MCP tools** | `search_ee_corpus`, `get_passage`, `cite` | Portable across hosts; explicit citations; auditable | Pi needs MCP extension; model must call tools |
| **B. Context middleware** | Harness injects top-k passages each turn | Works on Pi natively; lower tool friction | Less portable; harder to cite; prompt bloat |
| **C. Agentic multi-hop** | Plan: concept → example → verify numerically | Matches homework/research workflows | More steps, cost, failure points |

### Recommended combination (leaning)

1. **MCP tools as the portable core** (Pattern A) so Claude/Cursor/Codex/Pi-with-bridge share one RAG server.
2. Optional **Pi middleware** (Pattern B) as sugar for Pi-package users.
3. **Multi-hop policy in skills** (Pattern C): retrieve assumptions from books → compute/verify in MATLAB/Simulink → refuse fabricated “simulation” numbers.

### Division of labour

| Need | Source |
|------|--------|
| Definitions, assumptions, standard derivations, typical pitfalls | Textbook RAG |
| Idiomatic MATLAB/Simulink usage | MathWorks skills + MCP |
| Numeric answers, Bode data, load-flow results | MATLAB / Simulink / OSS sim |
| Pedagogy tone (tutor vs co-solver) | EE skill packs |

### Guardrails (from agentic-system-design)

- Max retrieval hops / tool calls per task.
- Citations required when a claim is attributed to a book.
- No silent tool failure; surface empty retrieval.
- Treat retrieved text as untrusted (prompt injection via PDF text).

### MCP-PENDING

Agent Patterns Catalog recipe IDs for “RAG + tool verifier” were not queryable in this environment; fill when MCP is available locally.

## Open questions

- Default top-k and rerank latency budget for interactive homework help.
- Whether citations should be mandatory in tutor mode or only co-solver mode.

## Sources

- [agentic-system-design](.cursor/skills/agentic-system-design/SKILL.md) — retrieved 2026-09-07 — reliability: primary (S3)
- [Pi Coding Agent](https://pi.dev/) — retrieved 2026-09-07 — reliability: primary (S4)
- [Harness Engineering](https://arxiv.org/abs/2609.00006) — retrieved 2026-09-07 — reliability: paper (S6)
- [MATLAB MCP Server](https://github.com/matlab/matlab-mcp-server) — retrieved 2026-09-07 — reliability: primary (S7)

## Confidence

Overall confidence for this note: high

Portable MCP + skill-level multi-hop matches both Pi’s extension model and the “works with other agents” goal.
