# Harvest Examples

**Purpose**: Good and bad patterns for harvesting temp/ insights to SoT.

---

## Good Example: Comprehensive Harvest

### Temp Files (Before)

```
temp/
  epic-015-notes.md (8KB)
  user-research-findings.md (12KB)
  api-schema-draft.md (4KB)
  pricing-discussion.md (6KB)
  debug-session-2026-01-10.log (15KB)
```

### Harvest Decisions

**epic-015-notes.md → Archive**
- Reason: Timeline, blockers, daily progress (useful for retro)
- Action: Move to `archive/2026-01/epic-015-notes.md`

**user-research-findings.md → Extract & Delete**
- Extract: 3 pain points to CFD-090, CFD-091, CFD-092
- Extract: 2 customer quotes (used in CFD entries)
- Delete: After extraction (insights preserved)

**api-schema-draft.md → Extract & Delete**
- Extract: Final schema to API-046 (User Preferences API)
- Delete: Draft superseded by final spec

**pricing-discussion.md → Extract & Archive**
- Extract: Final decision to BR-097 (Pricing Model: $50/mo)
- Archive: Team discussion (useful context for why we chose $50)

**debug-session-2026-01-10.log → Delete**
- Reason: Debugging logs (issue resolved, no future value)

### SoT Updates

**Created**:
- CFD-090: Onboarding confusion (Tier 1 evidence)
- CFD-091: Export feature request (Tier 2 evidence)
- CFD-092: Mobile app demand (Tier 1 evidence)
- BR-097: Pricing Model

**Updated**:
- API-046: Added final schema (from draft)

### Post-Harvest

**temp/**:
- Before: 5 files, 45KB
- After: 0 files, 0KB ✅

**SoT**:
- New IDs: 4
- Updated IDs: 1

**Archive**:
- epic-015-notes.md
- pricing-discussion.md

---

## Bad Example 1: No Extraction (Lost Insights)

### Temp Files (Before)

```
temp/
  user-interviews.md (20KB - contains 5 interviews with pain points)
  competitive-analysis.md (10KB - detailed competitor breakdown)
```

### Harvest (Bad)

**Action**: Deleted both files without review

**Result**:
- ❌ Lost 5 user pain points (no CFD entries created)
- ❌ Lost competitive insights (no CFD entries)
- ❌ Can't recover (files deleted)

### Fix

**Should Have**:
1. Reviewed user-interviews.md
2. Extracted each pain point to CFD-XXX
3. THEN deleted temp file

---

## Bad Example 2: Contaminating SoT

### Temp File

```markdown
# temp/pricing-decision.md

Team meeting 2026-01-10:
- Sarah suggested $50/mo
- John said $30/mo
- Discussed for 2 hours
- Looked at competitors: Asana ($30), Monday ($40), ClickUp ($35)
- Debated value vs cost
- Sarah won argument
- Final: $50/mo
```

### Bad Extraction

```markdown
# BR-097: Pricing Model

Team met on 2026-01-10. Sarah suggested $50/mo but John said $30/mo.
We discussed for 2 hours. We looked at competitors: Asana ($30), Monday ($40), ClickUp ($35).
We debated value vs cost. Sarah won the argument.
Final decision: $50/mo.
```

**Why Bad**: SoT contaminated with process, debate, names (not reusable)

### Good Extraction

**SoT (BR-097)**:
```markdown
# BR-097: Pricing Model

**Decision**: $50/month (per user)

**Rationale**:
- Positioned above mid-market ($30-40 range)
- Justifies premium features (advanced reporting, integrations)
- Competitive with high-end ($50-60 range: Asana Business)

**Alternatives Considered**:
- $30/mo: Too low (signals lower quality)
- $70/mo: Too high (limited market)
```

**Archive (pricing-discussion.md)**:
```markdown
[Full team discussion, debate, timeline]

Archived for: Retrospective on how we make pricing decisions
```

---

## Good Example: Selective Archiving

### Temp Files

```
temp/
  epic-020-timeline.md (progress log)
  epic-020-retro-notes.md (lessons learned)
  temp-calculation.txt (intermediate math)
```

### Decisions

**epic-020-timeline.md → Archive**
- Reason: Useful for post-mortem (blockers, how long tasks took)
- Action: `archive/2026-01/epic-020-timeline.md`

**epic-020-retro-notes.md → Extract & Delete**
- Extract: Lessons to team wiki or EPIC template updates
- Example: "In-app prompts drive 3x adoption vs email" → Update GTM playbook
- Delete: After extracting lessons

**temp-calculation.txt → Delete**
- Reason: Intermediate work (final number in SoT, don't need steps)

---

## Bad Example 3: Over-Archiving

### Bad Pattern

**Archive Everything "Just in Case"**:
```
archive/2026-01/
  debug-log-1.txt
  debug-log-2.txt
  scratch-notes.md
  random-thoughts.md
  temp-file-1.md
  temp-file-2.md
  [50 more files]
```

**Why Bad**:
- Archive becomes junk drawer
- Hard to find useful content
- No discrimination (noise alongside signal)

### Good Pattern

**Be Selective**:
```
archive/2026-01/
  epic-020-timeline.md (retro value)
  pricing-discussion.md (decision context)
  ab-test-results.md (future learning)
```

**Delete the Rest**: Debug logs, scratch notes, intermediate work

---

## Harvest Checklist (Good Pattern)

### Before Harvest

- [ ] List all temp/ files
- [ ] Scan each for extractable insights
- [ ] Categorize: Extract | Archive | Delete

### During Harvest

- [ ] Extract durable insights to SoT
- [ ] Create/update IDs with proper cross-references
- [ ] Move contextual files to archive (with manifest entry)
- [ ] Delete noise (with confirmation)

### After Harvest

- [ ] temp/ directory empty ✅
- [ ] SoT updated (all insights preserved) ✅
- [ ] Archive documented (manifest) ✅
- [ ] Harvest log complete ✅

---

*Reference: Use these examples when harvesting insights in `ghm-harvest` skill.*
