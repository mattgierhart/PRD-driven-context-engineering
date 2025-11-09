---
version: 3.2
purpose: Lean EPIC template with ID-based knowledge graph tracking. Keeps work scoped, ties to research, enforces documentation discipline.
summary: Defines goal + DoD, links to GitHub issues, tracks ID modifications/creation, manages scope/phase loops, temp file lifecycle, and mandatory wrap-up.
last_updated: 2025-11-09
authority: Refer to WORKFLOW-PRD-DEVELOPMENT.md for end-to-end guidance
changelog: v3.2 - Added Section 3A (ID Tracking) for knowledge graph integration
---

# EPIC-{NUMBER}: {Feature Name}

> **MANDATORY: Load These Files First (in order)**
>
> 1. Claude.md → Process rules
> 2. README.md → Current status
> 3. PRD.md → Requirements context
> 4. This EPIC → Today's execution
>
> **Status Emojis**: ✅ Complete · 🚧 In Progress · 🟡 Ready · 📋 Planning · 🚫 Blocked · 🔴 Emergency
> **Hierarchy**: EPIC = multi-issue program. Every GitHub issue must fit a single context window. EPIC stays open until all issues are closed, tested, documented, and SoT files are updated.

---

## 1. Epic Snapshot

### Goal & Definition of Done
- **Goal (tie to research/PRD)**: {Example: “Operationalize PRD v0.7.2 Requirement R3 for SMB admins.”}
- **User Capability After Completion**: {Describe what a real user can now do that was impossible before. Pull wording from validated user stories.}
- **Definition of Done**:
  - [ ] Users accomplish {key task} within {time/value metric}.
  - [ ] Data/telemetry captured in `{file/path}`.
  - [ ] Success metric(s) from research phase satisfied: {metric/value}.
- **Primary References**:
  - PRD Section: `PRD.md#{anchor}`
  - Research Artifact(s): `research/{file}.md`

### Dependencies & Risk Notes
- Upstream: {EPIC/issue/blocker}
- Downstream: {EPIC/launch dependency}
- Risk Impact on Command Center: ±{value}

### PRD Alignment
- Current PRD Version: v{0.x}
- Milestone Unlocked After Completion: v{0.x+1} (per WORKFLOW-PRD-DEVELOPMENT ladder)

---

## 2. GitHub Issue Manifest
| Issue ID / Title | Phase (A‑E) | Context Windows (Est → Actual) | Status | Evidence / Tests | Linked PR(s) |
|------------------|-------------|--------------------------------|--------|------------------|--------------|
| #123 – Example   | B           | 1 → 1                          | ✅     | `coverage/issue-123.json` | #456 |

