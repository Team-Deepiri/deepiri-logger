#!/usr/bin/env python3
import json
import subprocess
import sys
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "shared" / "schema.json").read_text())

def run_python_example():
    # Prefer an explicit Python binary via env, else use current interpreter
    python_bin = os.environ.get("PYTHON_BIN") or sys.executable
    proc = subprocess.run([str(python_bin), str(ROOT / "python" / "example_app.py")], capture_output=True, text=True)
    out = proc.stdout.strip()
    if not out:
        print("No output from python example", file=sys.stderr)
        return None
    try:
        obj = json.loads(out)
        return obj
    except Exception:
        # fallback: find JSON substring
        start = out.find('{')
        if start >= 0:
            return json.loads(out[start:])
    return None

def run_node_formatter():
    cwd = ROOT / "nodejs"
    node = "node"
    # build first
    subprocess.run(["npm", "run", "build"], cwd=cwd)
    proc = subprocess.run([node, "dist/format_and_print.js"], cwd=cwd, capture_output=True, text=True)
    out = proc.stdout.strip()
    if not out:
        print("No output from node formatter", file=sys.stderr)
        return None
    return json.loads(out)

def validate_schema(obj: dict) -> bool:
    try:
        import jsonschema
    except Exception:
        print("jsonschema not installed in venv; install with pip install jsonschema", file=sys.stderr)
        return False
    from jsonschema import validate, ValidationError
    try:
        validate(instance=obj, schema=SCHEMA)
        return True
    except ValidationError as e:
        print("Schema validation failed:", e, file=sys.stderr)
        return False

def check_masking(obj: dict) -> bool:
    s = json.dumps(obj)
    # naive checks for visible email/api key/token
    if "@" in s and "***@***" not in s:
        print("Email appears unmasked", file=sys.stderr)
        return False
    if "AKIA" in s or "sk_" in s or "Bearer " in s:
        print("Detected likely secret unmasked", file=sys.stderr)
        return False
    return True

def main():
    print("Running Python example...")
    py = run_python_example()
    print("Python output:", py)
    if py:
        print("Schema OK:", validate_schema(py))
        print("Masking OK:", check_masking(py))

    print("Running Node formatter...")
    nd = run_node_formatter()
    print("Node output:", nd)
    if nd:
        print("Schema OK:", validate_schema(nd))
        print("Masking OK:", check_masking(nd))

    # Rust validation skipped if cargo not available
    try:
        cargo = subprocess.run(["cargo", "--version"], capture_output=True, text=True)
        if cargo.returncode != 0:
            print("Cargo not available; skipping Rust validation")
        else:
            print("Rust validation not implemented in this script yet")
    except FileNotFoundError:
        print("Cargo not available; skipping Rust validation")

if __name__ == '__main__':
    main()
