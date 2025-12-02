---
version: 2.0
purpose: To serve as a living document, progressively built from validated market research to define a product's revenue-first requirements.
summary: Overhauled template to integrate a progressive, evidence-based, and revenue-first framework.
last_updated: 2025-08-20
---

# [Product Name] Product Requirements Document

**Authority**: See [WORKFLOW_MASTER.md](../workflows/WORKFLOW_MASTER.md) for complete workflow processes  
**Template Usage**: See [README.md](./README.md) for template usage guide  
**Standards**: See [STANDARDS.md](../../STANDARDS.md) for documentation hierarchy

<details>
<summary><strong>Click to Expand: How to Use This Research-Driven PRD Template</strong></summary>

### Progressive Research Integration Framework

This PRD is designed to be built progressively as research becomes available. Each version of the PRD is gated by the acquisition of specific research variables.

**PRD v0.1 Sources**:
- Executive Summary ← `MARKET_SIZE_CALC` + `PRICING_BENCHMARKS`
- Target Market ← `BUYER_SEGMENTS` + `PRIMARY_TARGETS`
- Goals & Success Metrics ← `PRICING_BENCHMARKS` + market validation

**PRD v0.2 Sources**:
- Product Strategy ← `COMPETITOR_PROFILES` + `FEATURE_LANDSCAPE`
- Competitive Substitute Analysis ← `SUBSTITUTE_SHORTLIST` + `PRICING_GAPS`
- Pricing Strategy ← `UNDERCUT_PRICE` + `PRICE_ANCHOR`

**PRD v0.3 Sources**:
- Feature Requirements ← `MVP_FEATURES` + `WORKFLOW_MAP`
- User Experience ← `CORE_WORKFLOW` + `VALUE_METRICS`
- Validation Tests ← `TEST_SCENARIOS` + `PRICING_HYPOTHESIS`

**PRD v0.4 Sources**:
- Validation Test Results ← `TEST_RESULTS` + `PURCHASE_BEHAVIOR`
- Go-to-Market Strategy ← `CHANNEL_PERFORMANCE` + `GTM_PLAN`
- Pricing Strategy (refined) ← `VALIDATED_PRICE` + conversion data

**PRD v0.5 Sources**:
- All sections finalized ← Complete variable ecosystem
- Technical Requirements ← `TECHNICAL_FEASIBILITY`
- Risk Analysis ← `BUSINESS_RISKS` + `PIVOT_GATES`

### Evidence Hierarchy (Buying Behavior First)
All claims in this document must be backed by evidence, prioritized as follows:

1.  **Buying Behavior Evidence (Primary)**: Invoices, receipts, budget line items, competitor pricing pages, labor costs for workarounds.
2.  **Pain Signal Evidence (Secondary)**: Support tickets, job posts hiring for a solution, forum threads about expensive workarounds.
3.  **User Quotes (Supporting)**: Direct complaints about cost, willingness to pay statements, feature requests with budget context.

### Research Gap Management
If a section lacks evidence, create a research gap request:
```
RESEARCH GAP IDENTIFIED:
- Missing Variable: [COMPETITOR_PROFILES for pricing strategy]
- Recommended Research: [Perplexity competitive analysis prompt]
- Expected Output: [Pricing tiers and feature comparison]  
- Time Estimate: [25 minutes]
- PRD Impact: [Can't finalize pricing without substitute analysis]
```

</details>

## PRD Meta Information
| Field | Value |
|-------|-------|
| **Current Version** | v0.1 |
| **Last Updated** | [Date and Time] |
| **Last Editor** | [Agent Name] |
| **Status** | [v0.1: Research/v0.2: Strategy/v0.3: Features/v0.4: Validation/v0.5: Handoff] |
| **Next Milestone** | [Next research variable needed] |
| **Evidence Strength** | [Buying Behavior/Pain Signal/User Quotes] |
| **Command Center** | `COMMAND_CENTER.md` - Single source of truth |

