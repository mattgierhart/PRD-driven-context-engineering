# MODEL-USAGE-GUIDE.md
**Optimizing Claude Opus and Sonnet for Maximum Efficiency**

**Version**: 1.0  
**Created**: 2025-07-06  
**Purpose**: Detailed protocols for efficient model usage in APOLLO workflow

---

## Overview

This guide provides detailed protocols for using Claude Opus and Sonnet models efficiently within the APOLLO workflow. The key insight: Opus excels at planning and complex problem-solving, while Sonnet efficiently executes well-defined tasks.

---

## Model Characteristics

### Claude Opus
**Strengths**:
- Complex reasoning and architecture design
- Breaking down ambiguous problems
- Creating detailed implementation plans
- Resolving intricate bugs and blockers
- Cross-domain synthesis
- Strategic decision making

**Context Window**: Standard (but more expensive)
**Best For**: Planning, architecture, complex debugging
**Cost**: Higher per token

### Claude Sonnet
**Strengths**:
- Following detailed instructions
- Writing code from specifications
- Implementing defined patterns
- Routine bug fixes
- Test implementation
- Documentation updates

**Context Window**: Standard (but more economical)
**Best For**: Execution, implementation, routine tasks
**Cost**: Lower per token

---

## Workflow Integration

### Phase-Based Model Usage

#### Phase 1-2: Product Definition & Feasibility
- **Primary Model**: User + AURA (not Claude)
- **Opus Role**: Review complex technical feasibility questions
- **Sonnet Role**: Not typically used

#### Phase 3: Design
- **Primary Model**: User + Design tools
- **Opus Role**: Design system architecture decisions
- **Sonnet Role**: Creating design documentation

#### Phase 4: Development
- **Primary Model**: Split between Opus (planning) and Sonnet (execution)
- **Opus Role**: Epic planning, task breakdown, architecture
- **Sonnet Role**: Implementation, testing, documentation

#### Phase 5: Enhancement
- **Primary Model**: Sonnet for routine enhancements
- **Opus Role**: Major feature additions or refactoring

---

## Epic Structure for Model Efficiency

### Opus-Optimized Sections
```markdown
## Planning & Architecture (Opus Domain)
**Model**: opus-required
**Complexity**: high

### System Design
[Detailed architecture decisions, trade-offs, patterns]

### Task Breakdown
[Comprehensive task list with clear specifications]

### Edge Cases & Error Handling
[Complex scenarios and resolution strategies]

### Integration Strategy
[How components connect, data flow, dependencies]
```

### Sonnet-Optimized Sections
```markdown
## Implementation Tasks (Sonnet Domain)
**Model**: sonnet-ready
**Complexity**: low-medium

### Task 1: Create User Component
**Specification**: [Clear, detailed instructions]
**Input**: [Required data/props]
**Output**: [Expected result]
**Tests**: [Test cases to implement]
```

---

## Handoff Protocols

### Opus to Sonnet Handoff
```markdown
## Handoff: Planning Complete
**From**: Opus
**To**: Sonnet
**Date**: [timestamp]

### Completed Planning
- [x] Architecture documented
- [x] All tasks specified with clear acceptance criteria
- [x] Test scenarios defined
- [x] Error handling strategies outlined

### Ready for Implementation
1. **Task**: [Specific task]
   - **File**: [Where to implement]
   - **Dependencies**: [What's needed]
   - **Tests**: [What tests to write]
   - **Success Criteria**: [How to verify completion]

### Model Guidance
- Follow specifications exactly
- If blocked after 3 attempts, document and skip
- Run tests after each implementation
- Update status in epic after each task
```

