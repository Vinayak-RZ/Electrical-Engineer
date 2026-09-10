import json

from electrical_engineer.mcp.server import fail_closed, handle


def test_mcp_fail_closed_on_gate() -> None:
    payload = fail_closed("abcd-20260910T000000Z")
    assert payload["waits"] is False
    assert "ui_url" in payload
    raw = handle(
        "tools/call",
        {"name": "run_workflow", "arguments": {"workflow_id": "photo-to-netlist"}},
    )
    assert raw.get("isError") is True
    body = json.loads(raw["content"][0]["text"])
    assert body["waits"] is False
    assert "ui" in body["cli_hint"]
