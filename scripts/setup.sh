#!/usr/bin/env bash
set -euo pipefail

if [[ -z "${IMPORT_IO_API_KEY:-}" ]]; then
  echo "IMPORT_IO_API_KEY is not set." >&2
  echo "Get an API key from: https://app.import.io/dash/account/settings" >&2
  echo "Export your Import.io API key before starting Claude Code:" >&2
  echo "  export IMPORT_IO_API_KEY='your-api-key'" >&2
  exit 1
fi

echo "IMPORT_IO_API_KEY is configured."
echo "Start chromium-mcp separately, then run:"
echo "  claude --plugin-dir $(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
