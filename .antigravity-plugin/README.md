# Import.io Web Scraper for Antigravity

Connect Antigravity to the hosted Import.io Web Scraper MCP service for rendered
web pages, structured extraction, pagination, HTML capture, and screenshots.
No local MCP server, Node package, or browser bridge is needed.

## Requirements

- A current Antigravity App or CLI with plugin support.
- An Import.io account and MCP key from <https://mcp.import.io/app/keys/new>.
- Permission to access the target websites and use the Import.io service.

Creating a key grants access to an account. Create or configure one only when
authorized. Do not paste keys into chat, source files, terminal commands, or logs.
The upstream Import.io API key belongs on the server, never in this plugin.

## Install a local copy

From the extracted **standalone Antigravity bundle** root, with Google's
official `agy` CLI installed:

```sh
agy plugin validate --strict .
agy plugin install .
agy plugin list --json
```

The plugin installs **disabled until configured**, because it declares a required
MCP variable. This is expected and does not indicate a failed install.

Open `/plugin` in the CLI, select the plugin in Installed, and press Space.
Alternatively, open **Customizations > Installed** in the Antigravity App and
toggle **Import.io Web Scraper** on. Enter the MCP key in Antigravity's setup
dialog. Do not add a literal key to `mcp_config.json`.

Then open `/mcp` in the CLI, or the App's MCP Servers section, and check the
connection. The bundled server is namespaced as
`import-io-web-scraper_import-io-web-scraper`. The credential variable is
`IMPORTIO_MCP_API_KEY`.

## Try the skill

Invoke `/import-io-web-scraper`, or describe a web extraction task. Begin with:

> Check whether the Import.io MCP tools are connected, without starting a scrape.

After you authorize any applicable service usage and sharing the target URL with
Import.io, try extracting the title and headings from <https://example.com>.
An authenticated scrape may consume Import.io credits. A successful plugin
validation or installation does not prove the hosted service is authenticated or
that extraction works.

## Troubleshooting

- **Disabled after install:** configure the key through `/plugin` or
  Customizations. A plain `agy plugin enable` is not a replacement for the setup
  dialog when variables are missing.
- **401 / 403:** check the account, key validity, and entitlement in the Import.io
  dashboard. Never include the key in a bug report.
- **No tools:** check `/mcp`, restart the server after setup, and start a fresh
  session if the skill does not appear. Tool discovery may be lazy.
- **Connection or timeout errors:** verify network access to
  `https://mcp.import.io/mcp`; use a smaller extraction scope. Do not assume the
  scrape succeeded.

For the release checklist and test evidence requirements, see
`docs/ANTIGRAVITY-VALIDATION.md`. This private adaptation has not been published
to the Antigravity Marketplace.
