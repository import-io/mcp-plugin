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
  version: 0.2.0
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
2. Ask them to run the local `importio-mcp` server and reload the plugin.
3. Do not silently complete a scraping task with a weaker browserless fallback unless the user explicitly asks for a fallback.

The local server normally listens on:

```text
http://127.0.0.1:9494/mcp
```

## Tool Selection

Use the most specific MCP tool available for the task:

- `importio_goto`: navigate to a URL when starting an interactive browser flow.
- `importio_render`: render a URL or page when a page load plus browser rendering is enough.
- `importio_get_html`: retrieve the current page HTML after navigation, waits, scrolling, or interactions.
- `importio_extract_data`: run structured extraction with a runtime config when the user needs fields or records.
- `importio_suggest_data`: inspect the current page for candidate tables and fields before configuring extraction.
- `importio_viewport`: set viewport size before visual validation or responsive scraping.
- `importio_wait`, `importio_action_wait_loading`, `importio_action_wait_for_selector`, `importio_action_wait_for_function`: wait for dynamic content intentionally.
- `importio_action_click`, `importio_action_input_change`, `importio_action_select_change`, `importio_action_keyboard`, `importio_action_scroll`: interact with the page.
- `importio_action_pagination`, `importio_action_loop`, `importio_action_flow_control`: model repeated extraction and pagination flows.
- `importio_action_screen_capture`: capture visual state when debugging or when the user requests screenshots.
- `importio_action_captcha`: use captcha-specific browser behavior when a flow encounters captcha handling.
- `importio_request_asset`: fetch an asset through the browser engine when page-relative assets matter.
- `importio_call_method`: use only when a documented websocket method is needed and no dedicated tool fits.
- `importio_stop`: close or stop the browser engine when the workflow is complete or stuck.

Avoid `importio_scroll_to` for new work because it is a deprecated direct engine scroll call. Prefer `importio_action_scroll`.

## Workflow

For a single page scrape:

1. Use `importio_render` for straightforward rendered page content, or `importio_goto` for an interactive flow.
2. Wait for meaningful content with a wait tool when the page is dynamic.
3. Use `importio_get_html`, `importio_suggest_data`, or `importio_extract_data` depending on the requested output.
4. Validate that the returned content contains the expected page, fields, and records before answering.

For interactive extraction:

1. Use `importio_goto`.
2. Set `importio_viewport` when layout matters.
3. Use action tools to click, type, select, scroll, and wait.
4. Use `importio_suggest_data` to identify extractable structures, then `importio_extract_data`.
5. Use screenshot or HTML tools to debug if the output is empty or malformed.

For pagination:

1. Extract records from the first page.
2. Identify the pagination mechanism with HTML or action tools.
3. Use `importio_action_pagination` or a loop/action sequence.
4. Validate deduplication and stop conditions.

## Error Handling

- Empty output: wait for selectors or loading, scroll if the page lazy-loads content, then retry extraction.
- Wrong page state: capture HTML or a screenshot, then adjust actions.
- Auth/API-key error: verify the plugin `importio_api_key` user config and the local server connection.
- Connection refused: ask the user to start `importio-mcp`; do not pretend scraping succeeded.
- Tool timeout: reduce scope, split pagination into smaller batches, or stop the browser engine and restart the flow.

## Security

- Do not expose the Import.io API key in responses, logs, generated files, URLs, or screenshots.
- Do not persist scraped personal data beyond what the user requested.
- Do not bypass access controls or scrape pages the user is not authorized to access.
