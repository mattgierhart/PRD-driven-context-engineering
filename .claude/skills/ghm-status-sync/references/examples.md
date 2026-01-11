# Status Sync Examples

**Purpose**: Good and bad patterns for README Command Center updates.

---

## Good Example: Weekly Status Update

### README Update (2026-01-11)

```markdown
# Product: DesignHub Command Center

**Last Updated**: 2026-01-11
**PRD Version**: v0.7 (Build Execution)
**Overall Health**: 🟢 On Track

---

## Current Status

**Phase**: Build Execution (v0.7)
**Progress**: 65% complete (13 of 20 EPICs done)
**Timeline**: On schedule for v0.8 gate (Jan 20)
**Next Milestone**: Complete EPIC-015 (User Preferences API) by Jan 15

---

## Active Work

**EPIC-015**: User Preferences API
- Status: In Progress (60% complete)
- Owner: Backend Team (Alice)
- Due: 2026-01-15
- Blockers: 0

**Deliverables**:
- [x] API contract (API-078)
- [x] Database schema (DBT-034)
- [ ] Implementation
- [ ] Tests (TEST-089, TEST-090)

---

## Metrics

**Development**:
- Test Coverage: 82% (↑ from 78% last week)
- Open Bugs: 12 (↓ from 15)
- P0/P1 Bugs: 1 (↓ from 3)

---

## Recent Changes

**Completed**:
- ✅ [2026-01-10] EPIC-012 (Dark Mode) - shipped to staging
- ✅ [2026-01-08] Passed internal code review

**Upcoming**:
- 📅 [2026-01-15] EPIC-015 completion
- 📅 [2026-01-20] v0.7 → v0.8 gate review

---

## Team Notes

**What's Going Well**:
- Test coverage trending up (82%, target 80%)
- Reduced bug count by 20%

**What Needs Attention**:
- 1 P0 bug remaining (database connection pool)
- Tech debt items growing (15 items, need cleanup sprint)
```

---

### Why This is Good

✅ **Specific numbers**: 65% complete, 82% coverage (not "making progress")
✅ **Trends shown**: ↑ coverage, ↓ bugs (context for numbers)
✅ **Timeline clear**: Jan 15, Jan 20 (concrete dates)
✅ **Actionable**: "Need cleanup sprint" (next action identified)

---

## Bad Example 1: Vague Update

### README Update (Bad)

```markdown
**Status**: Working on stuff
**Progress**: Going well
**Timeline**: Soon

We're building features and making progress. No major issues.
```

---

### Why This is Bad

❌ **No specifics**: "stuff", "well", "soon" (meaningless)
❌ **No numbers**: Can't track progress
❌ **No timeline**: When is "soon"?
❌ **No actionable items**: What needs attention?

---

## Good Example: Blocker Update

### README Update (Emergency)

```markdown
# Command Center

**Last Updated**: 2026-01-11 14:30
**Overall Health**: 🔴 BLOCKED
**Update Reason**: Critical blocker emerged

---

## CRITICAL BLOCKER

**BLOCKER-1**: Database migration failed in staging
- Impact: Blocks v0.7 → v0.8 gate (delayed 3 days)
- Root Cause: 10M record migration took 4 hours (timeout at 2 hours)
- Owner: Database Team (Bob)
- Due: 2026-01-13
- Status: In Progress

**Mitigation**:
- [ ] Split migration into batches (1M at a time)
- [ ] Run migration off-peak hours
- [ ] Test in staging clone (today)
- [ ] Re-run in staging (Jan 12)
- [ ] Gate review moved to Jan 23 (was Jan 20)

---

## Timeline Impact

**Original**: v0.8 gate Jan 20 → Launch Feb 1
**Revised**: v0.8 gate Jan 23 → Launch Feb 4

**Risk**: If mitigation fails, additional 1-week delay
```

---

### Why This is Good

