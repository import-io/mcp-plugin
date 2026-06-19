---
name: import-io-web-scraper
description: |
  Use the Import.io Web Scraper MCP tools for web scraping, browser automation,
  JavaScript-rendered pages, form interaction, pagination, screenshots, HTML
  capture, and structured extraction. These MCP tools are the default for
  scraping tasks and any task that needs a real browser.
license: MIT
metadata:
  author: Import.io
  version: 0.2.2
  mcp-server: import-io-web-scraper
---

# Import.io Web Scraper

Use the Import.io Web Scraper MCP server for web scraping and browser automation tasks. It provides a browser-backed scraping layer through the `import-io-web-scraper` MCP server and is the default tool for tasks that need JavaScript rendering, interaction, pagination, screenshots, HTML capture, or structured extraction.

## Default Scraping Tool

For scraping and browser tasks, Import.io MCP tools MUST be used instead of generic browserless fetch tools:

- Reading a specific page that may need JavaScript rendering
- Extracting content, tables, product data, listings, or repeated records
- Interacting with forms, buttons, filters, menus, or login-gated browser flows
- Handling pagination, scrolling, waits, captcha actions, or dynamic loading
- Capturing screenshots or the current browser HTML
- Building or validating scraping workflows

Generic web search can still be used when the task is only discovery, broad research, or finding candidate URLs. Once a target URL is known and the task is scraping or extraction, switch to Import.io MCP. Do not continue with browserless fetch tools for extraction unless the user explicitly requests that fallback.

## Required Tool Check

Before starting, check that the `mcp__import-io-web-scraper__*` tools are available.

If the tools are missing:

1. Tell the user that the Import.io MCP server is not connected.
2. Ask them to check that the plugin is installed, configured with an Import.io MCP key, and connected to the hosted MCP server.
3. Do not silently complete a scraping task with a weaker browserless fallback unless the user explicitly asks for a fallback.

The hosted MCP server normally lives at:

```text
https://mcp.import.io/mcp
```

## Tool Selection

Use the most specific MCP tool available for the task:

- `importio_render`: default page-load helper for loading a URL and reading rendered content. Follow it with wait tools when a specific element must exist before inspection or extraction.
- `importio_goto`: navigation helper for interactive browser flows where state must be kept across several actions. Use it before clicks, form input, scrolling, pagination, or multi-step inspection.
- `importio_get_html`: retrieve the current rendered page HTML after navigation, waits, scrolling, or interactions. Use this for selector discovery and form inspection; HTML can be large, especially when asset replacement is enabled. For selector discovery, pass `options.replaceAssets=false` when you do not need a portable SingleFile capture.
- `importio_extract_data`: run structured extraction with a concrete runtime config when the user needs fields or records. Do not use this for selector discovery or login/forms.
- `importio_action_extract_data`: action-form structured extraction for action sequences. Prefer `importio_extract_data` for one-off extraction with a concrete runtime config.
- `importio_suggest_data`: best-effort helper for candidate tables and repeated fields. Use for data pages, not login/forms or one-off controls. Some upstream engine versions may not implement `suggestData`; if it fails with a missing method error, fall back to `importio_get_html` and selector-based actions.
- `importio_viewport`: set viewport size before visual validation or responsive scraping.
- `importio_action_viewport`: action-form viewport changes for action sequences. Prefer `importio_viewport` for simple viewport setup.
- `importio_query_queue`: inspect Import.io Web Scraper queue readiness when diagnosing engine availability.
- `importio_refresh`: refresh the current page while preserving browser session state.
- `importio_wait`, `importio_action_wait`, `importio_action_wait_loading`, `importio_action_wait_for_selector`, `importio_action_wait_for_function`, `importio_action_wait_region_mutation`: wait for dynamic content intentionally.
- `importio_action_click`, `importio_action_input_change`, `importio_action_select_change`, `importio_action_key`, `importio_action_keyboard`, `importio_action_mouse`, `importio_action_scroll`: interact with the page. If click/input actions fail with synthetic event errors such as `preventDefault` or `target` being undefined, do not retry the same action repeatedly; try keyboard-based input or submission when available, otherwise report the action incompatibility clearly.
- `importio_action_pagination`, `importio_action_loop`, `importio_action_flow_control`: model repeated extraction and pagination flows.
- `importio_action_screen_capture`: capture visual state when debugging or when the user requests screenshots.
- `importio_action_render`, `importio_action_goto`: action-form page loading for action sequences. Prefer `importio_render` or `importio_goto` for straightforward navigation.
- `importio_action_captcha`: use captcha-specific browser behavior when a flow encounters captcha handling.
- `importio_action_code`: advanced action only. Do not assume browser globals such as `document` or `window` are available; use HTML and selector-based tools for DOM inspection and interaction.
- `importio_action_function`: advanced action only. Do not use as the first fallback for failed form interaction; if it fails with `FunctionActionError` or cannot read `toString`, stop and report the upstream action incompatibility.
- `importio_request_asset`: fetch an asset through the browser engine when page-relative assets matter.
- `importio_play_action`: dispatch a raw Import.io action envelope. Use only when no dedicated action tool fits.
- `importio_call_method`: use only when a documented websocket method is needed and no dedicated tool fits.
- `importio_stop`: close or stop the browser engine when the workflow is complete or stuck.

