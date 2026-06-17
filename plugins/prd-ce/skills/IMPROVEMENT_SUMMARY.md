# Skills Improvement Summary

**Period**: 2026-02-26
**Context**: CPO-level principles interview revealed skills lack connective tissue and confidence tracking. This document summarizes what was improved and the pattern for remaining work.

---

## Changes Made (Completed)

### 1. Created PRINCIPLES.md (.claude/skills/PRINCIPLES.md)

**Purpose**: North star reference document defining 6 core CPO principles that govern all skills.

**P1 & P4 (Must-Have)**:
- **P1: MVP is Sacred** — 0→1 methodology only; quality+speed balance, not velocity-first
- **P4: SoT is Living Evidence** — IDs track confidence (1-5) + evidence source; enables readiness assessment

**P2-P6 (High Priority)**:
- P2: Quality + Speed trade-off framework
- P3: Research drives scope — MVP definition must be explicit artifact
- P5: Distributed development needs connective tissue
- P6: Reuse-first, ask early about existing assets

**Confidence Model**: Detailed per-SoT-type progressions (CFD, FEA, TECH, DEP, API, ARC, RISK, etc.)

**Connective Tissue Standard**: Consumes / Produces format for all skills.

---

### 2. Updated ghm-id-register (SoT ID Entry Creation)

**Changes**:
- Added Step 3.5: "Evaluate Confidence" before registering any ID
- Updated entry template to include:
  - `Confidence: [1-5]/5 (source: [evidence source])`
  - `Next Confidence Target: [What would move this to next level]`
- Added confidence examples in all SoT types (CFD, FEA, TECH, DEP, etc.)
- Updated Quality Gates to include confidence assessment
- Added anti-patterns for inflated/missing confidence

**Impact**: All downstream skills now have a "confidence question" built into ID creation.

---

### 3. Updated prd-v01-problem-framing (Discovery)

**Changes**:
- Added **Consumes** section: clarifies this is the starting skill (no prior research needed)
- Added **Produces** section: explicitly lists CFD-* outputs + confidence requirements
- Updated Step 2 (Evidence Anchoring) with:
  - Confidence scoring model (1-5, pre-product)
  - Example CFD entry showing confidence annotation
  - Forward target path ("Would move to 3/5 if...")
- Strengthened research-first language throughout

**Impact**: v0.1 now explicitly tracks evidence strength as the first skill in the workflow.

---

### 4. Updated prd-v03-features-value-planning (Commercial)

**Changes**:
- Added **Consumes** section: explicitly lists CFD-, KPI-, BR- entries needed as inputs
- Added **Produces** section: features (FEA-*), governance rules (BR-FEA-*), **MVP-SCOPE artifact**
- Made **MVP-SCOPE explicit**: "These X features define our MVP"
  - Example format: `MVP-SCOPE: 5 P0 features + 3 P1 features = 8 total`
- Updated Downstream Connections table to clarify what v0.4+ consumes
- All FEA- examples include confidence scoring

**Impact**: v0.3 now makes MVP scope definition a visible, auditable decision point that gates v0.4+ work.

---

## Pattern for Remaining 22 Skills

All 22 remaining domain skills should follow this improvement pattern:

### Universal Changes (Apply to All Skills)

**1. Add Consumes / Produces sections**

After "Workflow Overview", add:

```markdown
## Consumes

This skill requires:
- **[ID-TYPE]**: [What entries needed from prior skills]
- **[ID-TYPE]**: [What entries needed]

Example: "CFD-* entries from v0.1-v0.2 research"

## Produces

This skill creates/updates:
- **[ID-TYPE]**: [What this skill outputs, with confidence requirements]
- **[ID-TYPE]**: [Other outputs]

Example: "FEA-* entries at confidence 2-3/5 (based on customer feedback evidence)"
```

**2. Add confidence examples to output templates**

For any SoT ID created by the skill, show example with confidence:

```markdown
### Example entry with confidence:
[ID]-###: [Description]
Confidence: [N]/5 (source: [evidence])
Next Target: [What would move to next level]
```

**3. Reference PRINCIPLES.md for SoT confidence models**

Point users to `.claude/skills/PRINCIPLES.md` for per-type confidence progressions.

### Skill-Specific Improvements

