# ID Registration Examples

**Purpose**: Good and bad patterns for registering SoT IDs.

---

## Good Example: Complete BR Registration

### New ID

**BR-095: Free Tier API Rate Limit**

**ID**: BR-095
**Type**: Business Rule (Monetization)
**Owner**: Product Team
**Created**: 2026-01-11

**Decision**: Free tier limited to 1,000 API requests per day

**Rationale**:
- Prevent abuse (unlimited free would enable scraping)
- Encourage upgrades (power users need more, convert to paid)
- Competitive positioning (similar to competitors: 500-2,000 range)

**Alternatives Considered**:
- 500 req/day: Too restrictive (feedback from beta)
- Unlimited: Abuse risk, no monetization incentive

**Linked IDs**:
- Upstream: CFD-078 (Beta users requested higher limits)
- Downstream: FEA-089 (Rate limit dashboard), API-067 (Rate limiting logic)

**Version History**:
| Version | Date | Change | Updated By |
|---------|------|--------|------------|
| 1.0 | 2026-01-11 | Initial definition | Alice |

---

### Validation: ✅ PASS

**Why**:
- ✅ Complete fields (ID, type, owner, date, decision, rationale)
- ✅ Valid cross-references (CFD → BR → FEA/API)
- ✅ No duplication (searched, no existing rate limit rule)
- ✅ Clear decision (specific number, justified)

---

## Bad Example 1: Incomplete Registration

### New ID (Bad)

**BR-096: Pricing**

**Decision**: We'll charge for premium features

---

### Validation: ❌ FAIL

**Blockers**:
- ❌ No ID explicitly stated (BR-096 in title, but not in body)
- ❌ No type field
- ❌ No owner
- ❌ No date
- ❌ Decision too vague ("charge for premium" - how much? which features?)
- ❌ No rationale
- ❌ No cross-references

**Fix**: Use BR template, fill all fields, be specific

---

## Bad Example 2: Duplicate ID

### Existing ID

**CFD-045: Users confused by onboarding step 3**
- Evidence: User interview (Sarah, 2026-01-05)
- Impact: 15 min avg time, should be < 2 min

### New ID Attempt (Bad)

**CFD-091: Onboarding step 3 is confusing**
- Evidence: User interview (John, 2026-01-10)
- Impact: Users don't know where to click

---

### Validation: ❌ FAIL (Duplicate)

**Problem**: CFD-091 duplicates CFD-045 (same pain point)

**Fix**: Update CFD-045 with additional evidence from John
- Don't create new ID
- Add John's quote to CFD-045
- Note: 2 users reported same issue (stronger signal)

---

## Good Example: API Registration with Schema

### New ID

**API-078: Update User Preferences**

**ID**: API-078
**Type**: API Contract
**Owner**: Backend Team
**Created**: 2026-01-11

**Endpoint**: `PATCH /api/users/:id/preferences`

**Request**:
```json
{
  "theme": "dark" | "light",
  "notifications": {
    "email": boolean,
    "push": boolean
  }
}
```

**Response (Success - 200)**:
```json
{
  "id": "user-123",
  "preferences": {
    "theme": "dark",
    "notifications": {
      "email": true,
      "push": false
    }
  },
  "updated_at": "2026-01-11T10:30:00Z"
}
```

**Response (Error - 400)**:
```json
{
  "error": "Invalid theme value",
  "message": "theme must be 'dark' or 'light'"
}
```

**Linked IDs**:
- FEA-067: User preferences feature
- DBT-034: user_preferences table

---

### Validation: ✅ PASS

**Why**:
- ✅ Complete schema (request + success + error)
- ✅ Specific (exact field names, types, values)
- ✅ Valid cross-references (FEA → API → DBT)

---

## Bad Example 3: Invalid Cross-References

### New ID (Bad)

**FEA-099: Dark Mode Feature**

**Linked IDs**:
- API-078: Dark mode API ❌ (backward reference)
- PER-101: Designer persona ❌ (wrong layer)

---

### Validation: ❌ FAIL

**Problems**:
1. ❌ FEA → API is wrong direction (should be API references FEA)
2. ❌ FEA → PER is wrong layer (should be UJ → PER, FEA → UJ)

**Fix**:
- Remove API-078 from FEA-099 (API-078 should reference FEA-099 instead)
- Link FEA-099 → UJ-045 → PER-101 (indirect relationship via journey)

---

## Good Example: CFD with Evidence Tiers

### New ID

**CFD-092: Export Feature Request**

**ID**: CFD-092
**Type**: Customer Feedback (Feature Request)
**Evidence Tier**: Tier 1 (Direct)
**Source**: Customer email, support ticket #1234
**Date**: 2026-01-09

**Feedback**:
"We need to export project data to CSV for reporting to our CFO quarterly."

**Impact**:
- Frequency: Quarterly (every 3 months)
- Workaround: Manual copy-paste (30 min each time)
- Willingness to Pay: "Would upgrade to Pro for this" (currently Free tier)

**Linked IDs**:
- BR-097: Export feature prioritized for Pro tier
- FEA-078: CSV export functionality

---

### Validation: ✅ PASS

**Why**:
- ✅ Evidence tier specified (Tier 1 = direct quote)
- ✅ Source attributed (email, ticket #1234)
- ✅ Impact quantified (quarterly, 30 min workaround)
- ✅ Revenue opportunity (willingness to upgrade)

---

## Registration Checklist Summary

### Before Registering

- [ ] Search SoT for duplicates
- [ ] Identify upstream IDs (what informed this?)
- [ ] Identify downstream IDs (what will use this?)

### During Registration

- [ ] All required fields complete
- [ ] Cross-references valid
- [ ] Content specific (not vague)
- [ ] Template purity (no methodology)

### After Registration

- [ ] ID added to SoT file
- [ ] Cross-references updated (other IDs linking to this)
- [ ] Version history logged

---

*Reference: Use these examples when registering IDs in `ghm-id-register` skill.*
