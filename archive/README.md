---
title: "Archive Directory Guide"
scope: "archive/"
updated: "2025-02-14"
---

# Archive

Closed EPICs, historical briefs, and frozen artifacts move here once they are no longer active.

## Folder structure
Organize the archive by year and month to mirror the cadence of lifecycle milestones:
```
archive/
├── 2025-01/
│   ├── EPIC-05-onboarding-flow.md
│   └── aura-session-notes.md
└── 2024-12/
    └── ...
```

## What to archive
- Completed EPICs with retrospectives
- Retired agent briefs or sub-agent rosters
- Deprecated SoT extracts (keep the live ID in `source-of-truth/`)
- Outcome reports and milestone summaries

## Before archiving
1. Ensure SoT IDs are updated and referenced from their canonical files.
2. Update the `README.md` Version History table with the final decision.
3. Link lessons learned in the current EPIC or product docs for easy retrieval.

Archived files should not be edited retroactively—create a new entry in the active directories if work resumes.