## Version Change Log
| Version | Date | Editor | Key Variables Integrated |
|---------|------|--------|--------------------------|
| v0.1 | [Date] | AURA | `MARKET_SIZE_CALC`, `PRICING_BENCHMARKS`, `BUYER_SEGMENTS` |
| v0.2 | [Date] | AURA | `COMPETITOR_PROFILES`, `FEATURE_LANDSCAPE`, `PRICING_GAPS` |
| v0.3 | [Date] | AURA | `MVP_FEATURES`, `WORKFLOW_MAP`, `TEST_SCENARIOS` |
| v0.4 | [Date] | AURA | `TEST_RESULTS`, `PURCHASE_BEHAVIOR`, `VALIDATED_PRICE` |
| v0.5 | [Date] | [Agent] | `TECHNICAL_FEASIBILITY`, `BUSINESS_RISKS`, `PIVOT_GATES` |

---

## Executive Summary (v0.1+)
**Product Name**: [Name]
**Product Type**: [SaaS/Mobile App/Platform/Tool]
**Target Launch**: [Date]
**Owner**: [Product Manager Name]

### Vision Statement
[One sentence describing the long-term vision for this product]

### Mission Statement
[2-3 sentences describing what the product does and why it exists]

## Problem Statement
### Current State
[Describe the current situation users face without this product]

### Pain Points
1. **[Pain Point 1]**: [Description and impact, supported by Pain Signal or Buying Behavior evidence]
2. **[Pain Point 2]**: [Description and impact, supported by Pain Signal or Buying Behavior evidence]

### Opportunity
[Describe the market opportunity and potential impact, quantified by market size calculation]

## Research Foundation (v0.1+)
<!-- Built from MARKET_PLAYERS + BUYER_SEGMENTS variables -->

### Market Player Ecosystem
| Player | Niche | Price Range | Customer Count | Strength | Evidence Source |
|--------|-------|-------------|----------------|----------|-----------------|
| [Tool1] | Enterprise | $X-Y/mo | [Est count] | [Feature area] | [Pricing page URL] |
| [Tool2] | SMB | $X-Y/mo | [Est count] | [Feature area] | [G2 reviews] |

### Validated Buyer Segments  
**Primary Target: [Title]**
- Company Size: [Size] with $[X] [budget_line] budget
- Pain Quote: "[Direct quote from research]"
- Spend Evidence: [Job post/budget source]
- Current Cost: $[Y]/month for [substitute/manual process]

### Market Size Calculation (Bottom-Up)
- Target Accounts: [X] (methodology: [source])
- Average Current Spend: $[Y] (evidence: [pricing research])
- Total Addressable: $[Z] (calculation: X × Y)
- Our Price Point: $[A] ([B]% of current spend)

## Competitive Substitute Analysis (v0.2+)
<!-- Built from COMPETITOR_PROFILES + TARGET_SUBSTITUTE variables -->

### Primary Substitute to Undercut
**Target: [Substitute Name]**
- Current Price: $[X]/month for [broad market]
- Our Niche: [Specific segment] with [specific needs]  
- Our Price: $[Y]/month ([Z]% savings)
- Wedge Strategy: "Like [Substitute] for [Niche] at [Z]% lower cost"

### Feature Landscape Analysis
| Feature Category | Market Standard | Niche Needs | Our Strategy | Evidence |
|------------------|-----------------|-------------|--------------|----------|
| [Core Workflow] | ✅ Complex | ❗ Simplified | Copy + Simplify | [Review quote] |
| [Enterprise Features] | ✅ Over-engineered | ❌ Unnecessary | Skip | [SMB complaints] |
| [Niche-Specific] | ❌ Missing | ✅ Critical | Build Enhanced | [Job requirements] |

### Positioning Matrix
```
COPY_EXACTLY = [Core features that work universally]
SIMPLIFY_FOR_NICHE = [Enterprise features to make SMB-friendly]  
ENHANCE_FOR_NICHE = [Gaps we’ll fill specifically]
SKIP_TO_SAVE_COST = [Premium features we won’t build]
```

## Product Strategy
### Positioning
[How this product is positioned against competitors, based on the Competitive Substitute Analysis]

