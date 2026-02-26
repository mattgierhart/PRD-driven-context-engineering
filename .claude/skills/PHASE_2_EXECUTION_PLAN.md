# Phase 2 Execution Plan: Consumes/Produces Pattern (22 Skills)

**Status**: Ready to execute
**Timeline**: Systematic gate-by-gate updates
**Decisions Locked**: Confidence (optional), MVP-SCOPE (PRD.md), Consolidation (after Phase 2)

---

## Phase 2 Scope: 22 Remaining Domain Skills

All skills need the same three universal changes:
1. **Consumes section** — List all upstream ID types this skill needs
2. **Produces section** — List all downstream ID types this skill creates
3. **Confidence examples** — Show format for IDs with confidence scoring where applicable

### Skills by Gate (Priority Order)

#### **v0.1: Discovery Spark** (1 skill remaining)

| Skill | Status | Changes |
|-------|--------|---------|
| user-value-articulation | Pending | Add Consumes/Produces; strengthen value extraction; confidence for CFD entries |

---

#### **v0.2: Market Definition** (2 skills)

| Skill | Status | Changes |
|-------|--------|---------|
| competitive-landscape-mapping | Pending | Add Consumes/Produces; competitive feature evidence; confidence examples for CFD |
| product-type-classification | Pending | Add Consumes/Produces; reference market landscape; show how this feeds v0.3 feature strategy |

---

#### **v0.3: Commercial Model** (3 skills)

| Skill | Status | Changes |
|-------|--------|---------|
| moat-definition | Pending | Add Consumes/Produces; link to BR- entries; confidence progression for BR-MOAT entries |
| outcome-definition | Pending | Add Consumes/Produces; link to KPI- entries; confidence as evidence accumulates |
| pricing-model | Pending | Add Consumes/Produces; link to BR-TIER entries; confidence for pricing decisions |

---

#### **v0.4: User Journeys** (3 skills)

| Skill | Status | Changes |
|-------|--------|---------|
| persona-definition | Pending | Add Consumes/Produces; reference MVP-SCOPE boundary; PER- entries |
| user-journey-mapping | Pending | Add Consumes/Produces; explicitly consume MVP-SCOPE from v0.3; UJ- entries |
| screen-flow-definition | Pending | Add Consumes/Produces; reference MVP-SCOPE; define which screens are in MVP; SCR- entries |

---

#### **v0.5: Red Team Review** (2 skills)

| Skill | Status | Changes |
|-------|--------|---------|
| risk-discovery-interview | Pending | Add Consumes/Produces; reference MVP-SCOPE feasibility; RISK- confidence progression |
| tech-stack-selection | Pending | Add Consumes/Produces; reference MVP-SCOPE tech constraints; TECH- confidence (decided → configured → tested → deployed) |

---

#### **v0.6: Architecture** (3 skills)

| Skill | Status | Changes |
|-------|--------|---------|
| architecture-design | Pending | Add Consumes/Produces; ARC- confidence progression; reference MVP boundaries |
| environment-setup | Pending | Add Consumes/Produces; TECH- confidence (env vars = 2/5); reference MVP scope |
| technical-specification | Pending | Add Consumes/Produces; API- and DBT- confidence; MVP scope as specification boundary |

---

#### **v0.7: Build Execution** (3 skills)

| Skill | Status | Changes |
|-------|--------|---------|
| epic-scoping | Pending | Add Consumes/Produces; EPIC- entries; strict MVP-SCOPE boundary |
| implementation-loop | Pending | Add Consumes/Produces; TEST- confidence integration; SoT updates during implementation |
| test-planning | Pending | Add Consumes/Produces; TEST- entries; confidence progression (planned → implemented → verified) |

---

#### **v0.8: Deployment & Ops** (3 skills)

| Skill | Status | Changes |
|-------|--------|---------|
| release-planning | Pending | Add Consumes/Produces; DEP- entries; confidence progression through deployment stages |
| monitoring-setup | Pending | Add Consumes/Produces; MON- entries; confidence for alerting thresholds |
| runbook-creation | Pending | Add Consumes/Produces; RUN- entries; reference DEP stages |

---

#### **v0.9: Go-to-Market** (3 skills)

| Skill | Status | Changes |
|-------|--------|---------|
| gtm-strategy | Pending | Add Consumes/Produces; GTM- entries; reference Delta features (FEA-) for messaging |
| feedback-loop-setup | Pending | Add Consumes/Produces; CFD- entries (post-launch); confidence tracking after ship |
| launch-metrics | Pending | Add Consumes/Produces; KPI- entries (launch-specific); reference outcome definitions from v0.3 |

