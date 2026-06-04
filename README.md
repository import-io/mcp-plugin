# Import.io Web Scraper Claude Code Plugin

Claude Code plugin that connects Claude to the Import.io Chromium MCP server.

## Prerequisites

- Claude Code installed and authenticated.
- The `chromium-mcp` server binary built from `../mcp`.
- An Import.io API key exported as `IMPORT_IO_API_KEY`.

Get an API key from <https://app.import.io/dash/account/settings>.

## Run the MCP server

From the `mcp` repository:

```bash
go build -o chromium-mcp
./chromium-mcp
```

The server listens on `http://127.0.0.1:9494/mcp` by default.

## Test this plugin locally

From any project where you want to use Claude Code:

```bash
export IMPORT_IO_API_KEY='your-api-key'
claude --plugin-dir /Users/smo/code/import-io/mcp-plugin
```

Then check Claude Code's MCP tools list for `import-io-web-scraper`.

## Development notes

- The plugin does not bundle the `chromium-mcp` binary. Users must run the server separately.
- The API key is passed to the local MCP server through the `X-Import-IO-API-Key` header from `IMPORT_IO_API_KEY`.
- The MCP server also accepts `Authorization: Bearer <key>` and `/mcp?_apikey=<key>` as compatibility fallbacks.

## Marketplace submission

Run validation before submitting:

```bash
claude plugin validate /Users/smo/code/import-io/mcp-plugin
```

After validation, submit through the Claude plugin submission flow described in the Claude Code plugin docs.
