# PRD-Driven Skills: Core Principles

**Purpose**: Define the CPO-level principles that govern all 25 domain skills (v0.1 through v1.0). Every skill improvement and consolidation decision should be validated against these principles.

**Derived from**: 20-year CPO interview on stage-appropriate decision-making, MVP clarity, SoT architecture, and distributed AI development.

---

## The Six Core Principles

### P1: MVP is Sacred (Must-Have) ⭐

**Statement**: This methodology is for 0→1 only. The goal is to deliver a *quality product to market fast* to hear user reaction. Not velocity-first, not cost-first — a disciplined balance between speed and value delivery.

**What this means**:
- The entire methodology ends at v1.0 Scale. PMF and post-PMF are different methodologies.
- "MVP" is not "smallest possible" — it's "minimum *viable*" (delivers value to at least some users)
- Success is: users react to the product, good or bad. Failure is: no reaction because the product wasn't ready.
- Thinking too far ahead (estimating costs at 10x scale, designing for infinite scalability, over-engineering) distorts MVP decisions.

**What skills should do**:
- Ask "what will users actually use in v1?" before designing infrastructure for v10.
- Resist premature optimization (cost, performance, reliability) that doesn't serve the MVP goal.
- Keep focus on *bringing the product to market*, not building the ultimate version.
- Scope decisions are OK (cut features to maintain quality+speed balance); tech decisions should not predict a future stage.

**Anti-pattern**: Tech stack skill choosing expensive infrastructure because it optimizes for 10x scale costs. ❌

---

### P2: Quality + Speed Balance

**Statement**: Optimization priority is: "deliver value fast enough to learn." Not velocity-only, not completeness-only — but the intersection of "good enough to matter" and "fast enough to hear from users."

**What this means**:
- The balance is qualitative, not a metric. Different products and markets will have different "good enough" thresholds.
- Scope decisions *can* be driven by cost constraints (cut features, reduce to a slice of the market). This is P2 at work.
- Tech decisions should *not* be driven by future-stage cost optimization. This violates P1.
- Quality means: the product delivers the value you promised; it's not gold-plated, but it's not broken.
- Speed means: you get to market in days/weeks, not months/years, with the MVP scope.

**What skills should do**:
- Encourage scope reduction (MVP clarification) when cost, complexity, or capability constraints emerge.
- Discourage tech shortcuts that compromise the product experience (e.g., "we'll optimize UI later").
- Help the user make explicit trade-offs: "you can have faster time-to-market by reducing scope, or slower by adding feature X."

**Anti-pattern**: Skipping testing to move faster, then shipping a broken product. ❌

---

### P3: Research Drives Scope (High Priority)

**Statement**: MVP definition is fuzzy because research is incomplete. Skills must *relentlessly interrogate and research* what the actual MVP should be. MVP scope must be an explicit, auditable artifact in the SoT/PRD.

**What this means**:
- Over-scoping happens when you assume user needs without research. Under-scoping happens when you miss a critical requirement.
- Both are expensive: over-scoping delays market entry; under-scoping requires immediate post-launch development.
- The methodology's job is to surface discovery tasks and user research that clarifies scope.
- "MVP scope" must be a named artifact in the SoT (e.g., `MVP-SCOPE.md` entry or explicit in FEA-/RISK- entries) — not implicit in the feature list.

**What skills should do**:
- Early-stage skills (v0.1-v0.4) should surface research questions that the user/team needs to answer.
- Discovery skills (v0.2 Landscape, v0.4 Journeys) should explicitly feed into v0.3 feature scoping.
- Make "MVP scope definition" a visible decision point: "Based on this research, here's the minimum viable feature set."
- Call out when research is incomplete: "We don't have enough user evidence to decide if feature X belongs in MVP."

**Anti-pattern**: Defining features based on competitive analysis alone, without understanding actual user jobs-to-be-done. ❌

---

### P4: SoT is Living Evidence (Must-Have) ⭐

**Statement**: IDs in the SoT are not one-time writes. Each ID carries a confidence score (1-5) and evidence source. As evidence accumulates (PM decision → interview → beta → usage), confidence increases. This enables readiness assessment ("can we build this yet?").

**What this means**:
- Every SoT ID (CFD-015, TECH-042, DEP-005, etc.) gets a confidence score indicating the strength of evidence behind it.
- Confidence score is simple: `1/5` (PM assumption) through `5/5` (production evidence). Highest source is tracked.
- Different SoT types have different confidence progressions (see **Confidence Score Model** below).
- A `confidence: 2/5` customer insight and a `confidence: 5/5` one are *different inputs to downstream decisions*.
- The confidence model enables distributed AI development: when an EPIC picks up work, it can see "this feature is 2/5 confidence, only from a PM interview" and act accordingly.

