---
name: prd-v05-multi-perspective-review
description: >
  Run a structured adversarial review of the PRD through six distinct reviewer personas (engineer, designer,
  executive, skeptic, customer, data analyst) during PRD v0.5 Red Team Review.
  Triggers on requests to review PRD from multiple angles, get stakeholder feedback, run adversarial review,
  or when user asks "review from different perspectives", "multi-perspective review", "adversarial review",
  "what would an engineer think?", "red team this PRD", "six lenses", "stakeholder review".
  Consumes FEA-, UJ-, SCR-, BR-, RISK-, CFD- entries. Produces structured findings per persona and updated RISK- entries.
---

# Multi-Perspective Review

Position in workflow: v0.5 Risk Discovery Interview → **v0.5 Multi-Perspective Review** → v0.5 Technical Stack Selection

This skill runs the PRD through **six adversarial reviewer personas** before technical decisions lock in. Each persona reviews the same material through a different professional lens and produces specific objections, questions, and recommendations. The goal is to surface hidden issues before they become expensive problems in v0.6–v0.8.

## Consumes

This skill requires prior work from v0.1–v0.5 Risk Discovery:

- **FEA-\* feature entries** (from v0.3) — Scope and priority; each persona evaluates whether features are justified from their lens
- **UJ-\* user journey entries** (from v0.4) — Flow and friction; designer and customer personas focus here
- **SCR-\* screen entries** (from v0.4) — UI structure; designer and customer personas review screen logic
- **BR-\* business rules** (from v0.2-v0.3) — Constraints; engineer, executive, and skeptic personas stress-test these
- **RISK-\* entries** (from v0.5 Risk Discovery) — Existing identified risks; personas may confirm, extend, or contradict
- **CFD-\* customer feedback** (from v0.1-v0.2) — Market evidence; customer and skeptic personas validate evidence quality

This skill assumes v0.5 Risk Discovery Interview is complete so RISK- entries exist as reference.

## Produces

This skill creates/updates:

- **Per-persona finding sets** — Structured objections, questions, and recommendations from each of the 6 reviewers (documented in temp/ as `temp/multi-perspective-review-YYYY-MM-DD.md`)
- **New or updated RISK-\* entries** — Findings that rise to the level of a risk are registered using `ghm-id-register` or added directly to RISK- register in PRD.md
- **Resolved questions log** — Issues raised by personas that were immediately answered (owner confirms resolution)
- **Blocking issues list** — Items any persona flagged as a hard blocker before proceeding to Technical Stack Selection

All findings are **advisory inputs** from the AI personas; the human owner decides which findings are accepted, which produce new RISK- entries, and which are dismissed with rationale.

## The Six Reviewer Personas

Each persona has a fixed professional lens and a standard set of concerns. The AI adopts each persona fully—it does not hedge or soften findings.

### 1. Engineer — Feasibility Lens

**Role**: Senior backend/fullstack engineer, 5+ years, pragmatic about what takes how long.

**Concerns**:
- Which features have hidden technical complexity not reflected in the current scope?
- Which integrations, APIs, or third-party dependencies are underestimated?
- What data model decisions will become costly to change after v0.7?
- Where does the feature set create unexpected infrastructure load?
- Which FEA- items are technically dependent on other FEA- items not yet planned?
- What testing surface is being neglected in the current scope?

**Output format**:
```
ENGINEER REVIEW:
Blocking: [List of features/decisions the engineer would refuse to build as-spec'd]
High-effort underestimates: [Items that will take 3x longer than assumed]
Technical dependencies missing: [FEA- items with hidden prerequisites]
Data model risks: [Schema decisions that create future migration pain]
Recommended changes: [Specific scope or spec adjustments]
```

---

### 2. Designer — UX Clarity Lens

**Role**: Senior product designer focused on user empathy, interaction clarity, and accessibility.

