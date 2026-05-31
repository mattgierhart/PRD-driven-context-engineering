# API Contracts (SoT File)

## API-001 | GET /v1/items

- **Purpose**: List items for the current user.
- **Request**: query params `limit`, `offset`.
- **Response**: JSON array of item objects; pagination headers.
- **Related IDs**: [BR-001](SoT.BUSINESS_RULES.md#br-001) rate limit.

## API-002 | POST /v1/items/:id/archive

- **Purpose**: Archive an item. Irreversible; logged.
- **Request**: path param `id`.
- **Response**: 204 No Content on success.
- **Related IDs**: [BR-002](SoT.BUSINESS_RULES.md#br-002) audit logging.

## API-003 | GET /v1/health

- **Purpose**: Service liveness probe.
- **Request**: none.
- **Response**: `{status: "ok"}` with 200, otherwise 503.
- **Related IDs**: [ARC-001](SoT.TECHNICAL_DECISIONS.md#arc-001) architecture overview.