- **Naming Convention**: Use format `EPIC-{XX}-{brief-description}` (e.g., `EPIC-03-user-auth`, `EPIC-12-payment-flow`)
- **Evidence**: Link to logs, screenshots, or SoT entries proving completion.
- **Deferred Work**: If an issue expands beyond a window, split it and add the new issue to the manifest before continuing.
- **Cleanup**: Close issues as work completes (don't batch). Update status column in real-time. Link PRs before merging.

---

## 3. Scope & File Impact
| Operation | Count | Notes |
|-----------|-------|-------|
| Files to Create | 0 | |
| Files to Modify | 0 | |
| Files to Delete | 0 | |
| Critical Dependencies | 0 | |
| Required Tests | 0 | |

### SoT Files to Update This EPIC

- [ ] README.md (Truth Table)
- [ ] PRD.md (if milestone change)
- [ ] testing-playbook.md (if new test patterns)
- [ ] deployment-playbook.md (if deployment changes)
- [ ] BUSINESS_RULES.md (if rules added/changed)
- [ ] API_CONTRACTS.md (if API changes)
- [ ] user-journeys/{journey}.md (if UX changes)
- [ ] Other: _____________________

Architecture Sketch (optional):

```
project/
├── src/feature/        # {changes}
├── tests/feature/      # {planned coverage}
└── docs/               # {docs to update}
```

---

## 3A. ID Tracking (Knowledge Graph)

> **Purpose**: Track all SoT artifact IDs modified or created during this EPIC. Enables impact analysis, cross-reference validation, and documentation traceability.

### IDs Modified This EPIC

| ID | Type | SoT File | Description | Status | Date Modified | Notes |
|----|------|----------|-------------|--------|---------------|-------|
| API-045 | Endpoint | API_CONTRACTS.md | OCR upload endpoint | ✅ Complete | 2025-11-08 | Added retry logic |
| TEST-301 | Test | testing-playbook.md | OCR happy path | 🚧 In Progress | - | Adding timeout scenarios |

### IDs Created This EPIC

| ID | Type | SoT File | Description | Status | Date Created | Related IDs |
|----|------|----------|-------------|--------|--------------|-------------|
| API-046 | Endpoint | API_CONTRACTS.md | Retry failed OCR | ✅ Complete | 2025-11-08 | API-045, TEST-303 |
| TEST-303 | Test | testing-playbook.md | Validates retry logic | ✅ Complete | 2025-11-09 | API-046 |

### ID Impact Map

**Primary IDs** (core changes): API-045, API-046
**Affected IDs** (downstream impact): UJ-101 (improved UX), TEST-301 (updated), TEST-302 (updated)
**Referenced IDs** (dependencies): BR-112 (no change), DEP-027 (no change), DBT-018 (no change)

**ID Dependency Chain**:

```
API-046 (new retry endpoint)
  ├─→ API-045 (original endpoint - enhanced)
  ├─→ TEST-303 (validates retry)
  ├─→ UJ-101 (improves this user journey)
  └─→ DEP-027 (uses same Google Document AI service)
```

**Cross-Reference Validation**:

- [ ] All modified IDs have bidirectional references updated
- [ ] All created IDs added to ID-REGISTRY.md (auto-sync)
- [ ] All referenced IDs exist in their SoT files
- [ ] README.md updated with active IDs from this EPIC

---

## 4. Operational Phases (A‑E)
> Phases loop as needed (e.g., Tech Debt fix → Testing). Log every loop in the Phase Re-entry table.

| Phase | Objective | Key Actions |
|-------|-----------|-------------|
| **A – Planning & Architecture** | Confirm approach & scope | Read `README.md#command-center`, `PRD.md` anchor, capture risks, plan delegation. |
| **B – Core Implementation** | Build features tied to issue manifest | Reference `TECHNICAL-ARCHITECTURE.md` + `API_CONTRACTS.md`; keep issues scoped per window. |
| **C – Integration & Testing** | Wire components + verify | Follow `testing-playbook.md#coverage`, attach test logs & coverage artifacts. |
| **D – Tech Debt & Polish** | Pay down debt discovered in B/C | Log debt, resolve or file new issues, re-run tests after fixes. |
| **E – Documentation & Handoff** | Update Three-File stack + SoTs | README Truth Table, PRD change log (if milestone), SoT updates, temp extraction, archive. |

---

## 5. Phase Re-entry Log
| Date | Returned To Phase | Trigger (Issue / Finding) | Action Taken | Outcome |
|------|-------------------|---------------------------|--------------|---------|
| - | - | - | - | - |

---

## 6. Task Checklist
> Use this for lightweight tracking. Each task must reference a GitHub issue from the manifest.

### Task 1 – {Name} (`Issue #123`, Phase B)
- Status: 📋 / 🔄 / ✅ / 🚫
- Acceptance Criteria:  
  - [ ] {criterion}
  - [ ] {criterion}
- Test Command: `npm run test:{scope}`

*(Duplicate for Task 2..N as needed.)*

---

## 7. Phase E Wrap‑Up (Doc + Temp Extraction)

### Temp Files Created This EPIC

| Temp File | Purpose | Extracted To (SoT) | Archived Date | Archive Location |
|-----------|---------|-------------------|---------------|------------------|
| | | | | |

### Documentation Updates

- [ ] README.md updated (Truth Table, Active EPIC, Learning Repository, Active IDs list)
- [ ] PRD.md updated if milestone advanced (add change-log entry with temp archive link)
- [ ] SoT files updated (testing, deployment, BUSINESS_RULES, customer-feedback, etc.) with metadata header (`last_updated`, `last_verified`)
- [ ] All modified IDs have updated "Related IDs" sections (bidirectional references)
- [ ] All created IDs added to their respective SoT files with complete metadata
- [ ] ID-REGISTRY.md auto-synced via `npm run codex:sync-registry` (if implemented)
- [ ] All temp file content extracted into appropriate SoTs
- [ ] Temp files moved to `archive/YYYY-MM/`
- [ ] Verified no PRD references to archived temps (only SoT references)
- [ ] Tech debt outcomes recorded (resolved vs deferred issue ID)

---

## 8. Epic Completion Checklist
- **Issues & Scope**
  - [ ] All manifest issues closed with evidence.
  - [ ] Any stretch/deferred work captured as new issues.
- **Testing**
  - [ ] Required suites executed (unit/integration/E2E) with artifact links.
  - [ ] Coverage meets targets: Statement ≥80%, Branch ≥75%, Function ≥85%, Line ≥80%
  - [ ] Coverage report attached (`coverage/coverage-summary.json`).
  - [ ] Regression / smoke tests logged for user-facing paths.
- **Tech Debt**
  - [ ] Debt introduced resolved or logged with owner + due date.
  - [ ] Performance/UX benchmarks captured post-optimization.
- **Documentation**
  - [ ] README, PRD (if applicable), and EPIC file updated.
  - [ ] SoT documents updated + temp files archived.
  - [ ] Phase Re-entry Log finalized.
  - [ ] User journeys updated if UI/UX changes made (user-journeys/{journey}.md).
- **Admin**
  - [ ] Branch merged, CI green.
  - [ ] Product Owner sign-off recorded.

> Only rename the file with ✅ once every item above is satisfied.

---

## 9. Testing Notes (Optional)
- Coverage Target: {value}% (per `README.md` risk score)
- Special Scenarios: {list critical workflows or data sets}
- Reference: `testing-playbook.md#{anchor}` for detailed procedures.

---

*End of template – keep concise, enforce discipline, and reference WORKFLOW-PRD-DEVELOPMENT.md for deeper guidance.*
