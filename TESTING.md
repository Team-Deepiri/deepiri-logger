Running tests and parity validator

Quick steps to run the parity validator and smoke-tests locally:

1. Python environment

```bash
cd deepiri-logger
python3 -m venv .venv
. .venv/bin/activate
pip install --upgrade pip
pip install structlog jsonschema
```

2. Node environment

```bash
cd nodejs
npm ci
npm run build
cd ..
```

3. Run parity validator

```bash
. .venv/bin/activate
python scripts/validate_parity.py
```

What the validator does:
- Runs the Python example (python/example_app.py) and validates JSON output against `shared/schema.json` and masking rules from `shared/pii-patterns.yml`.
- Builds the Node adapter and runs the node formatter (`nodejs/dist/format_and_print.js`) to validate Node output as well.

Smoke tests
- To quickly test the Python adapter import path from a service repo, run:

```bash
python -c "import sys, pathlib; p=pathlib.Path('path/to/deepiri-logger/python').resolve(); sys.path.insert(0,str(p)); import deepiri_logger; print('OK', deepiri_logger)"
```

Notes
- The validator requires `node` and `npm` on your PATH, and Python 3.8+.
- For CI, ensure `structlog` and `jsonschema` are installed in the runner environment before executing `scripts/validate_parity.py`.