| Gate | Skills | Priority Changes |
|------|--------|------------------|
| **v0.1** | problem-framing ✅, user-value-articulation | Strengthen research interrogation; make evidence tier explicit in outputs |
| **v0.2** | competitive-landscape-mapping, product-type-classification | Add Consumes/Produces; CFD examples with confidence |
| **v0.3** | moat-definition, outcome-definition, pricing-model | Add Consumes/Produces; make MVP scope implications explicit |
| **v0.4** | persona-definition, user-journey-mapping, screen-flow-definition | Add Consumes/Produces; reference MVP-SCOPE from v0.3 as boundary |
| **v0.5** | risk-discovery-interview, tech-stack-selection | Add Consumes/Produces; reference MVP-SCOPE; assess risk/tech feasibility within MVP |
| **v0.6** | architecture-design, environment-setup, technical-specification | Add Consumes/Produces; confidence scoring for TECH-, API-, ARC-, DBT- entries |
| **v0.7** | epic-scoping, implementation-loop, test-planning | Add Consumes/Produces; strengthen connective tissue between EPIC phases; TEST- confidence |
| **v0.8** | release-planning, monitoring-setup, runbook-creation | Add Consumes/Produces; DEP-, MON-, RUN- confidence progressions |
| **v0.9** | gtm-strategy, feedback-loop-setup, launch-metrics | Add Consumes/Produces; CFD feedback confidence tracking post-launch |

---

## How to Verify Improvements

### For Individual Skills

1. **Can a fresh context window use this skill?**
   - Read the Consumes section: can you find all required SoT entries?
   - Read the Produces section: will the output be usable by downstream skills?

2. **Do outputs include confidence?**
   - Examples show confidence scores (1-5) + source + forward target
   - Anti-patterns include "inflated confidence" and "missing source"

3. **Is MVP scope clear?**
   - Discovery/commercial skills (v0.1-v0.3) make MVP scope signals explicit
   - Execution skills (v0.7-v0.8) reference MVP scope as their boundary

### Workflow Integration Test

Trace a mock product through v0.1 → v0.3 → v0.7:

1. **v0.1 output**: CFD-001, CFD-002 (confidence: 3/5, source: customer-interviews)
2. **v0.3 output**: FEA-001–008, MVP-SCOPE artifact (5 features + 3 nice-to-have)
3. **v0.7 output**: EPICs aligned to MVP-SCOPE, each EPIC with TEST-* entries (confidence builds as implementation progresses)

At each handoff, the downstream skill should be able to read the upstream output and proceed without rework.

---

## Consolidation Decision (Issue #54)

**Current Status**: 25 skills remain separate. **Consolidation deferred pending outcome of improvements.**

**Decision Framework**:

After all 25 skills are improved with Consumes/Produces connective tissue:

1. **If connective tissue makes workflows clear** → Skills stay separate (lower discovery overhead, modular)
2. **If connective tissue reveals tight coupling** → Consolidate gate-skills (e.g., v0.3 features + moat + outcomes + pricing as one workflow)

**Current observation**: v0.3 (features + moat + outcomes + pricing) appears tightly coupled. May benefit from being one gate-skill: `prd-commercial`. But this decision should happen **after** connective tissue makes dependencies explicit.

---

## Next Steps

**Phase 1 (Remaining)**: Apply Consumes/Produces pattern to 22 skills
- Time estimate: 8-12 hours (systematic updates, same pattern)
- High-impact skills first (v0.2, v0.5, v0.6, v0.7)

**Phase 2**: Test workflow integration end-to-end
- Trace mock product through v0.1 → v0.9
- Verify outputs flow cleanly between skill handoffs
- Surface any broken connective tissue

**Phase 3**: Consolidation decision
- Re-evaluate Issue #54 with full picture of improved skills
- Decide: keep 25 separate or merge into gate-skills

---

## Files Modified

| File | Changes |
|------|---------|
| `.claude/skills/PRINCIPLES.md` | **Created** — 6 principles + confidence model + audit checklist |
| `.claude/skills/ghm-id-register/SKILL.md` | **Updated** — Add confidence scoring step + examples |
| `.claude/skills/prd-v01-problem-framing/SKILL.md` | **Updated** — Add Consumes/Produces, confidence examples, research emphasis |
| `.claude/skills/prd-v03-features-value-planning/SKILL.md` | **Updated** — Add Consumes/Produces, MVP-SCOPE artifact, confidence examples |

---

## User Decisions (Locked)

✅ **Decision 1: Confidence Scoring** → **Optional**
- Confidence is an input point in the development process; let it evolve through usage before making it mandatory
- Anti-patterns flag missing/inflated confidence, but won't gate advancement

✅ **Decision 2: MVP-SCOPE Artifact Location** → **PRD.md**
- MVP-SCOPE lives in PRD.md, referenced from v0.4+ as the boundary between in-scope and post-launch backlog
- Note: Individual unique IDs can include an optional property flag ("impacts_mvp: true/false") if needed for filtering

✅ **Decision 3: Consolidation Timing** → **Complete Phase 2 First**
- Finish all 22 skills updates with Consumes/Produces pattern
- Then evaluate consolidation based on full picture of improved skills
- Trust the analysis and process over initial gut instinct

