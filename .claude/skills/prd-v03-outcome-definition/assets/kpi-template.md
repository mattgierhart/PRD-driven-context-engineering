# KPI Definition Worksheet

**Product**: [Product Name]
**Product Type**: [Clone | Unbundle | Undercut | Slice | Wrapper | Innovation]
**PRD Version**: v0.3
**Date**: YYYY-MM-DD

---

## Pre-Flight Check

Before defining KPIs, confirm:

- [ ] Product Type Classification complete (BR-XXX exists)
- [ ] Competitive landscape mapped (CFD-XXX with competitor metrics)
- [ ] Pricing model hypothesis exists
- [ ] User value articulation complete (what outcome users get)

---

## KPI Definition Template

### KPI-001: [Primary Revenue Metric]

**Tier**: 1 (Required)
**Category**: Lagging

| Field | Value |
|-------|-------|
| **Name** | [e.g., Monthly Recurring Revenue] |
| **Definition** | [Exact calculation: sum of active subscription values] |
| **Target** | [Specific number with timeframe: $5K MRR by Day 60] |
| **Evidence** | [CFD-XXX or benchmark source] |
| **Downstream Gate** | [Which decision uses this threshold] |
| **Measurement** | [Tool + frequency: Stripe dashboard, weekly] |

---

### KPI-002: [Primary Conversion Metric]

**Tier**: 2
**Category**: Leading

| Field | Value |
|-------|-------|
| **Name** | [e.g., Trial-to-Paid Conversion Rate] |
| **Definition** | [Exact calculation: paid / started trial × 100] |
| **Target** | [Specific %: >25% based on 14-day trial benchmark] |
| **Evidence** | [CFD-XXX or benchmark source] |
| **Downstream Gate** | [e.g., Beta success criteria] |
| **Measurement** | [Tool + frequency] |

---

### KPI-003: [Customer Success Metric]

**Tier**: 1 or 2
**Category**: Leading

| Field | Value |
|-------|-------|
| **Name** | [e.g., Time to First Value] |
| **Definition** | [Exact calculation: minutes from signup to first [value event]] |
| **Target** | [Specific threshold: <5 minutes for self-serve] |
| **Evidence** | [CFD-XXX or benchmark source] |
| **Downstream Gate** | [e.g., UX iteration trigger] |
| **Measurement** | [Tool + frequency] |

---

### KPI-004: [Retention/Churn Metric]

**Tier**: 1
**Category**: Lagging

| Field | Value |
|-------|-------|
| **Name** | [e.g., Monthly Logo Churn] |
| **Definition** | [Exact calculation: cancelled / start of month × 100] |
| **Target** | [Specific %: <5% monthly for SMB SaaS] |
| **Evidence** | [Benchmark: ChartMogul SMB SaaS 3-5%] |
| **Downstream Gate** | [e.g., Gate 4 Unit Economics] |
| **Measurement** | [Tool + frequency] |

---

### KPI-005: [Unit Economics Metric]

**Tier**: 1
**Category**: Lagging

| Field | Value |
|-------|-------|
| **Name** | [e.g., LTV:CAC Ratio] |
| **Definition** | [Exact calculation: (ARPA × Gross Margin / Churn) / CAC] |
| **Target** | [Specific ratio: ≥3:1] |
| **Evidence** | [Standard SaaS benchmark] |
| **Downstream Gate** | [e.g., Scaling decision gate] |
| **Measurement** | [Tool + frequency: Monthly calculation] |

---

## Product Type Validation

For **[Product Type from BR-XXX]**, verify metric alignment:

| Required Check | Status |
|----------------|--------|
| Primary metrics match product type table | [ ] |
| Anti-metrics NOT included | [ ] |
| At least 1 Tier 1 metric defined | [ ] |
| Leading + Lagging pair exists | [ ] |
| All targets have evidence source | [ ] |
| All KPIs have downstream gate linkage | [ ] |

---

## KPI Summary Table

| ID | Name | Tier | Category | Target | Gate |
|----|------|------|----------|--------|------|
| KPI-001 | | 1 | Lagging | | |
| KPI-002 | | 2 | Leading | | |
| KPI-003 | | 1/2 | Leading | | |
| KPI-004 | | 1 | Lagging | | |
| KPI-005 | | 1 | Lagging | | |

---

## Decision Gates Using These KPIs

| Gate | KPI(s) | Threshold | Action if Failed |
|------|--------|-----------|------------------|
| v0.5 Red Team | KPI-001 | | Pivot evaluation |
| Beta Success | KPI-002, KPI-003 | | Product iteration |
| Unit Economics | KPI-004, KPI-005 | | No scaling |
| Launch Go/No-Go | All | | Delay launch |

---

## Next Steps

After completing this worksheet:

1. [ ] Transfer KPI- entries to `KPI_REGISTRY.md` (SoT file)
2. [ ] Update PRD v0.3 with KPI references
3. [ ] Create BR- entries for any derived business rules (e.g., "BR-XXX: No launch if LTV:CAC <3:1")
4. [ ] Proceed to Pricing Model Selection skill
