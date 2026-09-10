# Spatiotemporal composability for EE workflows (paradigm, not a harness fork)

## Purpose

Map DeepSeek Harness / Cordis **spatiotemporal composability** and Temporal **child-workflow vs activity** thinking onto Electrical Engineer’s H3 CLI — without adopting DSH, Cordis, or a Temporal cluster as the product runtime.

## Findings

Claim | Evidence (URL) | Confidence
--- | --- | ---
DeepSeek Harness (`dsh`) is an **everything-is-a-plugin** coding-agent harness on Cordis: models, tools, skills, sessions, sandboxes, loops, and UI are swappable plugins | https://deepseek.com/harness/en/ ; https://github.com/deepseek-ai/DeepSeek-Harness | high
Cordis composition is **spatial** (which plugins are mounted) and **temporal** (when they activate, unload, or intercept a turn). The paper that names the paradigm is *A Programming Paradigm for Spatiotemporal Composability* | https://arxiv.org/abs/2608.25512 ; https://deepseek-harness.github.io/deepseek-harness/en/reference/ | high
In DSH the **workflow seam is optional and is not the agent loop**. `ctx.workflowEngine` runs a model-written script that can spawn children; one engine per context; invalid meta is rejected before the script runs | https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/subsystems/workflow.md | high
DSH workflows are **dynamic scripts** (`parallel()` / `pipeline()` combinators plus `agent()` children), not a checked-in DAG catalog. Nested saved workflows are explicitly out of that seam | same workflow.md; package README “No saved or nested workflows” | high
Temporal’s modularity lesson: **Activities** = one external action (call a simulator). **Child workflows** = a composite with its own lifecycle. “When in doubt, use an Activity.” Do not use children just to organise code | https://docs.temporal.io/child-workflows ; https://docs.temporal.io/design-patterns/child-workflows | high
Forking DSH or running Cordis as Electrical Engineer would be **H4/H5** (owning a unique harness). PID/PRD already lock **H3**: thin CLI wrapping portable skills + tools | `docs/PID.md`; `docs/PRD.md` | high

### What to steal (paradigm)

| Idea | In DSH / Temporal | Local EE mapping (sketch, not locked) |
|-----|-------------------|----------------------------------------|
| Seam | Service definition + provider + consumer | `simulate` seam: ngspice **or** MATLAB behind one node id |
| Plugin in space | Swap a provider without rewriting the loop | Swap OSS vs MATLAB without a second CLI |
| Plugin in time | Intercept `tools/pre-execute`; unload a plugin | Gate plugin runs **before** a simulate node; allow-all unloads it for this run |
| Workflow ≠ loop | `ctx.workflowEngine` is optional | Hosts keep their loops; CLI runs a recipe |
| Activity vs child | Simulator call vs “photo then sim then explain” | **Node** = activity. **Named recipe** = small DAG of nodes. **Compose** = new recipe from allowlisted nodes |
| Fail closed | Invalid `meta` throws before run | Unknown node id or illegal edge is rejected before spice starts |

### What not to steal

- The DSH **agent loop**, session JSONL log, Electron UI, or TypeScript plugin tree.
- Model-written orchestration **scripts** as the only way to compose (H3 wants **named**, testable recipes students and evals can call).
- A Temporal **server**, workers, or event history. Durability here is a **run directory of files** (owner lock).

### Dynamic composition without a second harness

Three composition grades, all compatible with “predefined workflows plus stitch-at-runtime”:

1. **Catalog recipe** — checked-in DAG: `solve-circuit-homework` = retrieve → derive → simulate-if-needed → explain.
2. **Allowlisted stitch** — router emits a DAG whose node ids must exist in the registry; write that DAG into the run directory; runner executes it.
3. **DSH-style script** — model writes `pipeline(photo, simulate, explain)`. Powerful; hardest to eval; closest to a unique loop.

H3 bias: (1) and (2). Treat (3) as a later optional seam, like DSH treats workflow as optional — not the product identity.

## Open questions

- How strict is the stitch allowlist (any registered node vs typed ports so `simulate` cannot feed `ask-human` garbage)?
- Does “compose” write a one-shot DAG file, or only select a catalog recipe?
- Is a node allowed to call another recipe (Temporal child) or only other nodes (activities)?

## Sources

- [DeepSeek Harness developer preview](https://deepseek.com/harness/en/) — retrieved 2026-09-10 — reliability: vendor
- [deepseek-ai/DeepSeek-Harness](https://github.com/deepseek-ai/DeepSeek-Harness) — retrieved 2026-09-10 — reliability: primary
- [DSH architecture (Cordis plugins, seams, loop)](https://deepseek-harness.github.io/deepseek-harness/en/reference/) — retrieved 2026-09-10 — reliability: primary
- [DSH workflow subsystem](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/subsystems/workflow.md) — retrieved 2026-09-10 — reliability: primary
- [A Programming Paradigm for Spatiotemporal Composability](https://arxiv.org/abs/2608.25512) — retrieved 2026-09-10 — reliability: paper (HTML timed out; abstract/title confirmed via arXiv abs)
- [Temporal child workflows](https://docs.temporal.io/child-workflows) — retrieved 2026-09-10 — reliability: primary
- [Temporal child-workflow design pattern](https://docs.temporal.io/design-patterns/child-workflows) — retrieved 2026-09-10 — reliability: primary
- [PID](../../docs/PID.md) — retrieved 2026-09-10 — reliability: primary

## Confidence

Overall confidence for this note: high

DSH/Cordis docs are primary. The Cordis paper body was not fetched (timeout); the mapping to H3 is an engineering reading, not a claim that Electrical Engineer should run Cordis.
