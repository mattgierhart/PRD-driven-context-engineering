---
version: 1.1
purpose: Source of Truth for technology choices, architecture decisions, and environment specifications.
id_prefix: TECH-XXX, ARC-XXX, ENV-XXX
last_updated: 2026-01-18
authority: This is a SoT file - IDs here are referenced by PRD.md, EPICs, and code
---

# Technical Decisions (SoT File)

> **Purpose**: Record technology selections, architecture decisions, and environment specifications.
> **ID Prefixes**: TECH-XXX (stack decisions), ARC-XXX (architecture decisions), ENV-XXX (environment setup)
> **Status**: Active SoT file
> **Cross-References**: Referenced by PRD.md v0.5-v0.6, SoT.API_CONTRACTS.md, EPICs

## Navigation by Category

**Stack Decisions** (TECH-001 to TECH-099):

- [TECH-001](#tech-001-decision-name) - {Technology decision}

**Architecture Decisions** (ARC-001 to ARC-099):

- [ARC-001](#arc-001-decision-name) - {Architecture decision}

**Environment Specifications** (ENV-001 to ENV-099):

- [ENV-001](#env-001-development-environment) - Development environment setup

---

## TECH-001: {Decision Name}

**ID**: TECH-001
**Category**: Frontend | Backend | Database | Infrastructure | DevOps
**Status**: Accepted | Deprecated | Superseded
**Decision Date**: YYYY-MM-DD
**Last Reviewed**: YYYY-MM-DD

### Context

{What problem or need drove this decision?}

### Decision

{What technology/approach was chosen?}

### Rationale

- **Chosen because**: {Primary reasons}
- **Alternatives considered**: {What else was evaluated}
- **Trade-offs accepted**: {Known downsides}

### Related IDs

- [API-XXX](SoT.API_CONTRACTS.md#api-xxx) - {API using this technology}
- [BR-XXX](SoT.BUSINESS_RULES.md#br-xxx) - {Business rule driving this choice}
- [INT-XXX](SoT.INTEGRATIONS.md#int-xxx) - {Integration enabled by this}

---

## ARC-001: {Decision Name}

**ID**: ARC-001
**Category**: Data Flow | Security | Scaling | Integration | Patterns
**Status**: Accepted | Deprecated | Superseded
**Decision Date**: YYYY-MM-DD
**Last Reviewed**: YYYY-MM-DD

### Context

{What architectural challenge needed solving?}

### Decision

{What architecture pattern/approach was chosen?}

### Rationale

- **Chosen because**: {Primary reasons}
- **Alternatives considered**: {What else was evaluated}
- **Consequences**: {What this enables or constrains}

### Related IDs

- [TECH-XXX](#tech-xxx-decision-name) - {Technology enabling this}
- [DBT-XXX](SoT.DATA_MODEL.md#dbt-xxx) - {Data model affected}
- [UJ-XXX](SoT.USER_JOURNEYS.md#uj-xxx) - {Journey this supports}

---

## ENV-001: Development Environment

**ID**: ENV-001
**Category**: Development Setup
**Status**: Template | Date: YYYY-MM-DD
**Last Reviewed**: YYYY-MM-DD
**Owner**: {Team/Person responsible}

### Purpose

Document the development environment requirements for this project. This enables:

- Consistent setups across team members
- Faster onboarding for new developers
- AI agent environment understanding
- Reproducible development builds

### CLIs (Global System Tools)

{List system-level tools installed via package manager}

```bash
# Example installation commands (customize for your project)
# brew install [tool1] [tool2]  # macOS
# apt install [tool1] [tool2]   # Linux
```

**Common categories:**

- Version managers (mise, asdf, nvm, pyenv)
- Data processing (jq, yq)
- API testing (httpie, curl)
- Search tools (ripgrep)
- Git workflows (gh CLI)

### Language-Specific Packages (Per-Project)

{List packages installed in project, not globally}

```bash
# Example for Node/NPM projects
# npm install --save-dev [package1] [package2]

# Example for Python projects
# pip install --dev [package1] [package2]
```

**Common categories:**

- Linting (eslint, ruff, golangci-lint)
- Formatting (prettier, black)
- Type checking (typescript, mypy)
- Testing (jest, pytest)

### Configuration Files

{List configuration files with brief purpose}

| File | Purpose |
|------|---------|
| `{config-file}` | {What it configures} |

### Scripts

{Define standard scripts in package manifest}

```json
{
  "scripts": {
    "validate": "{command to run all quality checks}",
    "fix": "{command to auto-fix issues}",
    "test": "{command to run tests}"
  }
}
```

### Environment Manager Tasks (Optional)

{If using mise, asdf, direnv, etc.}

```toml
# Example for mise (.mise.toml)
# [tasks.validate]
# run = "{quality check command}"
# description = "{what this validates}"
```

### MCPs (Only if CLIs Insufficient)

**Rule**: Prefer CLIs over MCPs when both are available.

| Operation | CLI Available | MCP Available | Use |
|-----------|---------------|---------------|-----|
| {operation} | {yes/no + name} | {yes/no + name} | {CLI/MCP} |

**Rationale**: CLIs work in all environments (local, CI/CD, cloud). MCPs only work in specific contexts.

### Verification

```bash
# Commands to verify environment is set up correctly

# 1. Verify system tools
# [tool1] --version
# [tool2] --version

# 2. Verify project packages
# {package manager ls command}

# 3. Verify quality checks work
# npm run validate  # or equivalent

# 4. Verify tests pass
# npm test  # or equivalent
```

### Troubleshooting

**Issue**: {Common problem}
**Fix**: {Solution}

### Related IDs

- [TECH-XXX](#tech-xxx-decision-name) - {Technology this environment supports}
- [ARC-XXX](#arc-xxx-decision-name) - {Architecture context}

---

## ENV-002: CI/CD Pipeline (Optional)

**ID**: ENV-002
**Category**: Automation
**Status**: Template | Date: YYYY-MM-DD

### Purpose

Document CI/CD pipeline configuration for automated testing and deployment.

### Workflow Files

{Reference workflow configuration files}

### Required Secrets

| Secret | Purpose | Where to Set |
|--------|---------|--------------|
| `{SECRET_NAME}` | {Purpose} | {GitHub/GitLab settings} |

### Pipeline Stages

1. **{Stage Name}**: {What happens}
2. **{Stage Name}**: {What happens}

### Related IDs

- [ENV-001](#env-001-development-environment) - Local environment this mirrors
- [DEP-XXX](SoT.DEPLOYMENT.md#dep-xxx) - Deployment steps

---

## ENV-003: Production Infrastructure (Optional)

**ID**: ENV-003
**Category**: Infrastructure
**Status**: Template | Date: YYYY-MM-DD

### Purpose

Document production hosting and services configuration.

### Hosting Platform

{Platform name and configuration}

### Environment Variables

| Variable | Purpose | Required |
|----------|---------|----------|
| `{VAR_NAME}` | {Purpose} | {Yes/No} |

### Services

| Service | Purpose | Connection |
|---------|---------|------------|
| {Service} | {Purpose} | {How connected} |

### Related IDs

- [DEP-XXX](SoT.DEPLOYMENT.md#dep-xxx) - Deployment procedures
- [MON-XXX](SoT.DEPLOYMENT.md#mon-xxx) - Monitoring setup

---

## Deprecated Decisions

### TECH-XXX: {Decision Name} [SUPERSEDED]

**Status**: Superseded (YYYY-MM-DD)
**Replacement**: [TECH-YYY](#tech-yyy-decision-name)
**Reason**: {Why decision was changed}
**Migration**: {How to transition}

---

## Cross-Reference Index

**Decisions by Domain**:

- Frontend: TECH-001, ARC-001
- Backend: TECH-002, ARC-002
- Environment: ENV-001, ENV-002, ENV-003

**Decisions by EPIC**:

- EPIC-01 implemented: TECH-001, ARC-001, ENV-001

---

## Update Protocol

### When to Add New IDs

1. **TECH-XXX**: Selecting a new technology, framework, or tool
2. **ARC-XXX**: Making a structural decision about system design
3. **ENV-XXX**: Documenting environment requirements (dev setup, CI/CD, infrastructure)

### Bidirectional Reference Checklist

When adding a new TECH/ARC/ENV-XXX:

- [ ] Update PRD.md v0.5/v0.6 section if applicable
- [ ] Update related API contracts if affected
- [ ] Update EPIC Section 2 "Context & IDs" list
- [ ] Update SoT.UNIQUE_ID_SYSTEM.md registry if maintained

---

*End of SoT.TECHNICAL_DECISIONS.md - Authoritative source for TECH-XXX, ARC-XXX, and ENV-XXX IDs*
