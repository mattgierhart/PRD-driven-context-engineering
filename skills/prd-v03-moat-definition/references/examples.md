# Market Moat Analysis Examples

## Good Examples

### Example 1: Salesforce CRM Moat Analysis (SMB Targeting)

**Context**: Evaluating Salesforce for SMB warranty management product (HomeFalcon).

**Analysis**:
```
CFD-MOT-001: Salesforce CRM Moat Analysis
Competitor: Salesforce
Moat Type: Switching Costs (primary), Data/IP (secondary)
Moat Strength: Strong

Evidence:
- Multi-year contracts with early termination fees
- Average customer has 3+ years of CRM data
- Deep integrations with 100+ apps (AppExchange ecosystem)
- Custom objects/workflows create workflow lock-in

Switching Costs Inventory:
- Financial: $0-50K (depends on contract) — Strong
- Time/Effort: 80-200 hours migration — Strong
- Data Migration: Exportable to CSV, but relationships complex — Moderate
- Workflow Retraining: Significant (unique Salesforce methodology) — Strong
- Integration Rework: Major (API dependencies everywhere) — Strong

Vulnerability: SMB segment (under 10 employees)
- Most SMBs don't use custom objects, integrations, or multi-year contracts
- Switching cost for basic CRM: <10 hours
- Price sensitivity high: $75/user/mo feels excessive

Targeting Implication: DON'T compete for mid-market CRM. DO target SMBs
who only need warranty tracking (subset of CRM), position as specialized tool
not replacement.

Confidence: High — validated via customer interviews + pricing page analysis
```

**Why this works**:
- Specific moat type identified with evidence
- Quantified switching costs (hours, dollars)
- Found the segment where moat doesn't apply
- Clear targeting decision with rationale

---

### Example 2: Notion Eroding Moat Analysis

**Context**: Evaluating Notion for documentation/wiki product.

**Analysis**:
```
CFD-MOT-002: Notion Moat Analysis
Competitor: Notion
Moat Type: Network Effects (primary), Switching Costs (secondary)
Moat Strength: Moderate → Eroding

Evidence:
- Network effect: Collaboration value increases with team adoption
- BUT: Single-player use cases don't benefit from network effect
- Switching costs: Markdown export available, data portable
- Growing complaints: "Too slow", "Feature bloat"

Switching Costs Inventory:
- Financial: $0 (monthly billing) — Weak
- Time/Effort: 10-20 hours for team wiki — Moderate
- Data Migration: Full Markdown export available — Weak
- Workflow Retraining: Low (familiar UX patterns) — Weak
- Integration Rework: Limited API dependencies — Weak

Erosion Signals:
- 40+ new competitors in 2023-2024
- Reddit threads: "Notion alternatives" trending
- Feature bloat complaints increasing
- Performance issues driving users to simpler tools

Vulnerability: Speed-focused users, simple use cases
Targeting Implication: WEDGE on speed + simplicity. Enter via single-player
use case (personal wiki) where network effect doesn't apply.

Confidence: Medium — based on review analysis + competitor landscape
```

