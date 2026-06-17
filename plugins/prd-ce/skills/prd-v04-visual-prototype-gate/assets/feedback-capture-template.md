# Feedback Capture Template

> **Purpose**: Route prototype feedback to specific SoT IDs. Every piece of feedback must land on an ID — no orphaned notes.

## Instructions for Reviewers

1. Review each prototype screen alongside its SCR- entry
2. For each screen, note what works and what doesn't
3. Categorize each feedback item using the Type column
4. Claude (or the team) dispositions each item into the correct SoT update

## Feedback Table

| Screen | SCR- ID | Feedback Item | Type | Disposition | Updated ID |
|--------|---------|---------------|------|-------------|------------|
| {Screen Name} | SCR-001 | {What needs to change or what works well} | SCR / DES / CFD / BR | Accepted / Deferred / Rejected | {ID updated} |
| {Screen Name} | SCR-002 | | | | |
| {Screen Name} | SCR-003 | | | | |

## Feedback Types

| Type | Meaning | Routes To | Example |
|------|---------|-----------|---------|
| **SCR** | Screen purpose, layout, or elements need to change | Update SCR-XXX entry in SoT.USER_JOURNEYS.md | "Dashboard should show alerts first, not metrics" |
| **DES** | Component pattern needs to change or new pattern identified | Update/create DES-XXX in SoT.DESIGN_COMPONENTS.md | "Cards should have hover states" |
| **CFD** | New user insight surfaced — didn't know this before | Create CFD-XXX in SoT.customer_feedback.md | "Reviewer says their users would never click here" |
| **BR** | Business rule discovered or changed through visual review | Update BR-XXX in SoT.BUSINESS_RULES.md | "Legal says we can't show competitor pricing" |
| **UJ** | Journey flow itself needs to change (not just the screen) | Update UJ-XXX in SoT.USER_JOURNEYS.md | "Users need a confirmation step before submit" |

## Disposition Rules

- **Accepted**: Update the target SoT ID immediately. Log the change.
- **Deferred**: Add to PRD Open Questions for the relevant stage. Note the SCR- ID it came from.
- **Rejected**: Note rationale in the feedback table. No SoT update needed.

## After Review Completion

1. All Accepted items have been applied to their SoT files
2. Regenerate Stitch prompts for any SCR- entries that changed materially
3. Re-review only changed screens (don't restart full review)
4. When all feedback is dispositioned → v0.4 Visual Prototype Gate passes

## Review Cadence

- **Minimum**: 1 review cycle with 1 stakeholder before advancing to v0.5
- **Recommended**: 2 cycles — first with product owner, second with a proxy user
- **Maximum before diminishing returns**: 3 cycles. If still iterating after 3, the problem is upstream (journey or persona definition needs work, not screens)
