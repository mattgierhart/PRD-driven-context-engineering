# CFD- Post-Launch Feedback Template

Copy and fill for each feedback item captured post-launch:

```
CFD-XXX: [Feedback Title]
Type: [Support Ticket | Feature Request | Bug Report | NPS Response | Community Post | Survey Response]
Source: [Intercom | Zendesk | Discord | In-App | Email | Twitter | Other]
Date: [YYYY-MM-DD]
User Segment: [PER-XXX if identifiable]

Verbatim: "[Exact user quote or description]"

Processed:
  Category: [UX | Performance | Feature Gap | Bug | Praise | Confusion]
  Sentiment: [Positive | Neutral | Negative | Frustrated]
  Priority: [Critical | High | Medium | Low]
  Frequency: [One-off | Repeated | Trending]

Impact Assessment:
  Users Affected: [Count or estimate]
  KPI Impact: [KPI-XXX affected if applicable]
  Revenue Risk: [High | Medium | Low | None]

Action:
  Response: [How we responded to user]
  Internal Action: [What we're doing about it]
  Linked IDs: [BR-XXX, FEA-XXX, RISK-XXX created/updated]
  Status: [New | Acknowledged | In Progress | Resolved | Won't Fix]

Resolution:
  Outcome: [What happened]
  Date: [YYYY-MM-DD]
  Follow-up: [Did we close the loop with user?]
```

---

## Field Reference

### Type Selection

| Type | When to Use |
|------|-------------|
| Support Ticket | User contacted support with question/issue |
| Feature Request | User explicitly asked for new functionality |
| Bug Report | User reported something broken |
| NPS Response | Feedback from Net Promoter Score survey |
| Community Post | Feedback from Discord, forum, social media |
| Survey Response | Feedback from scheduled surveys |

### Category Selection

| Category | Signals |
|----------|---------|
| UX | "Can't find", "confusing", "don't understand" |
| Performance | "Slow", "takes forever", "timeout" |
| Feature Gap | "Wish it could", "need to", "missing" |
| Bug | "Broken", "error", "doesn't work" |
| Praise | "Love it", "amazing", "exactly what I needed" |
| Confusion | "Expected X but got Y", "unclear" |

### Priority Selection

| Priority | Criteria |
|----------|----------|
| Critical | Data loss, security, blocks core journey, multiple reports |
| High | Impacts main features, revenue risk, frequent reports |
| Medium | Degraded experience, workaround exists |
| Low | Edge case, minor inconvenience, single report |

### Frequency Assessment

| Frequency | Definition |
|-----------|------------|
| One-off | First time seeing this feedback |
| Repeated | Seen 2-5 times from different users |
| Trending | Growing volume, becoming common |

---

## Examples

### Feature Request (High Priority)

```
CFD-101: "Can't figure out how to export my data"
Type: Support Ticket
Source: Intercom
Date: 2025-01-15
User Segment: PER-001 (Startup Founder)

Verbatim: "I've been using the tool for a week and I can't find
          any way to export my work. I need to share results with
          my team. Is this possible? If not, this is a dealbreaker."

Processed:
  Category: Feature Gap
  Sentiment: Frustrated
  Priority: High
  Frequency: Repeated (3rd request this week)

Impact Assessment:
  Users Affected: ~50 (based on support volume)
  KPI Impact: KPI-104 (D7 Retention) — export needed for team use case
  Revenue Risk: High — multiple users mentioned "dealbreaker"

Action:
  Response: "Thanks for reaching out! Export is on our roadmap.
             We're prioritizing this for our next release."
  Internal Action: Escalated to product team, added to backlog
  Linked IDs: FEA-025 (Export Feature) created, EPIC-05 updated
  Status: In Progress

Resolution:
  Outcome: FEA-025 shipped in v1.2
  Date: 2025-02-01
  Follow-up: Emailed user with release notes
```

### NPS Detractor (Critical)