**Why this works**:
- Identified eroding moat with specific signals
- Network effect analyzed correctly (doesn't apply to all segments)
- Found wedge opportunity with clear entry point

---

### Example 3: Spreadsheet Competitor (Workaround Analysis)

**Context**: Evaluating "doing it manually in Excel" for inventory tracking.

**Analysis**:
```
CFD-MOT-003: Spreadsheet Workaround Moat Analysis
Competitor: Manual Excel/Google Sheets tracking
Moat Type: Inertia + Brand/Trust (familiarity)
Moat Strength: Weak but persistent

Evidence:
- No financial lock-in — Weak
- Low switching friction technically — Weak
- BUT: Behavioral inertia extremely high
- "We've always done it this way" — Moderate (habit moat)

Switching Costs Inventory:
- Financial: $0 (spreadsheets are free) — None
- Time/Effort: 2-4 hours to learn new tool — Weak
- Data Migration: CSV import easy — None
- Workflow Retraining: Must change habit — Moderate
- Integration Rework: None — None

The Real Moat: Behavioral inertia
- Risk aversion: "What if the new thing breaks?"
- Learning curve avoidance: "I know Excel"
- Budget justification: "Hard to explain spending on software"

Vulnerability: Pain threshold
When manual tracking FAILS (lost item, missed warranty, compliance audit),
users become ready to switch.

Targeting Implication: DIRECT COMPETITION. Focus on pain moments
(missed warranty claim, lost item recovery). Make first value <5 minutes
to overcome inertia.

Confidence: High — this is the primary competitor for most SMB tools
```

**Why this works**:
- Analyzed workaround competitor (Type 4) often ignored
- Identified behavioral moat (inertia) not just technical
- Found trigger moments that overcome weak moat

---

## Bad Examples

### Bad Example 1: Vague Assessment

**Wrong**:
```
CFD-MOT-XXX: Competitor X Analysis
They're a big player with lots of customers and brand recognition.
Moat: Strong
Targeting: We should probably avoid them.
```

**Why it fails**:
- No specific moat type identified
- "Big" and "lots of customers" aren't moat evidence
- No switching cost quantification
- No segment analysis (where IS their moat weak?)

**Fix**: Specify moat type, quantify switching costs, find vulnerable segment.

---

### Bad Example 2: Underestimated Integration Moat

**Wrong**:
```
CFD-MOT-XXX: Slack Moat Analysis
Moat Type: Network Effects
Moat Strength: Moderate — people can switch to Teams

Switching Costs Inventory:
- Data Migration: Can export history — Weak
- Workflow Retraining: Similar UX to Teams — Weak

Targeting: Direct competition viable
```

**Reality check** (what actually happened):
- Ignored integration moat (500+ Slack apps, custom bots)
- Underestimated workflow lock-in (team habits, channel structure)
- Companies that tried switching spent 6+ months, many reverted

**Why it fails**:
- Network effects analysis incomplete (ignored two-sided marketplace for apps)
- Integration moat completely missed
- No validation from actual switching attempts

**Fix**: Include integration inventory, validate switching cost with real cases.

---

### Bad Example 3: Assumed Moat Without Validation

**Wrong**:
```
CFD-MOT-XXX: [Startup] Moat Analysis
Moat Type: Data/IP — they have AI
Moat Strength: Strong — AI is hard to replicate
Targeting: Avoid
```

**Why it fails**:
- "They have AI" isn't a data moat
- No analysis of what data they have or if it's proprietary
- No assessment of whether AI actually provides advantage
- Assumed strength without evidence

**Fix**: 
- What specific data do they have?
- Is it proprietary or could we get similar data?
- Does the AI actually work better than alternatives?
- Validate with user reviews, not assumptions

---

## Pattern: Common Failure Modes

| Failure Mode | Symptom | Prevention |
|--------------|---------|------------|
| **Assumed moat** | "They're big, must be defensible" | Require evidence per moat claim |
| **Underestimated integration** | Only counted feature parity | Map actual API dependencies |
| **Ignored behavioral moat** | Focused on technical switching | Include habit/inertia analysis |
| **Overestimated opportunity** | "Their moat is weak everywhere" | Find WHERE specifically |
| **Missed eroding signals** | Analyzed current state only | Track complaints, new entrants |

---

## Evidence Quality Guide

When assessing moats, rate your evidence:

| Quality | Source | Confidence |
|---------|--------|------------|
| **Tier 1** | Customer interviews who switched, actual migration attempts | 90%+ |
| **Tier 2** | Reviews mentioning switching experience, competitor case studies | 70-80% |
| **Tier 3** | Pricing page analysis, feature comparison | 50-65% |
| **Tier 4** | Assumption based on category norms | 30-45% |
| **Tier 5** | Speculation | <20% — BLOCK |

**Rule**: Don't make targeting decisions on Tier 4-5 moat analysis.
