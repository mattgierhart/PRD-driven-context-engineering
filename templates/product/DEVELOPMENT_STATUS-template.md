---
version: 1.1
purpose: To provide a real-time, comprehensive overview of a project's development status, covering everything from sprint progress to key metrics and blockers.
summary: Added a standardized metadata header and a contextual "Authority, Template Usage, and Standards" section.
last_updated: 2025-07-02
---

# Development Status: [Product Name]

## Authority, Template Usage, and Standards

- **Authority**: This status document is a key artifact in the project management workflow defined in [WORKFLOW-MASTER.md](../workflows/WORKFLOW-MASTER.md).
- **Template Usage**: See the [Template Usage Guide](./README.md) for how to maintain and update this document. It should be updated at least weekly.
- **Standards**: All information reported here must be accurate and align with the project standards in [STANDARDS.md](../../STANDARDS.md).

**Last Updated**: [Date Time]
**Sprint**: [Current Sprint Number/Name]
**Phase**: [Discovery/Development/Testing/Launch]

## Current Sprint Overview

### Sprint Goals
1. [Primary goal for this sprint]
2. [Secondary goal]
3. [Tertiary goal]

### Sprint Timeline
- **Start Date**: [Date]
- **End Date**: [Date]
- **Days Remaining**: [X]

## Progress Summary

### Completed This Sprint ✅
- [x] [Completed feature/task 1]
- [x] [Completed feature/task 2]
- [x] [Completed feature/task 3]

### In Progress 🚧
- [ ] [Task 1] - 75% complete - [Assignee]
- [ ] [Task 2] - 50% complete - [Assignee]
- [ ] [Task 3] - 25% complete - [Assignee]

### Upcoming This Sprint 📋
- [ ] [Planned task 1]
- [ ] [Planned task 2]
- [ ] [Planned task 3]

## Key Metrics

### Development Velocity
- **Story Points Completed**: [X/Y]
- **Features Shipped**: [X]
- **Bugs Fixed**: [X]
- **Tech Debt Addressed**: [X items]

### Quality Metrics
- **Test Coverage**: [X]%
- **Build Success Rate**: [X]%
- **Performance Score**: [X/100]
- **Open Issues**: [X]

### Business Metrics
- **Active Users**: [X]
- **Revenue**: $[X] MRR
- **Conversion Rate**: [X]%
- **Churn Rate**: [X]%

## Blockers & Issues 🚨

