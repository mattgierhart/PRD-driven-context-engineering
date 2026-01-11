# Status Sync Triggers

**Purpose**: When to update README Command Center status.

---

## Automatic Triggers (Must Sync)

### Trigger 1: Gate Status Change

**When**: Passing or blocking any PRD lifecycle gate

**Update**:
- Gate status (passed/blocked/conditional)
- Current PRD version
- Blockers (if blocked)
- Next milestone

**Frequency**: Immediately after gate check

---

### Trigger 2: EPIC Status Change

**When**: EPIC starts, completes, or gets blocked

**Update**:
- Active EPIC
- Progress percentage
- Blockers (if any)
- Timeline adjustment

**Frequency**: When EPIC state changes

---

### Trigger 3: Critical Blocker

**When**: P0/P1 blocker emerges that delays gate or launch

**Update**:
- Blocker list
- Overall health (change to 🔴 Blocked)
- Timeline impact
- Mitigation plan

**Frequency**: Immediately when blocker identified

---

### Trigger 4: Launch Metrics Change

**When**: Post-launch, metrics significantly change

**Update**:
- Metrics dashboard
- Health status (if metrics below target)
- Action items

**Frequency**: Daily (first week), weekly (after)

**Significant Change**: >10% deviation from target

---

## Scheduled Triggers (Should Sync)

### Trigger 5: Weekly Sync

**When**: Every Monday 9 AM (or weekly team sync)

**Update**:
- Progress indicators
- ID creation activity
- Recent changes
- Upcoming milestones

**Frequency**: Weekly

---

### Trigger 6: End of Sprint

**When**: Sprint retrospective or planning

**Update**:
- Completed work
- Sprint metrics
- Next sprint plan
- Team notes (what's going well, what needs attention)

**Frequency**: Bi-weekly (or sprint cadence)

---

### Trigger 7: Monthly Review

**When**: First Monday of month

**Update**:
- Full status review
- Metrics trends (vs last month)
- Roadmap adjustments
- Stakeholder communication

**Frequency**: Monthly

---

## Optional Triggers (Good to Sync)

### Trigger 8: Major Decision

**When**: Product/technical decision with PRD impact

**Update**:
- Team notes (decisions made)
- Impact on timeline or scope

**Example Decisions**:
- Pricing change
- Scope cut
- Architecture change

---

### Trigger 9: Team Change

**When**: Team member joins/leaves, ownership changes

**Update**:
- EPIC ownership
- Blocker ownership
- Contact information

---

### Trigger 10: External Dependency

**When**: Waiting on external team/vendor

**Update**:
- Blocker list (external dependency)
- Timeline impact
- Alternative plan (if dependency delays)

---

## Sync Frequency by Phase

| PRD Phase | Sync Frequency | Reason |
|-----------|----------------|--------|
| **v0.1-v0.3** (Planning) | Weekly | High decision rate |
| **v0.4-v0.6** (Design) | Bi-weekly | Steady progress |
| **v0.7** (Build) | Weekly | Active development |
| **v0.8** (Deployment) | Daily | Critical phase |
| **v0.9-v1.0** (Launch) | Daily (first week), then weekly | Metrics monitoring |

---

## Sync Checklist

Before syncing:

- [ ] Collect latest data (gate status, EPIC progress, metrics)
- [ ] Identify changes since last update
- [ ] Update dashboard numbers
- [ ] Flag blockers/risks
- [ ] Review team notes

During sync:

- [ ] Update Current Status section
- [ ] Update Progress Indicators
- [ ] Update Blockers & Risks
- [ ] Update Metrics (if applicable)
- [ ] Update Recent Changes
- [ ] Update Team Notes

After sync:

- [ ] Commit changes to README.md
- [ ] Notify team (Slack/email if major change)
- [ ] Schedule next sync

---

## Red Flags (Sync Immediately)

🚨 **Immediate Sync Needed**:
- Gate blocked (can't advance)
- Launch metrics 50%+ below target
- P0 bug in production
- Team member departure (blocking progress)
- External dependency delayed >1 week

---

*Reference: Use these triggers to determine when to sync status in `ghm-status-sync` skill.*
