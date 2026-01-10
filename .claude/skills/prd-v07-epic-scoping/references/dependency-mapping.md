# Dependency Mapping Guide

## Why Dependencies Matter

EPIC dependencies determine:
1. **Build order**: What must be done first
2. **Parallel work**: What can be done simultaneously
3. **Risk exposure**: What blocks the most work if delayed

## Dependency Types

### 1. Data Dependencies
One EPIC creates data another EPIC needs.

```
EPIC-01 creates → users table
EPIC-02 needs → users table for foreign keys
Result: EPIC-01 → EPIC-02
```

### 2. API Dependencies
One EPIC's UI needs another EPIC's API.

```
EPIC-03 UI → calls API-020 (reports)
EPIC-02 implements → API-020
Result: EPIC-02 → EPIC-03
```

### 3. Auth Dependencies
Most EPICs need authentication.

```
EPIC-01 implements → auth
EPIC-02, 03, 04 → need auth
Result: EPIC-01 → {EPIC-02, EPIC-03, EPIC-04}
```

### 4. External Dependencies
Setup required before development.

```
EPIC-01 needs → Supabase project
External → Supabase setup
Result: External → EPIC-01
```

## Mapping Process

### Step 1: List All EPICs with Their IDs

| EPIC | APIs | Tables | Screens |
|------|------|--------|---------|
| EPIC-01 | API-001–005 | DBT-010, 011 | SCR-000–003 |
| EPIC-02 | API-010–013 | DBT-020, 021 | SCR-010–012 |
| EPIC-03 | API-020–025 | DBT-030, 031 | SCR-020–024 |

### Step 2: Identify Cross-EPIC References

Check each EPIC's specifications:
- Does any API reference a table from another EPIC?
- Does any screen call an API from another EPIC?
- Does any table have a foreign key to another EPIC's table?

### Step 3: Draw Dependency Graph

```
         ┌─────────────────────────────────┐
         │           External               │
         │     (Supabase, Stripe, etc.)    │
         └────────────────┬────────────────┘
                          │
                          ▼
         ┌─────────────────────────────────┐
         │         EPIC-01: Auth           │
         │    (Foundation, no deps)        │
         └────────────────┬────────────────┘
                          │
         ┌────────────────┼────────────────┐
         ▼                ▼                ▼
┌─────────────┐   ┌─────────────┐   ┌─────────────┐
│  EPIC-02    │   │  EPIC-03    │   │  EPIC-04    │
│ Data Sources│   │  Billing    │   │  Settings   │
└──────┬──────┘   └─────────────┘   └─────────────┘
       │
       ▼
┌─────────────┐
│  EPIC-05    │
│   Reports   │
└─────────────┘
```

### Step 4: Identify Critical Path

The **critical path** is the longest chain of dependencies.

In the example above:
- External → EPIC-01 → EPIC-02 → EPIC-05

This is the critical path. Delays here delay the whole project.

### Step 5: Find Parallel Opportunities

EPICs at the same level with no dependencies between them can be parallel:
- EPIC-02, EPIC-03, EPIC-04 can all start after EPIC-01
- If you have multiple developers, assign parallel EPICs

## Common Patterns

### Pattern: Foundation First
```
EPIC-00: Infrastructure
    │
    ├──► EPIC-01: Feature A
    ├──► EPIC-02: Feature B
    └──► EPIC-03: Feature C
```

One EPIC sets up everything others need.

### Pattern: Layer Cake
```
EPIC-01: Data Layer
    │
    └──► EPIC-02: API Layer
            │
            └──► EPIC-03: UI Layer
```

Each layer depends on the one below.

### Pattern: Feature Branches
```
EPIC-01: Core
    │
    ├──► EPIC-02: Feature A ──► EPIC-04: Feature A+
    │
    └──► EPIC-03: Feature B ──► EPIC-05: Feature B+
```

Features branch from core, then have their own extensions.

## Detecting Circular Dependencies

**Symptoms:**
- Can't determine build order
- "X needs Y needs X"

**Solution:**
1. Identify the shared element
2. Extract it to a new EPIC (EPIC-00)
3. Both original EPICs now depend on EPIC-00

**Before:**
```
EPIC-01 ←──→ EPIC-02 (circular!)
```

**After:**
```
EPIC-00 (shared foundation)
    │
    ├──► EPIC-01
    └──► EPIC-02
```

## Dependency Matrix Template

| EPIC | Depends On | Enables | Parallel With |
|------|------------|---------|---------------|
| EPIC-01 | External | EPIC-02, 03, 04 | None |
| EPIC-02 | EPIC-01 | EPIC-05 | EPIC-03, 04 |
| EPIC-03 | EPIC-01 | None | EPIC-02, 04 |
| EPIC-04 | EPIC-01 | None | EPIC-02, 03 |
| EPIC-05 | EPIC-02 | None | EPIC-03, 04 |
