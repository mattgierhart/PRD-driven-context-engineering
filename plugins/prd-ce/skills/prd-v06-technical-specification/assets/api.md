# API- Template

Copy and fill for each API endpoint:

```
API-XXX: [Endpoint Name]
Method: [GET | POST | PUT | PATCH | DELETE]
Path: [/resource/{id}/action]
Purpose: [What this endpoint does]
Auth: [Public | User | Admin | Service]

Journey: [UJ-XXX]
Screen: [SCR-XXX]

Request:
  Headers:
    - Authorization: Bearer <token>
  Params:
    - [param]: [type] — Description
  Query:
    - [param]: [type] (optional/required, default X) — Description
  Body:
    {
      [field]: [type] — Description
    }

Response:
  Success (200/201):
    {
      data: { ... }
    }
  Errors:
    - 400: [When this occurs]
    - 401: [When this occurs]
    - 403: [When this occurs]
    - 404: [When this occurs]

Business Rules: [BR-XXX]
Data: [DBT-XXX]
Rate Limit: [X requests/minute]
```

## Method Selection Guide

| If the endpoint... | Method is... |
|--------------------|--------------|
| Retrieves data | GET |
| Creates new resource | POST |
| Replaces entire resource | PUT |
| Updates part of resource | PATCH |
| Removes resource | DELETE |

## Auth Levels

| Level | Who can access |
|-------|----------------|
| Public | Anyone, no token |
| User | Authenticated user |
| Admin | User with admin role |
| Service | Internal service-to-service |

## Checklist Before Adding

- [ ] Is this endpoint used by a SCR- or UJ-?
- [ ] Are all request parameters documented?
- [ ] Is the success response shape defined?
- [ ] Are all error cases documented?
- [ ] Is the auth level specified?
- [ ] Are DBT- tables identified?
