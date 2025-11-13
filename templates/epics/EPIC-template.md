---
version: 4.0
purpose: Execution container for a single lifecycle window. Tracks scope, SoT IDs, and gate movement.
last_updated: 2025-01-05
authority: Pair with `workflows/PRD-VERSION-LIFECYCLE.md` for gate rituals and reviews.
---

# EPIC-{NUMBER}: {Feature / Outcome}

> **Load Order (3 + 1 + SoT)**
> 1. `README.md` → current status + navigation.
> 2. `PRD.md` → lifecycle intent (note target gate).
> 3. `CLAUDE.md` → behavior rules for agents touching code.
> 4. `epics/EPIC-{NUMBER}.md` → this file.
> 5. Linked SoT files (IDs listed in Section 3A).

> **Status Icons**: ✅ Done · 🚧 In Progress · 🟡 Ready · 📋 Planning · 🚫 Blocked · 🔴 Risk

---

## 1. Epic Snapshot

### Goal & Definition of Done
- **Goal (tie to PRD)**: {“Advance v0.x requirement {anchor} into production readiness.”}
- **User Outcome**: {What end users gain when this ships.}
- **Definition of Done**:
  - [ ] Required capability available to target persona (reference UJ-XXX).
  - [ ] Relevant SoT files updated (IDs tracked below).
  - [ ] Tests + metrics recorded (link to artifacts).
  - [ ] README + PRD change log updated if gate advances.

### Dependencies & Risk Notes
- **Upstream**: {EPIC / external constraint}
- **Downstream**: {EPIC / release dependency}
- **Risk Summary**: {Key risk + mitigation reference}

### Lifecycle Alignment
- **Current PRD Gate**: v0.{x}
- **Target Gate After EPIC**: v0.{x+1}
- **Gate Criteria References**: See [`workflows/PRD-VERSION-LIFECYCLE.md`](../workflows/PRD-VERSION-LIFECYCLE.md) (consult section for v0.{x}).

---

## 2. Issue Manifest
| Issue | Phase | Context Windows (Est → Actual) | Status | Evidence | Linked PR |
|-------|-------|---------------------------------|--------|----------|-----------|
| #{ID} – {Title} | {Plan / Build / Verify / Wrap} | 1 → 1 | 🚧 | `{path/to/artifact}` | #PR |

- **Naming**: Issues follow `EPIC-{NUMBER}-{slug}` for clarity.
- **Context Windows**: Maintain 1 window per issue. Split if expanding.
- **Evidence**: Attach logs, test output, or SoT IDs confirming completion.

---

## 3. Scope & File Impact
| Operation | Count | Notes |
|-----------|-------|-------|
| Files to Create | {#} | |
| Files to Modify | {#} | |
| Files to Delete | {#} | |
| Critical Dependencies | {#} | |
| Required Tests | {#} | |

### Planned SoT Touchpoints
- [ ] README.md (lifecycle metrics)
- [ ] PRD.md (if gate advances)
- [ ] USER-JOURNEYS.md (UJ-XXX)
- [ ] BUSINESS_RULES.md (BR-XXX)
- [ ] API_CONTRACTS.md (API-XXX)
- [ ] ACTUAL-SCHEMA.md (DBT-XXX)
- [ ] testing-playbook.md (TEST-XXX)
- [ ] deployment-playbook.md (DEP-XXX)
- [ ] customer-feedback.md (CFD-XXX)
- [ ] Other: __________________

---

## 3A. ID Tracking (Knowledge Graph)

**IDs Modified This EPIC**
| ID | Type | SoT File | Description | Status | Date | Notes |
|----|------|----------|-------------|--------|------|-------|
| API-### | Endpoint | API_CONTRACTS.md | {Change summary} | 🚧 | YYYY-MM-DD | {Notes} |

**IDs Created This EPIC**
| ID | Type | SoT File | Description | Status | Date | Related IDs |
|----|------|----------|-------------|--------|------|-------------|
| TEST-### | Test | testing-playbook.md | {Purpose} | ✅ | YYYY-MM-DD | API-### |

**Referenced (No Change)**
- BR-### — {Reason}
- DBT-### — {Reason}

**Impact Narrative**
- {2-3 sentences describing how the above IDs change the product.}

> Update `.codex/ID-REGISTRY.md` (or equivalent) after each working session.

---

## 4. Phases & Rituals
| Phase | Objective | Key Actions | Exit Signals |
|-------|-----------|-------------|--------------|
| **Plan** | Confirm scope, dependencies, risks | Sync with PRD + lifecycle gate, outline tests, capture unknowns. | ✅ Risks logged, SoT touchpoints identified. |
| **Build** | Implement scoped work | Pair with CLAUDE.md rules, keep issues within window. | ✅ Feature behind tests/flags, code reviewed. |
| **Verify** | Test + integrate | Execute required suites, capture artifacts, update SoT IDs. | ✅ Coverage thresholds met, evidence stored. |
| **Wrap** | Documentation & handoff | Update README, PRD, SoT, archive temps, log learnings. | ✅ Checklist complete, gate review ready. |

Phase loops are expected. Log each return in Section 5.

---

## 5. Phase Re-entry Log
| Date | Returned To Phase | Trigger | Action | Outcome |
|------|-------------------|---------|--------|---------|
| YYYY-MM-DD | Build | {Bug / feedback} | {Action taken} | {Result} |

---

## 6. Task Checklist (Tie to Issues)

### Task {N} — {Summary} (`Issue #{ID}` · Phase {Plan/Build/Verify/Wrap})
- Status: 📋 / 🔄 / ✅ / 🚫
- Acceptance Criteria:
  - [ ] {Criterion}
  - [ ] {Criterion}
- Test Command: `{npm run test:scope}`

*(Duplicate per task.)*

---

## 7. Temp Files & Extraction

### Temp Artifacts Created
| Temp File | Owner | Purpose | Extraction Target (SoT) | Archived On | Archive Path |
|-----------|-------|---------|-------------------------|-------------|--------------|
| temp/{file}.md | {Name} | {Why it exists} | {SoT file / ID} | YYYY-MM-DD | archive/YYYY-MM/ |

### Wrap Checklist
- [ ] README metrics refreshed (`workflow:verify`).
- [ ] PRD change log updated (if gate movement).
- [ ] SoT files updated & cross-linked.
- [ ] Temp artifacts harvested + archived.
- [ ] Linked PRs merged and tagged with EPIC ID.

---

## 8. Epic Completion Review
- **Issues & Scope**
  - [ ] Manifest complete, no dangling work.
  - [ ] Deferred scope captured as new issues/EPIC.
- **Testing & Quality**
  - [ ] Required suites run with evidence.
  - [ ] Coverage targets met (Statement ≥80%, Branch ≥75%, Function ≥85%, Line ≥80%).
  - [ ] Regression notes captured in TEST-XXX entries.
- **Lifecycle & Docs**
  - [ ] Gate review request filed (reference Section 4 exit signals).
  - [ ] README, PRD, and SoT updated + cross-referenced.
  - [ ] Learnings captured in README "EPIC Learning" section.

**Next Gate Review**: {Date / participants}

