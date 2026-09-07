# Pi feasibility — package vs fork vs hybrid

## Purpose

Answer whether Electrical-Engineer should ship as a **Pi package**, a **Pi fork**, a **hybrid**, or abandon Pi as the primary base.

## Findings

Claim | Evidence (URL) | Confidence
--- | --- | ---
Pi’s product thesis is “adapt Pi to your workflows” via extensions and packages, not fork-first | https://pi.dev/ | high
RAG is a **first-class documented extension pattern** (inject/filter context each turn) | https://pi.dev/ | high
Extension hooks for RAG without forking: `before_agent_start`, `context`, `session_before_compact`, plus `registerTool` | https://pi.dev/docs/latest/extensions | high
Existence proofs: community packages already ship RAG/context (`pi-mega-compact`, `pi-context-loader`) | https://pi.dev/packages/pi-mega-compact | high
MCP is **intentionally omitted** from core; community adapters exist (e.g. `pi-mcp-adapter`) | https://pi.dev/ ; https://pi.dev/packages/pi-mcp-adapter | high
Skills follow Agent Skills (`SKILL.md`); Pi can point at `~/.claude/skills` and `~/.codex/skills` | https://pi.dev/docs/latest/skills | high
Sub-agents are omitted from core; community packages spawn child `pi` processes | https://pi.dev/ | high
Four embed surfaces (interactive / print / RPC / SDK) support “works with others” | https://pi.dev/ | high
Forking buys default EE constitution and UX but pays ongoing merge cost against Earendil upstream | https://pi.dev/ + https://arxiv.org/abs/2609.00006 | med
A pure fork is unnecessary if EE value lives in **skills + RAG MCP/extension + MATLAB tooling** that other hosts can also load | https://pi.dev/ ; https://composio.dev/content/pi-agent-vs-codex | med

### Package / Fork / Hybrid scoring (qualitative)

| Criterion | Package | Soft fork | Hard fork |
|-----------|---------|-----------|-----------|
| Time to first useful EE agent | Best | Medium | Worst |
| Cross-agent reuse (Claude/Cursor/Codex) | Best if skills/MCP portable | Medium | Worst |
| RAG fit | Good (extension) | Good | Good |
| MATLAB MCP fit | Needs MCP extension on Pi; native on Claude/Cursor | Same | Same |
| Maintenance | Best | Medium | Worst |
| Differentiation / control | Medium | High | Highest |
| Exit cost if Pi stagnates | Low (skills/MCP remain) | Medium | High |

### Stance

**Hybrid leaning Package-first (recommended direction for synthesis):**

1. Ship **EE skill packs** + an **EE textbook RAG MCP server** + documented MATLAB/Simulink MCP wiring that work on **Claude Code / Cursor / Codex** (and on Pi once an MCP extension is installed or we publish one).
2. Optionally publish a **Pi package** that wires extensions (RAG context injection, MCP bridge, EE defaults) for users who want `pi install …`.
3. **Do not hard-fork Pi** unless package/extension APIs cannot enforce EE verification policy (refuse unverified numeric claims) or context injection proves insufficient.

### Three strongest reasons

1. Pi documents RAG via extensions — the niche bet does not require owning the harness binary.
2. User priority is “works with other agents”; portable MCP + skills beat a sealed fork.
3. MATLAB already ships an official MCP server aimed at Claude/Codex/VS Code — host-agnostic tools amplify that.

### Two strongest objections

1. Pi’s lack of built-in MCP adds a bridge we must build or depend on; Claude/Cursor may be smoother day-one hosts.
2. Soft product identity (“Electrical Engineer agent”) is harder when users install pieces into three different hosts — a fork gives a single branded CLI.

### What would change our mind (falsifiers)

- Extension API cannot inject retrieval results reliably before tool calls → revisit soft fork.
- Upstream Pi rejects or breaks package APIs quarterly → fork or abandon Pi.
- User insists on a single branded binary UX above portability → soft fork becomes acceptable.

## Open questions

- Is there already a maintained community MCP extension for Pi we should prefer over writing one?
- How stable is the TypeScript extension API across Pi releases?

## Sources

- [Pi Coding Agent](https://pi.dev/) — retrieved 2026-09-07 — reliability: primary (S4)
- [Pi Extensions docs](https://pi.dev/docs/latest/extensions) — retrieved 2026-09-07 — reliability: primary
- [Pi Skills docs](https://pi.dev/docs/latest/skills) — retrieved 2026-09-07 — reliability: primary
- [pi-mcp-adapter](https://pi.dev/packages/pi-mcp-adapter) — retrieved 2026-09-07 — reliability: primary
- [pi-mega-compact](https://pi.dev/packages/pi-mega-compact) — retrieved 2026-09-07 — reliability: primary
- [Pi vs Codex](https://composio.dev/content/pi-agent-vs-codex) — retrieved 2026-09-07 — reliability: secondary (S5)
- [Harness Engineering](https://arxiv.org/abs/2609.00006) — retrieved 2026-09-07 — reliability: paper (S6)
- [MATLAB MCP Server](https://github.com/matlab/matlab-mcp-server) — retrieved 2026-09-07 — reliability: primary (S7)

## Confidence

Overall confidence for this note: high

The package-first hybrid stance follows directly from Pi’s published architecture. Remaining uncertainty is operational (MCP-on-Pi packaging), not conceptual.
