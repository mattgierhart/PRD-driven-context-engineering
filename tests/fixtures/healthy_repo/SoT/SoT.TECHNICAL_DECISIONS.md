# Technical Decisions (SoT File)

## TECH-001 | Backend runtime: Node.js

- **Decision**: Use Node.js 20 LTS for backend services.
- **Rationale**: Strong ecosystem for HTTP services; aligns with team expertise.
- **Alternatives Considered**: Go (faster compile/runtime but smaller hiring pool), Python (slower for hot paths).

## TECH-002 | Database: PostgreSQL

- **Decision**: PostgreSQL 16 via managed service.
- **Rationale**: ACID guarantees needed for audit logs; team fluent in SQL.
- **Alternatives Considered**: MongoDB (weaker consistency), DynamoDB (vendor lock-in).

## TECH-003 | Auth: OAuth + JWT

- **Decision**: OAuth 2.0 issuer + short-lived JWT access tokens.
- **Rationale**: Standard pattern; avoids custom crypto.
- **Alternatives Considered**: Session cookies (simpler but harder for mobile), custom tokens (NIH risk).

## ARC-001 | Three-tier architecture

- **Decision**: Web frontend → API gateway → service layer → PostgreSQL.
- **Rationale**: Clear separation; allows independent scaling of layers.
- **Alternatives Considered**: Monolith (faster to ship but harder to scale), event-driven (operational overhead not justified for MVP).
- **Related IDs**: [BR-003](SoT.BUSINESS_RULES.md#br-003), [DBT-001](SoT.DATA_MODEL.md#dbt-001).
