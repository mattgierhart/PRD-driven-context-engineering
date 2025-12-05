# PRD v0.4 Research Agent Instructions

> Part of the PRD Instruction Library (`docs/prd/instructions/`). Keep filenames and structure consistent when cloning for future PRD stages.

## Mission Alignment
**Objective:** Collect and synthesize persona + journey evidence (interviews, screen captures, workflow audits) so AURA can author the PRD v0.4 User Journeys section with SoT-ready UJ- IDs.
**Downstream Consumer:** AURA converts your findings into Persona summaries, Journey tables, and dependency callouts for upcoming EPICs.
**Deliverable Count:** Provide 3–7 Journey Cards covering the highest-priority personas identified in v0.3. Each Journey Card must align to one persona + trigger + desired value outcome.
**Methodology Alignment:** Every interview or artifact should land in SoT as CFD- (qualitative evidence) and be tied to proposed UJ- IDs. Tag any BR-/API- implications discovered (e.g., compliance steps, integration requirements).

## ID Interlock Map
- **Inputs:** Segment + monetization IDs (`CFD-SGM-*`, `CFD-PRC-*`, `BR-PRC-*`), risk notes from v0.5 backlog, and open questions documented in PRD v0.3.
- **Processing:** For each persona/journey, trace which monetization assumption it validates. Extend or cross-link IDs accordingly (e.g., `CFD-PRC-210` references `UJ-LAB-01` once interviews confirm willingness to pay).
- **Outputs:**
  - Candidate `UJ-*` IDs per journey with references to supporting `CFD-UJ-*` artifacts.
  - Updated `CFD-*` entries for quotes, pain metrics, or tool stack observations.
  - Dependency stubs for `BR-`, `API-`, `DBT-`, or `TEST-` IDs triggered by journey insights.
  - Lifecycle hooks calling out which risks/assumptions must be challenged in v0.5.