---

## Universal Template for All 22 Skills

Every skill update follows this pattern:

### Section 1: Consumes

```markdown
## Consumes

This skill requires prior work from [upstream gates]:

- **[ID-TYPE]**: [What entries needed, from which gate]
- **[ID-TYPE]**: [Other inputs]

Example: "CFD-* entries from v0.1-v0.2 research"
```

**What to include**:
- List ALL upstream ID types this skill depends on
- Specify which gate(s) produce those IDs
- Be explicit about whether prior work is optional or required

### Section 2: Produces

```markdown
## Produces

This skill creates/updates:

- **[ID-TYPE]**: [What this skill outputs, with confidence requirements]
- **[ID-TYPE]**: [Other outputs]

Example: "FEA-* entries at confidence 2-3/5 (based on customer feedback evidence)"
```

**What to include**:
- List ALL ID types this skill creates/updates
- Note typical confidence range (if applicable)
- Specify which downstream skills consume these IDs

### Section 3: Confidence Examples (If Applicable)

For any step that produces SoT IDs, add example:

```markdown
### Example entry with confidence:

[ID]-###: [Description]
Confidence: [N]/5 (source: [evidence])
Next Target: [What would move to next level]
```

---

## Execution Order (Recommended)

**Batches by coherence** (related gates execute together):

1. **Batch 1** (v0.1-v0.2): user-value-articulation, competitive-landscape-mapping, product-type-classification
   *Estimated: 3 skills, 1-2 hours*

2. **Batch 2** (v0.3): moat-definition, outcome-definition, pricing-model
   *Estimated: 3 skills, 1-2 hours*

3. **Batch 3** (v0.4): persona-definition, user-journey-mapping, screen-flow-definition
   *Estimated: 3 skills, 1-2 hours*

4. **Batch 4** (v0.5): risk-discovery-interview, tech-stack-selection
   *Estimated: 2 skills, 1-2 hours*

5. **Batch 5** (v0.6): architecture-design, environment-setup, technical-specification
   *Estimated: 3 skills, 1-2 hours*

6. **Batch 6** (v0.7): epic-scoping, implementation-loop, test-planning
   *Estimated: 3 skills, 1-2 hours*

7. **Batch 7** (v0.8): release-planning, monitoring-setup, runbook-creation
   *Estimated: 3 skills, 1-2 hours*

8. **Batch 8** (v0.9): gtm-strategy, feedback-loop-setup, launch-metrics
   *Estimated: 3 skills, 1-2 hours*

**Total estimated effort**: 8-10 hours for all 22 skills

---

## Quality Check After Each Batch

After each batch, verify:

- [ ] All Consumes sections list actual upstream dependencies (not hypothetical)
- [ ] All Produces sections are clear about what this skill creates
- [ ] If confidence examples are included, they follow the standard format
- [ ] No "methodology teaching" creeps into Produces (only describe IDs, not how to use them)
- [ ] Cross-references between batches are accurate (v0.2 Produces should match v0.3 Consumes)

---

## Phase 2 Completion Criteria

Phase 2 is done when:

1. ✅ All 22 skills have Consumes/Produces sections
2. ✅ Examples follow confidence format where applicable
3. ✅ Cross-skill references are bidirectional (v0.X Produces → v0.(X+1) Consumes)
4. ✅ No orphan IDs or dangling references
5. ✅ Git history shows batch-by-batch commits with clear messages

---

## Next: Phase 3 (Post-Phase 2)

After all 22 skills are updated:

1. **Workflow Integration Test** — Trace mock product through v0.1 → v0.3 → v0.7
2. **Connective Tissue Audit** — Verify outputs of skill X feed cleanly into inputs of skill X+1
3. **SoT Confidence Spot-Check** — Sample 5-10 CFD/FEA/TECH entries to confirm confidence annotation consistency
4. **Consolidation Analysis** — Evaluate whether gate-skills should be merged based on coupling revealed by Consumes/Produces

---

## Notes

- **Confidence is optional in Phase 2** — Some skills won't produce SoT IDs (e.g., product-type-classification). Skip confidence examples for non-SoT outputs.
- **MVP-SCOPE reference** — v0.4 and beyond should explicitly reference "MVP-SCOPE artifact from v0.3" in their Consumes sections.
- **Greenfield bias** — While updating, note anywhere a skill assumes greenfield; document for post-Phase 2 review.
