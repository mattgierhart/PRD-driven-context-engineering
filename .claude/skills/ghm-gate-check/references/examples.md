# Gate Check Examples

**Purpose**: Good and bad patterns for gate validation with pass/fail scenarios.

---

## Good Example: v0.2 → v0.3 Gate Pass

### Context
Project management tool for design teams

### Artifacts Submitted

**Competitive Analysis (CFD)**:
- CFD-021: Figma (strengths: design integration, weaknesses: weak project management)
- CFD-022: Asana (strengths: robust PM, weaknesses: no design tools)
- CFD-023: Notion (strengths: flexible, weaknesses: not design-specific)

**Product Type (BR-012)**:
- Classification: Unbundle
- Rationale: Extract project management from generic tools, specialize for designers

**Positioning**:
- Differentiation: Built-in asset management, Figma integration, design workflows
- Target: Design teams switching from Asana (need design-specific features)

### Validation Result: ✅ PASS

**Why**:
- ✅ 3 competitors analyzed thoroughly
- ✅ Product type justified (unbundle strategy clear)
- ✅ Differentiation specific (not "better PM")
- ✅ Clear switching target (Asana users needing design features)

**Action**: Advance to v0.3 (Commercial Model)

---

## Bad Example 1: v0.1 → v0.2 Gate Blocked

### Context
AI-powered scheduling assistant

### Artifacts Submitted

**CFD Entries**:
- CFD-001: "Users want better scheduling" (no evidence, no specifics)
- CFD-002: "Calendars are annoying" (vague, no quantification)

**Problem Statement**:
"People hate scheduling meetings"

**Value Hypothesis**:
"Our AI will make it easier"

### Validation Result: ❌ BLOCKED

**Blockers**:
1. ❌ No evidence for pain points (CFD entries empty)
2. ❌ Problem too vague ("hate scheduling" - what specifically?)
3. ❌ Value unclear ("easier" - how? by how much?)

**Required Actions**:
- [ ] Conduct 10 user interviews (find specific pain: time zone confusion? back-and-forth emails?)
- [ ] Quantify problem (how many hours/week lost? how much frustration?)
- [ ] Define specific value ("reduce scheduling time from 5 min to 30 sec")

**Re-check Date**: 2 weeks (after user research)

---

## Bad Example 2: v0.3 → v0.4 Conditional Pass

### Context
CRM for real estate agents

### Artifacts Submitted

**Pricing Model (BR-034)**:
- Model: Tiered pricing
- Tiers: Free, Pro ($50/mo), Enterprise (custom)
- Justification: "Feels right, competitors charge $30-100"

**Success Metrics (KPI-011, KPI-012)**:
- Primary: 1,000 total signups Month 1
- Secondary: 100 Pro subscribers

**Moat Analysis**:
- Defensibility: "We'll build integrations with MLS systems"
- Competitor moats: "They're slow, we're fast"

**Features (FEA-XXX)**:
- 25 features listed, all marked "high priority"

### Validation Result: ⚠️ CONDITIONAL PASS

**Issues**:
1. ⚠️ Pricing not validated (survey? willingness to pay?)
2. ⚠️ Primary KPI is vanity metric (total signups, not activation)
3. ⚠️ Moat weak ("integrations" - competitors can copy)
4. ⚠️ No feature prioritization (can't build 25 features for MVP)

**Conditions to Address (within 1 week)**:
- [ ] Survey 20 real estate agents: "Would you pay $50/mo for [value prop]?"
- [ ] Change primary KPI to "activated users" (define activation)
- [ ] Re-assess moat (data moat? network effects? brand?)
- [ ] Prioritize features: Mark 5 as MVP, rest as "post-MVP"

**Decision**: Can advance, but must fix conditions before v0.5

---

## Good Example: v0.7 → v0.8 Gate Pass

### Context
Dark mode feature for SaaS product

### Artifacts Submitted

**EPICs**:
- EPIC-012: CSS theme variables (1 week)
- EPIC-013: User preference storage (3 days)
- EPIC-014: Toggle UI component (2 days)

**Tests (TEST-XXX)**:
- TEST-034: Dark mode toggle saves preference
- TEST-035: Theme applies correctly across all screens
- TEST-036: Accessibility (WCAG AA compliance)
- Coverage: 85%
- All tests passing ✅

**Code Traceability**:
- `ThemeProvider.tsx`: @implements BR-089 (User preference persistence)
- `ToggleComponent.tsx`: @implements UI-012 (Dark mode toggle)

### Validation Result: ✅ PASS

**Why**:
- ✅ EPICs right-sized (days to 1 week, fit in context)
- ✅ Comprehensive test coverage (85%, includes accessibility)
- ✅ All tests passing
- ✅ Code traceable (can find which code implements which spec)

**Action**: Advance to v0.8 (Deployment planning)

---

## Bad Example 3: v0.5 → v0.6 Gate Blocked

### Context
Marketplace for freelance designers

### Artifacts Submitted

**Risks (RISK-XXX)**:
- RISK-001: "Might not work" (no specifics)
- RISK-002: "Competition" (too vague)

**Tech Stack (TECH-XXX)**:
- TECH-001: "Build custom payment processor" (buy decision: none)
- TECH-002: "Build custom search engine" (buy decision: none)
- TECH-003: "Build custom email system" (buy decision: none)

### Validation Result: ❌ BLOCKED

**Blockers**:
1. ❌ Risks too vague (not actionable)
2. ❌ Build vs buy: Building everything from scratch (NIH syndrome)
3. ❌ No risk mitigations

**Required Actions**:
- [ ] Define specific risks (e.g., "Cold start problem: need both designers and clients to launch")
- [ ] Mitigation for each risk (e.g., "Recruit 50 designers pre-launch")
- [ ] Reconsider build vs buy (Stripe for payments, Algolia for search, SendGrid for email)
- [ ] Justify any build decision (why not buy? ROI? Strategic value?)

**Re-check Date**: 1 week

---

## Pass/Fail Pattern Summary

### Patterns That Pass

**Good CFD Entries**:
- Specific pain point
- Evidence (quote, survey data, support ticket count)
- Quantified (frequency, severity)

**Good KPIs**:
- Actionable (not vanity)
- Thresholds (success/caution/failure)
- Tied to business outcome

**Good Features**:
- Prioritized (MVP vs post-MVP)
- Tied to business rules and outcomes
- Traceability (FEA → BR → KPI)

**Good Tests**:
- > 80% coverage
- All passing
- Include edge cases, accessibility

---

### Patterns That Block

**Bad CFD Entries**:
- Vague ("users want better tools")
- No evidence (hunches)
- Not quantified

**Bad KPIs**:
- Vanity metrics (total signups)
- No thresholds (how do we know if we're succeeding?)
- Not tied to revenue/retention

**Bad Features**:
- All "high priority" (no trade-offs)
- No traceability (can't connect to business value)
- Scope creep (50 features for MVP)

**Bad Build Decisions**:
- NIH syndrome (build everything)
- No justification (why not Stripe? Twilio? AWS?)
- Ignoring opportunity cost

---

## Conditional Pass Criteria

**When to Use**:
- 80%+ of criteria met
- Issues are fixable in < 1 week
- Blocker conditions not present

**Example Conditions**:
- Pricing model needs validation (survey 20 users)
- KPI needs to change from vanity to actionable
- Features need prioritization (mark MVP vs post-MVP)

**Follow-up**:
- Set deadline (1 week)
- Assign owner
- Re-validate when complete

---

*Reference: Use these examples when performing gate checks in `ghm-gate-check` skill.*
