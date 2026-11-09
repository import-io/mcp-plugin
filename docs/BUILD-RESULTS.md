# Import.io Antigravity adaptation: validation results

Date: 2026-11-07

## Result

The standalone Antigravity 0.3.0 plugin bundle passed Google's CLI 1.5.3 strict
validation and a local install into a fresh, isolated cloud-only profile.
It is disabled until the account key is configured, which is expected.

This is a tested packaging and installation candidate, not a fully live-tested
integration or an accepted Marketplace listing.

## Provenance

- Upstream: https://github.com/import-io/mcp-plugin
- Base commit: b50a86e12b747ba95cb7df7c9d8142e7b8bf1f74
- Platform: Linux x86_64; Python 3.12.14
- Official CLI: 1.5.3, downloaded by Google's official installer with its SHA-512
  verification passing. The binary was installed only inside this task's
  isolated directory; no existing user shell profile or installation was changed.
- Standalone ZIP SHA-256: 3bdd3e8860b969ea1ca3bfd9f15989de3e6ebaf032f0752b66f78691ec3fd662

## Passed checks

- 19 unit tests: manifest contract, credential placeholders, host-aware skill,
  unchanged Claude files, allowlisted packaging, deterministic ZIP, safe paths,
  refusal to overwrite existing build directories, and no embedded MCP keys.
- Official manifest JSON Schema snapshot validation using jsonschema 4.26.0.
- Python compile check and shell syntax check for the unchanged setup script.
- `agy plugin validate --strict` on the final standalone bundle: exit 0.
- `agy plugin install` on the final bundle into a fresh HOME: exit 0.
- `agy plugin list --json`: version 0.3.0, enabled false, one skill and one MCP
  server, both named import-io-web-scraper.
- Byte-for-byte comparison of every installed file to the final eight-file bundle.
- Independent source/package review: no blocking defects identified.
- Extracted the source-review ZIP, re-ran tests and schema validation, and
  rebuilt a byte-identical standalone ZIP.

Developer note: packaging and standard-library unit tests need Python 3.9+;
the pinned jsonschema dependency for the separate schema check requires 3.10+.

## Compatibility detail

CLI 1.5.3 emits a strict warning for Claude's `.mcp.json` in the multi-provider
source tree. Removing that file would disturb the Claude integration. Instead,
`scripts/package_antigravity.py` generates the standalone Antigravity bundle,
which passes strict validation without altering any Claude configuration.
The source root itself still produces that expected warning; install the bundle.

## Not run or not claimed

- Google account sign-in, Antigravity credential-dialog interaction, or MCP-key
  creation/configuration. No credentials were used or generated.
- Hosted MCP authentication, tool calls, live scraping, pagination, screenshot
  capture, paid service usage, or restart behavior after credential setup.
- App or IDE UI validation.
- Final light/dark icon visual QA. The icon is the official public website
  favicon with an expanded 128-pixel SVG canvas and padding; structural checks
  passed. Local SVG preview was blocked by a missing rendering delegate.
- Public repository modification, pushing, pull requests, external sharing,
  Marketplace submission, or Google partner acceptance.

## Isolation

The original checkout has a clean Git status. Claude's plugin manifest,
marketplace manifest, MCP config, setup script, and license remain byte-for-byte
identical to upstream. No server-side changes were made. Both installation
tests used separate fresh HOME/config/cache directories and left their plugin
disabled, without connecting to the Import.io service.

## Remaining gates

Review the source and listing icon with Import.io maintainers, then run the
authorized test-account acceptance steps in ANTIGRAVITY-VALIDATION.md. Confirm
Google's intake approval separately. Publication requires separate approval.
