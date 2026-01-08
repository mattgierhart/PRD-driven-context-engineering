# Feature Value Planning Examples

## Good Examples

### Example 1: Fast Follow — Scheduling Tool

**Context**: Building a Calendly alternative for freelancers

**Feature Set (ordered by priority)**:
```
FEA-001: Calendar Sync (Parity, P0)
- Parity with Calendly, required for basic function
- Links: KPI-001 (activation), CFD-003 (competitor audit)

FEA-002: Custom Booking Page (Parity, P0)  
- Table stakes for category
- Links: KPI-002 (trial→paid), CFD-003

FEA-003: Unlimited Event Types (Delta, P0)
- Calendly charges extra; our moat = unlimited free
- Links: BR-008 (moat: no artificial limits), CFD-007 (pricing complaints)

FEA-004: Client Notes (Tier, P1)
- Pro tier differentiator
- Links: BR-012 (Pro tier), KPI-004 (upgrade rate)
```

**Why it works**:
- Parity features establish category credibility (P0)
- Single delta feature is compelling and defensible (unlimited vs. limits)
- Tier feature supports monetization without blocking adoption
- All features have explicit traceability

### Example 2: Slice — Field Service CRM

**Context**: Building CRM slice for HVAC technicians (incumbent: Salesforce)

**Feature Set**:
```
FEA-001: Mobile-First Job Cards (Delta, P0)
- Salesforce is desktop-first; technicians need mobile
- Links: KPI-001 (TTFV), BR-002 (moat: mobile-native), CFD-011

FEA-002: Offline Sync (Delta, P0)
- Technicians in basements/attics lose signal
- Links: KPI-003 (completion rate), BR-002, CFD-015

FEA-003: Basic Contact Management (Parity, P1)
- 20% of Salesforce features for 80% of use cases
- Links: CFD-008 (feature audit—only contact basics used)

FEA-004: Equipment History Lookup (Delta, P1)
- Niche-specific; Salesforce doesn't have
- Links: CFD-018 (user interviews), KPI-005 (repeat booking rate)
```

**Why it works**:
- Delta features are P0 because differentiation IS the value
- Parity is minimal (20% match, not 100%)
- Niche-specific features serve the segment deeply
- Evidence hierarchy: High for delta, Medium for parity

### Example 3: Innovation — New Category

**Context**: Building AI meeting note-taker before category existed

**Feature Set**:
```
FEA-001: Auto-Transcription (Moat, P0)
- Core technology = moat (proprietary model)
- Links: BR-001 (moat: AI accuracy), KPI-001 (activation)

FEA-002: Action Item Extraction (Moat, P0)
- AI capability competitors can't easily match
- Links: BR-001, KPI-003 (feature stickiness)

FEA-003: Calendar Integration (Table Stakes, P1)
- Expected by users, but not differentiation
- Links: CFD-022 (user feedback)

FEA-004: Slack Notifications (Table Stakes, P2)
- Nice but not blocking adoption
- Links: N/A (defer to backlog)
```

**Why it works**:
- Moat features are 60%+ of scope
- Table stakes minimized to essentials
- Clear distinction: AI capabilities = moat; integrations = table stakes

---

## Bad Examples

### Bad Example 1: Feature Creep

**Context**: MVP for task management tool

**Problematic Feature Set**:
```
FEA-001: Task Creation (Table Stakes, P0)
FEA-002: Due Dates (Table Stakes, P0)
FEA-003: Recurring Tasks (Parity, P1)
FEA-004: Custom Themes (P2)
FEA-005: Gamification Badges (P2)
FEA-006: Social Sharing (P2)
FEA-007: AI Task Suggestions (P2)
FEA-008: Voice Input (P2)
FEA-009: Widget Support (P2)
FEA-010: Analytics Dashboard (P2)
```

**What went wrong**:
- P2 features outnumber P0/P1 (6 vs 4 = 60% bloat)
- No delta feature — nothing differentiating
- No moat features — easy to replicate
- FEA-004–010 have no KPI- or CFD- links

**Fix**: Cut FEA-004–010; add one compelling delta feature with moat traceability.

### Bad Example 2: Orphaned Features

**Context**: E-commerce platform

**Problematic entry**:
```
FEA-015: Advanced Analytics Dashboard
Type: Tier (Pro)
Priority: P1
Description: Shows sales trends and customer insights
Outcome Link: N/A
Moat Link: N/A
Pricing Link: N/A
Competitor Comparison: "Similar to others"
Validation: "Marketing thinks it's important"
```

**What went wrong**:
- No KPI- link (doesn't support success metric)
- No BR- link (doesn't support moat or pricing)
- Vague competitor comparison
- Validation is assumption, not evidence

**Fix**: Either find CFD- evidence and link to KPI-, or demote to P2/cut.

### Bad Example 3: Implementation as Feature

**Problematic entry**:
```
FEA-022: Use Redis for Session Management
Type: Table Stakes
Priority: P1
Description: Implement Redis caching layer for sessions
```

**What went wrong**:
- This is an implementation detail, not a user-facing feature
- Users don't know/care about Redis
- No testable user outcome

**Fix**: Reframe as user outcome: "FEA-022: Sub-100ms Page Loads — Fast session retrieval for snappy UX"

### Bad Example 4: Parity Inflation

**Context**: Fast-follow CRM tool

**Problematic pattern**:
- 47 features all marked "Parity, P0"
- Rationale: "Salesforce has it, so we need it"

**What went wrong**:
- Not all incumbent features are actually used
- No differentiation (why switch to an identical product?)
- Scope bloat guarantees missed deadlines

**Fix**: 
1. Audit competitor features by actual usage (CFD- research)
2. Apply 80/20: which 20% of features serve 80% of use cases?
3. Reserve 20% of scope for delta features

---

## Pattern: Feature-to-Strategy Traceability

**Minimum viable traceability** (every P0/P1 feature needs at least one):

| Feature Type | Required Links |
|--------------|----------------|
| Moat | BR- (moat rule) |
| Outcome | KPI- (success metric) |
| Parity | CFD- (competitor evidence) |
| Delta | CFD- (gap evidence) + BR- (moat, if defensible) |
| Tier | BR- (pricing tier) |
| Table Stakes | None required (but justify inclusion) |

**Orphan test**: If a feature has no KPI-, BR-, or CFD- link, it needs justification or removal.
