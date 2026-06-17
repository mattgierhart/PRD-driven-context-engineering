# Technology Evaluation Scorecard

Use this when comparing Buy/Integrate options.

## Scorecard Template

| Criterion | Weight | Option A | Option B | Option C |
|-----------|--------|----------|----------|----------|
| **Fit** (solves our need) | 25% | /5 | /5 | /5 |
| **Cost** (at scale) | 20% | /5 | /5 | /5 |
| **Complexity** (integration effort) | 20% | /5 | /5 | /5 |
| **Lock-in** (switching cost) | 15% | /5 | /5 | /5 |
| **Maturity** (production-ready) | 10% | /5 | /5 | /5 |
| **Support** (help available) | 10% | /5 | /5 | /5 |
| **Weighted Total** | 100% | | | |

## Scoring Guide

### Fit (25%)
- 5: Solves need perfectly, no gaps
- 4: Solves most needs, minor workarounds
- 3: Adequate, some limitations
- 2: Significant gaps
- 1: Poor fit

### Cost (20%)
- 5: Free or negligible at scale
- 4: Reasonable, predictable pricing
- 3: Moderate cost
- 2: Expensive but justifiable
- 1: Prohibitively expensive at scale

### Complexity (20%)
- 5: Drop-in integration, <1 day
- 4: Straightforward, 1-3 days
- 3: Moderate effort, 1 week
- 2: Significant work, 2+ weeks
- 1: Major undertaking

### Lock-in (15%)
- 5: Data portable, easy to switch
- 4: Some effort to migrate
- 3: Moderate switching cost
- 2: Significant migration work
- 1: Effectively locked in

### Maturity (10%)
- 5: Battle-tested, excellent docs
- 4: Production-ready, good docs
- 3: Stable, adequate docs
- 2: Some rough edges
- 1: Immature, poor docs

### Support (10%)
- 5: Excellent support + community
- 4: Good support options
- 3: Adequate support
- 2: Limited support
- 1: No support

## Example Completed Scorecard

**Evaluating: Authentication Service**

| Criterion | Weight | Clerk | Auth0 | Firebase Auth |
|-----------|--------|-------|-------|---------------|
| **Fit** | 25% | 5 | 5 | 4 |
| **Cost** | 20% | 4 | 3 | 5 |
| **Complexity** | 20% | 5 | 3 | 4 |
| **Lock-in** | 15% | 3 | 3 | 2 |
| **Maturity** | 10% | 4 | 5 | 5 |
| **Support** | 10% | 4 | 5 | 3 |
| **Weighted Total** | 100% | **4.3** | **3.8** | **3.8** |

**Decision**: Clerk — Best developer experience, good fit, reasonable cost.
