# Harvest Log: EPIC-XXX

**EPIC**: EPIC-XXX - [Epic Name]
**Date**: YYYY-MM-DD
**Harvested By**: [Name]
**Status**: [Complete | Partial | Pending]

---

## Harvest Summary

**Temp Files Reviewed**: [Count]
**Insights Extracted**: [Count]
**SoT Entries Created/Updated**: [Count]
**Archived Files**: [Count]
**Deleted Files**: [Count]

---

## Temp File Inventory

| File | Type | Size | Last Modified | Disposition |
|------|------|------|---------------|-------------|
| `temp/epic-012-notes.md` | Scratchpad | 2KB | 2026-01-10 | Extract → Archive |
| `temp/user-interview-3.md` | Research | 5KB | 2026-01-09 | Migrate to CFD → Delete |
| `temp/api-draft.md` | Spec | 3KB | 2026-01-08 | Migrate to API → Delete |
| `temp/debug-log.txt` | Debug | 10KB | 2026-01-11 | Delete (no value) |

---

## Extraction Decisions

### Extract to SoT (Durable Insights)

**Decision Rule**: Information with reuse value beyond this EPIC

**File**: `temp/user-interview-3.md`
**Extract**:
- Pain point: "Users confused by onboarding step 3" (15 min avg time, should be < 2 min)
- Quote: "I didn't know where to click next"
- **Action**: Create CFD-089 (Onboarding friction - step 3)

**File**: `temp/api-draft.md`
**Extract**:
- Final API contract for user preferences endpoint
- **Action**: Update API-045 with finalized schema

**File**: `temp/epic-012-notes.md`
**Extract**:
- Architecture decision: Chose Redis for session storage (evaluated vs Memcached, Redis supports persistence)
- **Action**: Update ARC-023 with decision rationale

---

### Archive (Contextual Value)

**Decision Rule**: Useful for retrospective, but not reusable as SoT

**File**: `temp/epic-012-notes.md`
**Reason**: Contains timeline, blockers, day-by-day progress (useful for post-mortem, not general SoT)
**Action**: Move to `archive/2026-01/epic-012-notes.md`

---

### Delete (No Future Value)

**Decision Rule**: Noise, superseded, or debug artifacts

**File**: `temp/debug-log.txt`
**Reason**: Debugging session logs (issue resolved, no longer relevant)
**Action**: Delete

**File**: `temp/user-interview-3.md`
**Reason**: After extracting CFD-089, raw interview notes have no additional value
**Action**: Delete (insights preserved in CFD)

---

## SoT Updates Made

### Created IDs

**CFD-089: Onboarding Friction - Step 3**
- Type: Customer Feedback (Pain Point)
- Evidence Tier: Tier 1 (Direct user quote)
- Source: User interview #3
- Impact: 15 min avg time (vs 2 min target)
- Action: Redesign step 3 with clearer CTA

**BR-091: Session Storage Technology**
- Type: Business Rule (Technical Decision)
- Decision: Redis (vs Memcached)
- Rationale: Need persistence for session recovery
- Trade-off: Slightly higher cost, better reliability

---

### Updated IDs

**API-045: User Preferences Endpoint**
- Added: Final schema (previously draft)
- Changed: Response format (nested preferences object)

**ARC-023: Session Management Architecture**
- Added: Technology choice (Redis)
- Added: Decision rationale

---

## Archive Manifest

**Files Moved to Archive**:
- `archive/2026-01/epic-012-notes.md` (16KB, epic progress log)

**Archive Purpose**: Post-mortem reference, team retrospective

---

## Deletion Log

**Files Deleted** (Cannot Recover):
- `temp/debug-log.txt` (10KB, no value)
- `temp/user-interview-3.md` (5KB, extracted to CFD-089)

**Confirmation**: ✅ Reviewed for extractable insights before deletion

---

## Validation Checklist

- [ ] All temp files reviewed (none skipped)
- [ ] Durable insights extracted to SoT
- [ ] SoT IDs validated (no orphans, cross-references correct)
- [ ] Archive files documented (manifest entry)
- [ ] Deletions confirmed (no accidental loss)
- [ ] temp/ directory clean (ready for next EPIC)

---

## Post-Harvest State

**Temp Directory**:
- Before: 4 files, 20KB
- After: 0 files, 0KB ✅

**SoT Additions**:
- New IDs: 2 (CFD-089, BR-091)
- Updated IDs: 2 (API-045, ARC-023)

**Archive**:
- New files: 1 (epic-012-notes.md)

---

## Lessons for Next EPIC

**What Worked**:
- Daily scratch notes in temp/ (easy to extract later)
- Consistent file naming (`epic-XXX-topic.md`)

**What to Improve**:
- Mark "TO SoT" inline in temp files (faster harvest)
- Delete debug logs sooner (don't accumulate noise)

---

*Template: Use this log to document harvest process after EPIC completion in `ghm-harvest` skill.*