### Unique Value Proposition
[What makes this product unique and valuable, derived from the Positioning Matrix]

## Pricing Strategy (v0.2+ → v0.4 Validated)
<!-- Built from PRICING_GAPS + VALIDATED_PRICE variables -->

### Market-Anchored Pricing
- **Reference Price**: $[X]/month (what [target_buyer] pays [substitute])
- **Our Price**: $[Y]/month ([Z]% of reference price)
- **Psychological Anchor**: "[A]% of what you pay for [substitute_name]"
- **Value Justification**: [Specific niche benefits] + [cost savings]

### Validated Pricing Tiers
| Tier | Price | Target | Core Value | Upgrade Trigger | Test Results |
|------|-------|--------|------------|-----------------|--------------|
| Free | $0 | Trial users | [Basic workflow] | Export/share limits | N/A |
| Starter | $[X] | [Buyer segment] | [Full workflow] + [key features] | [Y]% acceptance rate |
| Pro | $[Y] | [Power users] | [Advanced features] | [Usage-based trigger] | [Z]% upgrade rate |

### Validation Evidence
- **Price Acceptance**: [A]% clicked "Start Trial" at $[X] price point
- **Feature Value**: [Core feature] ranked #[B] most important  
- **Switching Intent**: [C]% would switch from current solution
- **Budget Source**: [Reallocated/New] from [department/tool category]

## Goals & Success Metrics (v0.1+)
### Business Goals
1. **Revenue**: $[Amount] MRR within [Timeframe], based on `PRICING_BENCHMARKS`
2. **Users**: [Number] active users within [Timeframe]
3. **Market Share**: [X]% of target market

### Key Performance Indicators (KPIs)
- **Acquisition**: [Metric] new users/month
- **Activation**: [X]% complete onboarding
- **Retention**: [X]% monthly retention rate
- **Revenue**: $[X] average revenue per user
- **Referral**: [X]% users refer others

## Feature Requirements (v0.3+)
<!-- Built from MVP_FEATURES + WORKFLOW_MAP variables -->

### Current State Workflow (Evidence-Based)
| Step | Current Action | Time Cost | $ Cost | Friction Point | Evidence |
|------|----------------|-----------|--------|----------------|----------|
| 1 | [Manual process] | X min | $Y | [Pain point] | [User quote] |
| 2 | [Tool usage] | X min | $Y | [Limitation] | [Review] |
**Total Cost**: [X] hours/month × $[Y]/hour = $[Z]/month per user

### MVP Features (Revenue-Prioritized)

**Revenue Tier 1: Direct Payment Drivers**
Features users will specifically pay for:

**Feature: [Revenue Feature Name]**
- **Replaces**: Workflow steps [X, Y] saving [Z] minutes per use
- **Business Value**: $[A] monthly savings vs current process  
- **User Story**: As [validated buyer], I want [specific action] so I can [quantified benefit]
- **Acceptance Criteria**: 
  * Complete [action] in <[X] seconds
  * Achieve [Y]% accuracy vs manual process
  * Export/share results (conversion trigger)
- **Revenue Attribution**: Primary upgrade trigger from free to $[Z]/month
- **Evidence Source**: [Research variable reference]

**Revenue Tier 2: Retention Drivers**
Features that prevent churn and increase LTV

**Revenue Tier 3: Acquisition Drivers**  
Features that drive referrals and reduce CAC

### Out of Scope (Timeline Protection)
- [Complex Feature]: Deferred to v2 (reason: [complexity vs revenue impact])
- [Integration]: Wave 2 (reason: [not critical path to revenue])
- [Premium Feature]: Never (reason: [maintains price advantage])

## User Experience (v0.3+)
<!-- Built from CORE_WORKFLOW + VALUE_METRICS variables -->

### Core User Workflow
[Diagram or description of the simplified, high-value workflow our product enables, based on WORKFLOW_MAP]

### Information Architecture
[High-level structure, focused on the revenue-generating path]

