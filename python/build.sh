#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
if [ ! -d ../.venv ]; then
  echo "No .venv found; create one with: python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt"
fi
. .venv/bin/activate
python -m pip install --upgrade build
python -m build
echo "Built Python packages in dist/"
