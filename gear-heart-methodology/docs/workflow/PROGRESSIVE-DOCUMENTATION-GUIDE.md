# PROGRESSIVE-DOCUMENTATION-GUIDE.md
**Single Source of Truth Through Progressive Updates**

**Version**: 1.1  
**Created**: 2025-07-06  
**Last Updated**: 2025-07-28 - Added consolidated template references, removed archived MODEL-USAGE-GUIDE
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

### Research Template (Consolidated)
**File**: `research-template.md`
**Versions**: v0.1 (Market Spark) → v0.5 (Decision Framework)
**Purpose**: Single progressive document for all research phases

```markdown
## Version History & Progression
| Version | Phase | Date | Editor | Changes |
|---------|-------|------|--------|---------|
| v0.1 | Market Spark | [Date] | User + AURA | Initial spark and problem identification |

### Version Triggers
- **v0.1 → v0.2**: Market definition research complete
- **v0.2 → v0.3**: Competitive analysis complete
- **v0.3 → v0.4**: User validation complete
- **v0.4 → v0.5**: Analysis complete, ready for Gate 1
```

### Design Brief Template (Consolidated)
**File**: `design-brief-template.md`
**Versions**: v1.0 → v2.0 (Progressive refinement)
**Purpose**: Comprehensive design documentation incorporating all design phases

**Key Features**:
- Design tokens integrated directly
- UXPilot prompt generation embedded
- Component extraction guides included
- No separate token or experience templates needed

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

## Version Reference Strategies

**Challenge**: When you tell Claude Code "we're working on v2.0", it naturally wants to see what v1.0 looked like, potentially contaminating new development with old implementation patterns.

**Solution**: Reference-only architecture that provides behavioral context without code access.

### Layer 1: Behavioral Contracts (Recommended)
**Purpose**: Document what previous versions did, not how they did it
**Location**: `docs/v{X}-contracts/` in current version directory

```markdown
# v1.0 Behavioral Contracts

## Authentication
**Endpoint**: POST /api/auth/login
**Input**: { email, password }
**Output**: { token, user }
**Behavior**: Returns JWT valid for 24 hours
**Reference**: GitHub release v1.0

## Document Upload  
**Endpoint**: POST /api/documents
**Input**: FormData with file
**Output**: { id, url, status }
**Behavior**: Processes PDF, extracts text
**Reference**: GitHub release v1.0
```

### Layer 2: Version Context Documentation
**File**: `VERSION-CONTEXT.md` in current version directory
**Purpose**: Clarify relationships between versions and reference rules

```markdown
# Product Version Context

## Current Version: v2.0
**Status**: Phoenix restart with v1 learnings
**Relationship to v1.0**: Complete rewrite, behavioral compatibility

## v1.0 Reference
**Location**: GitHub release v1.0
**Access**: Reference only - DO NOT CLONE
**Deployed**: https://product-v1.domain.com

## What We're Keeping from v1.0
- Authentication flow (behavior, not code)
- API contract structure (format, not implementation)
- User experience patterns (flow, not styling)

## What We're Changing in v2.0
- Complete structural reorganization  
- Modern architecture patterns
- Improved performance and scalability

## How to Reference v1.0
1. Read behavioral contracts in docs/v1-contracts/
2. Test against deployed v1.0 instance
3. NEVER import v1.0 code directly
4. Use v1.0 as acceptance criteria only
```

### Layer 3: GitHub Release Strategy
**Approach**: Tag previous versions as GitHub releases with behavioral documentation

**Implementation**:
1. **Create Release**: Tag v1.0 with comprehensive release notes
2. **Attach Contracts**: Include behavioral contracts as release assets
3. **Link Documentation**: Reference release URL in v2.0 docs
4. **API Reference**: Use GitHub API for safe, read-only access

```javascript
// Safe v1.0 reference via GitHub API
const { Octokit } = require("@octokit/rest");

class V1Reference {
  async getV1Behavior(endpoint) {
    const release = await this.octokit.repos.getReleaseByTag({
      owner: 'username',
      repo: 'product',
      tag: 'v1.0'
    });
    return this.extractBehaviorFromRelease(release.data, endpoint);
  }
}
```

### Layer 4: Clean Room Implementation
**Principle**: Treat previous versions as external APIs, not source code

**Rules for Claude Code**:
- ✅ Check behavioral contracts in docs/v{X}-contracts/
- ✅ Test against deployed v{X} instance for validation
- ✅ Use GitHub release links for reference
- ❌ Never clone previous version repositories
- ❌ Never copy previous version code
- ❌ Never import previous version files
- ❌ Never look at previous version implementation

**Implementation Protocol**:
1. **Implement Fresh**: Build based on behavioral requirements
2. **Test Compatibility**: Validate against previous version behavior
3. **Document Decisions**: Track implementation choices vs. previous approaches
4. **Maintain Boundaries**: Keep versions architecturally separate

### Layer 5: Agent Context Management
**Product Owner Agent Enhancement**: Configure agents to handle version queries safely

```markdown
## When Claude asks about v1.0

RESPOND WITH:
"I can provide v1.0 behavioral references without code access:

1. **Behavioral Contracts**: See docs/v1-contracts/
2. **Deployed Instance**: https://product-v1.domain.com
3. **GitHub Release**: Tagged as v1.0 (reference only)
4. **Key Decisions**: See docs/v1-learnings.md

For v2.0 development:
- Implement fresh based on contracts
- Test against v1.0 behavior
- Never copy v1.0 code
- Use clean room implementation"

## Version Confusion Prevention

If Claude says:
- "Let me look at v1.0 code..." → STOP
- "I'll check the previous implementation..." → STOP  
- "Based on v1.0's approach..." → STOP

Correct to:
- "Let me check v1.0 behavioral contracts..."
- "I'll verify against v1.0 behavior..."
- "Based on v1.0's requirements..."
```

### Benefits of Reference-Only Architecture
- **Prevents Code Contamination**: No old patterns infect new implementation
- **Maintains Behavioral Compatibility**: Users experience consistent functionality
- **Enables Clean Architecture**: Fresh implementation with modern patterns
- **Simplifies Context Management**: Clear boundaries between versions
- **Supports Progressive Documentation**: Single source of truth per version

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

### ❌ Template Sprawl
**Wrong**: Separate templates for each phase
```
templates/research-phase/market-spark-PRD-v01.md
templates/research-phase/perplexity-research-prompt.md
templates/research-phase/red-team-analysis-template.md
templates/design/design-tokens-template.md
templates/design/design-experience-template.md
```

**Right**: Consolidated progressive templates
```
templates/research-template.md (all research phases)
templates/design-brief-template.md (all design elements)
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
From Example Product project:
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
*For agent catalog, see [/.claude/agents/](../../.claude/agents/)*