## Business Rule Criteria & Key Questions
1. **Persona Alignment:** Does each `UJ-*` candidate clearly map back to the monetization model (who pays, who operates, who benefits)?
2. **Evidence Coverage:** Are pain claims supported by traceable `CFD-` artifacts, and do they quantify severity/frequency to justify investment priority?
3. **Integration/Policy Needs:** Have you explicitly captured every compliance or integration step as a proposed `BR-`, `API-`, or `DBT-` item so architecture work isn’t surprised later?
4. **Journey Completeness:** Does each Journey Card explain the trigger, steps, and desired value sufficiently for build leads to scope EPICs?
5. **Lifecycle Continuity:** Do the lifecycle notes specify which risks the Red Team must pressure-test and which assumptions may force loopbacks if invalidated?
6. **Real-User & Device Coverage:** Have you confirmed actual users (or stand-ins) plus their primary devices for upcoming validation so the team can schedule real hardware testing early, per [CFD-401](../../../../source_of_truth/customer_feedback.md#cfd-401-partial-ghm-adoption-during-48-hour-inventory-build)?

## Research Workflow
1. **Brief Review:** Load PRD v0.3 (Commercial Model + Guardrails) and highlight assumptions that require user validation. Confirm persona list + hypotheses.
2. **Interview Planning:** Build an interview tracker listing persona, channel, scheduled date, primary device, and hypothesis focus. Ensure coverage across roles (buyer, operator, analyst) as defined in v0.2/v0.3.
3. **Device & Context Validation:** Confirm at least two participants will review flows on their actual hardware (e.g., mobile vs. desktop) so responsive and interaction insights reach AURA. Log findings inline with references to [CFD-401](../../../../source_of_truth/customer_feedback.md#cfd-401-partial-ghm-adoption-during-48-hour-inventory-build).
4. **Data Collection:** Conduct interviews or gather secondary evidence (forum posts, public talks) within the last 90 days. Record transcripts/screenshots. Capture workflow steps, emotional cues, blockers, and success definitions.
5. **Journey Mapping:** Translate insights into discrete steps (Trigger → Actions → Tools → Pains → Desired Value). Note integration requirements, metrics, and cross-team dependencies.
6. **Evidence Logging:** Store raw notes in `user-interview-{date}-{persona}.md`. Map quotes to candidate CFD- IDs (`CFD-UJ-###`) and assign a tentative UJ- ID for each Journey Card.
7. **Dependency Flagging:** Identify requirements for BR- (policies), API-/DBT- (data contracts), or TEST- IDs emerging from each journey.
8. **Handoff Assembly:** Produce Journey Cards + Persona Summaries + Evidence Ledger. Include a cross-journey matrix showing coverage vs. PRD sections.

## Output Package
### Coverage Matrix (top of submission)
| Journey ID | Persona | Trigger | Tools Today | Pain Severity | Proposed UJ- ID |
|------------|---------|---------|-------------|---------------|-----------------|

### Journey Card Template (per journey)
```
# Journey – [Persona] handles [Trigger]
🆔 **Journey ID:** [slug, e.g., `journey-lab-sample-intake`]
🪪 **Proposed UJ- ID:** `UJ-###` (placeholder until SoT entry)

## Persona Snapshot
- Role & org size
- KPI / definition of success
- Tooling maturity

## Current Journey
1. **Trigger:** [Description + evidence]
2. **Step:** [Action] → Tool → Pain → Quote (Artifact)
3. ... (3–7 steps)

## Pain & Opportunity Summary
- Pain 1 (severity, frequency)
- Pain 2 ...

## Desired Value
- Outcome statements referencing monetization hooks (from v0.3)

## Dependencies & ID Hooks
- `BR-` needs: [policy enforcement]
- `API-/DBT-` needs: [data contracts]
- `TEST-` needs: [validation tasks]

## Evidence Ledger
| CFD- ID | Source | Capture Date | Usage |
```

### Persona Reference Sheet
Provide 1-page persona outlines consolidating overlapping interviews. Include empathy map bullets and data/integration stakes.

## Research Constraints
- **Recency:** Interviews must be conducted or sourced within 90 days.
- **Verbatim Quotes:** Capture at least one direct quote per pain point with timestamp/source.
- **Step Depth:** Minimum 3 steps, maximum 7 steps per journey to keep fidelity manageable.
- **Persona Separation:** Avoid blending personas; if a journey covers multiple roles, split the steps by owner.
- **Privacy:** Redact PII but retain enough context to prove authenticity (industry, company size, etc.).
- **Hardware Reality:** Document which device type each participant used (phone, tablet, desktop). If device coverage is missing, flag it as a gap referencing [CFD-401](../../../../source_of_truth/customer_feedback.md#cfd-401-partial-ghm-adoption-during-48-hour-inventory-build).

## Quality Gates
| Criterion | Pass | Fail |
|-----------|------|------|
| **Coverage** | ≥3 journeys covering both buyer + operator personas | Single persona focus |
| **Pain Severity** | Quantified by time/cost/risk, evidence cited | Generic "it's hard" statements |
| **Dependency Insight** | BR-/API-/TEST- implications listed | No downstream hooks |
| **Traceability** | Each step cites a CFD- artifact | Missing evidence for steps |
| **Lifecycle Hook** | Calls out what v0.5 needs to challenge/test | No reference to next gate |

## Packaging for AURA
- Bundle Journey Cards and Persona Sheets in a single doc per assignment; include artifact folders labeled with Journey ID.
- Provide an index linking Journey IDs to evidence files and proposed UJ- IDs to aid SoT entry.
- Flag any conflicting insights or unresolved hypotheses requiring additional interviews.

## Reporting Checklist
- [ ] Coverage Matrix complete
- [ ] 3–7 Journey Cards authored with artifacts
- [ ] Persona reference sheets provided
- [ ] Candidate UJ-/CFD-/BR-/API- IDs listed
- [ ] Lifecycle notes for v0.5 Red Team captured