**Concerns**:
- Which user journeys have unresolved friction points the current screens don't address?
- Where is the UJ- flow asking users to do something cognitively expensive?
- Which SCR- screens lack a clear primary action or have ambiguous navigation?
- What onboarding or empty states are missing from the current screen plan?
- Where does the product assume user knowledge that new users won't have?
- Are there accessibility gaps in the current screen definitions?

**Output format**:
```
DESIGNER REVIEW:
Friction points: [UJ- steps where users will likely drop or make errors]
Unclear screens: [SCR- entries with ambiguous primary action or missing state]
Missing screens: [States that aren't in SCR- but will be needed: empty, error, loading]
Onboarding gaps: [What new users won't understand without guidance]
Accessibility flags: [Interactions that exclude users with disabilities]
Recommended changes: [Specific UX or screen adjustments]
```

---

### 3. Executive — Strategic Fit & ROI Lens

**Role**: VP Product or C-suite; focused on revenue, competitive positioning, and resource allocation.

**Concerns**:
- Does the feature set justify the investment relative to the KPI- targets?
- Which FEA- items are nice-to-haves that wouldn't move the core KPI-?
- Where is the product over-investing in a feature no competitor has ever validated?
- What is the minimum viable scope to reach the first KPI- threshold?
- Does the pricing model (BR-) create the right revenue trajectory?
- What would justify killing this project at v0.5 instead of proceeding?

**Output format**:
```
EXECUTIVE REVIEW:
ROI question: [Features where cost > realistic revenue contribution]
Scope trim candidates: [FEA- items that don't move primary KPI-]
Strategic risks: [Market or positioning concerns not captured in RISK-]
Kill criteria: [What outcome at launch would justify stopping investment]
Minimum viable scope: [What subset would validate the core value proposition fastest]
Recommended changes: [Prioritization or scope adjustments]
```

---

### 4. Skeptic — Assumptions & Evidence Lens

**Role**: Experienced PM or researcher who has seen products fail when assumptions go untested.

**Concerns**:
- Which CFD- entries are based on a small or biased sample?
- Which FEA- items assume user behavior that hasn't been validated?
- Which BR- business rules were decided without competitive or market evidence?
- What is the biggest "we assume" statement in the PRD that has never been tested?
- Which KPI- targets are aspirational rather than evidence-based?
- What evidence would change the current product direction if it proved false?

**Output format**:
```
SKEPTIC REVIEW:
Weakest assumptions: [Beliefs driving FEA- scope with no CFD- support]
Evidence gaps: [Market or user claims with no validation]
Aspirational metrics: [KPI- targets not grounded in benchmarks or prior data]
Critical test: [The single most important assumption to validate before v0.6]
Contradictions: [Places where CFD- evidence conflicts with FEA- or BR- decisions]
Recommended changes: [Validation steps or scope adjustments]
```

---

### 5. Customer — Usability & Value Lens

**Role**: Target user persona from PER-; pragmatic, time-constrained, not interested in features—only outcomes.

**Concerns**:
- What is the first thing I (as PER-001) try to do, and how long does it take to succeed?
- Which features solve a problem I never complained about?
- At which point in the UJ- flow would I give up or switch to a competitor?
- What would make me tell a colleague about this product?
- What would make me churn in the first 30 days?
- Is the pricing (BR-) something I would pay without thinking twice?

**Output format**:
```
CUSTOMER REVIEW (as [PER-001 persona name]):
Time-to-value: [How long before I get the outcome I came for?]
Frustration points: [Where I'd drop off in UJ- flow]
Unneeded features: [FEA- items solving a problem I don't have]
Referral trigger: [What outcome would make me tell others]
Churn trigger: [What would make me leave in month 1]
Pricing reaction: [Honest reaction to the current BR- pricing]
Recommended changes: [Specific adjustments from the customer lens]
```

---

### 6. Data Analyst — Measurability Lens

**Role**: Analytics engineer or data analyst; can only trust what can be measured; skeptical of unmeasurable success.

**Concerns**:
- Which KPI- metrics lack a defined event or data source to measure them?
- Which FEA- items have no measurable success signal?
- Where does the product rely on qualitative signals that can't be tracked at scale?
- What instrumentation needs to be built before launch for KPI- to be measurable?
- Which UJ- journeys have no funnel tracking defined?
- What does "activation" mean in concrete, trackable terms?

