# Skills Inventory

> **Navigation index for PRD lifecycle skills. Each skill transforms inputs into outputs with evidence.**

---

## Quick Navigation

| Stage | Skill | Status | Folder |
|-------|-------|--------|--------|
| **v0.1 Spark** | [Problem Framing](#skill-problem-framing) | ✅ Ready | [`prd-v01-problem-framing/`](prd-v01-problem-framing/) |
| **v0.1 Spark** | [User Value Articulation](#skill-user-value-articulation) | ✅ Ready | [`prd-v01-user-value-articulation/`](prd-v01-user-value-articulation/) |
| **v0.2 Market** | [Competitive Landscape Mapping](#skill-competitive-landscape-mapping) | ✅ Ready | [`prd-v02-competitive-landscape-mapping/`](prd-v02-competitive-landscape-mapping/) |
| **v0.2 Market** | [Product Type Classification](#skill-product-type-classification) | ✅ Ready | [`prd-v02-product-type-classification/`](prd-v02-product-type-classification/) |
| **v0.3 Commercial** | [Outcome Definition](#skill-outcome-definition) | ✅ Ready | [`prd-v03-outcome-definition/`](prd-v03-outcome-definition/) |
| **v0.3 Commercial** | [Pricing Model Selection](#skill-pricing-model-selection) | ✅ Ready | [`prd-v03-pricing-model/`](prd-v03-pricing-model/) |
| **v0.3 Commercial** | [Moat Definition](#skill-moat-definition) | ✅ Ready | [`prd-v03-moat-definition/`](prd-v03-moat-definition/) |
| **v0.3 Commercial** | [Feature Value Planning](#skill-feature-value-planning) | ✅ Ready | [`prd-v03-features-value-planning/`](prd-v03-features-value-planning/) |
| **v0.4 Journeys** | [Persona Definition](#skill-persona-definition) | 📋 Spec | `prd-v04-persona-definition/` |
| **v0.4 Journeys** | [User Journey Mapping](#skill-user-journey-mapping) | 📋 Spec | `prd-v04-user-journey-mapping/` |
| **v0.4 Journeys** | [Screen Flow Definition](#skill-screen-flow-definition) | 📋 Spec | `prd-v04-screen-flow-definition/` |
| **v0.5 Review** | [Risk Discovery Interview](#skill-risk-discovery-interview) | 📋 Spec | `prd-v05-risk-discovery-interview/` |
| **v0.5 Review** | [Technical Stack Selection](#skill-technical-stack-selection) | 📋 Spec | `prd-v05-technical-stack-selection/` |
| **v0.6 Architecture** | [Architecture Design](#skill-architecture-design) | 📋 Spec | `prd-v06-architecture-design/` |
| **v0.6 Architecture** | [Technical Specification](#skill-technical-specification) | 📋 Spec | `prd-v06-technical-specification/` |

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

### v0.5 Red Team Review — Risks & Stack Selection

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

**Execution:**
1. Dump raw idea as unfiltered paragraph
2. Desk research — find 5 examples of people experiencing this problem
3. Root cause exploration — 5 Whys (don't go too deep)
4. Draft 1-3 problem statements using Design Thinking format
5. Define kill criteria

**Template:** `[USER TYPE] needs a way to [NEED] because [INSIGHT/BARRIER].`

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

**Framework:**
| Type | Evidence | Sales Cycle | Positioning |
|------|----------|-------------|-------------|
| **Fast Follow** | 3+ competitors, users paying | Short | "Better/cheaper than X" |
| **Slice** | Ecosystem exists, gap in integrations | Medium | "Best [thing] for [ecosystem]" |
| **Innovation** | No competitors, behavior change needed | Long | "New way to [outcome]" |

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

**Execution:**
1. Map when customer gets value (value timing)
2. Align to product type
3. Evaluate models (per-seat, usage, flat, tiered, freemium)
4. Calculate SMB penalty for per-user competitors
5. Define entry price point with unit economics check
6. Set guardrails (what's off-limits)
7. Plan WTP validation

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

---

### SKILL: Persona Definition

```yaml
name: prd-v04-persona-definition
stage: v0.4
status: spec
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
status: spec
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
status: spec
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
status: spec
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
status: spec
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
status: spec
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
status: spec
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

---

## Creating New Skills

1. Copy [`SKILL_TEMPLATE/`](SKILL_TEMPLATE/) to `prd-v{XX}-{name}/`
2. Update YAML frontmatter (name, description, triggers)
3. Write concise SKILL.md (<500 lines)
4. Add reference files to `references/`
5. Add templates to `assets/`
6. Update this inventory

See [`README.md`](README.md) for best practices.
