# TECH- Template (Reuse/Extend)

Use for Reuse and Extend decisions where an existing asset covers the need.

```
TECH-XXX: [Technology/Capability Name]
Category: [Reuse | Extend]
Layer: [Derived from capability area]
Purpose: [What problem this solves for the new product]

Reuse From: [Source product or asset — e.g., "Product-A — Keycloak deployment"]
Reuse Scope: [Full reuse | Extend | Shared instance | Pattern only]
Current State: [What exists today and how it's deployed]
Changes Needed: [What the new product needs that doesn't exist yet, or "None" for full reuse]

Shared or Separate: [Shared deployment (separate namespace/realm) | Separate instance | Same instance]

Features Served: [FEA-XXX, FEA-YYY]
Risk Constraints: [RISK-XXX if any]

Cost: [Incremental cost — often $0 for reuse, or cost of extending]
Integration Complexity: [Low | Medium | High]
Lock-in Risk: [Already committed — note if this matters]

# Optional:
Product Family Notes: [Cross-product impact, SSO considerations, shared data]
```

## When to Use This Template

| Situation | Use This Template |
|-----------|-------------------|
| Sibling product already runs this service | Yes — Reuse |
| Service exists but needs new features for this product | Yes — Extend |
| Service exists but is wrong for this product | No — use standard template with Category: Replace |
| No existing asset | No — use standard template |

## Checklist Before Adding

- [ ] Verified the existing asset actually works for this use case
- [ ] Confirmed with team that the asset is still actively maintained
- [ ] Documented any changes needed (even if "None")
- [ ] Shared vs. separate deployment decision is explicit
- [ ] Features Served references are correct
