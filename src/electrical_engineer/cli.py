"""CLI command surface. Later nodes fill mcp/eval/ui/rag/memory bodies."""

from __future__ import annotations

import argparse
import sys

from electrical_engineer import __version__

COMMANDS = ("run", "workflows", "mcp", "eval", "ui", "rag", "memory")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="electrical-engineer")
    p.add_argument("--version", action="version", version=f"electrical-engineer {__version__}")
    sub = p.add_subparsers(dest="cmd")
    run = sub.add_parser("run")
    run.add_argument("workflow_id", nargs="?")
    run.add_argument("--allow-all", action="store_true")
    sub.add_parser("workflows")
    sub.add_parser("mcp")
    ev = sub.add_parser("eval")
    ev.add_argument("--pack")
    ui = sub.add_parser("ui")
    ui.add_argument("--run")
    rag = sub.add_parser("rag")
    rag.add_argument("action", nargs="?", default="list")
    mem = sub.add_parser("memory")
    mem.add_argument("action", nargs="?", default="list")
    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.cmd is None:
        parser.print_help()
        return 0
    print(args.cmd)
    return 0


if __name__ == "__main__":
    sys.exit(main())
