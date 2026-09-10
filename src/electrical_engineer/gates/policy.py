"""TOML gates: most-restrictive wins. EE_ALLOW_ALL does not disable unchecked."""

from __future__ import annotations

import os
import tomllib
from dataclasses import dataclass
from pathlib import Path

UNCHECKED = "unchecked"
MAX_INTERRUPTS = 2

DENY = 3
ASK = 2
AUTO = 1


@dataclass(frozen=True)
class GateDecision:
    action: str
    policy: int  # AUTO/ASK/DENY
    interrupt: bool


class GateAbort(Exception):
    """Third interrupt aborts the run."""


def _rank(name: str) -> int:
    n = name.lower()
    if n in {"deny", "deny-by-default"}:
        return DENY
    if n in {"ask"}:
        return ASK
    return AUTO


def load_toml(path: Path) -> dict:
    if not path.is_file():
        return {}
    return tomllib.loads(path.read_text())


def merge_gates(global_cfg: dict, project_cfg: dict) -> dict:
    keys = set(global_cfg) | set(project_cfg)
    out: dict[str, int] = {}
    for k in keys:
        a = _rank(str(global_cfg.get(k, "auto")))
        b = _rank(str(project_cfg.get(k, "auto")))
        out[k] = max(a, b)
    return out


def allow_all_env() -> bool:
    return os.environ.get("EE_ALLOW_ALL", "") in {"1", "true", "TRUE", "yes"}


class GateBox:
    def __init__(self, merged: dict[str, int], *, allow_all: bool = False) -> None:
        self.merged = merged
        self.allow_all = allow_all
        self.interrupts = 0

    def decide(self, action: str) -> GateDecision:
        policy = self.merged.get(action, AUTO)
        if self.allow_all and policy != DENY:
            # skip asks; never skip unchecked (caller still labels)
            return GateDecision(action, AUTO, interrupt=False)
        if policy == ASK:
            self.interrupts += 1
            if self.interrupts > MAX_INTERRUPTS:
                raise GateAbort("interrupt budget exceeded")
            return GateDecision(action, ASK, interrupt=True)
        if policy == DENY:
            return GateDecision(action, DENY, interrupt=False)
        return GateDecision(action, AUTO, interrupt=False)
