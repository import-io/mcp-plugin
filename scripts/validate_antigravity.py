#!/usr/bin/env python3
"""Offline validation with a pinned copy of Google's published JSON Schema."""

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    try:
        from jsonschema import Draft202012Validator
    except ImportError:
        sys.exit("Missing developer dependency: install requirements-dev.txt in an approved virtual environment.")
    schema = json.loads((ROOT / "tests/fixtures/antigravity-plugin.schema.json").read_text())
    manifest = json.loads((ROOT / ".antigravity-plugin/plugin.json").read_text())
    Draft202012Validator.check_schema(schema)
    errors = sorted(Draft202012Validator(schema).iter_errors(manifest), key=lambda e: str(e.path))
    if errors:
        for error in errors:
            print(f"{list(error.path)}: {error.message}", file=sys.stderr)
        sys.exit(1)
    print("PASS: Antigravity manifest matches the official schema snapshot (2026-11-07).")
    print("This offline check does not replace agy plugin validate --strict or live acceptance tests.")


if __name__ == "__main__":
    main()
