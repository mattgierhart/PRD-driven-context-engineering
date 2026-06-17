# Gate Criteria Reference

**Purpose**: Detailed criteria for each PRD lifecycle gate with rationale and common failure patterns.

---

## Gate Philosophy

**Why Gates Matter**:
- Prevent advancing with incomplete foundation
- Ensure cross-functional alignment
- Reduce rework (cheaper to fix early)
- Maintain quality standards

**Gate Rule**: "Can't skip, but can iterate within stage"

---

## v0.1 → v0.2 Gate (Spark → Market Definition)

### Purpose
Validate that we understand the problem and customer value before analyzing market.

### Mandatory Artifacts

**CFD Entries** (Customer Feedback & Data):
- Minimum: 3 pain point entries
- Evidence type: User interviews, surveys, support tickets, usage data
- Evidence tier: At least 1 Tier 1 (direct quote/data)

**Problem Statement** (in PRD):
- Who has this problem (persona sketch)
- What is the problem (specific, not vague)
- Why it matters (frequency, severity, cost)

**Value Hypothesis** (in PRD):
- What outcome user gets (measurable)
- How life improves (before/after)

### Quality Indicators

**Good**:
- Pain points quantified ("30% of support tickets about X")
- Evidence from multiple sources (not just 1 customer)
- Problem matches target market (B2B pain, B2B product)

**Bad**:
- Vague problem ("users want better tools")
- No evidence (founder hunches)
- Problem doesn't match monetization (free product for enterprise pain)

### Common Failure Patterns

**Failure 1: Solution Disguised as Problem**
- Bad: "Users need a better calendar app"
- Good: "Users miss 20% of meetings due to calendar sync issues"

**Failure 2: Rare Edge Case**
- Bad: "1 user complained about dark mode"
- Good: "30% of users request dark mode (500 tickets/year)"

**Failure 3: No Willingness to Pay**
- Bad: "Users want this but won't pay"
- Good: "Users currently pay $X for inferior solution"

---

## v0.2 → v0.3 Gate (Market Definition → Commercial Model)

### Purpose
Ensure we understand competitive landscape and positioning before building.

### Mandatory Artifacts

**Competitive Analysis** (CFD):
- Minimum: 3 competitors analyzed
- For each: Strengths, weaknesses, pricing, market share estimate

**Product Type** (BR):
- Classification: Clone | Unbundle | Undercut | Slice | Wrapper | Innovation
- Rationale: Why this type, what it implies for GTM

**Positioning** (in PRD):
- Our differentiation (specific, defensible)
- Target switching users (from which competitor)

### Quality Indicators

**Good**:
- Honest competitor assessment (not "we're better at everything")
- Clear switching cost analysis ("users switch because...")
- Product type matches execution (Innovation = patient capital, Clone = fast execution)

**Bad**:
- Ignoring major competitor ("they don't count")
- No differentiation ("we do the same thing, better")
- Product type wrong (calling Clone "Innovation")

### Common Failure Patterns

**Failure 1: Competitor Blindness**
- Bad: "No one does this" (usually false)
- Good: "X does this, but for enterprise; we target SMB"

**Failure 2: Feature Parity Trap**
- Bad: "We need all features they have + more"
- Good: "We unbundle their one feature, do it 10x better"

**Failure 3: Wrong Product Type**
- Bad: Calling fast-follow a "novel innovation"
- Good: "We're a Clone, so we need speed-to-market advantage"

---

## v0.3 → v0.4 Gate (Commercial Model → User Journeys)

### Purpose
Lock in business model and success metrics before detailed design.

### Mandatory Artifacts

**Pricing Model** (BR):
- Model type: Freemium, Trial, Usage-based, Flat, Tiered
- Price points: Specific numbers with justification
- Competitive positioning: Cheaper/same/premium vs competitors

**Success Metrics** (KPI):
- Primary KPI: One north star metric
- Secondary KPIs: 3-5 supporting metrics
- Thresholds: Success/caution/failure levels

**Moat Analysis** (CFD):
- Our defensibility: Network effects, data, brand, integration, etc.
- Competitor moats: What makes them hard to displace
- Wedge strategy: How we enter despite their moat

**Feature Priorities** (FEA):
- Parity features (must-have to compete)
- Delta features (our differentiation)
- Nice-to-have (post-MVP)

### Quality Indicators

