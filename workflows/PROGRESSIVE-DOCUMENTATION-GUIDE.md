# PROGRESSIVE-DOCUMENTATION-GUIDE.md
**Single Source of Truth Through Progressive Updates**

**Version**: 1.0  
**Created**: 2025-07-06  
**Purpose**: Detailed guidelines for maintaining single, evolving documents rather than creating document sprawl

---

## Core Philosophy

**One Document, Many Versions > Many Documents, No Clarity**

Progressive documentation maintains a single source of truth for each major artifact (PRD, Epic, Design Brief) that evolves through clearly tracked versions. This approach:
- Reduces information fragmentation
- Maintains complete history
- Simplifies handoffs
- Enables better decision tracking

---

## Document Types and Progression

### Product Requirements Document (PRD)
**File**: `{product-name}-PRD.md`
**Versions**: v0.1 → v0.2 → ... → v1.0 → v1.1 (post-launch)

```markdown
## PRD Meta Information
| Field | Value |
|-------|-------|
| **Current Version** | v0.5 |
| **Last Updated** | 2025-07-06 14:30 UTC |
| **Last Editor** | AURA |
| **Status** | Red Team Analysis |
| **Next Milestone** | Gate 1 Decision |
| **Total Edits** | 5 |

## Version Change Log
| Version | Date | Editor | Changes Made |
|---------|------|--------|--------------|
| v0.1 | 2025-07-01 | User + AURA | Initial market spark |
| v0.2 | 2025-07-02 | AURA | Added market research |
| v0.3 | 2025-07-03 | AURA | Competitive analysis |
| v0.4 | 2025-07-04 | AURA | User validation |
| v0.5 | 2025-07-05 | AURA | Red team analysis |
```

### Epic Documents
**File**: `epics/EPIC-{number}-{name}.md`
**Versions**: Planning (v0.1-0.3) → Execution (v0.4+)

```markdown
---
epic_id: EPIC-01
version: 0.4
status: in_progress
model_history: "opus(v0.1-0.3), sonnet(v0.4)"
---

## Epic Version History
| Version | Date | Model | Changes |
|---------|------|-------|---------|
| 0.1 | 2025-07-01 | Opus | Initial structure |
| 0.2 | 2025-07-02 | Opus | Architecture defined |
| 0.3 | 2025-07-03 | Opus | Task breakdown |
| 0.4 | 2025-07-05 | Sonnet | Implementation 40% |
```

---

## Update Patterns

### Appending Content
Use when adding new information without changing existing content:

```markdown
<!-- Previous content remains unchanged -->

<!-- APPENDED: 2025-07-06 by Claude -->
## New Section: Performance Optimization

Based on latest testing, we need to address:
- Database query optimization
- Caching strategy
- Bundle size reduction
<!-- END APPEND -->
```

### Revising Content
Use when existing content needs modification:

```markdown
<!-- REVISED: 2025-07-06 by Claude - Reason: Updated based on feasibility analysis -->
## Technical Architecture

### Previous Approach (v0.6)
~[Strikethrough previous content for reference]~

### Current Approach (v0.7)
[New content with explanation of changes]
<!-- END REVISION -->
```

### Inline Updates
For small changes, use inline notation:

```markdown
- Budget: ~$5000~ $3000 <!-- UPDATED: 2025-07-06, reduced after optimization -->
- Timeline: 14 days <!-- CONFIRMED: 2025-07-06, feasibility verified -->
```

---

## Version Increment Guidelines

### When to Increment Versions

#### Minor Increments (0.1 → 0.2)
- Adding new sections
- Completing planned analyses
- Updating based on feedback
- Refining existing content

#### Major Increments (0.x → 1.0)
- Document approved/finalized
- Moving to next phase
- Fundamental strategy change
- Ready for implementation

#### Post-Launch (1.0 → 1.1)
- Feature additions
- Strategy pivots
- Lessons learned
- Optimization updates

### Version Increment Checklist
1. [ ] Update version number in metadata
2. [ ] Add entry to version history table
3. [ ] Update "Last Updated" timestamp
4. [ ] Update "Last Editor" field
5. [ ] Summarize changes in log entry
6. [ ] Update status if applicable

