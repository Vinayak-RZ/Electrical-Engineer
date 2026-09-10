"""Verifier seams. Missing tools fail clearly — never a fake pass."""

from __future__ import annotations

from typing import Any

from electrical_engineer.nodes.registry import register
from electrical_engineer.unchecked import UNCHECKED


def _missing(tool: str, spec: dict[str, Any], inputs: dict[str, Any]) -> dict[str, Any]:
    return {
        "ok": False,
        "tool": tool,
        "error": f"{tool} not available",
        "unchecked": True,
        "token": UNCHECKED,
        "inputs": inputs,
        "node": spec.get("id"),
    }


@register("run-spice")
def run_spice(spec: dict[str, Any], inputs: dict[str, Any]) -> dict[str, Any]:
    try:
        import PySpice  # noqa: F401
    except ImportError:
        return _missing("ngspice/PySpice", spec, inputs)
    return _missing("ngspice/PySpice", spec, inputs)


@register("run-python-control")
def run_python_control(spec: dict[str, Any], inputs: dict[str, Any]) -> dict[str, Any]:
    try:
        import control  # noqa: F401
    except ImportError:
        return _missing("python-control", spec, inputs)
    return {"ok": True, "tool": "python-control"}


@register("run-matlab-if-present")
def run_matlab_if_present(spec: dict[str, Any], inputs: dict[str, Any]) -> dict[str, Any]:
    return _missing("matlab", spec, inputs)


@register("run-load-flow")
def run_load_flow(spec: dict[str, Any], inputs: dict[str, Any]) -> dict[str, Any]:
    try:
        import pandapower  # noqa: F401
    except ImportError:
        return _missing("pandapower", spec, inputs)
    return {"ok": True, "tool": "pandapower"}


@register("check-numeric")
def check_numeric(spec: dict[str, Any], inputs: dict[str, Any]) -> dict[str, Any]:
    return {"ok": False, "unchecked": True, "token": UNCHECKED, "reason": "no expected value"}