### Design Principles
1. **Revenue-Focused**: Guide users to value and conversion.
2. **Fast & Simple**: Beat substitutes on ease of use.
3. **Trustworthy**: Clearly show data sources and accuracy.
4. **Accessible**: WCAG 2.1 AA compliant.

## Go-to-Market Strategy (v0.4+)
<!-- Built from CHANNEL_PERFORMANCE + GTM_PLAN variables -->

### Launch Plan
[Phased launch plan based on validated channels and target segments]

### Validated Marketing Channels
[List of channels with performance data from tests]

## Validation Test Results (v0.4+)
<!-- Built from TEST_RESULTS + PURCHASE_BEHAVIOR variables -->

### Business Validation Results
**Test 1: Pricing Resistance**
- Method: [Smoke test landing page/survey]
- Sample: [X] [target_segment] visitors  
- Results: [Y]% conversion at $[Z] price point
- Insight: [Key learning about price sensitivity]
- Decision: [Validated/Adjust] pricing strategy

**Test 2: Purchase Intent**  
- Method: [Fake door test/pre-order page]
- Sample: [A] visitors from [channel]
- Results: [B]% signed up for waitlist
- Quality: [C]% provided business email (vs personal)
- Decision: [Strong/Medium/Weak] purchase signals

**Test 3: Feature Value Validation**
- Method: [Prototype walkthrough/survey]
- Sample: [X] users familiar with [substitute]
- Results: [Y]% prefer our approach
- Time Savings: [Z]% faster than current workflow
- Decision: [Confirmed/Iterate] feature priorities

### Purchase Behavior Evidence
- **Switching Patterns**: Users switch from [substitute] after [X] weeks evaluation
- **Decision Factors**: [Cost 60%, Features 30%, Ease 10%] (ranked)
- **Budget Process**: [Self-service/Manager approval/Committee] for $[Y] tools
- **Timeline**: [Z] days average from need identification to purchase

## Technical Requirements (v0.5+)
<!-- Built from TECHNICAL_FEASIBILITY variable -->
[Technical requirements focused on delivering the MVP features and supporting the GTM strategy]

## Risk Analysis & Quality Assurance (v0.5+)
<!-- Built from BUSINESS_RISKS + PIVOT_GATES variables -->

### Quality Assurance Framework
#### Evidence Traceability
Every PRD claim must reference:
- **Source Research Variable**: [BUYER_SEGMENTS.pain_quote]
- **Original Evidence**: [Job post URL/review screenshot]
- **Research Tool Used**: [Perplexity pricing search]
- **Validation Method**: [How evidence was confirmed]

#### Revenue Impact Scoring
For every feature, include:
- **Direct Revenue**: Will users pay specifically for this? (High/Medium/Low)
- **Retention Value**: Does this prevent churn? (High/Medium/Low)
- **Acquisition Value**: Does this drive signups? (High/Medium/Low)
- **Build Effort**: Development complexity (Low/Medium/High)
- **Priority Score**: (Revenue Values / Build Effort)

### Business Risks
| Risk | Probability | Impact | Mitigation | Pivot/Kill Criterion |
|------|------------|--------|------------|----------------------|
| Low adoption | Medium | High | Refine GTM based on `CHANNEL_PERFORMANCE` | Missed conversion targets in validation tests |
| Competitor response | High | Medium | Focus on niche wedge strategy | Core value prop invalidated by competitor move |
| Pricing resistance | Medium | Medium | Adjust pricing based on `VALIDATED_PRICE` | Price acceptance below [X]% in tests |

### Development Handoff Checklist
PRD v0.5 must include:
- [ ] Every feature has business acceptance criteria
- [ ] Success metrics are measurable and tied to revenue
- [ ] Pricing strategy has market validation evidence
- [ ] Target customer has documented budget and pain
- [ ] Go-to-market plan has proven channel access
- [ ] Risk assessment includes pivot/kill criteria
- [ ] Technical requirements focus on business outcomes

## Appendix
### Research Data
- [Link to research reports and variable definitions]
- [Link to validation test results]

### Design Assets
- [Link to workflow diagrams and prototypes]

---
*PRD Version: 2.0 | Status: [Specify Status]*