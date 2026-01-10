---
title: "Template Purity Standard"
updated: "2026-01-10"
authority: "Context Engineering Methodology"
---

# Template Purity Standard

> **Core Principle**: Templates should be self-documenting for maintenance while remaining free of methodology teaching.

This document codifies the standard for maintaining SoT template quality discovered during Phase 1 SoT audit (2026-01-10), aligned with Context Engineering's **Just-in-Time Context** principle (README.md:117-118).

---

## 1. The Discovery

### 1.1 The Tension

During the Phase 1 SoT template audit, we identified a critical tension:

- Templates need maintenance documentation to be self-documenting
- But methodology teaching creates context bloat
- Moving ALL instructions to CLAUDE.md violates context density optimization

### 1.2 The Resolution

Two distinct content types require different placement:

- **Template Self-Documentation** stays IN the template (loaded just-in-time)
- **Methodology Teaching** moves to skill references (loaded by skills when needed)

### 1.3 The Litmus Test

When reviewing content in a SoT template, ask:

> **"Is this teaching me how to maintain the file structure, or teaching me domain knowledge about what makes good content?"**

**Decision Rule**:
- **File structure maintenance** → Keep in template (just-in-time context)
- **Domain knowledge/methodology** → Move to skill references (skill-loaded context)

---

## 2. Template Purity Categories

### 2.1 🟢 KEEP: Template Self-Documentation

**Definition**: Operational instructions for maintaining THIS specific file's structure and integrity.

**Characteristics**:
- File-specific (applies only to this template)
- Structural (about the file itself, not its content)
- Procedural (when/how to update this file)
- Maintenance-focused (preserving integrity)

**Examples** (Keep in Template):
- ✅ "When to Add New UJ-XXX IDs" - Timing for adding entries
- ✅ "Bidirectional Reference Checklist" - Structural integrity checks
- ✅ "Maintenance Protocol" for schema migrations - File update workflow
- ✅ "Update Protocol" - When/how to modify this file
- ✅ ID numbering conventions for this template type
- ✅ Cross-reference validation rules
- ✅ Required fields checklist for new entries

**Why Keep**:
- Loaded only when the template is actively being used
- Prevents context bloat in CLAUDE.md
- Self-documenting: template teaches its own maintenance
- Aligns with "Just-in-Time Context" principle

**Location Pattern**:
- Place at end of template in `## Maintenance Protocol` or `## Update Protocol` section
- Can also appear in YAML frontmatter or navigation sections if brief

---

### 2.2 🔴 MOVE: Methodology Teaching

**Definition**: Domain knowledge about what makes GOOD content for this template type.

**Characteristics**:
- Domain-specific (about the CONTENT, not the file)
- Evaluative (what makes a good vs. bad entry)
- Instructional (how to think about this type of work)
- Cross-file (affects decisions across multiple files)

**Examples** (Move to Skill References):
- ❌ "Key Learnings for GHM" - Teaches what to look for in feedback
- ❌ "What Makes a Good API Contract" - Evaluation criteria
- ❌ "Design Tool Prompts" - Example workflows for design work
- ❌ "Implementation Notes" - How to apply learnings across files
- ❌ "Best Practices" - General guidance for this domain
- ❌ Good/bad examples with pattern analysis
- ❌ "How to analyze" or "How to interpret" sections

**Why Move**:
- Skills load this context when creating/analyzing entries
- Not needed for every template read
- Prevents methodology from being scattered across templates
- Allows methodology to evolve independently from structure

**Destination Pattern**:
- `.claude/skills/[skill-name]/references/`
- Create files like:
  - `examples.md` (good/bad patterns)
  - `evaluation-criteria.md` (what makes quality content)
  - `analysis-guide.md` (how to interpret/apply)
  - `best-practices.md` (domain-specific guidance)

---

### 2.3 🟡 BORDERLINE: Template Usage Instructions