**Good**:
- Pricing justified (competitor comparison, value-based)
- KPIs tied to revenue/retention (not vanity)
- Moat realistic (not "first mover advantage")
- Features clearly prioritized (MVP scope set)

**Bad**:
- Pricing random ($99 because it "feels right")
- KPIs are vanity metrics (total signups)
- No moat ("we'll just execute better")
- All features "high priority" (no trade-offs)

### Common Failure Patterns

**Failure 1: Pricing Without Validation**
- Bad: "We'll charge $50/month" (no research)
- Good: "Competitors charge $30-100; we're $50 (mid-market, validated in survey)"

**Failure 2: Vanity KPIs**
- Bad: "Total signups" (doesn't predict revenue)
- Good: "Activated users" (predicts retention/revenue)

**Failure 3: No Moat**
- Bad: "We'll just outwork them"
- Good: "Network effects (each user makes product better for all)"

---

## v0.4 → v0.5 Gate (User Journeys → Red Team)

### Purpose
Ensure we understand user needs and workflows before identifying risks.

### Mandatory Artifacts

**Personas** (PER):
- Primary persona: Detailed behavioral profile
- Secondary personas: Brief profiles

**User Journeys** (UJ):
- Critical paths: Trigger → Steps → Value moment
- Minimum: 3 journeys (core product value)

**Screen Flows** (SCR):
- UI structure: Which screens support which journeys
- Navigation: How users move through product

### Quality Indicators

**Good**:
- Personas behavioral (not just demographic)
- Journeys tied to KPIs (journey completion = success metric)
- Screens minimal (reduce scope creep)

**Bad**:
- Personas generic ("small business owner")
- Journeys don't match features (disconnect)
- Too many screens (over-designed)

### Common Failure Patterns

**Failure 1: Demographic Personas**
- Bad: "Sarah, 35, marketer, likes coffee"
- Good: "Sarah needs fast reporting to justify spend to CFO quarterly"

**Failure 2: Journeys Don't Match Features**
- Bad: Journey requires export, but no export feature
- Good: Every journey maps to features (FEA-XXX)

**Failure 3: Screen Bloat**
- Bad: 50 screens for MVP
- Good: 10 screens (ruthless prioritization)

---

## v0.5 → v0.6 Gate (Red Team → Architecture)

### Purpose
Surface risks and finalize tech stack before detailed architecture.

### Mandatory Artifacts

**Risk Register** (RISK):
- Minimum: 5 risks (technical, market, execution, competitive)
- Each risk: Probability, impact, mitigation

**Tech Stack** (TECH):
- Build decisions: What we're building from scratch
- Buy decisions: What we're licensing/purchasing
- Integrate decisions: What we're integrating (APIs, services)

### Quality Indicators

**Good**:
- Risks concrete (not "it might fail")
- Mitigations actionable (not "work harder")
- Build vs buy justified (ROI, strategic value)

**Bad**:
- Generic risks ("market might not want this")
- No mitigations ("we'll deal with it later")
- Build everything (NIH syndrome)

### Common Failure Patterns

**Failure 1: Vague Risks**
- Bad: "Technical challenges might arise"
- Good: "Database migration for 10M records might take 4 hours (prod downtime risk)"

**Failure 2: Build Everything**
- Bad: "We'll build our own payment processor"
- Good: "Integrate Stripe (faster, lower risk, $0.30 + 2.9%)"

**Failure 3: No Risk Mitigation**
- Bad: Risk identified, no plan
- Good: Risk + mitigation + owner + timeline

---

## v0.6 → v0.7 Gate (Architecture → Build)

### Purpose
Ensure architecture is complete before implementation begins.

### Mandatory Artifacts

**Architecture Design** (ARC):
- Component diagram: Major services and boundaries
- Data flow: How data moves through system
- Integration points: External dependencies

**API Contracts** (API):
- Endpoints: All APIs needed for UJ-XXX
- Request/response: Detailed schemas

**Data Models** (DBT):
- Tables/collections: All entities
- Relationships: Foreign keys, joins

### Quality Indicators

**Good**:
- Architecture decisions have trade-offs (considered alternatives)
- APIs cover all user journeys (no gaps)
- Data models normalized (DRY, no redundancy)

**Bad**:
- Architecture "just evolved" (no intentional design)
- APIs don't match journeys (missing endpoints)
- Data models ad-hoc (will cause tech debt)

### Common Failure Patterns

**Failure 1: No Alternatives Considered**
- Bad: "We'll use microservices" (why?)
- Good: "Microservices vs monolith: chose monolith for MVP speed, will split later"

**Failure 2: API-Journey Mismatch**
- Bad: User journey needs real-time updates, but only batch API
- Good: Every journey step has corresponding API

**Failure 3: Data Model Gaps**
- Bad: Feature needs user preferences, but no table/column
- Good: All features have data model support

---

## v0.7 → v0.8 Gate (Build → Deployment)

### Purpose
Ensure code is complete, tested, and traceable before deployment.

### Mandatory Artifacts

**EPICs** (EPIC):
- Work broken into context-window-sized chunks
- Each epic: Objective, IDs referenced, dependencies

**Tests** (TEST):
- Unit tests: Code coverage > 80%
- Integration tests: Critical paths covered
- All tests passing

**Code Traceability**:
- @implements tags: Major units reference IDs
- Commit messages: Reference IDs

### Quality Indicators

**Good**:
- EPICs small (fit in context window, 1-2 week work)
- Tests comprehensive (not just happy path)
- Code readable (IDs make it clear what implements what)

**Bad**:
- EPICs huge (months of work)
- No tests or low coverage
- Code cryptic (no ID references)

### Common Failure Patterns

**Failure 1: Epic Too Large**
- Bad: EPIC-001 "Build entire product" (months)
- Good: EPIC-001 "User authentication" (1 week)

**Failure 2: No Test Coverage**
- Bad: "We'll test manually"
- Good: 80%+ coverage, automated CI

**Failure 3: No Traceability**
- Bad: Can't find which code implements BR-045
- Good: @implements BR-045 tag in code

---

## v0.8 → v0.9 Gate (Deployment → GTM)

### Purpose
Ensure operational readiness before launch.

### Mandatory Artifacts

**Deployment Plan** (DEP):
- Strategy: Phased rollout, feature flag, big bang
- Rollback plan: How to undo if issues

**Runbooks** (RUN):
- Incident response: P0/P1 scenarios
- Tested: Not just written, but validated

**Monitoring** (MON):
- Dashboards: Key metrics visible
- Alerts: Errors, latency, SLO breaches
- SLOs: Defined and tracked

### Quality Indicators

**Good**:
- Deployment plan tested (not first time in prod)
- Runbooks practical (commands, not theory)
- Monitoring comprehensive (all critical paths)

**Bad**:
- No rollback plan
- Runbooks untested (will fail in incident)
- Monitoring missing (blind in production)

### Common Failure Patterns

**Failure 1: No Rollback**
- Bad: "We'll roll forward" (hubris)
- Good: Feature flag or code rollback plan

**Failure 2: Theoretical Runbooks**
- Bad: "Just restart the server" (which server? how?)
- Good: `kubectl rollout restart deployment/api` (specific command)

**Failure 3: No Monitoring**
- Bad: Rely on user complaints
- Good: Alerts fire before users notice

---

## v0.9 → v1.0 Gate (GTM → Launch)

### Purpose
Ensure GTM plan and metrics in place before declaring product launched.

### Mandatory Artifacts

**GTM Strategy** (GTM):
- Messaging: Problem, solution, differentiation
- Channels: Which channels, why
- Timeline: Phased rollout plan

**Launch Metrics** (KPI):
- Acquisition: Signup targets
- Activation: "Aha moment" metric
- Retention: D7, D30 targets
- Revenue: Conversion targets (if applicable)

**Feedback Loop**:
- Channels: Where user feedback collected
- Process: How feedback reviewed, acted on

### Quality Indicators

**Good**:
- GTM matches product type (Innovation ≠ big bang)
- Metrics actionable (not vanity)
- Feedback monitored (daily in first week)

**Bad**:
- Generic GTM ("email and ads")
- Vanity metrics ("total signups")
- No feedback loop (users in void)

### Common Failure Patterns

**Failure 1: Wrong GTM for Product Type**
- Bad: Innovation product with big bang launch (users need education)
- Good: Innovation product with beta → soft launch → scale

**Failure 2: Vanity Metrics**
- Bad: Track total signups (doesn't predict retention)
- Good: Track activation rate (predicts retention)

**Failure 3: No Feedback Loop**
- Bad: Launch and hope
- Good: Daily NPS, support tickets, user interviews in Week 1

---

*Reference: Use these criteria when validating gates in `ghm-gate-check` skill.*
