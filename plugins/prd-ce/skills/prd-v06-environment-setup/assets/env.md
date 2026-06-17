# ENV- Entry Template

Copy and customize this template for your project's environment specifications.

---

## ENV-001: Development Environment

**ID**: ENV-001
**Category**: Development Setup
**Status**: Approved | Date: YYYY-MM-DD
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
# macOS (Homebrew)
brew install {tool1} {tool2}

# Linux (apt)
apt install {tool1} {tool2}

# Windows (winget/scoop)
winget install {tool1} {tool2}
```

| Tool | Version | Purpose |
|------|---------|---------|
| `{tool}` | `{version}` | {What it's used for} |

### Language-Specific Packages (Per-Project)

{List packages installed in project, not globally}

```bash
# Node.js/NPM
npm install --save-dev {package1} {package2}

# Python
pip install --dev {package1} {package2}

# Go
go install {package1}@latest
```

| Package | Purpose |
|---------|---------|
| `{package}` | {What it's used for} |

### Configuration Files

| File | Purpose |
|------|---------|
| `{config-file}` | {What it configures} |

### Scripts

Add to your package manifest (package.json, pyproject.toml, etc.):

```json
{
  "scripts": {
    "validate": "{command to run all quality checks}",
    "fix": "{command to auto-fix issues}",
    "test": "{command to run tests}",
    "build": "{command to build project}"
  }
}
```

### Environment Manager Tasks (Optional)

If using mise, add to `.mise.toml`:

```toml
[tasks.validate]
run = "{quality check command}"
description = "Run all quality checks"

[tasks.fix]
run = "{auto-fix command}"
description = "Auto-fix code issues"
```

### MCPs (Only if CLIs Insufficient)

**Rule**: Prefer CLIs over MCPs when both are available.

| Operation | CLI | MCP | Decision |
|-----------|-----|-----|----------|
| {operation} | {cli-name or "None"} | {mcp-name or "None"} | {Use CLI / Use MCP / N/A} |

### Verification

```bash
# 1. Verify system tools installed
{tool1} --version
{tool2} --version

# 2. Verify project packages installed
npm list --dev  # or equivalent

# 3. Verify quality checks work
npm run validate  # or equivalent

# 4. Verify tests pass
npm test  # or equivalent

# 5. Verify build works
npm run build  # or equivalent
```

### Troubleshooting

**Issue**: {Common problem}
**Fix**: {Solution}

**Issue**: {Another common problem}
**Fix**: {Solution}

### Related IDs

- [TECH-XXX](../SoT.TECHNICAL_DECISIONS.md#tech-xxx) - {Technology this environment supports}
- [ARC-XXX](../SoT.TECHNICAL_DECISIONS.md#arc-xxx) - {Architecture context}

---

## ENV-002: CI/CD Pipeline (Optional)

**ID**: ENV-002
**Category**: Automation
**Status**: Approved | Date: YYYY-MM-DD
**Owner**: {Team/Person responsible}

### Purpose

Document CI/CD pipeline configuration for automated testing and deployment.

### Workflow Files

| File | Purpose |
|------|---------|
| `.github/workflows/{name}.yml` | {What this workflow does} |

### Required Secrets

| Secret | Purpose | Where to Set |
|--------|---------|--------------|
| `{SECRET_NAME}` | {Purpose} | GitHub Settings → Secrets |

### Pipeline Stages

1. **Checkout**: Clone repository
2. **Setup**: Install dependencies (mirrors ENV-001)
3. **Validate**: Run quality checks
4. **Test**: Run test suite
5. **Build**: Create artifacts
6. **Deploy**: Deploy to environment (if applicable)

### Environment Matrix

| Environment | Trigger | Target |
|-------------|---------|--------|
| `staging` | Push to `main` | {staging URL} |
| `production` | Release tag | {production URL} |

### Related IDs

- [ENV-001](#env-001-development-environment) - Local environment this mirrors
- [DEP-XXX](../SoT.DEPLOYMENT.md#dep-xxx) - Deployment procedures

---

## ENV-003: Production Infrastructure (Optional)

**ID**: ENV-003
**Category**: Infrastructure
**Status**: Approved | Date: YYYY-MM-DD
**Owner**: {Team/Person responsible}

### Purpose

Document production hosting and services configuration.

### Hosting Platform

**Provider**: {AWS / GCP / Vercel / etc.}
**Region**: {Region}
**Tier**: {Free / Paid tier}

### Environment Variables

| Variable | Purpose | Required | Default |
|----------|---------|----------|---------|
| `{VAR_NAME}` | {Purpose} | Yes/No | {default or "None"} |

### Services

| Service | Purpose | Connection Method |
|---------|---------|-------------------|
| Database | {e.g., PostgreSQL} | {Connection string env var} |
| Cache | {e.g., Redis} | {Connection details} |
| Storage | {e.g., S3} | {Bucket configuration} |

### Scaling Configuration

| Resource | Min | Max | Trigger |
|----------|-----|-----|---------|
| {e.g., Web instances} | 1 | 10 | CPU > 70% |

### Related IDs

- [DEP-XXX](../SoT.DEPLOYMENT.md#dep-xxx) - Deployment procedures
- [MON-XXX](../SoT.DEPLOYMENT.md#mon-xxx) - Monitoring setup
- [RUN-XXX](../SoT.DEPLOYMENT.md#run-xxx) - Operational runbooks
