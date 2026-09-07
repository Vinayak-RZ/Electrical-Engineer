# Open-source verification tier

## Purpose

Map licence-free simulation and analysis tools that can back an EE agent when MATLAB/Simulink is unavailable, and show coverage gaps.

## Findings

Claim | Evidence (URL) | Confidence
--- | --- | ---
MCP servers already expose **ngspice / LTspice** simulation to agents | https://github.com/cognitohazard/ltspice-mcp ; https://github.com/Casys-AI/mcp-spice ; https://github.com/clanker-lover/spicebridge | high
Python ecosystems cover power-system steady-state (`pandapower`, `PyPSA`) and classical control (`python-control`) plus symbolic math (`sympy`) | project docs / ecosystem knowledge | med
OSS tier is strongest for **circuits (SPICE)** and partial for **power/control**; weakest for full **machines + Simulink-style multi-domain labs** | coverage matrix below | med

### Coverage matrix (coarse)

| Domain | OSS options | vs MATLAB/Simulink |
|--------|-------------|--------------------|
| Analog/digital circuits | ngspice/LTspice MCPs, PySpice | Competitive for many undergrad nets |
| Power systems (load flow, simple contingency) | pandapower, PyPSA | Good for study-level LF; protection/dynamics weaker |
| Control (LTI, Bode, root locus) | python-control, scipy.signal | Good for classical; Simulink remains richer for nonlinear plants |
| Power electronics | ngspice limited; specialized Python libs uneven | MATLAB/Simulink + PLECS-class tools usually ahead |
| Electrical machines | Modelica/Simscape alternatives exist but fragmented | Simscape Electrical typically easier for undergrad labs |
| Symbolic derivations | sympy | Strong complement even when MATLAB exists |

### Stance

**Hybrid:** MATLAB primary when present; **OSS fallback** documented and MCP-wired for circuits-first continuity. If CP-2 shows no MATLAB, promote OSS (+ sympy) to primary and narrow machine/drive lab ambitions until a sim strategy is chosen.

## Open questions

- Which single SPICE MCP to standardize on for quality and security (netlist sandboxing)?
- Whether to vendor a minimal pandapower skill pack in-repo later.

## Sources

- [ltspice-mcp](https://github.com/cognitohazard/ltspice-mcp) — retrieved 2026-09-07 — reliability: primary (S17)
- [mcp-spice](https://github.com/Casys-AI/mcp-spice) — retrieved 2026-09-07 — reliability: primary (S18)
- [spicebridge](https://github.com/clanker-lover/spicebridge) — retrieved 2026-09-07 — reliability: primary (S19)
- [matlab-simulink-surface.md](matlab-simulink-surface.md) — retrieved 2026-09-07 — reliability: primary

## Confidence

Overall confidence for this note: med

Existence of SPICE MCPs is high confidence; breadth of Python power/machines coverage needs hands-on spikes before strong claims.