**Output format**:
```
DATA ANALYST REVIEW:
Unmeasurable KPIs: [KPI- entries with no defined data source or event]
Missing instrumentation: [Events that must be tracked but aren't yet defined]
Funnel gaps: [UJ- steps with no tracking defined]
Activation definition: [Specific event that marks a user as "activated"]
Leading indicators: [Early metrics that predict KPI- outcomes before v1.0 data is available]
Recommended changes: [Specific tracking or instrumentation requirements]
```

---

## Review Execution Flow

### Phase 1: Context Load (AI prepares)

Before running any persona, the AI:
1. Reads all FEA-, UJ-, SCR-, BR-, RISK-, CFD- entries
2. Identifies the 2-3 most important issues per persona from prior context
3. Prepares targeted questions (don't ask generic questions that don't reference actual IDs)

### Phase 2: Sequential Persona Reviews

Run personas in order: Engineer → Designer → Executive → Skeptic → Customer → Data Analyst.

For each persona:
1. AI adopts the persona fully and produces the structured review output above
2. User reads the review and responds (confirms, disputes, or provides more context)
3. AI updates findings based on user response
4. Findings that rise to RISK- level are flagged for registration

### Phase 3: Synthesis

After all 6 reviews:

1. **Blocking issues**: Items any persona marked "blocking" — require resolution before v0.5 can close
2. **High-priority findings**: Issues raised by 2+ personas from different lenses — highest confidence issues
3. **New RISK- candidates**: Findings that meet RISK- criteria (Impact ≥ Medium, not already captured)
4. **Scope trim candidates**: Features flagged by Executive + Skeptic + Customer as low-value

### Phase 4: RISK- Registration

For any finding that rises to a risk:
1. Create RISK- entry using existing template from `prd-v05-risk-discovery-interview`
2. Add source tag: `Source: multi-perspective-review, [Persona]`
3. Register using `ghm-id-register`

## Quality Gates

Before proceeding to Technical Stack Selection:

- [ ] All 6 personas have completed their review
- [ ] User has responded to each persona's findings
- [ ] Blocking issues are either resolved or explicitly escalated to RISK-
- [ ] Any new RISK- entries are registered with `ghm-id-register`
- [ ] Synthesis table is complete (blocking, high-priority, scope-trim candidates)
- [ ] Owner has signed off that findings are either actioned or accepted as-is

## Anti-Patterns to Avoid

| Anti-Pattern | Signal | Fix |
|---|---|---|
| Generic feedback | "This looks good" / "I have concerns about UX" | Every finding must reference a specific FEA-, UJ-, SCR-, or BR- ID |
| All personas agree | Every persona gives similar feedback | Personas should genuinely conflict; if they don't, the AI is softening its outputs |
| No RISK- registration | Findings discussed but never recorded | Any finding above "nitpick" must become a RISK- or be explicitly dismissed with rationale |
| Owner confirms everything immediately | No real engagement | Findings are meant to create productive disagreement; push back on superficial confirmations |
| Skipping personas | "We don't need the executive lens" | Run all 6; the value is in the unexpected conflict across lenses |

## Downstream Connections

Multi-Perspective Review findings feed into:

| Consumer | What It Uses | Example |
|---|---|---|
| **v0.5 Technical Stack Selection** | Engineer findings on complexity | RISK- from engineer review constrains tech choices |
| **v0.6 Architecture Design** | Engineer + Data Analyst findings | ARC- decisions address performance and instrumentation concerns |
| **v0.4 Screen Flow (revision)** | Designer + Customer findings | SCR- entries updated to address friction and missing states |
| **v0.3 Features (revision)** | Executive + Skeptic findings | FEA- priorities adjusted based on ROI and evidence quality |
| **v0.9 GTM Strategy** | Customer + Executive findings | GTM messaging addresses concerns surfaced in customer lens |
