---
version: 1.3
purpose: To provide a complete guide for setting up and configuring a development, staging, or production environment for a project.
summary: Added progressive documentation features, model-specific guidance, and testing-first approach.
last_updated: 2025-07-06
epic_id: EPIC-01
epic_name: "{Environment Name} Setup"
epic_type: "environment"
status: "planning"
model_restrictions: "none"
---

# EPIC-01: Environment Setup - [Environment Name] v{0.1}

## Epic Meta Information
| Field | Value |
|-------|-------|
| **Current Version** | v0.1 |
| **Planning Version** | v0.1-0.3 (Opus) |
| **Execution Version** | v0.4+ (Sonnet) |
| **Last Updated** | [Date and Time] |
| **Last Editor** | [Model/User] |
| **Status** | Planning Phase |
| **Completion** | 0% |

## Version History
| Version | Date | Editor | Changes |
|---------|------|--------|---------|
| v0.1 | [Date] | [Editor] | Initial environment setup plan |

## Quick Navigation
- [Overview](#overview)
- [Environment Requirements](#environment-requirements)
- [Testing Infrastructure](#testing-infrastructure)
- [Setup Instructions](#setup-instructions)
- [Configuration](#configuration)
- [Verification](#verification)
- [Progress Log](#progress-log)
- [Handoff History](#handoff-history)

**Authority**: See [WORKFLOW_MASTER.md](../workflows/WORKFLOW_MASTER.md) for complete workflow processes  
**Template Usage**: See [README.md](./README.md) for template usage guide  
**Standards**: See [STANDARDS.md](../../STANDARDS.md) for documentation hierarchy

## Overview
**Purpose**: Define complete environment setup and configuration
**Scope**: [Development/Staging/Production]
**Priority**: [High/Medium/Low]
**Created**: [Date]
**Last Updated**: [Date]

## Environment Requirements

### System Requirements
- **OS**: [Required OS versions]
- **Runtime**: [Node.js, Python, etc. versions]
- **Memory**: [Minimum RAM]
- **Storage**: [Minimum disk space]

### Dependencies
```json
{
  "runtime": {
    "node": ">=18.0.0",
    "npm": ">=9.0.0"
  },
  "global": [
    "vercel@latest",
    "railway@latest"
  ]
}
```

## Testing Infrastructure {#testing-infrastructure}
<!-- Model: opus for planning, sonnet for setup -->

### Testing Framework Setup
**Required Before Development (Gate 3.5)**:
- [ ] Jest configuration for unit tests
- [ ] Testing library setup for integration tests
- [ ] E2E framework selection and setup
- [ ] Test database configuration
- [ ] Mock services configuration
- [ ] Coverage reporting setup

### Test Environment Variables
```env
# Test Database
TEST_DATABASE_URL=postgresql://test:test@localhost:5432/test_db

# Test Services
TEST_REDIS_URL=redis://localhost:6380
TEST_API_URL=http://localhost:3001
```

### Testing Commands
```bash
# Verify test setup
npm run test:setup:verify

# Run all tests
npm test

# Coverage report
npm run test:coverage
```

## Setup Instructions {#setup-instructions}

### 1. Prerequisites
- [ ] Install required runtime versions
- [ ] Configure package managers
- [ ] Set up version managers (nvm, pyenv, etc.)
- [ ] Install global dependencies

### 2. Repository Setup
```bash
# Clone repository
git clone [repository-url]
cd [project-name]

# Install dependencies
npm install

# Copy environment variables
cp .env.example .env.local
```

### 3. Environment Variables
```env
# Application
NODE_ENV=development
APP_URL=http://localhost:3000

# Database
DATABASE_URL=postgresql://user:pass@localhost:5432/dbname
REDIS_URL=redis://localhost:6379

# External Services
STRIPE_SECRET_KEY=sk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...

# Authentication
NEXTAUTH_URL=http://localhost:3000
NEXTAUTH_SECRET=generated-secret-here
```

### 4. Database Setup
```bash
# Create database
createdb [database-name]

# Run migrations
npm run db:migrate

# Seed data (optional)
npm run db:seed
```

### 5. Service Configuration

#### Local Services
- **PostgreSQL**: Port 5432
- **Redis**: Port 6379
- **Application**: Port 3000

#### Docker Compose (Optional)
```yaml
version: '3.8'
services:
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: myapp
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    ports:
      - "5432:5432"
  
  redis:
    image: redis:7
    ports:
      - "6379:6379"
```

## Verification Steps

### 1. Environment Check
```bash
# Verify installations
node --version
npm --version
psql --version
redis-cli --version

# Check environment
npm run env:check
```

### 2. Connection Tests
- [ ] Database connection
- [ ] Redis connection
- [ ] External API connections
- [ ] File storage access

### 3. Initial Run
```bash
# Start development server
npm run dev

# Expected output
# ✓ Ready on http://localhost:3000
# ✓ Database connected
# ✓ Redis connected
```

## Troubleshooting

### Common Issues

#### Port Conflicts
```bash
# Find process using port
lsof -i :3000

# Kill process
kill -9 [PID]
```

#### Permission Errors
```bash
# Fix npm permissions
npm config set prefix ~/.npm-global
export PATH=~/.npm-global/bin:$PATH
```

#### Database Connection Failed
- Check PostgreSQL is running
- Verify credentials in .env
- Check firewall settings

## Environment-Specific Configurations

### Development
- Hot reload enabled
- Debug logging active
- Mock services available

### Staging
- Production builds
- Real service integrations
- Performance monitoring

### Production
- Optimized builds
- Security hardening
- Full monitoring suite

## Maintenance

### Regular Tasks
- [ ] Update dependencies monthly
- [ ] Rotate secrets quarterly
- [ ] Review environment variables
- [ ] Clean up old logs/cache

### Backup Procedures
```bash
# Backup database
pg_dump [database] > backup-$(date +%Y%m%d).sql

# Backup environment
cp .env .env.backup-$(date +%Y%m%d)
```

## Sub-Agent Commands

### Environment Analysis
```bash
@arch-review . --focus-on-config
@tech-debt-finder-fixer .env* --dry-run
```

### Setup Automation
```bash
@new-feature "environment setup script" --target scripts/
@test-gen scripts/setup.js
```

## Success Criteria
- [ ] All services start without errors
- [ ] All tests pass locally
- [ ] Development workflow is smooth
- [ ] Environment is reproducible

## Notes
[Additional environment-specific notes]

## Configuration {#configuration}
<!-- Document key configuration decisions here -->

## Implementation Tasks
<!-- Model: opus for planning, sonnet for execution -->

### Task Template
```markdown
#### Task [ID] - [Task Title]
*   **Status:** `To Do` | `In Progress` | `Done` | `Blocked` | `blocked-for-opus` | `blocked-for-user`
*   **Model Suitability:** `opus-only` | `sonnet-ready` | `either`
*   **User Action Required:** [If blocked-for-user, specify what's needed: API key, decision, access, etc.]
*   **Context:** [Why this task is necessary]
*   **Action Plan:** [What needs to be done]
*   **Validation:** [How to verify completion]
```

## Verification {#verification}
<!-- Document verification steps and results -->

## Progress Log {#progress-log}
<!-- APPEND new entries, don't replace -->
- [Date]: Environment planning started
- [Date]: Testing infrastructure configured
- [Date]: Development environment verified

## Handoff History {#handoff-history}
<!-- Track model transitions and blockers -->

<!-- HANDOFF: From [Model] to [Model] - [Date] -->
<!-- Summary of what was completed and what needs attention -->
<!-- END HANDOFF -->

## Gemini's Development Considerations
<!-- This section will be added by Gemini during review -->
<!-- Do not edit this section unless you are Gemini -->

---
*Template Version: 1.3*