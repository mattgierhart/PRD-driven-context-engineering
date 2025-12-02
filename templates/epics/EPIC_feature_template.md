---
version: 1.3
purpose: To outline the strategic context, design integration, technical approach, and implementation plan for a new product feature.
summary: Added progressive documentation features, model-specific guidance, and testing-first approach.
last_updated: 2025-07-06
epic_id: EPIC-XX
epic_name: "{Feature Name}"
epic_type: "feature"
status: "planning"
model_restrictions: "none"
---

# EPIC-{NUMBER}: {Feature Name} v{0.1}

## Epic Meta Information
| Field | Value |
|-------|-------|
| **Current Version** | v0.1 |
| **Planning Version** | v0.1-0.3 (Opus) |
| **Execution Version** | v0.4+ (Sonnet) |
| **Last Updated** | [Date and Time] |
| **Last Editor** | [Model/User] |
| **Status** | Planning Phase |
| **Completion** | 0% |

## Version History
| Version | Date | Editor | Changes |
|---------|------|--------|---------|
| v0.1 | [Date] | [Editor] | Initial epic structure |

## Quick Navigation
- [Strategic Context](#strategic-context)
- [Design Integration](#design-integration)
- [Technical Approach](#technical-approach)
- [Testing Strategy](#testing-strategy)
- [Implementation Plan](#implementation-plan)
- [Progress Log](#progress-log)
- [Handoff History](#handoff-history)

**Authority**: See [WORKFLOW_MASTER.md](../workflows/WORKFLOW_MASTER.md) for complete workflow processes  
**Template Usage**: See [README.md](./README.md) for template usage guide  
**Standards**: See [STANDARDS.md](../../STANDARDS.md) for documentation hierarchy

## Strategic Context (AURA) {#strategic-context}
- Market Need: 
- User Story: As a [user], I want [goal] so that [benefit]
- Success Metrics:
- Priority: [Critical/High/Medium]

## Design Integration (Product Designer Agent) {#design-integration}
- Design Brief Status: [Complete/In Progress/Not Started]
- User Journey Map: [Link to design file or brief description]
- Design Tool Integration: [UX Pilot/Lovable/Figma export status]
- Design System Compliance: [Components and patterns to follow]
- Design Validation: [Key UX considerations and constraints]

## Technical Approach (APOLLO) {#technical-approach}
<!-- Model: opus-required for architecture decisions -->
For the recommended technology stack and architectural principles, refer to the [TECH_STACK_BLUEPRINT.md](../../tools/tech-stack/TECH_STACK_BLUEPRINT.md).
- Architecture Decision:
- Technology Choices: [Refer to TECH_STACK_BLUEPRINT.md]
- Risk Assessment:
- Effort Estimate: [X context windows]

## Testing Strategy {#testing-strategy}
<!-- Model: opus for strategy, sonnet for implementation -->

### Test Planning (v0.2)
**Acceptance Criteria**:
- [ ] [Testable criterion 1]
- [ ] [Testable criterion 2]
- [ ] [Testable criterion 3]

**Test Scenarios**:
1. **Happy Path**: [Description]
2. **Edge Case 1**: [Description]
3. **Error Case 1**: [Description]

**Test Data Requirements**:
- [Data set 1]
- [Data set 2]

**Coverage Targets**:
- Unit Tests: 80%+
- Integration Tests: Critical paths
- E2E Tests: User journeys

## Implementation Plan (Claude Code) {#implementation-plan}

### Detailed Development Plan

---

#### Task [ID] - [Task Title]

*   **Status:** `To Do` | `In Progress` | `Done` | `Blocked` | `blocked-for-opus` | `blocked-for-user`
*   **Model Suitability:** `opus-only` | `sonnet-ready` | `either`
*   **User Action Required:** [If blocked-for-user, specify what's needed: API key, business decision, design approval, etc.]
*   **Context:** A brief explanation of *why* this task is necessary, referencing specific audit documents, user stories, or business requirements.
*   **Action Plan:** A clear, high-level description of *what* needs to be done. This serves as the primary instruction for the developer (Claude).
*   **Test First Approach:**
    *   **Tests to Write:** [List specific test files/cases to create before implementation]
    *   **Expected Behavior:** [Define what success looks like]
*   **Implementation Notes:** *(To be filled out by the developer during/after implementation)*
    *   A detailed log of *how* the task was accomplished. This is crucial for documentation and review.
    *   Should include:
        *   Files created or modified.
        *   Key functions, classes, or logic that were added or changed.
        *   Important commands run.
        *   Architectural or implementation decisions made.
    *   **Blockers Encountered:** [If status is blocked-for-opus, detail the issue]
*   **Validation:**
    *   Clear, objective criteria to confirm the task is complete and correct.
    *   Should include:
        *   Specific tests to run (e.g., `npm run test -- src/lib/__tests__/auth.test.ts`).
        *   Expected outcomes (e.g., "All tests must pass," "Lighthouse score for performance must be > 90").
        *   If applicable, manual verification steps.

---


## Progress Log
<!-- APPEND new entries, don't replace -->
- [Date]: Started implementation
- [Date]: Feature A complete, tests passing

## Handoff History {#handoff-history}
<!-- Track model transitions and blockers -->

<!-- HANDOFF: From [Model] to [Model] - [Date] -->
<!-- Summary of what was completed and what needs attention -->
<!-- END HANDOFF -->

## Gemini's Development Considerations
<!-- This section will be added by Gemini during review -->
<!-- Do not edit this section unless you are Gemini -->