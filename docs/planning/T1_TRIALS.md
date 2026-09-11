# T1 trials — student CLI/UI and Cursor-as-agent MCP

Recorded 2026-09-10 after [R1_BOOT.md](R1_BOOT.md). These are **live runs**, not unit-test names counted as trials.

| # | Role | Scenario | Result | Evidence |
|---|------|----------|--------|----------|
| 1 | student CLI | Happy `solve-circuit-problem` divider Vin=10 R1=R2=1k | **PASS** checked `value=5.0` | `eval/gold/circuits/divider-dc-01`; also R1 log |
| 2 | student CLI | Empty RAG filter `book_id=no-such-book` | **PASS** `empty: true` | `electrical_engineer.rag.retrieve` |
| 3 | student CLI | Unmatched path | **PASS** no `run-spice`, token `unchecked` | `unmatched-cosolver` |
| 4 | Cursor agent MCP | Gate fail-closed `photo-to-netlist` | **PASS** `waits: false`, `ui_url`, no hang | MCP `run_workflow` |
| 5 | student eval | Injection fixture cannot flip policy | **PASS** still `unchecked` under `EE_ALLOW_ALL` | `eval/gold/injection/flip-gates-01` |
| 6 | student CLI | Photo confirm, no sim | **PASS** `simulate: false`, no spice node | `photo-to-netlist` |
| 7 | student + MCP | compose-from-parts 16-cap / MCP ask | **PASS** ComposeError `more than 16 nodes`; MCP `gate_would_wait` | `compose.graph` + MCP |
| 8 | student CLI | Control Bode/step artifacts | **PASS** `bode.svg` + `step.png` in run dir. Files state `python-control missing` — not an invented Bode | `solve-control-problem` |
| 9 | student CLI | Other pack | **PASS** `solve-signals-problem` runs; honest `unchecked` + `CD-SIGNALS-MATLAB` | `docs/CANNOT_DO.md` |
| 10 | student UI | DESIGN-coinbase chrome | **PASS** `--ee-color-canvas: #ffffff`, primary `#0052ff`, pill `unchecked` badge, skip-link, no Coinbase wordmark, bind `127.0.0.1` | `ui/src/tokens.css`, `ui/src/slots/root.jsx` |

No regressions opened as silent. Control plots without the library stay labelled missing (cannot-do / unchecked), not fake gold.

MCP-as-agent trials: #4 and #7. Student CLI/UI: the rest.
