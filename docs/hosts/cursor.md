# Cursor

First-class host. Same kernel contract as Claude Code, Codex, and ChatGPT desktop.

1. Copy or symlink pack skills from `skills/*/SKILL.md` into `.cursor/skills/`
   (or the Cursor skills path you already use). Prefer the **root** skill plus
   the pack you are working in (progressive disclosure; FR19).
2. Add a project or user MCP stdio server in `.cursor/mcp.json` whose command
   is `electrical-engineer mcp` (from a venv where the package is installed).
3. As-built tools: `list_workflows`, `run_workflow`. Photo / compose / C5 ids
   **fail closed** and return a `ui_url` — they never wait on stdio. Target
   verbs: [`../PRD.md`](../PRD.md) FR17.
4. Persistent UI is `electrical-engineer ui` on `127.0.0.1:8765`.
5. Cursor is optional. CLI + UI without Cursor is a complete v1 path.
6. If you also enable MathWorks MCP, do not treat its scalars as checked
   until Electrical Engineer labels them (FR20).
