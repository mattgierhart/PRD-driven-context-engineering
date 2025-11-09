---
version: 1.0
purpose: Source of Truth file for customer feedback and insights. Each feedback item has a unique ID for cross-referencing.
id_prefix: CFD-XXX
last_updated: YYYY-MM-DD
authority: This is a SoT file - IDs created here are referenced by PRD.md, USER-JOURNEYS.md, BUSINESS_RULES.md, EPICs
---

# Customer Feedback (SoT File)

> **Purpose**: Centralized tracking of customer feedback, feature requests, and user insights.
> **ID Prefix**: CFD-XXX
> **Status**: Active SoT file
> **Cross-References**: Referenced by PRD.md, USER-JOURNEYS.md, BUSINESS_RULES.md, EPICs

## Navigation by Category

**Feature Requests** (CFD-001 to CFD-099):
- [CFD-001](#cfd-001-feedback-title) - {Feature request summary}
- [CFD-002](#cfd-002-feedback-title) - {Feature request summary}

**Bug Reports** (CFD-101 to CFD-199):
- [CFD-101](#cfd-101-feedback-title) - {Bug report summary}

**Usability Issues** (CFD-201 to CFD-299):
- [CFD-201](#cfd-201-feedback-title) - {Usability issue summary}

**Positive Feedback** (CFD-301 to CFD-399):
- [CFD-301](#cfd-301-feedback-title) - {Positive feedback summary}

**General Comments** (CFD-401 to CFD-499):
- [CFD-401](#cfd-401-feedback-title) - {General comment summary}

---

## CFD-001: {Feedback Title}

**ID**: CFD-001
**Category**: Feature Request | Bug Report | Usability Issue | Positive Feedback | General Comment
**Status**: New | Under Review | Planned | In Progress | Implemented | Declined | Duplicate
**Priority**: Critical | High | Medium | Low
**Created**: YYYY-MM-DD
**Last Updated**: YYYY-MM-DD
**Reported By**: {Number} users | {Customer name/segment}

### Feedback Summary

**What Users Said**: {Direct quote or paraphrased feedback from users}

**User Context**:
- User tier: Free | Basic | Pro | Enterprise
- User segment: {SMB | Enterprise | Individual | etc.}
- Platform: Web | iOS | Android | Desktop
- First reported: YYYY-MM-DD
- Total reports: {X} users

### Problem Statement

**Current Behavior**: {What happens now that users don't like}
**Expected Behavior**: {What users expect or want to happen}
**Impact**: {How this affects user experience, business metrics, or revenue}

**Pain Level**:
- Critical: Blocks core workflows
- High: Significant friction in important tasks
- Medium: Minor inconvenience in regular use
- Low: Nice-to-have improvement

### User Stories

**As a** {user type},
**I want** {capability},
**So that** {benefit}.

**Example**:
> As a household manager,
> I want to share product warranties with family members,
> So that anyone can file a claim when needed.

### Related IDs

**Affects User Journeys**:
- [UJ-XXX](USER-JOURNEYS.md#uj-xxx) - {Journey where issue occurs}
- [UJ-YYY](USER-JOURNEYS.md#uj-yyy) - {Another affected journey}

**Related Business Rules**:
- [BR-XXX](BUSINESS_RULES.md#br-xxx) - {Business rule that might need adjustment}

**Involves APIs**:
- [API-XXX](API_CONTRACTS.md#api-xxx) - {API that needs changes}

**Database Impact**:
- [DBT-XXX](ACTUAL-SCHEMA.md#dbt-xxx) - {Table that needs schema changes}

**Referenced in PRD**:
- Section: [PRD.md#{section}](PRD.md#{section}) - {Where this is addressed in PRD}

**Addressed by EPICs**:
- [EPIC-XX](epics/EPIC-XX-{name}.md) - {EPIC implementing this feedback}

**Duplicate Of** (if applicable):
- [CFD-YYY](#cfd-yyy-feedback-title) - Original feedback item

### Product Decision

**Decision**: Implement | Decline | Defer | Under Review
**Decision Date**: YYYY-MM-DD
**Decision Maker**: Product Owner | Engineering Lead | CEO

**Rationale**:
{Why we made this decision. Include:}
- Business alignment: {How this aligns with product strategy}
- Technical feasibility: {Implementation complexity}
- Resource requirements: {Effort estimate}
- ROI analysis: {Expected impact vs cost}

**If Declined**:
- Reason: {Why we chose not to implement}
- Alternative: {What users can do instead}
- Communication: {How we'll respond to users}

**If Deferred**:
- Planned for: {Future release/milestone}
- Conditions: {What needs to happen first}
- Review date: {When we'll revisit}

### Implementation Plan

**Proposed Solution**: {High-level approach to address feedback}

**Acceptance Criteria**:
- [ ] {Criterion 1 - must be measurable}
- [ ] {Criterion 2 - must be testable}
- [ ] {Criterion 3 - must satisfy original feedback}

**Success Metrics**:
- User satisfaction: Target {X}% improvement
- Task completion: Target {Y}% faster
- Error rate: Target <{Z}%
- Adoption rate: Target {W}% of users

**Implementation Status**:
- EPIC: [EPIC-XX](epics/EPIC-XX-{name}.md)
- Target Release: vX.Y.Z
- Estimated Delivery: YYYY-MM-DD
- Actual Delivery: YYYY-MM-DD

### Quantitative Data

**Frequency**:
- Reports per week: {X}
- Affected users: {Y} ({Z}% of active users)
- Support tickets: {W} tickets

**Impact Metrics**:
- Task abandonment rate: {X}%
- Average time to complete: {Y} seconds
- Error occurrences: {Z} per 1000 sessions
- NPS impact: {-W points}

**Business Impact**:
- Churn risk: {X users threatened to leave}
- Revenue at risk: ${Y}/month
- Support cost: ${Z}/month
- Competitive gap: {Assessment}

### Qualitative Insights

**User Quotes**:

> "This is frustrating because..."
> — User A, Free tier, iOS, 2025-11-01

> "I expected it to work like..."
> — User B, Pro tier, Android, 2025-11-03

**Common Themes**:
- {Theme 1}: {X}% of feedback mentions this
- {Theme 2}: {Y}% of feedback mentions this
- {Theme 3}: {Z}% of feedback mentions this

**Sentiment Analysis**:
- Frustrated: {X}%
- Confused: {Y}%
- Disappointed: {Z}%
- Satisfied (after workaround): {W}%

### Supporting Evidence

**Screenshots/Videos**:
- [Link to user recording showing issue]
- [Link to screenshot of confusion]

**Session Recordings**:
- Session IDs: {list of relevant session replay IDs}
- Heatmaps: {link to heatmap showing problematic UI}

**Analytics Data**:
- Event: `{event_name}` - {X} occurrences
- Funnel drop-off: {Y}% at step Z
- Time on task: {W} seconds (vs. {V} second target)

### Communication Log

**User Communication**:

| Date | Channel | Response | Follow-up |
|------|---------|----------|-----------|
| 2025-11-01 | Email | Acknowledged, investigating | Promised update in 2 weeks |
| 2025-11-15 | Email | Planned for next sprint | Will notify when shipped |
| 2025-12-01 | Email | Feature shipped | Requested feedback |

**Internal Communication**:
- Engineering sync: Discussed on 2025-11-05
- Product review: Prioritized on 2025-11-08
- Stakeholder update: CEO informed 2025-11-10

### Competitive Analysis

**How Competitors Handle This**:
- Competitor A: {How they solve this problem}
- Competitor B: {Their approach}
- Industry standard: {Common pattern}

**Differentiation Opportunity**:
{How we can do this better than competitors}

### Related Feedback

**Similar Requests**:
- [CFD-YYY](#cfd-yyy-similar-request) - Similar feedback from different angle
- [CFD-ZZZ](#cfd-zzz-related-issue) - Related but distinct issue

**Opposite Feedback** (if any):
- [CFD-WWW](#cfd-www-opposing-view) - Users who prefer current behavior

### Post-Implementation Follow-up

**User Validation** (after implementation):
- Re-surveyed users: {X} responded
- Satisfaction improvement: {Y}% → {Z}%
- Issue resolved: Yes | Partially | No
- New issues surfaced: {List any new problems}

**Metrics Post-Launch**:
- Feature adoption: {X}% of users
- Task completion improvement: {Y}% faster
- Error rate reduction: {Z}% → {W}%
- Support ticket reduction: {V}%

### Lessons Learned

**What Worked Well**:
- {Insight about successful implementation}

**What Could Be Better**:
- {Insight about improvement opportunities}

**For Future Reference**:
- {Pattern to reuse or avoid}

### Version History

| Version | Date | Changes | Updated By |
|---------|------|---------|------------|
| 1.0 | YYYY-MM-DD | Initial feedback captured | {Name} |
| 1.1 | YYYY-MM-DD | Added quantitative data | {Name} |
| 2.0 | YYYY-MM-DD | Marked as implemented | {Name} |

---

## CFD-002: {Next Feedback Item}

{Repeat the above structure for each feedback item}

---

## Implemented Feedback

### CFD-XXX: {Implemented Feedback Title} [IMPLEMENTED]

**Status**: Implemented (YYYY-MM-DD)
**Implemented In**: [EPIC-YY](epics/EPIC-YY-{name}.md)
**Release Version**: vX.Y.Z
**Success Metrics**: {Brief summary of post-implementation results}

---

## Declined Feedback

### CFD-XXX: {Declined Feedback Title} [DECLINED]

**Status**: Declined (YYYY-MM-DD)
**Reason**: {Brief explanation of why declined}
**Alternative**: {What users can do instead}
**User Communication**: {How we communicated this decision}

---

## Cross-Reference Index

> **Auto-Generated Section**: Run `npm run codex:sync-feedback` to rebuild

**Feedback by User Journey**:
- UJ-101 feedback: CFD-001, CFD-045, CFD-203
- UJ-102 feedback: CFD-002, CFD-102

**Feedback by Business Rule**:
- BR-001 related: CFD-001, CFD-012
- BR-112 related: CFD-045

**Feedback by Priority**:
- Critical: CFD-001, CFD-105
- High: CFD-002, CFD-012, CFD-046
- Medium: CFD-003, CFD-013

**Feedback by Status**:
- Implemented: CFD-xxx, CFD-yyy (count: X)
- In Progress: CFD-zzz (count: Y)
- Planned: CFD-www (count: Z)
- Under Review: CFD-vvv (count: W)
- Declined: CFD-uuu (count: V)

**Feedback by User Segment**:
- Free tier: CFD-001, CFD-012
- Pro tier: CFD-002, CFD-045
- Enterprise: CFD-105, CFD-203

---

*End of customer-feedback.md - This SoT file is the authoritative source for all CFD-XXX IDs*

## Feedback Collection Process

**Collection Channels**:
- In-app feedback widget
- Email: feedback@{product}.com
- Support tickets: Intercom/Zendesk
- User interviews: Scheduled sessions
- Social media: Twitter, Reddit mentions
- App store reviews: Monitored weekly

**Triage Process**:
1. Support team captures raw feedback
2. Product Owner assigns CFD-XXX ID
3. Categorize and prioritize
4. Link to relevant IDs (UJ, BR, API)
5. Add to PRD or EPIC as appropriate
6. Communicate status to user

**Review Cadence**:
- New feedback: Triaged within 48 hours
- Priority review: Weekly product sync
- Quarterly: Review all "Under Review" items
- Annually: Audit declined items for reconsideration
