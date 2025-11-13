---
title: "Custom Command Patterns"
audience: "AI + human build leads"
updated: "2025-02-14"
purpose: "Provide reusable chat commands aligned with the Gear Heart Methodology."
---

# CUSTOM-COMMANDS.md — Workflow Shortcuts

These commands keep agents operating inside the 3 + 1 + SoT + Temp guardrails. Adjust naming to match the chat platform you use (Slash commands, MCP triggers, etc.).

---

## `/load-context`
**When**: Starting any new working session or resuming after a break.

**What it does**
1. Loads navigation files in order (`CLAUDE.md` → `README.md` → `PRD.md`).
2. Fetches the active EPIC referenced in `README.md` → “Current Work Surface”.
3. Lists SoT IDs cited in the EPIC Section 3A for quick retrieval.

**Templates & References**
- [`templates/epics/EPIC-template.md`](../../templates/epics/EPIC-template.md)
- [`workflows/PRD-VERSION-LIFECYCLE.md`](../../workflows/PRD-VERSION-LIFECYCLE.md)

---

## `/gate-check`
**When**: Before promoting the PRD to the next lifecycle gate or closing an EPIC.

**Checklist surfaced**
- Current lifecycle gate from `PRD.md` metadata.
- Required evidence per gate (see [`workflows/WORKFLOW-PRD-DEVELOPMENT.md`](../../workflows/WORKFLOW-PRD-DEVELOPMENT.md)).
- Outstanding tests or SoT updates noted in EPIC Section 3A.

**Expected output**
- Pass/fail summary for each gate criterion.
- List of missing artifacts with pointers to the relevant template sections.
- Recommendation: “Advance / Blocked” with rationale.

---

## `/harvest-temp`
**When**: During EPIC Phase E (Documentation & Handoff).

**Steps enforced**
1. Enumerate all temp files created during the EPIC (Section 3A → Temp subsection).
2. Confirm extraction into the right SoT files (`source-of-truth/*.md`).
3. Stage archival location under `archive/YYYY-MM/`.
4. Prompt update to `README.md` metrics and learning logs.

**Related Guides**
- [`temp/README.md`](../../temp/README.md)
- [`source-of-truth/README.md`](../../source-of-truth/README.md)
- [`docs/REPO-ORGANIZATION.md`](../../docs/REPO-ORGANIZATION.md)

---

## `/id-register`
**When**: After creating new IDs (BR-/API-/UJ-/etc.).

**Output**
- Validates ID format via [`workflows/UNIQUE-ID-SYSTEM.md`](../../workflows/UNIQUE-ID-SYSTEM.md).
- Posts change log snippet that can be pasted into the active EPIC Section 3A.
- Reminds the operator to update cross references in `PRD.md` or `README.md` if applicable.

---

### Extending the Command Set
- Keep commands scoped to GHM rituals (context loading, gate checks, SoT hygiene).
- Store custom automation scripts alongside this file under `tools/`.
- Update the `updated` field in the front matter whenever the command behaviors change.