**Definition**: High-level guidance on the PURPOSE of this template.

**Characteristics**:
- Orientation (what this file is for)
- Scope (what belongs here vs. elsewhere)
- Authority (how this relates to other files)

**Decision Rule**:
- If **1-2 paragraphs** → Keep in template frontmatter or header
- If **multiple sections** → Move to README.md or SoT.README.md
- If **applies to ALL SoT files** → Move to SoT.README.md
- If **file-specific and brief** → Keep as header

**Examples**:
- 🟡 "Purpose & Context" header (1 paragraph) → Keep
- 🟡 "Authority, Template Usage, and Standards" (multi-section) → Move to SoT.README.md
- 🟡 "How This File Relates to Others" (1 paragraph) → Keep
- 🟡 "SoT File Governance" (applies to all) → Move to SoT.README.md

---

## 3. Validation Checklist

### 3.1 Template Purity (No Contamination)

After creating or updating a SoT template, verify:

- [ ] No "how to analyze" or "how to evaluate" content (methodology → skill references)
- [ ] No "best practices" or "key learnings" (domain knowledge → skill references)
- [ ] No cross-file workflows (multi-file coordination → skill references)
- [ ] No "what makes a good entry" evaluation criteria (methodology → skill references)
- [ ] Examples show FORMAT only, not instructional CONTENT

### 3.2 Template Self-Documentation (Correctly Included)

- [ ] Has "Update Protocol" or "Maintenance Protocol" section
- [ ] Documents when to add new IDs for this template type
- [ ] Includes cross-reference integrity checks
- [ ] Specifies required fields for new entries
- [ ] Self-documentation is file-specific (not generic advice)
- [ ] Self-documentation is under 20% of total file size

### 3.3 Context Efficiency

- [ ] Template can be read without loading other files
- [ ] Methodology examples are in skill references, not template
- [ ] File-specific maintenance instructions are included
- [ ] General governance is in SoT.README.md, not individual templates

---

## 4. Application Examples

### 4.1 Example: SoT.customer_feedback.md

**Before Cleanup** (Contaminated):
- Had "Key Learnings for GHM" section (methodology teaching)
- Had "Implementation Notes" (cross-file workflow)
- These violated template purity

**After Cleanup** (Pure):
- **Kept**: "Update Protocol" (when to add CFD-XXX IDs)
- **Moved**: "Key Learnings" → `.claude/skills/prd-v09-feedback-loop-setup/references/analysis-patterns.md`
- **Moved**: "Implementation Notes" → same skill reference file

**Result**: Template remains self-documenting for structure, but methodology lives where skills load it.

---

### 4.2 Example: SoT.USER_JOURNEYS.md

**Audit Finding**:
- Has "Update Protocol" (lines 178-198)
- Teaches when to add UJ-XXX IDs
- Includes bidirectional reference checklist

**Decision**: Keep (Template Self-Documentation)
- File-specific maintenance instructions
- Structural integrity checks
- Loaded just-in-time when template is in use

---

### 4.3 Example: SoT.DESIGN_BRIEF.md

**Audit Finding**:
- Has "Update Protocol" (template maintenance)
- Has "Design Tool Prompts" (example workflows)
- Has "Authority and Standards" (multi-section governance)

**Decision**: Mixed
- **Keep**: "Update Protocol" (template self-documentation)
- **Move**: "Design Tool Prompts" → `.claude/skills/prd-v04-screen-flow-definition/references/design-tool-examples.md`
- **Move**: "Authority and Standards" → `SoT.README.md` (applies to all SoT files)

---

## 5. Common Contamination Patterns

### 5.1 Pattern: Methodology Teaching (TRUE CONTAMINATION)

**Contaminated Version**:
```markdown
## How to Use This Template

When creating a new Business Rule, consider:
1. Is this rule evidence-based?
2. Does it tie to a pain point?
3. Can it be tested?

Use the following evaluation criteria...
```

