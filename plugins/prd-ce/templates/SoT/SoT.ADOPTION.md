---
version: 1.0
purpose: Source of Truth for adoption-stage data using Geoffrey Moore's Technology Adoption Lifecycle.
id_prefix: ADO-XXX
last_updated: 2026-05-22
authority: This is a SoT file - entries created and updated by v1.0 skills (chasm-adoption-moore, continuous-discovery-torres, mom-test-interview, case-study-builder, testimonial-collector)
---

# Adoption (SoT File)

> **Purpose**: Track current adoption-stage position, beachhead segment, whole-product gaps, reference accounts, and chasm-crossing strategy.
> **ID Prefix**: ADO-XXX
> **Status**: Active SoT file (v1.0 stage)
> **Source**: Created and updated by v1.0 PRD skills
> **Audience**: All agents (post-launch and v1.0 work especially)
> **Cross-References**: Referenced by GTM-* (positioning, channels), KPI- (adoption metrics), CFD- (customer evidence)

## ID Categories

Each ADO- entry belongs to one of four sub-types. Confidence scoring (1-5) per [P4](../`.claude/skills/PRINCIPLES.md`).

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

## Example Entries

### ADO-STAGE-001: Current Adoption Stage Assessment

- **Stage**: Early Adopters (with first chasm signals)
- **Evidence**:
  - Paying customers: 12. Of those: 9 are early-adopter shape (technologist founders, willing to debug, talk to founder weekly). 3 are early-majority shape (asked about SOC2, references, integration with existing stack).
  - Inbound shape changing: recent inquiries asking "do you have X integration?" — pragmatist behavior.
- **Confidence**: 3/5 (qualitative interview evidence, n=12)
- **Implications**: Chasm crossing is the next strategic question, not an aspiration. Beachhead selection needed (ADO-BEACHHEAD-).
- **Linked IDs**: CFD-100 (interview cohort), GTM-001 (positioning best-fit), KPI-101 (paid conversion rate)
- **Last verified**: YYYY-MM-DD
- **Status**: Active

### ADO-BEACHHEAD-001: Beachhead Segment

- **Segment**: [Specific firmographic + behavioral + use-case slice]
- **In-segment criteria** (must satisfy ALL):
  - [Firmographic: company size, industry, geography]
  - [Behavioral: tool stack, workflow, team shape]
  - [Trigger: when they need this NOW vs eventually]
- **Not in-segment** (explicitly excluded for chasm crossing):
  - [Adjacent segments — record them; come back via "bowling alley" later]
- **Rationale**: Why this segment first? (Pragmatist density + lowest whole-product gap + reference accessibility.)
- **Confidence**: 2/5 → 3/5 with first 5 closed-won deals in segment
- **Target**: 10 closed-won in this segment within [timeframe]
- **Linked IDs**: PER-001 (sharpened beachhead persona), CFD-XXX (segment interviews), ADO-STAGE-001
- **Status**: Active

### ADO-WHOLE-001: Whole-Product Gap — SSO Integration

- **Gap type**: Integration
- **Description**: Beachhead pragmatists require SSO (Okta / Azure AD) before purchase. Currently not shipped.
- **Reported by**: CFD-105, CFD-108, CFD-112 (three lost deals cited SSO)
- **Severity**: Blocker (no SSO = no deal in segment)
- **Owner**: Engineering Lead
- **Target close date**: YYYY-MM-DD
- **Confidence**: 4/5 (multiple lost-deal CFD- entries confirm)
- **Linked IDs**: FEA-X (SSO feature), EPIC-Y (delivery), ADO-BEACHHEAD-001

### ADO-REF-001: Reference Account — [Customer Name]

- **Customer**: [Logo / company name]
- **Segment fit**: ✓ In beachhead (ADO-BEACHHEAD-001)
- **Story strength**: [What outcome are they willing to talk about publicly?]
- **Consent**: [Approved for: logo / quote / case study / on-stage / podcast]
- **Target placement**: [Pricing page logo, blog case study, conference talk, AE talking points]
- **Confidence**: 4/5 (signed consent, story drafted, awaiting review)
- **Linked IDs**: CFD-XXX (customer interview), GTM-CASE-XXX (case study asset), ADO-BEACHHEAD-001

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
