## What this changes

<!-- One paragraph. Which lifecycle stage, skill, hook, template, or doc does this touch? -->

## IDs touched

<!-- BR-/UJ-/API-/LL- … IDs created or changed, or "none". SoT is updated before or during the change, never after. -->

## Checklist

- [ ] `python3 -m pytest tests/ -q` passes locally
- [ ] If anything under `.claude/` or a seeded file changed: `bash scripts/package-plugin.sh` was run and the regenerated `plugins/prd-ce/` is in this PR (`bash scripts/check-plugin-sync.sh` passes)
- [ ] Relative links only; no machine-local paths; no client-specific or unharvested `temp/` material
- [ ] Docs / README updated where the change is user-visible