**Clean Version**:
```markdown
## Update Protocol

**When to Add New BR-XXX IDs**:
- During PRD v0.2-v0.3 when defining commercial model
- When discovering constraints in user research
- When technical limitations create hard rules

**Required Fields**:
- Rule Statement (clear, testable)
- Evidence Source (CFD-XXX, API-XXX, or external)
- Enforcement (code/policy/manual)
```

**What Changed**: Removed evaluation guidance (→ skill references), kept structural maintenance.

---

### 5.2 Pattern: Cross-File Workflow Instructions (TRUE CONTAMINATION)

**Contaminated Version**:
```markdown
## Implementation Notes

After documenting customer feedback:
1. Update PRD.md section 4 if pain point is new
2. Add to CLAUDE.md if methodology needs adjustment
3. Link to relevant EPICs for implementation
```

**Clean Version**:
```markdown
## Cross-Reference Integrity

**Bidirectional Links**:
- If CFD-XXX references BR-YYY, ensure BR-YYY links back
- If CFD-XXX mentions UJ-ZZZ, validate journey includes feedback insight
- Update "Related IDs" section in both files
```

**What Changed**: Removed cross-file workflow (→ skill references), kept structural integrity checks.

---

### 5.3 Pattern: "Key Learnings" or "Best Practices" (TRUE CONTAMINATION)

**Contaminated Version**:
```markdown
## Key Learnings for Outcome Definition

1. **Revenue over vanity**: Target paying customers, not total users
2. **Leading + Lagging**: Pair actionable metrics with validation metrics
3. **Evidence-based thresholds**: No round numbers without benchmarks
```

**Clean Version**:
Template doesn't include this. Instead, it goes to:
`.claude/skills/prd-v03-outcome-definition/references/examples.md`

**What Changed**: Methodology teaching moved entirely to skill references.

---

## 6. Integration with CLAUDE.md

CLAUDE.md should reference this standard in the "Documentation Discipline" section:

```markdown
### Documentation Discipline

- **IDs**: Reference `BR-`, `UJ-`, `API-` IDs in code comments and commits.
- **SoT Updates**: Update `SoT/` files _before_ or _during_ code changes.
- **Template Purity**: Follow `SoT.TEMPLATE_PURITY_STANDARD.md`:
  - Keep template self-documentation IN templates (just-in-time context)
  - Move methodology teaching to skill references (skill-loaded context)
  - Use the litmus test: "File structure or domain knowledge?"
```

---

## 7. Maintenance of This Standard

### 7.1 When to Update This Document

- New contamination pattern discovered
- Ambiguous case needs clarification
- Methodology evolves and affects template design

### 7.2 How to Propose Changes

1. Identify pattern in actual template review
2. Document the tension (why it's unclear)
3. Apply the litmus test
4. Update this standard with new example
5. Update CLAUDE.md if execution rules change

### 7.3 Version History

| Version | Date       | Change                  | Reason                   |
| ------- | ---------- | ----------------------- | ------------------------ |
| 1.0     | 2026-01-10 | Initial standard created | Phase 1 SoT audit discovery |

---

## 8. Quick Reference Card

### 8.1 The Litmus Test

**File structure maintenance** → Keep in template
**Domain knowledge/methodology** → Move to skill references

### 8.2 KEEP in Templates

- Update protocols (when/how to modify THIS file)
- ID numbering conventions
- Cross-reference integrity checks
- Required fields checklist
- File-specific maintenance procedures

### 8.3 MOVE to Skill References

- "Key learnings" or "best practices"
- Evaluation criteria (what makes good content)
- Example workflows or prompts
- Cross-file coordination instructions
- Good/bad pattern examples

### 8.4 Context Efficiency Rule

If it's only useful when THIS template is active → Keep in template
If it's useful when CREATING content for this template → Move to skill references

---

*End of SoT.TEMPLATE_PURITY_STANDARD.md*
