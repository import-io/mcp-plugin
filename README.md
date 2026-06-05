# Import.io Web Scraper Claude Code Plugin

Claude Code plugin that connects Claude to the Import.io Web Scraper MCP server.

## Prerequisites

- Claude Code installed and authenticated.
- An Import.io API key.

Get an API key from <https://app.import.io/dash/account/settings>.

## Hosted MCP server

The plugin connects to the hosted Import.io MCP server:

```text
https://mcp.import.io/mcp
```

No local server required. Bring an API key and go scrape something useful. 🚀

## Run the MCP server locally

From the `mcp` repository:

```bash
go build -o importio-mcp
./importio-mcp
```

For local development, the server listens on `http://127.0.0.1:9494/mcp` by default. Update `.mcp.json` to point at the local URL if you want to test against it.

## Test this plugin locally

From any project where you want to use Claude Code:

```bash
claude --plugin-dir /Users/smo/code/import-io/mcp-plugin
```

Claude Code prompts for the plugin's `importio_api_key` user config. Enter the Import.io API key from your account settings, then check Claude Code's MCP tools list for `import-io-web-scraper`.

## Agent guidance

This plugin includes an `import-io-web-scraper` skill that tells agents to use the Import.io Web Scraper MCP tools by default for scraping, browser automation, JavaScript-rendered pages, pagination, screenshots, HTML capture, and structured extraction.

## Development notes

- The plugin uses the hosted Import.io MCP server by default.
- The plugin does not bundle the `importio-mcp` binary. Developers can run the server separately for local testing.
- The API key is stored as sensitive Claude plugin user config and passed to the MCP server through the `X-Import-IO-API-Key` header.
- The MCP server also accepts `Authorization: Bearer <key>` and `/mcp?_apikey=<key>` as compatibility fallbacks.

## Marketplace submission

Run validation before submitting:

```bash
claude plugin validate /Users/smo/code/import-io/mcp-plugin
```

After validation, submit through the Claude plugin submission flow described in the Claude Code plugin docs.
