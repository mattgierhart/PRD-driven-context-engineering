# Competitive Feature Matrix

Use this matrix to map features against competitors and identify parity/delta opportunities.

---

## Matrix Template

| Feature | Our Status | Competitor A | Competitor B | Competitor C | Type | Priority |
|---------|------------|--------------|--------------|--------------|------|----------|
| [Feature 1] | | | | | | |
| [Feature 2] | | | | | | |
| [Feature 3] | | | | | | |

### Status Legend

| Symbol | Meaning |
|--------|---------|
| ✅ | Shipped / Available |
| 🚧 | Building / In progress |
| 📋 | Planned |
| ❌ | Not available |
| ➕ | Our delta (we have, they don't) |
| ⭐ | Their strength (they're better) |

---

## Example: Scheduling Tool Matrix

| Feature | Us | Calendly | Acuity | SavvyCal | Type | Priority |
|---------|-----|----------|--------|----------|------|----------|
| Calendar sync | 🚧 | ✅ | ✅ | ✅ | Parity | P0 |
| Custom booking page | 🚧 | ✅ | ✅ | ✅ | Parity | P0 |
| Unlimited event types | ➕ | ❌ (paid) | ❌ (paid) | ✅ | Delta | P0 |
| Team scheduling | 📋 | ✅ | ⭐ | ✅ | Parity | P1 |
| Round-robin | ❌ | ⭐ | ✅ | ✅ | Defer | P3 |
| Workflows/automation | ❌ | ⭐ | ❌ | ✅ | Defer | P3 |
| Offline mode | ➕ | ❌ | ❌ | ❌ | Delta | P1 |

### Analysis from Example

**Parity requirements (P0)**:
- Calendar sync, custom booking page = table stakes
- Must match before users will consider switching

**Our deltas (competitive advantage)**:
- Unlimited event types → Price-based moat (they charge, we don't)
- Offline mode → Capability moat (they can't easily add)

**Defer (not MVP)**:
- Round-robin, workflows → Enterprise features, add post-PMF

---

## How to Complete This Matrix

### Step 1: List Competitor Features
Pull from CFD- entries (Competitive Landscape skill output):
- Feature lists from competitor websites
- G2/Capterra comparison pages
- User reviews mentioning features

### Step 2: Audit Usage (Critical)
Not all features matter. For each competitor feature, ask:
- Do users actually use this? (Check reviews, forums)
- Is it mentioned in buying decisions? (Check comparison threads)
- Is it a "checkbox feature" vs. core workflow?

**80/20 rule**: 20% of features drive 80% of value. Identify the 20%.

### Step 3: Classify Our Position
For each feature row:
- **Parity**: We must match to be considered
- **Delta**: We're better or unique
- **Defer**: Not essential for target segment

### Step 4: Assign Priority
Use this decision tree:

```
Is this feature used in core workflow?
├─ YES → Is competitor clearly better?
│   ├─ YES → Parity (P0 if blocking, P1 if not)
│   └─ NO → Can we be meaningfully better?
│       ├─ YES → Delta (P0 if moat-building)
│       └─ NO → Table stakes (P1)
└─ NO → Defer (P2/P3 or cut)
```

---

## Matrix → FEA- Conversion

Each row becomes a FEA- entry:

| Matrix Column | FEA- Field |
|---------------|------------|
| Feature | FEA-XXX: [Name] |
| Our Status | Current state |
| Type | Type classification |
| Priority | Priority tier |
| Competitor columns | Competitor Comparison field |

**Evidence source**: The matrix itself becomes CFD- evidence for feature decisions.

---

## Anti-Patterns

| Problem | Signal | Fix |
|---------|--------|-----|
| Parity inflation | >70% marked "Parity, P0" | Audit actual usage; apply 80/20 |
| No deltas | Everything is parity or defer | Find undercut opportunity or reconsider market |
| Competitor-driven scope | Building features because "they have it" | Validate with user evidence (CFD-) |
| Ignoring strengths (⭐) | No plan for competitor advantages | Either match or position around |
