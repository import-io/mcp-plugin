# Import.io Web Scraper Claude Code Plugin

Claude Code plugin that connects Claude to the Import.io Web Scraper MCP server.

## Prerequisites

- Claude Code installed and authenticated.
- The `importio-mcp` server binary built from `../mcp`.
- An Import.io API key.

Get an API key from <https://app.import.io/dash/account/settings>.

## Run the MCP server

From the `mcp` repository:

```bash
go build -o importio-mcp
./importio-mcp
```

The server listens on `http://127.0.0.1:9494/mcp` by default.

## Test this plugin locally

From any project where you want to use Claude Code:

```bash
claude --plugin-dir /Users/smo/code/import-io/mcp-plugin
```

Claude Code prompts for the plugin's `importio_api_key` user config. Enter the Import.io API key from your account settings, then check Claude Code's MCP tools list for `import-io-web-scraper`.

## Agent guidance

This plugin includes an `import-io-web-scraper` skill that tells agents to use the Import.io Web Scraper MCP tools by default for scraping, browser automation, JavaScript-rendered pages, pagination, screenshots, HTML capture, and structured extraction.

## Development notes

- The plugin does not bundle the `importio-mcp` binary. Users must run the server separately.
- The API key is stored as sensitive Claude plugin user config and passed to the local MCP server through the `X-Import-IO-API-Key` header.
- The MCP server also accepts `Authorization: Bearer <key>` and `/mcp?_apikey=<key>` as compatibility fallbacks.

## Marketplace submission

Run validation before submitting:

```bash
claude plugin validate /Users/smo/code/import-io/mcp-plugin
```

After validation, submit through the Claude plugin submission flow described in the Claude Code plugin docs.
