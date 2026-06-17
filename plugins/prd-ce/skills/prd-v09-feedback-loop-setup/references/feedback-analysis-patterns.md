# Feedback Analysis Patterns

> **Purpose**: Methodology guidance for analyzing customer feedback and translating insights into actionable improvements.
> **Source**: Extracted from SoT.customer_feedback.md during Phase 1 template purity cleanup (2026-01-10)
> **Use When**: Creating or analyzing CFD-XXX entries to ensure high-quality insights

---

## Key Learnings from Field Feedback

### Pattern 1: Specification Discipline

**What to Look For**: Feedback indicating AI produced poor quality or misaligned code.

**Root Cause**: Prompt quality is proportional to the clarity of SoT-backed requirements.

**Action**:
- Reinforce that builders translate user needs into explicit acceptance criteria BEFORE delegating to AI
- Link prompts to specific BR-XXX, UJ-XXX, or API-XXX entries
- Quick reminders in EPIC checklists to ground prompts in Source of Truth

**Evidence**:
- CFD-XXX: "AI produced quality code only when prompts were highly specific"

---

### Pattern 2: Real-User Loops

**What to Look For**: Feedback about scope bloat, overbuilding, or features users don't need.

**Root Cause**: Testing with assumptions instead of actual users prevents focus.

**Action**:
- Encourage immediate testing with actual users (even one person)
- Make feedback loops visible in EPIC checklists
- Don't wait for "complete" features before getting user input

**Evidence**:
- CFD-XXX: "Real-time feedback from target user prevented scope bloat"

---

### Pattern 3: Mobile-First Verification

**What to Look For**: Feedback about late-stage mobile layout issues, costly rework on responsive designs.

**Root Cause**: Relying on responsive previews instead of testing on real devices.

**Action**:
- Promote early validation on real devices (not just browser DevTools)
- Add device-specific testing to TEST-XXX entries
- Include mobile validation in UJ-XXX user journey definitions
- Test on actual phones/tablets, not simulators

**Evidence**:
- CFD-XXX: "Late mobile testing caused costly rework"

---

### Pattern 4: Distribution Visibility

**What to Look For**: Feedback about struggling with launch, finding users, or monetization after code is complete.

**Root Cause**: GTM/distribution tasks are treated as "later" instead of parallel to build work.

**Action**:
- Highlight that launch tasks (audience building, pricing experiments) must appear in planning artifacts
- Don't stop at "code complete" - build distribution plan alongside features
- Make GTM work visible in PRD v0.9 and EPIC checklists
- Consider distribution from v0.1-v0.2 (not just at the end)

**Evidence**:
- CFD-XXX: "Distribution remained the hardest part after launch"

---

## Implementation Patterns

### When to Update Cross-File Artifacts

After analyzing feedback and identifying actionable insights, consider updates to:

**CLAUDE.md** - Execution Rules:
- Use when feedback reveals systematic process gaps
- Example: Add guidance on SoT-grounded prompts, early mobile testing
- When: Patterns emerge across multiple CFD entries

**PRD.md** - Lifecycle Gates:
- Use when feedback shows missing validation criteria
- Example: Reflect mobile validation in v0.4 gates, distribution readiness in v0.9
- When: Gate criteria should have caught the issue

**epics/EPIC_TEMPLATE.md** - Execution Checklists:
- Use when feedback reveals missing checkpoints during execution
- Example: Add real-user loop reminders, mobile-first validation steps
- When: Pattern would prevent similar issues in future EPICs

**SoT.USER_JOURNEYS.md** - UJ-XXX Entries:
- Use when feedback reveals journey-specific validation needs
- Example: Capture mobile-specific steps in affected user journeys
- When: Journey definitions should include device considerations

**SoT.TESTING.md** - TEST-XXX Entries:
- Use when feedback shows gaps in test coverage
- Example: Add device validation tests tied to UJ-XXX entries
- When: Tests should have caught the issue before deployment

---

## Anti-Patterns

### ❌ Anti-Pattern: Methodology in CFD Template

**Wrong**:
```markdown
### Key Learnings for GHM
1. **Specification Discipline** — [explanation]
2. **Real-User Loops** — [explanation]
```

**Problem**: This teaches methodology in the template itself, creating context bloat.

**Right**: Extract to this skill reference file, reference it when analyzing feedback.

---

### ❌ Anti-Pattern: Cross-File Workflow in CFD Template

**Wrong**:
```markdown
### Implementation Notes
- Update CLAUDE.md execution rules...
- Add distribution reminders to planning workflows...
```

**Problem**: This is cross-file coordination (skill-level work), not template structure.

**Right**: Use this patterns file to guide analysis, document decisions in CFD "Product Decision" field.

---

### ❌ Anti-Pattern: Prescriptive File Updates

**Wrong**:
```markdown
### Linked Instruction Updates
- `../PRD.md` — reflect X in gates Y
- `../epics/EPIC_TEMPLATE.md` — add Z to checklists
```

**Problem**: Template shouldn't prescribe specific file edits; that's implementation work.

**Right**: Document the decision and rationale in CFD; let EPIC or separate work item handle updates.

---

## Good Pattern: Structured Analysis

### ✅ Correct CFD Structure

```markdown
### Feedback Summary
**What Users Said**: [Direct quote or paraphrase]
**User Context**: [Tier, segment, platform, etc.]

### Problem Statement
**Current Behavior**: [What's happening]
**Expected Behavior**: [What should happen]
**Impact**: [Why it matters]
**Pain Level**: [High/Medium/Low with context]

### Related IDs
- Referenced in PRD: [Where this ties to product strategy]
- Addressed by EPICs: [Work items to implement]

### Product Decision
**Decision**: [What we're doing about it]
**Decision Date**: YYYY-MM-DD
**Decision Maker**: [Who decided]
**Rationale**: [Why this decision]
```

**Why This Works**:
- Captures WHAT was learned (data structure)
- Doesn't prescribe HOW to apply learnings (methodology)
- Links to other IDs for traceability
- Documents decisions without cross-file workflows

---

## Usage Guide

### When Creating New CFD Entries

1. **Capture the raw feedback** in "Feedback Summary"
2. **Translate to problem statement** (current vs. expected behavior)
3. **Assess pain level** based on impact
4. **Look for patterns** using this reference file
5. **Document decision** in "Product Decision" field
6. **Link to related work** in "Related IDs"
7. **Do NOT embed methodology** in the CFD entry itself

### When Analyzing Existing CFD Entries

1. **Read multiple CFD entries** looking for patterns
2. **Reference this file** to identify known patterns
3. **Propose systemic fixes** (not one-off patches)
4. **Create EPIC or update artifacts** based on patterns
5. **Update this patterns file** if new patterns emerge

---

## Pattern Evolution

As more CFD entries accumulate, this file should grow to include:
- New patterns discovered in field feedback
- Specific examples from CFD-XXX entries
- Anti-patterns to avoid
- Decision frameworks for common scenarios

**Maintenance Rule**: When 3+ CFD entries show the same pattern, codify it here.

---

*End of feedback-analysis-patterns.md - Reference for prd-v09-feedback-loop-setup skill*
