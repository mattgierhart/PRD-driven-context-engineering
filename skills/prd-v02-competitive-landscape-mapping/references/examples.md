# Competitive Landscape Examples

Good and bad examples of competitive analysis with explanations.

---

## Example 1: Digital Signage Market

### Good Analysis

```
Current Behavior (documented FIRST):
- Users manage 15 screens manually
- USB drives updated weekly (4 hrs/week)
- No centralized scheduling
- Content created in PowerPoint

Direct Competitors:
| Competitor | Pricing | Funding | Gap Signal |
|------------|---------|---------|------------|
| Yodeck | $8/screen/mo | $12M Series A | Enterprise focus |
| ScreenCloud | $20/screen/mo | $10M | Complex setup |
| Rise Vision | Free tier | Bootstrapped | Limited templates |

CFD-042: G2 reviews show "pricing jumps for 10+ screens" (Tier 1)
CFD-043: Reddit r/digitalsignage: "need something simpler" (Tier 2)

Gap Analysis:
| Segment | Served? | Gap Evidence |
|---------|---------|--------------|
| Enterprise (100+ screens) | Well served | No gap |
| SMB (5-20 screens) | Underserved | Pricing complaints |
| Single location | Ignored | No affordable options |

1% Better Hypothesis:
We can be 1% better than Yodeck by offering flat pricing
at $49/month unlimited screens for single-location businesses.

Evidence:
- CFD-042: Users cite pricing as primary complaint
- CFD-043: Simplicity valued over features

Risk: Yodeck could launch SMB tier
```

### Why It's Good
- Started with current behavior (no competitor bias)
- Multiple competitor types documented
- CFD-IDs anchor every claim
- Gap analysis uses evidence tiers
- 1% hypothesis is specific and testable
- Risk acknowledged

---

### Bad Analysis

```
Competitive Analysis:
There are some digital signage tools but none are good.
Main competitors are Yodeck and ScreenCloud.
They're too expensive and complicated.
We'll be better by having a simpler UI.
```

### Why It's Bad
- No current behavior documented
- No evidence (no CFD-IDs)
- Vague gap ("too expensive" - how much?)
- "Better UI" isn't measurable
- No segment analysis
- No risk consideration

---

## Example 2: Invoice Processing

### Good Analysis

```
Current Behavior (documented FIRST):
- AP clerk processes 200 invoices/month
- Manual data entry from PDF to QuickBooks
- 3 hours/day on invoice processing
- Error rate ~5% requiring corrections

Direct Competitors:
| Competitor | Pricing | Target | Gap Signal |
|------------|---------|--------|------------|
| Bill.com | $45/user/mo | SMB | Feature bloat complaints |
| Tipalti | Enterprise pricing | Mid-market+ | Overkill for SMB |
| Stampli | $POA | AP teams | Requires AP team |

Adjacent Solutions:
- QuickBooks (has basic invoice capture)
- Expensify (expense-focused, not AP)
- Generic OCR tools (no workflow)

Workarounds Documented:
CFD-051: Reddit shows users combining Zapier + Google Sheets
CFD-052: Upwork: "$25/hr for invoice data entry" (validates spend)

Gap Analysis:
| Segment | Pain Level | Current Solution |
|---------|------------|------------------|
| 1-person accounting | High | Manual + spreadsheet |
| Small AP team (2-3) | Medium | Bill.com reluctantly |
| Large AP team (10+) | Low | Tipalti/Coupa |

Feature Matrix:
| Feature | Bill.com | Us (Planned) | Gap |
|---------|:--------:|:------------:|-----|
| OCR capture | ✅ | ✅ | Parity |
| QuickBooks sync | ✅ | ✅ | Parity |
| Approval workflow | ✅ | ❌ | Not needed for segment |
| Mobile capture | ❌ | ✅ | Our advantage |
| Flat pricing | ❌ | ✅ | Our advantage |

1% Better Hypothesis:
We can be 1% better than Bill.com by removing approval
workflows and offering mobile-first capture at flat $29/mo
for solo accountants processing <500 invoices/month.

Evidence:
- CFD-051: Users want simpler (no approval chains)
- CFD-052: $25/hr manual = $200+/mo budget exists
- G2 reviews: "too many features we don't use"

Risk: Bill.com launches "lite" tier
```

### Why It's Good
- Quantified current behavior (200/mo, 3 hrs/day, 5% errors)
- Three competitor types (direct, adjacent, workarounds)
- Workarounds validate willingness to pay
- Feature matrix shows intentional feature removal
- 1% hypothesis targets specific segment
- Evidence cited for every claim

---

## Example 3: False "No Competitors" Claim

### Bad Analysis

```
Competitive Landscape:
After extensive research, we found no direct competitors.
The market is wide open for our AI-powered solution.
We're creating a new category.
```

### Why It's Bad
- "No competitors" almost always wrong
- Didn't check workarounds
- Didn't check adjacent solutions
- "New category" = red flag (education cost)
- No evidence for "extensive research"

### Fixed Analysis

```
Competitive Landscape:
Direct competitors: None with exact approach (verified)

Adjacent solutions:
| Solution | How Users Adapt It |
|----------|-------------------|
| Spreadsheets | Manual tracking (CFD-061) |
| Generic tools | Workaround workflows (CFD-062) |
| Consultants | $150/hr manual service (CFD-063) |

Workarounds:
- CFD-061: 3 Reddit threads showing spreadsheet solutions
- CFD-062: Notion template with 5K downloads
- CFD-063: Upwork gigs averaging $2K/project

"Do Nothing" Cost:
- 10 hrs/week manual work = $500/week (CFD-064)

Classification:
INNOVATION type (no direct competitors) with high risk.
Workarounds validate pain but education cost will be high.
Consider if workaround (spreadsheet) can be productized
first (CLONE the workaround).

1% Better Hypothesis:
We can be 1% better than the spreadsheet workaround by
automating the [specific task] that takes 10 hrs/week.

Risk: Users may prefer free spreadsheet over paid tool
Mitigation: Offer free tier, prove 10x time savings
```

### Why Fixed Version Works
- Admits no direct competitors but shows alternatives
- Documents workarounds with evidence
- Quantifies "do nothing" cost
- Acknowledges innovation risk
- Suggests CLONE fallback strategy
- 1% hypothesis competes with workaround

---

## Anti-Pattern Summary

| Anti-Pattern | Example | Fix |
|--------------|---------|-----|
| Competitor-first | Started by listing tools | Document current behavior first |
| Vague gaps | "They're expensive" | "$45/mo vs our $29/mo" |
| No workarounds | Only listed software | Include spreadsheets, manual, consultants |
| False uniqueness | "No competitors" | Check adjacent + workarounds |
| Feature wars | "We have more features" | Focus on 1% that matters |
| No evidence | "Users want simpler" | Add CFD-ID with quote |
| 10x claims | "10x better" | Start with 1% provable |
