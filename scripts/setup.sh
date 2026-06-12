#!/usr/bin/env bash
set -euo pipefail

echo "Sign in and create an Import.io MCP key:"
echo "  https://mcp.import.io/app/keys/new"
echo
echo "Claude Code will prompt for the plugin mcp_api_key user config when the plugin is loaded."
echo "Use an mcp_live_... key. If testing locally, start importio-mcp separately with IMPORTIO_API_KEY set, then run:"
echo "  claude --plugin-dir $(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
