# Agent Memory Schema Implementation Plan

**Created**: 2025-01-16
**Author**: Claude (planning session)
**Input**: Agent Memory Schema v1.0
**Scope**: Refactor `.claude/agents/{HORIZON,STUDIO,WERK,METRO}.md`

---

## Executive Summary

This plan transforms the current agent files from "instruction-focused" documents into "memory-architected" documents. The core insight: **Instructions define behavior. Memory defines identity.**

### Gap Analysis

| Aspect | Current State | Target State |
|--------|---------------|--------------|
| **ID Ownership** | Implicit in "Outputs Produced" | Explicit "IDs I Own" section with SoT locations |
| **Learning Types** | Generic "Patterns Observed" | Domain-specific learning categories |
| **Context Requirements** | Vague "Inputs Required" | Stage-specific "What I Need Loaded" |
| **Ephemeral Definition** | Not defined | Explicit "What I Forget" section |
| **Learning Capture** | No protocol | Agent-specific post-work questions |
| **Harvest Tracking** | Basic "Harvest Candidates" | Enhanced with "Compounded To" destination |
| **Compounding Loop** | Not implemented | Explicit 3+ occurrence → extraction path |

---

## Implementation Phases

### Phase 1: Structure Refactor (All Agents)

Add **Memory Architecture** section after Identity, containing:

```markdown
## Memory Architecture

### IDs I Own
| Prefix | Meaning | SoT Location |
|--------|---------|--------------|

### What I Learn
| Category | What to Capture | Example |
|----------|-----------------|---------|

### What I Need Loaded
| Stage | Context Required |
|-------|------------------|

### What I Forget
- {Ephemeral item}
```

### Phase 2: Agent-Specific Content

#### HORIZON.md Changes

**IDs I Own** (from schema):
| Prefix | Meaning | SoT Location |
|--------|---------|--------------|
| BR- | Business rules & constraints | SoT.BUSINESS_RULES.md |
| UJ- | User journey definitions | SoT.USER_JOURNEYS.md |
| PER- | Persona definitions | SoT.USER_JOURNEYS.md |
| KPI- | Success metrics | PRD.md v0.3 |
| RISK- | Risk register entries | PRD.md v0.5 |
| CFD- | Customer feedback data | SoT.customer_feedback.md |

**What I Learn** categories:
- ICP Signals
- Journey Friction
- Pricing Sensitivity
- Competitive Tells
- Research Shortcuts
- Risk Patterns

**What I Need Loaded**:
| Stage | Context Required |
|-------|------------------|
| v0.1 | Problem statement, founder notes, market signals |
| v0.2 | v0.1 complete, competitive data, CFD- competitor mentions |
| v0.3 | v0.2 complete, pricing research, existing BR- |
| v0.4 | v0.3 complete, user research artifacts, STUDIO collaboration |
| v0.5 | v0.4 complete, WERK technical input, all BR-/UJ-/PER- |

**What I Forget**:
- Raw interview transcripts (extract insights → CFD-)
- Research URLs (capture findings → CFD-)
- Draft iterations (keep final versions only)
- Competitor pricing screenshots (capture data → CFD-)

**Learning Capture Protocol**:
```
After each PRD stage, ask:
1. What customer signal did I learn that predicts success/failure?
2. What assumption did I validate or invalidate? What was the evidence?
3. What competitive insight should inform future positioning?
4. What research method worked (or didn't) that I should remember?
5. What risk pattern emerged that I should watch for next time?
```

---

#### STUDIO.md Changes

**IDs I Own**:
| Prefix | Meaning | SoT Location |
|--------|---------|--------------|
| DES- | Design components & patterns | SoT.DESIGN_COMPONENTS.md |
| SCR- | Screen definitions | SoT.USER_JOURNEYS.md |
| DS- | Design system tokens | SoT.DESIGN_COMPONENTS.md |

**What I Learn** categories:
- Usability Gotchas
- Accessibility Wins
- Component Reuse
- Design-Dev Friction
- Persona Behaviors
- Platform Quirks

