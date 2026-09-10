"""Run ids and isolated directories. Audit only — no crash-resume."""

from __future__ import annotations

import os
import secrets
from datetime import UTC, datetime
from pathlib import Path

ALPHABET = "0123456789abcdefghjkmnpqrstvwxyz"


def new_run_id(*, now: datetime | None = None) -> str:
    n = int.from_bytes(secrets.token_bytes(3), "big")
    chars: list[str] = []
    for _ in range(4):
        chars.append(ALPHABET[n % 32])
        n //= 32
    suffix = "".join(reversed(chars))
    ts = (now or datetime.now(UTC)).strftime("%Y%m%dT%H%M%SZ")
    return f"{suffix}-{ts}"


def project_root(cwd: Path | None = None) -> Path:
    p = (cwd or Path.cwd()).resolve()
    for cand in [p, *p.parents]:
        if (cand / "workflows").is_dir() or (cand / ".electrical-engineer").is_dir():
            return cand
    return p


def create_run_dir(root: Path, run_id: str) -> Path:
    d = root / "runs" / run_id
    (d / "nodes").mkdir(parents=True)
    return d


def node_dir(run_dir: Path, node_id: str) -> Path:
    d = run_dir / "nodes" / node_id
    d.mkdir(parents=True, exist_ok=True)
    return d


def env_allow_all() -> bool:
    return os.environ.get("EE_ALLOW_ALL", "") in {"1", "true", "TRUE", "yes"}
