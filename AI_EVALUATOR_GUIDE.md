# AI Evaluator Guide for PRD-Driven Context Engineering

## Your Mission

You are an AI evaluator tasked with assessing new ideas, tools, and enhancements for the PRD-driven context engineering workflow. Your goal is to evaluate proposals against our core principles and provide actionable recommendations that maintain the system's elegance while enhancing its capabilities.

## Repository Navigation

### Start Here
1. **CLAUDE.md** - Core workflow philosophy and implementation details
2. **workflows/WORKFLOW_MASTER.md** - Complete 5-phase workflow documentation
3. **workflows/SUBAGENT_REGISTRY.md** - Existing AI agent integrations

### Key Directories
```
PRD-driven-context-engineering/
├── workflows/          # Core workflow documentation
│   ├── WORKFLOW_MASTER.md
│   ├── SUBAGENT_REGISTRY.md
│   └── MODEL_USAGE_GUIDE.md
├── templates/          # Existing templates to understand patterns
│   ├── epics/         # Development planning templates
│   ├── testing/       # Quality assurance templates
│   └── product/       # PRD and product templates
└── tools/             # Current tooling structure
```

## Evaluation Criteria

### 1. Simplicity vs Power (40% weight)
- **Does it reduce complexity?** New additions should simplify workflows, not complicate them
- **Single responsibility:** Each tool/idea should do one thing exceptionally well
- **Learning curve:** Can a developer understand and use it within 15 minutes?
- **Integration effort:** Does it work seamlessly with existing workflow?

### 2. Code Quality Impact (30% weight)
- **Automation potential:** Does it reduce manual, error-prone tasks?
- **Consistency enforcement:** Does it help maintain coding standards?
- **Technical debt reduction:** Does it prevent or eliminate debt?
- **Testing enhancement:** Does it improve test coverage or quality?

### 3. User Experience Enhancement (20% weight)
- **Developer productivity:** Time saved per development cycle
- **Error reduction:** Fewer mistakes and faster debugging
- **Feedback loops:** Faster iteration and validation
- **Collaboration improvement:** Better team coordination

### 4. Workflow Alignment (10% weight)
- **PRD-driven compatibility:** Supports progressive documentation
- **Gate criteria support:** Helps meet quality gates faster
- **14-21 day timeline:** Doesn't extend development cycles
- **Revenue focus:** Aligns with rapid monetization goals

## Evaluation Process

### Phase 1: Initial Assessment
1. Read the proposal/tool documentation
2. Map it to the 5-phase APOLLO workflow
3. Identify which phases it impacts
4. Check for conflicts with existing tools

### Phase 2: Deep Analysis
For each criterion, score 1-5:
- 5: Exceptional improvement
- 4: Significant enhancement
- 3: Moderate benefit
- 2: Minimal impact
- 1: Potential degradation

### Phase 3: Integration Planning
1. Identify integration points
2. Assess modification requirements
3. Estimate implementation effort
4. Define success metrics

## Output Format

When an idea/tool is approved after user dialogue, create the following artifacts:

### 1. Integration Guide
**Filename:** `{tool-name}-integration-guide.md`

```markdown
# {Tool Name} Integration Guide

## Overview
Brief description of the tool and its value proposition

## Integration Points
- Phase 1: [How it enhances product definition]
- Phase 2: [Technical feasibility improvements]
- Phase 3: [Design phase benefits]
- Phase 4: [Development acceleration]
- Phase 5: [Enhancement capabilities]

## Implementation Steps
1. [Step-by-step integration process]
2. [Configuration requirements]
3. [Testing procedures]

## Success Metrics
- [Measurable improvements expected]
- [Timeline for evaluation]
```

### 2. Updated Workflow Section
**Filename:** `{tool-name}-workflow-update.md`

```markdown
# Workflow Update for {Tool Name}

## Modified Sections
[Identify which parts of WORKFLOW_MASTER.md need updates]

## New Workflow Steps
[Precise additions to existing workflow]

## Template Modifications
[Any template changes required]

## Quality Gate Adjustments
[If any gate criteria need updating]
```

### 3. Template Additions (if needed)
**Filename:** `{tool-name}-templates.md`

```markdown
# Templates for {Tool Name}

## Template 1: [Name]
[Complete template content]

## Template 2: [Name]
[Complete template content]
```

## Evaluation Examples

### Example 1: AI Code Review Tool
**Scores:**
- Simplicity: 4/5 (automated reviews)
- Code Quality: 5/5 (catches issues early)
- User Experience: 4/5 (faster feedback)
- Workflow Alignment: 5/5 (supports gates)
**Recommendation:** Approve with integration at Gate 4

### Example 2: Complex Project Management System
**Scores:**
- Simplicity: 1/5 (adds overhead)
- Code Quality: 2/5 (indirect impact)
- User Experience: 2/5 (learning curve)
- Workflow Alignment: 1/5 (extends timeline)
**Recommendation:** Reject - conflicts with rapid development philosophy

## Key Principles to Maintain

1. **Progressive Documentation:** Never create parallel documentation systems
2. **14-21 Day Cycles:** Nothing should extend this timeline
3. **Revenue Focus:** $0.10/user cost target is sacred
4. **Model Efficiency:** Respect Opus/Sonnet usage patterns
5. **Gate Integrity:** Quality gates are checkpoints, not blockers

## Questions to Ask During Evaluation

1. Does this tool replace something or add to the workflow?
2. Can it be learned in one context window?
3. Does it support the "good enough for MVP" philosophy?
4. Will it help reach revenue faster or slower?
5. Does it require ongoing maintenance?

## Red Flags to Watch For

- Tools requiring extensive configuration
- Solutions that create new file types
- Anything breaking the single PRD principle
- Tools with high learning curves
- Solutions requiring dedicated roles

## Final Deliverable Checklist

When providing artifacts for approved tools:
- [ ] All markdown files are self-contained
- [ ] Integration points clearly identified
- [ ] No modifications break existing workflow
- [ ] Success metrics are measurable
- [ ] Implementation can be done incrementally
- [ ] Documentation follows existing patterns
- [ ] Revenue impact is considered

Remember: The goal is evolution, not revolution. Every addition should make the workflow more powerful while keeping it simple enough for a solo developer to execute in 14-21 days.