"""JSON-RPC MCP stdio. Never waits on humans."""

from __future__ import annotations

import json
import sys
from typing import Any

from electrical_engineer.catalog import list_workflow_ids

ASK_ON_MCP = {"photo-to-netlist", "compose-from-parts", "control-diagram-to-model"}

TOOLS = [
    {
        "name": "list_workflows",
        "description": "List named workflow ids",
        "inputSchema": {"type": "object", "properties": {}},
    },
    {
        "name": "run_workflow",
        "description": "Start a named workflow; never waits",
        "inputSchema": {
            "type": "object",
            "properties": {"workflow_id": {"type": "string"}},
            "required": ["workflow_id"],
        },
    },
]


def fail_closed(run_id: str | None = None) -> dict[str, Any]:
    from electrical_engineer.ui_server.app import ui_page_url

    hint = "electrical-engineer ui" + (f" --run {run_id}" if run_id else "")
    return {
        "error": "gate_would_wait",
        "ui_url": ui_page_url(run_id),
        "cli_hint": hint,
        "waits": False,
    }


def handle(method: str, params: dict[str, Any] | None) -> Any:
    params = params or {}
    if method == "initialize":
        return {
            "protocolVersion": "2024-11-05",
            "serverInfo": {"name": "electrical-engineer", "version": "0.1.0"},
            "capabilities": {"tools": {}},
        }
    if method == "tools/list":
        return {"tools": TOOLS}
    if method == "tools/call":
        name = params.get("name")
        args = params.get("arguments") or {}
        if name == "list_workflows":
            return {"content": [{"type": "text", "text": json.dumps(list_workflow_ids())}]}
        if name == "run_workflow":
            wid = str(args.get("workflow_id") or "")
            if wid in ASK_ON_MCP:
                return {
                    "content": [{"type": "text", "text": json.dumps(fail_closed())}],
                    "isError": True,
                }
            from electrical_engineer.runner.execute import execute

            result = execute(wid)
            return {
                "content": [
                    {
                        "type": "text",
                        "text": json.dumps(
                            {
                                "workflow_id": wid,
                                "waits": False,
                                "status": "started",
                                "run_id": result["run_id"],
                            }
                        ),
                    }
                ]
            }
    if method == "notifications/initialized":
        return None
    raise ValueError(method)


def serve(stdin=None, stdout=None) -> None:
    stdin = stdin or sys.stdin
    stdout = stdout or sys.stdout
    for line in stdin:
        line = line.strip()
        if not line:
            continue
        msg = json.loads(line)
        result = handle(msg.get("method", ""), msg.get("params"))
        if "id" in msg:
            stdout.write(json.dumps({"jsonrpc": "2.0", "id": msg["id"], "result": result}) + "\n")
            stdout.flush()
