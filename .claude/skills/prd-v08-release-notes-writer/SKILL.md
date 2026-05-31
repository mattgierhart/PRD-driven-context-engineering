---
name: prd-v08-release-notes-writer
description: >
  Write user-facing release notes from completed EPICs, deployment artifacts, and feature summaries during
  PRD v0.8 Deployment & Ops. Translates technical delivery into plain-language feature announcements for users and stakeholders.
  Triggers on requests to write release notes, announce a feature, draft a changelog, communicate what shipped,
  or when user asks "release notes", "what's new", "changelog", "feature announcement", "write the release notes",
  "communicate this release", "user-facing announcement".
  Consumes EPIC- completed entries, FEA-, DEP-, UJ-. Outputs structured release notes in multiple formats.
---

# Release Notes Writer

Position in workflow: v0.8 Release Planning → **v0.8 Release Notes Writer** → v0.9 GTM Strategy

This skill translates completed EPICs and deployment artifacts into **user-facing release notes** — what actually shipped, why it matters to users, and what they can do now that they couldn't before. It is explicitly separate from `prd-v08-release-planning` (which covers deployment strategy and go/no-go criteria) and from `prd-v09-gtm-strategy` (which covers launch messaging).

Release notes belong at the moment of deployment: after code ships but before the full GTM push.

## Consumes

This skill requires prior work from v0.7-v0.8:

- **EPIC-\* completed entries** (from v0.7 Implementation Loop) — What was built; EPIC titles, feature summaries, and deliverables define the raw material for release notes
- **FEA-\* feature entries** (from v0.3) — User-facing value description; the "why this matters" for each feature
- **DEP-\* deployment entries** (from v0.8 Release Planning) — Deployment scope, environment, and validation results that confirm what shipped
- **UJ-\* user journey entries** (from v0.4) — The user flow improved by the release; used to frame notes around what users can now accomplish
- **KPI-\* targets** (from v0.3) — Success metrics that the release aims to move; referenced in stakeholder summaries
- **MON-\* monitoring entries** (from v0.8 Monitoring Setup) — Known limitations or conditions that should appear as known issues

This skill assumes at least one EPIC is marked Complete with all TEST- passing and DEP- criteria met.

## Produces

This skill creates (saved in `temp/release-notes-[version]-[date].md` until harvested to an archive):

- **User-facing release notes** — Plain-language what's new, organized by user benefit (not technical component)
- **Stakeholder summary** — Executive version linking features to KPI- targets and business outcomes
- **In-app/email announcement draft** (optional) — Short-form content suitable for in-product notification or email
- **Changelog entry** — Technical changelog in standard format for developer audiences

## Release Notes Principles

1. **Write for users, not engineers** — "You can now export reports as PDF" not "Added PDF generation endpoint (API-045)"
2. **Lead with benefit, not feature** — "Save 3 hours per week on reporting" before "New export feature"
3. **One sentence per item** — If a feature needs three sentences to explain, the feature is being described, not communicated
4. **Known issues are trust-builders** — Documenting known limitations earns credibility; hiding them loses it
5. **Reference IDs in internal docs only** — FEA-, EPIC-, DEP- IDs appear in stakeholder summaries, not user-facing notes

---

## Step 1: Inventory What Shipped

For each completed EPIC in this release:

1. Read the EPIC file — capture: EPIC title, deliverables list, which FEA- entries it implements
2. Read the linked FEA- entries — capture: user-facing value description, priority tier
3. Read the UJ- entries impacted — capture: which step in the user journey improved
4. Check DEP- entries — confirm each EPIC's features actually shipped (DEP- validated = ✅)

**Shipping inventory table**:

```markdown
| EPIC | FEA- | What shipped | UJ- impacted | User benefit |
|---|---|---|---|---|
| EPIC-01 | FEA-003 | PDF export for reports | UJ-005 step 4 | Users can share reports externally |
| EPIC-02 | FEA-007 | Email digest for weekly summary | UJ-002 step 1 | Users get summary without logging in |
```

---

## Step 2: Draft User-Facing Release Notes

### Standard Format

```markdown
## What's New — [Product Name] [Version] | [Release Date]

### [Theme / Benefit Headline]

**[Feature name in plain language]**
[One sentence: what you can now do]
[One sentence: why it matters / time saved / problem solved]

**[Feature name in plain language]**
[One sentence: what you can now do]
[One sentence: why it matters / time saved / problem solved]

---

### Improvements

- [Small improvement 1] — [one-line benefit]
- [Small improvement 2] — [one-line benefit]

---

### Bug Fixes

- Fixed: [what was broken and is now fixed]
- Fixed: [what was broken and is now fixed]

---

### Known Issues

- [Issue description]: [Workaround if available, ETA for fix if known]
```

