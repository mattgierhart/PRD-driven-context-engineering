---
title: "Customer Feedback Insights"
scope: "source_of_truth/SoT.customer_feedback.md"
updated: "2025-11-15"
---

# Customer Feedback (SoT File)

> **Purpose**: Capture durable insights from teams applying PRD Led Context Engineering in the field.
> **ID Prefix**: CFD-XXX
> **Status**: Active SoT file
> **Cross-References**: PRD.md, README.md, CLAUDE.md, EPIC files

## Navigation by Category

**General Comments** (CFD-401 to CFD-499):
- [CFD-401](#cfd-401-partial-ghm-adoption-during-48-hour-inventory-build) - Partial GHM adoption during 48-hour inventory build

---

## CFD-401: Partial GHM Adoption During 48-Hour Inventory Build

**ID**: CFD-401  
**Category**: General Comment  
**Status**: Analyzed  
**Priority**: Medium  
**Created**: 2025-11-15  
**Last Updated**: 2025-11-15  
**Reported By**: 1 indie developer building SaaS for salon inventory

### Feedback Summary

**What Users Said**: A solo developer used only fragments of the Gear Heart process while building a salon inventory SaaS in 48 hours. They highlighted that AI produced quality code only when prompts were highly specific, real-time feedback from the target user prevented scope bloat, and late mobile testing caused costly rework. Distribution remained the hardest part after launch.

**User Context**:
- User tier: Independent builder exploring GHM practices  
- User segment: Indie SaaS creator supporting SMB clients  
- Platform: Web/mobile responsive app (Next.js, Supabase, Tailwind)  
- First reported: 2025-11-15  
- Total reports: 1

### Problem Statement

**Current Behavior**: Builders referencing GHM assets may skip critical upfront specification work, defer mobile validation, and underemphasize go-to-market planning when under tight deadlines.  
**Expected Behavior**: The methodology should make it easy—even under time pressure—to define precise AI prompts tied to requirements, mandate early device-specific testing, and surface GTM/distribution tasks alongside build work.  
**Impact**: Missed guidance increases rework, risks misaligned AI output, and leaves builders without a structured path for distribution.

**Pain Level**: Medium – Process gaps slow delivery and create avoidable churn, but do not block shipping entirely.

### Related IDs

- Referenced in PRD: Pending — incorporate into next PRD revision where mobile coverage or GTM strategy is defined.  
- Addressed by EPICs: To be scheduled.

### Product Decision

**Decision**: Implement learnings through documentation updates.  
**Decision Date**: 2025-11-15  
**Decision Maker**: Repository maintainers  
**Rationale**: Aligns with mission to make AI collaboration predictable; low implementation cost; high leverage across contributors.

---
