import importlib
import json

from electrical_engineer.mcp.server import handle


def test_import_cycle_clean() -> None:
    for name in (
        "electrical_engineer.cli",
        "electrical_engineer.ui_server.app",
        "electrical_engineer.mcp.server",
        "electrical_engineer.rag.retrieve",
        "electrical_engineer.local_llm.client",
        "electrical_engineer.runner.execute",
        "electrical_engineer.vision.fixtures",
    ):
        importlib.import_module(name)


def test_mcp_run_wires_execute() -> None:
    raw = handle(
        "tools/call",
        {"name": "run_workflow", "arguments": {"workflow_id": "unmatched-cosolver"}},
    )
    body = json.loads(raw["content"][0]["text"])
    assert body["waits"] is False
    assert body.get("run_id")
