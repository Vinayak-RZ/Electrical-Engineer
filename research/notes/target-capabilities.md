# Target capabilities — what “success” means

## Purpose

Define the capability set that would qualify **Electrical-Engineer** as a successful open-source project: an agentic harness that helps UG/PG electrical engineering students with reliable, explainable, verifiable work — and honestly explores how far current AI can go in core engineering.

## Findings

### North star

> **Behave like a strong undergraduate electrical engineer** — grounded in standard curricula (GATE EE, IIT/NIT, MIT/Berkeley/ETH-aligned topics), honest about assumptions, and **never presenting unverified numbers as facts**.

Secondary mission: **document the frontier** — publish what works, what fails, and how verification changes outcomes (open evals, not marketing claims).

### Audience and product tiers

| Tier | Audience | Intent |
|------|----------|--------|
| **UG core (v1)** | B.Tech / BE students; GATE aspirants; lab partners | Homework, tutorials, exam-style problems, schematic help |
| **PG stretch** | M.Tech researchers; design projects | Deeper design, parametric studies, literature-aware drafts |
| **Bounded fork** | Frozen UG feature set for classrooms | Stable, syllabus-aligned helper separate from experimental mainline |

### Capability pillars

#### 1. Solve — correct answers with verification

| Capability | Success signal | Verification |
|------------|----------------|--------------|
| Numeric problems (circuits, power, control, machines) | Answer matches gold within tolerance | SPICE, MATLAB, python-control, sympy, hand-checkable steps |
| Symbolic derivations | Required lemmas and final form present | Symbolic CAS + rubric |
| Multi-step exam questions | Consistent units, stated assumptions | Tool + rubric |

**Bar:** For checkable tasks, **no tool run → no numeric claim**.

#### 2. Explain — teach, not just answer

| Capability | Success signal |
|------------|----------------|
| Concept explanations | Correct assumptions; links to standard identities or retrieved textbook passages |
| Step-by-step solutions | Method matches problem type (e.g. mesh vs nodal, per-unit vs phase) |
| Socratic mode (optional) | Guides without dumping final answer when configured for learning |
| “Why wrong?” review | Identifies errors in student work with cited reasoning |

**Bar:** Explanations cite **source or derivation**; hallucinated formulae fail eval.

#### 3. Assignments and coursework

| Capability | Success signal |
|------------|----------------|
| End-to-end assignment help | Problem understanding → approach → verified result → structured write-up |
| Lab reports (structure) | Procedure, plots, discussion sections; numbers from actual runs |
| GATE-style section coverage | All ten GATE EE sections represented in eval set (depth varies) |
| Design problems | Meets stated specs; documents trade-offs |

**Bar:** Assignments are **assistive** — academic-integrity modes configurable; project does not optimize for undetectable cheating.

#### 4. Diagrams — circuits and control

| Capability | Success signal |
|------------|----------------|
| Ingest circuit schematics (photo, PDF, screen) | Draft netlist or editable schematic with labeled components |
| Ingest control block diagrams | Structured model (e.g. Simulink-ready) after user review |
| Edit gate | User confirms or corrects before simulation |
| Simulate from diagram | Transient, AC, DC, Bode, load flow (domain-appropriate) |
| Export | SPICE netlist, Simulink model, or open equivalent |

**Bar:** Raw vision output is **never** trusted for grades or safety-critical numbers without human confirmation and tool verification.

#### 5. Simulate and design

| Capability | Success signal |
|------------|----------------|
| Build and run models | MATLAB/Simulink when licensed; ngspice/LTspice/OpenEMT/python fallbacks |
| Controller design | Meets spec (margins, settling, overshoot) when simulated |
| Power / machines studies | Plausible results vs textbook benchmarks |
| Compare alternatives | States trade-offs with simulated evidence |

#### 6. Grounding — textbook and standards awareness

| Capability | Success signal |
|------------|----------------|
| Local RAG from user-owned or licensed packs | Retrieved passages support claims |
| BYO PDFs | User supplies books they have rights to use |
| No pirate corpora | Legal posture documented |

#### 7. Reliability and trust (cross-cutting)

| Principle | Implementation |
|-----------|----------------|
| Verify before present | Tool-gated numerics |
| Show provenance | Citations, simulation logs, assumption lists |
| Admit uncertainty | “Cannot verify” beats confident wrong |
| Human checkpoint | Irreversible or high-stakes steps need approval |
| Eval-driven claims | Capability claims tied to public or reproducible benchmarks |

### Task genres (from taxonomy)

All capabilities map to genres in `ee-task-taxonomy-draft.md`:

**Solve · Derive · Design · Simulate · Review · Explain · Report**

Priority domains for early depth: **circuits, power systems, control, machines**.

### What success looks like — project-level checklist

The project is **successful** when a student (or evaluator) can routinely:

1. **Ask** an EE question from coursework or GATE prep and get a **verified** answer with a **clear explanation**.
2. **Upload** a circuit or block diagram, **correct** the draft in a simple editor, and **run** a simulation whose outputs match expectations.
3. **Complete** a multi-part assignment with tool-checked numbers and a coherent report structure.
4. **Trust** that numbers came from simulators/solvers, not model memory.
5. **See** published eval results (pass/fail on gold tasks) — including known failure modes.

### Explicit non-goals (v1)

- Professional sign-off (licensed PE work, grid operations, safety certification).
- Autonomous hardware fabrication or live lab equipment control without human supervision.
- Redistributed copyrighted textbooks.
- Claiming “100% of all EE problems” without eval scope.

### PG / research stretch (post-UG fork)

- Parametric Simulink studies, literature triage, experiment-design drafts.
- EngDesign-style multi-hour design tasks with simulation grading.
- Analog/power PCB flows with physics-aware layout feedback.

## Open questions

- Weighting: exam-prep accuracy vs conceptual teaching quality in scoring?
- Minimum eval size per GATE section?
- Academic-integrity defaults for institutional deploy?

## Sources

- [ee-task-taxonomy-draft.md](ee-task-taxonomy-draft.md) — retrieved 2026-09-08 — reliability: primary
- [capability-eval-design.md](capability-eval-design.md) — retrieved 2026-09-08 — reliability: primary
- [ai-core-engineering-landscape.md](ai-core-engineering-landscape.md) — retrieved 2026-09-08 — reliability: primary
- [EngDesign benchmark](https://agi4engineering.github.io/Eng-Design/) — retrieved 2026-09-08 — reliability: paper
- [CircuitSense benchmark](https://arxiv.org/html/2509.22339) — retrieved 2026-09-08 — reliability: paper

## Confidence

Overall confidence for this note: **high** for framing; **med** for exact pass bars (thresholds deliberately deferred to eval harness work).
