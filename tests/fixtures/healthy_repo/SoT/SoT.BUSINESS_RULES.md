# Business Rules (SoT File)

## BR-001 | Rate limit enforcement

- **Rule Statement**: Free tier limited to 100 requests per day.
- **Rationale**: Prevents abuse while allowing meaningful evaluation.
- **Related IDs**: [API-001](SoT.API_CONTRACTS.md#api-001), [UJ-001](SoT.USER_JOURNEYS.md#uj-001).

## BR-002 | Audit logging for sensitive actions

- **Rule Statement**: Every destructive action writes an immutable audit log entry.
- **Rationale**: Regulatory compliance and security forensics.
- **Related IDs**: [API-002](SoT.API_CONTRACTS.md#api-002), [ARC-001](SoT.TECHNICAL_DECISIONS.md#arc-001).

## BR-003 | Data residency

- **Rule Statement**: User data must be stored in the region selected at signup.
- **Rationale**: GDPR and data sovereignty requirements.
- **Related IDs**: [ARC-001](SoT.TECHNICAL_DECISIONS.md#arc-001), [DBT-001](SoT.DATA_MODEL.md#dbt-001).