### Writing Rules

**Do**:
- Use active voice ("You can now...", "We fixed...", "Teams can...")
- Lead with the user action or outcome, not the technical implementation
- Group features by the user benefit they deliver, not by engineering EPIC
- Include "Known Issues" section even if short — it signals transparency

**Don't**:
- Use internal IDs (FEA-, EPIC-, API-) in user-facing notes
- Use engineering jargon ("endpoint", "migration", "schema", "refactor")
- Write more than 2 sentences per feature in user notes
- Promise future features in release notes (save for roadmap communication)

---

## Step 3: Draft Stakeholder Summary

The stakeholder summary is for internal leadership, investors, or board audiences. It connects the release to business outcomes.

```markdown
## Release Summary — [Product Name] [Version] | [Release Date]
**Release owner**: [PM name]
**Deployment confirmed**: [DEP- reference] ✅

### What Shipped

| Feature | EPIC | FEA- | Business Rationale |
|---|---|---|---|
| [Feature] | EPIC-XX | FEA-XX | [KPI- it moves and by how much] |

### KPI Impact Expected

| KPI | Current (KPI-XXX) | Target | Feature driving lift |
|---|---|---|---|
| [Metric] | [Current value] | [Target value] | [Feature name] |

### Known Issues / Caveats
- [Issue]: [Impact and mitigation]

### Next Release Preview
- [Brief preview of what's coming in the next release cycle]
```

---

## Step 4: Optional Short-Form Drafts

For in-product notifications or email announcements, write a 3-sentence version:

```markdown
SHORT-FORM DRAFT:

[Product name] just got [number] new [improvements / features / updates].
[Lead benefit in one sentence — what the most important change means for users.]
[CTA: "See what's new" / "Try it now" / "Learn more"]
```

---

## Step 5: Technical Changelog Entry

For developer audiences, API consumers, or open-source projects:

```markdown
## [Version] — [Date]

### Added
- [FEA-XXX] [Feature name]: [Technical description of what was added]

### Changed
- [FEA-XXX] [Feature name]: [What changed and why]

### Fixed
- [Bug description]: [Root cause and fix]

### Deprecated
- [API/feature]: [What to use instead, removal timeline]

### Breaking Changes
- None | [Description of breaking change and migration path]

### Known Issues
- [Issue]: [Workaround]
```

---

## Quality Gates

Before releasing to users:

- [ ] Every completed EPIC has at least one user-facing note (no EPIC is invisible to users)
- [ ] All FEA- items marked shipped in DEP- are represented in the notes
- [ ] Known issues from MON- entries are documented honestly
- [ ] No internal IDs appear in user-facing notes
- [ ] Stakeholder summary links every feature to a KPI-
- [ ] A named owner reviewed and approved the final draft
- [ ] Release notes are saved to `temp/` pending harvest to archive

## Anti-Patterns to Avoid

| Anti-Pattern | Signal | Fix |
|---|---|---|
| **Engineering-speak** | "Refactored the authentication layer" | "Sign-in is now faster and more reliable" |
| **Missing known issues** | All positives, no caveats | Include honest known issues section |
| **Feature dumping** | 15+ line items with no hierarchy | Group by theme or user benefit; highlight top 2-3 |
| **Internal ID leakage** | "FEA-003 now supports PDF export" | Remove all IDs from user-facing text |
| **Promise creep** | "Coming soon: [feature]" in release notes | Save future roadmap communication for product updates |
| **Passive voice** | "Reports can be exported as PDF by users" | "You can now export reports as PDF" |

## Downstream Connections

Release Notes feed into:

| Consumer | What It Uses | Example |
|---|---|---|
| **v0.9 GTM Strategy** | Feature announcement language | Release note headlines become GTM messaging inputs |
| **v0.9 Launch Metrics** | Confirmed shipped features | Launch metrics reference what actually shipped, not what was planned |
| **v1.0 Retention Analyzer** | Feature change log as context | Retention cohort analysis references which release cohorts used which features |
| **CFD- entries** | User reactions to announced features | User feedback on release notes feeds back to CFD- as post-launch signal |