✅ **Immediate update**: Same day blocker emerged
✅ **Health changed**: 🟢 → 🔴 (signals urgency)
✅ **Specific blocker**: Database migration (not "technical issues")
✅ **Timeline impact**: 3-day delay quantified
✅ **Mitigation plan**: Concrete steps with dates

---

## Bad Example 2: Stale Status

### README (Not Updated)

```markdown
**Last Updated**: 2025-12-15 (27 days ago)
**Phase**: v0.6 (Architecture)
**Status**: 🟢 On Track
```

**Actual State** (2026-01-11):
- Phase: v0.8 (Deployment)
- Status: 🔴 Blocked (migration issue)
- 2 gates passed since last update

---

### Why This is Bad

❌ **Stale**: 27 days old (meaningless)
❌ **Wrong phase**: Still showing v0.6 (actual: v0.8)
❌ **Wrong status**: Shows 🟢 (actual: 🔴)
❌ **Missing context**: Team operating blind

**Fix**: Sync at least weekly, immediately on blockers

---

## Good Example: Launch Metrics Update

### README Update (Post-Launch Week 1)

```markdown
# DesignHub Command Center

**Last Updated**: 2026-01-11
**PRD Version**: v1.0 (Launched!)
**Overall Health**: 🟡 At Risk
**Launch Date**: 2026-01-04

---

## Launch Metrics (7 Days)

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Signups | 1,000 | 1,234 | 🟢 123% |
| Activation | 40% | 35% | 🟡 88% |
| D7 Retention | 40% | 32% | 🟡 80% |
| NPS | 40 | 35 | 🟡 88% |
| MRR | $10k | $12k | 🟢 120% |

**Overall**: 🟡 At Risk (2 metrics below target)

---

## Action Items

**Activation (35% vs 40%)**:
- Issue: Users not completing onboarding step 3
- Action: A/B test new onboarding flow (launching today)
- Owner: Product Team (Sarah)
- Target: 40% by Week 2

**D7 Retention (32% vs 40%)**:
- Issue: Users trying once, not returning
- Action: Email drip campaign (Days 1, 3, 7)
- Owner: Growth Team (John)
- Target: 35% by Week 2, 40% by Week 4

---

## Next Review

**Date**: 2026-01-18 (1 week)
**Focus**: Did activation/retention improve?
```

---

### Why This is Good

✅ **Metrics table**: Easy to scan (target vs actual)
✅ **Status indicators**: 🟢/🟡 (visual health)
✅ **Action items**: Specific fixes with owners and targets
✅ **Weekly cadence**: Next review date set

---

## Update Frequency Patterns

### Good Pattern: Phase-Appropriate

| Phase | Update Frequency | Rationale |
|-------|------------------|-----------|
| Planning (v0.1-v0.3) | Weekly | Decisions made frequently |
| Design (v0.4-v0.6) | Bi-weekly | Steady progress |
| Build (v0.7) | Weekly | Active development |
| Deploy (v0.8) | Daily | Critical phase |
| Launch (v0.9-v1.0) | Daily (Week 1), Weekly (after) | Metrics monitoring |

---

### Bad Pattern: Inconsistent

- Week 1: Updated daily
- Week 2: No updates
- Week 3: Updated once
- Week 4: No updates

**Problem**: Team doesn't know if status is current

**Fix**: Set cadence, stick to it

---

## Status Sync Checklist

Before syncing:

- [ ] Gather latest data (gate, EPIC, metrics)
- [ ] Calculate changes since last update
- [ ] Identify blockers and risks
- [ ] Review team notes

During sync:

- [ ] Update "Last Updated" date
- [ ] Update phase and health indicator
- [ ] Update progress percentages
- [ ] Update blockers list
- [ ] Update metrics (if applicable)
- [ ] Update recent changes
- [ ] Update team notes

After sync:

- [ ] Commit to README.md
- [ ] Notify team (if major change)
- [ ] Schedule next sync

---

*Reference: Use these examples when syncing README status in `ghm-status-sync` skill.*