**What skills should do**:
- When creating/updating SoT IDs, include confidence score and source.
- Example: `CFD-015: Users want dark mode (confidence: 3/5, source: 5-user interviews Jan 2026)`
- Example: `TECH-042: Use Supabase for backend (confidence: 2/5, source: PM decision based on prior experience)`
- Include a forward-looking statement: "This would move to 4/5 if we validate with 3 beta testers."
- In ghm-sot-builder, ask: "What confidence is this at? What evidence would move it to the next level?"

**Anti-pattern**: Treating all SoT IDs as equally valid regardless of evidence. ❌

---

### P5: Distributed Development Needs Connective Tissue (High Priority)

**Statement**: Development happens across multiple AI context windows. Each EPIC picks up incomplete context. Clear work boundaries, cross-cutting traceability, and explicit connective tissue between skills prevent end-to-end risk and quality loss.

**What this means**:
- When v0.7 Build picks up work from v0.6 Architecture, the EPIC breakdown must be clear enough that a fresh AI context can execute it.
- Testing infrastructure can't be a blocker — test strategy should integrate into EPIC sequencing.
- "Connective tissue" = explicit Consumes/Produces links between skills. What does v0.2 produce that v0.3 needs?
- EPIC Phase definitions (Plan / Design / Build / Validate / Finish) and their boundaries matter because they're where context gets handed off.

**What skills should do**:
- Each skill should have an explicit **Consumes** section: "This skill requires these SoT entries as input."
- Each skill should have an explicit **Produces** section: "This skill creates/updates these SoT entries."
- Execution skills (v0.7-v0.8) should be very explicit about EPIC sequencing and what each EPIC boundary protects.
- Don't assume the next context window has all previous artifacts — make the handoff artifacts explicit.

**Anti-pattern**: v0.6 Architecture producing a spec that v0.7 Build can't act on without rework. ❌

---

### P6: Reuse-First, Ask Early (High Priority)

**Statement**: Don't assume greenfield. Ask "what do you already have?" and "what open-source solves this?" early in discovery. This is not about cost optimization (that's P2); it's about *realism*.

**What this means**:
- Products often integrate with existing systems, use off-the-shelf platforms, or have legacy code to work around.
- Tech stack decisions should surface the reuse question early (v0.5 Tech Stack Selection does this well).
- But discovery skills (v0.1-v0.4) should also be asking: "Do you already have customer data? Are you integrating with an existing platform? Do you have an existing codebase?"
- Greenfield bias = assuming everything is built from scratch. This biases toward over-scoping and wrong tool choices.

**What skills should do**:
- Ask the user/team early: "What existing assets, accounts, or platforms do you want to reuse?"
- Surface open-source tools that might solve parts of the functionality.
- Don't recommend specific vendors, but ask about reusable patterns and platforms.
- When greenfield is assumed, flag it: "This guidance assumes you're starting from scratch. If you're integrating with X, that changes the architecture."

**Anti-pattern**: Recommending a full custom build when an existing platform or open-source tool already solves 80% of the problem. ❌

---

## Confidence Score Model

### General Framework

Each SoT entry gets a confidence score (1-5) indicating evidence strength:

| Score | Evidence Level | What It Means | Examples |
|-------|----------------|---------------|----------|
| 1/5 | PM decision / assumption | Internal logic, no external validation | "PM thinks users want dark mode" |
| 2/5 | Secondary research / analysis | Informed by indirect evidence | "Competitive analysis shows 3 competitors have dark mode" |
| 3/5 | User interview / qualitative | Direct feedback from actual/potential users | "5 interviews confirmed users want dark mode" |
| 4/5 | Validated in beta / small scale | Real behavior in a limited setting | "10 beta testers used dark mode; 8 loved it" |
| 5/5 | Production evidence | Real behavior at scale | "80% of active users enable dark mode" |

### SoT Type–Specific Confidence Progressions

#### CFD (Customer Feedback)
- 1/5: PM belief or internal conversation
- 2/5: Competitive research, market report
- 3/5: Pre-product interviews (5+ users)
- 4/5: Beta cohort validation
- 5/5: Post-launch usage data

**Example**: `CFD-042: Dark mode improves retention (confidence: 4/5, source: beta-cohort-jan-2026-10-users)`

---

#### FEA (Features in PRD)
- 1/5: PM assumption / competitive parity
- 2/5: Competitive analysis (others have this)
- 3/5: Customer interviews identify this pain
- 4/5: Beta testers confirm they'd use it
- 5/5: Launched and users rely on it

**Example**: `FEA-15: Dark mode (confidence: 3/5, source: 5-customer-interviews-feb-2026)`

---

