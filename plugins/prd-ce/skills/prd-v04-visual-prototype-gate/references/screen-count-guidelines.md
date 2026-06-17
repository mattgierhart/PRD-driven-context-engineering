# Screen Count Guidelines

> How many screens should the visual prototype include? Default to the lower end.

## By Product Type

| Product Type | Recommended Screens | Rationale |
|---|---|---|
| IDE extension / developer tool | 3–4 | Trigger → analysis → result. Developers hate unnecessary screens. |
| B2B SaaS workflow tool | 4–6 | Onboarding → core loop → outcome. Most common pattern. |
| Dashboard / reporting tool | 3–5 | Overview → drill-down → action. |
| Consumer app | 4–7 | Discovery → setup → use → delight. Consumer apps need more emotional arc. |
| API / integration product | 3–4 | Config → run → output. Often the UI is minimal by design. |
| Internal tool / admin panel | 3–5 | List → detail → action. Functional over beautiful. |

## Rules of Thumb

- **3 screens** is the minimum for communicating a value proposition
- **5 screens** is the sweet spot for most B2B products
- **>8 screens** in a prototype usually means scope creep — revisit MVP-SCOPE
- If every UJ- step is its own screen, you may be over-decomposing journeys
- Modals and panels count as screens if they contain primary actions

## Prioritization

If you must cut screens, prioritize in this order:
1. **Money Shot** — the one frame that communicates core value (always include)
2. **Entry point** — first thing user sees (login, dashboard, landing)
3. **Core action** — the screen where the primary job-to-be-done happens
4. **Outcome/confirmation** — user sees the result of their action
5. **Settings/admin** — cut first, prototype last