### Sonnet to Opus Handoff
```markdown
## Handoff: Blocked Tasks
**From**: Sonnet
**To**: Opus
**Date**: [timestamp]

### Completed Since Last Handoff
- [x] Implemented user authentication
- [x] Created test suite for auth module
- [x] Updated documentation

### Blocked Tasks Requiring Opus
1. **Task**: Database schema optimization
   **Issue**: Performance degradation with large datasets
   **Attempted Solutions**:
   - Tried adding indexes (helped partially)
   - Attempted query optimization (minimal improvement)
   - Considered caching (unsure of approach)
   **Context**: [Code snippets, performance metrics]
   **Need**: Architecture decision on caching strategy

### Continue With
- Remaining "sonnet-ready" tasks in epic
- Documentation updates
- Test coverage improvements
```

---

## Error Handling Protocol

### Sonnet's 3-Attempt Rule
1. **First Attempt**: Follow specifications directly
2. **Second Attempt**: Try alternative approach within scope
3. **Third Attempt**: Simplify or work around if possible
4. **Document & Skip**: Create detailed handoff for Opus

### What Constitutes a Block
- Architecture decisions needed
- Specifications unclear or conflicting
- Performance optimization beyond simple fixes
- Security implications requiring analysis
- Integration issues with external systems

### What Doesn't Constitute a Block
- Simple syntax errors
- Missing dependencies (install and continue)
- Test failures from implementation bugs
- Documentation updates needed
- Code formatting issues

---

## Efficiency Tips

### For Opus Sessions
1. **Batch Complex Problems**: Save multiple architecture questions
2. **Request Comprehensive Plans**: Get all details in one session
3. **Define Clear Boundaries**: Specify what Sonnet should/shouldn't modify
4. **Create Decision Trees**: For complex logic Sonnet can follow

### For Sonnet Sessions
1. **Provide Complete Context**: Include all needed specifications
2. **Set Clear Boundaries**: Define scope to prevent drift
3. **Enable Fast Failure**: Give permission to skip after 3 attempts
4. **Batch Similar Tasks**: Group related implementations

---

## Progressive Documentation During Handoffs

### Maintain Continuity
- Append to existing sections, don't create new files
- Update version numbers in epic metadata
- Add handoff history to track model transitions
- Keep running status of completed/blocked tasks

### Version Control
```markdown
## Epic Version History
| Version | Date | Model | Changes |
|---------|------|-------|---------|
| 0.1 | [date] | Opus | Initial planning |
| 0.2 | [date] | Opus | Architecture defined |
| 0.3 | [date] | Opus | Task breakdown complete |
| 0.4 | [date] | Sonnet | Implementation started |
| 0.5 | [date] | Sonnet | 60% tasks complete, 2 blocked |
| 0.6 | [date] | Opus | Resolved blocks, refined architecture |
```

---

## Common Patterns

### Pattern: Complex Feature Development
1. **Opus**: Design feature architecture, create task list
2. **Sonnet**: Implement each component per specifications
3. **Sonnet**: Write tests for components
4. **Opus**: Review integration, resolve any blocks
5. **Sonnet**: Final integration and documentation

### Pattern: Bug Investigation and Fix
1. **Sonnet**: Attempt fix (up to 3 tries)
2. **Opus**: Analyze root cause if Sonnet blocked
3. **Opus**: Design solution approach
4. **Sonnet**: Implement fix per Opus design
5. **Sonnet**: Add regression tests

### Pattern: Performance Optimization
1. **Opus**: Analyze bottlenecks, design optimization strategy
2. **Sonnet**: Implement specific optimizations
3. **Sonnet**: Run performance tests
4. **Opus**: Review results, adjust strategy if needed

---

## Metrics for Success

### Efficiency Indicators
- **Handoff Frequency**: Aim for <2 per epic
- **Block Rate**: Target <10% of Sonnet tasks
- **Completion Rate**: >90% of planned tasks per session
- **Rework Rate**: <5% of implemented features

### Quality Indicators
- **Test Coverage**: Maintained or improved
- **Documentation**: Updated with each session
- **Architecture Adherence**: Implementations match plans
- **Progressive Updates**: Single source of truth maintained

---

*For workflow integration, see [WORKFLOW-MASTER.md](./WORKFLOW-MASTER.md)*  
*For commands, see [CUSTOM-COMMANDS.md](/development/tools/CUSTOM-COMMANDS.md)*