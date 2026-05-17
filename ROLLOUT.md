# Deepiri-Logger Rollout Guide

This document outlines recommended steps to package, integrate, and roll out
`deepiri-logger` across Deepiri services.

1) Packaging
  - Python: build wheel and sdist using `python -m build` from the `python/` folder.
  - Node: bump `package.json` version and `npm publish` (or use internal registry).
  - Rust: publish with `cargo publish` from the `rust/` crate.

2) Integration (submodule)
  - Add as git submodule: `git submodule add <repo> deps/deepiri-logger`
  - Update service to import the appropriate adapter (Python/Node/Rust) and call `init()`.
  - Open a PR that replaces local logger code with `deepiri-logger` usage and include validation logs.

3) Validation checklist
  - Run `scripts/validate_parity.py` locally to ensure masked output and schema compliance.
  - Verify CI jobs run the same validator.

4) Rollout strategy
  - Start with a low-risk backend service (e.g., `diri-cyrex`) and verify logs in staging.
  - After signoff, add to other repos in waves following team priorities.
