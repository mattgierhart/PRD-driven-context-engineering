# Readiness Protocol — Schema Reference

**Status**: v1.0 · schema_version `1.0` · last revised 2026-04-17

Readiness scoring tells you — at three levels of granularity — whether work in a PRD-CE repo is ready to advance. This document is the canonical schema reference. For the discipline rule see `.claude/rules/07-readiness-protocol.md`; for narrative context see the README's "Readiness Scoring" section.

---

## 1. Overview

Three composable scorers write to one file:

| Layer | Answers | Reads | Writes to `status/readiness.json` |
|---|---|---|---|
| **SoT file** (primitive) | "Is `SoT.X.md` in good shape?" | SoT files, domain profile | `sot_files.{path}` |
| **EPIC** (middle) | "Can we build this EPIC?" | SoT file scores, EPIC frontmatter + Section 3 | `epics.{EPIC-ID}` |
| **PRD stage** (composer) | "Can we advance v0.X → v0.Y?" | SoT file + EPIC scores, gate requirements | `stages.{v0.X}` |

The orchestrator `scripts/readiness.py` runs all three in dependency order (SoT → EPIC → stage) and produces a single text report + machine-readable JSON.

### File roles

| File | Role | Who writes |
|---|---|---|
| `PRD.md` (per-stage `readiness_inputs`) | Declared inputs: threshold overrides, dimension overrides | Human |
| `epics/EPIC-XX.md` (frontmatter `readiness_inputs`) | Declared inputs: dependencies, thresholds, overrides | Human |
| `epics/EPIC-XX.md` Section 3 "Context & IDs" | Referenced IDs the EPIC needs | Human |
| `.claude/domain-profile.yaml` | ID prefix → owning SoT file mapping | Human (stable) |
| `status/readiness.json` | All computed scores, causal links, summaries | Scorers (volatile) |

PRD.md stays diff-friendly — computed scores never write back to it. The JSON is the single sync target.

---

## 2. `readiness_inputs` frontmatter schema

### EPIC scope (`epics/EPIC-XX.md`)

```yaml
---
template_version: "3.3.0"
readiness_inputs:
  work_type: epic              # required
  depends_on_epics: []         # list of EPIC-IDs that must be Complete before this can build
  required_tests: auto         # auto = derived from Section 3 API-/BR- IDs; or explicit list [TEST-010, TEST-011]
  context_budget:              # optional; surfaces in downstream agent pre-load planning
    preload: 40000
    working_room: 160000
  threshold_warn: 70           # default 70
  threshold_block: 50          # default 50
  dimension_overrides: {}      # e.g. { confidence_avg: disabled, status_maturity: disabled }
---
```

Authoring rules:
- Do **not** include `required_specs:` — the scorer parses EPIC Section 3 directly. Maintaining a duplicate list causes drift.
- `work_type: epic` is required so the scorer picks the right scoring function.
- `dimension_overrides` values are `enabled` (default) or `disabled`. Disabled dimensions drop from the weighted sum; remaining weights renormalize to 1.0.

### Stage scope (`PRD.md`, embedded per-stage block)

```yaml
readiness_inputs:
  target_gate: "v0.6 → v0.7"   # optional — scorer autodetects from PRD.md "Next Target Gate"
  confidence_floor: 3          # minimum 1–5 confidence if the repo uses confidence fields
  threshold_warn: 70
  threshold_block: 50
  weight_overrides:            # optional; renormalized with universal defaults
    cross_ref_integrity: 0.30
```

The scorer reads the target gate from `PRD.md`'s "Next Target Gate" field if `target_gate` is not explicitly declared.

---

## 3. `status/readiness.json` structure

### Top-level

```json
{
  "last_computed": "2026-04-17T08:23:21.062830+00:00",
  "computed_by": "compute-prd-readiness@0.1.0",
  "schema_version": "1.0",
  "sot_files": { "...": { /* SoT block */ } },
  "epics":     { "...": { /* EPIC block */ } },
  "stages":    { "...": { /* Stage block */ } },
  "summary":   { /* see §6 */ }
}
```

