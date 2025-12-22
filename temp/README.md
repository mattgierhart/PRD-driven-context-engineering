---
title: "Temp Workspace Guide"
scope: "temp/"
updated: "2025-12-22"
---

# Temp Workspace

Short-lived notes, audits, and scratchpads live here. This directory is intentionally transient but **linked to execution**.

## Rules

1.  **Epic Association**: Every file MUST be associated with an Active Epic.
2.  **Archive, Don't Delete**: When the Epic closes, move these files to `archive/` or `specs/` (if durable). Do not just delete them; the context is valuable.

## Naming Convention

- **Format**: `EPIC-{XX}_{Topic}.md`
- **Examples**:
  - `temp/EPIC-05_audit_log.md`
  - `temp/EPIC-07_tech_debt_analysis.md`
  - `temp/EPIC-02_brainstorm.md`

## When to use temp files

- **Audits**: Checking `specs/` vs. Codebase.
- **Explorations**: Technical spikes or detailed design thoughts before they become `specs/`.
- **Tech Debt**: Documenting debt found during an Epic (before moving to a formal Backlog item).

> **Warning**: Never reference temp files from `PRD.md` or `README.md`. They are not sources of truth.
