"""OpenAI-compatible local client. Skip if the daemon is unset or down."""

from __future__ import annotations

import os
from typing import Any

import httpx

ENV_URL = "EE_LOCAL_LLM_URL"


def complete(prompt: str, *, timeout_s: float = 2.0) -> dict[str, Any]:
    base = os.environ.get(ENV_URL, "").rstrip("/")
    if not base:
        return {"skipped": True, "reason": f"{ENV_URL} unset", "byok": False}
    url = f"{base}/v1/chat/completions"
    try:
        r = httpx.post(
            url,
            json={
                "model": os.environ.get("EE_LOCAL_LLM_MODEL", "local"),
                "messages": [{"role": "user", "content": prompt}],
            },
            timeout=timeout_s,
        )
        r.raise_for_status()
        data = r.json()
        text = data["choices"][0]["message"]["content"]
        return {"skipped": False, "text": text, "byok": False}
    except (httpx.HTTPError, KeyError, IndexError, ValueError) as exc:
        return {"skipped": True, "reason": str(exc), "byok": False}