```
CFD-102: NPS Detractor Response
Type: NPS Response
Source: In-App Survey
Date: 2025-01-18
User Segment: PER-002 (Team Lead)

Verbatim: "Score: 4. Too slow. Takes forever to load projects
          and I give up waiting half the time."

Processed:
  Category: Performance
  Sentiment: Negative
  Priority: Critical
  Frequency: Trending (NPS dropped 10 points this week)

Impact Assessment:
  Users Affected: ~200 (20% of NPS responses mention speed)
  KPI Impact: KPI-103 (Activation), KPI-104 (Retention)
  Revenue Risk: High — performance is activation blocker

Action:
  Response: N/A (anonymous survey)
  Internal Action: Performance spike investigation started
  Linked IDs: RISK-012 (Performance Degradation) escalated
  Status: In Progress

Resolution:
  Outcome: Database query optimization deployed
  Date: 2025-01-22
  Follow-up: Next NPS cycle will measure improvement
```

### Community Feature Discussion (Medium)

```
CFD-103: Community Feature Discussion
Type: Community Post
Source: Discord #feature-requests
Date: 2025-01-20
User Segment: Power Users (multiple PER-)

Verbatim: "Thread: 47 messages discussing dark mode.
          Summary: 15 unique users requesting dark mode.
          Top comment: 'I work at night and this is eye-strain city.'"

Processed:
  Category: Feature Gap
  Sentiment: Neutral (constructive)
  Priority: Medium
  Frequency: Repeated (ongoing thread)

Impact Assessment:
  Users Affected: 15+ vocal, likely more silent
  KPI Impact: Minor — nice-to-have, not activation blocker
  Revenue Risk: Low

Action:
  Response: Community manager acknowledged, added to public roadmap
  Internal Action: Added to backlog as P2
  Linked IDs: FEA-030 (Dark Mode) created
  Status: Acknowledged

Resolution:
  Outcome: Pending — scheduled for Q2
  Date: N/A
  Follow-up: Posted on public roadmap
```

### Praise (Testimonial)

```
CFD-104: User Success Story
Type: Support Ticket
Source: Email
Date: 2025-01-25
User Segment: PER-001 (Startup Founder)

Verbatim: "I just wanted to say thank you. This tool helped us
          close our first enterprise client. The proposal we built
          using your platform impressed them so much they signed
          same-day. You've literally changed our business."

Processed:
  Category: Praise
  Sentiment: Positive
  Priority: Low (for triage)
  Frequency: One-off (unique story)

Impact Assessment:
  Users Affected: 1 (but testimonial value for many)
  KPI Impact: Validates KPI-101 (Revenue impact)
  Revenue Risk: None

Action:
  Response: Thanked user, asked for permission to use as testimonial
  Internal Action: Shared with team, added to success stories
  Linked IDs: GTM-015 (Customer Testimonials) updated
  Status: Resolved

Resolution:
  Outcome: User approved case study, featured on landing page
  Date: 2025-02-05
  Follow-up: Sent company swag as thanks
```

---

## Aggregation Template

Weekly or monthly, aggregate CFD- entries:

```
Feedback Summary: [Date Range]
================================

Volume:
- Total: [X] feedback items
- By Type: Support [X], Feature [X], Bug [X], NPS [X], Other [X]
- By Priority: Critical [X], High [X], Medium [X], Low [X]

Sentiment:
- Positive: [X%]
- Neutral: [X%]
- Negative: [X%]
- NPS Score: [X] (up/down from last period)

Top Themes:
1. [Theme] — [X] mentions, [linked IDs]
2. [Theme] — [X] mentions, [linked IDs]
3. [Theme] — [X] mentions, [linked IDs]

Actions Taken:
- FEA-XXX created based on [X] requests
- RISK-XXX escalated due to [X] reports
- BR-XXX updated to address [X] confusion

Response Metrics:
- Avg first response: [X] hours
- Resolution rate: [X%]
- Loop closed with user: [X%]
```
