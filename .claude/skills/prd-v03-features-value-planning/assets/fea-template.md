# FEA- Entry Template

Copy this template for each feature. Remove instructions after completing.

---

## FEA-XXX: [Feature Name]

**Type**: [Choose one: Moat | Outcome | Parity | Delta | Tier | Table Stakes]

**Priority**: [Choose one: P0 | P1 | P2 | P3]

**Description**: 
[What the feature does from user perspective. One sentence, verb-led.
GOOD: "Schedule meetings with single click from availability view"
BAD: "Implement Redis caching for sessions"]

---

### Strategic Traceability

**Outcome Link**: [KPI-XXX or "N/A"]
- [If KPI-XXX: How does this feature move that metric?]

**Moat Link**: [BR-XXX or "N/A"]
- [If BR-XXX: How does this feature support defensibility?]

**Pricing Link**: [BR-XXX tier rule, or "All tiers"]
- [Which tier(s) include this feature? Why?]

**Competitor Comparison**: [Choose one]
- [ ] Parity with [Competitor Name] — matches their capability
- [ ] Delta vs [Competitor Name] — our advantage
- [ ] Unique — no competitor offers this
- [ ] Table stakes — industry standard expectation

---

### Validation

**Evidence**: [CFD-XXX reference or validation method]
- [If CFD-XXX: Summarize the evidence]
- [If validation method: Describe how you'll validate before building]

**Confidence**: [High | Medium | Low]
- High = CFD- evidence from buying behavior or direct user research
- Medium = CFD- evidence from indirect signals (reviews, job posts)
- Low = Assumption (acceptable for P2/P3 only)

---

### Definition of Done

**Acceptance Criteria**:
- [ ] [Testable condition 1 — GOOD: "User completes in ≤3 clicks"]
- [ ] [Testable condition 2 — BAD: "Works well"]
- [ ] [Add more as needed]

**Dependencies**: [List FEA-XXX, API-XXX, or external dependencies]

---

### Downstream Usage

**User Journeys**: [Which UJ-XXX will use this feature?]

**EPIC Assignment**: [EPIC-XX or "TBD"]

---

## Quality Checklist

Before finalizing, verify:

- [ ] Description is user-facing (not implementation detail)
- [ ] Type classification is accurate
- [ ] Priority aligns with type (Moat/Outcome/Delta = P0 eligible; Table Stakes alone ≠ P0)
- [ ] At least one strategic link (KPI-, BR-, or CFD-) for P0/P1
- [ ] Acceptance criteria are testable
- [ ] Competitor comparison is specific (not "similar to others")