Avoid `importio_scroll_to` for new work because it is a deprecated direct engine scroll call. Prefer `importio_action_scroll`.

## Workflow

For a single page scrape:

1. Use `importio_render` for straightforward rendered page content, or `importio_goto` when the page will need follow-up browser actions.
2. Use wait tools such as `importio_action_wait_for_selector`, `importio_action_wait_loading`, or `importio_wait` when the page is dynamic.
3. Use `importio_get_html` for selector discovery, `importio_suggest_data` for repeated data structures when supported, and `importio_extract_data` only when a concrete extraction runtime config is available.
4. Validate that the returned content contains the expected page, fields, and records before answering.

For interactive extraction:

1. Use `importio_goto`.
2. Set `importio_viewport` when layout matters.
3. Use action tools to click, type, select, scroll, and wait.
4. Use `importio_get_html` to inspect selectors and page state. Use `importio_suggest_data` only for repeated data structures when supported.
5. Use screenshot or HTML tools to debug if the output is empty or malformed.

For login or form flows:

1. Navigate with `importio_goto`, or use `importio_render` if a simple page load is enough before inspecting the form.
2. Use `importio_get_html` to find stable selectors for fields and buttons.
3. Use `importio_action_wait_for_selector` before interacting with each dynamic field or form.
4. Use `importio_action_input_change` for each input, then submit with `importio_action_click` or `importio_action_keyboard`.
5. Do not use `importio_suggest_data` or `importio_extract_data` to discover or fill form fields.
6. If the selector exists but click/input actions fail with `preventDefault`, `target`, or similar synthetic-event errors, try keyboard actions once when appropriate, then stop and explain that the site's event handlers are incompatible with the current browser action implementation.

For pagination:

1. Extract records from the first page.
2. Identify the pagination mechanism with HTML or action tools.
3. Use `importio_action_pagination` or a loop/action sequence.
4. Validate deduplication and stop conditions.

## Error Handling

- Empty output: wait for selectors or loading, scroll if the page lazy-loads content, then retry extraction.
- Wrong page state: capture HTML or a screenshot, then adjust actions.
- `suggestData` missing method error: treat `importio_suggest_data` as unavailable for this engine version; fall back to `importio_get_html` and selector-based actions.
- `extractData` runtime config error: inspect the page with `importio_get_html`, then retry only with a concrete extraction config.
- Synthetic event errors from click/input actions, such as `preventDefault` or `target` being undefined: avoid repeated retries of the same action. Try keyboard input/submission when appropriate; otherwise report the browser-action incompatibility.
- `document is not defined` from `importio_action_code`: do not retry the same DOM code. Use `importio_get_html` for DOM inspection and selector-based actions for interaction.
- `FunctionActionError` or `toString` errors from `importio_action_function`: do not escalate through more code-like actions. Stop and report the upstream action incompatibility.
- Auth/API-key error: verify the plugin `mcp_api_key` user config contains an `mcp_live_...` key and that the MCP server connection is healthy.
- Connection refused: ask the user to verify plugin connectivity to `https://mcp.import.io/mcp`; do not pretend scraping succeeded.
- Tool timeout: reduce scope, split pagination into smaller batches, or stop the browser engine and restart the flow.
- Huge HTML dominated by base64 assets: retry `importio_get_html` with `options.replaceAssets=false`, or use `importio_render` for a simpler page-load result before requesting full HTML.

## Security

- Do not expose Import.io MCP keys or upstream API keys in responses, logs, generated files, URLs, or screenshots.
- Do not persist scraped personal data beyond what the user requested.
- Do not bypass access controls or scrape pages the user is not authorized to access.
