# Feature Matrix Template

Quick-copy templates for competitive feature comparison.

---

## Standard Feature Matrix

```markdown
| Feature | Us | [Comp A] | [Comp B] | [Comp C] | Notes |
|---------|:--:|:--------:|:--------:|:--------:|-------|
| [Feature 1] | 🔄 | ✅ | ✅ | ✅ | |
| [Feature 2] | 🔄 | ✅ | ❌ | ✅ | |
| [Feature 3] | ✅ | ❌ | ❌ | ❌ | Our advantage |
| [Feature 4] | ❌ | ✅ | ✅ | ✅ | Not for MVP |

**Legend:** ✅ Has | ❌ Missing | 🔄 Planned | ⚠️ Partial
```

---

## Detailed Feature Matrix (With Tiers)

```markdown
| Feature | Us | Tier | [Comp A] | Tier | [Comp B] | Tier |
|---------|:--:|:----:|:--------:|:----:|:--------:|:----:|
| [Feature 1] | ✅ | Free | ✅ | $20 | ✅ | $50 |
| [Feature 2] | ✅ | Pro | ❌ | — | ✅ | Free |
| [Feature 3] | ✅ | Free | ✅ | $50 | ❌ | — |

**Our Advantage:** [Feature X] free vs competitor's $50 tier
```

---

## Pricing Matrix

```markdown
| | Free | Starter | Pro | Enterprise |
|--|:----:|:-------:|:---:|:----------:|
| **Us (Planned)** | $0 | $X | $Y | $Z |
| [Comp A] | ❌ | $X | $Y | Custom |
| [Comp B] | $0 | $X | $Y | Custom |
| [Comp C] | ❌ | $X | $Y | $Z |

**Key Differences:**
- We offer [X] in Free tier (competitors charge $Y)
- Our Pro at $X vs competitor average $Y
```

---

## Integration Matrix

```markdown
| Integration | Us | [Comp A] | [Comp B] | Priority |
|-------------|:--:|:--------:|:--------:|:--------:|
| [Platform 1] | 🔄 | ✅ | ✅ | P0 |
| [Platform 2] | 🔄 | ✅ | ❌ | P1 |
| [Platform 3] | ❌ | ❌ | ❌ | P2 |
| [Platform 4] | ✅ | ❌ | ❌ | Differentiator |
```

---

## Support/Service Matrix

```markdown
| Support Type | Us | [Comp A] | [Comp B] |
|--------------|:--:|:--------:|:--------:|
| Email support | ✅ | ✅ | ✅ |
| Chat support | ✅ | ❌ | ✅ |
| Phone support | ❌ | ✅ | ❌ |
| Response SLA | 24hr | 48hr | 24hr |
| Onboarding | Self | $500 | Self |
```

---

## Mobile/Platform Matrix

```markdown
| Platform | Us | [Comp A] | [Comp B] |
|----------|:--:|:--------:|:--------:|
| Web app | ✅ | ✅ | ✅ |
| iOS app | 🔄 | ✅ | ❌ |
| Android app | 🔄 | ✅ | ❌ |
| Desktop (Mac) | ❌ | ✅ | ✅ |
| Desktop (Win) | ❌ | ✅ | ❌ |
| API | ✅ | ✅ | ⚠️ |
```

---

## Gap Summary Template

After completing matrix, summarize:

```markdown
## Feature Gap Summary

**Table Stakes (must match):**
- [Feature 1] — all competitors have, we need
- [Feature 2] — all competitors have, we need

**Our Advantages:**
- [Feature 3] — we have, competitors don't
- [Feature 4] — we do better because [reason]

**Intentional Gaps:**
- [Feature 5] — competitors have, we won't build
  - Reason: [Why not needed for our segment]

**Future Consideration:**
- [Feature 6] — nice to have, post-MVP
```

---

## Comparison Screenshot Log

Track competitor screenshots for reference:

```markdown
| Competitor | Page | Screenshot | Date | Notes |
|------------|------|------------|------|-------|
| [Comp A] | Pricing | /screenshots/comp-a-pricing.png | YYYY-MM-DD | |
| [Comp A] | Features | /screenshots/comp-a-features.png | YYYY-MM-DD | |
| [Comp B] | Pricing | /screenshots/comp-b-pricing.png | YYYY-MM-DD | |
```

---

## Usage Tips

1. **Start with table stakes** — what everyone has
2. **Identify 1-3 differentiators** — where we win
3. **Note pricing tiers** — features behind paywalls
4. **Track intentional gaps** — what we won't build
5. **Update quarterly** — competitors change
