---
alwaysApply: true
---

# Coding Standards

## Traceability Protocol (MANDATORY)

Every major code unit must declare which ID it implements.

```typescript
// @implements BR-101 (Free Limit)
// @see API-045
export class RateLimiter { ... }
```

- **Tests First**: Create/Update tests (`TEST-`) for every feature.
- **No Secrets**: Never commit credentials.
- **Small Commits**: Group changes by ID/Feature.
