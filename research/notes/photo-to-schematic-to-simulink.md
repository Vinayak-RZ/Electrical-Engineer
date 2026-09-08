# Photo to schematic UI to Simulink

## Purpose

Research the workflow: user uploads a **photo or screenshot of a circuit diagram** → agent reconstructs a machine-readable circuit → **shows an editable schematic in a UI** → user runs **simulation** (prefer Simulink when available).

## Findings

Claim | Evidence (URL) | Confidence
--- | --- | ---
2025–2026 research shows strong progress on **schematic image → SPICE netlist** pipelines (detection + connectivity + OCR/VLM) | https://arxiv.org/html/2607.01609 | high
SINA reports ~96% netlist-generation accuracy on evaluated IC/PCB-style schematics (open-source pipeline) | https://arxiv.org/html/2607.01609 | med
Hand-drawn / phone photos of textbook figures remain harder than clean CAD renders; expect human edit step | domain practice + OmniSch/PCBnet difficulty notes | high
MATLAB can build simulation artifacts from SPICE-like netlists via **Linear Circuit Wizard** (linear circuits) and **subcircuit2ssc** (Simscape) | https://www.mathworks.com/help/msblks/ug/model-linear-circuit-response-from-spice-netlist.html ; https://www.mathworks.com/help/sps/ref/subcircuit2ssc.html | high
Simulink models can also be assembled programmatically with `add_block` / wiring APIs | https://www.mathworks.com/help/simulink/slref/add_block.html | high
A usable product needs **netlist as intermediate**, **UI as source of truth after user edits**, then sim export | this note’s pipeline | high

### End-to-end pipeline

```mermaid
flowchart LR
  Photo[Photo or screenshot] --> Vision[Detect components and wires]
  Vision --> Netlist[SPICE-like netlist draft]
  Netlist --> UI[Editable schematic UI]
  UI --> UserEdit[User corrects topology values]
  UserEdit --> Canonical[Canonical netlist or .slx]
  Canonical --> Sim[Simulate]
  Sim --> Results[Waveforms and numbers]
```

### Stage details

| Stage | Options | Notes for Electrical-Engineer |
|-------|---------|-------------------------------|
| Vision → graph | SINA-like YOLO+CCL+OCR+VLM; Circuit-Think; PCBnet-style agents; frontier VLM direct netlist | Prefer structured pipeline over pure VLM for checkable topology |
| Intermediate | SPICE netlist + component list + geometry | Enables both ngspice and MATLAB paths |
| UI | Local web canvas (React + schematic lib), or Schemdraw/export SVG, or KiCad | Must allow edit wires/values before sim |
| Simulate (preferred) | MATLAB MCP → Linear Circuit Wizard / Simscape / `add_block` Simulink | Needs local MATLAB + toolboxes |
| Simulate (fallback) | ngspice MCP / PySpice | Keeps path alive without licence |

### UI requirements (research bar)

- Render reconstructed schematic (not only dump netlist text).
- Let user fix wrong connections, values, reference designators.
- Export canonical netlist / Simulink model after edits.
- Show simulation results next to the schematic (plots).
- Work **locally** (localhost UI or embedded TUI with exported SVG as minimum).

### Failure modes

- Crossing wires misread as junctions.
- Hand-drawn slanted resistors / unlabeled op-amps.
- Values in tiny fonts fail OCR.
- Ground/power symbols vary by textbook style.
- Nonlinear circuits exceed Linear Circuit Wizard scope → need Simscape or SPICE.
- Blind trust in vision output without UI confirmation → wrong sim “proves” wrong circuit.

### Stance for later build

1. Treat **vision → draft netlist** as assistive, not authoritative.
2. **UI edit gate** before any simulation claim.
3. Prefer **Simulink/Simscape when MATLAB is present**; keep **ngspice** as local fallback for the same netlist.
4. Scope v1 to **lumped textbook circuits** (R/L/C, sources, op-amps, basic switches); defer dense PCB sheets.

## Open questions

- Which schematic UI toolkit is lightest for a local package (web canvas vs desktop)?
- Do we store `.slx` as artifact or always regenerate from netlist?
- Offline VLM for photo parse vs requiring a local multimodal model (heavy) vs optional cloud vision (conflicts with “entirely local”).

## Sources

- [SINA schematic image to netlist](https://arxiv.org/html/2607.01609) — retrieved 2026-09-08 — reliability: paper
- [PCBnet schematic to SPICE](https://arxiv.org/html/2608.27923) — retrieved 2026-09-08 — reliability: paper
- [OmniSch PCB schematic benchmark](https://doi.org/10.48550/arxiv.2604.00270) — retrieved 2026-09-08 — reliability: paper
- [Model linear circuit from SPICE netlist (MathWorks)](https://www.mathworks.com/help/msblks/ug/model-linear-circuit-response-from-spice-netlist.html) — retrieved 2026-09-08 — reliability: primary
- [subcircuit2ssc](https://www.mathworks.com/help/sps/ref/subcircuit2ssc.html) — retrieved 2026-09-08 — reliability: primary
- [add_block](https://www.mathworks.com/help/simulink/slref/add_block.html) — retrieved 2026-09-08 — reliability: primary
- [matlab-simulink-surface.md](matlab-simulink-surface.md) — retrieved 2026-09-08 — reliability: primary
- [open-source-verification.md](open-source-verification.md) — retrieved 2026-09-08 — reliability: primary

## Confidence

Overall confidence for this note: high

Feasibility of the pipeline is high for clean schematics; phone-photo robustness and full offline multimodal stack remain the main risks.
