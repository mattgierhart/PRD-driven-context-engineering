# RISK- Template

Copy and fill for each identified risk:

```
RISK-XXX: [Risk Title]
Scoring Category: [Market | User | Technical]
Discovery Category: [Market | Technical | Adoption | Resource | Dependency | Timing]
Description: [What could go wrong]
Trigger: [What would cause this to happen]
Impact: [High | Medium | Low]
Likelihood: [High | Medium | Low]
Raw Score: [Impact × Likelihood, 1-9]
Status: [open | mitigating | mitigated | resolved | accepted]
Effective Score: [Raw Score × Status Weight]

Early Signal: [How we'd know this is happening]
Response: [Mitigate | Accept | Avoid | Transfer]
Mitigation: [Specific action if Response = Mitigate]
Owner: [Who is responsible]

Linked IDs: [FEA-XXX, UJ-XXX, BR-XXX affected]
Review Date: [When to reassess]
Added: [PRD stage when discovered, e.g., v0.5]
```

## Scoring Categories

The 6 discovery categories map to 3 scoring categories for the README scorecard:

| Scoring Category | Discovery Categories | Question |
|---|---|---|
| **Market** | Market, Timing | Will anyone buy this? |
| **User** | Adoption, Dependency | Will users succeed with this? |
| **Technical** | Technical, Resource | Can we build and run this? |

## Raw Score Calculation

| | Low Impact (1) | Medium Impact (2) | High Impact (3) |
|---|---|---|---|
| **High Likelihood (3)** | 3 | 6 | 9 |
| **Medium Likelihood (2)** | 2 | 4 | 6 |
| **Low Likelihood (1)** | 1 | 2 | 3 |

Raw Score = Impact value × Likelihood value

## Status Lifecycle & Weights

Risks move through statuses as work progresses. Each status carries a weight that reduces the effective score:

| Status | Weight | Meaning |
|--------|--------|---------|
| `open` | 1.0 | Identified, not yet addressed |
| `accepted` | 1.0 | Conscious choice to live with it |
| `mitigating` | 0.5 | Active work underway to reduce |
| `mitigated` | 0.25 | Controls in place, residual risk remains |
| `resolved` | 0.0 | Risk eliminated |

**Effective Score** = Raw Score × Status Weight

**Transitions**: `open` → `mitigating` → `mitigated` or `resolved`. A risk can also go `open` → `accepted` at any time.

## Risk Level Thresholds

Total Risk Score = Σ all effective scores across all RISK- entries.

| Level | Score Range | Indicator | Action |
|-------|------------|-----------|--------|
| Low | 0–12 | 🟢 | Proceed normally |
| Moderate | 13–25 | 🟡 | Monitor closely |
| Elevated | 26–40 | 🟠 | Active mitigation required |
| High | 41+ | 🔴 | Consider scope/timeline changes |

## Response Decision Guide

| If... | Then Response is... |
|-------|---------------------|
| You can reduce impact or likelihood with reasonable effort | Mitigate |
| Impact is low enough to live with | Accept |
| Risk is so severe that avoiding the cause is worth scope change | Avoid |
| Someone else (vendor, partner, insurance) can own the risk | Transfer |

## Continuous Risk Management

v0.5 establishes the baseline risk register, but risk discovery is **not a one-time event**:

| Stage | Typical New Risks |
|-------|-------------------|
| v0.6 Architecture | Infrastructure complexity, integration unknowns |
| v0.7 Build | Implementation blockers, test coverage gaps |
| v0.8 Deployment | Operational risks, security findings |
| v0.9 GTM | Market timing shifts, competitive moves |
| v1.0 Growth | Real adoption data contradicting assumptions |

When adding a risk after v0.5, use the `Added:` field to record which stage surfaced it.

**Update protocol**: When any RISK- status changes, update the README Risk Scorecard.

## Checklist Before Adding

- [ ] Is this a genuine risk with evidence, not just worry?
- [ ] Is the trigger specific and observable?
- [ ] Is impact/likelihood based on evidence, not gut feeling?
- [ ] Is the mitigation specific and actionable?
- [ ] Is there an owner who will monitor this?
- [ ] Will this be reviewed before launch?
- [ ] Is the scoring category (Market/User/Technical) assigned?
