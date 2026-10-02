# Import.io Web Scraper Claude Code Plugin

Claude Code plugin that connects Claude to the Import.io Web Scraper MCP server.

## Prerequisites

- Claude Code installed and authenticated.
- An Import.io MCP key (`mcp_live_...`).

Sign in at <https://mcp.import.io/login> and create an MCP key at <https://mcp.import.io/app/keys/new>.

## Hosted MCP server

The plugin connects to the hosted Import.io MCP server:

```text
https://mcp.import.io/mcp
```

No local server required. Bring an MCP key and go scrape something useful.

## Run the MCP server locally

From the `mcp` repository:

```bash
go build -o importio-mcp
IMPORTIO_API_KEY=your-upstream-key ./importio-mcp
```

For local development, the server listens on `http://127.0.0.1:9494/mcp` by default. The local server still needs its own upstream Import.io API key in `IMPORTIO_API_KEY`; clients should continue to authenticate with an MCP key. Update `.mcp.json` to point at the local URL if you want to test against it.

## Test this plugin locally

From any project where you want to use Claude Code:

```bash
claude --plugin-dir /Users/smo/code/import-io/mcp-plugin
```

Claude Code prompts for the plugin's `mcp_api_key` user config. Enter the `mcp_live_...` key from the Import.io MCP dashboard, then check Claude Code's MCP tools list for `import-io-web-scraper`.

## Agent guidance

This plugin includes an `import-io-web-scraper` skill that tells agents to use the Import.io Web Scraper MCP tools by default for scraping, browser automation, JavaScript-rendered pages, pagination, screenshots, HTML capture, and structured extraction.

## Development notes

- The plugin uses the hosted Import.io MCP server by default.
- The plugin does not bundle the `importio-mcp` binary. Developers can run the server separately for local testing.
- The MCP key is stored as sensitive Claude plugin user config and passed to the MCP server through `Authorization: Bearer mcp_live_...`.
- The upstream Import.io API key is server-side infrastructure and is not sent by plugin clients.

## Marketplace submission

Run validation before submitting:

```bash
claude plugin validate /Users/smo/code/import-io/mcp-plugin
```

After validation, submit through the Claude plugin submission flow described in the Claude Code plugin docs.

## Gemini CLI extension (preview)

This repository also contains the `import-io-web-scraper` Gemini CLI extension,
version `0.2.3-rc.1`. It connects to the hosted MCP endpoint using Streamable
HTTP and OAuth with the `mcp:tools` scope. This extension version is independent
of the Claude Code plugin version and does not identify the server runtime.

Install with Gemini CLI:

```bash
gemini extensions install https://github.com/import-io/mcp-plugin --ref master
```

Restart Gemini CLI, then use `/mcp auth import-io-web-scraper` to connect your
Import.io account and `/mcp list` to inspect the available tools. Use Gemini's
OAuth flow; do not place access tokens or API keys in this manifest.

An Import.io account is required and service usage may be metered. The manifest
requests no billing scopes, but it does not restrict the server's tool exposure
or establish what the server authorizes under `mcp:tools`.

Gemini installation and OAuth have not yet been tested end to end. The server
must support Gemini's localhost OAuth callback and return an `iss` parameter
matching `https://mcp.import.io`. Public OAuth discovery alone does not establish
compatibility. No scraping or paid usage test is included in this release.

This repository contains client configuration and agent guidance; it does not
contain the hosted MCP server implementation.
