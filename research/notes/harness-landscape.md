# Harness landscape comparison

## Purpose

Compare production coding-agent harnesses as candidate bases for an electrical-engineering specialist that must work with other agents, host textbook RAG, and attach MATLAB/Simulink verification.

## Findings

Claim | Evidence (URL) | Confidence
--- | --- | ---
A coding agent is a **model plus a harness**: loop, tools, context, safety, orchestration, extensions | https://arxiv.org/abs/2609.00006 | high
Across eleven studied harnesses, runtimes use **hand-rolled async loops**; none imported a general-purpose agent framework | https://arxiv.org/abs/2609.00006 | high
Skills lead MCP in adoption in that sample (9/11 vs 8/11) | https://arxiv.org/abs/2609.00006 | med
Pi is a **minimal** harness: extensions, skills, prompt templates, themes; packages via npm or git | https://pi.dev/ | high
Pi ships **without** built-in MCP, sub-agents, plan mode, permission popups, or todos — those are extension/package territory | https://pi.dev/ | high
Pi **explicitly documents RAG** as an extension use-case: inject messages, filter history, implement RAG or long-term memory | https://pi.dev/ | high
Pi modes: interactive, print/JSON, RPC, SDK — embeddable | https://pi.dev/ | high
Pi is MIT-licensed and designed to be modified (Earendil / open source) | https://composio.dev/content/pi-agent-vs-codex | med
Codex is a fuller product: sandbox, cloud, SDK, app-server; less “reshape the harness yourself” | https://composio.dev/content/pi-agent-vs-codex | med
Skill formats are converging across Pi / Claude Code / Codex (`AGENTS.md`, skills directories) | https://composio.dev/content/pi-agent-vs-codex | med

### Comparison matrix

| Dimension | Pi | Codex CLI | Claude Code | OpenHands | Aider |
|-----------|----|-----------|-------------|-----------|-------|
| Licence / openness | MIT; designed to customize | Open-source core (Rust) + product surface | Product; skills/MCP extensible | Open source | Open source |
| Extension model | TypeScript extensions + packages | SDK / app-server / config | Skills + MCP + plugins | Plugin/runtime APIs | Mostly CLI flags + conventions |
| Built-in MCP | **No** (add via extension) | Yes | Yes | Yes (typical) | Limited / external |
| Skills | Yes; on-demand progressive disclosure | Yes (shared skill direction) | Yes | Varies | Light |
| Context hooks for RAG | **Documented** (dynamic context extensions) | Via app integration / tools | Via MCP tools + skills | Tools / memory plugins | Repo map + chat; not RAG-first |
| Subagents | Not built-in; packages/extensions | Product feature | Product feature | Multi-agent workflows | Single-agent focus |
| Best fit for EE specialist | Strong if we own package(s) | Strong if we stay inside OpenAI product | Strong as *consumer* of our MCP/skills | Heavier platform | Too thin for domain RAG+lab |

### Seven canonical subsystems (survey)

Loop · tools · context management · safety · orchestration · extension surfaces · (plus telemetry/evals in practice). For EE, the critical insertion points are **context** (textbook RAG) and **tools** (MATLAB MCP / simulators).

## Open questions

- Exact maintenance cost of a third-party MCP extension for Pi vs using Claude/Cursor as the host and treating Pi as optional.
- Whether shared skill directories are enough for EE pedagogy modes without harness-level UX.

## Sources

- [Harness Engineering arXiv 2609.00006](https://arxiv.org/abs/2609.00006) — retrieved 2026-09-07 — reliability: paper (ledger S6)
- [Pi Coding Agent](https://pi.dev/) — retrieved 2026-09-07 — reliability: primary (S4)
- [Pi vs Codex (Composio)](https://composio.dev/content/pi-agent-vs-codex) — retrieved 2026-09-07 — reliability: secondary (S5)
- [MATLAB MCP Server](https://github.com/matlab/matlab-mcp-server) — retrieved 2026-09-07 — reliability: primary (S7)

## Confidence

Overall confidence for this note: high

Primary docs and a large empirical survey agree on Pi’s minimalism and extension-first RAG path. Product details for Codex/Claude evolve quickly; matrix cells for those products are medium confidence.
