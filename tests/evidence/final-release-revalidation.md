# Final release revalidation — Antigravity 0.3.0

Date: 2026-11-09. Performed after PR #3 merged to `master` (merge commit
`d4c8bab95e543c86bed8ffad81220b24fb2f9132`), closing the "revalidate the final
release build" gate in `docs/ANTIGRAVITY-VALIDATION.md`.

## Final artifact

- Built from merged `master` with `scripts/package_antigravity.py`.
- ZIP SHA-256: `d767fbade4e158cb356d4cc3695378201681dca152c094d5be16c1a3b32e6011`
- Differs from the live-acceptance bundle (`3bdd3e88…`) in two bundled files,
  both documentation-only additions made after live testing and disclosed in
  `live-acceptance-2026-11-09.md`: the skill's "Discovery and Lightweight
  Content Tools" section and the validation-results note in
  `docs/ANTIGRAVITY-VALIDATION.md`. No manifest, MCP configuration, icon, or
  packaging-code content changed between the two bundles.

## Checks on the final bundle

- 20/20 unit tests pass (includes the schema-provenance pin).
- Pinned manifest-schema validation passes.
- `agy plugin validate --strict` (Google CLI 1.5.3, Linux x86_64): pass.
- Install into a fresh isolated profile: exit 0; `plugin list --json` shows
  version 0.3.0, `enabled: false` until the credential variable is configured,
  exactly one skill and one MCP server.
- All eight installed files are byte-identical to the bundle.

## Status

Offline and isolated checks are complete for the final build. Remaining before
Marketplace submission: formal icon approval, App version capture, and Google
partner intake confirmation.
