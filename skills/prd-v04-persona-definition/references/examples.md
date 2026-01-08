# Persona Definition Examples

## Good Example: Primary Persona with Full Traceability

```
PER-001: The Overwhelmed Ops Manager
Source IDs: CFD-003, CFD-012, CFD-025, BR-041
Type: Primary
Segment: SMB SaaS (10-50 employees)

Demographics:
  Role: Operations Manager
  Context: Growing startup, wearing multiple hats
  Technical Level: Intermediate

Behavioral Profile:
  Goals: Reduce manual reporting time (CFD-012: "Save 5 hrs/week")
  Frustrations: Current tools require too much setup (CFD-003: "Notion takes forever")
  Decision Factors: Ease > features, must show ROI (CFD-025: CEO approval pattern)
  Current Workflow: Spreadsheets → manual entry → weekly compilation

Product Relationship:
  Primary Value: CFD-012 (time savings)
  Key Features: FEA-001 (auto-sync), FEA-003 (reports), FEA-007 (dashboard)
  Pricing Sensitivity: BR-030 (≤$50/mo SMB tier)
  Acquisition Channel: BR-041 (contract renewal trigger)

Marketing Hook: "Stop building reports. Start using them."
```

**Why it's good:**
- Every claim has a CFD- or BR- link
- Behavioral focus, not just demographics
- Clear feature mapping
- Actionable marketing hook

---

## Bad Example: Demographic-Only Persona

```
PER-001: Marketing Mary
Age: 28-35
Gender: Female
Education: Bachelor's degree
Income: $60-80K
Likes: Coffee, yoga, Instagram
Goals: Be successful at work
```

**Why it's bad:**
- No CFD- evidence links
- Demographics without behavior
- "Be successful" is not actionable
- No feature mapping
- No acquisition channel

---

## Bad Example: Persona Explosion

```
PER-001: SMB Marketing Manager
PER-002: SMB Marketing Director
PER-003: SMB CMO
PER-004: Enterprise Marketing Manager
PER-005: Enterprise Marketing Director
PER-006: Enterprise CMO
PER-007: Agency Marketing Manager
PER-008: Freelance Marketer
```

**Why it's bad:**
- 8 personas for one product = over-segmentation
- PER-001, 002, 003 likely have same behavior (consolidate)
- No clear Primary designation
- Splits by title, not behavior

**Fix:**
```
PER-001: The Hands-On Marketer (Primary)
  - Spans SMB Manager to Director
  - Actually uses the tool daily

PER-002: The Strategic Buyer (Secondary)
  - CMO/VP level across company sizes
  - Approves purchase, doesn't use daily
```

---

## Negative Persona Example

```
PER-003: The Enterprise Procurement Lead (Negative)
Source IDs: BR-045 (SMB-only targeting), CFD-030 (enterprise sales cycle data)
Type: Negative
Segment: Enterprise (500+ employees)

Why Excluded:
  - Sales cycle: 6-12 months (CFD-030) vs. our 14-day target
  - Procurement requirements exceed our compliance readiness
  - Deal size doesn't justify CAC

Marketing Implication: Exclude from paid campaigns, qualify out early in inbound
```

**Why it's good:**
- Explicit exclusion with evidence
- Prevents wasted sales effort
- Actionable marketing guidance
