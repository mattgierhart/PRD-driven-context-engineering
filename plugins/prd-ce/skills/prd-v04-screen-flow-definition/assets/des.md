# DES- Template

Copy and fill for each design system element:

```
DES-XXX: [Component/Pattern Name]
Type: [Component | Pattern | Layout]
Used In: [SCR-XXX, SCR-YYY]
Purpose: [What this element does]

States:
  - Default: [Normal state]
  - Loading: [When fetching data]
  - Empty: [No data state]
  - Error: [Error state]
  - Disabled: [When not interactive]

Variants: [If multiple versions exist]
Accessibility: [A11y considerations]
```

## Type Selection Guide

| If the element... | Type is... |
|-------------------|------------|
| Is a single reusable UI element | Component |
| Is a recurring interaction approach | Pattern |
| Is a page structure template | Layout |

## Common Components to Define

- Navigation (header, sidebar, breadcrumbs)
- Data display (cards, tables, lists)
- Forms (inputs, selects, buttons)
- Feedback (alerts, toasts, modals)
- Status (loading, empty, error states)

## Checklist Before Adding

- [ ] Is this element used on 2+ screens?
- [ ] Are all relevant states defined?
- [ ] Are accessibility requirements noted?
- [ ] Would an existing component work instead?
