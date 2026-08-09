---
alwaysApply: true
---

# Coding Standards

## Traceability Protocol (MANDATORY)

Every major code unit must declare which ID it implements.

```typescript
// @implements BR-101 (Free Limit)
// @see API-045
// @verifies BR-101   (on the test that checks it)
export class RateLimiter { ... }
```

These tags are not just comments — in v0.7 they are **harvested into the Development Graph** (`status/devgraph.json`) as bridge edges (`implements` / `verifies` / `references`) linking each code unit to the spec ID it realizes. That graph is what readiness uses to measure build-vs-blueprint (`implementation_coverage`) and what an optional visualization consumer may render. Untagged code shows up as an `orphan` node — a context leak. See [`docs/DEVELOPMENT_GRAPH.md`](../templates/docs/DEVELOPMENT_GRAPH.md).

- **Tests First**: Create/Update tests (`TEST-`) for every feature.
- **No Secrets**: Never commit credentials.
- **Small Commits**: Group changes by ID/Feature.
- **Tag Everything**: Every major unit carries `@implements`; tests carry `@verifies`. No orphan code.
