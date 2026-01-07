# Skills Inventory: v0.1–v0.3 (Revised)

ID: 2025-01-07_skills-v01-v03_v2 | Owner: Matt | Updated: 2025-01-07
Version note: v2 — Major restructure based on feedback. Moved skills to appropriate stages, reframed Signal Identification as User Value Articulation, added product type classification to Competitive Landscape, split Moat into two skills.
Links: PRD-driven-context-engineering/skills/

---

## Stage-Skill Mapping (Revised)

| Stage | Skills | Rationale |
|-------|--------|-----------|
| **v0.1 Spark** | Problem Framing, User Value Articulation | Validate problem + articulate user-facing value |
| **v0.2 Market** | Competitive Landscape Mapping, Product Type Classification | Understand market before defining segments |
| **v0.3 Commercial** | Outcome Definition, Pricing Model Selection, Our Moat Articulation, Market Moat Analysis, Fast-Follow Planning | Commercial decisions need market context |
| **v0.4/v0.5** | Constraints Scoping | Constrain after understanding customers, market, commercial model |
| **v0.9 Launch** | Unit Economics Baseline | Needs marketing plan to calculate CAC realistically |

---

## v0.1 Spark — Problem & Outcomes

**Stage Purpose:** Validate the problem is real and articulate what users need.
**PRD Section:** v0.1 Spark — Problem & Outcomes
**Gate Criteria:** Problem defined, User value articulated, Open Questions list.

---

### SKILL: Problem Framing

```yaml
---
name: problem-framing
stage: v0.1
owner: AURA
description: Transform a vague idea into 1-3 testable problem statements using Design Thinking structure.
id_outputs: [CFD-]
---
```

**Purpose:** Convert raw sparks into structured, testable problem statements that can be validated or killed quickly.

**When to Use:**
- New product ideation
- Pivot evaluation
- "Should this be a feature or a product?" decisions

