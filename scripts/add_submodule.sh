#!/usr/bin/env bash
set -euo pipefail
if [ $# -lt 1 ]; then
  echo "Usage: $0 <service-repo-path> [submodule-path]"
  exit 1
fi
SERVICE=$1
SUBPATH=${2:-deps/deepiri-logger}
git -C "$SERVICE" submodule add https://github.com/Team-Deepiri/deepiri-logger.git "$SUBPATH"
echo "Added submodule to $SERVICE at $SUBPATH"
