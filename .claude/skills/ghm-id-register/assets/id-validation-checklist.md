# ID Validation Checklist

**ID**: [ID-XXX]
**Type**: [BR | UJ | API | CFD | FEA | PER | KPI | etc.]
**Created By**: [Name]
**Date**: YYYY-MM-DD
**Status**: [Valid | Invalid | Needs Review]

---

## ID Format Validation

- [ ] **Correct Prefix**: Matches ID type (BR-, UJ-, API-, CFD-, etc.)
- [ ] **Sequential Number**: Next available in sequence (no gaps, no duplicates)
- [ ] **No Special Characters**: Only alphanumeric (BR-001, not BR_001 or BR.001)

**Example**:
- ✅ Valid: `BR-045` (Business Rule, sequential)
- ❌ Invalid: `BR_045` (underscore not allowed)
- ❌ Invalid: `RULE-045` (wrong prefix)

---

## Content Validation

### Required Fields

- [ ] **ID**: Explicitly stated at top
- [ ] **Title**: Descriptive, unique
- [ ] **Type**: Matches ID prefix
- [ ] **Created Date**: YYYY-MM-DD format
- [ ] **Owner**: Person or team responsible

### Content Quality

- [ ] **Description**: Clear, specific (not vague)
- [ ] **Self-Contained**: Can be understood without external context
- [ ] **No Duplication**: Doesn't overlap with existing IDs

---

## Cross-Reference Validation

### Inbound References

**Question**: "Which IDs reference this new ID?"

- [ ] **Zero Inbound OK for New IDs**: (Will be referenced later)
- [ ] **Document Expected References**: (Which IDs will reference this?)

### Outbound References

**Question**: "Which IDs does this new ID reference?"

- [ ] **All References Valid**: Referenced IDs exist
- [ ] **No Orphan References**: All referenced IDs findable in SoT
- [ ] **Reference Types Correct**: (CFD → BR ✅, BR → CFD ❌ unless justified)

**Valid Reference Patterns**:
- CFD → BR (feedback informs business rules) ✅
- BR → FEA (rules drive features) ✅
- FEA → API (features implemented by APIs) ✅
- API → DBT (APIs use data models) ✅
- UJ → PER (journeys for specific personas) ✅
- UJ → FEA (journeys use features) ✅

