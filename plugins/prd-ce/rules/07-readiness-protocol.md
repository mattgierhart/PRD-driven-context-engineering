---
alwaysApply: true
---

# Readiness Protocol

- **Three layers**: SoT files (primitive) → EPICs (compose SoT) → PRD stage (composes both). All scores write to `status/readiness.json`.
- **Code layer (v0.6→v0.7)**: once a build produces `status/devgraph.json`, two EPIC dimensions activate — `implementation_coverage` (scoped specs with implementing code) and `architecture_conformance` (`ARC-` rules that still hold) — plus an `unbuilt_specs` cap. They auto-disable before build, so pre-v0.7 scores are unaffected. Schema: `docs/DEVELOPMENT_GRAPH.md`.
- **Compute**: Run `python3 "${CLAUDE_PLUGIN_ROOT:-.}/scripts/readiness.py" run --repo "$PWD"`
  to refresh in either direct or plugin layout. Output survives in `status/readiness.json` with a
  `last_computed` timestamp.
- **Inspect**: use the same resolved script with `status --repo "$PWD"` (text report) or
  `status --repo "$PWD" --json` (machine-readable).
- **Thresholds**: `score ≥ 70` PASS, `50–69` WARN, `< 50` BLOCK. Exit codes 0/1/2 match.
- **Inputs**: Declared in `readiness_inputs:` frontmatter — PRD.md for stage scope, `epics/EPIC-XX.md` for epic scope. See `docs/READINESS_PROTOCOL.md` for schema.
- **Dimension overrides**: Use `dimension_overrides: { confidence_avg: disabled }` per item when the repo hasn't adopted a convention. Disabled dimensions drop; remaining weights renormalize.
- **Traceability**: EPIC caps cite `caused_by` SoT file; SoT blocks list `consumed_by_epics`. Agents follow the causal chain to find root-cause leverage.
- **Before advancing gates**: Run readiness. If `summary.current_stage.score < threshold_warn`, update the current PRD gate record and STOP; at v0.7+ also update the approved active EPIC (reinforces rule 05).

## Anti-Goodhart & Proxy Fidelity

The score is a **floor for advancement, not a target to optimize toward** (see [`PRINCIPLES.md` P7](../skills/PRINCIPLES.md)). The discipline:

- **Detection question** — whenever a score moves, ask: *"would this change for a genuine quality reason if I swapped in a wildly different artifact, or only because I padded the inputs?"* Padding (thin duplicate entries, decorative cross-refs, self-rated confidence with no source) is a **frozen-replay defect** — the proxy moves while real quality stays locked. Raise evidence tier, not entry volume.
- **Keep the scorer deterministic and LLM-free.** `readiness.py` makes no model calls; that is what makes hundreds of re-checks cheap and trustworthy. Do **not** add LLM-judged dimensions — a drifting judge is an un-cheap, un-reproducible proxy.
- **Quality floor, then cost.** Advancement weighs readiness *and* context cost: a gate cleared only by ballooning the context budget (EPIC `context_budget`) is not really cleared. Minimize context cost *subject to* readiness holding the floor — never trade real readiness for a greener number.
- **Proxy-check periodically.** Readiness stands in for "a product users will react to." If gates pass but products don't ship (or ship broken), fix the *scorer's* fidelity, not just the artifact.
