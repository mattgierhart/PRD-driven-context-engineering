# Gate Validation Checklist: v0.X → v0.Y

**PRD Version**: v0.X (Current) → v0.Y (Target)
**Product**: [Product Name]
**Date**: YYYY-MM-DD
**Validated By**: [Name]
**Status**: [Pass | Blocked | Conditional Pass]

---

## Gate Criteria

### Mandatory Artifacts (Must Have ALL)

- [ ] **PRD Document**
  - Version: v0.Y
  - Last updated: [Date]
  - Location: [Path]
  - Status: Complete

- [ ] **Source of Truth (SoT) IDs**
  - Required ID types: [List based on gate]
  - Count: [X required, Y created]
  - All IDs validated: [Yes/No]

- [ ] **Cross-References**
  - All IDs have valid relationships
  - No orphan IDs
  - No broken references

---

## Gate-Specific Checks

### v0.1 → v0.2 (Spark → Market Definition)

**Mandatory**:
- [ ] At least 3 CFD-XXX entries (customer pain points with evidence)
- [ ] Problem statement clearly defined in PRD v0.1
- [ ] Value hypothesis articulated (what user gains)

**Quality Checks**:
- [ ] Pain points backed by evidence (user interviews, surveys, support tickets)
- [ ] Evidence rated (Tier 1/2/3 - see CFD template)
- [ ] Problem quantified (frequency, severity, willingness to pay)

**Blocker Conditions**:
- ❌ No CFD entries (no validated problem)
- ❌ Problem too vague ("users want better tools")
- ❌ No evidence (hunches, not data)

---

### v0.2 → v0.3 (Market Definition → Commercial Model)

**Mandatory**:
- [ ] Competitive landscape mapped (CFD-XXX for each competitor)
- [ ] Product type classified (BR-XXX: Clone/Unbundle/Undercut/Slice/Wrapper/Innovation)
- [ ] Positioning defined relative to competitors

**Quality Checks**:
- [ ] At least 3 competitors analyzed
- [ ] Competitive advantages identified (not just features)
- [ ] Switching costs understood (why users will move)