Fields written by whichever scorer ran last — `computed_by` reflects the final writer. `schema_version` bumps on breaking shape changes.

### SoT file block

```json
{
  "target": "SoT/SoT.API_CONTRACTS.md",
  "work_type": "sot",
  "score": 55.8,
  "weighted_score": 69.8,
  "penalty": 14,
  "cap_applied": null,
  "caps": [],
  "entry_count": 28,
  "consumed_by_epics": ["EPIC-02", "EPIC-03", "..."],
  "dimensions": {
    "entry_count":         { "score": 100.0, "weight": 0.200 },
    "entry_depth":         { "score":  89.3, "weight": 0.333 },
    "cross_ref_density":   { "score":   0.0, "weight": 0.267 },
    "orphan_rate":         { "score": 100.0, "weight": 0.200 },
    "status_coverage":     { "status": "not_applicable" },
    "confidence_coverage": { "status": "not_applicable" }
  },
  "unmet_criteria": [ /* see §5 */ ]
}
```

### EPIC block

```json
{
  "target": "EPIC-01",
  "work_type": "epic",
  "state": "Planned",
  "score": 55.0,
  "weighted_score": 81.2,
  "penalty": 10,
  "cap_applied": 55,
  "caps": [
    {
      "rule": "test_coverage_zero",
      "cap": 55,
      "reason": "test_coverage_declared is 0 — v0.7 requires TEST- entries before build.",
      "caused_by": "SoT/SoT.TESTING.md",
      "caused_by_score": 0.0
    }
  ],
  "threshold_warn": 70,
  "threshold_block": 50,
  "dimensions": { /* see §4 */ },
  "unmet_criteria": [ /* see §5 */ ],
  "referenced_ids_count": 29,
  "file": "epics/EPIC-01-project-infrastructure.md"
}
```

### Stage block

```json
{
  "target": "v0.8",
  "work_type": "stage",
  "gate_description": "v0.7 → v0.8 (Build → Deployment)",
  "score": 36.6,
  "weighted_score": 61.6,
  "penalty": 25,
  "cap_applied": null,
  "caps": [],
  "threshold_warn": 70,
  "threshold_block": 50,
  "dimensions": { /* see §4 */ },
  "unmet_criteria": [ /* see §5 */ ]
}
```

---

## 4. Dimensions (all layers)

Each dimension scores 0–100. Dimensions that can't be evaluated (e.g. no Confidence fields exist in the repo) auto-mark `"status": "not_applicable"` and their weight redistributes.

### SoT file dimensions

