# PRD critique log (Proposed)

Lead merges. Critics were readonly. Owner intake (ChatGPT desktop first-class, dual MATLAB MCP, split ACI, no ChatGPT web) is not overturned by a critic.

## Loop 1 — fitness (student / harness / TA)

### Accepted

- CLI-without-host: numbers with no model; viva needs local/BYO model or a host; argument band omitted/`unchecked` without a model is honest.
- Public bound vs v1 enabled pack depth called out (ten packs are not equally gold in v1).
- FR18: unlabeled numerals in the argument band fail; provenance names the verifier.
- FR21: host-path YAML must not call `solve-explain`; gold/CLI rollback may keep it.
- FR22: MCP must speak host JSON-RPC framing and not crash on unknown methods; tool I/O includes problem/netlist/`run_id`. As-built NDJSON/`problem.json`-only is a later code defect, now a requirement.

### Rejected (reason)

- Make ChatGPT **web** a host — owner intake; web has no local stdio.
- Drop dual MATLAB MCP / FR20 — owner intake; clamp law stays.
- Printable Given/Find lab-report template as v1 FR — later; `summary.json` + argument band is the v1 leave-behind.
- Cut H3 vocabulary and split ACI from the PRD — implementers need them; student README is a later pass.
- Treat Skills-over-MCP as already shipped — FR22 + host doc: pin root skill until resources exist.
- LLM-as-judge of viva — not added.