**What I Need Loaded**:
| Stage | Context Required |
|-------|------------------|
| v0.3 | UJ- drafts, BR- constraints, pricing context from HORIZON |
| v0.4 | Complete UJ-, PER- personas, user research in temp/ |
| v0.6 | All SCR-/DES-, WERK technical constraints, component library caps |

**What I Forget**:
- Figma iteration history (keep final designs only)
- Rejected mockup variations (document decision, delete files)
- User test session recordings (extract insights → CFD-)
- Prototype links (capture findings, prototypes can be archived)

**Learning Capture Protocol**:
```
After design work, ask:
1. What usability pattern worked (or failed) that I should remember?
2. What component did I create that could be reused?
3. What accessibility approach should become standard?
4. What caused friction with WERK/HORIZON that I should prevent?
5. What persona-specific behavior should inform future designs?
```

---

#### WERK.md Changes

**IDs I Own**:
| Prefix | Meaning | SoT Location |
|--------|---------|--------------|
| ARC- | Architecture decisions | SoT.TECHNICAL_DECISIONS.md |
| TECH- | Technology stack selections | SoT.TECHNICAL_DECISIONS.md |
| API- | API endpoint contracts | SoT.API_CONTRACTS.md |
| DBT- | Database/data model definitions | SoT.DATA_MODEL.md |
| TEST- | Test specifications | SoT.TESTING.md |
| EPIC- | Implementation work packages | epics/ |
| DEP- | Deployment configurations | SoT.DEPLOYMENT.md |
| RUN- | Operational runbooks | SoT.DEPLOYMENT.md |

**What I Learn** categories:
- Implementation Patterns
- Performance Insights
- Dependency Pitfalls
- Test Strategies
- Why-We-Didn't
- Debugging Lessons
- Architecture Regrets

**What I Need Loaded**:
| Stage | Context Required |
|-------|------------------|
| v0.6 | PRD v0.5+, all BR-/UJ-/PER-, DES- from STUDIO, RISK- technical items |
| v0.7 | Complete API-/DBT-/ARC-, current EPIC, TEST- for scope |
| v0.8 | All EPICs complete, DEP- drafts, RUN- drafts, MON- requirements |

**What I Forget**:
- Build logs (summarize failures, delete logs)
- Debug session notes (extract patterns, delete notes)
- Dependency upgrade experiments (document decision, delete branches)
- Performance profiling raw data (capture insights, delete traces)

**Learning Capture Protocol**:
```
After each EPIC completion, ask:
1. What implementation pattern did I discover that should be reused?
2. What mistake did I make that can be prevented? (Add to anti-patterns)
3. What performance insight should inform future architecture?
4. What "why we didn't" decision should be documented?
5. What test strategy caught (or missed) bugs?
6. What would I do differently if starting over?
```

**Extraction Note** (unique to WERK):
```
Critical: When pattern appears 3+ times:
- Pattern appears 3+ times → Extract to CLAUDE.md or skill
- Architecture insight → Add to ARC- as learning
- Dependency pitfall → Add to TECH- as warning
```

---

#### METRO.md Changes

**IDs I Own**:
| Prefix | Meaning | SoT Location |
|--------|---------|--------------|
| GTM- | Go-to-market entries | PRD.md v0.9 |
| MON- | Monitoring configurations | SoT.DEPLOYMENT.md |

**Note**: METRO also *contributes to* CFD- (customer feedback) which HORIZON owns.

**What I Learn** categories:
- Channel Effectiveness
- Messaging Resonance
- Launch Timing
- Feedback Patterns
- Adoption Blockers
- Pricing Feedback

**What I Need Loaded**:
| Stage | Context Required |
|-------|------------------|
| v0.9 | PRD v0.8+, DEP- documentation, feature list from WERK, KPI- targets |
| v1.0 | Complete GTM-, CFD- post-launch, adoption metrics, channel data |

**What I Forget**:
- Campaign draft iterations (keep final + results)
- Social post variations (document what worked, delete rest)
- Email A/B test versions (capture winner + learnings)
- Raw analytics exports (extract insights → CFD-)

**Learning Capture Protocol**:
```
After launch activities, ask:
1. What channel/message combination worked that should be repeated?
2. What customer feedback pattern should HORIZON know about?
3. What adoption blocker appeared that affects product direction?
4. What pricing signal should inform commercial model?
5. What launch timing lesson should be remembered?
```

