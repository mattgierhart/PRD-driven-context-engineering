# Journey Sequencing Guide

## The Dependency Chain

Journeys have dependencies. Map them to understand build order.

### Basic Pattern

```
UJ-000: Onboarding
    │
    ├──→ UJ-001: Core Journey A (primary value)
    │        │
    │        └──→ UJ-002: Core Journey B (depends on A)
    │
    └──→ UJ-010: Recovery (available anytime after onboarding)
             │
             └──→ UJ-003: Power User (expansion)
```

### Sequencing Rules

1. **Onboarding gates everything**
   - No journey should assume onboarding is skipped
   - Onboarding sets up data/state for all other journeys

2. **Core journeys drive KPIs**
   - Sequence core journeys by which KPI- they affect
   - Activation KPI journey comes before retention KPI journey

3. **Recovery journeys are always-available**
   - They should work from any state
   - Don't sequence them as "after" something

4. **Power User journeys unlock after core completion**
   - Don't offer expansion before primary value delivered

### Example Sequence for SaaS Product

```
Phase 1: Getting Started
├── UJ-000: Account Creation (onboarding)
└── UJ-001: First Value Moment (core - activation KPI)

Phase 2: Depth
├── UJ-002: Data Integration (core - depth KPI)
└── UJ-003: Customization (core - engagement KPI)

Phase 3: Expansion
├── UJ-004: Team Invite (power user - expansion KPI)
└── UJ-005: Advanced Features (power user - upsell KPI)

Always Available:
├── UJ-010: Password Reset (recovery)
├── UJ-011: Billing Issue (recovery)
└── UJ-012: Support Contact (recovery)
```

### Visualizing Dependencies

For complex products, draw the dependency graph:

```
         ┌─────────────────────────────────────┐
         │           UJ-000: Onboarding         │
         └─────────────┬───────────────────────┘
                       │
         ┌─────────────┴───────────────┐
         ▼                             ▼
┌─────────────────┐          ┌─────────────────┐
│ UJ-001: First   │          │ UJ-002: Connect │
│ Report          │          │ Data Source     │
└────────┬────────┘          └────────┬────────┘
         │                            │
         └──────────┬─────────────────┘
                    ▼
         ┌─────────────────┐
         │ UJ-003: Share   │
         │ with Team       │
         └─────────────────┘
```

### Build Order Implications

Journey dependencies inform EPIC sequencing in v0.7:

| Journey | Depends On | Build Order |
|---------|------------|-------------|
| UJ-000 | None | EPIC-01 |
| UJ-001 | UJ-000 | EPIC-02 |
| UJ-002 | UJ-000 | EPIC-02 (parallel with UJ-001) |
| UJ-003 | UJ-001, UJ-002 | EPIC-03 |

This ensures we build foundations before dependent features.