#### TECH (Tech Stack Decisions)
- 1/5: PM preference or team comfort
- 2/5: Team experience with the tool
- 3/5: Local development successful
- 4/5: Staging environment proven
- 5/5: Production deployment successful

**Example**: `TECH-012: Supabase backend (confidence: 3/5, source: local-dev-successful)`

---

#### DEP (Deployment Steps)
- 1/5: Deployment planned, not executed
- 2/5: Deployment runbook documented
- 3/5: Successful local/dev deployment
- 4/5: Successful staging deployment
- 5/5: Successful production deployment

**Example**: `DEP-008: Blue-green deployment strategy (confidence: 2/5, source: documented-not-tested)`

---

#### RISK (Risks in PRD)
- 1/5: Potential risk identified
- 2/5: Risk researched, impact unclear
- 3/5: Risk impact estimated
- 4/5: Risk mitigation strategy designed
- 5/5: Risk mitigation tested/validated

**Example**: `RISK-003: Vendor lock-in with Supabase (confidence: 3/5, source: identified-impact-not-mitigated)`

---

#### API (API Contracts)
- 1/5: API designed on paper
- 2/5: API spec reviewed by team
- 3/5: API implementation started
- 4/5: API tested in staging
- 5/5: API tested in production

**Example**: `API-042: POST /users/{id}/preferences endpoint (confidence: 2/5, source: spec-reviewed)`

---

#### ARC (Architecture)
- 1/5: Architecture decision made
- 2/5: Architecture validated against requirements
- 3/5: Architecture prototyped
- 4/5: Architecture implemented in staging
- 5/5: Architecture proven in production

**Example**: `ARC-007: Microservices separation (confidence: 2/5, source: designed-not-prototyped)`

---

## Connective Tissue Standard: Consumes / Produces

Every skill should explicitly document what it requires as input and what it produces as output. This prevents isolated work and ensures workflows are clear.

### Format (in each SKILL.md)

```markdown
## Consumes

- **From v0.X [Previous Skill]**: List SoT IDs needed (CFD-, RISK-, etc.)
- Example: CFD-* (customer feedback), RISK-* (identified risks)

## Produces

- **For v0.Y [Next Skill]**: List SoT IDs this skill creates/updates
- Example: FEA-* (feature definitions), MVP-SCOPE (scope artifact)
- Include confidence score guidance: "Produce FEA entries at confidence: 3/5 minimum (based on user research)"
```

### Example: v0.2 → v0.3

**v0.2 Competitive Landscape Mapping** produces:
- CFD-* entries (competitive landscape findings)
- Guidance on "parity features" vs. "delta features"

**v0.3 Features & Pricing** consumes:
- CFD-* entries from v0.2 (to avoid building features competitors already have well)
- Prior FEA-* entries (if this is iteration, not greenfield)

---

## Audit Checklist: Apply to All 25 Skills

When improving any skill, check:

- [ ] **Consumes/Produces**: Explicit input/output SoT IDs documented?
- [ ] **Research-first**: Does the skill interrogate the user/domain before assuming answers? (v0.1-v0.4 should especially emphasize this)
- [ ] **MVP scope**: Does the skill make MVP scope decision explicit? (v0.1-v0.3 especially)
- [ ] **Confidence model**: Do SoT ID examples include confidence scores?
- [ ] **Greenfield bias**: Does the skill assume building from scratch, or does it surface reuse/integration paths?
- [ ] **Distributed context**: Is the skill clear enough that a fresh AI context (different from the one that created prior artifacts) can execute it?
- [ ] **P1 alignment**: Does the skill respect "MVP is sacred" or does it push toward premature optimization/over-engineering?
- [ ] **P4 alignment**: Does the skill help build confidence in SoT entries over time?

---

## Quick Reference: Which Principles Matter Most for Which Skills

| Skill Type | P1 | P3 | P4 | P5 | P6 |
|-----------|----|----|----|----|-----|
| **Discovery (v0.1-v0.4)** | ⭐ | ⭐ | High | — | High |
| **Risk & Tech (v0.5)** | ⭐ | High | ⭐ | — | High |
| **Architecture (v0.6)** | ⭐ | — | High | ⭐ | High |
| **Build (v0.7)** | ⭐ | — | High | ⭐ | — |
| **Release (v0.8)** | ⭐ | — | ⭐ | ⭐ | — |
| **Launch (v0.9)** | — | — | High | — | — |

---

## Next: Skill Improvement Sequence

Once you've internalized these principles:
1. **Audit** all 25 domain skills against the checklist above
2. **Prioritize** improvements by impact (discovery skills first, then execution)
3. **Update** each skill with Consumes/Produces, confidence examples, and MVP scope clarity
4. **Test** by tracing a mock product through 3 skills (v0.1 → v0.3 → v0.7) — outputs should flow cleanly
