# SCR- Template

Copy and fill for each screen:

```
SCR-XXX: [Screen Name]
Type: [Page | Modal | Panel | Component]
Purpose: [What user accomplishes on this screen]
Journeys: [UJ-XXX, UJ-YYY that use this screen]
Features: [FEA-XXX, FEA-YYY rendered on this screen]

Primary Actions: [Key user actions available]
Secondary Actions: [Less common but available actions]

Navigation:
  From: [SCR-XXX, SCR-YYY]
  To: [SCR-XXX, SCR-YYY]

Content:
  - [Data/element 1]
  - [Data/element 2]

Constraints: [BR-XXX rules affecting this screen]
Design Notes: [Persona-specific considerations]
```

## Type Selection Guide

| If the screen... | Type is... |
|------------------|------------|
| Is a primary navigation target | Page |
| Blocks the page for user decision | Modal |
| Shows contextual details alongside main content | Panel |
| Is reused across multiple pages | Component |

## Checklist Before Adding

- [ ] Is this screen part of at least one UJ-?
- [ ] Does this screen render at least one FEA-?
- [ ] Are navigation paths defined (From + To)?
- [ ] Are BR- constraints considered?
- [ ] Would a modal/panel work instead of a new page?
