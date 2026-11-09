# Antigravity validation and release checklist

## Scope and architecture

The integration reuses Import.io's hosted Streamable HTTP endpoint and existing
tool guidance. It does not create a second MCP server or translate tool schemas.
Antigravity discovers `.antigravity-plugin/plugin.json`, `mcp_config.json`, and
the shared `skills/` directory. Claude keeps its existing `.claude-plugin`
manifest, `.mcp.json`, sensitive user-config mechanism, and setup script.

The official public repository remains unchanged. The `repository` metadata
identifies the upstream project, not a published Antigravity release. Until the
maintainers publish this adaptation, install the local folder rather than the
GitHub URL.

## Automated checks

Run from the **source checkout** root (the release bundle intentionally does not
include development scripts or tests):

```sh
python3 -m unittest discover -s tests -v
python3 scripts/validate_antigravity.py
python3 scripts/package_antigravity.py
agy plugin validate --strict ./dist/import-io-web-scraper-0.3.0
agy plugin install ./dist/import-io-web-scraper-0.3.0
agy plugin list --json
```

The build scripts and unit suite require Python 3.9 or newer. The unit suite
uses the Python standard library. The schema check uses
`jsonschema==4.26.0` and a pinned snapshot of Google's published JSON Schema;
this is a developer-only dependency, not a plugin runtime dependency. If it is
not already installed, install `requirements-dev.txt` in an approved virtual
environment. Offline checks do not replace Google's strict CLI validator.

CLI 1.5.3 warns that `.mcp.json` is ignored, even in a multi-provider source tree.
This makes strict validation of the source tree fail. The release builder copies
an explicit allowlist into a standalone plugin folder and ZIP, excluding
Claude-only files, Git metadata, tests, credentials, and build tools. Strictly
validate and install **that bundle**, not the shared source checkout. The
builder refuses to overwrite an existing output; choose `--output` for a new
build directory.

For an isolated installation, set `HOME` and the XDG configuration/cache
directories to a fresh writable temporary directory, and invoke the same `agy`
binary by absolute path. Do not reuse an authenticated user's profile. Inspect
the install output and `list --json` for the exact plugin name, version, one
skill, one MCP server, and a disabled state before credentials are configured.

## Live acceptance tests: authorization and account required

These tests have not passed merely because the plugin installs. Run them only
in an authorized Antigravity test profile with permission to configure account
access, share test URLs with Import.io, and incur any applicable service usage.

1. Configure an authorized test-account MCP key through the Antigravity setup
   dialog. Confirm the credential is not written into the plugin package. Do not
   record the key or authentication header in screenshots or transcripts.
2. Check `/mcp` or the App's MCP Servers section. Confirm the server connects and
   discover the actual tool definitions, including `importio_render`,
   `importio_get_html`, and `importio_stop`. Use the runtime names rather than
   assuming Claude-style prefixes.
3. Invoke `/import-io-web-scraper` and ask for a connection check only. Confirm
   the skill loads and does not start a scrape.
4. With service usage approved, render `https://example.com`, wait if needed,
   and verify the returned title/heading is "Example Domain". Use the tool's
   discovered argument schema; do not guess required parameters.
5. On an approved public fixture, navigate, wait for a stable selector, read
   rendered HTML, and extract a small record set with a concrete runtime config.
   Confirm expected columns, record counts, and source URLs. Test a two-page
   fixture with a bounded stop condition and deduplication.
6. Capture one screenshot if authorized and confirm it depicts the expected
   page. Stop the browser engine after the test.
7. Verify missing/revoked credentials produce an actionable error, without
   leaking the key or silently falling back to another scraping provider.
8. Restart the authorized Antigravity profile. Confirm the plugin remains
   configured and is available in a fresh session.

Record CLI/App version, operating system, date, plugin commit/package hash,
observed tools, pass/fail for each step, and redacted errors. Account access,
credit usage, live extraction, restart behavior, and App UI remain unverified
until those specific tests have run.

## Publication gates

- Obtain maintainer review of the shared skill changes and release version.
- Confirm the official website icon is the approved listing asset and check
  legibility in light and dark themes.
- Re-run strict validation and local install on the final release.
- Complete authorized live acceptance tests above.
- Obtain explicit approval before uploading, sending, pushing, opening a pull
  request, or submitting the package to any external party.
- Confirm Google partner intake approval separately. A submitted interest form
  is not Marketplace acceptance.

## Primary references

- Build and validation: <https://antigravity.google/docs/build-plugins>
- Install and credential dialog: <https://antigravity.google/docs/plugins>
- Streamable HTTP and MCP configuration: <https://antigravity.google/docs/mcp>
- Official CLI download: <https://antigravity.google/docs/getting-started>
- Manifest schema: <https://antigravity.google/schemas/v1/plugin.json>
- Upstream source: <https://github.com/import-io/mcp-plugin>

Checked 2026-11-07. The schema currently permits some names and aliases that the
authoring guide discourages; this package follows the stricter documented
lowercase kebab-case naming and canonical fields.
