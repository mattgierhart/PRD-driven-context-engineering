# CUSTOM-COMMANDS.md
**Custom Workflow Commands for APOLLO Development**

**Version**: 1.0  
**Created**: 2025-07-06  
**Purpose**: Define custom commands for efficient workflow navigation and model-aware development

---

## Command Overview

These custom commands help you navigate the APOLLO workflow efficiently, especially when switching between Claude Opus and Sonnet models. Commands are not model-specific but provide reminders and context for optimal model usage.

---

## Planning Commands

### `/plan`
**Purpose**: Initialize planning phase with Opus model  
**When to Use**: Starting new epic planning, architecture decisions, or resolving complex blockers  
**Expected Output**: 
- Reminder to switch to Opus model
- Loaded planning templates based on current phase
- Current epic planning status summary

**Template References**:
- [EPIC-environment-template.md](templates/EPIC-environment-template.md) - For setup planning
- [EPIC-feature-template.md](templates/EPIC-feature-template.md) - For feature planning
- [product-PRD-template.md](templates/product-PRD-template.md) - For PRD updates

**Progressive Documentation**: Updates existing epic files with planning sections, maintains version history

### `/gate-check`
**Purpose**: Validate current gate criteria  
**When to Use**: Before proceeding to next phase  
**Expected Output**:
- Current gate requirements checklist
- Completion status for each criterion
- Missing requirements highlighted
- Go/No-go recommendation

**Template References**:
- Gate criteria from [WORKFLOW-MASTER.md](workflows/WORKFLOW-MASTER.md#quality-gates-and-success-criteria)

**Progressive Documentation**: Adds gate validation results to PRD version history

---

## Execution Commands

### `/execute`
**Purpose**: Initialize execution phase with Sonnet model  
**When to Use**: Beginning code implementation from approved plans  
**Expected Output**:
- Reminder to use Sonnet model
- Execution checklist for current epic
- List of "sonnet-safe" tasks
- Warning about complex tasks requiring Opus

**Template References**:
- Current epic's task list
- [Testing Standards](workflows/TESTING-STANDARDS.md) for test implementation

**Progressive Documentation**: Updates epic task status, adds implementation notes

### `/test-verify`
**Purpose**: Verify testing infrastructure readiness  
**When to Use**: At Gate 3.5, before development begins  
**Expected Output**:
```
Testing Infrastructure Status:
✓ Jest configured and running
✓ Coverage reporting: 0% (expected before development)
✓ Test database configured
✗ E2E framework not installed
✓ Sample unit test passing
✗ CI/CD pipeline not configured

Ready for development: NO
Missing: E2E framework, CI/CD setup
```

**Template References**:
- [Testing setup guides](CLAUDE.md#standard-testing-setup-by-stack)
- Tech-specific test configurations

**Progressive Documentation**: Creates test status report in epic

---

## Handoff Commands

### `/handoff-claude`
**Purpose**: Generate handoff from Sonnet to Opus  
**When to Use**: When Sonnet encounters blocking issues after 3 attempts  
**Expected Output**:
```markdown
## Handoff to Opus Model

**From**: Sonnet
**Date**: [timestamp]
**Epic**: [current epic]

### Blocked Tasks
1. **Task**: [task description]
   - **Error**: [error details]
   - **Attempts**: 3
   - **Context**: [relevant code/config]
   - **Suggested Approach**: [if any]

### Completed Tasks
- [list of completed tasks since last handoff]

### Files Modified
- [list of changed files]

### Next Steps for Opus
1. Resolve blocked tasks
2. Update epic planning if needed
3. Provide detailed instructions for Sonnet
```

**Progressive Documentation**: Appends to epic's "Handoff History" section

### `/handoff-gemini`
**Purpose**: Generate strategic review handoff  
**When to Use**: After completing major features or reaching gates  
**Expected Output**:
```markdown
## Handoff to Gemini Strategic Review

**From**: Claude Code
**Date**: [timestamp]
**Phase**: [current phase]

### Updated Files for Review
- PRD: [version and changes]
- Epics: [list of modified epics]
- Code: [key implementation files]

### Strategic Questions
1. [Architecture concerns]
2. [Performance considerations]
3. [Security review points]

### Request
"Gemini, please perform a [specific type] review of [product-name]. 
Key files: [list]. Focus areas: [specific concerns]."
```

**Progressive Documentation**: Creates review request in PRD

---

## Workflow Navigation Commands

### `/epic-status`
**Purpose**: Generate comprehensive epic status  
**When to Use**: Daily progress checks, before handoffs  
**Expected Output**:
- Summary of all epics with completion percentages
- Blocked tasks across all epics
- Recently completed milestones
- Upcoming critical tasks

**Template References**: Epic metadata headers for status tracking

**Progressive Documentation**: Updates DEVELOPMENT_STATUS.md

### `/doc-sync`
**Purpose**: Ensure documentation consistency  
**When to Use**: After major updates, before handoffs  
**Expected Output**:
- Version alignment check (PRD, epics, briefs)
- Outdated references identified
- Suggested updates listed
- Progressive documentation compliance report

---

## Best Practices

### Command Usage Flow
1. **Start Planning**: `/plan` → Load Opus-optimized templates
2. **Check Readiness**: `/gate-check` → Validate phase completion
3. **Setup Testing**: `/test-verify` → Ensure infrastructure ready
4. **Begin Coding**: `/execute` → Switch to Sonnet with clear tasks
5. **Handle Blocks**: `/handoff-claude` → Document issues for Opus
6. **Request Review**: `/handoff-gemini` → Prepare strategic review

### Progressive Documentation with Commands
- Commands should UPDATE existing documents, not create new ones
- Each command output includes version increment guidance
- Handoffs append to history sections, don't replace content
- Status updates modify metadata headers

### Model-Aware Command Usage
While commands work with any model, optimal usage:
- **Opus**: `/plan`, `/gate-check`, reviewing `/handoff-claude` outputs
- **Sonnet**: `/execute`, `/test-verify`, generating `/handoff-claude`
- **Either**: `/epic-status`, `/doc-sync`, `/handoff-gemini`

---

## Implementation Notes

These commands are conceptual workflow aids. They:
- Provide structured reminders for model switching
- Reference appropriate templates and documentation
- Enforce progressive documentation principles
- Maintain consistency across the APOLLO workflow

Future enhancements could include:
- Automated template loading
- Real-time status tracking
- Integration with MCP servers
- Custom command shortcuts for common workflows

---

*For workflow details, see [WORKFLOW-MASTER.md](workflows/WORKFLOW-MASTER.md)*  
*For model usage guidelines, see [MODEL-USAGE-GUIDE.md](workflows/MODEL-USAGE-GUIDE.md)*