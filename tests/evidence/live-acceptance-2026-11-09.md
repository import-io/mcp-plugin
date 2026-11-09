# Live acceptance record — Antigravity 0.3.0

Date: 2026-11-09. Tester: Søren Mathiasen. Run against the private validation
candidate in isolated throwaway profiles; not a publication.

## Artifact under test

- Bundle: `import-io-web-scraper-0.3.0.zip`, SHA-256
  `3bdd3e8860b969ea1ca3bfd9f15989de3e6ebaf032f0752b66f78691ec3fd662` (the
  installable ZIP shared for review).
- Source: `importio-antigravity-source-review-0.3.0.zip`, SHA-256
  `e6b6bfe886c97964687daf37f3f76ef035d116aa98a7f2b7bcda0be0e3bd2c5d`, based on
  upstream commit `b50a86e12b747ba95cb7df7c9d8142e7b8bf1f74`.
- The skill documentation for six discovery tools (see below) was committed
  after this test; the tested bundle predates that documentation-only change.
  Rebuild and revalidate the final release before any submission.

## Environment

- Antigravity CLI 1.5.3, Linux x86_64.
- Antigravity App (Linux); version not recorded — capture before submission.
- Isolated temporary `HOME`/XDG profiles; no production profile used.
- Authorized test-account MCP key entered through the Antigravity setup dialog.
  It was not written into the plugin package, chat, or this record. All test
  profiles were deleted after testing and the deletion was verified.

## Checklist results (per docs/ANTIGRAVITY-VALIDATION.md)

| Step | Result |
|------|--------|
| 1. Credential via setup dialog | Pass — plugin enabled after the dialog; key not in the package |
| 2. Connection and tool discovery | Pass — `import-io-web-scraper_import-io-web-scraper` connected; 42 tools including `importio_render`, `importio_get_html`, `importio_stop` |
| 3. Skill load, connection-only check | Pass — skill loaded; the check started no scrape |
| 4. example.com render | Pass — title and heading "Example Domain"; engine stopped |
| 5. Two-page bounded extraction | Pass — approved public fixture (URL not recorded); two-page limit enforced, records deduplicated, expected columns, counts, and source URLs |
| 6. Screenshot | Pass — captured image depicted the expected page; engine stopped; image kept private, not committed |
| 7. Invalid credential | Pass — dummy value produced an actionable auth error; no key echo; no silent fallback to another provider |
| 8. Restart persistence | Pass — plugin remained configured and the server connected after relaunch |
| App checks | Pass — Customizations > Installed lists the plugin; MCP Servers connected; icon legible in light and dark themes (tester-verified screenshot) |

Results are tester-confirmed. The step-2/3 connection transcript (42 tool
names) was captured in the review conversation; raw per-step transcripts for
steps 4–8 were not retained. If fully documented per-step output is required
for submission, rerun with output capture.

## Catalog observation

The live catalog exposes 42 tools. Six (`importio_web_search`,
`importio_web_fetch`, `importio_page_text`, `importio_page_links`,
`importio_page_snippets`, `importio_search_cards`) were previously undocumented
in the shared skill; guidance for them was added on this branch after the test.

## Remaining before publication

Formal icon approval, App version capture, final-build strict revalidation with
a recorded hash, maintainer review, and Google partner intake confirmation.
