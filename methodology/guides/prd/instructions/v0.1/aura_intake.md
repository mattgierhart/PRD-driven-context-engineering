# PRD v0.1 AURA Intake Instructions

> Part of the PRD Instruction Library (`docs/prd/instructions/`). Keep filenames and structure consistent when cloning for future PRD stages.

## Mission Alignment
**Objective:** Transform validated research idea sparks into the PRD v0.1 draft covering Problem, Users, Value Proposition, and Future Work without breaking Gear Heart Methodology (GHM) discipline.
**Inputs:** Research bundles produced with the [PRD v0.1 Research Agent Instructions](./research_agents.md). Assume facts, links, and quotes are already verified and mapped to candidate SoT IDs.
**Deliverable:** A PRD v0.1 packet per idea that is ready for cross-functional review and prioritization, including next-ID recommendations for the Source-of-Truth (SoT) library.

## Intake Checklist
Before drafting, confirm the bundle includes:
- Summary Sheet with Idea ID, Industry, Primary Pain Point, and MVP hook
- Completed Output Template (all sections populated)
- Pricing and community evidence files named `[idea-id]__[artifact-type].*`
- Hand-off note suggesting Opportunity and High-Level Solution framing + lifecycle next step (e.g., "promote to v0.2 once ICP confirmed")
- Assumptions & Open Questions enumerated
- Methodology signal showing PRD sections impacted and proposed SoT IDs

If any item is missing, flag the gap to the research lead before proceeding.

## Processing Workflow
1. **Bundle Review:** Read the Summary Sheet to select the idea(s) for drafting. Confirm the methodology signal covers PRD sections + candidate IDs, then use the `ARTIFACTS FOR AURA` references to locate supporting files.
2. **Problem Synthesis:** Extract the Primary Pain Point, demand signals, and community quotes to craft a concise Problem statement. Highlight quantified impact.
3. **User Definition:** Translate the Ideal Customer Profile into explicit user personas (roles, organization size, operational context). Note any assumptions supplied and tie each persona to eventual UJ- IDs.
4. **Value Proposition:** Combine MVP Scope and Market Validation to articulate the promised outcomes and differentiators versus competitors. Document which BR-/CFD- IDs will capture supporting rules or feedback.
5. **Future Work Hooks:** Leverage the Assumptions & Open Questions and Hand-off note to outline potential extensions, risks, and validation tasks. Identify the PRD lifecycle stage to pursue next.
6. **Traceability Tagging:** Cite Idea ID, artifact filenames, and proposed IDs inline so reviewers can jump back to evidence quickly and register new SoT cards.
7. **Review & Polish:** Ensure clarity, consistent terminology, and that no new facts are introduced without evidence from the bundle. Confirm the draft signals readiness for the v0.1 gate review.

## Output Template (per idea)
```
# [Idea ID] – PRD v0.1 Draft

## Problem
[2-3 paragraphs summarizing the workflow pain, quantified impact, and context. Include citations like (Artifact: pricing1.png).]

## Target Users
- Primary persona: [Role, organization size, workflow trigger]
- Secondary persona(s): [If applicable]
- Assumptions: [Borrowed from research; note any unresolved questions]

## Value Proposition
- Core outcome: [What success looks like for the user]
- Differentiators: [Why this solution beats competitors, referencing demand signals]
- MVP Scope Alignment: [How the MVP feature set delivers the outcome]
- SoT Hooks: [List BR-/CFD- IDs to instantiate with this draft]

## Future Work & Validation
- Near-term experiments: [Customer interviews, pilot metrics]
- Expansion ideas: [Potential next features, integrations]
- Risks & mitigation: [Gaps from Assumptions/Open Questions]
- Lifecycle Next Step: [What milestone to schedule (e.g., v0.2 Market Definition)]

## Evidence Index
| Artifact | Description | Usage in Draft |
|----------|-------------|----------------|
| [idea-id]__pricing1.png | Competitor pricing capture | Problem (market willingness to pay)
| ... | ... | ... |

## ID Register Stub
- Proposed IDs: [List candidate CFD-/BR-/UJ- entries, even if placeholders]
- Dependencies: [Cross-reference existing IDs this work touches]
```

## Quality Gates
| Checkpoint | Pass Condition |
|------------|----------------|
| **Problem Clarity** | Pain point is stated with quantifiable stakes pulled from research evidence. |
| **User Fit** | Personas mirror the Ideal Customer Profile with any assumptions explicitly tagged. |
| **Evidence Traceability** | Every claim references a linked artifact or quote and lists the supporting artifact ID/file. |
| **Scope Discipline** | MVP description sticks to features validated by research; no new scope creep. |
| **Future Work Utility** | Actionable next steps stem from Assumptions & Open Questions, not speculation, and include lifecycle planning. |
| **ID Hygiene** | Candidate SoT IDs are listed with owners or next steps for creation. |

## Handoff & Collaboration
- Store PRD drafts alongside the research bundle using the naming convention `[idea-id]__prd-v0.1.md`.
- Post a summary update highlighting key insights, flagged risks, and any additional information requests for researchers.
- If facts appear inconsistent, annotate the draft and request clarification instead of rewriting evidence.

## Reporting Checklist
- [ ] PRD draft saved with correct file name
- [ ] All sections completed using the template
- [ ] Evidence Index populated and cross-referenced
- [ ] ID Register Stub filled in and linked to SoT backlog
- [ ] Outstanding questions escalated to research lead
- [ ] Summary update shared with product stakeholders, including lifecycle recommendation
