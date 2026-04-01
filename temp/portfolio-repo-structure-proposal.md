# Portfolio Repo Structure — Proposal for Feedback

> **Status**: Draft for review — not an implementation spec.
> **Next step**: Validate against a real IBM portfolio (their repos, their teams, their products).
> **Audience**: Everyone on the team — leadership, designers, backend engineers, data scientists, scrum masters.

---

## What Is This?

A proposal for how to structure a **portfolio-level repository** that sits above multiple product repos. The portfolio repo does NOT contain product code. It contains strategy, intelligence, and standards that help the team:

1. **See into the future** — find the next products by reading signals across existing ones.
2. **Design connected products** — ensure new products are born into the ecosystem, not bolted on later.
3. **Keep documentation consistent** — so any team member or AI agent can move between products without re-learning the structure.

This builds on the PRD-driven context engineering methodology that each product repo already uses. The portfolio is a layer above — it coordinates, it doesn't control.

---

## Who Needs to Understand This

This system only works if everyone on the team understands it. Not just the methodology — their role in it.

| Role | What They Need to Know | How They Interact with the Portfolio |
|------|----------------------|-------------------------------------|
| **Leadership** | Portfolio strategy, pipeline prioritization, ecosystem vision | Owns PORTFOLIO.md, reviews signal registry, makes go/no-go on candidates |
| **Scrum Masters** | How product work connects back to portfolio, freshness rituals | Updates product manifests, maintains Jira cross-references, flags stale docs |
| **Designers** | Shared design standards, cross-product UX consistency | Consumes P:DES- standards, contributes screen flows that respect ecosystem contracts |
| **Backend Engineers** | Ecosystem API contracts, shared infrastructure rules | Implements P:API- contracts, honors P:BR- cross-product rules in their product code |
| **Data Scientists** | Signal registry, demand patterns, gap analysis | Contributes to intelligence layer, analyzes cross-product usage data for signal discovery |
| **AI Agents** | CLAUDE.md rules, SoT structure, ID namespaces | Reads portfolio context during incubation, inherits constraints when products graduate |

---

## The Three Goals in Detail

### Goal 1: See Into the Future — Portfolio as Intelligence Layer

Every product repo running this methodology already generates strategic intelligence that's currently trapped inside individual repos:

- `CFD-` entries capture what customers ask for
- `BR-` entries capture what the product can and can't do
- `UJ-` entries reveal where user journeys dead-end
- `RISK-` entries surface unmet challenges
- v0.3 competitive analysis maps the landscape per product

**The portfolio harvests these signals across all products to find whitespace.**

#### The Signal Registry

The single most valuable artifact in the portfolio. It pulls from product repos:

```markdown
## Signal Registry

| ID | Source Product | Source ID | Signal | Frequency | Potential Response |
|----|---------------|-----------|--------|-----------|-------------------|
| SIG-001 | Product Alpha | CFD-034 | "Can I share reports externally?" | 12 req/qtr | New product or feature? |
| SIG-002 | Product Beta | UJ-008 | Journey dead-ends at export | High drop-off | Integration product? |
| SIG-003 | Alpha + Beta | BR-045, BR-012 | Both built auth independently | Tech debt | Shared platform service |
| SIG-004 | (no product) | Competitive gap | Competitor X launched [capability] | Market pressure | New product candidate |
```

#### Gap Analysis

Cross-product journey breaks reveal what's missing:

```markdown
| User Intent | Starts In | Gets To | Breaks At | Gap Type |
|-------------|-----------|---------|-----------|----------|
| "Manage customer lifecycle" | Alpha (onboard) | Beta (billing) | No handoff | Integration gap |
| "Get executive dashboard" | Beta (reports) | Nowhere | No analytics | Product gap |
```

Gap types drive different responses:
- **Integration gap** → Portfolio EPIC for API contracts between existing products
- **Feature gap** → Routed to product squad backlog
- **Product gap** → New product candidate, enters the pipeline

---

### Goal 2: Design Connected Products — The Ecosystem Pipeline

New products move through a funnel:

```
Signal Registry → Candidate → Incubation (v0.1-v0.5 in portfolio) → Own Repo (v0.6+)
```

#### Candidates

One-pagers derived from the signal registry:

```markdown
# Candidate: Analytics Hub

## Origin Signals
- SIG-004: No portfolio answer to competitor X analytics
- SIG-002: Product Beta journey dead-ends at export

## Ecosystem Fit
- Consumes: Product Alpha report data (API-045)
- Consumes: Product Beta export format (API-023)
- Provides: Dashboard embedding for all products (new P:API-XXX)

## Decision
- [ ] Prioritized for incubation
- [ ] Deferred (reason: ___)
- [ ] Rejected (reason: ___)
```

#### Incubation: v0.1 through v0.5 Happens in the Portfolio

Early-stage product work (strategy, market research, user journeys) doesn't need its own repo. It needs access to the portfolio's intelligence. The Horizon and Studio agents work here with full access to every product's SoT, the signal registry, and existing integration contracts.

#### Graduation to Own Repo (v0.5 → v0.6)

