---
title: "Customer Feedback Insights"
scope: "source_of_truth/customer_feedback.md"
updated: "2025-11-15"
---

# Customer Feedback (SoT File)

> **Purpose**: Capture durable insights from teams applying Gear Heart Methodology in the field.
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

### Key Learnings for GHM

1. **Specification Discipline** — Reinforce that prompt quality is proportional to the clarity of SoT-backed requirements. Builders need quick reminders to translate user needs into explicit acceptance criteria before delegating to AI.  
2. **Real-User Loops** — Encourage immediate testing with actual users (even one) to prevent overbuilding. Feedback loops should be visible in EPIC checklists.  
3. **Mobile-First Verification** — Promote early validation on real devices, not just responsive previews, to avoid late-stage layout fixes.  
4. **Distribution Visibility** — Highlight that launch tasks (audience building, pricing experiments) must appear in planning artifacts so builders do not stop at “code complete.”

### Related IDs

- Referenced in PRD: Pending — incorporate into next PRD revision where mobile coverage or GTM strategy is defined.  
- Addressed by EPICs: To be scheduled.

### Product Decision

**Decision**: Implement learnings through documentation updates.  
**Decision Date**: 2025-11-15  
**Decision Maker**: Repository maintainers  
**Rationale**: Aligns with mission to make AI collaboration predictable; low implementation cost; high leverage across contributors.

### Implementation Notes

- Update CLAUDE.md execution rules to stress SoT-grounded prompts and early mobile testing.
- Add distribution reminders to planning workflows when next revised.
- Monitor future field reports to see if additional SoT entries (e.g., BR, UJ) should codify these behaviors.

### Linked Instruction Updates

- `docs/prd/instructions/README.md` — directs editors to consult this entry before adjusting stage playbooks so field learnings propagate quickly.
- `docs/prd/instructions/v0.4/` — embeds real-user loops and mobile-first validation requirements into both research and intake flows.
- `docs/prd/instructions/v0.5/aura_intake.md` — adds a distribution readiness gate so launch motions are tracked with the same rigor as build tasks.
- `docs/prd/instructions/v0.6/aura_intake.md` — codifies SoT-grounded prompt prep and device validation expectations before architecture sign-off.

---
