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
| **v0.3 Commercial** | [Outcome Definition](#skill-outcome-definition) | 📋 Spec | — |
| **v0.3 Commercial** | [Pricing Model Selection](#skill-pricing-model-selection) | 📋 Spec | — |
| **v0.3 Commercial** | [Our Moat Articulation](#skill-our-moat-articulation) | 📋 Spec | — |
| **v0.3 Commercial** | [Market Moat Analysis](#skill-market-moat-analysis) | 📋 Spec | — |
| **v0.3 Commercial** | [Fast-Follow Planning](#skill-fast-follow-planning) | 📋 Spec | — |

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
**Gate:** Pricing model selected, Moat articulated, Outcomes defined.

| Skill | Input | Output | IDs Created |
|-------|-------|--------|-------------|
| Outcome Definition | Product type, pricing signals | Measurable KPIs | KPI- |
| Pricing Model Selection | Competitive pricing, product type | Pricing structure | BR- |
| Our Moat Articulation | Competitive landscape | Defensibility strategy | BR- |
| Market Moat Analysis | Competitor moats | Targeting strategy | CFD-, BR- |
| Fast-Follow Planning | Gaps, 1% hypothesis | Validation experiments | CFD-, BR- |

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
status: spec
triggers: "define success metrics", "what are our KPIs", "measurable outcomes"
id_outputs: [KPI-]
```

**Purpose:** Set measurable success criteria informed by product type and market.

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
status: spec
triggers: "how to price", "pricing model", "monetization"
id_outputs: [BR-]
```

**Purpose:** Select pricing that matches value delivery cadence.

**Execution:**
1. Map when customer gets value
2. Align to product type
3. Evaluate models (per-seat, usage, flat, tiered, freemium)
4. Define entry price point
5. Set guardrails (what's off-limits)

---

### SKILL: Our Moat Articulation

```yaml
name: prd-v03-our-moat
stage: v0.3
status: spec
triggers: "what's our moat", "why us", "defensibility"
id_outputs: [BR-]
```

**Purpose:** Define what makes US defensible.

**Moat Types:**
| Type | Time to Build | Marketing Angle |
|------|---------------|-----------------|
| Network Effects | 12-24 mo | "Join X users already..." |
| Switching Costs | 6-12 mo | "Your data, always exportable" |
| Cost Advantages | 12-36 mo | "Simple pricing, no surprises" |
| **Price Clarity** | Immediate | "One price. No gotchas." |
| Speed | 3-6 mo (temp) | "Built for [niche]" |

---

### SKILL: Market Moat Analysis

```yaml
name: prd-v03-market-moat
stage: v0.3
status: spec
triggers: "competitor moats", "switching costs", "who to target"
id_outputs: [CFD-, BR-]
```

**Purpose:** Analyze competitor moats to inform targeting strategy.

**Decision Framework:**
| If market shows... | Target... |
|--------------------|-----------|
| Strong moats, high switching | New-to-category |
| Weak moats, low switching | Switchers |
| High churn triggers despite moats | Switchers at trigger moments |

---

### SKILL: Fast-Follow Planning

```yaml
name: prd-v03-fast-follow
stage: v0.3
status: spec
triggers: "validate before building", "quick experiments", "test hypothesis"
id_outputs: [CFD-, BR-]
```

**Purpose:** Test commercial hypotheses with minimal build investment.

**Execution:**
1. Review competitive gaps and 1% hypothesis
2. Filter for <30 day validation
3. Design experiment (landing page, manual service, concierge)
4. Define go/no-go criteria
5. Execute and log results

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
| v0.3 | Our Moat Articulation | BR- (moat strategy) |
| v0.3 | Market Moat Analysis | CFD- (moats), BR- (targeting) |
| v0.3 | Fast-Follow Planning | CFD- (validation), BR- (go/no-go) |

---

## Creating New Skills

1. Copy [`SKILL_TEMPLATE/`](SKILL_TEMPLATE/) to `prd-v{XX}-{name}/`
2. Update YAML frontmatter (name, description, triggers)
3. Write concise SKILL.md (<500 lines)
4. Add reference files to `references/`
5. Add templates to `assets/`
6. Update this inventory

See [`README.md`](README.md) for best practices.