| Dimension | Weight | What it measures |
|---|---:|---|
| `entry_count` | 0.15 | Populated (≥3 entries) vs. sparse vs. placeholder. Placeholder files (no entries + "pending"/"todo"/"placeholder" marker) score 0. |
| `entry_depth` | 0.25 | Percentage of entries ≥15 words AND containing a structural keyword (`rationale`, `request`, `response`, `fields`, `step`, etc.). Catches stub templates. |
| `cross_ref_density` | 0.20 | Percentage of entries referencing at least one other ID in their body. Isolated entries are weak knowledge-graph nodes. |
| `orphan_rate` | 0.15 | Percentage of entries cited somewhere outside their own SoT file. Never-referenced entries are dead weight. |
| `status_coverage` | 0.10 | Percentage with a `Status:` field. Auto-disabled if zero entries have it (repo doesn't use the convention). |
| `confidence_coverage` | 0.15 | Percentage with a `Confidence: N/5` field. Auto-disabled if zero entries have it. |

### EPIC dimensions

| Dimension | Weight | What it measures |
|---|---:|---|
| `spec_resolution` | 0.20 | Percentage of Section 3 referenced IDs that resolve to a definition. Dangling IDs = high-severity unmet. |
| `spec_depth` | 0.15 | Percentage of resolved IDs that pass the non-stub heuristic. |
| `test_coverage_declared` | 0.15 | For each API-/BR- in scope, does a TEST- entry reference it back? Enforces v0.7 test-first methodology. |
| `upstream_gate` | 0.10 | Is the owning stage's score above threshold? Inherits stage readiness. |
| `dependency_readiness` | 0.10 | Percentage of `depends_on_epics` in State = Complete. |
| `ambiguity_load` | 0.05 | Unresolved rows in Session State → Assumptions & Ambiguities log. 20-point deduction each. |
| `confidence_avg` | 0.15 | Mean confidence of referenced IDs (scaled to 0–100). Auto-disabled if no Confidence fields found. |
| `status_maturity` | 0.05 | Percentage of resolved IDs with `Status ≠ Draft`. Auto-disabled if no Status fields found. |
| `file_readiness` | 0.05 | Percentage of SoT files the EPIC depends on that contain real entries (not placeholders). Catches `SoT.USER_JOURNEYS.md: *Pending PRD development*` cases. |

### Stage dimensions

| Dimension | Weight | What it measures |
|---|---:|---|
| `required_ids_present` | 0.30 | Fraction of gate-mandated prefixes meeting their minimum count. Sourced from `GATE_REQUIREMENTS` in `_readiness/stage.py` (mirrors `.claude/skills/ghm-gate-check/references/gate-criteria.md`). |
| `relevant_sot_readiness` | 0.30 | Weighted mean of SoT file scores for files this gate depends on. |
| `cross_ref_integrity` | 0.20 | Percentage of known-prefix ID references across the repo that resolve. False-positive-resistant (only counts prefixes in `domain-profile.yaml`). |
| `downstream_epic_readiness` | 0.20 | For v0.7+ gates: mean EPIC score. Auto-disabled for pre-v0.7 gates. |

---

## 5. `unmet_criteria` entry shape

Each item in an `unmet_criteria` list:

```json
{
  "dimension": "spec_resolution",
  "ref": "UJ-001",
  "reason": "UJ-001 referenced in EPIC Section 3 but not defined in any SoT/PRD file.",
  "severity": "high",
  "caused_by": "SoT/SoT.USER_JOURNEYS.md",
  "caused_by_score": 0.0,
  "fix": "Define UJ-001 in its SoT file, or remove the reference from Section 3."
}
```

- **severity**: `high`, `medium`, `low` — drives penalty size (see §7).
- **caused_by**: path of the SoT file implicated. Set for dimensions whose failure is attributable to a single file.
- **caused_by_score**: SoT file's current score. Lets consumers rank by leverage.
- **fix**: short actionable suggestion, not a tutorial.
- **ref**: the specific ID or file the criterion concerns. Optional; dimension-level issues (e.g. too many dangling refs overall) omit it.

---

## 6. `summary` block

Produced by every scorer run; always reflects the current `readiness.json` state.

```json
{
  "sot_files_total": 11,
  "sot_files_passing": 4,
  "epics_total": 8,
  "epics_passing": 0,
  "threshold": 70,
  "top_blockers": [
    {
      "file": "SoT/SoT.TESTING.md",
      "score": 0.0,
      "blocks": 8,
      "blocking_epics": ["EPIC-01", "EPIC-02", "..."],
      "impact": 800
    }
  ],
  "current_stage": { "target": "v0.8", "score": 36.6, "passing": false }
}
```

`impact = (100 − score) × blocks`. Ranks SoT files by the aggregate pain they cause — the "fix this first" list.

---

## 7. Scoring formula

```
weighted_score = Σ (dimension_score × dimension_weight)
                 over enabled dimensions (weights renormalize to 1.0)

raw_penalty    = Σ SEVERITY_PENALTY[c.severity] for c in unmet_criteria
penalty        = min(raw_penalty, MAX_PENALTY = 25)

cap            = min(100, each CRITICAL_CAP triggered by dimension state)

final_score    = min(cap, max(0, weighted_score − penalty))
```

**Constants** (in `scripts/_readiness/common.py`):

| Constant | Value | Purpose |
|---|---|---|
| `SEVERITY_PENALTY.high` | 10 | Per high-severity unmet |
| `SEVERITY_PENALTY.medium` | 3 | Per medium-severity unmet |
| `SEVERITY_PENALTY.low` | 1 | Per low-severity unmet |
| `MAX_PENALTY` | 25 | Prevents pile-ons from crushing scores |

**Critical caps** (EPIC):

| Rule | Cap | Trigger |
|---|---|---|
| `test_coverage_zero` | 55 | `test_coverage_declared == 0` and EPIC references any API-/BR-. |
| `spec_resolution_low` | 60 | `spec_resolution < 80%` — too many dangling IDs. |
| `stub_sot_file` | 60 | Any SoT file the EPIC depends on is a placeholder stub. |

**Critical caps** (Stage):

| Rule | Cap | Trigger |
|---|---|---|
| `missing_mandatory_artifacts` | 45 | `required_ids_present < 50%` — gate cannot pass regardless of other signals. |
| `cross_ref_broken` | 60 | `cross_ref_integrity < 60%` — repo integrity compromised. |

**Critical caps** (SoT):

| Rule | Cap | Trigger |
|---|---|---|
| `placeholder_file` | 10 | No entries + placeholder marker in body. |
| `nearly_empty` | 40 | 1–2 entries but file is referenced externally. |

---

## 8. Weights — defaults and overrides

**Universal defaults** live in `scripts/_readiness/common.py` (per-layer constants). Per-gate overrides live in `PRD.md`'s `readiness_inputs.weight_overrides` for the stage in question. Overrides merge with defaults; renormalization ensures sum = 1.0.

**When to override**:
- v0.1 evidence-heavy gates → boost `cross_ref_integrity` or confidence-tier weight.
- v0.8 test-coverage-heavy gates → boost `test_coverage_declared` (EPIC layer).
- Project-wide preference → set in `.claude/readiness-config.yaml` (optional repo-level file).

**When not to override**: if the default is "close enough," leave it. Overrides are easy to forget and drift; the universal defaults intentionally cover ~80% of cases.

---

## 9. Invocation

```bash
# Compute all three layers, print text report, exit with pass/warn/block code
python scripts/readiness.py run

# Print report from existing readiness.json without recomputing
python scripts/readiness.py status

# Emit raw JSON instead of text
python scripts/readiness.py run --json

# CI-friendly: suppress output, exit code only
python scripts/readiness.py run --quiet

# Override target gate
python scripts/readiness.py run --gate v0.7

# Run one layer at a time (for debugging)
python scripts/compute-sot-readiness.py all
python scripts/compute-readiness.py epics/EPIC-01.md --merge
python scripts/compute-prd-readiness.py --gate v0.8
```

**Exit codes** (from `readiness.py`):

| Code | Meaning |
|---|---|
| 0 | All items (stages, EPICs, SoT files) scored ≥ `threshold_warn`. |
| 1 | At least one item in WARN band (`threshold_block` ≤ score < `threshold_warn`). |
| 2 | At least one item in BLOCK band (score < `threshold_block`). |
| 3 | Runtime error (missing files, invalid inputs, etc.). |

---

## 10. Interpreting the report

Read the report top-to-bottom as a causal chain:

1. **Stage** tells you whether the repo can advance. If BLOCK, the next question is *why*.
2. **EPICs** tell you which work packages are blocked. Each cap cites its `caused_by` SoT file.
3. **SoT files** tell you the root cause. The `top_blockers` list orders files by leverage — fixing the top item unblocks the most EPICs.

The `NEXT ACTIONS` section translates the leverage view into a punch list — highest-impact first. An author's workflow is typically: fix #1, re-run `readiness.py run`, fix #2, etc. The stage score rises as SoT files rise.

---

## 11. Extending the schema

When adding a new dimension:
1. Add the dimension function in the relevant `_readiness/{sot|epic|stage}.py` module — signature `(ctx, index, ...) -> tuple[Optional[float], list[dict]]`.
2. Add weight to the corresponding `_WEIGHTS` constant in `common.py`, ensuring weights still sum to 1.0 when all enabled.
3. Update this schema doc (§4) with the dimension row.
4. Add a smoke test in `tests/test_readiness.py`.
5. Bump `SCHEMA_VERSION` in `common.py` if existing consumers would break.

When adding a critical cap:
1. Add the trigger logic + cap value in the layer's compute function.
2. Document in §7.
3. Add a smoke test that verifies the cap triggers under the expected condition.
