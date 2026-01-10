# Phase 1: SoT Template Audit Report

**Date**: 2026-01-10
**Auditor**: Claude (via Matt's collaborator review)
**Scope**: All 10 SoT template files for methodology contamination
**Purpose**: Ensure templates provide pure structure without teaching methodology

---

## Executive Summary

**Total Files Audited**: 10
**Contamination Found**: 4 files (40%)
**Clean Templates**: 4 files (40%)
**Appropriately Instructional**: 2 files (20%)

### Key Finding

Matt's concern about `SoT.customer_feedback.md` is **valid and represents the most severe contamination** in the template library. This file contains methodology teaching ("Key Learnings for GHM") and procedural instructions that belong in skill reference files or CLAUDE.md, not in a structural template.

---

## Detailed Findings

### 🔴 SEVERE: SoT.customer_feedback.md

**Contamination Level**: Critical
**Lines Affected**: 50-56, 69-81

**Issues Identified**:

1. **Lines 50-56: "Key Learnings for GHM"**
   - Contains methodology teaching about:
     - "Specification Discipline"
     - "Real-User Loops"
     - "Mobile-First Verification"
     - "Distribution Visibility"
   - This is product development guidance, not template structure

2. **Lines 69-81: "Implementation Notes" & "Linked Instruction Updates"**
   - Procedural instructions on what to do with feedback
   - Tells agents WHERE to apply learnings (CLAUDE.md, PRD.md, etc.)
   - This is workflow instruction, not data structure

**Why It's Contamination**:
- Template should define FIELDS for storing feedback (summary, context, problem statement, etc.)
- Should NOT teach HOW to interpret or act on feedback
- Methodology belongs in skill references (e.g., `.claude/skills/prd-v09-feedback-loop-setup/references/examples.md`)

**Recommended Fix**:
- Remove "Key Learnings" section entirely
- Remove "Implementation Notes" section
- Move this content to: `.claude/skills/prd-v09-feedback-loop-setup/references/feedback-analysis.md`
- Keep only: ID, Category, Status, Summary, Context, Problem Statement, Related IDs, Decision

---

### 🟡 MODERATE: SoT.DESIGN_BRIEF.md

**Contamination Level**: Moderate
**Lines Affected**: 1-7, 242-286, 289-314, 409-429

**Issues Identified**:

1. **Lines 1-7: "Authority, Template Usage, and Standards"**
   - Explains governance and how to use the template
   - Should be in README.md or skill documentation

2. **Lines 242-286: "Design Tool Prompts"**
   - Example prompts for UX Pilot, Lovable, Figma
   - This is methodology guidance, not design specification structure
   - These examples belong in skill references

3. **Lines 289-314: "Project Timeline & Handoffs"**
   - Process/workflow instructions
   - Belongs in PRD lifecycle or skill documentation

4. **Lines 409-429: "Update Protocol"**
   - Instructions on when/how to add DES-XXX IDs
   - Process documentation, not template structure

**Why It's Contamination**:
- Design brief should define WHAT gets documented (personas, journeys, components)
- Should NOT teach WHEN or HOW to create designs
- Prompt examples are useful but belong in skill references for v0.4 stage

**Recommended Fix**:
- Remove "Authority, Template Usage, and Standards" (move to README.md)
- Move "Design Tool Prompts" to `.claude/skills/prd-v04-screen-flow-definition/references/design-tool-examples.md`
- Move "Project Timeline" to PRD.md v0.4 gate description
- Move "Update Protocol" to CLAUDE.md or skill documentation

---

### 🟢 MINOR: SoT.USER_JOURNEYS.md

**Contamination Level**: Minor
**Lines Affected**: 178-198

**Issues Identified**:

1. **Lines 178-198: "Update Protocol"**
   - "When to Add New UJ-XXX IDs"
   - "Bidirectional Reference Checklist"
   - Process instructions for maintaining the template

**Why It's Borderline**:
- This section teaches template maintenance, not user journey methodology
- Could be considered acceptable as "template self-documentation"
- However, it's still instructional rather than structural

**Recommended Fix**:
- **Option A** (Strict): Move to CLAUDE.md "Execution Rules" section
- **Option B** (Pragmatic): Keep as-is since it's template maintenance, not methodology
- **Recommended**: Option A for consistency

---

### 🟢 MINOR: SoT.ACTUAL_SCHEMA.md

**Contamination Level**: Minor
**Lines Affected**: 422-433

**Issues Identified**:

1. **Lines 422-433: "Maintenance Protocol"**
   - Instructions on creating migrations and updating schema
   - Process documentation for schema changes

**Recommended Fix**:
- Move to CLAUDE.md or skill documentation for v0.6 Technical Specification
- This is workflow instruction, not schema structure

---

### ✅ CLEAN: SoT.BUSINESS_RULES.md

**Status**: Excellent template example
**Contamination**: None

**Why It's Clean**:
- Pure structural template with field definitions
- No methodology teaching
- No procedural instructions
- Shows WHAT to document, not HOW or WHEN
- Examples within template are structural (showing format), not instructional

**Use as Reference**: This template should be the gold standard for all others

---

### ✅ CLEAN: SoT.API_CONTRACTS.md

**Status**: Clean template
**Contamination**: None

**Why It's Clean**:
- Comprehensive API specification structure
- Field definitions without methodology
- Technical examples show FORMAT, not PROCESS

---

### ✅ CLEAN: SoT.deployment_playbook.md

**Status**: Clean template
**Contamination**: None

**Why It's Clean**:
- Structural template for deployment procedures
- No process teaching beyond the template itself

---

### ✅ CLEAN: SoT.testing_playbook.md

**Status**: Clean template
**Contamination**: None

**Why It's Clean**:
- Test case structure without methodology guidance
- Coverage targets are configuration, not instruction

---

### ✅ APPROPRIATELY INSTRUCTIONAL: SoT.UNIQUE_ID_SYSTEM.md

**Status**: Correct to be instructional
**Contamination**: N/A (this file's PURPOSE is governance)

**Why It's Appropriate**:
- This file IS the methodology for ID management
- It's not a template for creating IDs; it's the rulebook for the ID system
- Governance documentation should be prescriptive

---

### ✅ APPROPRIATELY INSTRUCTIONAL: SoT.README.md

**Status**: Correct to be instructional
**Contamination**: N/A (this is a guide file)

**Why It's Appropriate**:
- Meta-documentation about the SoT directory
- Purpose is to orient users, not to be a template

---

## Contamination Patterns Identified

### Pattern 1: "How to Use This Template"
- **Found in**: SoT.customer_feedback.md, SoT.DESIGN_BRIEF.md
- **Problem**: Templates should be self-evident through structure
- **Fix**: Move usage instructions to CLAUDE.md or skill references

### Pattern 2: "What to Do with This Data"
- **Found in**: SoT.customer_feedback.md ("Implementation Notes")
- **Problem**: Templates store data; skills describe actions
- **Fix**: Move action instructions to skill reference files

### Pattern 3: "Update Protocol" Sections
- **Found in**: SoT.USER_JOURNEYS.md, SoT.DESIGN_BRIEF.md, SoT.ACTUAL_SCHEMA.md
- **Problem**: Process instructions embedded in templates
- **Fix**: Consolidate all update protocols in CLAUDE.md "Execution Rules"

### Pattern 4: "Example Prompts/Workflows"
- **Found in**: SoT.DESIGN_BRIEF.md ("Design Tool Prompts")
- **Problem**: Methodology examples masquerading as template content
- **Fix**: Move to skill references as "good examples"

---

## Product Development Perspective

### Why This Matters for Product Outcomes

1. **Agent Confusion**: When templates teach methodology, agents don't know whether they're filling out a form or following instructions
2. **Skill Redundancy**: If templates contain methodology, skills can't evolve independently
3. **Context Bloating**: Methodology in templates means every template read loads unnecessary context
4. **Maintenance Burden**: Changes to methodology require updating multiple templates instead of single skill references

### Best Practice from Product Work

In mature product orgs, templates are like database schemas—they define structure. Documentation teaches usage. When these blur:
- Forms become documentation (bad UX)
- Documentation becomes data (hard to maintain)
- Systems resist change (technical debt)

The same applies here: **Templates are the schema for the knowledge graph. Skills are the documentation for using that schema.**

---

## Recommendations

### Priority 1: Fix Severe Contamination

**File**: `SoT.customer_feedback.md`

**Actions**:
1. Remove lines 50-56 ("Key Learnings for GHM")
2. Remove lines 69-81 ("Implementation Notes" and "Linked Instruction Updates")
3. Create `.claude/skills/prd-v09-feedback-loop-setup/references/feedback-analysis-patterns.md`
4. Move removed content to new reference file with examples

**Rationale**: This is Matt's primary concern and represents the clearest violation of template principles

### Priority 2: Fix Moderate Contamination

**File**: `SoT.DESIGN_BRIEF.md`

**Actions**:
1. Remove "Authority, Template Usage" header (move to README.md)
2. Extract "Design Tool Prompts" to `.claude/skills/prd-v04-screen-flow-definition/references/design-tool-examples.md`
3. Remove "Project Timeline" (move to PRD.md v0.4 gate)
4. Move "Update Protocol" to CLAUDE.md

### Priority 3: Fix Minor Contamination

**Files**: `SoT.USER_JOURNEYS.md`, `SoT.ACTUAL_SCHEMA.md`

**Actions**:
1. Consolidate all "Update Protocol" sections into CLAUDE.md under "Documentation Discipline"
2. Create single section in CLAUDE.md: "SoT Maintenance Protocols"
3. Remove from individual templates

### Priority 4: Document the Standard

**Action**: Add section to CLAUDE.md

```markdown
## Template Purity Standard

SoT templates MUST contain only:
1. YAML frontmatter (metadata)
2. Field definitions and structure
3. ID navigation and cross-references
4. Example FORMAT (not example CONTENT that teaches)

Templates MUST NOT contain:
1. "How to use this template" instructions
2. "When to create IDs" decision trees
3. "What to do with this data" workflows
4. Methodology teaching or best practices

Rule: If it teaches HOW or WHEN, it belongs in CLAUDE.md or skill references.
If it defines WHAT or WHERE, it belongs in the template.
```

---

## Validation Checklist

After fixes, each template should pass:

- [ ] No "How to" instructions for using the template
- [ ] No "When to" decision criteria for creating entries
- [ ] No "What to do next" workflow instructions
- [ ] No methodology teaching or best practices
- [ ] Only structural elements (fields, IDs, cross-references)
- [ ] Examples show FORMAT only, not instructional content
- [ ] Can be understood by reading field names alone

---

## Next Steps

1. **Review this audit** with Matt's collaborator
2. **Prioritize fixes** based on severity
3. **Create extraction plan** for moving contaminated content to appropriate locations
4. **Execute cleanup** on templates
5. **Validate** that extracted content lands in correct skill references
6. **Document** the template purity standard in CLAUDE.md

---

## Appendix: Template Purity Examples

### ❌ Contaminated Template

```markdown
## CFD-001: Customer Feedback Entry

### Key Learnings
This feedback shows we need better mobile testing.
We should update CLAUDE.md to emphasize device validation.

### Implementation Notes
- Update PRD.md section 4
- Add to EPIC checklist
```

### ✅ Pure Template

```markdown
## CFD-001: Customer Feedback Entry

**ID**: CFD-001
**Category**: General Comment
**Status**: Analyzed
**Priority**: Medium

### Feedback Summary
{What the user said}

### Problem Statement
{What needs to change}

### Related IDs
- Referenced in PRD: {section}
- Addressed by EPICs: {EPIC-XX}
```

The pure template defines STRUCTURE. The contaminated template teaches METHODOLOGY.

---

**End of Audit Report**
