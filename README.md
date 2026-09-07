# Electrical-Engineer

Agentic harness which can do anything that an undergrad electrical engineer can.

## Cursor coding config

This repo vendors [cursor-config-coding](https://github.com/Vinayak-RZ/cursor-config-coding) for agent rules, skills, and MCP.

| Asset | Location |
|-------|----------|
| Rules & skills | [`.cursor/`](.cursor/) |
| Vendor pin | [`.cursor/VENDOR.md`](.cursor/VENDOR.md) |
| Agent instructions | [`AGENTS.md`](AGENTS.md) |
| Skills manifest | [`skills-manifest.json`](skills-manifest.json) |
| Config docs | [`docs/cursor-config/`](docs/cursor-config/) |
| Helper scripts | [`scripts/cursor-config/`](scripts/cursor-config/) |

Cloud Agents load `.cursor/rules` and `.cursor/skills` from this repository history — keep them committed (do not symlink to an external clone).
