# Phase 1: SoT Template Audit Report

**Date**: 2026-01-10
**Last Updated**: 2026-01-10 (Revised after context efficiency discussion)
**Auditor**: Claude (via Matt's collaborator review)
**Scope**: All 10 SoT template files for methodology contamination
**Purpose**: Ensure templates provide pure structure without teaching methodology

---

## Critical Discovery: The Template Self-Documentation Principle

**Initial Concern**: All instructional content in templates was flagged as contamination.

**Refinement**: During review, we identified a critical distinction aligned with Context Engineering's **Just-in-Time Context** principle (README.md:117-118):

- **Template Self-Documentation** (KEEP): Operational instructions for maintaining the file structure
  - Loaded only when template is in use (just-in-time context)
  - Example: "Update Protocol" - when/how to add IDs to this specific file

- **Methodology Teaching** (MOVE): Domain knowledge about what makes good content
  - Should be loaded by skills when creating entries (skill-loaded context)
  - Example: "Key Learnings" - evaluation criteria for feedback analysis

**Impact**: This distinction prevents context bloat in CLAUDE.md while preserving template self-documentation.

**Documentation**: See `SoT.TEMPLATE_PURITY_STANDARD.md` for the full standard.

---

## Executive Summary

**Total Files Audited**: 10
**True Contamination Found**: 2 files (20%)
**Template Self-Documentation (Correct)**: 5 files (50%)
**Clean Templates**: 1 file (10%)
**Appropriately Instructional**: 2 files (20%)

### Key Finding

Matt's concern about `SoT.customer_feedback.md` is **valid and represents the most severe contamination** in the template library. This file contains methodology teaching ("Key Learnings for GHM") and cross-file workflow instructions that belong in skill reference files, not in a structural template.

However, "Update Protocol" sections in other templates are **correctly placed** as template self-documentation.

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

### 🟡 MIXED: SoT.DESIGN_BRIEF.md

**Contamination Level**: Moderate (Mixed Content)
**Lines Affected**: 1-7, 242-286, 289-314, 409-429

**Content Identified**:

1. **Lines 1-7: "Authority, Template Usage, and Standards"**
   - Multi-section governance documentation
   - Applies to all SoT files, not just design brief

2. **Lines 242-286: "Design Tool Prompts"**
   - Example prompts for UX Pilot, Lovable, Figma
   - Methodology guidance for using design tools
   - These are workflow examples, not template structure

3. **Lines 289-314: "Project Timeline & Handoffs"**
   - Process/workflow instructions across PRD lifecycle
   - Belongs in PRD lifecycle or skill documentation

4. **Lines 409-429: "Update Protocol"**
   - Instructions on when/how to add DES-XXX IDs
   - Template maintenance for this specific file

**Revised Assessment**:

✅ **KEEP** (Template Self-Documentation):
- Lines 409-429: "Update Protocol" - File-specific maintenance

🔴 **MOVE** (Methodology Teaching):
- Lines 1-7: "Authority, Template Usage, and Standards" → `SoT.README.md` (applies to all SoT files)
- Lines 242-286: "Design Tool Prompts" → `.claude/skills/prd-v04-screen-flow-definition/references/design-tool-examples.md`
- Lines 289-314: "Project Timeline" → PRD.md v0.4 gate description

**Why**:
- "Update Protocol" is file-specific maintenance (template self-documentation)
- "Design Tool Prompts" are methodology examples (skill reference material)
- "Authority and Standards" are general governance (belongs in SoT.README.md)

---

### ✅ CORRECT: SoT.USER_JOURNEYS.md

**Contamination Level**: None (Template Self-Documentation)
**Lines Affected**: 178-198

**Content Identified**:

1. **Lines 178-198: "Update Protocol"**
   - "When to Add New UJ-XXX IDs"
   - "Bidirectional Reference Checklist"
   - Process instructions for maintaining the template structure

**Why It's Correct** (Revised Assessment):
- This is **template self-documentation**, not methodology teaching
- Loaded only when the UJ template is actively in use (just-in-time context)
- File-specific maintenance instructions (not generic advice)
- Teaches HOW to maintain file structure, not WHAT makes a good user journey

**Alignment with Context Efficiency**:
- Keeping this in the template prevents loading it in every session via CLAUDE.md
- Follows "Just-in-Time Context" principle
- Self-documenting template pattern

**Recommended Action**: **Keep as-is**

---

### ✅ CORRECT: SoT.ACTUAL_SCHEMA.md

**Contamination Level**: None (Template Self-Documentation)
**Lines Affected**: 422-433

**Content Identified**:

1. **Lines 422-433: "Maintenance Protocol"**
   - Instructions on creating migrations and updating schema
   - Process documentation for schema changes specific to this file

**Why It's Correct** (Revised Assessment):
- This is **template self-documentation** for database schema maintenance
- File-specific workflow (how to keep schema in sync with migrations)
- Loaded only when working with schema documentation
- Teaches HOW to maintain this file, not WHAT makes a good schema design

**Alignment with Context Efficiency**:
- Schema maintenance workflow is only relevant when updating DBT-XXX entries
- Loading this in CLAUDE.md would bloat context for non-schema work
- Just-in-time loading when template is active

**Recommended Action**: **Keep as-is**

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

### Pattern 1: Methodology Teaching (TRUE CONTAMINATION)
- **Found in**: SoT.customer_feedback.md ("Key Learnings for GHM")
- **Problem**: Teaches WHAT to look for in feedback (domain knowledge)
- **Why it's contamination**: This is loaded every time template is read, but only useful when creating entries
- **Fix**: Move to `.claude/skills/prd-v09-feedback-loop-setup/references/analysis-patterns.md`

### Pattern 2: Cross-File Workflow Instructions (TRUE CONTAMINATION)
- **Found in**: SoT.customer_feedback.md ("Implementation Notes")
- **Problem**: Tells agents what to do with feedback across multiple files
- **Why it's contamination**: This is skill-level coordination, not template structure
- **Fix**: Move to skill reference files

### Pattern 3: "Example Prompts/Workflows" (TRUE CONTAMINATION)
- **Found in**: SoT.DESIGN_BRIEF.md ("Design Tool Prompts")
- **Problem**: Methodology examples for using design tools
- **Why it's contamination**: These are workflow examples, not template structure
- **Fix**: Move to `.claude/skills/prd-v04-screen-flow-definition/references/design-tool-examples.md`

### Pattern 4: General Governance (MISPLACED, NOT CONTAMINATION)
- **Found in**: SoT.DESIGN_BRIEF.md ("Authority, Template Usage, and Standards")
- **Problem**: Applies to all SoT files, not just design brief
- **Why it's misplaced**: Not contamination per se, just wrong location
- **Fix**: Move to `SoT.README.md` (applies to all SoT files)

### Pattern 5: "Update Protocol" Sections (CORRECT PLACEMENT - NOT CONTAMINATION)
- **Found in**: SoT.USER_JOURNEYS.md, SoT.DESIGN_BRIEF.md, SoT.ACTUAL_SCHEMA.md
- **Initial assessment**: Flagged as contamination
- **Revised assessment**: This is **template self-documentation** (correct placement)
- **Why it's correct**: File-specific maintenance loaded just-in-time when template is active
- **Action**: Keep in templates

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

## Revised Recommendations

### Priority 1: Fix Severe Contamination

**File**: `SoT.customer_feedback.md`

**Actions**:
1. Remove lines 50-56 ("Key Learnings for GHM")
2. Remove lines 69-81 ("Implementation Notes" and "Linked Instruction Updates")
3. Create `.claude/skills/prd-v09-feedback-loop-setup/references/feedback-analysis-patterns.md`
4. Move removed content to new reference file with examples

**Rationale**: This is Matt's primary concern and represents the clearest violation of template principles

**Impact**: Removes methodology teaching while preserving template structure

---

### Priority 2: Fix Moderate Contamination

**File**: `SoT.DESIGN_BRIEF.md`

**Actions**:
1. Remove "Authority, Template Usage" header (move to `SoT.README.md`)
2. Extract "Design Tool Prompts" (lines 242-286) to `.claude/skills/prd-v04-screen-flow-definition/references/design-tool-examples.md`
3. Move "Project Timeline" (lines 289-314) to PRD.md v0.4 gate description
4. **KEEP "Update Protocol" (lines 409-429)** - This is correct template self-documentation

**Rationale**: Separate methodology examples from template structure while preserving self-documentation

**Impact**: Template becomes pure structure with file-specific maintenance instructions

---

### Priority 3: Document the Standard

**Action**: Create `SoT.TEMPLATE_PURITY_STANDARD.md` (COMPLETED)

**Rationale**: Codify the distinction between template self-documentation and methodology teaching

**Impact**: Provides reference for future template creation and maintenance

---

### Priority 4: Update CLAUDE.md with Standard Reference

**Action**: Add reference to template purity standard in CLAUDE.md

**Location**: "Documentation Discipline" section

**Content**:
```markdown
### Documentation Discipline

- **IDs**: Reference `BR-`, `UJ-`, `API-` IDs in code comments and commits.
- **SoT Updates**: Update `SoT/` files _before_ or _during_ code changes.
- **Template Purity**: Follow `SoT.TEMPLATE_PURITY_STANDARD.md`:
  - Keep template self-documentation IN templates (just-in-time context)
  - Move methodology teaching to skill references (skill-loaded context)
  - Use the litmus test: "File structure or domain knowledge?"
```

**Rationale**: Ensure agents understand the standard without loading full details

**Impact**: Maintains context efficiency while referencing comprehensive standard

---

## Revised Validation Checklist

After fixes, each template should pass:

### Template Purity (No Contamination)
- [ ] No methodology teaching (e.g., "Key Learnings", "Best Practices")
- [ ] No "what makes a good entry" evaluation criteria
- [ ] No cross-file workflow instructions (e.g., "Update PRD.md when...")
- [ ] No example prompts/workflows for domain work
- [ ] Examples show FORMAT only, not instructional CONTENT

### Template Self-Documentation (Correctly Included)
- [ ] Has "Update Protocol" or "Maintenance Protocol" section
- [ ] Documents when to add new IDs for this template type
- [ ] Includes cross-reference integrity checks (bidirectional links)
- [ ] Specifies required fields for new entries
- [ ] Self-documentation is file-specific (not generic)
- [ ] Self-documentation is under 20% of total file size

### Context Efficiency
- [ ] Template can be understood without loading skill references
- [ ] Methodology examples are referenced, not embedded
- [ ] File-specific maintenance instructions are included
- [ ] General governance is in SoT.README.md, not individual templates

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
