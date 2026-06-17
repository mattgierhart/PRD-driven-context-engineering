# Epic Scoping Examples

## Example: Well-Scoped MVP EPICs

**Product**: B2B SaaS analytics dashboard
**Total Scope**: 15 API endpoints, 8 tables, 12 screens

### Epic Breakdown

```
EPIC-01: Infrastructure & Auth
  APIs: API-001–005 (auth endpoints)
  Tables: DBT-010 (users), DBT-011 (sessions)
  Screens: SCR-000–003 (auth screens)
  Dependencies: None
  Enables: All other EPICs

EPIC-02: Data Sources
  APIs: API-010–013 (data source CRUD)
  Tables: DBT-020 (data_sources), DBT-021 (connections)
  Screens: SCR-010–012 (data source management)
  Dependencies: EPIC-01
  Enables: EPIC-03, EPIC-04

EPIC-03: Report Builder
  APIs: API-020–025 (reports CRUD + generation)
  Tables: DBT-030 (reports), DBT-031 (templates)
  Screens: SCR-020–024 (report builder)
  Dependencies: EPIC-01, EPIC-02
  Enables: EPIC-05

EPIC-04: Dashboard
  APIs: API-030–032 (dashboard data)
  Tables: DBT-040 (dashboards), DBT-041 (widgets)
  Screens: SCR-030–033 (dashboard views)
  Dependencies: EPIC-01, EPIC-02
  Enables: None (leaf)

EPIC-05: Sharing & Export
  APIs: API-040–043 (sharing, export)
  Tables: DBT-050 (shares)
  Screens: SCR-040–042 (sharing UI)
  Dependencies: EPIC-03
  Enables: None (leaf)
```

### Dependency Graph

```
EPIC-01 (Auth)
    │
    ├──► EPIC-02 (Data Sources)
    │        │
    │        ├──► EPIC-03 (Reports) ──► EPIC-05 (Sharing)
    │        │
    │        └──► EPIC-04 (Dashboard)
    │
    └──► (all EPICs need auth)
```

### Why This Works

- **5 EPICs for MVP**: Manageable scope
- **Clear dependencies**: Build order is obvious
- **Right-sized**: Each EPIC has 3-6 APIs, 2-3 tables
- **Coherent domains**: Each EPIC is a logical unit
- **No circular deps**: Clean DAG

---

## Anti-Pattern: Mega-EPIC

**Bad:**
```
EPIC-01: Build the Product
  Goal: Implement all features
  APIs: API-001–050
  Tables: DBT-001–025
  Screens: SCR-001–030
```

**Problem**:
- Can't hold all context at once
- No clear progress indicators
- No natural stopping points

---

## Anti-Pattern: Micro-EPICs

**Bad:**
```
EPIC-01: Create users table
EPIC-02: Create sessions table
EPIC-03: Implement signup endpoint
EPIC-04: Implement login endpoint
EPIC-05: Implement logout endpoint
EPIC-06: Build signup form
EPIC-07: Build login form
... (50 more EPICs)
```

**Problem**:
- Overhead of managing 50+ EPICs
- Artificial boundaries (signup form needs signup endpoint)
- Lost coherence

**Fix**: Consolidate into `EPIC-01: Authentication` with Context Windows for schema → API → UI

---

## Example: Context Windows in Detail

```
EPIC-02: Data Sources

## 4. Context Windows

### Window 1: Database Schema (Day 1)
Focus: Get the data model right before writing any code

- [ ] Review DBT-020 (data_sources) specification
- [ ] Create migration for data_sources table
- [ ] Add RLS policies for multi-tenant isolation
- [ ] Create seed data for testing
- [ ] Verify schema in Supabase Studio

Completion Signal: Can query data_sources table with test data

### Window 2: API Endpoints (Day 2-3)
Focus: Implement CRUD operations with proper auth

- [ ] Implement POST /data-sources (API-010)
- [ ] Implement GET /data-sources (API-011) with pagination
- [ ] Implement GET /data-sources/:id (API-012)
- [ ] Implement DELETE /data-sources/:id (API-013)
- [ ] Add validation per BR-020 (connection limits)
- [ ] Write integration tests

Completion Signal: All TEST-020–029 passing

### Window 3: UI Integration (Day 4-5)
Focus: Connect UI to APIs

- [ ] Build data source list view (SCR-010)
- [ ] Build add data source modal (SCR-011)
- [ ] Build data source detail/edit (SCR-012)
- [ ] Add loading, error, and empty states
- [ ] Manual test UJ-002 (connect data source)

Completion Signal: Can complete UJ-002 end-to-end
```

---

## Example: Handling Dependencies

### Scenario: Circular Dependency Detected

**Problem:**
```
EPIC-01: User Management
  - Needs team info to show user's team

EPIC-02: Team Management
  - Needs user info to show team members
```

**Solution:** Extract shared foundation

```
EPIC-00: Core Data Model (NEW)
  - DBT-010 (users) basic schema
  - DBT-020 (teams) basic schema
  - DBT-021 (team_members) join table
  - No UI, just foundation

EPIC-01: User Management
  - Depends on: EPIC-00
  - User CRUD, profile, etc.

EPIC-02: Team Management
  - Depends on: EPIC-00
  - Team CRUD, invites, etc.
```

Now there's no circular dependency—both depend on the foundation.

---

## Sequencing Decision Guide

| If... | Sequence... |
|-------|-------------|
| Feature B needs data from Feature A | A before B |
| Screen X shows data from multiple features | Build data features first, then X |
| Multiple features share a component | Build component in first EPIC that needs it |
| External service is shared | Setup external service in EPIC-00 or first user |
| Uncertainty about approach | Research spike as Context Window 0 |
