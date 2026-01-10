---
title: "Subagent Definitions"
updated: 2025-01-09
---

# Subagents

Subagents provide isolated context for repeatable tasks. They run in fresh context windows, preventing main session pollution.

## Tier 1: Documentation Subagents (High Frequency)

| Subagent | Trigger | Output |
|----------|---------|--------|
| README-Status-Updater | Gate change, EPIC status change | Updated README dashboard |
| ID-Registrar | New BR-/UJ-/API-/CFD- created | Validated entry + cross-refs |
| Session-Closer | End of work session | EPIC Section 0 + commit |
| Gate-Checker | Before lifecycle advance | Pass/block summary |
| Harvest-Agent | EPIC Phase E | Extracted SoT entries |

## Tier 2: Research Subagents (On Demand)

| Subagent | Trigger | Output |
|----------|---------|--------|
| Competitor-Analyst | v0.3 deep-dive | CFD-XXX competitive entries |
| Tech-Scout | v0.6 exploration | Options analysis |
| User-Researcher | v0.4 synthesis | Pain validation |

---

## Invocation Pattern

```
Invoke {Subagent-Name}:
- Objective: {specific goal}
- Context: {files to load}
- Deliver: {expected output}
- Scope: {boundaries - what NOT to do}
```

---

## README-Status-Updater

### Purpose
Synchronize README.md Command Center with current project state.

### Context to Load
- README.md (current)
- README_template.md (structure reference)
- PRD.md metadata block
- Active EPIC Section 0

### Synchronization Rules
1. **Lifecycle Stage**: Pull from PRD.md "Current Lifecycle Gate"
2. **Gate Table**:
   - 🟢 Complete (passed gates)
   - 🟡 In Progress (current gate)
   - ⚪ Pending (future gates)
3. **Active EPIC**: Update header metadata
4. **Blockers**: Pull from EPIC Section 0

### Output
- Updated README.md
- Change summary

### Boundaries
- DO: Status sync, link updates, gate progression
- DON'T: Content changes to descriptions, new sections

---

## ID-Registrar

### Purpose
Validate and register new SoT IDs with cross-reference integrity.

### Context to Load
- specs/SoT.UNIQUE_ID_SYSTEM.md
- Target SoT file for ID type
- Active EPIC Section 3A

### Validation Rules
1. Format: [PREFIX]-[3-digit number]
2. Uniqueness: Highest existing + 1
3. Required fields per template
4. Cross-references must exist

### Output
- Formatted SoT entry
- Cross-reference updates
- EPIC Section 3A log entry

### Boundaries
- DO: Format validation, uniqueness, cross-refs
- DON'T: Content decisions about ID meaning

---

## Session-Closer

### Purpose
Capture session state for seamless handoff.

### Context to Load
- Active EPIC (full file)
- Git status
- Recent work context

### Protocol
1. Progress summary with ID references
2. Stop point (file:line)
3. Next steps (numbered)
4. Context notes (decisions, blockers)
5. Files changed list
6. Commit message: `session: [EPIC-XX] {summary}`

### Output
- Updated EPIC Section 0
- Staged commit
- Updated agent memory (if patterns observed)

### Boundaries
- DO: State capture, commit staging
- DON'T: Continue work, make decisions

---

## Gate-Checker

### Purpose
Validate gate criteria before lifecycle advancement.

### Context to Load
- PRD.md (gate criteria for target version)
- Relevant SoT files
- Active EPIC

### Checklist
1. Required evidence (CFD-XXX references)
2. Required outputs (BR-XXX, UJ-XXX, etc.)
3. Handoff readiness
4. Open blockers

### Output
- Pass/Block summary
- Missing artifacts list
- Recommendation with rationale

### Boundaries
- DO: Validation, gap identification
- DON'T: Create missing artifacts, override blocks

---

## Harvest-Agent

### Purpose
Extract durable insights from temp/ to SoT files.

### Context to Load
- temp/ contents associated with EPIC
- specs/ templates
- EPIC Section 3A

### Protocol
1. Enumerate temp files from EPIC
2. Identify SoT-worthy content
3. Format per SoT templates
4. Stage archive location
5. Update README metrics

### Output
- New SoT entries
- Archive manifest
- Temp cleanup list

### Boundaries
- DO: Extract, format, archive
- DON'T: Create new analysis, modify conclusions
