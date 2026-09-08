# AI in core engineering — landscape and opportunity

## Purpose

Survey how AI (especially LLMs and agentic systems) is reshaping **core engineering** — electrical, mechanical, civil, manufacturing — with emphasis on electrical engineering, student impact (UG/PG, India and global), reliability constraints, and where an open-source undergrad EE agent can contribute.

## Findings

### Why core engineering lags software AI (but is accelerating)

Claim | Evidence | Confidence
--- | --- | ---
Physical engineering adoption trails software because mistakes have physical cost (safety, liability, recall), not just a bad deploy | [MITTR / LTTS report](https://wp.technologyreview.com/wp-content/uploads/2026/03/MITTR-Insights_LTTS_Report_March26.pdf); [Agentic AI in Engineering and Manufacturing (arXiv:2604.09633)](https://arxiv.org/pdf/2604.09633) | high
Industry interviews (30+ orgs) find adoption blocked more by **fragmented data, legacy CAD/CAE/EDA lock-in, auditability requirements** than raw model IQ | [arXiv:2604.09633](https://arxiv.org/pdf/2604.09633) | high
SimScale 2025 survey: ~97% expect AI productivity gains, but only ~3% report achieving them — expectation–execution gap | [State of Engineering AI 2025](https://explore.simscale.com/hubfs/resources/reports/state-of-engineering-ai-2025.pdf) | med
Winning pattern: **LLM for intent + deterministic tools for truth** (simulation, SPICE, FEA, code-checkers), human checkpoint on irreversible steps | [AEC Magazine civil agents](https://aecmag.com/features/ai-agents-for-civil-engineers/); [Harness as an Asset / CAAF (arXiv:2604.2604.17025)](https://doi.org/10.48550/arxiv.2604.17025) | high

**Implication for Electrical-Engineer:** reliability is not a nice-to-have — it is the product. Numeric answers must be tool-verified; diagrams must pass edit gates before simulation; explanations must cite sources or show derivations.

### Electrical engineering — where AI is working today (2025–2026)

| Area | What works | Representative work | Maturity |
|------|------------|---------------------|----------|
| **Circuit Q&A & tutoring** | Socratic dialogue + SPICE-in-the-loop; topology-aware retrieval beats plain text RAG | [AITEE](https://arxiv.org/html/2505.21582), [ElectroSage](https://github.com/EmminiX/ElectroSage) | early production / research |
| **Schematic image → netlist** | Hybrid CV + OCR + VLM + multi-agent correction; 84–96% connectivity on benchmarks | [SINA](https://arxiv.org/html/2601.22114), [PCBnet](https://arxiv.org/html/2608.27923) | research → pilot |
| **Circuit understanding benchmarks** | Perception strong (~85%+); symbolic derivation from diagrams weak (<19% on hard tasks) | [CircuitSense](https://arxiv.org/html/2509.22339), [OmniSch](https://arxiv.org/html/2604.00270v1) | benchmark stage |
| **Analog / power circuit design agents** | Multi-agent + SPICE loops; novel topologies but physics-layout gaps remain | [AaLLM](https://arxiv.org/html/2608.13472), [Power Circuit AI](https://doi.org/10.1109/idcd69431.2026.11519438) | research |
| **RF / PCB end-to-end** | Frontier LLM agents driving CST, ADS, KiCad from spec with engineer review | [Prompt to Prototype RF (arXiv:2608.31006)](https://arxiv.org/abs/2608.31006) | research demo |
| **Control / Simulink** | MCP tools for model read/edit/test; agentic control design workflows | [Simulink Agentic Toolkit](https://github.com/simulink/simulink-agentic-toolkit), [MATLAB Agentic AI](https://www.mathworks.com/products/matlab/agentic-ai.html) | vendor production |
| **EDA industry** | Copilots + autonomous agents for RTL, verification, PCB (Siemens Fuse, Synopsys.ai, Cadence) | [EDA AI market study](https://www.marknteladvisors.com/research-library/united-states-electronic-design-automation-ai-market-study.html) | commercial scale |
| **Open verification stack** | ngspice/LTspice MCP, power-system EMT MCP, Python MNA | [SPICEBridge](https://github.com/clanker-lover/spicebridge), [ltspice-mcp](https://pypi.org/project/ltspice-mcp/), [OpenEMT](https://github.com/h-d-engineer/OpenEMT) | OSS emerging |

### Cross-domain engineering AI (context for “core engineering”)

Claim | Evidence | Confidence
--- | --- | ---
**EngDesign** (NeurIPS 2025 Datasets track): 101 simulation-graded design tasks across 9 engineering domains including control, analog IC, signal processing — shifts eval from text matching to functional verification | [EngDesign](https://agi4engineering.github.io/Eng-Design/), [arXiv:2509.16204](https://arxiv.org/html/2509.16204v2) | high
**Engineering.ai**: hierarchical multi-agent “chief engineer” coordinating CFD, FEA, acoustics, optimization — weeks → hours on UAV wing study | [arXiv:2511.00122](https://arxiv.org/pdf/2511.00122) | med
Mechanical/manufacturing agents in production: CAD review, simulation setup, workflow orchestration (CoLab, SimScale, Synera) | [SimuTecra ME agents](https://simutecra.com/blogs/ai-agents-in-mechanical-engineering-beyond-prompt-engineering); [Colab design agents](https://www.colabsoftware.com/post/ai-agents-for-engineering-design-real-examples-capabilities-and-how-to-evaluate-them) | med
Civil: truss-from-image agents + validated structural solvers; building-code search | [AEC Magazine](https://aecmag.com/features/ai-agents-for-civil-engineers/) | med

EE sits in a **sweet spot** among core disciplines: rich open simulation (SPICE, control toolboxes), structured diagrams (schematics, block diagrams), and heavy exam/coursework demand — but still needs the same verify-before-trust harness as mechanical or civil.

### Student impact — India and global

Claim | Evidence | Confidence
--- | --- | ---
Indian UG expectations are well-bounded by **GATE EE** (10 technical sections) and IIT/NIT curricula — good eval scaffold | [GATE EE syllabus](https://static.collegedekho.com/media/uploads/2024/07/01/gate-_ee_2025_syllabus.pdf); `ee-task-taxonomy-draft.md` | high
GATE-prep and EE tutoring prototypes exist (Gemini tutors, question banks, Socratic platforms) but rarely combine **verified simulation + textbook grounding + diagram ingest** in one OSS harness | [BreakiT GATE](https://github.com/GaneshArihanth/BreakiT-Gate_Prep_Assistant); AITEE; ElectroSage | med
Global EE curricula (MIT, Berkeley, ETH) align on circuits, signals, machines, power, control — same task genres (solve, derive, design, simulate, explain) | `ee-task-taxonomy-draft.md` | high
**Opportunity:** a reliable, local-first, OSS EE agent could democratize what today requires expensive tutoring + MATLAB licences + hours on Piazza/Discord — especially where faculty bandwidth is thin.

### Why few builders focus on core engineering AI

1. **Data and tool fragmentation** — EDA/CAE files are proprietary; APIs are new or gated.
2. **Verification tax** — every answer needs a simulator or symbolic check; pure chat products skip this.
3. **Liability and trust** — bridges, grids, and power electronics do not tolerate hallucinated numbers.
4. **Smaller TAM narrative** — VC and OSS attention flow to code agents; EE looks “niche” until EDA giants and benchmarks (EngDesign, CircuitSense) prove otherwise.
5. **Multimodal hardness** — schematics and block diagrams need spatial + symbolic reasoning; benchmarks show large perception/reasoning gap.

This is exactly why an **open, eval-driven** project matters: publish what works, what fails, and how verification changes the curve.

### Reliability patterns that transfer to Electrical-Engineer

| Pattern | Description | Repo alignment |
|---------|-------------|----------------|
| **Tool-gated numerics** | LLM proposes; SPICE/MATLAB/python-control computes; never present unverified numbers as results | `matlab-simulink-surface.md`, `open-source-verification.md` |
| **Structure-aware retrieval** | Topology/graph similarity for circuits, not just text chunks | AITEE MRI; future RAG note |
| **Human edit gate on vision** | Photo/sketch → draft schematic → user confirms → simulate | `photo-to-schematic-to-simulink.md` |
| **Simulation-based eval** | EngDesign-style functional tests, not string match | `capability-eval-design.md` |
| **Citation-grounded explain** | Claims tied to textbook passages or standard identities | RAG stack recommendation |
| **Socratic vs answer-dump** | Teach with scaffolding; configurable for exam prep vs homework | product choice for UG fork |

### Gaps — what is still hard (honest limits)

- **Symbolic derivation from diagrams** — CircuitSense: SOTA models <19% on hardest symbolic tasks despite >85% perception.
- **Physics-aware layout** — Power PCB agents achieve connectivity but struggle creepage, thermal, commutation inductance.
- **Long-horizon design without drift** — safety constraints decay in long prompts (CAAF “context rot”).
- **Licence-bound tools** — MATLAB/Simulink excellence vs OSS parity for machines/power.
- **Copyright** — textbook RAG needs BYO or licensed embedding packs; no pirate corpora.

### Strategic fit for this repository

| User vision | Research-backed stance |
|-------------|------------------------|
| UG/PG student helper (India + global) | GATE × task-genre taxonomy + verified solve/simulate + explain with citations |
| Explore AI limits in core engineering | Publish eval harness, EngDesign/CircuitSense-aligned tasks, failure modes |
| Circuit & control diagram ingest | Photo→editable schematic→sim pipeline; Simulink MCP for block diagrams |
| Reliability first | Tool-verified numerics; no fake simulation; human gates on vision |
| Open source | Skills + MCP + local RAG packs; OSS SPICE/power fallbacks |
| UG-bounded fork later | Keep capability tiers explicit (UG core vs PG/research stretch) in README |

## Open questions

- Minimum gold-task set per GATE section before claiming “undergrad-capable”?
- India-specific: Hindi/regional language explain vs English-only v1?
- PG fork: which stretch genres (literature triage, parametric studies) enter scope first?
- Can structure-aware retrieval be replicated without training custom GNNs (AITEE-style)?
- Public leaderboard vs private student data — privacy model for OSS deployment?

## Sources

- [AITEE — Agentic Tutor for EE](https://arxiv.org/html/2505.21582) — retrieved 2026-09-08 — reliability: paper
- [AITEE IEEE Access (MRI)](https://doi.org/10.1109/access.2026.3679269) — retrieved 2026-09-08 — reliability: paper
- [AaLLM analog design](https://arxiv.org/html/2608.13472) — retrieved 2026-09-08 — reliability: paper
- [CircuitSense benchmark](https://arxiv.org/html/2509.22339) — retrieved 2026-09-08 — reliability: paper
- [EngDesign benchmark](https://agi4engineering.github.io/Eng-Design/) — retrieved 2026-09-08 — reliability: paper
- [OmniSch schematic benchmark](https://arxiv.org/html/2604.00270v1) — retrieved 2026-09-08 — reliability: paper
- [PCBnet dataset](https://arxiv.org/html/2608.27923) — retrieved 2026-09-08 — reliability: paper
- [SINA schematic-to-netlist](https://arxiv.org/html/2601.22114) — retrieved 2026-09-08 — reliability: paper
- [Agentic AI in Engineering and Manufacturing](https://arxiv.org/pdf/2604.09633) — retrieved 2026-09-08 — reliability: paper
- [Harness as an Asset / CAAF](https://doi.org/10.48550/arxiv.2604.17025) — retrieved 2026-09-08 — reliability: paper
- [State of Engineering AI 2025 (SimScale)](https://explore.simscale.com/hubfs/resources/reports/state-of-engineering-ai-2025.pdf) — retrieved 2026-09-08 — reliability: vendor
- [MITTR / LTTS physical vs digital engineering](https://wp.technologyreview.com/wp-content/uploads/2026/03/MITTR-Insights_LTTS_Report_March26.pdf) — retrieved 2026-09-08 — reliability: secondary
- [Simulink Agentic Toolkit](https://github.com/simulink/simulink-agentic-toolkit) — retrieved 2026-09-08 — reliability: vendor
- [MATLAB Agentic AI](https://www.mathworks.com/products/matlab/agentic-ai.html) — retrieved 2026-09-08 — reliability: vendor
- [SPICEBridge](https://github.com/clanker-lover/spicebridge) — retrieved 2026-09-08 — reliability: primary
- [OpenEMT](https://github.com/h-d-engineer/OpenEMT) — retrieved 2026-09-08 — reliability: primary
- [AEC civil agents](https://aecmag.com/features/ai-agents-for-civil-engineers/) — retrieved 2026-09-08 — reliability: secondary
- [Engineering.ai platform](https://arxiv.org/pdf/2511.00122) — retrieved 2026-09-08 — reliability: paper
- [GATE EE syllabus 2025](https://static.collegedekho.com/media/uploads/2024/07/01/gate-_ee_2025_syllabus.pdf) — retrieved 2026-09-08 — reliability: secondary

## Confidence

Overall confidence for this note: **high** on directional trends and architectural patterns; **med** on market-size figures and vendor adoption rates.

Confidence would rise with hands-on replication of schematic-ingest pipelines and a pinned EngDesign/CircuitSense eval slice on chosen models. It would fall if major vendors retract agentic APIs or if benchmark tasks prove non-representative of Indian UG coursework.