**Invalid Reference Patterns**:
- BR → CFD (rules don't inform feedback) ❌
- API → UJ (APIs don't create journeys) ❌
- DBT → FEA (data models don't drive features) ❌

---

## Conflict Detection

### Scope Overlap Check

- [ ] **Search Same Domain**: Are there existing IDs in the same prefix with overlapping scope?
- [ ] **Value Contradiction**: Does this ID's value/rule contradict any existing ID?
- [ ] **Precedence Clear**: If multiple IDs govern the same area, is precedence documented?

**Common Conflict Patterns**:
- Two BR- entries governing the same feature with different limits (e.g., BR-045 "100/day" vs BR-078 "unlimited for premium")
- Two API- entries for the same resource with different schemas
- Two UJ- entries for the same persona with contradictory flows

**Resolution**: If conflict detected, add `conflicts-with` typed relationship to both entries and document resolution in the EPIC.

---

## Type-Specific Validation

### BR (Business Rule)

- [ ] **Decision Clear**: Explicit choice made
- [ ] **Rationale Provided**: Why this rule exists
- [ ] **Alternatives Considered**: (Optional but recommended)

### CFD (Customer Feedback & Data)

- [ ] **Evidence Type**: Quote, survey, usage data, support ticket
- [ ] **Evidence Tier**: Tier 1 (direct) | Tier 2 (indirect) | Tier 3 (inferred)
- [ ] **Source Attribution**: Who/where/when

### API (API Contract)

- [ ] **Endpoint Defined**: Method + path (GET /api/users/:id)
- [ ] **Request Schema**: Parameters, body
- [ ] **Response Schema**: Success + error formats

### UJ (User Journey)

- [ ] **Trigger Defined**: What starts the journey
- [ ] **Steps Listed**: Sequence of actions
- [ ] **Value Moment**: When user gets value

### FEA (Feature)

- [ ] **Linked to Business Rule**: (BR-XXX)
- [ ] **Linked to Outcome**: (KPI-XXX)
- [ ] **Priority**: Parity | Delta | Nice-to-Have

---

## SoT Location Validation

- [ ] **Correct SoT File**: ID type matches file
  - BR → `SoT.BUSINESS_RULES.md`
  - CFD → `SoT.customer_feedback.md`
  - API → `SoT.API_CONTRACTS.md`
  - UJ, PER, SCR → `SoT.USER_JOURNEYS.md`
  - DBT → `SoT.DATA_MODEL.md`
  - TEST → `SoT.TESTING.md`
  - DEP, RUN, MON → `SoT.DEPLOYMENT.md`
  - DES → `SoT.DESIGN_COMPONENTS.md`
  - TECH, ARC → `SoT.TECHNICAL_DECISIONS.md`
  - INT → `SoT.INTEGRATIONS.md`
  - FEA, RISK, GTM → `PRD.md` (inline in respective sections)

- [ ] **Template Purity**: No methodology in SoT entry (belongs in skill references)

---

## Traceability Validation

### Forward Traceability

**Question**: "If I start at this ID, where does it lead?"

- [ ] **Downstream IDs Identified**: (Which IDs use/implement this?)
- [ ] **Example**: BR-045 → FEA-012 → API-023 → DBT-008

### Backward Traceability

**Question**: "If I start at this ID, where did it come from?"

- [ ] **Upstream IDs Identified**: (Which IDs informed this?)
- [ ] **Example**: DBT-008 ← API-023 ← FEA-012 ← BR-045 ← CFD-089

---

## Duplication Check

### Search for Existing

Before registering new ID:

- [ ] **Searched SoT**: Full-text search for similar concept
- [ ] **Reviewed Related IDs**: Checked cross-references
- [ ] **Confirmed Uniqueness**: This ID adds new information

**Common Duplications**:
- ❌ Creating CFD-050 when CFD-023 describes same pain point
- ❌ Creating BR-078 when BR-045 already defines this rule
- ✅ Creating BR-078 for different rule (unique)

---

## Versioning Validation

- [ ] **Version History**: Table present with columns: Date, Field, Previous, New, Reason, EPIC
- [ ] **Initial Entry**: Row logged with "Initial creation" and EPIC reference
- [ ] **Field-Level Tracking**: For updates, each changed field gets its own row with previous and new values
- [ ] **EPIC Traceability**: Every change row references the EPIC that prompted the change

---

## Cross-Functional Validation

### Stakeholder Review

For critical IDs (BR, API, KPI):

- [ ] **Product Review**: Product manager approved
- [ ] **Engineering Review**: (For API, DBT) Engineering approved
- [ ] **Business Review**: (For KPI, BR) Business stakeholder approved

---

## Validation Result

### ✅ Valid (Pass)

**Criteria**:
- All required fields present
- Cross-references valid
- No duplication
- Content quality high

**Action**: Register ID, add to SoT

---

### ⚠️ Needs Review (Conditional)

**Criteria**:
- Minor issues (fixable)
- Unclear cross-references (needs clarification)
- Possible duplication (needs confirmation)

**Action**: Fix issues, re-validate

**Issues to Fix**:
- [ ] [Issue 1]
- [ ] [Issue 2]

---

### ❌ Invalid (Reject)

**Criteria**:
- Missing required fields
- Broken cross-references
- Duplicate of existing ID
- Wrong ID type

**Action**: Do NOT register, fix fundamental issues

**Blockers**:
- [ ] [Blocker 1]
- [ ] [Blocker 2]

---

## Sign-Off

**Validated By**: [Name]
**Date**: YYYY-MM-DD
**Status**: [Valid | Needs Review | Invalid]

**Comments**: [Any notes or recommendations]

---

*Template: Use this checklist when registering new SoT IDs in `ghm-id-register` skill.*
