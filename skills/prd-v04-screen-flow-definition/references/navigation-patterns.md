# Navigation Patterns Guide

## Pattern Overview

| Pattern | Structure | Best For |
|---------|-----------|----------|
| **Hub & Spoke** | Central hub, navigate out and back | Dashboard apps, CRMs |
| **Linear Flow** | Step 1 → Step 2 → Step 3 | Onboarding, Checkout |
| **Hierarchical** | Category → Subcategory → Item | Content apps, Documentation |
| **Flat** | All screens peer-level | Simple tools, Utilities |

---

## Hub & Spoke

```
          ┌─────────────┐
          │  Dashboard  │ ← Hub (always accessible)
          │   (Hub)     │
          └──────┬──────┘
       ┌─────────┼─────────┐
       ▼         ▼         ▼
┌──────────┐ ┌──────────┐ ┌──────────┐
│ Reports  │ │  Data    │ │ Settings │ ← Spokes
│ (Spoke)  │ │ (Spoke)  │ │ (Spoke)  │
└──────────┘ └──────────┘ └──────────┘
```

**When to use:**
- User needs quick access to multiple features
- No strict sequence required
- Dashboard provides orientation/status

**Implementation:**
- Persistent nav bar with hub access
- Each spoke has "back to dashboard" path
- Spokes can link to each other (not required)

---

## Linear Flow

```
┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
│  Step 1  │ → │  Step 2  │ → │  Step 3  │ → │ Complete │
│  (Info)  │   │ (Config) │   │ (Review) │   │ (Success)│
└──────────┘   └──────────┘   └──────────┘   └──────────┘
     ↑              ↑              ↑
     └──────────────┴──────────────┘
              (Back navigation)
```

**When to use:**
- Tasks with required sequence
- Onboarding flows
- Checkout/purchase flows
- Setup wizards

**Implementation:**
- Progress indicator showing current step
- Back button at each step
- "Skip" option only if step is optional
- Exit with confirmation ("Are you sure?")

---

## Hierarchical

```
┌─────────────────────────────────────────┐
│               Categories                │
│  [Docs]  [API]  [Guides]  [Support]     │
└────────────────────┬────────────────────┘
                     ▼
┌─────────────────────────────────────────┐
│          Docs → Subcategories           │
│  [Getting Started]  [Advanced]  [FAQ]   │
└────────────────────┬────────────────────┘
                     ▼
┌─────────────────────────────────────────┐
│     Getting Started → Articles          │
│  [Install]  [First Steps]  [Config]     │
└────────────────────┬────────────────────┘
                     ▼
┌─────────────────────────────────────────┐
│           Article Detail                │
│  [Content...]                           │
└─────────────────────────────────────────┘
```

**When to use:**
- Content-heavy applications
- Documentation sites
- E-commerce catalogs
- File managers

**Implementation:**
- Breadcrumb navigation
- Sidebar showing hierarchy
- Parent/child relationships clear
- Search as escape hatch

---

## Flat

```
┌──────────┐   ┌──────────┐   ┌──────────┐
│ Screen A │ ↔ │ Screen B │ ↔ │ Screen C │
└──────────┘   └──────────┘   └──────────┘
      ↑              ↑              ↑
      └──────────────┴──────────────┘
           (All screens peer-level)
```

**When to use:**
- Simple single-purpose tools
- Few screens (3-5)
- No natural hierarchy
- Quick utilities

**Implementation:**
- Tab bar or simple toggle
- All screens equally accessible
- Minimal navigation chrome

---

## Hybrid Patterns

Most products combine patterns:

```
Hub & Spoke (main app)
    │
    ├── Dashboard (hub)
    │       ├── Reports (spoke)
    │       ├── Settings (spoke)
    │       └── Data (spoke)
    │
    └── Linear Flow (onboarding)
            ├── Step 1: Account
            ├── Step 2: Connect Data
            └── Step 3: First Report
```

**Rule**: Use linear for sequences, hub & spoke for daily use.

---

## Navigation Elements

| Element | Purpose | When to Use |
|---------|---------|-------------|
| **Top Nav** | Global navigation | Hub access, user menu |
| **Sidebar** | Section navigation | Hierarchical, many options |
| **Tabs** | In-page navigation | Related content, same level |
| **Breadcrumbs** | Location + back navigation | Hierarchical depth |
| **Back Button** | Previous screen | Linear flows, detail views |
| **Bottom Nav** | Mobile primary actions | Mobile apps, 3-5 items |

---

## Anti-Patterns

| Anti-Pattern | Problem | Fix |
|--------------|---------|-----|
| **Hamburger everything** | Hides important nav | Use visible nav for key items |
| **No breadcrumbs in hierarchy** | User gets lost | Add breadcrumbs for depth >2 |
| **Linear without progress** | User doesn't know how long | Show step indicator |
| **Dead-end screens** | Can't navigate away | Always provide escape path |
| **Inconsistent nav location** | User relearns each page | Keep nav in same position |
