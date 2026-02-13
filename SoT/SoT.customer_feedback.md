---
version: 1.0
purpose: Source of Truth for customer feedback, user research insights, and validated learnings.
id_prefix: CFD-XXX
last_updated: YYYY-MM-DD
authority: This is a SoT file - IDs here are referenced by PRD.md, SoT.USER_JOURNEYS.md, EPICs
---
<!-- SECTION: template-structure -->

# Customer Feedback (SoT File)

> **Purpose**: Capture durable insights from customer feedback, user research, and validated learnings.
> **ID Prefix**: CFD-XXX
> **Status**: Active SoT file
> **Cross-References**: Referenced by PRD.md, SoT.USER_JOURNEYS.md, SoT.BUSINESS_RULES.md

## Navigation by Category

**User Research** (CFD-001 to CFD-099):

- [CFD-001](#cfd-001-insight-name) - {Insight name}

**Feature Requests** (CFD-101 to CFD-199):

- [CFD-101](#cfd-101-request-name) - {Request name}

**Bug Reports** (CFD-201 to CFD-299):

- [CFD-201](#cfd-201-issue-name) - {Issue name}

**General Feedback** (CFD-301 to CFD-399):

- [CFD-301](#cfd-301-feedback-name) - {Feedback name}

---

## CFD-001: {Insight Name}

**ID**: CFD-001
**Category**: User Research | Feature Request | Bug Report | General
**Status**: New | Analyzed | Actioned | Declined
**Priority**: Critical | High | Medium | Low
**Created**: YYYY-MM-DD
**Last Updated**: YYYY-MM-DD
**Reported By**: {User segment or count}

### Feedback Summary

**What Users Said**: {Summary of the feedback in user's words.}

**User Context**:

- User tier: {Free/Paid/Enterprise}
- User segment: {Persona or segment}
- First reported: YYYY-MM-DD
- Total reports: {Number of users reporting this}

### Problem Statement

**Current Behavior**: {What happens now}
**Expected Behavior**: {What users expect}
**Impact**: {How this affects users}

**Pain Level**: Low | Medium | High | Critical

### Related IDs

- [UJ-XXX](SoT.USER_JOURNEYS.md#uj-xxx) - {Affected journey}
- [BR-XXX](SoT.BUSINESS_RULES.md#br-xxx) - {Related rule}
- [FEA-XXX in PRD](../PRD.md) - {Feature addressing this}

### Product Decision

**Decision**: Implement | Defer | Decline | Needs Research
**Decision Date**: YYYY-MM-DD
**Decision Maker**: {Role/Name}
**Rationale**: {Why this decision was made}

<!-- /SECTION: template-structure -->

---
<!-- CUSTOMIZABLE: entries -->

## Deprecated Entries

### CFD-XXX: {Name} [DEPRECATED]

**Status**: Deprecated (YYYY-MM-DD)
**Reason**: {Why deprecated - addressed, no longer relevant, etc.}

<!-- /CUSTOMIZABLE: entries -->

---

## Cross-Reference Index

**Feedback by Journey**:

- UJ-001 feedback: CFD-001, CFD-101

**Feedback by Status**:

- Actioned: CFD-001
- Pending: CFD-101

---

## Update Protocol

### When to Add New CFD-XXX IDs

1. **User Research**: Validated insight from research sessions
2. **Feature Request**: Request from multiple users or key accounts
3. **Bug Report**: User-reported issue with product impact
4. **General Feedback**: Pattern observed across multiple interactions

### Bidirectional Reference Checklist

When adding a new CFD-XXX:

- [ ] Link to affected UJ-XXX in SoT.USER_JOURNEYS.md
- [ ] Update PRD.md if creating new feature to address
- [ ] Update SoT.BUSINESS_RULES.md if rule change needed
- [ ] Update EPIC if feedback relates to active work

---

*End of SoT.customer_feedback.md - Authoritative source for all CFD-XXX IDs*
