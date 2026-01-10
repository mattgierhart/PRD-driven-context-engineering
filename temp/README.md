---
title: "Temp Workspace Guide"
scope: "temp/"
updated: "2025-01-10"
---

# Temp Workspace

Short-lived notes, audits, and scratchpads organized by PRD lifecycle stage. This directory is intentionally transient but **linked to execution**.

## Structure

Each subfolder corresponds to a PRD version gate:

```text
temp/
├── v0.1-intake/        # Initial research, market signals, user pain points
├── v0.2-validation/    # Market validation drafts, user interview notes
├── v0.3-competitive/   # Competitor analysis, differentiation notes
├── v0.4-positioning/   # Value proposition drafts, positioning exploration
├── v0.5-requirements/  # Early requirements work, feature brainstorms
├── v0.6-architecture/  # Technical exploration, architecture spikes
└── v0.7-build/         # Implementation notes, debugging logs, tech debt
```

## Rules

1. **Stage Association**: Place files in the folder matching their PRD stage context.
2. **Epic Association**: Every file SHOULD reference an Active Epic when applicable.
3. **Extract, Then Archive**: When work completes, extract durable content to `SoT/`, then move the temp file to `archive/`.

## Naming Convention

- **Format**: `{Topic}_{YYYY-MM-DD}.md` or `EPIC-{XX}_{Topic}.md`
- **Examples**:
  - `v0.2-validation/user_interviews_2025-01-10.md`
  - `v0.6-architecture/EPIC-03_api_design_spike.md`
  - `v0.7-build/EPIC-05_tech_debt_analysis.md`

## When to Use Temp Files

- **Research**: Market signals, competitor notes, user feedback
- **Explorations**: Technical spikes, design thoughts before they become `SoT/`
- **Audits**: Checking `SoT/` vs. codebase
- **Tech Debt**: Documenting debt found during an Epic

> **Warning**: Never reference temp files from `PRD.md` or `README.md`. They are not sources of truth.
