# EE workflow catalog draft (human names)

## Purpose

Draft an **extensive**, student-readable named workflow catalog from the UG curriculum union and the task-genre taxonomy. Names are **not frozen**. Recipes are specified for architecture later; they are not implemented here.

## Findings

Claim | Evidence (URL or path) | Confidence
--- | --- | ---
Public bound is the **union of UG packs**, not GATE-only | `docs/curriculum-map.md` | high
Genres that cover real coursework: Solve, Derive, Design, Simulate, Review, Explain, Report | `research/notes/ee-task-taxonomy-draft.md` | high
Photo-to-sim is a **stub** in this architecture pass (C4 P1) | owner lock; `research/notes/photo-to-schematic-to-simulink.md` | high
Cross-cutting glue (unmatched co-solver, compose, eval, RAG cite) must exist or the hybrid router has nothing to fall through to | `docs/PRD.md` FR1, FR2, FR9 | high

### How to read an id

`kebab-case` id for CLI (`electrical-engineer run solve-circuit-problem`). **Title** is what a student should understand. **Pack** is the curriculum pack. **Genre** is the taxonomy. **v1** = specify fully in architecture after Q&A. **stub** = contract only.

### Cross-cutting recipes

| id | Title | Genre | Notes |
|----|-------|-------|-------|
| unmatched-cosolver | Answer an EE question (unchecked if not verified) | Solve / Explain | Hybrid fall-through; never silent invention |
| search-textbook | Look up a concept in my books | Explain | BYO RAG; citations |
| run-eval-task | Run a gold homework task | Eval | FR9 |
| compose-from-parts | Build a one-off workflow from allowed steps | Compose | Dynamic stitch; fail closed |
| list-workflows | List available workflows | Meta | CLI/MCP discovery |

### Circuits

| id | Title | Genre | Depth |
|----|-------|-------|-------|
| solve-circuit-problem | Solve a circuit homework problem | Solve | v1 |
| derive-circuit-identity | Derive a circuit result from laws | Derive | v1 |
| simulate-circuit-netlist | Simulate a netlist (SPICE) | Simulate | v1 |
| design-passive-network | Design a simple RLC network to spec | Design | v1 |
| review-circuit-solution | Find mistakes in a circuit solution | Review | v1 |
| explain-circuit-concept | Explain a circuit idea for a viva | Explain | v1 |
| write-circuits-lab-report | Structure a circuits lab report | Report | v1 |
| photo-to-circuit-netlist | Photo of a circuit to a draft netlist | Simulate | **stub** |

### Signals

| id | Title | Genre | Depth |
|----|-------|-------|-------|
| solve-signals-problem | Solve a signals-and-systems problem | Solve | v1 |
| derive-transform-step | Derive a Fourier or Laplace step | Derive | later |
| simulate-lti-system | Simulate an LTI system | Simulate | v1 |
| explain-signals-concept | Explain a signals idea | Explain | v1 |
| review-signals-solution | Find mistakes in a signals solution | Review | later |

### Electronics

| id | Title | Genre | Depth |
|----|-------|-------|-------|
| solve-electronics-problem | Solve an analog or digital electronics problem | Solve | v1 |
| simulate-electronics-netlist | Simulate an electronics netlist | Simulate | v1 |
| design-opamp-stage | Design a simple op-amp stage to spec | Design | later |
| explain-electronics-concept | Explain a devices or digital idea | Explain | v1 |
| review-electronics-solution | Find mistakes in an electronics solution | Review | later |

### Machines

| id | Title | Genre | Depth |
|----|-------|-------|-------|
| solve-machines-problem | Solve a machines or transformer problem | Solve | v1 |
| explain-oc-sc-test | Explain OC/SC tests and equivalent circuit | Explain | v1 |
| simulate-machine-start | Simulate a machine start-up (when a tool exists) | Simulate | later |
| write-machines-lab-report | Structure a machines lab report | Report | v1 |
| review-machines-solution | Find mistakes in a machines solution | Review | later |

### Power (study-level, not control-room)

| id | Title | Genre | Depth |
|----|-------|-------|-------|
| solve-power-problem | Solve a power-systems homework problem | Solve | v1 |
| simulate-load-flow | Run a study-level load flow | Simulate | v1 |
| explain-per-unit | Explain the per-unit system | Explain | v1 |
| review-power-model | Review a power-system model or solution | Review | later |
| explain-protection-study | Explain protection at study level (not live settings) | Explain | later |

### Control

| id | Title | Genre | Depth |
|----|-------|-------|-------|
| solve-control-problem | Solve a classical control problem | Solve | v1 |
| design-pid-gains | Choose PID or lead-lag gains to spec | Design | v1 |
| simulate-control-loop | Simulate a feedback loop | Simulate | v1 |
| explain-stability | Explain stability, Bode, or root locus | Explain | v1 |
| control-diagram-to-model | Block diagram or Bode figure to a model | Simulate | **stub** (after C4) |
| write-control-lab-report | Structure a control lab report | Report | v1 |

### Power electronics

| id | Title | Genre | Depth |
|----|-------|-------|-------|
| solve-power-electronics-problem | Solve a converter homework problem | Solve | v1 |
| simulate-converter | Simulate a basic converter | Simulate | later |
| explain-power-electronics | Explain a converter or drive-adjacent idea | Explain | v1 |

### Measurements, EM, maths

| id | Title | Genre | Depth |
|----|-------|-------|-------|
| solve-measurements-problem | Solve a measurements problem | Solve | later |
| explain-instrument | Explain an instrument or error model | Explain | later |
| solve-em-fields-problem | Solve an undergrad EM/fields problem | Solve | later |
| explain-em-fields | Explain a fields idea | Explain | later |
| solve-ee-maths | Solve maths-for-EE (ODE, Fourier, complex) | Solve | v1 |
| derive-ee-maths | Derive a maths-for-EE step | Derive | v1 |

### Shared node types (not student-facing recipes)

These are the **activities** recipes compose: `retrieve-passage`, `check-numeric`, `run-spice`, `run-python-control`, `run-matlab-if-present`, `ask-human`, `label-unchecked`, `write-run-summary`. Students invoke **titles** above, not node ids.

## Open questions

- Are titles + ids acceptable, or should titles be even shorter?
- Collapse per-pack `explain-*` into one `explain-ee-concept` with a pack flag?
- Which **v1** rows are truly first-slice vs catalog-complete-but-later (P1 pack order is circuits then control)?

## Sources

- [curriculum-map.md](../../docs/curriculum-map.md) — retrieved 2026-09-10 — reliability: primary
- [ee-task-taxonomy-draft.md](ee-task-taxonomy-draft.md) — retrieved 2026-09-10 — reliability: primary
- [photo-to-schematic-to-simulink.md](photo-to-schematic-to-simulink.md) — retrieved 2026-09-10 — reliability: primary
- [PRD.md](../../docs/PRD.md) — retrieved 2026-09-10 — reliability: primary

## Confidence

Overall confidence for this note: high that these packs and genres belong; medium that this exact id list is the one to freeze (owner will confirm at the Q&A gate).