---

## Multi-Model Collaboration

### Handoff Annotations
When multiple models work on same document:

```markdown
<!-- HANDOFF: From Opus to Sonnet - 2025-07-06 -->
Planning sections above are complete. 
Ready for implementation of tasks 1-5.
<!-- END HANDOFF -->

<!-- HANDOFF: From Sonnet to Opus - 2025-07-07 -->
Tasks 1-3 complete. Blocked on task 4 (see notes).
Need architecture decision for caching.
<!-- END HANDOFF -->
```

### Model-Specific Sections
```markdown
## Architecture Design <!-- opus-domain -->
[Complex architectural decisions]

## Implementation Guide <!-- sonnet-ready -->
[Step-by-step implementation instructions]

## Gemini's Strategic Considerations <!-- gemini-added -->
[Strategic review feedback]
```

---

## Cross-Reference Management

### Internal References
Use relative links within document:
```markdown
See [Technical Architecture](#technical-architecture) for details.
As defined in [Version 0.3](#version-history), we...
```

### External References
Link to other documents sparingly:
```markdown
## Technical Details
For in-depth research, see [research/technical-analysis.md].
Epic breakdown available in [epics/EPIC-01-Foundation.md].
```

### Reference Update Protocol
When updating references:
1. Search document for all references
2. Update links if paths change
3. Verify external documents exist
4. Note reference updates in version log

---

## Common Anti-Patterns to Avoid

### ❌ Document Proliferation
**Wrong**: Creating new files for each update
```
product-PRD-v1.md
product-PRD-v2.md
product-PRD-v2-final.md
product-PRD-v2-final-FINAL.md
```

**Right**: Single file with version history
```
product-PRD.md (contains all versions)
```

### ❌ Orphaned Information
**Wrong**: Information scattered across files
```
"See product-notes.md for pricing"
"Architecture in tech-spike.md"
"Decisions in meeting-notes-july.md"
```

**Right**: Consolidated in primary document
```
product-PRD.md contains all core information
References to supporting docs only when necessary
```

### ❌ Hidden Updates
**Wrong**: Changing content without notation
```
Budget: $3000  # Changed from $5000 with no note
```

**Right**: Transparent change tracking
```
Budget: ~$5000~ $3000 <!-- UPDATED: 2025-07-06, reduced after optimization -->
```

---

## Tools and Commands

### Progressive Update Commands
- `/doc-sync`: Verify document consistency
- `/version-bump`: Guided version increment
- `/handoff-claude`: Generate handoff sections
- `/consolidate`: Merge scattered information

### Quick Reference Snippets

**Version Table Header**:
```markdown
## Version Change Log
| Version | Date | Editor | Changes Made |
|---------|------|--------|--------------|
```

**Append Marker**:
```markdown
<!-- APPENDED: [DATE] by [EDITOR] -->
[New content]
<!-- END APPEND -->
```

**Revision Marker**:
```markdown
<!-- REVISED: [DATE] by [EDITOR] - Reason: [EXPLANATION] -->
[Updated content]
<!-- END REVISION -->
```

---

## Benefits Tracking

### Metrics of Success
- **Document Count**: Fewer files to maintain
- **Information Retrieval**: Faster to find information
- **Handoff Time**: Reduced context switching
- **Decision Tracking**: Clear audit trail
- **Conflict Reduction**: Single source prevents conflicts

### Example Results
From HomeFalcon project:
- Reduced 15 PRD drafts to 1 progressive PRD
- Eliminated 8 duplicate epic files
- 75% faster handoffs between models
- 100% decision traceability

---

## Integration with Workflow

### Gate Reviews
Each gate should check:
- [ ] Document versions updated
- [ ] Change logs complete
- [ ] No orphaned information
- [ ] References verified
- [ ] Progressive principles followed

### Model Transitions
Each model switch should:
1. Review current version
2. Add handoff annotation
3. Update version after changes
4. Maintain progressive structure

---

*For workflow details, see [WORKFLOW-MASTER.md](./WORKFLOW-MASTER.md)*  
*For model usage, see [MODEL-USAGE-GUIDE.md](./MODEL-USAGE-GUIDE.md)*