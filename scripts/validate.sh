#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
export PATH="${HOME}/.local/bin:${PATH}"
uv run ruff check .
uv run pytest -q
if [[ -f eval/gold/circuits ]] || [[ -d eval/gold/circuits ]]; then
  uv run electrical-engineer eval --pack circuits || true
fi
# Bind must never be 0.0.0.0 in product code.
if grep -R --include='*.py' --include='*.ts' --include='*.tsx' -n '0.0.0.0' src ui 2>/dev/null | grep -v test; then
  echo "refusing 0.0.0.0 bind" >&2
  exit 1
fi