**Critical Note**: Feed learnings back to HORIZON via CFD-XXX entries. The feedback loop is METRO's most important output.

---

### Phase 3: Project Memory Enhancement

Refactor the **Project Memory** section in all agents:

#### Current Structure (to keep):
- Project Context
- Key Decisions
- Collaboration Notes
- Handoff Friction
- Open Questions

#### Enhanced/Modified:
**Patterns Observed** → **Patterns Learned** with new columns:

```markdown
### Patterns Learned

| Date | Pattern | Evidence (IDs) | Compounded To |
|------|---------|----------------|---------------|
| —    | —       | —              | —             |
```

The "Compounded To" column tracks where patterns were extracted:
- `CLAUDE.md` — universal discipline
- `skill: {name}` — stage-specific skill
- `{AGENT}.md` — domain-specific pattern
- `ARC-XXX` / `BR-XXX` — SoT entry

**Harvest Candidates** → **Harvest Queue**:

```markdown
### Harvest Queue

| Pattern | Occurrences | Target Extraction |
|---------|-------------|-------------------|
| —       | —           | —                 |
```

---

### Phase 4: Preserve Existing Value

Elements to **keep unchanged**:
- Identity section (expand slightly with "room" concept)
- Primary Responsibilities
- Collaboration Model diagrams
- Decision Authority
- Handoff Contracts
- Subagent Templates
- Anti-patterns
- Agent-specific memory tables (Feedback Loop Log, Technical Debt Log, etc.)

Elements to **merge/refactor**:
- "Inputs Required" → absorbed into "What I Need Loaded"
- "Outputs Produced" → absorbed into "IDs I Own" (but keep the full table for clarity)

---

## Implementation Sequence

### Step 1: HORIZON.md
1. Add "Memory Architecture" section after Identity
2. Move/refactor Inputs to "What I Need Loaded"
3. Add Learning Capture Protocol
4. Enhance Project Memory section
5. Validate ID ownership against SoT.UNIQUE_ID_SYSTEM.md

### Step 2: STUDIO.md
Same pattern, with DS- prefix addition (design system tokens)

### Step 3: WERK.md
Same pattern, with extraction note unique to builder role

### Step 4: METRO.md
Same pattern, with emphasis on feedback loop to HORIZON

---

## Validation Criteria

After implementation, each agent file should clearly answer:

1. **"What does this agent remember?"** → Memory Architecture section
2. **"What IDs does this agent own?"** → IDs I Own table
3. **"What patterns does this agent learn?"** → What I Learn table
4. **"What context does this agent need?"** → What I Need Loaded table
5. **"What does this agent forget?"** → What I Forget list
6. **"How does learning get extracted?"** → Learning Capture Protocol + Harvest Queue

### Cross-Validation

- [ ] All ID prefixes in agent files match SoT.UNIQUE_ID_SYSTEM.md
- [ ] No agent-specific patterns exist in CLAUDE.md
- [ ] Harvest path is explicit for each agent
- [ ] Learning categories are domain-appropriate (not generic)
- [ ] Ephemeral lists are actionable (specify what to extract before deletion)

---

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Agent files become too long | Keep Memory Architecture concise; detailed patterns live in Project Memory |
| Overlap in ID ownership | METRO "contributes to" CFD- but HORIZON "owns" it — use explicit language |
| Learning categories too abstract | Each category has concrete examples in the table |
| Protocol becomes ignored | Integrate into session end workflow in CLAUDE.md |

---

## Open Questions

1. **Should Learning Capture Protocol be automated via hooks?** — Could trigger at session end
2. **DS- prefix not in SoT.UNIQUE_ID_SYSTEM.md** — Should we add it, or is it covered by DES-?
3. **Compounding threshold** — Is 3 occurrences the right threshold for extraction?
4. **Project Memory persistence** — How do patterns survive when agent files are forked?

---

## Next Steps

1. Review this plan with Matt
2. Decide on open questions
3. Implement Phase 1-4 sequentially
4. Validate against criteria
5. Commit with message: `feat(agents): implement Agent Memory Schema v1.0`

---

*End of Implementation Plan*
