#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
echo "Run this from nodejs/ to publish to npm (ensure correct registry)."
echo "Dry-run: npm publish --dry-run"
echo "To publish: npm publish"
