#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
echo "From the rust/ folder run: cargo publish --workspace"
echo "Ensure you have the appropriate credentials and that versions are bumped in Cargo.toml."
