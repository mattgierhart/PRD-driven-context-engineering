# GTM Constraints Matrix by Product Type

Each product type carries inherited constraints that flow into v0.3 and beyond. These are not suggestions—they are guardrails.

## Constraints Summary Table

| Type | Pricing Constraint | Channel Constraint | Scope Constraint | Timeline |
|------|-------------------|-------------------|------------------|----------|
| Clone | Match or beat leader | Same channels as leader | Feature parity on core | 14-21 days |
| Unbundle | Premium for vertical depth | Own the vertical channel | 10x better than platform | 21-30 days |
| Undercut | 50-70% below leader | Direct to niche | Ruthless feature cuts | 7-14 days |
| Slice | Follow platform norms | Platform marketplace | Platform integration first | 14-21 days |
| Wrapper | Value-based (time saved) | Integration partners | API stability critical | 14-21 days |
| Innovation | Value-based (pain severity) | Education-heavy | MVP to prove concept | 30-60 days |

---

## Detailed Constraints by Type

### CLONE Constraints

**Pricing**:
- Must match or slightly undercut leader
- Cannot charge premium without clear differentiation
- Anchor: Leader's price ± 20%

**Channel**:
- Go where leader's customers already are
- If leader uses SEO, you need SEO
- If leader uses sales, you need sales (or find different segment)

**Scope**:
- Core workflow must match leader
- Table-stakes features are mandatory
- Differentiation through execution, not features

**Timeline**:
- 14-21 days to MVP
- Speed is competitive advantage
- Leader will respond—ship fast

**v0.3 Implications**:
- Success metric: Feature parity + [differentiator]
- Pricing model: Same as leader (subscription/usage/seat)
- MVP scope: Core workflow + 1-2 enhancements

---

### UNBUNDLE Constraints

**Pricing**:
- Can charge premium vs. platform's bundled price
- Value = vertical depth + specialized features
- Anchor: What would user pay for JUST this category?

**Channel**:
- Must own distribution to vertical
- Platform's users won't find you organically
- Build audience in the vertical (content, community, partnerships)

**Scope**:
- Must be 10x better than platform's version
- Depth > breadth
- Features platform will NEVER build

**Timeline**:
- 21-30 days to MVP
- More scope than Undercut (need to be clearly better)
- Platform won't respond quickly (not their priority)

**v0.3 Implications**:
- Success metric: Category NPS vs. platform
- Pricing model: Often higher than platform's implicit allocation
- MVP scope: Core vertical workflow with 3-5 differentiating features

---

### UNDERCUT Constraints

**Pricing**:
- MUST be 50-70% below leader
- Price is the headline, not the footnote
- Sustainable margin required (can't lose money)

**Channel**:
- Direct to niche (leader ignores them)
- Price-sensitive buyers respond to clear savings
- Self-serve preferred (low CAC required for low price)

**Scope**:
- Ruthlessly cut features niche doesn't need
- 80% of value at 30% of features
- Simplicity is a feature

**Timeline**:
- 7-14 days to MVP (simplest type)
- Speed matters—others see the gap too
- Validate price sensitivity before building

**v0.3 Implications**:
- Success metric: Price per [unit] vs. leader
- Pricing model: Simpler than leader (flat rate > per-seat)
- MVP scope: Core workflow ONLY, no nice-to-haves

---

### SLICE Constraints

**Pricing**:
- Follow platform marketplace norms
- Often freemium with paid tiers
- Factor in platform's revenue share (15-30%)

**Channel**:
- Platform marketplace is primary channel
- Optimize for marketplace discovery (keywords, reviews)
- Secondary: Direct to platform's power users

**Scope**:
- Integration quality is #1 priority
- Must work seamlessly with platform
- Features extend platform, don't replace it

**Timeline**:
- 14-21 days to MVP
- Platform approval process may add time
- API changes can break you—build resilient

**v0.3 Implications**:
- Success metric: Marketplace ranking, install rate
- Pricing model: Match marketplace category norms
- MVP scope: Single integration done exceptionally well

---

### WRAPPER Constraints

**Pricing**:
- Value-based: Time saved × hourly rate
- Or: Errors prevented × cost of error
- Must be < cost of building integration themselves

**Channel**:
- Integration partners (tool vendors want connectors)
- Technical communities (developers, ops teams)
- Content marketing (tutorials, documentation)

**Scope**:
- API stability is critical (you depend on others)
- Must handle edge cases gracefully
- Error handling > feature count

**Timeline**:
- 14-21 days to MVP
- Depends on API complexity
- Build for API versioning from day 1

**v0.3 Implications**:
- Success metric: Data accuracy, sync reliability
- Pricing model: Usage-based (API calls, records synced)
- MVP scope: One integration pair, bulletproof reliability

---

### INNOVATION Constraints

**Pricing**:
- Value-based on pain severity
- No anchor exists—you set the market
- Early adopters pay for novelty

**Channel**:
- Education-heavy (content, webinars, demos)
- Early adopters, not mainstream
- Community building required

**Scope**:
- Minimum to prove concept works
- Expect pivots—don't over-build
- Focus on learning, not features

**Timeline**:
- 30-60 days to MVP (longest)
- Validation checkpoints required
- Kill fast if signals negative

**v0.3 Implications**:
- Success metric: Adoption rate, retention
- Pricing model: Start high (early adopters), adjust later
- MVP scope: Core innovation only, manual everything else

---

## Constraint Inheritance Rules

When creating BR entries for v0.3, reference these constraints:

```markdown
BR-XXX: GTM Constraints (from Product Type: [TYPE])

Pricing Constraint: [Copy from above]
- Anchor: [Specific competitor/market reference]
- Range: [$X - $Y]
- Model: [Subscription/Usage/Seat/Flat]

Channel Constraint: [Copy from above]
- Primary: [Specific channel]
- Secondary: [Specific channel]
- Avoid: [Channels that don't fit type]

Scope Constraint: [Copy from above]
- Must Have: [Features required by type]
- Must NOT Have: [Features that violate type]
- Differentiator: [What makes this type work]

Timeline Constraint: [Copy from above]
- MVP Target: [X days]
- Validation Gate: [What must be true before v0.4]
```

## Type-Specific Metrics (for v0.3 Outcome Definition)

| Type | Primary Metric | Secondary Metric | Avoid Measuring |
|------|---------------|------------------|-----------------|
| Clone | Feature completion % | User satisfaction vs. leader | Price (you're matching) |
| Unbundle | Vertical NPS | Depth of usage | Breadth of features |
| Undercut | Price delta vs. leader | CAC (must be low) | Feature count |
| Slice | Marketplace rank | Install-to-active rate | Standalone usage |
| Wrapper | Sync accuracy % | Time saved per user | Feature count |
| Innovation | Adoption rate | Retention (do they stay?) | Revenue (too early) |
