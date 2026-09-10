# Node plan — B_UI — FastAPI + React slots

> Parent: [EXECUTION_GRAPH.md](../../EXECUTION_GRAPH.md)

| Field | Value |
|-------|-------|
| **Node id** | `B_UI` |
| **Job** | Persistent localhost workspace: FastAPI + Vite React + Zustand + slot registry |
| **Wave** | 4 |
| **Depends on** | U1 `slot_map` |
| **Write paths** | `ui/**`, `src/electrical_engineer/ui_server/**`, `tests/integration/test_ui_bind.py` |
| **Read paths** | `docs/ui-ia.md`, `docs/frontend-architecture.md` |
| **subagent_type** | generalPurpose |
| **Model** | `cursor-grok-4.6-high` |
| **Isolation** | `ui/` + `ui_server/` only |

---

## Objective

`electrical-engineer ui` starts FastAPI on **127.0.0.1** (not 0.0.0.0), serves `/api/runs`, `/api/runs/{id}`, artifacts, RAG inventory, memory excerpts, photo-confirm POST. Vite React app: thin slot registry (`register(name, Component)`), shell renders `root` only, plugins live as folders under `ui/src/slots/`. Zustand: layout + current run id. CSS tokens + CSS modules; no MUI, Ant, Tailwind-as-architecture. Auto-open browser unless `EE_NO_BROWSER=1`. Library SVG/PNG only — no model-invented circuit bitmaps. **No agent loop in the browser** (H5 falsifier).

## Non-goals

- Cordis / DSH packages
- KiCad-class editor
- WAN / LAN bind
- Image generation

## Contract

**Input:** `{ "slot_map": [] }`

**Output:** `{ "ui_server": true, "bind": "127.0.0.1", "slots_implemented": [], "auto_open": true }`

## Commits

| # | Commit | Gate |
|---|--------|------|
| 25 | `feat(ui): FastAPI 127.0.0.1` | bind test |
| 26 | `feat(ui): Vite React shell` | build |
| 27 | `feat(ui): slot registry` | register test |
| 28 | `feat(ui): zustand layout store` | unit |
| 29 | `feat(ui): run list + detail` | API |
| 30 | `feat(ui): artifact SVG/PNG` | no remote images required |
| 31 | `feat(ui): photo.confirm slot` | confirm POST |
| 32 | `feat(ui): a11y + auto-open flag` | EE_NO_BROWSER |

## Do not

- `app.run(host="0.0.0.0")`
- Import `@deepseek-ai/*` or cordis
- Put an LLM client in React

## Return to graph

`ui_server`, bind proof, failures.
