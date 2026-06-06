---
alwaysApply: true
---

# Readiness Protocol

- **Three layers**: SoT files (primitive) → EPICs (compose SoT) → PRD stage (composes both). All scores write to `status/readiness.json`.
- **Code layer (v0.6→v0.7)**: once a build produces `status/devgraph.json`, two EPIC dimensions activate — `implementation_coverage` (scoped specs with implementing code) and `architecture_conformance` (`ARC-` rules that still hold) — plus an `unbuilt_specs` cap. They auto-disable before build, so pre-v0.7 scores are unaffected. Schema: `docs/DEVELOPMENT_GRAPH.md`.
- **Compute**: Run `python scripts/readiness.py run` to refresh. Output survives in `status/readiness.json` with `last_computed` timestamp.
- **Inspect**: `readiness.py status` (text report) or `readiness.py status --json` (machine-readable).
- **Thresholds**: `score ≥ 70` PASS, `50–69` WARN, `< 50` BLOCK. Exit codes 0/1/2 match.
- **Inputs**: Declared in `readiness_inputs:` frontmatter — PRD.md for stage scope, `epics/EPIC-XX.md` for epic scope. See `docs/READINESS_PROTOCOL.md` for schema.
- **Dimension overrides**: Use `dimension_overrides: { confidence_avg: disabled }` per item when the repo hasn't adopted a convention. Disabled dimensions drop; remaining weights renormalize.
- **Traceability**: EPIC caps cite `caused_by` SoT file; SoT blocks list `consumed_by_epics`. Agents follow the causal chain to find root-cause leverage.
- **Before advancing gates**: Run readiness. If `summary.current_stage.score < threshold_warn`, update the EPIC and STOP (reinforces rule 05).
