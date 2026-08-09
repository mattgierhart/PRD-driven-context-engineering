---
version: 1.0
purpose: Source of Truth for adoption-stage data using Geoffrey Moore's Technology Adoption Lifecycle.
id_prefix: ADO-XXX
last_updated: YYYY-MM-DD
authority: Template structure only until product-specific ADO records are accepted and added to the PRD SoT snapshot.
template_state: uninitialized
---

# Adoption (SoT File)

> **Purpose**: Track current adoption-stage position, beachhead segment, whole-product gaps, reference accounts, and chasm-crossing strategy.
> **ID Prefix**: ADO-XXX
> **Status**: Uninitialized template — no ADO records are accepted
> **Source**: Created and updated by v1.0 PRD skills
> **Audience**: All agents (post-launch and v1.0 work especially)
> **Cross-References**: Referenced by GTM-* (positioning, channels), KPI- (adoption metrics), CFD- (customer evidence)

## ID Categories

Each ADO- entry belongs to one of four sub-types. Confidence uses the active methodology's 1–5
evidence scale and must name its source and next validation target.

### ADO-STAGE-XXX: Adoption-stage assessment

Where the product currently sits on Moore's lifecycle. One active entry at a time (older snapshots remain in history). Confidence based on evidence (qualitative customer composition, paid-customer composition, growth rate, retention shape).

### ADO-BEACHHEAD-XXX: Beachhead segment definition

The single early-majority sub-segment chosen as the chasm-crossing target. Sharper than the Dunford best-fit (which spans early adopters + early majority). Strict "in / not in" criteria.

### ADO-WHOLE-XXX: Whole-product gap

Specific product / service / integration / reference / process that pragmatist buyers expect but is currently missing. Each gap has an owner and a target close date.

### ADO-REF-XXX: Reference account

Named customer being cultivated as a public reference for the beachhead segment. Tracks reference-readiness (consent, story strength, target placement — pricing page, case study, conference talk).

---

## Stage Reference: Moore's Technology Adoption Lifecycle

| Stage | % of market | Buyer mindset | What they need to buy |
|-------|-------------|---------------|------------------------|
| **Innovators** (2.5%) | Technologists / tinkerers | Want to try new things; high tolerance for incomplete products | Vision, access, technical depth |
| **Early Adopters** (13.5%) | Visionaries | Want strategic advantage; tolerate rough edges if upside is large | Bold vision + ROI story |
| **— THE CHASM —** | — | — | — |
| **Early Majority** (34%) | Pragmatists | Want reliable productivity gains; need proof from peers | Whole product + references in their segment |
| **Late Majority** (34%) | Conservatives | Want safe, mature, defaults | Maturity, market leadership, low risk |
| **Laggards** (16%) | Skeptics | Resist change | (Generally not worth targeting) |

The chasm — the gap between Early Adopters and Early Majority — is where most products die. The buyer behavior change from "I love bold new ideas" to "show me 3 references in my industry" is enormous.

---

## Synthetic Format Examples — Non-authoritative

> These records demonstrate field shape only. Every name, ID, count, claim, status, and confidence
> value is fictional or a placeholder. Replace them with attributable evidence and owner-accepted
> IDs before treating any ADO record as product truth.

### ADO-STAGE-001: Current Adoption Stage Assessment

- **Stage**: Early Adopters (with first chasm signals)
- **Evidence**:
  - {Attributable customer-composition evidence}
  - {Attributable inbound, retention, or purchasing-behavior evidence}
- **Confidence**: {N}/5 ({source and limitations})
- **Implications**: {What the accepted evidence changes}
- **Linked IDs**: {CFD-XXX, GTM-XXX, KPI-XXX}
- **Last verified**: YYYY-MM-DD
- **Status**: Template — non-authoritative

### ADO-BEACHHEAD-001: Beachhead Segment

- **Segment**: [Specific firmographic + behavioral + use-case slice]
- **In-segment criteria** (must satisfy ALL):
  - [Firmographic: company size, industry, geography]
  - [Behavioral: tool stack, workflow, team shape]
  - [Trigger: when they need this NOW vs eventually]
- **Not in-segment** (explicitly excluded for chasm crossing):
  - [Adjacent segments — record them; come back via "bowling alley" later]
- **Rationale**: Why this segment first? (Pragmatist density + lowest whole-product gap + reference accessibility.)
- **Confidence**: {N}/5 ({source and limitations})
- **Target**: {Accepted outcome and timeframe}
- **Linked IDs**: {PER-XXX, CFD-XXX, ADO-STAGE-XXX}
- **Status**: Template — non-authoritative

### ADO-WHOLE-001: Whole-Product Gap — {Name}

- **Gap type**: Integration
- **Description**: {Evidence-backed missing expectation}
- **Reported by**: {CFD-XXX references}
- **Severity**: {Blocker | Serious | Moderate}
- **Owner**: {Role}
- **Target close date**: YYYY-MM-DD
- **Confidence**: {N}/5 ({source and limitations})
- **Linked IDs**: {FEA-XXX, EPIC-XX at v0.7+, ADO-BEACHHEAD-XXX}
- **Status**: Template — non-authoritative

### ADO-REF-001: Reference Account — [Customer Name]

- **Customer**: [Logo / company name]
- **Segment fit**: ✓ In beachhead (ADO-BEACHHEAD-001)
- **Story strength**: [What outcome are they willing to talk about publicly?]
- **Consent**: [Approved for: logo / quote / case study / on-stage / podcast]
- **Target placement**: [Pricing page logo, blog case study, conference talk, AE talking points]
- **Confidence**: {N}/5 ({consent and review state})
- **Linked IDs**: CFD-XXX (customer interview), GTM-CASE-XXX (case study asset), ADO-BEACHHEAD-001
- **Status**: Template — non-authoritative

---

## Update Protocol

1. **Created by**:
   - `prd-v10-chasm-adoption-moore` — initial ADO-STAGE-, ADO-BEACHHEAD-, ADO-WHOLE-
   - `prd-v10-case-study-builder` — populates ADO-REF- as cases ship
   - Continuous discovery skills update ADO-STAGE- confidence as evidence accumulates
2. **Confidence progression** (P4):
   - 1/5: Internal assumption only
   - 2/5: Secondary research / competitor signal
   - 3/5: Qualitative customer evidence (interviews)
   - 4/5: Quantitative beta-cohort or pre-launch usage data
   - 5/5: Production evidence (paying-customer behavior at scale)
3. **Re-assess cadence**:
   - ADO-STAGE: Monthly during v1.0 push; quarterly after stable
   - ADO-BEACHHEAD: Re-test only when 10+ closed-won evidence available or chasm-crossing strategy shifts
   - ADO-WHOLE: Reviewed every sprint until closed
   - ADO-REF: Updated as consent / placement status changes
4. **Stale flag**: Entries older than 90 days without re-verification get `⚠️ STALE`.
5. **Archive**: When ADO-STAGE moves forward (Early Adopters → Bowling Alley → Tornado), preserve prior snapshots in `## Stage History` section below.

---

## Stage History

> **Append-only**: When ADO-STAGE assessment changes, snapshot the prior state here.

_(No entries yet)_

---

## Cross-Reference Index

| ADO ID | Related IDs | Sub-type |
|--------|-------------|----------|
| _(populated as entries are created)_ | | |
