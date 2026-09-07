# MATLAB and Simulink agent surface

## Purpose

Describe how MathWorks’ official MCP and agentic toolkits can serve as the numerical/lab verification surface for an EE agent.

## Findings

Claim | Evidence (URL) | Confidence
--- | --- | ---
MathWorks publishes an official **MATLAB MCP Server** for AI coding agents | https://github.com/matlab/matlab-mcp-server | high
Core MCP tools include evaluate/run code, run tests, static check, and detect toolboxes | https://github.com/matlab/matlab-agentic-toolkit ; https://www.mathworks.com/products/matlab-agentic-toolkit.html | high
**MATLAB Agentic Toolkit** installs the MCP server and registers skills for idiomatic MATLAB | https://github.com/matlab/matlab-agentic-toolkit | high
**Simulink Agentic Toolkit** adds model read/edit/simulate workflows on the same MCP bridge | https://github.com/matlab/simulink-agentic-toolkit | high
Session modes matter (`new` / `existing` / `auto`); long simulations need raised tool timeouts | MathWorks toolkit troubleshooting docs (referenced from toolkit READMEs) | med
Undergrad EE labs typically need subsets of Control System Toolbox, Simscape Electrical, Specialized Power Systems / powerlib, Signal Processing, Symbolic Math — exact set is licence-dependent | domain practice + MathWorks product lines | med

### Responsibility split

| Agent need | MathWorks surface |
|------------|-------------------|
| Run `.m` scripts / live numeric checks | `evaluate_matlab_code` / `run_matlab_file` |
| Unit tests for student code | `run_matlab_test_file` |
| Avoid hallucinated APIs | skills + `check_matlab_code` + toolbox detect |
| Build/simulate `.slx` labs | Simulink toolkit tools + MBD skills |

### Failure modes

- No MATLAB licence / installation on the machine.
- Network/VPN licence failures when MCP starts MATLAB (hangs or opaque errors).
- Missing shared session (`existing`/`shareMATLABSession`) → empty workspace / wrong models.
- Missing toolbox → cryptic failures; call `detect_matlab_toolboxes` first.
- Tool timeout too short for load-flow or long transients (Codex docs often raise to ≥600s).
- Multi-user shared MCP conflicts with MathWorks licence expectations.
- Agent claims “simulated” results without calling MCP (policy must forbid).
- Destructive clears / overwriting student models without approval.
- Curriculum note: Specialized Power Systems libraries migrate toward native Simscape Electrical on newer releases — skill packs must track that.

### Stance (D5 leaning)

**MATLAB/Simulink is the intended primary verifier** when a licence exists. Pair with textbook RAG for concepts; never treat model priors as measurement.

## Open questions

- User CP-2: which toolboxes are actually installed?
- Minimum MATLAB release for MCP + Simulink toolkit features.

## Sources

- [matlab-mcp-server](https://github.com/matlab/matlab-mcp-server) — retrieved 2026-09-07 — reliability: primary (S7)
- [matlab-agentic-toolkit](https://github.com/matlab/matlab-agentic-toolkit) — retrieved 2026-09-07 — reliability: primary (S8)
- [simulink-agentic-toolkit](https://github.com/matlab/simulink-agentic-toolkit) — retrieved 2026-09-07 — reliability: primary (S9)
- [MathWorks product page](https://www.mathworks.com/products/matlab-agentic-toolkit.html) — retrieved 2026-09-07 — reliability: vendor (S10)

## Confidence

Overall confidence for this note: high

Official repos establish the tool surface; campus licence details remain user-specific.