**Blocker Conditions**:
- ❌ No competitive analysis (don't know the market)
- ❌ Product type unclear (strategy implications unknown)
- ❌ No differentiation ("we're better" without specifics)

---

### v0.3 → v0.4 (Commercial Model → User Journeys)

**Mandatory**:
- [ ] Pricing model defined (BR-XXX)
- [ ] Success metrics defined (KPI-XXX for each key outcome)
- [ ] Moat/defensibility analyzed (CFD-XXX)
- [ ] Features prioritized with strategic traceability (FEA-XXX)

**Quality Checks**:
- [ ] Pricing model validated (competitor comparison, willingness to pay)
- [ ] KPIs have thresholds (success/caution/failure criteria)
- [ ] Moat is defensible (not just "first mover advantage")
- [ ] Features tied to business rules and outcomes

**Blocker Conditions**:
- ❌ No pricing model (how will we make money?)
- ❌ No KPIs (how do we measure success?)
- ❌ Features not prioritized (building everything)

---

### v0.4 → v0.5 (User Journeys → Red Team)

**Mandatory**:
- [ ] Personas defined (PER-XXX)
- [ ] User journeys mapped (UJ-XXX for critical paths)
- [ ] Screen flows defined (SCR-XXX)
- [ ] Journeys connect features to personas

**Quality Checks**:
- [ ] At least 1 primary persona (detailed behavioral profile)
- [ ] At least 3 critical user journeys (trigger → value moment)
- [ ] Screen flows complete (all journeys have screens)
- [ ] Pain points and value moments identified in journeys

**Blocker Conditions**:
- ❌ No personas (who are we building for?)
- ❌ No journeys (how do users achieve outcomes?)
- ❌ Journeys don't match features (disconnect)

---

### v0.5 → v0.6 (Red Team → Architecture)

**Mandatory**:
- [ ] Risk assessment complete (RISK-XXX)
- [ ] Technical stack selected (TECH-XXX)
- [ ] Build/buy/integrate decisions made

**Quality Checks**:
- [ ] At least 5 risks identified (technical, market, execution)
- [ ] Each risk has mitigation plan
- [ ] Stack selections have rationale (not just "familiar tech")
- [ ] Build vs buy justified (cost, time, strategic value)

**Blocker Conditions**:
- ❌ No risk assessment (blind spots)
- ❌ Stack selected without justification
- ❌ No build vs buy analysis (over-engineering or under-utilizing)

---

### v0.6 → v0.7 (Architecture → Build)

**Mandatory**:
- [ ] Architecture design documented (ARC-XXX)
- [ ] API contracts defined (API-XXX)
- [ ] Data models defined (DBT-XXX)
- [ ] Component relationships clear

**Quality Checks**:
- [ ] Architecture decisions have trade-off analysis
- [ ] API contracts match user journeys and features
- [ ] Data models support all features
- [ ] Dependencies and boundaries documented

**Blocker Conditions**:
- ❌ No architecture design (how will system work?)
- ❌ APIs don't cover all user journeys
- ❌ Data models incomplete

---

### v0.7 → v0.8 (Build → Deployment)

**Mandatory**:
- [ ] EPICs scoped (EPIC-XXX)
- [ ] Test plans defined (TEST-XXX)
- [ ] Code implementation complete with traceability (@implements tags)
- [ ] All tests passing

**Quality Checks**:
- [ ] EPICs fit in context windows (not too large)
- [ ] Every API and BR has test coverage
- [ ] Code traceability (each major unit references IDs)
- [ ] No critical bugs

**Blocker Conditions**:
- ❌ No EPICs (work not scoped)
- ❌ No tests (can't verify correctness)
- ❌ Tests failing
- ❌ Missing traceability (can't tie code to specs)

---

### v0.8 → v0.9 (Deployment → GTM)

**Mandatory**:
- [ ] Deployment plan (DEP-XXX)
- [ ] Runbooks created (RUN-XXX)
- [ ] Monitoring setup (MON-XXX)

**Quality Checks**:
- [ ] Deployment plan has rollback strategy
- [ ] Runbooks tested (not theoretical)
- [ ] Monitoring covers critical paths
- [ ] SLOs defined for production

**Blocker Conditions**:
- ❌ No deployment plan (how will we ship?)
- ❌ No runbooks (how to handle incidents?)
- ❌ No monitoring (flying blind in production)

---

### v0.9 → v1.0 (GTM → Launch)

**Mandatory**:
- [ ] GTM strategy (GTM-XXX)
- [ ] Launch metrics defined (KPI-XXX)
- [ ] Feedback loop setup (channels for user input)

**Quality Checks**:
- [ ] GTM strategy matches product type (see BR-XXX)
- [ ] Launch metrics are actionable (not vanity)
- [ ] Feedback channels monitored (support, NPS, user interviews)

**Blocker Conditions**:
- ❌ No GTM plan (how will users find us?)
- ❌ No launch metrics (how measure success?)
- ❌ No feedback loop (can't iterate post-launch)

---

## Overall Gate Status

### Pass Criteria

**Green (Pass)**:
- ✅ All mandatory artifacts present
- ✅ All quality checks met
- ✅ No blocker conditions
- ✅ Cross-references validated
- ✅ SoT updated (no temp/ contamination)

**Action**: Advance to next PRD version

---

### Conditional Pass Criteria

**Yellow (Pass with Conditions)**:
- ⚠️ All mandatory artifacts present
- ⚠️ 80%+ quality checks met
- ⚠️ No blocker conditions
- ⚠️ Minor issues documented (to fix in next phase)

**Action**: Advance, but address issues within 1 week

**Conditions**:
- [ ] [Issue 1 to fix]
- [ ] [Issue 2 to fix]

---

### Blocked Criteria

**Red (Blocked)**:
- ❌ Missing mandatory artifacts, OR
- ❌ < 80% quality checks met, OR
- ❌ Blocker condition present

**Action**: DO NOT ADVANCE until resolved

**Blockers**:
- [ ] [Blocker 1 - specific issue]
- [ ] [Blocker 2 - specific issue]

**Resolution Plan**:
- Owner: [Who will fix]
- Timeline: [When fixed]
- Re-check: [Date for re-validation]

---

## Sign-Off

**Validated By**: [Name]
**Date**: YYYY-MM-DD
**Decision**: [Pass | Conditional Pass | Blocked]

**Comments**:
[Any additional notes, context, or recommendations]

---

*Template: Use this checklist before advancing PRD versions in `ghm-gate-check` skill.*
