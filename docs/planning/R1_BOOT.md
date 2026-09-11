# R1 boot evidence

Recorded 2026-09-10 on Ubuntu. Bind is **127.0.0.1** only. Local LLM skipped (unset).

## 1. electrical-engineer --help

```text
usage: electrical-engineer [-h] [--version]
                           {run,workflows,mcp,eval,ui,rag,memory} ...

positional arguments:
  {run,workflows,mcp,eval,ui,rag,memory}

options:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
```

## 2. electrical-engineer run solve-circuit-problem

```text
txps-20260910T214431Z
{
  "recipe_id": "solve-circuit-problem",
  "run_id": "txps-20260910T214431Z",
  "unchecked": false,
  "token": null,
  "value": 5.0,
  "paths": [
    "/workspace/runs/txps-20260910T214431Z/summary.json"
  ],
  "nodes": {
    "retrieve": {
      "unchecked": null,
      "ok": null
    },
    "solve": {
      "unchecked": false,
      "ok": null
    },
    "check": {
      "unchecked": false,
      "ok": true
    },
    "label": {
      "unchecked": false,
      "ok": null
    },
    "summary": {
      "unchecked": false,
      "ok": null
    }
  }
}
```

## 3. MCP stdio initialize + list_workflows

```text
{"jsonrpc": "2.0", "id": 1, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "electrical-engineer", "version": "0.1.0"}, "capabilities": {"tools": {}}}}
{"jsonrpc": "2.0", "id": 2, "result": {"tools": [{"name": "list_workflows", "description": "List named workflow ids", "inputSchema": {"type": "object", "properties": {}}}, {"name": "run_workflow", "description": "Start a named workflow; never waits", "inputSchema": {"type": "object", "properties": {"workflow_id": {"type": "string"}}, "required": ["workflow_id"]}}]}}
```

## 4. UI health on 127.0.0.1

```text
{"bind":"127.0.0.1","ok":true}
bind 127.0.0.1 port 8765
```

## Local LLM

EE_LOCAL_LLM_URL unset → skip-if-missing (see tests/unit/test_local_llm.py).
