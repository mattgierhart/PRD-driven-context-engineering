# KPI Benchmark Sources

> **Teaching reference:** Verify every external benchmark at the time of use. The illustrative
> internal-policy section below is synthetic and is not a framework standard or empirical result.

## SaaS Revenue Metrics

### Churn Rates
| Segment | Good | Acceptable | Concerning | Source |
|---------|------|------------|------------|--------|
| SMB Monthly | <5% | 5-7% | >7% | ChartMogul SaaS Benchmarks 2023 |
| SMB Annual | <5% | 5-10% | >10% | SaaStr benchmarks |
| Enterprise Annual | <3% | 3-5% | >5% | OpenView SaaS Metrics |

### LTV:CAC Ratio
| Stage | Minimum | Healthy | Excellent |
|-------|---------|---------|-----------|
| Early (pre-PMF) | 1:1 | 2:1 | 3:1 |
| Growth | 3:1 | 4:1 | 5:1+ |
| Mature | 3:1 | 5:1 | 7:1+ |

**Rule**: Below 3:1 at scale = unsustainable unit economics

### CAC Payback Period
| Model | Good | Acceptable | Concerning |
|-------|------|------------|------------|
| Self-serve | <3 months | 3-6 months | >6 months |
| Sales-assisted | <12 months | 12-18 months | >18 months |
| Enterprise | <18 months | 18-24 months | >24 months |

---

## Conversion Metrics

### Trial-to-Paid Conversion
| Model | Low | Average | High |
|-------|-----|---------|------|
| Freemium | 2-3% | 4-5% | >7% |
| Free trial (14-day) | 15% | 25% | >40% |
| Free trial (30-day) | 10% | 20% | >30% |
| Reverse trial | 20% | 35% | >50% |

### Time to Value (TTFV)
| Product Type | Target | Source |
|--------------|--------|--------|
| Self-serve SaaS | <5 minutes | ProductLed benchmarks |
| PLG tools | <10 minutes | OpenView PLG Index |
| B2B with onboarding | <1 day | Industry standard |
| Enterprise | <1 week | Enterprise SaaS norms |

---

## Product-Type Specific Benchmarks

### Clone/Undercut Products
| Metric | Target | Rationale |
|--------|--------|-----------|
| Feature parity | 80%+ of leader's core features | Less = not credible alternative |
| Price delta | 50-70% below leader | Less = not compelling switch |
| TTFV vs. leader | Equal or faster | Slower = lose on experience |

### Slice Products (Marketplace)
| Metric | Good | Excellent | Source |
|--------|------|-----------|--------|
| App store rating | 4.0+ | 4.5+ | Platform norms |
| Install→activate | 30%+ | 50%+ | Shopify app benchmarks |
| 30-day retention | 40%+ | 60%+ | Platform ecosystem data |

### Innovation Products
| Metric | Early Stage | Growth Stage |
|--------|-------------|--------------|
| Education→trial | 5-10% | 15-25% |
| Trial→activation | 20-30% | 40-50% |
| Reference customers | 3-5 | 10-20 |
| Time to behavioral change | Track, no benchmark | Depends on behavior |

---

## Illustrative Internal Policies (Synthetic)

### Revenue Velocity
| Milestone | Target | Gate |
|-----------|--------|------|
| Market signal → first dollar | {owner-defined} | v0.5 Red Team |
| First dollar → initial recurring-revenue target | {owner-defined} | Scaling decision |
| Initial → growth recurring-revenue target | {owner-defined} | Investment decision |

### Infrastructure Constraints
| Metric | Constraint | Source |
|--------|------------|--------|
| Cost per user | {product-specific limit} | BR-001 synthetic policy example |
| Test coverage | {product-specific threshold} | BR-002 synthetic quality example |
| Bundle size (JS) | {product-specific budget} | BR-003 synthetic performance example |

### Development Timeline
| Product Type | MVP Target | Evidence |
|--------------|------------|----------|
| Undercut | {owner-defined} | Validate scope and economics |
| Clone | {owner-defined} | Validate required parity |
| Slice | {owner-defined} | Validate platform integration |
| Wrapper | {owner-defined} | Validate API dependencies |
| Unbundle | {owner-defined} | Validate vertical depth |
| Innovation | {owner-defined} | Validate education and behavior change |

---

## Benchmark Sources (for citation)

| Source | URL | Best For |
|--------|-----|----------|
| ChartMogul SaaS Benchmarks | chartmogul.com/reports | Churn, MRR growth |
| OpenView SaaS Metrics | openviewpartners.com | PLG, expansion revenue |
| SaaStr | saastr.com | Pricing, sales metrics |
| ProductLed | productled.com | Activation, TTFV |
| Lenny's Newsletter | lennysnewsletter.com | Consumer benchmarks |
| First Round Review | review.firstround.com | Startup metrics |

**Usage**: When setting targets, cite benchmark source in KPI- entry Evidence field.
