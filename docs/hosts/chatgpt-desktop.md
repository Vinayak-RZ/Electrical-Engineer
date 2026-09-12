# ChatGPT desktop

First-class host **on the desktop app**. Same kernel **contract** (verbs, gates,
`unchecked`) as Cursor / Claude Code / Codex. Weaker native repo editing than
Cursor — that is expected. First-class does not mean identical IDE UX.

## Surfaces

| Surface | First-class | Notes |
|---------|-------------|-------|
| ChatGPT desktop **Chat / Work** | Yes | Settings → MCP servers → STDIO `electrical-engineer mcp`. Method via MCP-served skills when folders are unavailable. Keep a terminal for `ui` / `eval`. |
| ChatGPT desktop **Codex** view | Yes | Shared `~/.codex/config.toml`. Skill folders + MCP + CLI. See [`openai.md`](openai.md). |
| ChatGPT **web** / mobile | **No** | No local stdio MCP. Use CLI + UI, or the desktop app. |

OpenAI documents that the desktop app, Codex CLI, and IDE extension share MCP
configuration. Configure once.

## Chat / Work setup

1. Install `electrical-engineer` in a venv on this machine.
2. Open Settings → MCP servers → Add server → STDIO.
3. Command: `electrical-engineer` with arg `mcp` (full path to the venv
   binary if Settings cannot see PATH).
4. Save and restart as the app requires.
5. In the composer, confirm tools via `/mcp` (or the app’s equivalent).
6. Run `electrical-engineer ui` in a terminal for photo confirm, plots, and
   gates that must not block MCP.

Until Skills-over-MCP is implemented, paste or pin the **root** skill text
once per project (progressive disclosure: verb map + `unchecked` law only).
Do not paste textbooks.

## Must not

- Promise chatgpt.com in a browser as a simulator host.
- Let MATLAB Copilot (if also connected) mint a checked `Vout` (FR20).
- Wait on a human inside MCP (fail closed, `ui_url`).
