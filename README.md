# Import.io Web Scraper

Claude Code and Google Antigravity plugins for the hosted Import.io Web Scraper MCP server.

## Antigravity — private validation candidate

Antigravity support is a local validation candidate, not a published release or an
accepted Marketplace listing. Authentication, live extraction, restart/reconnect,
and App/IDE behavior still need authorized testing. Icon approval and light/dark
visual checks are also pending. Do not push, share, or submit this candidate
without separate approval.

The integration uses the existing hosted service, with an account owner's MCP key
entered through Antigravity's credential dialog. No additional server is needed.
See [.antigravity-plugin/README.md](.antigravity-plugin/README.md) for setup and
[docs/ANTIGRAVITY-VALIDATION.md](docs/ANTIGRAVITY-VALIDATION.md) for acceptance and
publication gates.

Build and validate the standalone bundle:

```bash
python3 scripts/package_antigravity.py
agy plugin validate --strict ./dist/import-io-web-scraper-0.3.0
```

Install that bundle, not the shared source root. Google CLI 1.5.3 warns about
Claude's `.mcp.json` in the shared root, which fails strict validation. The builder
excludes Claude-only files without changing them and refuses to overwrite an
existing build.

### Offline development checks

Packaging and unit tests require Python 3.9+. The separate schema check requires
Python 3.10+ and the pinned developer dependency in `requirements-dev.txt`:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/validate_antigravity.py
```

Use a fresh `HOME` and XDG configuration/cache/data directories for installation
checks; do not use an authenticated profile. The plugin should install disabled
until its credential is configured. These checks do not make live scraping calls.

The Antigravity candidate and shared skill are version `0.3.0`; the unchanged
Claude plugin and marketplace manifests remain version `0.2.2`.

The original candidate's build evidence is retained in
[docs/BUILD-RESULTS.md](docs/BUILD-RESULTS.md) and `tests/evidence/`.

## Claude Code

The existing Claude manifest, marketplace configuration, MCP configuration, and
setup script are unchanged.

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