**Thinking (before execution):**
- Who specifically is experiencing this pain? Can I find 5 through desk research this week?
- What's the temporal trigger? Why is this painful NOW vs. 3 years ago?
- What would make me abandon this idea? (If nothing, I'm not being honest)
- Am I describing a problem or a solution-in-disguise?
- Do I have 1 problem or actually 2-3 related problems?

**Inputs Required:**
- Initial idea (even informal, messy)
- Target user sketch (role, context, not demographics)
- Founder/stakeholder "why us, why now" narrative

**Execution Pattern:**
1. **Dump** — Write the raw spark as a single unfiltered paragraph
2. **Desk research** — Find 5 examples of people experiencing this problem (forums, reviews, social media, industry reports)
3. **Root cause exploration** — Use 5 Whys cautiously to find root, but don't go so deep you lose the actionable problem
4. **Problem statement drafting** — Write 1-3 problem statements using Design Thinking structure (see template below)
5. **Invert** — "Who does NOT have this problem?" to sharpen target
6. **Kill criteria** — Define 2-3 pieces of evidence that would stop this
7. **Output** — Problem statement(s) + anti-problem + kill criteria + CFD- entries from desk research

**Problem Statement Template (Design Thinking):**
```
[USER TYPE] needs a way to [USER'S NEED] because [INSIGHT/BARRIER].

Example:
"Independent salon owners need a way to track product inventory without manual spreadsheets because they lose 2-3 hours weekly on reordering and often run out of popular items."
```

**Why 1-3 statements?**
- 1 statement = tight focus, easier to validate
- 2-3 statements = exploring whether this is one problem or adjacent problems
- >3 statements = you don't have clarity yet, keep refining

**ID Outputs:**

| Output | ID Type | PRD Location | Example |
|--------|---------|--------------|---------|
| Desk research findings | CFD-001+ | `specs/SoT.customer_feedback.md` | "CFD-001: Reddit r/salonowners — 47 upvotes on post about 'inventory nightmare'" |
| User quotes/evidence | CFD- | `specs/SoT.customer_feedback.md` | "CFD-002: G2 review of competitor: 'I still use spreadsheets because their inventory is too complex'" |
| Problem statement(s) | — | v0.1 Problem Statement | Direct PRD content |
| Kill criteria | — | v0.1 Open Questions | "If <3 of 10 interviewees mention this unprompted, kill" |

**Quality Criteria:**
- [ ] 1-3 problem statements using Design Thinking template
- [ ] "Who" is specific enough to find 5 through desk research
- [ ] "Why now" has a temporal trigger (not evergreen pain)
- [ ] At least 2 kill criteria defined
- [ ] At least 3 CFD- entries from desk research with sources

**Good CFD- Examples:**
- "CFD-001: Reddit r/salonowners — 47 upvotes, 23 comments on post 'How do you track inventory?' Top comment: 'I gave up and just over-order everything'" — *Specific source, quantified engagement, direct quote*
- "CFD-002: Yelp reviews for 3 salons mention 'they were out of my color' — customer-facing pain signal" — *Downstream impact evidence*

**Bad CFD- Examples:**
- "CFD-001: Salon owners struggle with inventory" — *No source, no specificity, no quote*
- "CFD-002: Market research shows inventory is a problem" — *Vague, unverifiable*

**Anti-Patterns (NEVER do this):**
- Solution-first framing ("We need an app that...")
- "Everyone" as target user
- Evergreen problems with no urgency trigger
- No kill criteria (unfalsifiable ideas waste months)
- Skipping desk research and assuming you know the problem
- Going too deep with 5 Whys until problem becomes abstract/philosophical
- CFD- entries without sources or quotes

---

### SKILL: User Value Articulation

```yaml
---
name: user-value-articulation
stage: v0.1
owner: AURA
description: Define what users need this product to do and how THEY will know it worked.
id_outputs: [CFD-]
---
```

**Purpose:** Translate the problem statement into positive user outcomes that can feed onboarding, marketing messages, and success criteria.

**When to Use:**
- After problem framing
- Before any competitive analysis
- To define what "success" looks like from the USER's perspective

**Thinking (before execution):**
- If this product works perfectly, what does the user's life look like?
- How will the USER know it worked? (Not our metrics—their experience)
- What would they tell a friend this product did for them?
- Is the outcome always measurable, or sometimes a feeling/confidence?

**Inputs Required:**
- Validated problem statement(s)
- Desk research findings (CFD- entries)
- User context (when/where they experience the problem)

**Execution Pattern:**
1. **Flip the problem** — Restate each problem as a positive user outcome
2. **User language** — Write outcomes in words users would actually say
3. **Success signals** — For each outcome: How does the USER know it worked?
4. **Onboarding test** — Could this outcome be the first thing shown in onboarding?
5. **Marketing test** — Could this outcome be a headline?
6. **Output** — User value statements + user-facing success signals

**User Value Statement Template:**
```
With [PRODUCT], [USER TYPE] can [POSITIVE OUTCOME] so they [DOWNSTREAM BENEFIT].

They know it's working when [USER-VISIBLE SUCCESS SIGNAL].

Example:
"With ProductX, salon owners can reorder products in 2 clicks so they never run out of client favorites.

They know it's working when they stop getting 'we're out of that color' moments."
```

**ID Outputs:**

| Output | ID Type | PRD Location | Example |
|--------|---------|--------------|---------|
| User outcome language | CFD- | `specs/SoT.customer_feedback.md` | "CFD-003: User value hypothesis — 'Never run out of popular products' resonates based on CFD-001 pain" |
| Success signal validation | CFD- | `specs/SoT.customer_feedback.md` | "CFD-004: Hypothesis — Users measure success by 'zero stockouts' not 'inventory accuracy %'" |

**Quality Criteria:**
- [ ] Each problem statement has a corresponding positive user outcome
- [ ] Outcomes use user language (not product/feature language)
- [ ] At least one user-visible success signal per outcome
- [ ] Outcomes could work as onboarding headline
- [ ] Outcomes could work as marketing headline
- [ ] CFD- entries document the user value hypotheses

**Good User Value Examples:**
- "Never run out of popular products" — *User language, outcome-focused*
- "Know exactly what to reorder before you need it" — *Proactive benefit*
- "Stop losing clients to stockouts" — *Downstream impact they care about*

**Bad User Value Examples:**
- "Accurate inventory tracking" — *Feature language, not outcome*
- "99.5% inventory accuracy" — *Metric users don't think about*
- "Streamlined inventory management" — *Jargon, not user language*

**Success Signal Types:**

| Signal Type | Example | User-Visible? |
|-------------|---------|---------------|
| Absence of pain | "No more 'we're out' moments" | Yes — they notice when problem stops |
| Time saved | "Reordering takes 5 min instead of 2 hours" | Yes — if dramatic |
| Confidence gained | "I know what's in stock without checking" | Yes — feeling, not metric |
| Downstream outcome | "Clients get what they came for" | Yes — customer satisfaction |
| Internal metric | "Inventory accuracy 99.5%" | No — users don't track this |

**Anti-Patterns (NEVER do this):**
- Feature-focused language ("track inventory," "manage products")
- Internal metrics as success signals (accuracy %, sync rate)
- Outcomes users have to be taught to value
- Skipping the onboarding/marketing test
- Generic outcomes that apply to any product

---

## v0.2 Market Definition — Competitive Landscape & Product Type

**Stage Purpose:** Understand the market, competitors, and what type of product we're building.
**PRD Section:** v0.2 Market Definition — Segments & ICP
**Gate Criteria:** Competitive landscape mapped, Product type identified, Segments sized.

---

### SKILL: Competitive Landscape Mapping

```yaml
---
name: competitive-landscape
stage: v0.2
owner: AURA
description: Map what exists today, who's solving similar problems, and where gaps exist.
id_outputs: [CFD-, BR-]
---
```

**Purpose:** Understand the market reality before defining our position in it.

**When to Use:**
- After problem framing and user value articulation
- Before defining ICP or pricing
- To determine what type of product we're building

**Thinking (before execution):**
- What do potential users do TODAY? (Before I search for competitors)
- Who else is validating this problem by building solutions?
- Is "do nothing" or "manual workaround" the real competitor?
- What industry verticals are being served? Which are ignored?
- What geographies are being served? Which are ignored?

**Inputs Required:**
- Problem statement(s)
- User value articulation
- Initial target user description

**Execution Pattern:**
1. **Current state** — Document what WE do today (if existing product) or what TARGET USERS do today
2. **Competitor discovery** — Search for solutions addressing similar problems:
   - Direct competitors (same problem, same users)
   - Adjacent solutions (related problems, overlapping users)
   - Manual workarounds (spreadsheets, pen/paper, hiring someone)
   - "Do nothing" (what happens if they ignore the problem)
3. **Industry analysis** — Which verticals are served vs. have gaps?
4. **Geography analysis** — Which geos are served vs. have gaps?
5. **Feature matrix** — Compare relevant features across competitors
6. **1% better hypothesis** — What specific improvement could win?
7. **Output** — Landscape map + feature matrix + gap analysis + 1% hypothesis

**ID Outputs:**

| Output | ID Type | PRD Location | Example |
|--------|---------|--------------|---------|
| Competitor intelligence | CFD-101+ | `specs/SoT.customer_feedback.md` | "CFD-101: Competitor X — $29/mo, 4.2★ on Capterra, 'great for big salons, overkill for small'" |
| Feature comparison | CFD- | `specs/SoT.customer_feedback.md` | "CFD-102: Feature matrix shows no competitor has 1-click reorder from low-stock alert" |
| Industry gaps | CFD- | `specs/SoT.customer_feedback.md` | "CFD-103: All competitors target US/UK — no Spanish-language option for LATAM market" |
| Competitive constraints | BR- | `specs/SoT.BUSINESS_RULES.md` | "BR-101: Must beat Competitor X on mobile (their top complaint in reviews)" |

**Industry/Geo Gap Template:**

| Vertical | Competitors Serving | Gap Opportunity |
|----------|---------------------|-----------------|
| Hair salons | CompA, CompB, CompC | Saturated — no gap |
| Nail salons | CompA (poorly) | Underserved — feature gaps |
| Barbershops | None specifically | Unserved — potential niche |
| Med spas | CompD (enterprise only) | SMB gap |

| Geography | Competitors | Gap Opportunity |
|-----------|-------------|-----------------|
| US | CompA, CompB, CompC | Saturated |
| UK | CompA, CompB | Moderate competition |
| LATAM | None (no Spanish) | Language gap |
| APAC | CompE only | Underserved |

**Feature Matrix Template:**

| Feature | Us (planned) | CompA | CompB | CompC | Gap? |
|---------|--------------|-------|-------|-------|------|
| Low-stock alerts | ✓ | ✓ | ✓ | ✗ | No |
| 1-click reorder | ✓ | ✗ | ✗ | ✗ | **YES** |
| Mobile app | ✓ | Partial | ✓ | ✗ | Partial |
| Spanish language | ✓ | ✗ | ✗ | ✗ | **YES** |

**1% Better Hypothesis Template:**
```
We can be 1% better than [COMPETITOR] by [SPECIFIC IMPROVEMENT] for [SPECIFIC SEGMENT].

This matters because [EVIDENCE FROM RESEARCH].

Example:
"We can be 1% better than CompA by offering 1-click reorder from low-stock alerts for independent salon owners.

This matters because CompA users' #1 complaint on G2 is 'too many clicks to reorder' (CFD-102)."
```

**Quality Criteria:**
- [ ] "What we/users do today" documented first
- [ ] At least 3 direct competitors + 2 indirect/substitutes
- [ ] "Do nothing" and manual workarounds analyzed
- [ ] Industry vertical gaps identified
- [ ] Geographic gaps identified
- [ ] Feature comparison matrix completed
- [ ] 1% better hypothesis with evidence
- [ ] All intelligence logged as CFD- entries

**Anti-Patterns (NEVER do this):**
- Starting with competitor search before understanding user's current state
- Only analyzing funded/visible startups
- Ignoring "do nothing" as the real competitor
- Feature matrix without user-relevant features
- 1% hypothesis without evidence from research
- Gaps that don't connect to validated problem

---

### SKILL: Product Type Classification

```yaml
---
name: product-type-classification
stage: v0.2
owner: AURA
description: Determine if this is a Fast Follow, Slice, or Innovation product to set expectations for sales cycle and positioning.
id_outputs: [BR-]
---
```

**Purpose:** Classify the product type to set realistic expectations and choose appropriate go-to-market strategy.

**When to Use:**
- After competitive landscape mapping
- Before pricing or positioning decisions
- To align team on what kind of build this is

**Thinking (before execution):**
- Are there successful products already validating this problem?
- Are users currently paying for solutions? How much?
- Is this a whole product or a piece of an ecosystem?
- How much user education will sales require?

**Product Type Framework:**

| Type | Definition | Evidence | Sales Cycle | Positioning Strategy |
|------|------------|----------|-------------|---------------------|
| **Fast Follow** | Direct competition exists, problem validated, users paying | Multiple funded competitors, clear market pricing, users switching between solutions | Short — users understand the category | "Better/cheaper/faster than X" — comparative |
| **Slice** | Fits into existing ecosystem, solves specific problem others ignore | Ecosystem exists (e.g., Shopify apps), users cobbling together solutions, gap in integrations | Medium — need to explain the slice | "The best [specific thing] for [ecosystem]" — niche |
| **Innovation** | New category, users not paying for this yet | No direct competitors, users don't know they need it, requires behavior change | Long — education required | "A new way to [outcome]" — category creation |

**Execution Pattern:**
1. **Evidence review** — Look at competitive landscape findings
2. **Payment validation** — Are users currently paying for similar solutions?
3. **Ecosystem check** — Does this fit into a larger ecosystem or stand alone?
4. **Education assessment** — How much do users need to learn?
5. **Classification** — Assign type with confidence level
6. **Implications** — Document what this means for sales, pricing, positioning
7. **Output** — Product type + evidence + strategic implications

**ID Outputs:**

| Output | ID Type | PRD Location | Example |
|--------|---------|--------------|---------|
| Product type decision | BR- | `specs/SoT.BUSINESS_RULES.md` | "BR-102: Product type = Fast Follow (salon inventory has 5+ funded competitors, users paying $20-50/mo)" |
| Go-to-market constraint | BR- | `specs/SoT.BUSINESS_RULES.md` | "BR-103: Positioning must be comparative ('better than CompA') not educational" |
| Sales cycle expectation | BR- | `specs/SoT.BUSINESS_RULES.md` | "BR-104: Target sales cycle <14 days (users already understand category)" |

**Classification Decision Tree:**

```
Are users currently paying for solutions to this problem?
├── YES → Are there 3+ direct competitors?
│   ├── YES → FAST FOLLOW
│   └── NO → Does this fit into an existing ecosystem?
│       ├── YES → SLICE
│       └── NO → Early FAST FOLLOW or INNOVATION (assess education needed)
└── NO → Does this fit into an existing ecosystem?
    ├── YES → SLICE (ecosystem validated, problem slice is new)
    └── NO → INNOVATION (category creation)
```

**Quality Criteria:**
- [ ] Classification based on competitive landscape evidence
- [ ] Payment validation documented (are users paying today?)
- [ ] Ecosystem fit assessed
- [ ] Education requirement estimated
- [ ] Strategic implications documented
- [ ] BR- entries capture classification and implications

**Anti-Patterns (NEVER do this):**
- Classifying as Innovation to avoid competition (usually wishful thinking)
- Ignoring that Fast Follow requires differentiation (not just "me too")
- Treating Slice products as standalone (ecosystem integration is critical)
- Underestimating Innovation sales cycle

---

## v0.3 Commercial Model — Pricing, Positioning & Moat

**Stage Purpose:** Define how we win commercially.
**PRD Section:** v0.3 Commercial Model — Pricing & Positioning
**Gate Criteria:** Pricing model selected, Moat articulated, Outcomes defined.

---

### SKILL: Outcome Definition

```yaml
---
name: outcome-definition
stage: v0.3
owner: AURA
description: Define measurable business outcomes now that commercial model context exists.
id_outputs: [KPI-]
---
```

**Purpose:** Set measurable success criteria informed by product type, pricing model, and market context.

**When to Use:**
- After competitive landscape and product type classification
- Before finalizing pricing
- When stakeholders need aligned success criteria

**Thinking (before execution):**
- Given our product type (Fast Follow/Slice/Innovation), what timeline is realistic?
- Given our pricing model, what's a meaningful revenue target?
- What leading indicators predict the lagging outcomes?
- What's the minimum success that justifies continued investment?

**Inputs Required:**
- Product type classification
- Competitive pricing signals
- User value articulation (from v0.1)

**Execution Pattern:**
1. **Product type calibration** — Adjust expectations based on Fast Follow/Slice/Innovation
2. **Outcome brainstorm** — List 10+ possible outcomes
3. **Filter** — Keep only those where "achieving ONLY this = celebration"
4. **Quantify** — Add numbers, dates based on market reality
5. **Sequence** — Tag as leading (early) or lagging (late)
6. **Feasibility** — How would we measure in week 1?
7. **Output** — Outcome table with realistic targets

**Outcome Calibration by Product Type:**

| Product Type | Realistic 90-day Outcome | Why |
|--------------|--------------------------|-----|
| Fast Follow | 10-50 paying customers, $1-5K MRR | Users understand category, shorter sales cycle |
| Slice | 5-20 paying customers, integration partnerships | Ecosystem validation matters as much as revenue |
| Innovation | 3-10 design partners, validated willingness-to-pay | Education cycle is longer, early adopters first |

**ID Outputs:**

| Output | ID Type | PRD Location | Example |
|--------|---------|--------------|---------|
| Success metrics | KPI-001+ | PRD v0.3 or `specs/` | "KPI-001: 3 paying customers within 60 days (Fast Follow baseline)" |
| Leading indicators | KPI- | PRD v0.3 | "KPI-002: 20% landing page → trial conversion (week 2 signal)" |

**Quality Criteria:**
- [ ] Outcomes calibrated to product type
- [ ] Each outcome has number + date
- [ ] At least 1 leading indicator
- [ ] Measurement method defined
- [ ] KPI- entries created

**Anti-Patterns (NEVER do this):**
- Setting Innovation timelines for Fast Follow product (or vice versa)
- Vanity metrics without conversion context
- All lagging indicators
- Outcomes that can't be measured until month 6

---

### SKILL: Pricing Model Selection

```yaml
---
name: pricing-model
stage: v0.3
owner: AURA
description: Choose monetization structure aligned with value delivery and product type.
id_outputs: [BR-]
---
```

*[Keeping this skill largely as-is from v1 — it was marked as "very good and in the right place"]*

**Purpose:** Select a pricing model that matches HOW and WHEN customers receive value.

**When to Use:**
- After competitive analysis and product type classification
- When unit economics need definition
- Before building any pricing UI/logic

**Thinking (before execution):**
- When does the customer get value? (One-time? Recurring? Per-use?)
- What do competitors charge? Why that model?
- What's the entry price point? (What gets someone in the door?)
- What pricing moves are OFF-LIMITS for us?
- Does our product type affect pricing? (Innovation may need different model than Fast Follow)

**Inputs Required:**
- Competitive pricing signals
- Product type classification
- ICP willingness-to-pay indicators
- Value delivery pattern

**Execution Pattern:**
1. **Map value timing** — When does customer get value? How often?
2. **Product type alignment** — Does pricing fit our type?
   - Fast Follow: Must be competitive with existing pricing
   - Slice: Often usage-based or tied to ecosystem value
   - Innovation: May need value-based or outcome-based pricing
3. **Model evaluation** — Consider: per-seat, usage, flat, tiered, freemium
4. **Competitive test** — What model do competitors use? Why?
5. **Entry definition** — What's the minimum viable price point?
6. **Guardrails** — What pricing moves are off-limits?
7. **Output** — Model recommendation + tier sketch + guardrails

**ID Outputs:**

| Output | ID Type | PRD Location | Example |
|--------|---------|--------------|---------|
| Pricing rules | BR-105+ | `specs/SoT.BUSINESS_RULES.md` | "BR-105: Usage-based at $0.02/product tracked" |
| Tier definitions | BR- | `specs/SoT.BUSINESS_RULES.md` | "BR-106: Free tier limited to 50 products" |
| Pricing guardrails | BR- | `specs/SoT.BUSINESS_RULES.md` | "BR-107: No annual-only plans" |

**Quality Criteria:**
- [ ] Model matches value delivery cadence
- [ ] Model appropriate for product type
- [ ] At least 2 alternatives considered with trade-offs
- [ ] Entry price point defined
- [ ] Guardrails documented
- [ ] All pricing rules as BR- entries

**Anti-Patterns (NEVER do this):**
- Copying competitor pricing without understanding their model
- Innovation product with Fast Follow pricing expectations
- No entry point (only expensive tiers)
- Pricing decisions without BR- entries

---

### SKILL: Our Moat Articulation

```yaml
---
name: our-moat-articulation
stage: v0.3
owner: AURA
description: Define what makes US defensible and what actions deepen that moat.
id_outputs: [BR-]
---
```

**Purpose:** Honestly assess OUR defensibility and what actions would strengthen it.

**When to Use:**
- After competitive analysis
- When explaining "why us" to investors/partners
- To guide build priorities

**Thinking (before execution):**
- What can competitors NOT easily copy about us?
- Is price a moat for us? (Clarity and simplicity can be)
- How long until a competitor catches up?
- What build decisions would DEEPEN our moat?
- How does our moat feed marketing messaging?

**Inputs Required:**
- Competitive landscape
- Team/founder unique strengths
- Pricing model

**Moat Types (including Price):**

| Moat Type | Description | Maturity Time | Marketing Angle |
|-----------|-------------|---------------|-----------------|
| Network Effects | Value increases with users | 12-24 months | "Join X users already..." |
| Switching Costs | Painful to leave | 6-12 months | "Your data, always exportable" (reduces fear) |
| Cost Advantages | Cheaper to operate | 12-36 months | "Simple pricing, no surprises" |
| Brand/Trust | Reputation matters | 24-48 months | "Trusted by..." |
| Data/Learning | Proprietary insight | 12-24 months | "Gets smarter as you use it" |
| Speed | First-mover in niche | 3-6 months (temporary) | "Built for [specific niche]" |
| **Price Clarity** | Simpler/clearer than competitors | Immediate | "One price. No gotchas." |

**Execution Pattern:**
1. **Inventory** — List what competitors CAN'T easily copy
2. **Include price** — Is our pricing simpler, clearer, or more honest?
3. **Classify** — Map to moat types
4. **Assess strength** — How long until competitor catches up?
5. **Marketing translation** — How does this become messaging?
6. **Deepening actions** — What builds this moat over time?
7. **Output** — Moat type + strength + marketing angle + actions

**ID Outputs:**

| Output | ID Type | PRD Location | Example |
|--------|---------|--------------|---------|
| Moat strategy | BR-108+ | `specs/SoT.BUSINESS_RULES.md` | "BR-108: Our moat = price clarity (one flat rate vs competitor's complex tiers)" |
| Moat-building priorities | BR- | `specs/SoT.BUSINESS_RULES.md` | "BR-109: Prioritize features that increase data lock-in (export always available to reduce anxiety)" |
| Marketing angle | BR- | `specs/SoT.BUSINESS_RULES.md` | "BR-110: Lead messaging with 'simple pricing' (CFD-101 shows competitor pricing is top complaint)" |

**Quality Criteria:**
- [ ] Moat type explicitly named
- [ ] Price/clarity considered as potential moat
- [ ] Honest strength assessment
- [ ] Marketing translation defined
- [ ] At least 2 moat-building actions
- [ ] BR- entries capture strategy

**Anti-Patterns (NEVER do this):**
- Claiming "better product" as a moat
- Ignoring price as a moat option
- Moat strategy with no marketing translation
- No BR- entries (moat becomes aspirational)

---

### SKILL: Market Moat Analysis

```yaml
---
name: market-moat-analysis
stage: v0.3
owner: AURA
description: Analyze competitor moats and switching dynamics to inform targeting strategy.
id_outputs: [CFD-, BR-]
---
```

**Purpose:** Understand whether to target new customers, switching customers, or both—based on market moat realities.

**When to Use:**
- After competitive landscape mapping
- When deciding acquisition strategy
- To understand switching friction in the market

**Thinking (before execution):**
- How hard is it for users to switch FROM competitors?
- What's the switching cost (time, data migration, learning curve)?
- Are competitor moats strong or weak?
- Should we target new-to-category or switching customers?
- What would make someone switch despite friction?

**Inputs Required:**
- Competitive landscape
- Competitor reviews (especially churn reasons)
- User workflow understanding

**Execution Pattern:**
1. **Switching cost audit** — For each competitor: What does switching require?
2. **Moat strength assessment** — Rate each competitor's moat
3. **Churn trigger research** — Why DO people leave competitors?
4. **Target decision** — New customers, switching, or both?
5. **Switching enablement** — If targeting switchers, what reduces friction?
6. **Output** — Market moat map + targeting decision + switching strategy

**Market Moat Assessment Template:**

| Competitor | Moat Type | Strength | Switching Cost | Churn Triggers | Target? |
|------------|-----------|----------|----------------|----------------|---------|
| CompA | Data lock-in | Strong | High (no export) | Price increases, poor support | Hard target |
| CompB | Brand | Moderate | Low (easy export) | Missing features | Good target |
| CompC | None | Weak | Very low | Any reason | Easy target |

**Targeting Decision Framework:**

| If market shows... | Target... | Because... |
|--------------------|-----------|------------|
| Strong moats, high switching costs | New-to-category customers | Switching is too hard, find greenfield |
| Weak moats, low switching costs | Switchers from competitors | Easy wins, users already educated |
| Mixed | Both, with different messaging | Segment your acquisition approach |
| High churn triggers despite strong moats | Switchers at trigger moments | Time campaigns to trigger events |

**ID Outputs:**

| Output | ID Type | PRD Location | Example |
|--------|---------|--------------|---------|
| Competitor moat assessment | CFD-104+ | `specs/SoT.customer_feedback.md` | "CFD-104: CompA has strong data lock-in — no export feature, users complain but don't leave" |
| Targeting decision | BR- | `specs/SoT.BUSINESS_RULES.md` | "BR-111: Target switchers from CompB/CompC (weak moats), avoid CompA users" |
| Switching enablement | BR- | `specs/SoT.BUSINESS_RULES.md` | "BR-112: Build CompB import tool as launch feature" |

**Quality Criteria:**
- [ ] Each major competitor's moat assessed
- [ ] Switching costs documented
- [ ] Churn triggers identified from reviews/research
- [ ] Targeting decision made with rationale
- [ ] If targeting switchers, friction-reduction plan exists
- [ ] CFD- and BR- entries capture analysis

**Anti-Patterns (NEVER do this):**
- Assuming all competitors have weak moats
- Targeting customers with high switching costs without a plan
- Ignoring that new-to-category may need more education
- No switching enablement for switcher-targeting strategy

---

### SKILL: Fast-Follow Planning

```yaml
---
name: fast-follow
stage: v0.3
owner: AURA
description: Define quick validation experiments before major build investment.
id_outputs: [CFD-, BR-]
---
```

*[Keeping largely as-is from v1]*

**Purpose:** Test commercial hypotheses with minimal build investment.

**When to Use:**
- After pricing model selected
- Before major development investment
- When testing market response to positioning

**Execution Pattern:**
1. **Gap review** — Review competitive gaps and 1% better hypothesis
2. **Filter for speed** — What could we validate in <30 days?
3. **Validation design** — Landing page? Manual service? Concierge MVP?
4. **Criteria definition** — What result = proceed? What = kill?
5. **Output** — Opportunity table + validation plan + go/no-go criteria

**ID Outputs:**

| Output | ID Type | PRD Location | Example |
|--------|---------|--------------|---------|
| Validation results | CFD-105+ | `specs/SoT.customer_feedback.md` | "CFD-105: Landing page got 12% signup (target 5%)" |
| Go/no-go rules | BR- | `specs/SoT.BUSINESS_RULES.md` | "BR-113: Proceed only if >5% conversion" |

**Quality Criteria:**
- [ ] Each experiment achievable in <30 days
- [ ] Go/no-go criteria are binary
- [ ] All results logged as CFD-

---

## Skills Moved to Later Stages

### Constraints Scoping → v0.4 or v0.5

**Rationale:** Constraints need market, competitive, and commercial context to be meaningful. Constraining too early leads to arbitrary limits; constraining after understanding customers/market/model produces enforceable boundaries.

### Unit Economics Baseline → v0.9 Launch

**Rationale:** Realistic CAC requires marketing plan. Unit economics before GTM strategy produces guesses, not analysis.

---

## ID Output Summary (Revised)

| Stage | Skill | Primary ID Outputs |
|-------|-------|-------------------|
| v0.1 | Problem Framing | CFD- (desk research) |
| v0.1 | User Value Articulation | CFD- (value hypotheses) |
| v0.2 | Competitive Landscape | CFD- (intelligence), BR- (competitive rules) |
| v0.2 | Product Type Classification | BR- (type, GTM constraints) |
| v0.3 | Outcome Definition | KPI- (metrics) |
| v0.3 | Pricing Model | BR- (pricing rules) |
| v0.3 | Our Moat Articulation | BR- (moat strategy) |
| v0.3 | Market Moat Analysis | CFD- (competitor moats), BR- (targeting) |
| v0.3 | Fast-Follow Planning | CFD- (validation), BR- (go/no-go) |

---

## Research Prompts Needed

1. **Problem Framing:** Design Thinking problem statement structures — what formats work best? Examples of good/bad problem statements.

2. **User Value Articulation:** How do successful products articulate user outcomes in onboarding and marketing? Good/bad examples.

3. **Competitive Landscape:** How do teams actually do competitive analysis? Shortcuts that work vs. fail. Feature matrix best practices.

4. **Product Type:** Case studies of Fast Follow vs. Slice vs. Innovation — how did classification affect GTM success?

5. **Market Moat Analysis:** Research on switching costs and moat strength — how do B2B SaaS companies assess competitor defensibility?

---

## Next Steps

1. Matt reviews restructured skills — gaps? misalignments?
2. Prioritize which research prompts to run first
3. Sharpen skills with real examples
4. Define SKILL.md file structure for repo
