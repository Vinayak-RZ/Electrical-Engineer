# Capability evaluation design

## Purpose

Propose *how* to measure progress toward an undergrad-capable EE agent — rubrics and splits only. No launch thresholds, no PRD requirements.

## Findings

Claim | Evidence (URL) | Confidence
--- | --- | ---
Agentic systems need golden tasks and adversarial cases before user-facing claims | `.cursor/skills/agentic-system-design/SKILL.md` | high
Some EE work is **checkable** (numeric, simulate) and some is **judgement** (explanation quality, lab narrative) | `ee-task-taxonomy-draft.md` | high
OpenAI-style “research intern” framing emphasises well-scoped multi-hour tasks under human direction, not autonomous PI work | public OpenAI research-intern discussions (secondary) | med

### Rubric options (pick later)

| Rubric | Scores | Best for |
|--------|--------|----------|
| R1 Verified numeric | Pass if tool-checked answer matches gold within tol | Solve/Simulate |
| R2 Derivation checklist | Required intermediate lemmas present | Derive |
| R3 Citation-grounded explain | Claims tied to retrieved passages or standard identities | Explain + RAG |
| R4 Design constraints | Meets stated specs; states assumptions | Design |
| R5 Review catch-rate | Finds seeded bugs in flawed solutions | Review |
| R6 Process / intern | Plan→act→verify with human checkpoints logged | Long-horizon |

### Verified vs judgement split

| Class | Examples | Scoring |
|-------|----------|---------|
| Verified | Load-flow voltages, Bode margins, SPICE node voltages | Automatic via MATLAB/OSS tools |
| Hybrid | Compensator design | Spec check auto; elegance human/judge |
| Judgement | Conceptual explanations, lab report clarity | Rubric + optional LLM-judge with citations |

### Research-intern step framing (stretch)

Map long tasks to Decide → Design → Build → Run → Analyze → Communicate. Evaluate whether the agent stops for human input on irreversible changes and whether “Run” actually called a simulator.

### Does not decide

- Accuracy percentages or launch bars.
- Which model vendor to require.
- Whether PG topics are in scope for v1 product.

## Open questions

- Inter-rater reliability if faculty score judgement tasks.
- How to weight RAG citation failures vs numeric failures.

## Sources

- [agentic-system-design](.cursor/skills/agentic-system-design/SKILL.md) — retrieved 2026-09-07 — reliability: primary (S3)
- [ee-task-taxonomy-draft.md](ee-task-taxonomy-draft.md) — retrieved 2026-09-07 — reliability: primary
- [rag-eval-methodology.md](rag-eval-methodology.md) — retrieved 2026-09-07 — reliability: primary

## Confidence

Overall confidence for this note: high

Enough structure to build an eval harness later; thresholds remain explicitly out of scope.
