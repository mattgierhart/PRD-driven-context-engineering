# Harvest Patterns

**Purpose**: Decision framework for extracting temp/ insights to SoT, archiving context, and deleting noise.

---

## Harvest Philosophy

**Core Principle**: "Temp is scratch, SoT is durable"

**Why Harvest**:
- Prevent SoT contamination (methodology in templates)
- Preserve insights (don't lose learnings)
- Clean workspace (fresh start for next EPIC)

**When to Harvest**: End of EPIC Phase E (before closing EPIC)

---

## Three-Way Sort: Extract | Archive | Delete

### Extract → SoT (Durable Knowledge)

**Decision Rule**: "Will this be useful beyond this EPIC?"

**Examples**:
- ✅ User pain points (CFD)
- ✅ Architecture decisions (ARC, BR)
- ✅ API contracts (API)
- ✅ Customer quotes (CFD)
- ✅ Competitive insights (CFD)

**Anti-Examples**:
- ❌ "Tried approach X, didn't work" (contextual, archive instead)
- ❌ Daily progress notes (contextual, archive)
- ❌ Debugging session logs (noise, delete)

---

### Archive (Contextual Value)

**Decision Rule**: "Useful for retrospective, but not general SoT"

**Examples**:
- ✅ EPIC timeline (what happened when)
- ✅ Blockers and resolutions (how we solved issues)
- ✅ Team discussions (context for decisions)
- ✅ Experiment results (A/B test data)

**Archive Location**: `archive/YYYY-MM/epic-XXX-description.md`

**Purpose**: Post-mortem, team learning, future retrospectives

---

### Delete (No Future Value)

**Decision Rule**: "Will anyone ever need this again?"

**Examples**:
- ✅ Debug logs (issue resolved)
- ✅ Scratch calculations (final number in SoT)
- ✅ Duplicate notes (consolidated version in SoT)
- ✅ Superseded drafts (final version in SoT)

**Safety Check**: Review once before deletion (can't recover)

---

## Extraction Patterns

### Pattern 1: User Research → CFD

**Temp File**:
```markdown
# User Interview 5

Date: 2026-01-10
User: Sarah (Design Lead at startup)

Pain Points:
- "I spend 2 hours/day searching for design files" (frustrated)
- "Our team uses Dropbox, Figma, and Slack - files everywhere" (chaotic)

Needs:
- Unified search across tools
- Quick preview without downloading
```

**Extract to SoT**:
```markdown
# CFD-092: File Search Friction

**Type**: Pain Point
**Source**: User interview (Sarah, Design Lead, 2026-01-10)
**Evidence Tier**: Tier 1 (Direct quote)

**Pain**: "I spend 2 hours/day searching for design files across Dropbox, Figma, and Slack"

**Impact**:
- Time: 2 hours/day wasted (25% of workday)
- Emotion: Frustrated ("files everywhere")

**Implication**: Unified search is high-value feature
```

**Delete**: `temp/user-interview-5.md` (insights extracted)

---

### Pattern 2: Technical Decision → BR/ARC

**Temp File**:
```markdown
# Database Choice

Evaluated: PostgreSQL vs MongoDB

PostgreSQL Pros:
- Strong ACID guarantees
- Mature ecosystem
- Team familiar

MongoDB Pros:
- Schema flexibility
- Faster for document storage

Decision: PostgreSQL (data integrity > schema flexibility for our use case)
```

**Extract to SoT**:
```markdown
# BR-095: Database Technology Choice

**Decision**: PostgreSQL

**Alternatives Considered**: MongoDB

**Rationale**:
- ACID guarantees critical (financial data)
- Team expertise (faster development)
- Schema stability (known data model)

**Trade-off**: Less schema flexibility, but acceptable (data model stable)
```

**Delete**: `temp/database-choice.md` (decision captured in BR)

---

### Pattern 3: Experiment Result → Archive

**Temp File**:
```markdown
# A/B Test: Onboarding Flow

Variant A (Current): 40% activation
Variant B (New flow): 55% activation

Winner: Variant B
Rolled out: 2026-01-12
```

**Archive**:
```markdown
# archive/2026-01/ab-test-onboarding.md

[Same content]

Archived because:
- Experiment complete, winner chosen
- Useful for future onboarding changes (learn what worked)
- Not general SoT (specific to this time period)
```

**Do NOT Extract to SoT**: Time-bound experiment, not durable principle

---

### Pattern 4: Daily Notes → Archive or Delete

**Temp File**:
```markdown
# EPIC-012 Daily Log

Day 1: Started API design, blocked on auth token format
Day 2: Resolved auth, drafted endpoints
Day 3: Code review, updated schema
Day 4: Tests written, all passing
Day 5: Deployed to staging
```

**Archive**: `archive/2026-01/epic-012-daily-log.md`
- Useful for retrospective (understand blockers, timeline)
- Not SoT (too specific to this EPIC)

**Alternative**: Delete if no retrospective planned
- Only keep if post-mortem will reference it

---

## Common Mistakes

### Mistake 1: Extracting Noise to SoT

**Bad**:
```markdown
# CFD-093: User Said They Like Blue

User mentioned they prefer blue color scheme.
```

**Why Bad**: One user opinion ≠ pattern. Noise, not insight.

**Fix**: Only extract when pattern (3+ users) or high-impact single user

---

### Mistake 2: Deleting Insights

**Bad**: Delete temp file with unique customer quote before extracting to CFD

**Fix**: Always review temp files for extractable insights BEFORE deletion

---

### Mistake 3: Over-Archiving

**Bad**: Archive everything "just in case"

**Why Bad**: Archive becomes junk drawer (hard to find useful content)

**Fix**: Be selective. Only archive if future retrospective value.

---

### Mistake 4: Contaminating SoT with Context

**Bad**:
```markdown
# BR-096: API Rate Limit

We chose 1000 req/min after discussing with team on Slack.
Sarah thought 500, but John argued for 1000 because...
[3 paragraphs of deliberation]

Final decision: 1000 req/min
```

**Fix**:
```markdown
# BR-096: API Rate Limit

**Decision**: 1,000 requests/min

**Rationale**: Balance between UX (responsive) and cost (infrastructure)

**Alternatives Considered**: 500 req/min (too restrictive for power users)
```

**Archive team discussion separately** (if useful for retrospective)

---

## Harvest Workflow

### Step 1: Inventory (List All Temp Files)

```bash
ls temp/
```

Output:
```
epic-012-notes.md
user-interview-3.md
api-draft.md
debug-log.txt
```

---

### Step 2: Categorize (Extract | Archive | Delete)

| File | Category | Reason |
|------|----------|--------|
| `epic-012-notes.md` | Archive | Timeline useful for retro |
| `user-interview-3.md` | Extract → Delete | Extract pain point to CFD, then delete |
| `api-draft.md` | Extract → Delete | Migrate to API-045, then delete |
| `debug-log.txt` | Delete | No value (debug session) |

---

### Step 3: Extract Insights to SoT

- Create CFD-089 from user-interview-3.md
- Update API-045 from api-draft.md
- Document in harvest log

---

### Step 4: Archive Contextual Files

- Move `epic-012-notes.md` to `archive/2026-01/`
- Update archive manifest

---

### Step 5: Delete Noise

- Delete `debug-log.txt`
- Delete `user-interview-3.md` (after extracting CFD-089)
- Delete `api-draft.md` (after updating API-045)

---

### Step 6: Validate

- [ ] temp/ directory empty (clean slate)
- [ ] All insights in SoT (nothing lost)
- [ ] Archive manifest updated
- [ ] Harvest log complete

---

## Archive Organization

### Directory Structure

```
archive/
  2026-01/
    epic-012-notes.md
    ab-test-onboarding.md
    team-discussion-pricing.md
  2025-12/
    epic-008-notes.md
    user-research-summary.md
```

### Naming Convention

`YYYY-MM/epic-XXX-description.md` or `YYYY-MM/topic-description.md`

---

## Harvest Log Purpose

**Why Document Harvest**:
- Audit trail (what was deleted, why)
- Prevent accidental loss (reviewed before deletion)
- Team learning (patterns for next EPIC)

**Log Sections**:
1. Inventory (what files existed)
2. Categorization (extract/archive/delete decisions)
3. SoT updates (what was created/changed)
4. Archive manifest (what was preserved)
5. Deletion log (what was removed)

---

*Reference: Use these patterns when harvesting temp/ insights in `ghm-harvest` skill.*
