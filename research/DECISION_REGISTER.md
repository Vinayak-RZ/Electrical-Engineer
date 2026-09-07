# Decision register

Stances for this research phase. Status: `open` | `leaning` | `proposed` | `deferred`.

| ID | Decision | Options | Stance | Decide-by phase | Notes |
|----|----------|---------|--------|-----------------|-------|
| D1 | Harness base | O1 Pi package · O2 Pi fork · O3 thin MCP+skills · O4 custom harness | open | Phase E | Evidence in `pi-feasibility.md`, scoring in `option-scoring.md` |
| D2 | Knowledge grounding | model priors · skills only · textbook RAG · fine-tune | leaning: **textbook RAG + skills + tool verification** | Phase B/E | Fine-tune parked |
| D3 | Corpus rights model | owned PDFs · library · OER · BYO-runtime | deferred: **BYO + OER default** | Phase B (CP-1) | No book text in repo |
| D4 | RAG insertion | MCP tools · context middleware · agentic multi-hop | open | Phase B | May combine |
| D5 | Primary verifier | MATLAB/Simulink · open-source stack · hybrid | leaning: **MATLAB primary, OSS fallback** | Phase C (CP-2) | |
| D6 | Distribution | sealed app first · works-with-other-agents first | proposed: **works-with-other-agents first** | Phase A | User direction |
| D7 | Capability framing | exam scores · task genres × verification | leaning: **task genres × verification** | Phase D | |
| D8 | Recommended build path | O1–O4 | open | Phase E | Output of synthesis |

## Sources

- Research plan and user direction — retrieved 2026-09-07 — reliability: primary
- `agentic-system-design` skill (RAG vs fine-tune default) — retrieved 2026-09-07 — reliability: primary

## Confidence

Overall confidence for this register: med

Stances marked `leaning` / `deferred` await note evidence and user CP-1/CP-2 confirmation.
