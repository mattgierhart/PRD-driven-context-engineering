# Phase 2: Skill Assets & References Creation Roadmap

**Date**: 2026-01-10
**Status**: Phase 1 Complete | Phase 2 In Progress
**Purpose**: Roadmap for completing missing skill assets and references

---

## Phase 1: Completed ✅

**Standard Creation**:
- ✅ Created `SoT.TEMPLATE_PURITY_STANDARD.md`
- ✅ Integrated into ecosystem (SoT.README.md, CLAUDE.md)
- ✅ Codified litmus test: "File structure or domain knowledge?"

**Template Cleanup**:
- ✅ Cleaned `SoT.customer_feedback.md` (severe contamination)
- ✅ Cleaned `SoT.DESIGN_BRIEF.md` (moderate contamination)

**Skill References Created**:
- ✅ `.claude/skills/prd-v09-feedback-loop-setup/references/feedback-analysis-patterns.md`
- ✅ `.claude/skills/prd-v04-screen-flow-definition/references/design-tool-examples.md`

---

## Phase 2: Remaining Work

### v08 Skills (Deployment & Ops)

#### prd-v08-monitoring-setup

**Referenced in SKILL.md** (lines 282-286):

**Assets needed**:
- `assets/mon-template.md` - Template for creating MON-XXX entries

**References needed**:
- `references/monitoring-stack.md` - Tool examples (Datadog, New Relic, Grafana, Prometheus, etc.)
- `references/slo-guide.md` - SLO calculation and error budget guide
- `references/dashboard-guide.md` - Dashboard design best practices

**Content to include**:
- Monitoring stack comparison (pros/cons for different contexts)
- SLO calculation formulas and examples
- Dashboard hierarchy patterns
- Alert tuning guidelines

---

#### prd-v08-release-planning

**Expected files** (based on pattern):

**Assets needed**:
- `assets/dep-template.md` - Template for DEP-XXX (deployment step) entries

**References needed**:
- `references/deployment-strategies.md` - Blue-green, canary, rolling, feature flags
- `references/rollback-procedures.md` - Rollback decision trees and procedures
- `references/examples.md` - Good/bad deployment plan examples

**Content to include**:
- Deployment strategy selection criteria
- Rollback triggers and procedures
- Environment promotion workflow
- Go/no-go checklist patterns

---

#### prd-v08-runbook-creation

**Expected files** (based on pattern):

**Assets needed**:
- `assets/run-template.md` - Template for RUN-XXX (runbook) entries

**References needed**:
- `references/incident-response.md` - Incident response patterns
- `references/troubleshooting-trees.md` - Decision tree structures
- `references/examples.md` - Good/bad runbook examples

**Content to include**:
- Runbook structure (symptoms, diagnosis, resolution)
- Common incident patterns
- On-call playbook patterns
- Post-mortem template

---

### v09 Skills (Go-to-Market)

#### prd-v09-gtm-strategy

**Expected files** (based on pattern):

**Assets needed**:
- `assets/gtm-template.md` - Template for GTM-XXX entries

**References needed**:
- `references/launch-strategies.md` - Launch patterns (beta, phased, big-bang)
- `references/messaging-frameworks.md` - Value prop, positioning templates
- `references/channel-selection.md` - Channel selection criteria
- `references/examples.md` - Good/bad GTM strategy examples

**Content to include**:
- Product launch checklists by type
- Messaging framework (problem/solution/differentiation)
- Channel ROI assessment
- Launch sequence patterns

---

#### prd-v09-launch-metrics

**Expected files** (based on pattern):

**Assets needed**:
- `assets/kpi-template.md` - Template for KPI-XXX entries (may already exist in v03-outcome-definition)

**References needed**:
- `references/launch-metrics.md` - Launch-specific metrics vs growth metrics
- `references/validation-criteria.md` - How to know if launch succeeded
- `references/examples.md` - Good/bad launch metric examples

**Content to include**:
- Launch metric vs growth metric distinction
- Early indicator vs lagging indicator patterns
- Product-market fit signals
- Pivot triggers

---

### GHM Skills (Methodology Management)

#### ghm-gate-check

**Expected files**:

**Assets needed**:
- `assets/gate-checklist-template.md` - Template for gate validation

**References needed**:
- `references/gate-criteria.md` - Criteria for each PRD lifecycle gate
- `references/examples.md` - Pass/block scenarios

**Content to include**:
- Gate validation decision tree
- Mandatory vs optional criteria
- Blocker resolution patterns
- Gate bypass protocols (when acceptable)

---

#### ghm-harvest

**Expected files**:

**Assets needed**:
- `assets/harvest-log-template.md` - Template for documenting harvested insights

**References needed**:
- `references/harvest-patterns.md` - What to preserve vs what to discard
- `references/examples.md` - Good/bad harvest examples