Once a product passes the v0.5 Red Team Review, it gets its own repo:

- Product repo created from methodology fork
- PRD.md pre-populated with v0.1-v0.5 work
- SoT/ pre-seeded with inherited portfolio constraints (P:BR-, P:API-)
- Product manifest created in portfolio
- Squad assigned, Jira project created

The new product is **born knowing its ecosystem context**.

#### Ecosystem Contracts

The portfolio maintains integration standards that all products must honor:

```markdown
### P:API-001: Unified Authentication
- Protocol: OAuth 2.0 + RBAC
- Products: Alpha (provider), Beta (consumer), Gamma (consumer)
- Breaking Change Policy: 90-day deprecation window

### P:DES-001: Design System
- Package: @portfolio/ui-components v3.x
- Products: All customer-facing
```

---

### Goal 3: Documentation Consistency

#### The Standard

Every product repo must follow the same structure. This is what makes Goals 1 and 2 possible — if products document differently, the portfolio can't aggregate intelligence.

```
Required in every product repo:
├── README.md          # Portfolio README template
├── PRD.md             # Portfolio PRD template
├── CLAUDE.md          # Portfolio base rules + product overrides
├── SoT/              # Standard ID prefixes
├── epics/            # Standard EPIC template
└── .claude/          # Portfolio-standard hooks
```

#### ID Namespacing

```
Product-scoped (owned by product repos):
  BR-XXX, UJ-XXX, API-XXX, etc.

Portfolio-scoped (owned by portfolio repo):
  P:BR-XXX   — Cross-product business rules
  P:API-XXX  — Ecosystem integration contracts
  P:DES-XXX  — Shared design standards
  P:SIG-XXX  — Demand signals
  P:DEC-XXX  — Portfolio architecture decisions

Cross-reference syntax (in product repos):
  @portfolio P:BR-003
```

#### Template Governance

The portfolio owns canonical templates. Product repos inherit them. Drift is tracked:

```yaml
# products/product-alpha.yaml
template_version: "3.2.0"
portfolio_template_version: "3.4.0"
template_drift: 2 minor versions    # Visible in dashboard
```

---

## Keeping Documentation Fresh

The biggest risk at portfolio scale is stale docs. Our approach: **design for visible staleness and low refresh cost**, not discipline mandates.

### Every artifact carries its age

```markdown
| Product | Gate | Last Verified | Freshness |
|---------|------|---------------|-----------|
| Alpha   | v0.7 | 15 days ago  | STALE     |
| Beta    | v0.4 | 3 days ago   | Fresh     |
| Gamma   | v0.6 | 31 days ago  | STALE     |
```

### The product repo is source of truth; the portfolio is a cache

We never ask squads to maintain two things. They maintain their product repo. The portfolio pulls from it during lightweight sync rituals.

### Refresh is a 5-minute task

**Product-side (end of sprint):** Update lifecycle gate in README, update cross-product API versions.

**Portfolio-side (weekly/biweekly):** Read each product's README, update manifests, flag new dependencies.

### Event-driven triggers, not calendar mandates

Update the portfolio when:
- A product advances a lifecycle gate
- A cross-product API contract changes
- A new product joins the portfolio
- A portfolio EPIC completes a phase
- Quarterly full freshness audit

---

## The Jira Connection

Since we don't have programmatic Jira access, we use **honest manual cross-references**:

```markdown
| Squad | Jira Epic | Status (last checked) | Checked |
|-------|-----------|----------------------|---------|
| Alpha | ALPHA-234 | In Progress | 2026-03-28 |
| Beta  | BETA-89   | Not Started | 2026-03-28 |
```

The "Checked" column makes staleness visible. No one mistakes this for real-time data.

---

## Proposed Repo Structure

```text
portfolio/
├── README.md                    # Portfolio dashboard + product health
├── CLAUDE.md                    # Portfolio agent rules
├── PORTFOLIO.md                 # Portfolio strategy (replaces PRD.md at this level)
│
├── products/                    # Product registry (lightweight manifests)
│   ├── product-alpha.yaml
│   ├── product-beta.yaml
│   └── product-gamma.yaml
│
├── intelligence/                # Goal 1: See the future
│   ├── signal-registry.md
│   ├── gap-analysis.md
│   ├── demand-patterns.md
│   └── ecosystem-map.md
│
├── pipeline/                    # Goal 2: Design connected products
│   ├── candidates/
│   ├── incubating/              # v0.1-v0.5 PRD work lives here
│   └── graduation-checklist.md
│
├── SoT/                         # Portfolio-level Source of Truth
│   ├── SoT.ECOSYSTEM_CONTRACTS.md
│   ├── SoT.PORTFOLIO_RULES.md
│   ├── SoT.DESIGN_STANDARDS.md
│   ├── SoT.PORTFOLIO_DECISIONS.md
│   └── SoT.UNIQUE_ID_SYSTEM.md
│
├── templates/                   # Goal 3: Documentation consistency
│   ├── README_template.md
│   ├── PRD_template.md
│   ├── EPIC_TEMPLATE.md
│   ├── CLAUDE_base.md
│   └── SoT_templates/
│
├── epics/                       # Portfolio-level EPICs (cross-product)
├── temp/
└── .claude/
    ├── agents/
    ├── skills/
    └── hooks/
```

