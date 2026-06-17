# Screen Flow Definition Examples

## Good Example: Dashboard Screen with Full Traceability

```
SCR-001: Main Dashboard
Type: Page
Purpose: Central hub showing key metrics and quick actions for daily use
Journeys: UJ-001 (Step 4 - see report preview), UJ-003 (Step 1 - start point)
Features: FEA-007 (dashboard), FEA-003 (reports preview), FEA-012 (notifications)

Primary Actions:
  - Create New Report (→ SCR-002)
  - View Data Sources (→ SCR-003)

Secondary Actions:
  - Invite Team Member (→ Modal: SCR-020)
  - Access Settings (→ SCR-010)
  - View Help (→ SCR-015)

Navigation:
  From: SCR-000 (Login), any screen via top nav
  To: SCR-002 (Report Builder), SCR-003 (Data Sources), SCR-010 (Settings)

Content:
  - Key metrics summary (3 data cards - DES-001)
  - Recent reports list (5 items max)
  - Data source health indicators
  - Notification bell with count

Constraints:
  - BR-015 (data refreshes every 5 min)
  - BR-020 (admin sees all; user sees own data)

Design Notes:
  - PER-001 wants "at-a-glance" status, avoid requiring clicks to see health
  - Show "Create Report" prominently for UJ-001 activation
```

**Why it's good:**
- Clear purpose tied to user need
- Journey steps mapped to screen role
- Features explicitly listed
- Navigation is bidirectional
- Constraints considered
- Persona-specific design notes

---

## Good Example: Modal for Quick Action

```
SCR-020: Invite Team Member (Modal)
Type: Modal
Purpose: Quick team invite without leaving current context
Journeys: UJ-004 (Step 2 - send invite)
Features: FEA-015 (team management)

Primary Actions:
  - Enter email + role → Send Invite
  - Cancel (close modal)

Navigation:
  From: SCR-001 (Dashboard), SCR-010 (Settings - Team tab)
  To: Returns to invoking screen

Content:
  - Email input field
  - Role selector (Admin / Editor / Viewer)
  - "Send Invite" button
  - Cancel link

Constraints:
  - BR-025 (max 5 team members on free tier)
  - BR-026 (admin-only action)

Design Notes:
  - Show remaining invite count on free tier
  - Disable "Send" until valid email entered
```

**Why modal is appropriate:**
- Single, focused action
- User doesn't need to see other content
- Quick return to previous context

---

## Bad Example: Screen Explosion

```
SCR-001: Dashboard
SCR-002: Dashboard - Reports Tab
SCR-003: Dashboard - Analytics Tab
SCR-004: Dashboard - Settings Tab
SCR-005: Dashboard - Help Tab
SCR-006: Report List
SCR-007: Report Detail
SCR-008: Report Edit
SCR-009: Report Create
SCR-010: Report Preview
...
(30+ screens for MVP)
```

**Why it's bad:**
- Tabs should be one screen with states, not separate SCR-
- Report CRUD could consolidate (List + Detail/Edit)
- 30+ screens = too complex for MVP

**Fix:**
```
SCR-001: Dashboard (with tab navigation - single page)
SCR-002: Report Builder (handles Create + Edit)
SCR-003: Report View (handles Detail + Preview)
```

---

## Good Example: Design System Component

```
DES-001: Metric Card
Type: Component
Used In: SCR-001 (Dashboard), SCR-005 (Analytics), SCR-007 (Report Detail)
Purpose: Display single KPI with trend indicator and sparkline

States:
  - Default: Value + trend arrow + sparkline
  - Loading: Skeleton placeholder (animated)
  - Empty: "No data" with setup prompt
  - Error: "Failed to load" with retry button
  - Disabled: Grayed out (for locked features)

Variants:
  - Small: Dashboard grid (120x80px)
  - Large: Report detail (240x160px)
  - Compact: Mobile view (full width, 60px height)

Accessibility:
  - ARIA label: "[Metric name] is [value], [trend direction] [percent] from last period"
  - Color not sole indicator (trend arrow + text)
  - Minimum contrast 4.5:1
```

---

## Feature-to-Screen Matrix Example

| Feature | SCR-001 | SCR-002 | SCR-003 | SCR-010 |
|---------|---------|---------|---------|---------|
| FEA-001 (auto-sync) | Status | Config | | |
| FEA-003 (reports) | Preview | Full | | |
| FEA-007 (dashboard) | ✓ | | | |
| FEA-010 (auth) | | | | ✓ |
| FEA-015 (team) | Invite btn | | | Full |

**Reading the matrix:**
- FEA-001 shows status on dashboard, full config on SCR-002
- FEA-003 has preview on dashboard, full experience on SCR-002
- FEA-010 only appears on Settings (SCR-010)
- Every feature has at least one screen (no orphans)
