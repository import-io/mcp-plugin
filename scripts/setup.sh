#!/usr/bin/env bash
set -euo pipefail

echo "Get an Import.io API key from:"
echo "  https://app.import.io/dash/account/settings"
echo
echo "Claude Code will prompt for the plugin importio_api_key user config when the plugin is loaded."
echo "Start importio-mcp separately, then run:"
echo "  claude --plugin-dir $(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