**Content to include**:
- Decision criteria harvesting patterns
- Code-to-SoT extraction rules
- Temp file triage patterns
- Archive vs integrate decision tree

---

#### ghm-id-register

**Expected files**:

**Assets needed**:
- `assets/id-validation-checklist.md` - Checklist for validating new IDs

**References needed**:
- `references/cross-reference-patterns.md` - Valid vs invalid ID relationships
- `references/examples.md` - Good/bad ID registration examples

**Content to include**:
- ID naming conventions
- Cross-reference validation rules
- Orphan ID detection
- Deprecation patterns

---

#### ghm-status-sync

**Expected files**:

**Assets needed**:
- `assets/status-sync-template.md` - Template for README Command Center updates

**References needed**:
- `references/sync-triggers.md` - When to sync status
- `references/examples.md` - Good/bad status sync examples

**Content to include**:
- Command Center update patterns
- Gate status visualization
- Blocker surfacing patterns
- Metric update frequency

---

## Creation Pattern

For each skill, follow this pattern:

### 1. Assets (Templates for Creating Entries)

**Purpose**: Copy-paste templates for SoT entries
**Format**: Blank templates with field placeholders
**Example**: `assets/mon-template.md` for creating MON-XXX entries

**Template structure**:
```markdown
# [ID-XXX]: [Title]

**ID**: [ID-XXX]
**Type**: [Type from skill taxonomy]
**Owner**: [Team/Person]
**Created**: YYYY-MM-DD

[Field definitions from SKILL.md OUTPUT section]

## Related IDs
- [Cross-references]

## Version History
| Version | Date | Change | Updated By |
|---------|------|--------|------------|
| 1.0 | YYYY-MM-DD | Initial creation | [Name] |
```

### 2. References (Methodology and Examples)

**Purpose**: Teach good practices and provide examples
**Format**: Structured guides with examples

**Common reference files**:
1. `examples.md` - Good/bad pattern examples
2. `[domain]-guide.md` - Domain-specific methodology
3. `[tool/pattern]-selection.md` - Decision frameworks

**Example structure**:
```markdown
# [Topic] Guide

## Good Patterns

### Pattern 1: [Name]
**When to Use**: [Context]
**Example**: [Concrete example]
**Why It Works**: [Explanation]

## Bad Patterns (Anti-Patterns)

### Anti-Pattern 1: [Name]
**Problem**: [What's wrong]
**Example**: [Concrete example]
**Fix**: [How to do it correctly]

## Decision Framework
[Criteria for choosing between options]
```

---

## Quality Standards

Based on product development experience, each asset/reference should:

### Assets (Templates)

- [ ] **Completeness**: All fields from SKILL.md output template
- [ ] **Clarity**: Field descriptions and examples
- [ ] **Traceability**: Cross-reference placeholders
- [ ] **Versioning**: Version history table
- [ ] **Validation**: Checklist for completeness

### References

- [ ] **Practical**: Real-world examples, not theoretical
- [ ] **Actionable**: Clear decision criteria
- [ ] **Concise**: Dense information, minimal fluff
- [ ] **Product-focused**: Tied to outcomes, not just process
- [ ] **Pattern-based**: Transferable lessons, not one-offs

---

## Prioritization

### High Priority (Core PRD Lifecycle)

1. v08-monitoring-setup (observability is critical)
2. v08-release-planning (deployment safety)
3. v08-runbook-creation (operational readiness)
4. v09-gtm-strategy (launch success)
5. v09-launch-metrics (validation)

### Medium Priority (Methodology Management)

6. ghm-gate-check (quality gates)
7. ghm-status-sync (visibility)
8. ghm-harvest (knowledge capture)
9. ghm-id-register (governance)

---

## Estimated Scope

**Per skill**:
- 1 asset file: ~100-200 lines (template)
- 2-4 reference files: ~200-400 lines each (guides + examples)

**Total for 9 skills**:
- ~9 asset files
- ~27-36 reference files
- Estimated total: ~7,000-12,000 lines of documentation

**Time estimate** (with product development rigor):
- Per skill: 30-45 minutes (asset + references)
- Total: 4.5-6.75 hours of focused work

---

## Next Session Continuation Points

**If continuing immediately**:
1. Start with v08-monitoring-setup (in progress)
2. Complete v08 skills (deployment & ops cluster)
3. Then v09 skills (GTM cluster)
4. Finally GHM skills (management cluster)

**If resuming later**:
1. Review this roadmap
2. Check skill SKILL.md files for referenced files
3. Follow the creation pattern above
4. Validate against quality standards

---

## Success Criteria

Phase 2 complete when:
- [ ] All 9 skills have complete assets and references
- [ ] All files referenced in SKILL.md exist
- [ ] Templates are copy-paste ready
- [ ] References include good/bad examples
- [ ] Committed and pushed to remote

---

*End of Phase 2 Roadmap*
