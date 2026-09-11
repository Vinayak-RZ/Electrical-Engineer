# Cursor

1. Copy or symlink pack skills from `skills/*/SKILL.md` into the Cursor skills path you already use.
2. Add an MCP stdio server whose command is `electrical-engineer mcp` (from a venv where the package is installed).
3. Tools: `list_workflows`, `run_workflow`. Photo / compose / C5 ids **fail closed** and return a `ui_url` — they never wait on stdio.
4. Persistent UI is `electrical-engineer ui` on `127.0.0.1:8765`. Cursor is optional.