---

## How It Flows

```
Existing Products generate signals (CFD-, UJ dead ends, RISK-)
        |
        v
Portfolio harvests --> Signal Registry
        |
        v
Horizon agent runs Gap Analysis + Demand Patterns
        |
        v
Candidates emerge --> Prioritized by portfolio strategy
        |
        v
Incubation (v0.1-v0.5) happens IN portfolio with full ecosystem context
        |
        v
Graduation --> New repo, pre-wired to ecosystem contracts
        |
        v
Product squad executes v0.6-v1.0 against Jira backlog
        |
        v
Product generates new signals --> cycle repeats
```

---

## Open Questions — Areas of Low Confidence

These need answers from the real IBM portfolio before we move to implementation.

### On Signal Harvesting (Goal 1)

1. **Who does the harvesting?** The signal registry requires someone to read across product repos and extract CFD/UJ/BR signals. Is this a dedicated portfolio role, a rotating responsibility, or something we expect AI agents to do? Each answer has very different tooling implications.

2. **Signal volume and noise.** With multiple products generating CFD- entries, the signal registry could become overwhelming. What's the triage mechanism? Who decides "this is a real signal" vs. "this is one customer's edge case"?

3. **Access patterns.** How often do product teams actually read their own CFD- and RISK- entries today? If those entries are sparse or inconsistent, the intelligence layer has nothing to harvest. What's the actual state of SoT maturity across the IBM products?

### On the Pipeline (Goal 2)

4. **Incubation ownership.** Who drives v0.1-v0.5 for an incubating product? Is it leadership? A dedicated incubation team? The squad that will eventually own it? This affects whether incubation work lives in the portfolio repo or gets a temporary repo earlier.

5. **Graduation timing.** We propose graduation at v0.5 (after Red Team Review). Is that too early or too late? Some teams may want their own repo at v0.3 once commercial viability is clear. Others may want to stay in portfolio through v0.6 (Architecture).

6. **Ecosystem contract enforcement.** P:API- contracts are only useful if products actually implement them. What happens when a product deviates? Is this a CI check? A review gate? A stern conversation? The enforcement mechanism determines whether contracts are real or aspirational.

### On Documentation Consistency (Goal 3)

7. **Template adoption friction.** Existing products may already have their own documentation patterns. How much rework is acceptable to bring them into compliance with portfolio templates? Is there a "grandfather" period, or is it all-at-once?

8. **ID collision in practice.** We propose the `P:` namespace for portfolio IDs. But what if two products already use overlapping ID numbers (both have BR-001)? Do we retroactively namespace product IDs, or accept that cross-product references always need the product name?

9. **CLAUDE.md inheritance.** We propose a base CLAUDE.md that products extend. In practice, products may have conflicting agent rules. How do we handle conflicts between portfolio-level rules and product-level needs?

### On Freshness (Cross-cutting)

10. **Realistic refresh cadence.** We propose event-driven updates and 5-minute rituals. But in reality, sprint ceremonies already feel full. Will scrum masters actually do this? What's the minimum viable freshness ritual that teams will actually follow?

11. **Staleness accountability.** The dashboard shows freshness traffic lights. But who acts on a red light? If no one is accountable for "your product manifest is 30 days stale," the dashboard becomes decoration.

### On Team Adoption (Cross-cutting)

12. **Mental model gap.** This system assumes everyone understands the PRD lifecycle, ID system, and SoT structure. Today, how many people on the IBM team actually do? What's the gap between "the people who forked the repo" and "the designers and data scientists who need to use it"?

13. **Scrum master role shift.** This proposal asks scrum masters to maintain product manifests and Jira cross-references — work that doesn't exist in standard Scrum. Is that a natural fit, or does it need a different role?

14. **Designer and data scientist entry points.** These roles may never touch the repo directly. Do they need a simplified view? A dashboard? Or do we expect them to read markdown files in a git repo?

### On Scale

15. **How many products?** The architecture works differently for 3 products vs. 30. At 3, a human can hold the whole portfolio in their head. At 30, the signal registry and gap analysis become databases, not markdown files. How many products are we designing for?

16. **Portfolio repo size.** If incubating products live in the portfolio, and we accumulate intelligence artifacts, how big does this repo get? Is there a point where we need to archive or split?

---

## What We Need Before Implementation

1. **Access to the actual IBM product repos** — to assess SoT maturity, ID usage, and documentation patterns.
2. **Answers to the open questions above** — especially #1 (who harvests), #7 (template friction), #12 (team understanding), and #15 (scale).
3. **A rollout plan** — to be designed separately, covering training, adoption sequence, and success metrics.
4. **A real cross-product example** — pick two products that should integrate, and trace the full flow from signal to ecosystem contract. This will stress-test the proposal.

---

*This document is a proposal for feedback, not a spec. It will evolve based on what we learn from the real portfolio.*
