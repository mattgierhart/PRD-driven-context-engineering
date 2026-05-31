# Testing (SoT File)

## TEST-001 | List items honors rate limit

- **Given**: free-tier user with 100 requests already used today
- **When**: user calls API-001 again
- **Then**: 429 Too Many Requests; BR-001 enforced.
- **Covers**: [API-001](SoT.API_CONTRACTS.md#api-001), [BR-001](SoT.BUSINESS_RULES.md#br-001).

## TEST-002 | Archive writes audit log

- **Given**: authenticated user and an unarchived item
- **When**: user calls API-002 archive endpoint
- **Then**: item archived; AuditLog entry created per BR-002; DBT-002 persisted.
- **Covers**: [API-002](SoT.API_CONTRACTS.md#api-002), [BR-002](SoT.BUSINESS_RULES.md#br-002), [DBT-002](SoT.DATA_MODEL.md#dbt-002).

## TEST-003 | Health endpoint returns 200 when DB reachable

- **Given**: service running with DB connection
- **When**: GET API-003 health endpoint
- **Then**: 200 with `{status: "ok"}`.
- **Covers**: [API-003](SoT.API_CONTRACTS.md#api-003).

## TEST-004 | Data stored in selected region

- **Given**: user signs up selecting EU region
- **When**: user creates an item
- **Then**: row persisted in EU database shard per BR-003.
- **Covers**: [BR-003](SoT.BUSINESS_RULES.md#br-003), [DBT-001](SoT.DATA_MODEL.md#dbt-001).
