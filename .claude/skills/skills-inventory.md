# Skills Inventory

> **Navigation index for PRD lifecycle skills. Each skill transforms inputs into outputs with evidence.**

---

## Quick Navigation

| Stage | Skill | Status | Folder |
|-------|-------|--------|--------|
| **v0.1 Spark** | [Problem Framing](#skill-problem-framing) | ✅ Ready | [`prd-v01-problem-framing/`](prd-v01-problem-framing/) |
| **v0.1 Spark** | [User Value Articulation](#skill-user-value-articulation) | ✅ Ready | [`prd-v01-user-value-articulation/`](prd-v01-user-value-articulation/) |
| **v0.2 Market Definition** | [Competitive Landscape Mapping](#skill-competitive-landscape-mapping) | ✅ Ready | [`prd-v02-competitive-landscape-mapping/`](prd-v02-competitive-landscape-mapping/) |
| **v0.2 Market Definition** | [Product Type Classification](#skill-product-type-classification) | ✅ Ready | [`prd-v02-product-type-classification/`](prd-v02-product-type-classification/) |
| **v0.3 Commercial Model** | [Outcome Definition](#skill-outcome-definition) | ✅ Ready | [`prd-v03-outcome-definition/`](prd-v03-outcome-definition/) |
| **v0.3 Commercial Model** | [Pricing Model Selection](#skill-pricing-model-selection) | ✅ Ready | [`prd-v03-pricing-model/`](prd-v03-pricing-model/) |
| **v0.3 Commercial Model** | [Moat Definition](#skill-moat-definition) | ✅ Ready | [`prd-v03-moat-definition/`](prd-v03-moat-definition/) |
| **v0.3 Commercial Model** | [Feature Value Planning](#skill-feature-value-planning) | ✅ Ready | [`prd-v03-features-value-planning/`](prd-v03-features-value-planning/) |
| **v0.4 User Journeys** | [Persona Definition](#skill-persona-definition) | ✅ Ready | [`prd-v04-persona-definition/`](prd-v04-persona-definition/) |
| **v0.4 User Journeys** | [User Journey Mapping](#skill-user-journey-mapping) | ✅ Ready | [`prd-v04-user-journey-mapping/`](prd-v04-user-journey-mapping/) |
| **v0.4 User Journeys** | [Screen Flow Definition](#skill-screen-flow-definition) | ✅ Ready | [`prd-v04-screen-flow-definition/`](prd-v04-screen-flow-definition/) |
| **v0.5 Red Team Review** | [Risk Discovery Interview](#skill-risk-discovery-interview) | ✅ Ready | [`prd-v05-risk-discovery-interview/`](prd-v05-risk-discovery-interview/) |
| **v0.5 Red Team Review** | [Technical Stack Selection](#skill-technical-stack-selection) | ✅ Ready | [`prd-v05-technical-stack-selection/`](prd-v05-technical-stack-selection/) |
| **v0.6 Architecture** | [Architecture Design](#skill-architecture-design) | ✅ Ready | [`prd-v06-architecture-design/`](prd-v06-architecture-design/) |
| **v0.6 Architecture** | [Technical Specification](#skill-technical-specification) | ✅ Ready | [`prd-v06-technical-specification/`](prd-v06-technical-specification/) |
| **v0.7 Build Execution** | [Epic Scoping](#skill-epic-scoping) | ✅ Ready | [`prd-v07-epic-scoping/`](prd-v07-epic-scoping/) |
| **v0.7 Build Execution** | [Test Planning](#skill-test-planning) | ✅ Ready | [`prd-v07-test-planning/`](prd-v07-test-planning/) |
| **v0.7 Build Execution** | [Implementation Loop](#skill-implementation-loop) | ✅ Ready | [`prd-v07-implementation-loop/`](prd-v07-implementation-loop/) |
| **v0.8 Release & Deployment** | [Release Planning](#skill-release-planning) | ✅ Ready | [`prd-v08-release-planning/`](prd-v08-release-planning/) |
| **v0.8 Release & Deployment** | [Runbook Creation](#skill-runbook-creation) | ✅ Ready | [`prd-v08-runbook-creation/`](prd-v08-runbook-creation/) |
| **v0.8 Release & Deployment** | [Monitoring Setup](#skill-monitoring-setup) | ✅ Ready | [`prd-v08-monitoring-setup/`](prd-v08-monitoring-setup/) |
| **v0.9 Launch** | [GTM Strategy](#skill-gtm-strategy) | ✅ Ready | [`prd-v09-gtm-strategy/`](prd-v09-gtm-strategy/) |
| **v0.9 Launch** | [Launch Metrics](#skill-launch-metrics) | ✅ Ready | [`prd-v09-launch-metrics/`](prd-v09-launch-metrics/) |
| **v0.9 Launch** | [Feedback Loop Setup](#skill-feedback-loop-setup) | ✅ Ready | [`prd-v09-feedback-loop-setup/`](prd-v09-feedback-loop-setup/) |
| **Methodology** | [SoT Builder](#skill-sot-builder) | ✅ Ready | [`ghm-sot-builder/`](ghm-sot-builder/) |

**Legend:** ✅ Ready = SKILL.md complete | 📋 Spec = specification below, needs implementation

---

## Stage Overview

### v0.1 Spark — Problem & Outcomes

**Purpose:** Validate the problem is real and articulate what users need.
**Gate:** Problem defined, User value articulated, Open Questions list.

| Skill | Input | Output | IDs Created |
|-------|-------|--------|-------------|
| Problem Framing | Raw idea | 1-3 testable problem statements | CFD- |
| User Value Articulation | Pain points (CFD-) | Value statements | CFD- (value hypotheses) |

### v0.2 Market Definition — Competitive Landscape & Product Type

**Purpose:** Understand the market, competitors, and what type of product we're building.
**Gate:** Competitive landscape mapped, Product type identified, Segments sized.

| Skill | Input | Output | IDs Created |
|-------|-------|--------|-------------|
| Competitive Landscape Mapping | Problem + value statements | Landscape map, feature matrix | CFD-, BR- |
| Product Type Classification | Competitive landscape | Fast Follow / Slice / Innovation | BR- |

### v0.3 Commercial Model — Pricing, Positioning & Moat

**Purpose:** Define how we win commercially.
**Gate:** Pricing model selected, Moat articulated, Outcomes defined, Features prioritized.

| Skill | Input | Output | IDs Created |
|-------|-------|--------|-------------|
| Outcome Definition | Product type, pricing signals | Measurable KPIs | KPI- |
| Pricing Model Selection | Competitive pricing, product type | Pricing structure | BR- |
| Moat Definition | Competitive landscape | Defensibility strategy, targeting rules | CFD-, BR- |
| Feature Value Planning | KPIs, pricing, moat definitions | Prioritized features with traceability | FEA-, BR-FEA- |

### v0.4 User Journeys — From Pain to Value

**Purpose:** Define who uses the product, how they accomplish goals, and what screens they see.
**Gate:** Personas defined, user journeys mapped with triggers and value moments, screen flows established with feature-to-UI traceability.

| Skill | Input | Output | IDs Created |
|-------|-------|--------|-------------|
| Persona Definition | CFD- (v0.1-v0.3), BR- (targeting), FEA- (features) | Behavioral personas (max 5) | PER- |
| User Journey Mapping | PER- (personas), FEA- (features), KPI- (outcomes) | User missions with step flows | UJ- |
| Screen Flow Definition | UJ- (journeys), FEA- (features), BR- (constraints) | Screen inventory with navigation | SCR-, DES- |

### v0.5 Red Team Review — Risks & Technical Stack

**Purpose:** Surface risks through guided interview and select technical stack for implementation.
**Gate:** Risks documented with mitigations, technical stack decisions made (build/buy/integrate), research items identified.

| Skill | Input | Output | IDs Created |
|-------|-------|--------|-------------|
| Risk Discovery Interview | All prior IDs, product context | Risk register with owner decisions | RISK- |
| Technical Stack Selection | FEA- (features), SCR- (screens), RISK- (constraints) | Stack decisions and tool selections | TECH- |

### v0.6 Architecture — Technical Blueprint

**Purpose:** Define system architecture and implementation contracts based on stack selections.
**Gate:** Architecture decisions documented, API contracts defined, data models specified, integration patterns established.

| Skill | Input | Output | IDs Created |
|-------|-------|--------|-------------|
| Architecture Design | TECH- (stack), RISK- (constraints), FEA- (features) | System architecture with component relationships | ARC- |
| Technical Specification | ARC- (architecture), TECH- (Build items), UJ- (flows), SCR- (screens) | API contracts and data models | API-, DBT- |

### v0.7 Build Execution — Implementation

**Purpose:** Execute implementation in focused "context windows" (EPICs) with test-first discipline and continuous SoT updates.
**Gate:** Code tested (TEST-), SoT matches code, all EPICs complete, ready for deployment.

| Skill | Input | Output | IDs Created |
|-------|-------|--------|-------------|
| Epic Scoping | API-, DBT-, FEA-, ARC- | Context-window-sized work packages | EPIC- |
| Test Planning | API-, DBT-, BR-, UJ- | Test cases before implementation | TEST- |
| Implementation Loop | EPIC-, TEST- | Working code with traceability | (updates existing IDs) |

### v0.8 Release & Deployment — Operational Readiness

**Purpose:** Prepare for production deployment with release criteria, operational runbooks, and monitoring infrastructure.
**Gate:** Runbooks documented (RUN-), monitoring configured (MON-), rollback plan validated (DEP-).

| Skill | Input | Output | IDs Created |
|-------|-------|--------|-------------|
| Release Planning | EPIC- (complete), TEST-, ARC- | Deployment environments, release criteria, rollback triggers | DEP- |
| Runbook Creation | DEP-, RISK-, MON- (alerts) | Operational playbooks for incidents, deployments, maintenance | RUN- |
| Monitoring Setup | DEP-, RUN-, KPI- | Metrics, alerts, dashboards, SLOs | MON- |

### v0.9 Go-to-Market — Launch & Feedback

**Purpose:** Coordinate launch activities, define success metrics, and establish feedback loops for continuous improvement.
**Gate:** Launch metrics defined (KPI-), feedback channels active (CFD-), GTM execution underway.

| Skill | Input | Output | IDs Created |
|-------|-------|--------|-------------|
| GTM Strategy | PER-, CFD-, BR- (product type), MON- (readiness) | Launch plan, messaging, channels, timeline | GTM- |
| Launch Metrics | GTM-, KPI- (v0.3), MON- | Launch-specific success criteria and tracking | KPI- (launch variant) |
| Feedback Loop Setup | GTM-, KPI-, all prior IDs | Feedback channels, processing workflow, CFD- templates | CFD- (post-launch) |

---

## Skill Specifications

### SKILL: Problem Framing

```yaml
name: prd-v01-problem-framing
stage: v0.1
status: ready
folder: prd-v01-problem-framing/
triggers: "frame the problem", "define pain points", "write problem statement", "start v0.1"
id_outputs: [CFD-]
```

**Purpose:** Convert raw sparks into structured, testable problem statements.

**Position in workflow:** Raw idea → **v0.1 Problem Framing** → v0.1 User Value Articulation

**Execution:**
1. Dump raw idea as unfiltered paragraph
2. Desk research — find 5 examples of people experiencing this problem
3. Root cause exploration — 5 Whys (don't go too deep)
4. Draft 1-3 problem statements using Design Thinking format
5. Define kill criteria

**Problem Statement Template:** `[USER TYPE] needs a way to [NEED] because [INSIGHT/BARRIER].`

**CFD- Output Template (Desk Research):**
```
CFD-XXX: [Research Finding Title]
Type: Desk Research
Source: [URL, publication, forum thread]
Date: [When found]
Finding: [What we learned]
Relevance: [How this validates/invalidates the problem]
Quote: [Direct quote if available]
```

**CFD- Output Template (Pain Point):**
```
CFD-XXX: [Pain Point Title]
Type: Pain Point
User Type: [Who experiences this]
Pain: [What hurts]
Frequency: [How often — daily, weekly, per event]
Severity: [How much it hurts — annoyance to business-critical]
Current Workaround: [What they do today]
Evidence: [CFD-YYY desk research that supports this]
```

**Anti-Patterns:**
| Pattern | Signal | Fix |
|---------|--------|-----|
| Solution masquerading as problem | "Users need a dashboard" | Ask "why?" until you find the pain |
| Too broad | "Businesses struggle with efficiency" | Narrow to specific user type and context |
| No evidence | Problem assumed, not validated | Require 3+ desk research findings |
| Inventor's bias | "I have this problem" | Find 5 others who have it too |
| Skipping kill criteria | No way to know if problem is real | Define what evidence would kill the idea |

**Downstream Connections:**
| Consumer | What It Uses | Example |
|----------|--------------|---------|
| **User Value Articulation** | CFD- pain points become value inputs | CFD-001 (pain) → CFD-010 (value) |
| **v0.2 Competitive Landscape** | Problem context for competitor search | "Who else solves CFD-001?" |
| **v0.4 Persona Definition** | USER TYPE seeds persona creation | USER TYPE → PER-001 |

---

### SKILL: User Value Articulation

```yaml
name: prd-v01-user-value-articulation
stage: v0.1
status: ready
folder: prd-v01-user-value-articulation/
triggers: "what value do users get", "define outcomes", "articulate benefit", "pain to value"
id_outputs: [CFD-]
```

**Purpose:** Transform pain points into evidence-anchored value statements.

**Position in workflow:** v0.1 Problem Framing → **v0.1 User Value Articulation** → v0.2 Competitive Landscape

**Execution:**
1. Receive pain points (CFD-IDs from Problem Framing)
2. Identify value unit (Time / Money / Risk / Capability)
3. Transform pain → value using patterns
4. Anchor to evidence
5. Create CFD entry tagged as value hypothesis

**Transformation Patterns:**
| Pain | → | Value |
|------|---|-------|
| Costs X time | → | Reclaim X time for [activity] |
| Costs $X | → | Save $X [or redirect to growth] |
| Risks $X penalty | → | Eliminate $X exposure |
| Cannot do X | → | Now able to X when [trigger] |

**CFD- Output Template (Value Hypothesis):**
```
CFD-XXX: [Value Statement Title]
Type: Value Hypothesis
Pain Source: [CFD-YYY that this addresses]
Value Unit: [Time | Money | Risk | Capability]
Value Statement: [User] can now [outcome] instead of [current pain]
Quantification: [Estimated savings/gains if possible]
Validation Method: [How we'll test this — survey, interview, prototype]
Confidence: [High | Medium | Low] — based on evidence strength
```

**Anti-Patterns:**
| Pattern | Signal | Fix |
|---------|--------|-----|
| Feature as value | "Users get a dashboard" | Reframe as outcome: "Users see status in 2 seconds" |
| Unquantified value | "Users save time" | Add specificity: "Users save 2 hours per week" |
| Value without pain | Value statement has no CFD- pain link | Every value must trace to documented pain |
| Aspirational value | "Users will love this" | Ground in evidence, not hope |
| Single value unit | Only time savings considered | Explore all four units (Time/Money/Risk/Capability) |

**Downstream Connections:**
| Consumer | What It Uses | Example |
|----------|--------------|---------|
| **v0.2 Competitive Landscape** | Value statements define what to compare | "Do competitors deliver CFD-010 value?" |
| **v0.3 Outcome Definition** | Value hypotheses inform KPI selection | CFD-010 (time saved) → KPI-001 (TTFV) |
| **v0.3 Pricing Model** | Value quantification anchors pricing | CFD-010 ($500/mo saved) → price ≤ $100/mo |
| **v0.4 Persona Definition** | Primary value links to persona | PER-001 cares most about CFD-010 |

---

### SKILL: Competitive Landscape Mapping

```yaml
name: prd-v02-competitive-landscape-mapping
stage: v0.2
status: ready
folder: prd-v02-competitive-landscape-mapping/
triggers: "competitive analysis", "who else solves this", "market landscape", "what alternatives exist", "competitor research"
id_outputs: [CFD-, BR-]
```

**Purpose:** Understand market reality before defining our position.

**Position in workflow:** v0.1 User Value Articulation → **v0.2 Competitive Landscape Mapping** → v0.2 Product Type Classification

**Execution:**
1. Document what users do TODAY (before searching competitors)
2. Competitor discovery — direct, adjacent, workarounds, "do nothing"
3. Industry/geography gap analysis
4. Feature comparison matrix
5. 1% better hypothesis with evidence

**Key Outputs:**
- Industry/geo gap table
- Feature matrix
- 1% better hypothesis: "We can be 1% better than [X] by [Y] for [Z]"

**CFD- Output Template (Competitor Intelligence):**
```
CFD-XXX: [Competitor Name] Analysis
Type: Competitor Intelligence
Category: [Direct | Adjacent | Workaround | Do Nothing]
Website: [URL]
Pricing: [Model and price points]
Target Segment: [Who they serve]
Key Features: [Top 3-5 capabilities]
Strengths: [What they do well]
Weaknesses: [Where they fall short]
User Sentiment: [Reviews, complaints, praise]
Market Position: [Leader | Challenger | Niche | Emerging]
```

**BR- Output Template (Competitive Rule):**
```
BR-XXX: [Rule Name]
Type: Competitive Positioning
Rule: [Constraint or requirement based on competitive reality]
Evidence: [CFD-YYY competitor analysis that drives this]
Implication: [What this means for our product]
```

**Anti-Patterns:**
| Pattern | Signal | Fix |
|---------|--------|-----|
| Competitor tunnel vision | Only looking at direct competitors | Include adjacent, workarounds, "do nothing" |
| Feature obsession | Comparing features without context | Compare on value delivered, not feature count |
| Ignoring pricing | Features compared, pricing ignored | Pricing is a feature — document it |
| Recency bias | Only looking at current competitors | Research failed competitors too (why they died) |
| Confirmation bias | Only finding evidence that supports your idea | Actively seek disconfirming evidence |

**Downstream Connections:**
| Consumer | What It Uses | Example |
|----------|--------------|---------|
| **Product Type Classification** | Competitor count determines type | 5+ competitors → Fast Follow |
| **v0.3 Pricing Model** | Competitor pricing anchors our pricing | CFD-020 (competitor $50/mo) → BR-030 |
| **v0.3 Moat Definition** | Competitor moats inform our strategy | CFD-021 (competitor moat) → our vulnerability |
| **v0.3 Feature Value Planning** | Feature matrix defines parity features | CFD-022 (feature list) → FEA-001 (parity) |

---

### SKILL: Product Type Classification

```yaml
name: prd-v02-product-type-classification
stage: v0.2
status: ready
folder: prd-v02-product-type-classification/
triggers: "what type of product", "fast follow or innovation", "sales cycle", "clone or innovate", "product strategy"
id_outputs: [BR-]
```

**Purpose:** Classify product type to set realistic expectations.

**Position in workflow:** v0.2 Competitive Landscape Mapping → **v0.2 Product Type Classification** → v0.3 Outcome Definition

**Framework:**
| Type | Evidence | Sales Cycle | Positioning |
|------|----------|-------------|-------------|
| **Fast Follow** | 3+ competitors, users paying | Short | "Better/cheaper than X" |
| **Slice** | Ecosystem exists, gap in integrations | Medium | "Best [thing] for [ecosystem]" |
| **Innovation** | No competitors, behavior change needed | Long | "New way to [outcome]" |

**BR- Output Template (Product Type):**
```
BR-XXX: Product Type Classification
Type: Strategic Constraint
Classification: [Fast Follow | Slice | Innovation]
Evidence: [CFD-YYY competitor data that supports this]
Sales Cycle Expectation: [Short | Medium | Long]
Positioning Template: [How we'll describe ourselves]
GTM Implication: [What this means for go-to-market]
Feature Strategy: [Parity-first | Niche-depth | Education-heavy]
```

**Extended Type Framework:**
| Type | Sub-type | Evidence | Strategy |
|------|----------|----------|----------|
| **Fast Follow** | Clone | Identical feature set needed | Match features, compete on price/UX |
| **Fast Follow** | Undercut | Price-sensitive segment exists | Same features, lower price |
| **Slice** | Unbundle | Platform does too much | Extract one capability, do it better |
| **Slice** | Wrapper | API exists, UX doesn't | Build UX on existing infrastructure |
| **Innovation** | Category Creation | No existing mental model | Heavy education investment |

**Anti-Patterns:**
| Pattern | Signal | Fix |
|---------|--------|-----|
| Wishful innovation | Calling it innovation to avoid competition | Be honest — if competitors exist, it's not innovation |
| Ignoring evidence | Classifying without CFD- support | Every classification needs competitive evidence |
| Static typing | Assuming type never changes | Re-evaluate as market evolves |
| One-size strategy | Applying same approach regardless of type | Strategy must match type |

**Downstream Connections:**
| Consumer | What It Uses | Example |
|----------|--------------|---------|
| **v0.3 Outcome Definition** | Type determines realistic KPI targets | Innovation → 3-10 design partners (not 50 customers) |
| **v0.3 Pricing Model** | Type influences pricing strategy | Fast Follow → price anchored to competitors |
| **v0.3 Feature Value Planning** | Type determines parity vs. delta balance | Fast Follow → BR-FEA-001 (parity first) |
| **v0.9 GTM** | Type shapes messaging and channels | Innovation → education-first content |

---

### SKILL: Outcome Definition

```yaml
name: prd-v03-outcome-definition
stage: v0.3
status: ready
folder: prd-v03-outcome-definition/
triggers: "define success metrics", "what are our KPIs", "measurable outcomes", "how do we measure success?"
id_outputs: [KPI-]
```

**Purpose:** Set measurable success criteria informed by product type and market.

**Position in workflow:** v0.2 Product Type Classification → **v0.3 Outcome Definition** → v0.3 Pricing Model Selection

**Execution:**
1. Review product type from v0.2 classification
2. Select Tier 1 (revenue), Tier 2 (conversion), and Tier 3 (engagement) metrics
3. Align metrics to product type (Clone, Undercut, Slice, Wrapper, Innovation)
4. Set evidence-based targets (not arbitrary numbers)
5. Define downstream gate linkages

**Calibration by Product Type:**
| Type | 90-day Outcome | Why |
|------|----------------|-----|
| Fast Follow | 10-50 customers, $1-5K MRR | Short sales cycle |
| Slice | 5-20 customers, partnerships | Ecosystem validation |
| Innovation | 3-10 design partners | Education cycle |

**KPI- Output Template:**
```
KPI-XXX: [Metric Name]
Tier: [Tier 1 | Tier 2 | Tier 3]
Category: [Leading | Lagging]
Definition: [Exact calculation formula]
Target: [Specific threshold with evidence source]
Evidence: [CFD-XXX or benchmark source]
Downstream Gate: [Which decision uses this — e.g., "v0.5 Red Team kill criteria"]
Measurement: [How/when measured — e.g., "Weekly via Mixpanel"]
```

**Anti-Patterns:**
| Pattern | Signal | Fix |
|---------|--------|-----|
| Vanity metrics | "50K users" with no revenue link | Require Tier 1 metric for every product |
| Arbitrary targets | "10% improvement" without baseline | Anchor to competitive benchmarks or evidence |
| All lagging metrics | No leading indicators | Include leading metrics for early course correction |
| Wrong metrics for type | Innovation product tracking MAU | Match metrics to product type expectations |
| Unmeasurable outcomes | "Better experience" | Every KPI needs a measurement method |

**Downstream Connections:**
| Consumer | What It Uses | Example |
|----------|--------------|---------|
| **v0.3 Pricing Model** | KPI- revenue targets inform pricing | KPI-001 ($5K MRR) → price × volume math |
| **v0.3 Feature Value Planning** | Features must support KPI | FEA-001 → KPI-002 (activation) |
| **v0.4 User Journey Mapping** | Journeys drive KPI outcomes | UJ-001 → KPI-001 (conversion) |
| **v0.5 Red Team** | KPI- thresholds become kill criteria | "If KPI-001 not hit by Day 21, pivot" |

---

### SKILL: Pricing Model Selection

```yaml
name: prd-v03-pricing-model
stage: v0.3
status: ready
folder: prd-v03-pricing-model/
triggers: "how to price", "pricing model", "monetization", "how much should we charge?"
id_outputs: [BR-]
```

**Purpose:** Select pricing that matches value delivery cadence.

**Position in workflow:** v0.3 Outcome Definition → **v0.3 Pricing Model Selection** → v0.3 Moat Definition

**Execution:**
1. Map when customer gets value (value timing)
2. Align to product type
3. Evaluate models (per-seat, usage, flat, tiered, freemium)
4. Calculate SMB penalty for per-user competitors
5. Define entry price point with unit economics check
6. Set guardrails (what's off-limits)
7. Plan WTP validation

**BR- Output Template (Pricing Rule):**
```
BR-XXX: [Pricing Rule Name]
Type: Pricing Constraint
Model: [Per-seat | Usage | Flat | Tiered | Freemium | Hybrid]
Entry Price: [$ amount and billing frequency]
Value Anchor: [CFD-YYY value quantification that justifies price]
Competitor Anchor: [CFD-ZZZ competitor pricing reference]
Guardrails: [What we won't do — e.g., "No per-seat for SMB"]
Unit Economics: [CAC, LTV assumptions]
Validation Plan: [How we'll test WTP]
```

**Anti-Patterns:**
| Pattern | Signal | Fix |
|---------|--------|-----|
| Pricing in a vacuum | No competitor or value reference | Anchor to CFD- evidence |
| Cost-plus pricing | "It costs us $X so we charge $2X" | Price on value, not cost |
| Copying competitors | Same price without differentiation | If same price, must be 10x better |
| Freemium without strategy | "We'll figure out monetization later" | Define conversion trigger upfront |
| Ignoring segment | Same price for SMB and Enterprise | Segment-appropriate pricing |

**Downstream Connections:**
| Consumer | What It Uses | Example |
|----------|--------------|---------|
| **v0.3 Feature Value Planning** | Pricing tiers define tier features | BR-030 (Pro tier) → FEA-005 (Pro feature) |
| **v0.4 User Journey Mapping** | Pricing touchpoints in journey | UJ-003 includes upgrade prompt |
| **v0.5 Technical Stack** | Payment processing needs | BR-030 → TECH-010 (Stripe) |
| **v0.9 GTM** | Pricing as marketing message | BR-030 (undercut) → "50% cheaper" |

---

### SKILL: Moat Definition

```yaml
name: prd-v03-moat-definition
stage: v0.3
status: ready
folder: prd-v03-moat-definition/
triggers: "what's our moat", "competitor moats", "defensibility", "switching costs", "who to target"
id_outputs: [CFD-, BR-]
```

**Purpose:** Analyze competitor defensibility and define our own moat strategy.

**Position in workflow:** v0.3 Pricing Model Selection → **v0.3 Moat Definition** → v0.3 Feature Value Planning

**Execution:**
1. Pull competitor data from v0.2 Competitive Landscape
2. Identify moat types (Switching Costs, Network Effects, Data/IP, Brand/Trust, Scale, Regulatory)
3. Rate moat strength (Impenetrable → Eroding)
4. Inventory switching costs (Financial, Time, Data, Workflow, Integration)
5. Identify vulnerabilities and targeting opportunities
6. Define our defensibility strategy

**Targeting Decision Framework:**
| If market shows... | Target... |
|--------------------|-----------|
| Strong moats, high switching | New-to-category |
| Weak moats, low switching | Switchers |
| High churn triggers despite moats | Switchers at trigger moments |

**CFD- Output Template (Moat Analysis):**
```
CFD-XXX: [Competitor] Moat Analysis
Type: Moat Assessment
Competitor: [CFD-YYY reference]
Moat Types: [Switching Costs | Network Effects | Data/IP | Brand/Trust | Scale | Regulatory]
Moat Strength: [Impenetrable | Strong | Moderate | Weak | Eroding]
Switching Costs: [Financial, Time, Data, Workflow, Integration costs]
Vulnerabilities: [Where moat is weakest]
Trigger Moments: [When users are most likely to switch]
```

**BR- Output Template (Targeting Rule):**
```
BR-XXX: [Targeting Rule Name]
Type: Targeting Constraint
Target Segment: [New-to-category | Switchers | Trigger-based]
Evidence: [CFD-YYY moat analysis that supports this]
Implication: [How this affects messaging, channels, timing]
Our Moat Strategy: [How we'll build defensibility]
```

**Anti-Patterns:**
| Pattern | Signal | Fix |
|---------|--------|-----|
| Moat envy | "They have network effects, we can't win" | Find vulnerabilities — every moat has cracks |
| Ignoring switching costs | Assuming users will switch easily | Quantify actual switching costs |
| No moat plan | Focused only on competitor moats | Define how WE build defensibility |
| Static moat view | Assuming moats are permanent | Moats erode — look for weakening signals |
| Wrong target | Fighting entrenched competitors head-on | Target where moats are weakest |

**Downstream Connections:**
| Consumer | What It Uses | Example |
|----------|--------------|---------|
| **v0.3 Feature Value Planning** | Moat features get priority | BR-040 (data moat) → FEA-010 (data collection) |
| **v0.4 Persona Definition** | Targeting rules define personas | BR-041 (target switchers) → PER-001 (frustrated user) |
| **v0.5 Risk Discovery** | Moat gaps become risks | Weak moat → RISK-005 (competitor copy) |
| **v0.9 GTM** | Targeting rules shape GTM | BR-041 → target at contract renewal |

---

### SKILL: Feature Value Planning

```yaml
name: prd-v03-feature-value-planning
stage: v0.3
status: ready
folder: prd-v03-features-value-planning/
triggers: "define features", "prioritize capabilities", "scope MVP", "what features do we build?", "feature priority", "parity vs delta"
id_outputs: [FEA-, BR-FEA-]
```

**Purpose:** Define and prioritize features with strategic traceability.

**Position in workflow:** v0.3 Moat Definition → **v0.3 Feature Value Planning** → v0.4 Persona Definition

**Execution:**
1. Consume KPI- (Outcome Definition), BR- (Pricing, Moat), and CFD- (landscape) from prior steps
2. Classify features (Moat, Outcome, Parity, Delta, Tier, Table Stakes)
3. Apply product type constraints (Fast Follow: parity first; Innovation: moat focus)
4. Prioritize using P0-P3 tiers with evidence thresholds
5. Create FEA- entries with full traceability
6. Establish BR-FEA- governance rules

**Feature Classification:**
| Type | Definition | Strategic Purpose |
|------|------------|-------------------|
| **Moat** | Builds competitive advantage | Supports BR- moat rule |
| **Outcome** | Directly drives KPI | Tied to KPI- entry |
| **Parity** | Matches competitor baseline | From Competitive Landscape |
| **Delta** | Differentiation from competitors | Our advantage |
| **Tier** | Differentiates pricing packages | From Pricing BR- |
| **Table Stakes** | Expected but not differentiating | Industry standard |

**FEA- Output Template:**
```
FEA-XXX: [Feature Name]
Classification: [Moat | Outcome | Parity | Delta | Tier | Table Stakes]
Priority: [P0 | P1 | P2 | P3]
Description: [What this feature does]
User Value: [CFD-YYY value hypothesis it delivers]
KPI Link: [KPI-XXX it drives]
Competitive Reference: [CFD-ZZZ if parity/delta]
Pricing Tier: [Free | Pro | Enterprise] if tier feature
Dependencies: [Other FEA- or BR- required]
Effort Estimate: [S | M | L | XL]
```

**BR-FEA- Output Template (Feature Governance):**
```
BR-FEA-XXX: [Governance Rule Name]
Type: Feature Governance
Rule: [Constraint on feature decisions]
Rationale: [Why this rule exists]
Applies To: [Which FEA- entries this affects]
Example: [Concrete application of rule]
```

**Priority Evidence Thresholds:**
| Priority | Evidence Required | Example |
|----------|-------------------|---------|
| **P0** | Multiple CFD- pain points + KPI link | Core value delivery |
| **P1** | At least one CFD- + competitive parity | Important but not blocking |
| **P2** | Competitive delta or moat contribution | Differentiation |
| **P3** | Nice-to-have, no strong evidence | Future consideration |

**Anti-Patterns:**
| Pattern | Signal | Fix |
|---------|--------|-----|
| Feature factory | Long list with no prioritization | Apply P0-P3 framework |
| No traceability | Features without CFD- or KPI- links | Every FEA- needs evidence |
| Parity obsession | Only matching competitors | Include delta features |
| Scope creep | P3 features consuming resources | Defer P3 until P0-P1 complete |
| Missing governance | No BR-FEA- rules | Define at least 2-3 governance rules |

**Downstream Connections:**
| Consumer | What It Uses | Example |
|----------|--------------|---------|
| **v0.4 Persona Definition** | Features link to personas | PER-001 cares about FEA-001 |
| **v0.4 User Journey Mapping** | Features become journey steps | UJ-001 Step 3 → FEA-002 |
| **v0.4 Screen Flow Definition** | Features render on screens | SCR-003 includes FEA-001, FEA-002 |
| **v0.5 Technical Stack Selection** | Features drive tech needs | FEA-010 (AI) → TECH-005 (OpenAI) |
| **v0.6 Technical Specification** | Features become API contracts | FEA-001 → API-001, API-002 |

---

### SKILL: Persona Definition

```yaml
name: prd-v04-persona-definition
stage: v0.4
status: ready
folder: prd-v04-persona-definition/
triggers: "define personas", "who are our users", "user profiles", "target users", "persona creation", "who uses this product"
id_outputs: [PER-]
```

**Purpose:** Synthesize behavioral personas from prior stage evidence for journey mapping and marketing.

**Position in workflow:** v0.3 Feature Value Planning → **v0.4 Persona Definition** → v0.4 User Journey Mapping

**Constraint:** Maximum 5 personas. Most products need 1-2. If you have more than 3, you're likely over-segmenting.

**Execution:**
1. Pull USER TYPE from v0.1 Problem Framing (CFD-)
2. Pull SEGMENTS from v0.2 Market Definition (CFD-, BR-)
3. Pull targeting rules from v0.3 Moat Definition (BR-)
4. Synthesize behavioral patterns from all CFD- evidence
5. Identify which FEA- features matter most to each persona
6. Create PER- entries with full traceability to source IDs

**PER- Output Template:**
```
PER-XXX: [Persona Name]
Source IDs: [CFD-XXX, CFD-YYY, BR-ZZZ that inform this persona]
Segment: [From v0.2 market segment]

Demographics:
  Role: [Job title / function]
  Context: [Company size, industry, team structure]
  Technical Level: [Novice | Intermediate | Expert]

Behavioral Profile:
  Goals: [What they're trying to achieve]
  Frustrations: [Current pain points — from CFD-]
  Decision Factors: [What influences their choices]
  Current Workflow: [How they solve this today]

Product Relationship:
  Primary Value: [CFD- value hypothesis they care about most]
  Key Features: [FEA-XXX, FEA-YYY most relevant to them]
  Pricing Sensitivity: [From BR- pricing rules]
  Acquisition Channel: [How they'll find us — from BR- targeting]

Marketing Hook: [One-sentence pitch for this persona]
```

**Persona Types:**
| Type | Definition | When to Create |
|------|------------|----------------|
| **Primary** | Core user, drives most revenue | Always (at least 1) |
| **Secondary** | Important but not primary buyer | If distinct needs exist |
| **Negative** | Who we explicitly exclude | If exclusion is strategic |
| **Aspirational** | Future target, not current focus | Only for roadmap planning |

**Evidence Requirements:**
| Persona Field | Must Link To |
|---------------|--------------|
| Goals | CFD- value hypothesis |
| Frustrations | CFD- pain points |
| Decision Factors | CFD- competitive research |
| Key Features | FEA- entries |
| Pricing Sensitivity | BR- pricing rules |
| Acquisition Channel | BR- targeting rules |

**Anti-Patterns:**
| Pattern | Signal | Fix |
|---------|--------|-----|
| Persona explosion | >5 personas | Consolidate by behavior, not demographics |
| Fictional personas | No CFD- links | Every attribute needs evidence |
| Demographic-only | "25-35 year old male" | Focus on behaviors and goals |
| All personas are primary | "Everyone is important" | Rank by revenue potential |
| Copy-paste from competitors | Generic descriptions | Ground in YOUR research |

**Downstream Connections:**
| Consumer | What It Uses | Example |
|----------|--------------|---------|
| **User Journey Mapping** | Each UJ- references a PER- | UJ-001 is for PER-001 |
| **v0.9 GTM** | Marketing messaging per persona | Campaign for PER-002 |
| **Sales Enablement** | Persona-specific pitches | Discovery questions per PER- |
| **Feature Prioritization** | Persona impact scoring | FEA-003 serves PER-001, PER-002 |

---

### SKILL: User Journey Mapping

```yaml
name: prd-v04-user-journey-mapping
stage: v0.4
status: ready
folder: prd-v04-user-journey-mapping/
triggers: "map user journeys", "define user flows", "user missions", "how do users accomplish", "journey mapping", "what steps do users take", "pain to value flow"
id_outputs: [UJ-]
```

**Purpose:** Map user missions from trigger to value moment, organizing features into coherent paths.

**Position in workflow:** v0.4 Persona Definition → **v0.4 User Journey Mapping** → v0.4 Screen Flow Definition

**Execution:**
1. Pull PER- (personas) from Persona Definition
2. Pull FEA- (features) and KPI- (outcomes) from v0.3
3. Define trigger events — what causes the user to start
4. Map step flow using features as building blocks
5. Identify pain points at each step (where friction exists)
6. Mark "moments of value" — where user gets payoff
7. Create UJ- entries with full traceability

**UJ- Output Template:**
```
UJ-XXX: [Journey Title]
Persona: [PER-XXX]
Trigger: [Event that initiates journey]
Goal: [What user wants to accomplish]
Steps:
  1. [Action] → FEA-XXX
  2. [Action] → FEA-XXX
  3. [Action] → FEA-XXX
Pain Points: [Friction moments to design around]
Moment of Value: [When user achieves goal]
KPI Link: [KPI-XXX this journey drives]
Dependencies: [BR-XXX, API-XXX if known]
```

**Journey Types:**
| Type | Purpose | Priority Signal |
|------|---------|-----------------|
| **Core** | Primary value delivery | Must complete for activation |
| **Onboarding** | First-time user setup | Blocks all other journeys |
| **Recovery** | Error handling, support | Retention protection |
| **Power User** | Advanced workflows | Expansion/upsell |

**Anti-Patterns:**
| Pattern | Signal | Fix |
|---------|--------|-----|
| Feature-first journeys | Steps = feature list | Start with user goal, map features to it |
| No trigger | "User opens app" | Define specific trigger event |
| No value moment | Journey ends without payoff | Each journey needs clear outcome |
| Orphaned features | FEA- not in any journey | Add to journey or cut from scope |

---

### SKILL: Screen Flow Definition

```yaml
name: prd-v04-screen-flow-definition
stage: v0.4
status: ready
folder: prd-v04-screen-flow-definition/
triggers: "define screens", "screen flow", "UI structure", "what screens do we need", "information architecture", "navigation design", "wireframe planning"
id_outputs: [SCR-, DES-]
```

**Purpose:** Connect user journeys to screens, defining the UI structure and navigation paths.

**Position in workflow:** v0.4 User Journey Mapping → **v0.4 Screen Flow Definition** → v0.5 Red Team Review

**Execution:**
1. Pull UJ- (journeys) and FEA- (features) from prior steps
2. Inventory unique screens needed across all journeys
3. Map features to screens (many:many relationship)
4. Define navigation structure (hierarchy, transitions)
5. Identify shared components (headers, modals, patterns)
6. Create SCR- entries with feature and journey traceability
7. Establish DES- entries for design system elements

**SCR- Output Template:**
```
SCR-XXX: [Screen Name]
Type: [Page | Modal | Panel | Component]
Purpose: [What user accomplishes on this screen]
Journeys: [UJ-XXX, UJ-YYY that use this screen]
Features: [FEA-XXX, FEA-YYY rendered on this screen]
Primary Actions: [Key user actions available]
Navigation:
  From: [SCR-XXX, SCR-YYY]
  To: [SCR-XXX, SCR-YYY]
Constraints: [BR-XXX rules affecting this screen]
```

**DES- Output Template:**
```
DES-XXX: [Component/Pattern Name]
Type: [Component | Pattern | Layout]
Used In: [SCR-XXX, SCR-YYY]
Purpose: [What this element does]
States: [Default, Loading, Error, Empty, etc.]
```

**Screen Categorization:**
| Category | Examples | Design Priority |
|----------|----------|-----------------|
| **Entry Points** | Login, Landing, Dashboard | High (first impressions) |
| **Core Workflow** | Main task screens | High (value delivery) |
| **Settings/Admin** | Preferences, Account | Medium (necessary evil) |
| **Support/Help** | Docs, Contact, FAQ | Low (failure recovery) |

**Navigation Patterns:**
| Pattern | When to Use | Example |
|---------|-------------|---------|
| **Hub & Spoke** | Dashboard-centric apps | Home → Task → Home |
| **Linear Flow** | Wizard/checkout | Step 1 → Step 2 → Step 3 |
| **Hierarchical** | Content-heavy apps | Category → List → Detail |
| **Flat** | Simple single-purpose apps | All screens peer level |

**Anti-Patterns:**
| Pattern | Signal | Fix |
|---------|--------|-----|
| Screen explosion | >20 unique screens for MVP | Consolidate; use modals/panels |
| Feature-per-screen | 1:1 FEA to SCR mapping | Group related features |
| No shared components | Every screen is unique | Extract DES- patterns |
| Navigation dead-ends | Can't get back | Ensure bidirectional paths |
| Journey disconnect | SCR- not tied to UJ- | Every screen serves a journey |

---

### SKILL: Risk Discovery Interview

```yaml
name: prd-v05-risk-discovery-interview
stage: v0.5
status: ready
folder: prd-v05-risk-discovery-interview/
triggers: "identify risks", "what could go wrong", "red team", "risk assessment", "stress test the idea", "challenge assumptions"
id_outputs: [RISK-]
```

**Purpose:** Surface risks through guided questioning, helping the user consider pivots, constraints, and prioritization.

**Position in workflow:** v0.4 Screen Flow Definition → **v0.5 Risk Discovery Interview** → v0.5 Technical Stack Selection

**Mode:** Interactive interview — AI asks questions, user reflects and decides.

**Design Principles:**
1. **Interview, not inquisition** — Facilitate discovery, don't interrogate
2. **Inform, not kill** — Surface risks so user can mitigate, not abandon
3. **User owns decisions** — AI facilitates, user assigns severity and response
4. **Actionable outputs** — Every risk has a mitigation path or explicit "accept"

**Interview Flow:**
1. **Market Risks** — "What if competitors respond? What if the market shifts?"
2. **Execution Risks** — "What's the hardest part to build? What could slip?"
3. **Adoption Risks** — "What if users don't understand the value? What blocks activation?"
4. **Resource Risks** — "What skills are missing? What's the budget constraint?"
5. **Dependency Risks** — "What external factors could block progress?"

**Question Framework:**
| Category | Example Questions |
|----------|-------------------|
| **Market** | "What happens if [competitor] launches this feature next month?" |
| **Technical** | "Which feature has the most technical uncertainty?" |
| **Adoption** | "What's the biggest friction point in the onboarding journey?" |
| **Resource** | "If you had to cut scope by 50%, what stays?" |
| **Timing** | "What external deadline or event affects this launch?" |

**RISK- Output Template:**
```
RISK-XXX: [Risk Title]
Category: [Market | Technical | Adoption | Resource | Dependency | Timing]
Description: [What could go wrong]
Trigger: [What would cause this to happen]
Impact: [High | Medium | Low] — User assessed
Likelihood: [High | Medium | Low] — User assessed
Early Signal: [How we'd know this is happening]
Response: [Mitigate | Accept | Avoid | Transfer]
Mitigation: [Specific action if Response = Mitigate]
Owner: [Who is responsible for monitoring]
Linked IDs: [FEA-XXX, UJ-XXX, BR-XXX affected]
```

**Risk Response Types:**
| Response | When to Use | Example |
|----------|-------------|---------|
| **Mitigate** | Can reduce impact/likelihood | Add fallback provider for API dependency |
| **Accept** | Low impact or unavoidable | "Competitor might copy us — we accept" |
| **Avoid** | Change plan to eliminate risk | Remove feature with high technical risk |
| **Transfer** | Someone else owns the risk | Use managed service instead of self-host |

**Interview Techniques:**
- **Pre-mortem**: "It's 6 months from now and the product failed. Why?"
- **Constraint forcing**: "If you only had 2 developers, what would you cut?"
- **Dependency mapping**: "What external factor could block launch?"
- **Assumption surfacing**: "What must be true for this to work?"

**Anti-Patterns:**
| Pattern | Signal | Fix |
|---------|--------|-----|
| Risk theater | 50+ risks documented | Focus on top 10 that matter |
| All high severity | Everything is critical | Force rank; only 3-5 can be "High" |
| No owner | Risks without accountability | Every RISK- needs an owner |
| Mitigation = "be careful" | Vague responses | Require specific, testable actions |
| Interview becomes lecture | AI talks more than user | Ask, listen, summarize |

**Downstream Connections:**
| Consumer | What It Uses | Example |
|----------|--------------|---------|
| **Technical Stack Selection** | RISK- constraints affect tech choices | RISK-003 (latency) → choose edge hosting |
| **v0.6 Architecture** | Risk mitigations become requirements | RISK-005 → add circuit breaker |
| **v0.7 Build Execution** | Risk monitoring in EPIC | Track RISK-001 early signals |

---

### SKILL: Technical Stack Selection

```yaml
name: prd-v05-technical-stack-selection
stage: v0.5
status: ready
folder: prd-v05-technical-stack-selection/
triggers: "select tech stack", "what technologies", "build or buy", "technical decisions", "what tools do we need", "evaluate solutions"
id_outputs: [TECH-]
```

**Purpose:** Determine what technologies are needed to build the product, making build/buy/integrate decisions.

**Position in workflow:** v0.5 Risk Discovery Interview → **v0.5 Technical Stack Selection** → v0.6 Architecture

**Mode:** Research + analysis — AI researches options, presents trade-offs, user decides.

**Execution:**
1. Inventory technical needs from FEA- (features) and SCR- (screens)
2. Identify constraints from RISK- entries and BR- rules
3. Categorize each need: Build | Buy | Integrate | Research
4. For Buy/Integrate: research specific tools/services
5. For Research: define what needs to be learned before deciding
6. Create TECH- entries with rationale and trade-offs

**TECH- Output Template:**
```
TECH-XXX: [Technology/Capability Name]
Category: [Build | Buy | Integrate | Research]
Purpose: [What problem this solves]
Features Served: [FEA-XXX, FEA-YYY]
Screens Affected: [SCR-XXX, SCR-YYY]
Risk Constraints: [RISK-XXX that influenced this decision]

Decision: [Specific choice made]
Alternatives Considered: [What else was evaluated]
Trade-offs: [Pros and cons of this choice]
Cost: [Pricing model, estimated cost]
Integration Complexity: [Low | Medium | High]

Research Needed: [If Category = Research, what must be learned]
Evaluation Criteria: [How to decide if Research]
```

**Decision Framework:**
| Category | When to Choose | Examples |
|----------|----------------|----------|
| **Build** | Core differentiator, no good alternatives, full control needed | Custom matching algorithm, proprietary workflow |
| **Buy** | Commodity capability, proven solutions exist, not a differentiator | Payment processing (Stripe), Auth (Auth0) |
| **Integrate** | Ecosystem play, user expects integration, data lives elsewhere | CRM sync, calendar integration |
| **Research** | High uncertainty, multiple viable options, need POC first | "Which vector DB?" — need to benchmark |

**Technology Categories to Address:**
| Layer | Questions to Answer |
|-------|---------------------|
| **Frontend** | Framework? Hosting? Mobile/Web/Both? |
| **Backend** | Language? Framework? Serverless or servers? |
| **Database** | SQL/NoSQL? Managed or self-hosted? |
| **Auth** | Build or buy? SSO requirements? |
| **Payments** | If monetized, what processor? |
| **Infrastructure** | Cloud provider? Edge? CDN? |
| **Integrations** | What external services? APIs? |
| **AI/ML** | If applicable, what models/services? |
| **Analytics** | Product analytics? Error tracking? |
| **DevOps** | CI/CD? Monitoring? Logging? |

**Evaluation Criteria for Buy/Integrate:**
| Criterion | Questions |
|-----------|-----------|
| **Fit** | Does it solve our specific need? |
| **Cost** | What's the pricing model? Scale implications? |
| **Complexity** | How hard to integrate? Ongoing maintenance? |
| **Lock-in** | How hard to switch later? |
| **Maturity** | Production-ready? Good documentation? |
| **Support** | What help is available? |

**Anti-Patterns:**
| Pattern | Signal | Fix |
|---------|--------|-----|
| Resume-driven development | "Let's use [hot tech]" | Choose boring technology for non-differentiators |
| Build everything | No Buy/Integrate decisions | Challenge: is this really a differentiator? |
| Buy everything | No Build decisions | Some things must be custom for your moat |
| Analysis paralysis | Research everything | Time-box research; decide with 70% confidence |
| Ignoring constraints | Tech choice conflicts with RISK- | Review RISK- before finalizing |

**Downstream Connections:**
| Consumer | What It Uses | Example |
|----------|--------------|---------|
| **v0.6 Architecture** | TECH- selections define the system | TECH-001 (Next.js) → frontend architecture |
| **v0.7 Build Execution** | TECH- Research items become spikes | TECH-005 (Research) → EPIC task |
| **Hiring/Resourcing** | TECH- Build items define skills needed | TECH-003 (Rust) → need Rust developer |

---

### SKILL: Architecture Design

```yaml
name: prd-v06-architecture-design
stage: v0.6
status: ready
folder: prd-v06-architecture-design/
triggers: "design architecture", "system design", "how do components connect", "architecture decisions", "technical architecture", "system overview"
id_outputs: [ARC-]
```

**Purpose:** Define how system components connect, establishing boundaries, patterns, and integration approaches.

**Position in workflow:** v0.5 Technical Stack Selection → **v0.6 Architecture Design** → v0.6 Technical Specification

**Mode:** Design + documentation — AI proposes architecture, user validates and refines.

**Execution:**
1. Pull TECH- decisions (what we're building with)
2. Pull RISK- constraints (what we must account for)
3. Pull FEA- features (what the system must do)
4. Define system boundaries (what's in/out of scope)
5. Map component relationships (how parts connect)
6. Document integration patterns for Buy/Integrate decisions
7. Create ARC- entries with rationale

**ARC- Output Template:**
```
ARC-XXX: [Decision Title]
Category: [Structure | Integration | Security | Performance | Data | DevOps]
Context: [What prompted this decision]
Decision: [What we decided]
Rationale: [Why this choice]
Alternatives Rejected: [What else was considered and why not]
Consequences: [What this enables/constrains]
Related IDs: [TECH-XXX, RISK-XXX, FEA-XXX]
```

**Architecture Categories:**

| Category | What It Covers | Example Decisions |
|----------|----------------|-------------------|
| **Structure** | Component organization, boundaries | Monolith vs microservices, module structure |
| **Integration** | External service connections | API gateway pattern, webhook handlers |
| **Security** | Auth, authorization, data protection | JWT strategy, role-based access |
| **Performance** | Scaling, caching, optimization | CDN strategy, database indexing |
| **Data** | Storage, flow, consistency | Event sourcing, CQRS, replication |
| **DevOps** | Deployment, monitoring, CI/CD | Container orchestration, observability |

**System Diagram Elements:**
- **Components**: Services, databases, external systems
- **Boundaries**: Security perimeters, trust zones
- **Data flows**: How information moves between components
- **Integration points**: Where Buy/Integrate items connect

**Integration Pattern Guidance:**

| TECH- Category | Architecture Concern |
|----------------|---------------------|
| **Build** | Internal component design, API surface |
| **Buy** | Vendor abstraction layer, fallback strategy |
| **Integrate** | Data sync approach, webhook handling |

**Anti-Patterns:**
| Pattern | Signal | Fix |
|---------|--------|-----|
| Architecture astronaut | Over-engineering for hypothetical scale | Design for current needs + 10x, not 1000x |
| Missing boundaries | Everything can call everything | Define clear interfaces between components |
| Ignoring RISK- | Architecture doesn't address known risks | Map each High RISK- to architectural mitigation |
| Vendor lock-in | No abstraction over Buy decisions | Add adapter layer for critical integrations |
| Diagram without decisions | Pretty pictures, no ARC- records | Every box needs a decision rationale |

**Downstream Connections:**
| Consumer | What It Uses | Example |
|----------|--------------|---------|
| **Technical Specification** | ARC- informs API and DBT design | ARC-001 (microservices) → separate API contracts |
| **v0.7 Build Execution** | ARC- defines EPIC scope boundaries | ARC-003 (auth service) → EPIC-02 |
| **Infrastructure Setup** | ARC- drives deployment topology | ARC-005 (edge caching) → CDN config |

---

### SKILL: Technical Specification

```yaml
name: prd-v06-technical-specification
stage: v0.6
status: ready
folder: prd-v06-technical-specification/
triggers: "define APIs", "data model", "database schema", "API contracts", "technical spec", "endpoint design", "schema design"
id_outputs: [API-, DBT-]
```

**Purpose:** Define implementation contracts (APIs and data models) that developers will build against.

**Position in workflow:** v0.6 Architecture Design → **v0.6 Technical Specification** → v0.7 Build Execution

**Mode:** Specification — AI drafts contracts based on architecture, user validates requirements.

**Execution:**
1. Pull ARC- decisions (system structure)
2. Pull TECH- Build items (what we're implementing)
3. Pull UJ- journeys (user flows to support)
4. Pull SCR- screens (UI data requirements)
5. Define API contracts for each endpoint
6. Define data models for each entity
7. Validate API ↔ DBT consistency
8. Create API- and DBT- entries

**API- Output Template:**
```
API-XXX: [Endpoint Name]
Method: [GET | POST | PUT | PATCH | DELETE]
Path: [/resource/{id}/action]
Purpose: [What this endpoint does]
Auth: [Public | User | Admin | Service]
Journey: [UJ-XXX that uses this]
Screen: [SCR-XXX that calls this]

Request:
  Headers: [Required headers]
  Body: [JSON schema or description]

Response:
  Success (200/201): [Response shape]
  Errors: [4xx/5xx codes and meanings]

Business Rules: [BR-XXX enforced here]
Data: [DBT-XXX entities accessed]
```

**DBT- Output Template:**
```
DBT-XXX: [Entity Name]
Purpose: [What this entity represents]
Table: [database_table_name]

Fields:
  - id: [type] — Primary key
  - field_name: [type] — Description
  - created_at: timestamp — Record creation
  - updated_at: timestamp — Last modification

Relationships:
  - belongs_to: [DBT-YYY] via [foreign_key]
  - has_many: [DBT-ZZZ]

Indexes:
  - [field_name] — Query pattern it supports

Constraints:
  - [Unique, not null, check constraints]

Business Rules: [BR-XXX that affect this entity]
```

**API Design Principles:**
| Principle | Guidance |
|-----------|----------|
| **Resource-oriented** | URLs represent nouns, not verbs |
| **Consistent naming** | Plural nouns, kebab-case |
| **Stateless** | No server-side session state |
| **Versioned** | /v1/ prefix for breaking changes |
| **Documented errors** | Clear error codes and messages |

**Data Model Principles:**
| Principle | Guidance |
|-----------|----------|
| **Normalized** | Avoid redundancy (unless denormalized for performance) |
| **Audit trail** | created_at, updated_at on all tables |
| **Soft delete** | deleted_at instead of hard delete (if needed) |
| **Foreign keys** | Enforce referential integrity |
| **Index strategy** | Index fields used in WHERE and JOIN |

**Validation Checklist:**
- [ ] Every SCR- screen has APIs to fetch/submit its data
- [ ] Every UJ- journey step maps to API calls
- [ ] Every API- response maps to DBT- fields
- [ ] Every BR- business rule is enforced in API- or DBT-
- [ ] No orphaned DBT- tables (unused by any API-)

**Anti-Patterns:**
| Pattern | Signal | Fix |
|---------|--------|-----|
| API/UI mismatch | Screen needs data not in any API | Add API- or modify existing |
| Schema sprawl | 50+ tables for MVP | Consolidate; YAGNI applies |
| Missing constraints | No validation, anything accepted | Add BR- enforcement |
| N+1 queries baked in | API design requires multiple calls for one view | Add compound endpoints |
| No error handling | Only happy path documented | Define all error responses |

**Downstream Connections:**
| Consumer | What It Uses | Example |
|----------|--------------|---------|
| **v0.7 Build Execution** | API- and DBT- are implementation tasks | EPIC-01 implements API-001–005 |
| **Testing** | API- defines test contracts | TEST-001 validates API-001 |
| **Documentation** | API- becomes API docs | OpenAPI spec from API- entries |

---

### SKILL: Epic Scoping

```yaml
name: prd-v07-epic-scoping
stage: v0.7
status: ready
folder: prd-v07-epic-scoping/
triggers: "create epics", "scope work", "break down work", "context window sizing", "what to build first", "implementation planning", "epic breakdown"
id_outputs: [EPIC-]
```

**Purpose:** Transform v0.6 specifications into context-window-sized work packages (EPICs) that maintain focus without overwhelming cognitive capacity.

**Position in workflow:** v0.6 Technical Specification → **v0.7 Epic Scoping** → v0.7 Test Planning

**Core Concept — Epic = Context Window:**
> An EPIC is not a "big user story." It is a **cognitive boundary**—a scope of work that fits in working memory (human or AI). The goal is to load exactly what's needed to complete a focused task without distraction.

**Execution:**
1. Inventory implementation items from API-, DBT-, FEA-, ARC-
2. Identify natural boundaries (feature clusters, data domains, architectural seams)
3. Size each potential EPIC against context window capacity
4. Sequence EPICs by dependencies (what must be built first)
5. Create EPIC- entries with full ID references
6. Validate: Can an agent complete this EPIC without needing more context than fits in a session?

**EPIC- Output Template:**
```
EPIC-XXX: [Epic Name]
State: [Planned | In Progress | Testing | Complete]
Lifecycle: v0.7 Build Execution

## Objective & Scope
Goal: [What specific outcome this EPIC achieves]
Deliverables:
  - [ ] [Feature/capability A]
  - [ ] [Feature/capability B]
Out of Scope: [What we are NOT doing in this EPIC]

## Context & IDs
Business Rules: [BR-XXX, BR-YYY]
User Journeys: [UJ-XXX, UJ-YYY]
APIs: [API-XXX to API-ZZZ]
Data Models: [DBT-XXX, DBT-YYY]
Architecture: [ARC-XXX]
Features: [FEA-XXX, FEA-YYY]
Tests: [TEST-XXX to TEST-ZZZ] (added during Test Planning)

## Dependencies
Requires: [EPIC-YYY must complete first]
Enables: [EPIC-ZZZ depends on this]

## Context Windows (Build Phases)
Window 1: [Focus Area] — e.g., "Database Schema"
Window 2: [Focus Area] — e.g., "API Endpoints"
Window 3: [Focus Area] — e.g., "UI Integration"
```

**Sizing Rules:**
| Size | Characteristics | When to Split |
|------|-----------------|---------------|
| **Right-sized** | 3-5 API endpoints, 2-4 DBT tables, 1-2 UJ flows | Good fit |
| **Too big** | >10 APIs, >5 tables, multiple unrelated features | Split by domain |
| **Too small** | Single endpoint, no meaningful deliverable | Merge with related |

**Sequencing Framework:**
| Order | Priority | Rationale |
|-------|----------|-----------|
| 1 | Infrastructure EPICs | Auth, DB setup, project scaffolding |
| 2 | Core data model EPICs | Foundation entities other features depend on |
| 3 | Critical path EPICs | UJ- journeys that drive KPI- metrics |
| 4 | Supporting feature EPICs | Secondary features, admin, settings |

**EPIC Template Structure (5 Phases):**
- **Phase A: Plan** — Load context (PRD, specs, README)
- **Phase B: Design** — Update/create ID drafts in specs/
- **Phase C: Build** — Nested Context Windows for focus
- **Phase D: Validate** — Tests, manual checks, code traceability
- **Phase E: Finish** — Temp cleanup, spec finalization

**Anti-Patterns:**
| Pattern | Signal | Fix |
|---------|--------|-----|
| Epic explosion | 20+ EPICs for MVP | Consolidate; most MVPs need 3-7 |
| One mega-EPIC | Everything in one EPIC | Split by architectural boundary |
| No ID references | EPIC without BR-, API-, DBT- links | Every EPIC must reference specs/ |
| Circular dependencies | EPIC-01 needs EPIC-02 which needs EPIC-01 | Identify shared foundation, make it EPIC-00 |
| Context overload | Agent can't hold full EPIC in mind | Split into smaller Context Windows |
| Missing sequencing | No build order defined | Establish explicit dependency chain |

**Downstream Connections:**
| Consumer | What It Uses | Example |
|----------|--------------|---------|
| **Test Planning** | EPIC- scope defines test boundaries | TEST- entries for EPIC-01 scope |
| **Implementation Loop** | EPIC- is execution unit | Work happens inside EPIC context |
| **Session Management** | EPIC Section 0 tracks progress | Where to resume next session |

---

### SKILL: Test Planning

```yaml
name: prd-v07-test-planning
stage: v0.7
status: ready
folder: prd-v07-test-planning/
triggers: "define tests", "test planning", "what to test", "test cases", "test coverage", "TEST-", "test-first"
id_outputs: [TEST-]
```

**Purpose:** Define test cases BEFORE implementation, ensuring every API, business rule, and user journey has verifiable acceptance criteria.

**Position in workflow:** v0.7 Epic Scoping → **v0.7 Test Planning** → v0.7 Implementation Loop

**Core Principle — Test-First:**
> Tests are not an afterthought. They are the **contract** that defines what "done" means. If you can't write the test, you don't understand the requirement.

**Execution:**
1. Pull EPIC- scope (which APIs, DBTs, BRs are included)
2. For each API-: Define request/response tests
3. For each BR-: Define rule validation tests
4. For each UJ-: Define end-to-end flow tests
5. For each DBT-: Define data integrity tests
6. Create TEST- entries linked to implementation IDs
7. Add TEST- references back to EPIC-

**TEST- Output Template:**
```
TEST-XXX: [Test Name]
Type: [Unit | Integration | E2E | Contract | Performance]
Tests: [API-XXX | BR-XXX | UJ-XXX | DBT-XXX]
EPIC: [EPIC-XXX this test belongs to]

Given: [Preconditions]
When: [Action/trigger]
Then: [Expected outcome]

Validation Method: [Automated | Manual | Both]
Automation: [Test file path when implemented]
Priority: [Critical | High | Medium | Low]
```

**Test Type Guidance:**
| Type | What It Tests | When to Use | Example |
|------|---------------|-------------|---------|
| **Unit** | Single function/method | Business logic, calculations | BR-001 limit check |
| **Integration** | Component boundaries | API ↔ Database | API-001 creates DBT-001 record |
| **E2E** | Full user flow | Critical journeys | UJ-001 onboarding completes |
| **Contract** | API shape/types | External integrations | API-001 response matches schema |
| **Performance** | Speed/load | Critical paths | API-001 responds < 200ms |

**Coverage Requirements:**
| ID Type | Minimum Coverage | Rationale |
|---------|------------------|-----------|
| **API-** | 1 happy path + 1 error per endpoint | Endpoints are integration points |
| **BR-** | 1 test per rule, boundary cases included | Rules are product logic |
| **UJ-** | 1 E2E test per core journey | Journeys are user value |
| **DBT-** | Constraint tests for critical fields | Data integrity is foundational |

**Test Priority Framework:**
| Priority | Criteria | Example |
|----------|----------|---------|
| **Critical** | Breaks core value, data loss possible | User auth, payment processing |
| **High** | Blocks key journey, user-facing error | Onboarding flow, main feature |
| **Medium** | Degrades experience, workaround exists | Settings, non-critical features |
| **Low** | Edge case, admin-only, cosmetic | Rare scenarios, admin tools |

**Given-When-Then Examples:**
```
TEST-001: User creation succeeds with valid data
Tests: API-001 (POST /users), BR-001 (email uniqueness)
EPIC: EPIC-01

Given: No user with email "test@example.com" exists
When: POST /users with valid name, email, password
Then: 201 Created, user record in DBT-001, welcome email queued

TEST-002: User creation fails with duplicate email
Tests: API-001, BR-001
EPIC: EPIC-01

Given: User with email "test@example.com" already exists
When: POST /users with same email
Then: 409 Conflict, no new record, clear error message
```

**Anti-Patterns:**
| Pattern | Signal | Fix |
|---------|--------|-----|
| Tests after code | "We'll add tests later" | Define TEST- before writing code |
| Only happy path | No error case tests | Every API needs at least 1 error test |
| Orphaned tests | TEST- not linked to API-/BR-/UJ- | Every test must trace to a spec ID |
| Test explosion | 200+ tests for MVP | Focus on critical paths; 30-50 tests typical |
| Vague assertions | "System works correctly" | Specific, measurable outcomes |
| No automation path | Manual-only critical tests | Critical tests must be automatable |

**Downstream Connections:**
| Consumer | What It Uses | Example |
|----------|--------------|---------|
| **Implementation Loop** | TEST- defines acceptance criteria | EPIC done when TEST-001–010 pass |
| **EPIC Validation (Phase D)** | TEST- list for validation | Run all TEST- for EPIC |
| **CI/CD** | TEST- becomes automated suite | TEST- entries → test files |

---

### SKILL: Implementation Loop

```yaml
name: prd-v07-implementation-loop
stage: v0.7
status: ready
folder: prd-v07-implementation-loop/
triggers: "start building", "implement epic", "coding", "development", "build execution", "implementation", "write code"
id_outputs: []  # Updates existing IDs, creates code
```

**Purpose:** Execute implementation within EPICs following the discipline of test-first development, continuous SoT updates, and code traceability.

**Position in workflow:** v0.7 Test Planning → **v0.7 Implementation Loop** → v0.8 Release

**Mode:** Iterative execution within EPIC context.

**Core Loop (The Heartbeat):**
```
1. Load Context     → Read EPIC, referenced IDs, Session State
2. Select Focus     → Choose a Context Window from Phase C
3. Write Test       → Implement TEST- entry (Red)
4. Write Code       → Implement to pass test (Green)
5. Tag Code         → Add // @implements ID comments
6. Update SoT       → Update specs/ if implementation reveals changes
7. Validate         → Run tests, check traceability
8. Update Session   → Write to Section 0 before stopping
→ REPEAT until EPIC complete
```

**Session State Protocol (MANDATORY):**
Before ending ANY session:
```
## 0. Session State (The "Brain Dump")
- **Last Action**: [What was just completed]
- **Stopping Point**: [Exact file/line or test failure]
- **Next Steps**: [Exact instructions for next session]
- **Context**: [Key decisions, blockers, open questions]
```

**Code Traceability Protocol:**
Every major code unit MUST declare which ID it implements:
```typescript
// @implements API-001 (Create User endpoint)
// @see BR-001 (Email uniqueness)
// @see DBT-001 (Users table)
export async function createUser(data: CreateUserInput): Promise<User> {
  // ...
}
```

**Traceability Patterns:**
| Code Element | Tag Pattern | Example |
|--------------|-------------|---------|
| API handler | `@implements API-XXX` | API endpoint function |
| Business logic | `@implements BR-XXX` | Validation, rules |
| Database model | `@implements DBT-XXX` | Schema definition |
| UI component | `@implements SCR-XXX` | Screen component |
| Test file | `@tests TEST-XXX` | Test implementation |

**SoT Update Rules:**
| Situation | Action |
|-----------|--------|
| Spec matches implementation | No update needed |
| Implementation reveals new constraint | Add BR- entry |
| API shape changed during build | Update API- entry |
| New field needed in schema | Update DBT- entry |
| Spec was wrong/incomplete | Fix spec AND code |

**Context Window Navigation:**
Within an EPIC's Phase C (Build), work through Context Windows sequentially:
```
**Context Window 1: Database Schema**
- [ ] Create DBT-001 migration
- [ ] Seed test data
- [ ] Run migration tests

**Context Window 2: API Endpoints**
- [ ] Implement API-001 (Create)
- [ ] Implement API-002 (Read)
- [ ] Run API tests

**Context Window 3: UI Integration**
- [ ] Build SCR-001 form
- [ ] Connect to API-001
- [ ] Run E2E tests
```

**Phase D Validation Checklist:**
- [ ] All TEST- entries for this EPIC pass
- [ ] `// @implements` tags present in all major code units
- [ ] Manual flow verification against UJ-
- [ ] No orphaned code (everything traces to an ID)
- [ ] specs/ updated to match implementation

**Phase E Finish (Harvest):**
- [ ] Move useful temp/ notes to specs/ or archive/
- [ ] Verify all specs/ files match final code
- [ ] Clean Session State (Section 0)
- [ ] Update EPIC state to Complete
- [ ] Log completion in Change Log

**Anti-Patterns:**
| Pattern | Signal | Fix |
|---------|--------|-----|
| Test-after | Code written, then "add tests" | Write TEST- implementation first |
| Spec drift | Code diverges from specs/ | Update SoT during implementation, not later |
| Missing traceability | Code has no @implements tags | Add tags as you write, not in cleanup |
| Session amnesia | No Section 0 update | ALWAYS update before stopping |
| Context switching | Jumping between EPICs | Finish one EPIC before starting another |
| One-shot building | No iteration, just code dump | Follow the loop: test → code → tag → update |
| Orphaned implementation | Code not linked to any ID | Every function serves an ID |

**Red Flags (Stop and Fix):**
| Signal | Action |
|--------|--------|
| Can't write test | Requirement unclear → revisit spec |
| Test keeps failing | Implementation wrong OR spec wrong → investigate |
| Need to touch code outside EPIC scope | Wrong EPIC boundaries → re-scope |
| Lost context mid-session | Load Session State, verify EPIC context |

**Downstream Connections:**
| Consumer | What It Uses | Example |
|----------|--------------|---------|
| **v0.8 Release** | Completed EPICs ready for deployment | All TEST- pass, SoT current |
| **Code Review** | @implements tags for review context | Reviewer sees which BR- this enforces |
| **Future Sessions** | Session State for continuity | Pick up exactly where left off |

---

### SKILL: Release Planning

```yaml
name: prd-v08-release-planning
stage: v0.8
status: ready
folder: prd-v08-release-planning/
triggers: "release planning", "deployment plan", "how do we deploy", "release criteria", "rollback strategy", "go-live checklist"
id_outputs: [DEP-]
```

**Purpose:** Transform completed EPICs into production-ready releases by defining deployment environments, release criteria, rollback triggers, and operational readiness gates.

**Position in workflow:** v0.7 Implementation Loop → **v0.8 Release Planning** → v0.8 Runbook Creation

**Execution:**
1. Inventory completed EPICs (API-, DBT-, FEA- included)
2. Define deployment environments (staging, production, preview)
3. Establish release criteria (tests, performance, security)
4. Define rollback triggers (error rate, latency thresholds)
5. Document validation steps (smoke tests, journey verification)
6. Create DEP- entries with full traceability

**DEP- Output Template:**
```
DEP-XXX: [Deployment Item Title]
Type: [Environment | Criteria | Rollback | Validation | Step]
Stage: [Pre-deploy | Deploy | Post-deploy | Rollback]
Description: [What this deployment item covers]
Owner: [Who is responsible]
Linked IDs: [EPIC-XXX, API-XXX, TEST-XXX related]
```

**Anti-Patterns:**
| Pattern | Signal | Fix |
|---------|--------|-----|
| Deploy and pray | No validation steps defined | Add DEP- validation entries |
| No rollback plan | "We'll figure it out" | Define triggers and procedures upfront |
| Environment drift | Staging doesn't match production | Infrastructure as code, sync configs |
| Unclear ownership | No one knows who approves | Assign owner to each DEP- |

**Downstream Connections:**
| Consumer | What It Uses | Example |
|----------|--------------|---------|
| **Runbook Creation** | DEP- rollback procedures become runbook inputs | DEP-003 → RUN-005 |
| **Monitoring Setup** | DEP- thresholds inform alerting | DEP-003 (2% error) → MON-001 |
| **v0.9 GTM Strategy** | Release readiness gates launch | All DEP- met → GTM-001 |

---

### SKILL: Runbook Creation

```yaml
name: prd-v08-runbook-creation
stage: v0.8
status: ready
folder: prd-v08-runbook-creation/
triggers: "create runbooks", "operational procedures", "incident response", "on-call guide", "how do we handle incidents", "maintenance procedures"
id_outputs: [RUN-]
```

**Purpose:** Create step-by-step operational playbooks that enable anyone on-call to handle incidents, perform deployments, and execute maintenance tasks.

**Position in workflow:** v0.8 Release Planning → **v0.8 Runbook Creation** → v0.8 Monitoring Setup

**Execution:**
1. Identify critical scenarios (alerts, deployments, RISK- responses)
2. Map each scenario to a runbook
3. Document step-by-step procedures with commands
4. Define escalation paths
5. Add verification steps
6. Create RUN- entries with full traceability

**RUN- Output Template:**
```
RUN-XXX: [Runbook Title]
Category: [Incident | Deployment | Maintenance | Recovery | Escalation]
Trigger: [What initiates this runbook]
Owner: [Team or role responsible]
Last Tested: [Date of last drill/use]
Procedure: [Numbered steps with commands]
Escalation: [When and who to escalate to]
Linked IDs: [MON-XXX, DEP-XXX, RISK-XXX related]
```

**Anti-Patterns:**
| Pattern | Signal | Fix |
|---------|--------|-----|
| Too vague | "Investigate the issue" | Add specific commands and checks |
| No verification | Steps without confirmation | Add verification after each step |
| Assuming knowledge | "You know how to do this" | Write for someone's first day |
| No escalation | Dead ends with no help path | Always define escalation |

**Downstream Connections:**
| Consumer | What It Uses | Example |
|----------|--------------|---------|
| **Monitoring Setup** | RUN- procedures linked from alerts | MON-001 → RUN-001 |
| **On-Call Team** | RUN- as operational reference | Night incident → RUN-001 |
| **Post-Mortems** | RUN- gaps inform improvements | "Runbook missing step" → Update RUN- |

---

### SKILL: Monitoring Setup

```yaml
name: prd-v08-monitoring-setup
stage: v0.8
status: ready
folder: prd-v08-monitoring-setup/
triggers: "monitoring setup", "alerting strategy", "what should we monitor", "observability", "SLOs", "dashboards", "metrics"
id_outputs: [MON-]
```

**Purpose:** Define what to measure, when to alert, and how to visualize system health—creating the observability foundation for rapid incident detection.

**Position in workflow:** v0.8 Runbook Creation → **v0.8 Monitoring Setup** → v0.9 GTM Strategy

**Execution:**
1. Define SLOs (uptime, latency, error rate)
2. Identify key metrics per layer (infrastructure, application, business)
3. Set alert thresholds (warning, critical)
4. Map alerts to runbooks
5. Design dashboards
6. Create MON- entries with full traceability

**MON- Output Template:**
```
MON-XXX: [Monitoring Rule Title]
Type: [Metric | Alert | Dashboard | SLO]
Layer: [Infrastructure | Application | Business | User Experience]
Owner: [Team responsible]
For Metric: Name, Unit, Source, Aggregation
For Alert: Threshold, Severity, Runbook link, Notification
For SLO: Target, Window, Error Budget
Linked IDs: [API-XXX, RUN-XXX, KPI-XXX related]
```

**Anti-Patterns:**
| Pattern | Signal | Fix |
|---------|--------|-----|
| Alert fatigue | Too many alerts, team ignores | Tune thresholds, remove noise |
| No runbook link | Alert fires, no one knows what to do | Every alert → RUN- |
| Missing baselines | No historical comparison | Establish baselines before launch |
| Over-monitoring | 500 metrics, can't find signal | Focus on RED/USE fundamentals |

**Downstream Connections:**
| Consumer | What It Uses | Example |
|----------|--------------|---------|
| **On-Call Team** | MON- alerts trigger response | MON-003 → page engineer |
| **v0.9 Launch Metrics** | MON- provides baseline data | MON-001 baseline → KPI-010 |
| **DEP- Rollback** | MON- thresholds trigger rollback | MON-002 breach → DEP-003 |

---

### SKILL: GTM Strategy

```yaml
name: prd-v09-gtm-strategy
stage: v0.9
status: ready
folder: prd-v09-gtm-strategy/
triggers: "go-to-market", "GTM", "launch plan", "how do we launch", "marketing strategy", "messaging", "launch channels"
id_outputs: [GTM-]
```

**Purpose:** Define how the product reaches its target users—the channels, messaging, timing, and coordination required for a successful launch.

**Position in workflow:** v0.8 Monitoring Setup → **v0.9 GTM Strategy** → v0.9 Launch Metrics

**Execution:**
1. Review target personas (PER-)
2. Define core messaging (from CFD- value hypotheses)
3. Select launch channels (match to personas)
4. Plan launch timeline (pre-launch, launch day, post-launch)
5. Assign ownership
6. Create GTM- entries with full traceability

**GTM- Output Template:**
```
GTM-XXX: [GTM Item Title]
Type: [Messaging | Channel | Timeline | Task | Asset]
Owner: [Person or team responsible]
Status: [Planned | In Progress | Ready | Live]
For Messaging: Audience (PER-), Message, Supporting Evidence (CFD-)
For Channel: Channel, Strategy, Success Metric
For Timeline: Phase, Activities, Dependencies, Milestones
Linked IDs: [PER-XXX, CFD-XXX, KPI-XXX related]
```

**Anti-Patterns:**
| Pattern | Signal | Fix |
|---------|--------|-----|
| Launch and leave | Big launch day, then silence | Plan 30 days of post-launch activity |
| Everything everywhere | All channels, no focus | Pick 2-3 channels, do them well |
| Features not benefits | "We have X, Y, Z" | "You can achieve X, Y, Z" |
| No measurement | "The launch went well (I think)" | Define KPI- before launch |

**Downstream Connections:**
| Consumer | What It Uses | Example |
|----------|--------------|---------|
| **Launch Metrics** | GTM- channels inform tracking | GTM-002 (PH) → KPI-005 |
| **Feedback Loop Setup** | GTM- channels become feedback sources | GTM-002 comments → CFD-100 |
| **Sales** | GTM- messaging for outreach | GTM-001 → sales email template |

---

### SKILL: Launch Metrics

```yaml
name: prd-v09-launch-metrics
stage: v0.9
status: ready
folder: prd-v09-launch-metrics/
triggers: "launch metrics", "launch KPIs", "how do we measure launch success", "tracking setup", "success criteria", "analytics"
id_outputs: [KPI-]
```

**Purpose:** Define how launch success is measured—specific metrics, targets, tracking infrastructure, and the dashboards that make progress visible.

**Position in workflow:** v0.9 GTM Strategy → **v0.9 Launch Metrics** → v0.9 Feedback Loop Setup

**Execution:**
1. Review v0.3 Outcome Definition KPIs
2. Define launch-specific metrics (reach, acquisition, activation, retention)
3. Set targets per timeframe (Day 1, Day 7, Day 30, Day 90)
4. Configure tracking infrastructure
5. Create visibility (dashboards, alerts)
6. Create/Update KPI- entries for launch

**KPI- Output Template (Launch Variant):**
```
KPI-XXX: [Launch Metric Name]
Tier: [Tier 1 | Tier 2 | Tier 3]
Category: [Reach | Acquisition | Activation | Retention | Revenue | Referral]
Stage: Launch (v0.9)
Owner: [Who monitors this metric]
Definition: [Exact calculation formula]
Targets: Day 1, Day 7, Day 30, Day 90
Action Thresholds: Red, Yellow, Green
GTM Connection: [GTM-XXX channels this measures]
v0.3 KPI Link: [KPI-YYY from Outcome Definition if applicable]
```

**Anti-Patterns:**
| Pattern | Signal | Fix |
|---------|--------|-----|
| Vanity metrics only | Tracking visitors but not activation | Focus on funnel progression |
| No targets | "We got 1000 signups!" (is that good?) | Set explicit targets per timeframe |
| Lagging only | Only tracking revenue | Add leading indicators (activation) |
| No action thresholds | Metrics exist but no response plan | Define red/yellow/green zones |

**Downstream Connections:**
| Consumer | What It Uses | Example |
|----------|--------------|---------|
| **Feedback Loop Setup** | KPI- thresholds trigger feedback collection | KPI-103 <30% → investigate with CFD- |
| **Daily Standup** | KPI- dashboard for launch status | "Activation at 42%, on track" |
| **v1.0 Planning** | KPI- baselines for growth targets | KPI-102 baseline → 10% MoM growth |

---

### SKILL: Feedback Loop Setup

```yaml
name: prd-v09-feedback-loop-setup
stage: v0.9
status: ready
folder: prd-v09-feedback-loop-setup/
triggers: "feedback loop", "how do we collect feedback", "user research", "post-launch feedback", "customer feedback", "NPS", "voice of customer"
id_outputs: [CFD-]
```

**Purpose:** Establish systematic channels for capturing, processing, and acting on post-launch user feedback—closing the loop between user experience and product iteration.

**Position in workflow:** v0.9 Launch Metrics → **v0.9 Feedback Loop Setup** → v1.0 Market Adoption

**Execution:**
1. Map feedback touchpoints (support, in-app, community, surveys)
2. Design feedback capture (widgets, taxonomies, workflows)
3. Define processing workflow (triage, categorize, prioritize)
4. Establish feedback → ID flow (CFD- → BR-, FEA-, RISK-)
5. Set up monitoring (volume, sentiment, response time)
6. Create CFD- entries for post-launch feedback

**CFD- Output Template (Post-Launch Feedback):**
```
CFD-XXX: [Feedback Title]
Type: [Support Ticket | Feature Request | Bug Report | NPS Response | Community Post | Survey Response]
Source: [Channel where feedback came from]
Date: [When received]
User Segment: [PER-XXX if identifiable]
Verbatim: "[Exact user quote]"
Processed: Category, Sentiment, Priority, Frequency
Impact Assessment: Users Affected, KPI Impact, Revenue Risk
Action: Response, Internal Action, Linked IDs, Status
Resolution: Outcome, Date, Follow-up
```

**Anti-Patterns:**
| Pattern | Signal | Fix |
|---------|--------|-----|
| Feedback graveyard | Collect but never act | Mandate weekly triage meeting |
| No closing loop | Users never hear back | Require follow-up on High+ priority |
| Volume without insight | "We got 500 tickets" | Categorize and trend analysis |
| Anecdote-driven | "One user said..." | Require frequency data |

**Downstream Connections:**
| Consumer | What It Uses | Example |
|----------|--------------|---------|
| **v1.0 Planning** | CFD- feedback informs roadmap | CFD-101 frequency → FEA-025 priority |
| **Product Development** | CFD- → FEA-, BR- updates | "Users need X" → FEA-030 |
| **Marketing** | CFD- testimonials for GTM- | Positive CFD- → case study |

---

## ID Output Summary

| Stage | Skill | Primary IDs |
|-------|-------|-------------|
| v0.1 | Problem Framing | CFD- (desk research) |
| v0.1 | User Value Articulation | CFD- (value hypotheses) |
| v0.2 | Competitive Landscape | CFD- (intelligence), BR- (rules) |
| v0.2 | Product Type Classification | BR- (type, GTM constraints) |
| v0.3 | Outcome Definition | KPI- (metrics) |
| v0.3 | Pricing Model | BR- (pricing rules) |
| v0.3 | Moat Definition | CFD- (moats), BR- (targeting, defensibility) |
| v0.3 | Feature Value Planning | FEA- (features), BR-FEA- (governance) |
| v0.4 | Persona Definition | PER- (personas) |
| v0.4 | User Journey Mapping | UJ- (user journeys) |
| v0.4 | Screen Flow Definition | SCR- (screens), DES- (design patterns) |
| v0.5 | Risk Discovery Interview | RISK- (risks with mitigations) |
| v0.5 | Technical Stack Selection | TECH- (build/buy/integrate decisions) |
| v0.6 | Architecture Design | ARC- (architecture decisions) |
| v0.6 | Technical Specification | API- (endpoints), DBT- (data models) |
| v0.7 | Epic Scoping | EPIC- (work packages) |
| v0.7 | Test Planning | TEST- (test cases) |
| v0.7 | Implementation Loop | (updates existing IDs, creates code) |
| v0.8 | Release Planning | DEP- (deployment items) |
| v0.8 | Runbook Creation | RUN- (runbooks) |
| v0.8 | Monitoring Setup | MON- (monitoring rules) |
| v0.9 | GTM Strategy | GTM- (go-to-market items) |
| v0.9 | Launch Metrics | KPI- (launch metrics) |
| v0.9 | Feedback Loop Setup | CFD- (post-launch feedback) |

---

### SKILL: SoT Builder

```yaml
name: ghm-sot-builder
stage: Methodology
status: ready
folder: ghm-sot-builder/
triggers: "create SoT", "new source of truth", "I need to track [X] but there's no SoT for it", "create new SoT file", "add artifact type"
id_outputs: []  # Creates new SoT files, not IDs
```

**Purpose:** Create new Source of Truth files when existing templates don't fit your product's unique needs.

**Position in workflow:** Used ad-hoc when forking the repo or when a new artifact type emerges (rare: 3-4 times per product lifecycle).

**When to Use:**
- Forking repo and existing SoT files don't cover your artifact types
- Product needs to track a concept that doesn't fit existing ID prefixes
- Need to consolidate scattered documentation into a canonical SoT

**When NOT to Use:**
- An existing SoT file covers your need (just add entries there)
- You want to track temporary/session-specific data (use `temp/` instead)
- The artifact type is already covered by `ghm-id-register`

**Execution:**
1. Confirm no existing SoT fits the need
2. Design schema (ID prefix, categories, required fields)
3. Draft template using `assets/sot-template.md`
4. Validate template purity (no methodology teaching)
5. Register in SoT.README.md and SoT.UNIQUE_ID_SYSTEM.md

**Core Output:**
A new `SoT/SoT.{NAME}.md` file with:
- YAML frontmatter (version, purpose, id_prefix, authority)
- Purpose block
- Navigation by category
- Entry template structure
- Cross-reference index
- Update protocol

**Template Purity Litmus Test:**
> "Is this teaching me how to maintain the FILE STRUCTURE, or teaching me DOMAIN KNOWLEDGE about what makes good content?"
- File structure maintenance → Keep in template
- Domain knowledge → Move to skill references

**Quality Gates:**
- [ ] ID prefix is unique across all SoT files
- [ ] Template follows purity standard (no methodology teaching)
- [ ] Update protocol included
- [ ] Cross-reference index structure defined
- [ ] SoT.README.md updated
- [ ] SoT.UNIQUE_ID_SYSTEM.md updated

**Anti-Patterns:**
| Pattern | Signal | Fix |
|---------|--------|-----|
| Methodology in template | "Best practices for X" | Move to skill references |
| Duplicate prefix | Using BR- for a new file | Choose unique prefix |
| Too generic | "Notes.md" | Be specific: "Partner_Integrations.md" |
| No update protocol | Template without maintenance section | Add "Update Protocol" section |
| Orphan SoT | Not registered in SoT.README.md | Always register new files |

**Downstream Connections:**
| Consumer | What It Uses | Example |
|----------|--------------|---------|
| **ghm-id-register** | New SoT file for adding entries | Use new PIC- prefix |
| **All PRD skills** | New IDs available for cross-referencing | FEA-001 → PIC-001 |
| **SoT.UNIQUE_ID_SYSTEM.md** | New prefix in registry | PIC- added to prefixes |

---

## Creating New Skills

1. Copy [`SKILL_TEMPLATE/`](SKILL_TEMPLATE/) to `prd-v{XX}-{name}/`
2. Update YAML frontmatter (name, description, triggers)
3. Write concise SKILL.md (<500 lines)
4. Add reference files to `references/`
5. Add templates to `assets/`
6. Update this inventory

See [`README.md`](README.md) for best practices.
