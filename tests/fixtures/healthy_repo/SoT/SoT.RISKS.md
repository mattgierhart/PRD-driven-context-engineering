# Risks (SoT File)

## RISK-001 | Rate-limit bypass via token rotation

- **Description**: Free-tier users might rotate accounts to bypass BR-001 limit.
- **Mitigation**: IP-based secondary limiter; rate-limit on signup.
- **Related IDs**: [BR-001](SoT.BUSINESS_RULES.md#br-001).

## RISK-002 | Audit log tampering

- **Description**: Compromised service account could alter audit history.
- **Mitigation**: Append-only table with trigger blocking UPDATE/DELETE; off-site replication.
- **Related IDs**: [BR-002](SoT.BUSINESS_RULES.md#br-002), [DBT-002](SoT.DATA_MODEL.md#dbt-002).

## RISK-003 | Regional outage causing cross-region reads

- **Description**: If EU DB is down, app might fall back to US reads, violating BR-003.
- **Mitigation**: Hard region checks in query layer; fail closed.
- **Related IDs**: [BR-003](SoT.BUSINESS_RULES.md#br-003), [ARC-001](SoT.TECHNICAL_DECISIONS.md#arc-001).

## RISK-004 | JWT secret leak

- **Description**: Compromised signing key allows token forgery.
- **Mitigation**: KMS-backed signing; short token lifetime; rotate quarterly.
- **Related IDs**: [TECH-003](SoT.TECHNICAL_DECISIONS.md#tech-003).

## RISK-005 | Team skills gap: JWT operations

- **Description**: Team new to JWT lifecycle management.
- **Mitigation**: Runbook + oncall training before launch.
- **Related IDs**: [TECH-003](SoT.TECHNICAL_DECISIONS.md#tech-003).
