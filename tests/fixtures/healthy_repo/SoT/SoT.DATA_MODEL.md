# Data Model (SoT File)

## DBT-001 | Item

- **Description**: Core user-owned record.
- **Fields**: id (uuid), owner_id (uuid), created_at, archived_at (nullable), region.
- **Relationships**: belongs_to User; has_many AuditLog entries.
- **Related IDs**: [BR-003](SoT.BUSINESS_RULES.md#br-003) data residency.

## DBT-002 | AuditLog

- **Description**: Immutable append-only log of sensitive actions.
- **Fields**: id, actor_id, action, target_id, timestamp, metadata JSON.
- **Relationships**: belongs_to User (actor).
- **Related IDs**: [BR-002](SoT.BUSINESS_RULES.md#br-002) audit logging.

## DBT-003 | User

- **Description**: Registered user with region preference and auth identity.
- **Fields**: id (uuid), email, region, oauth_subject, created_at.
- **Relationships**: has_many Item (DBT-001); has_many AuditLog (DBT-002).
- **Related IDs**: [BR-003](SoT.BUSINESS_RULES.md#br-003), [TECH-003](SoT.TECHNICAL_DECISIONS.md#tech-003).
