# EE task taxonomy draft

## Purpose

Draft task genres an undergrad-capable EE agent should attempt, grounded in GATE EE and representative curricula (IIT Roorkee, MIT, Berkeley, ETH), without setting product requirements.

## Findings

Claim | Evidence (URL) | Confidence
--- | --- | ---
GATE EE defines ten technical sections that bound Indian undergrad expectations | https://static.collegedekho.com/media/uploads/2024/07/01/gate-_ee_2025_syllabus.pdf | high
IIT Roorkee EE emphasises power, machines, drives, control, power electronics in programme materials | https://iitr.ac.in/Departments/Electrical%20Engineering%20Department/Academics/Programmes.html | high
ETH Electric Energy track centres power electronics, machines, power system analysis, control | https://ethz.ch/content/dam/ethz/special-interest/itet/department/Studies/Electric_Energy_Engineering.pdf | high
MIT/Berkeley broaden toward circuits, signals, devices; energy/control appear as tracks/electives | https://catalog.mit.edu/subjects/6/ ; https://eecs.berkeley.edu/resources/undergrads/ece-major-information/ece-major-upper-division-degree-requirements/ | high

### Task genres

| Genre | Meaning | Example (circuits) | Example (power) | Example (control) | Example (machines) |
|-------|---------|--------------------|-----------------|-------------------|--------------------|
| Solve | Produce numeric/symbolic answer | Mesh currents | Fault current | Settling time | Efficiency |
| Derive | Show steps from first principles | Thevenin proof sketch | Swing equation setup | Routh array | Torque from energy |
| Design | Choose topology/parameters to specs | Lead network | Compensation | PID gains | Starter sizing |
| Simulate | Build/run a model | SPICE transient | Load flow | Simulink plant | Machine start-up |
| Review | Critique a solution/model | Mark student mesh | Check Ybus signs | Stability claim | Test misread |
| Explain | Teach concept with assumptions | Resonance | Per-unit | Controllability | Slip |
| Report | Lab-style write-up structure | Procedure + plots | Contingency memo | Step-response lab | OC/SC tests |

### GATE section × genres × verification

| GATE section | Primary genres | Preferred verification |
|--------------|----------------|------------------------|
| Engineering Mathematics | Solve, Derive | sympy / hand |
| Electric Circuits | Solve, Derive, Simulate, Explain | Hand + SPICE/MATLAB |
| Electromagnetic Fields | Derive, Explain, Solve | Hand (+ numeric when needed) |
| Signals and Systems | Solve, Derive, Explain | MATLAB / python-control |
| Electrical Machines | Solve, Simulate, Report, Explain | MATLAB/Simulink / hand tests |
| Power Systems | Solve, Simulate, Design, Explain | MATLAB / pandapower |
| Control Systems | Solve, Design, Simulate, Explain | MATLAB / python-control |
| Electrical and Electronic Measurements | Explain, Solve, Review | Hand + instrument models |
| Analog and Digital Electronics | Solve, Design, Simulate | SPICE / MATLAB |
| Power Electronics | Solve, Design, Simulate | Simulink / SPICE |

Priority domains for early depth: **circuits, power systems, control, machines** (user direction + IITR/ETH weighting).

### Stretch genres (PG/research intern — light map only)

Literature triage, experiment design, parametric Simulink studies, draft method notes — under Decide→Design→Build→Run→Analyze→Communicate. Not primary for undergrad framing.

## Open questions

- How many gold tasks per GATE section before taxonomy feels “covered” for evals?
- Lab-report genre may need template skills separate from solve/simulate.

## Sources

- [GATE EE syllabus](https://static.collegedekho.com/media/uploads/2024/07/01/gate-_ee_2025_syllabus.pdf) — retrieved 2026-09-07 — reliability: secondary (S11)
- [IIT Roorkee EE Programmes](https://iitr.ac.in/Departments/Electrical%20Engineering%20Department/Academics/Programmes.html) — retrieved 2026-09-07 — reliability: primary (S12)
- [ETH Electric Energy Engineering](https://ethz.ch/content/dam/ethz/special-interest/itet/department/Studies/Electric_Energy_Engineering.pdf) — retrieved 2026-09-07 — reliability: primary (S13)
- [MIT Course 6](https://catalog.mit.edu/subjects/6/) — retrieved 2026-09-07 — reliability: primary (S14)
- [Berkeley ECE upper division](https://eecs.berkeley.edu/resources/undergrads/ece-major-information/ece-major-upper-division-degree-requirements/) — retrieved 2026-09-07 — reliability: primary (S15)
- [IIT Madras course PDF](https://www.ee.iitm.ac.in/assets/documents/2026-Jan-May-Course-description.pdf) — retrieved 2026-09-07 — reliability: primary (S24)

## Confidence

Overall confidence for this note: high

Section coverage is solid; example tasks are illustrative, not an exam bank.