### Critical Blockers
1. **[Blocker Title]**
   - **Impact**: [High/Medium/Low]
   - **Description**: [What's blocking progress]
   - **Action Needed**: [What needs to happen]
   - **Owner**: [Who can unblock]
   - **ETA**: [When it will be resolved]

### Technical Issues
1. **[Issue Title]**
   - **Severity**: [Critical/Major/Minor]
   - **Description**: [Issue details]
   - **Workaround**: [Temporary solution if any]
   - **Fix ETA**: [Expected resolution date]

## Next Sprint Planning

### Priority Queue
1. **P0 - Must Have**
   - [ ] [Critical feature 1]
   - [ ] [Critical feature 2]

2. **P1 - Should Have**
   - [ ] [Important feature 1]
   - [ ] [Important feature 2]

3. **P2 - Nice to Have**
   - [ ] [Enhancement 1]
   - [ ] [Enhancement 2]

### Resource Allocation
- **Engineering**: [X] developers available
- **Design**: [X] hours allocated
- **QA**: [X] hours allocated
- **DevOps**: [X] hours allocated

## Technical Debt Tracker

### High Priority Debt
- [ ] [Debt item 1] - [Impact: Performance/Security/Maintenance]
- [ ] [Debt item 2] - [Impact: Performance/Security/Maintenance]

### Medium Priority Debt
- [ ] [Debt item 1] - [Impact description]
- [ ] [Debt item 2] - [Impact description]

### Debt Metrics
- **Total Debt Items**: [X]
- **Debt Ratio**: [X]% of codebase
- **Average Age**: [X] days
- **Resolution Rate**: [X] items/sprint

## Feature Status

### Live Features 🟢
| Feature | Launch Date | Adoption | Performance |
|---------|------------|----------|-------------|
| [Feature 1] | [Date] | [X]% users | [Metrics] |
| [Feature 2] | [Date] | [X]% users | [Metrics] |

### Beta Features 🟡
| Feature | Beta Users | Feedback Score | GA Date |
|---------|------------|----------------|---------|
| [Feature 1] | [X] | [X]/10 | [Date] |
| [Feature 2] | [X] | [X]/10 | [Date] |

### In Development 🔵
| Feature | Progress | Target Date | Dependencies |
|---------|----------|-------------|--------------|
| [Feature 1] | [X]% | [Date] | [List] |
| [Feature 2] | [X]% | [Date] | [List] |

## Infrastructure Status

### System Health
- **Uptime**: [X]% (last 30 days)
- **Response Time**: [X]ms average
- **Error Rate**: [X]%
- **Database Size**: [X] GB

### Recent Incidents
| Date | Issue | Duration | Impact | Resolution |
|------|-------|----------|--------|------------|
| [Date] | [Issue] | [Xm] | [Users affected] | [Fix applied] |

### Upcoming Maintenance
- [ ] [Maintenance task 1] - [Date]
- [ ] [Maintenance task 2] - [Date]

## Team Updates

### Wins 🎉
- [Team win 1]
- [Team win 2]
- [Team win 3]

### Challenges 😅
- [Challenge 1] - [How we're addressing it]
- [Challenge 2] - [How we're addressing it]

### Team Health
- **Morale**: [High/Medium/Low]
- **Capacity**: [X]% utilized
- **Burnout Risk**: [Low/Medium/High]

## Customer Feedback

### Recent Feedback
1. **[Feature Request]** - [X] votes
2. **[Bug Report]** - Status: [Fixed/In Progress/Backlog]
3. **[Improvement Suggestion]** - Priority: [High/Medium/Low]

### NPS Score: [X]
- Promoters: [X]%
- Passives: [X]%
- Detractors: [X]%

## Financial Status

### Revenue Tracking
- **MRR**: $[Current] (Target: $[X])
- **Growth Rate**: [X]% MoM
- **CAC**: $[X]
- **LTV**: $[X]
- **Runway**: [X] months

### Cost Management
- **Infrastructure**: $[X]/month
- **Tools/Services**: $[X]/month
- **Total Burn**: $[X]/month

## Action Items

### This Week
1. [ ] [Action 1] - Owner: [Name] - Due: [Date]
2. [ ] [Action 2] - Owner: [Name] - Due: [Date]
3. [ ] [Action 3] - Owner: [Name] - Due: [Date]

### Decisions Needed
1. **[Decision 1]**
   - Options: [A, B, C]
   - Recommendation: [Option]
   - Deadline: [Date]

## Sub-Agent Tasks

### Automated Analysis
```bash
# Weekly tech debt check
@tech-debt-finder-fixer . --report-only

# Performance validation
@perf-optimize . --analyze

# Architecture health
@arch-review . --quick-scan
```

### Suggested Improvements
Based on current status:
1. Consider running: `@refactor [high-complexity-file]`
2. Generate tests for new features: `@test-gen [new-feature-dir]`
3. Optimize slow endpoints: `@perf-optimize api/ --focus-on-slow`

## Notes & Comments

### Important Reminders
- [Reminder 1]
- [Reminder 2]

### Dependencies
- Waiting on [external dependency]
- Blocked by [internal process]

### Risks
- [Risk 1]: [Mitigation plan]
- [Risk 2]: [Mitigation plan]

---

## Quick Links
- [Project Board](link)
- [Architecture Docs](link)
- [API Documentation](link)
- [Deployment Guide](link)
- [Team Calendar](link)

---
*Status updated by: [Name] | Next update: [Date]*