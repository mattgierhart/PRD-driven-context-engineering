---
version: 1.3
purpose: To define a comprehensive deployment strategy and procedure for a project, ensuring smooth and reliable releases.
summary: Added progressive documentation features, model-specific guidance, and testing-first approach.
last_updated: 2025-07-06
epic_id: EPIC-05
epic_name: "{Project Name} Deployment"
epic_type: "deployment"
status: "planning"
model_restrictions: "none"
---

# EPIC-05: Deployment - [Project Name] v{0.1}

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
| v0.1 | [Date] | [Editor] | Initial deployment strategy |

## Quick Navigation
- [Overview](#overview)
- [Deployment Architecture](#deployment-architecture)
- [Pre-Deployment Testing](#pre-deployment-testing)
- [Pre-Deployment Checklist](#pre-deployment-checklist)
- [Deployment Procedures](#deployment-procedures)
- [Post-Deployment](#post-deployment)
- [Rollback Procedures](#rollback-procedures)
- [Progress Log](#progress-log)
- [Handoff History](#handoff-history)

**Authority**: See [WORKFLOW-MASTER.md](../workflows/WORKFLOW-MASTER.md) for complete workflow processes  
**Template Usage**: See [README.md](./README.md) for template usage guide  
**Standards**: See [STANDARDS.md](../../STANDARDS.md) for documentation hierarchy

## Overview
**Purpose**: Define deployment strategy and procedures
**Environments**: [Dev → Staging → Production]
**Deployment Type**: [Continuous/Scheduled/Manual]
**Created**: [Date]
**Last Updated**: [Date]

## Deployment Architecture

### Infrastructure Overview
```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│    Local    │ --> │   Staging   │ --> │ Production  │
│    Dev      │     │   Server    │     │   Server    │
└─────────────┘     └─────────────┘     └─────────────┘
       |                   |                    |
       v                   v                    v
   Feature          Preview/Test           Live Users
   Branches          Environment            Environment
```

### Technology Stack
- **Frontend Hosting**: Vercel
- **Backend Platform**: Supabase (Database + Auth + Storage + Edge Functions)
- **CDN**: Vercel Edge Network
- **Monitoring**: Supabase Dashboard + Vercel Analytics + Sentry

**Tech Stack Details**: See [TECH-STACK-BLUEPRINT.md](../tech-stack/TECH-STACK-BLUEPRINT.md)

## Pre-Deployment Testing {#pre-deployment-testing}
<!-- Model: opus for strategy, sonnet for execution -->

### Testing Requirements (Gate 4)
**All Tests Must Pass Before Deployment**:
- [ ] Unit tests: 100% pass rate
- [ ] Integration tests: All critical paths verified
- [ ] E2E tests: User journeys validated
- [ ] Performance tests: Benchmarks met
- [ ] Security scan: No high/critical vulnerabilities
- [ ] Accessibility audit: WCAG 2.1 AA compliant

### Test Commands
```bash
# Full test suite
npm run test:all

# Pre-deployment validation
npm run test:pre-deploy

# Performance check
npm run test:performance

# Security audit
npm run audit:security
```

## Pre-Deployment Checklist {#pre-deployment-checklist}

### Code Quality
- [ ] All tests passing
- [ ] Code review completed
- [ ] No console errors/warnings
- [ ] Security scan passed

### Performance
- [ ] Bundle size < 500KB
- [ ] Lighthouse score > 90
- [ ] Load time < 2 seconds
- [ ] API response < 500ms

### Configuration
- [ ] Environment variables set
- [ ] Secrets rotated if needed
- [ ] Feature flags configured
- [ ] Rate limits configured

## Deployment Process

### 1. Staging Deployment

#### Automatic (CI/CD)
```yaml
# .github/workflows/deploy-staging.yml
name: Deploy to Staging
on:
  push:
    branches: [develop]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
      - run: npm ci
      - run: npm test
      - run: npm run build
      - run: vercel --prod --env=staging
```

#### Manual
```bash
# Build and test
npm run build
npm test

# Deploy to staging
vercel --env=staging

# Or using Supabase CLI
railway up --environment=staging
```

### 2. Production Deployment

#### Pre-Production Steps
1. **Create Release Branch**
   ```bash
   git checkout -b release/v1.2.3
   git push origin release/v1.2.3
   ```

2. **Final Checks**
   - [ ] Staging tested thoroughly
   - [ ] Database migrations ready
   - [ ] Rollback plan documented
   - [ ] Team notified

3. **Tag Release**
   ```bash
   git tag -a v1.2.3 -m "Release version 1.2.3"
   git push origin v1.2.3
   ```

#### Production Deploy
```bash
# Using Vercel
vercel --prod

# Using Supabase
railway up --environment=production

# Using custom script
npm run deploy:production
```

### 3. Post-Deployment

#### Verification
- [ ] Application loads correctly
- [ ] Critical user flows work
- [ ] Monitoring shows normal metrics
- [ ] No error spike in logs

#### Smoke Tests
```bash
# Run smoke tests
npm run test:smoke

# Check critical endpoints
curl https://api.example.com/health
curl https://api.example.com/api/status
```

## Rollback Procedures

### Immediate Rollback (< 5 minutes)
```bash
# Vercel
vercel rollback

# Supabase
railway rollback

# Git revert
git revert HEAD
git push origin main
```

### Database Rollback
```bash
# Backup current state
pg_dump production_db > backup_emergency.sql

# Restore previous version
psql production_db < backup_previous.sql

# Run rollback migrations
npm run db:rollback
```

### Emergency Procedures
1. **Enable maintenance mode**
   ```bash
   vercel env pull
   echo "MAINTENANCE_MODE=true" >> .env
   vercel env push
   ```

2. **Notify users**
   - Update status page
   - Send notification emails
   - Post on social media

3. **Fix and redeploy**
   ```bash
   # Fix issues
   # Test thoroughly
   # Deploy fix
   vercel --prod --force
   ```

## Environment Configuration

### Staging Environment
```env
NODE_ENV=staging
APP_URL=https://staging.example.com
DATABASE_URL=postgresql://staging-connection
STRIPE_SECRET_KEY=sk_test_...
```

### Production Environment
```env
NODE_ENV=production
APP_URL=https://example.com
DATABASE_URL=postgresql://prod-connection
STRIPE_SECRET_KEY=sk_live_...
```

## Monitoring & Alerts

### Health Checks
```javascript
// pages/api/health.js
export default function handler(req, res) {
  const checks = {
    database: checkDatabase(),
    redis: checkRedis(),
    stripe: checkStripe(),
  };
  
  const healthy = Object.values(checks).every(Boolean);
  res.status(healthy ? 200 : 503).json({ 
    status: healthy ? 'healthy' : 'unhealthy',
    checks 
  });
}
```

### Alert Configuration
- **Downtime**: Immediate notification
- **Error Rate > 5%**: Alert within 5 minutes
- **Response Time > 1s**: Alert within 15 minutes
- **Failed Deployments**: Immediate notification

## Security Considerations

### Pre-Deployment Security
- [ ] Dependencies updated
- [ ] Security headers configured
- [ ] HTTPS enforced
- [ ] API rate limiting enabled

### Secret Management
```bash
# Rotate secrets
vercel env rm STRIPE_SECRET_KEY
vercel env add STRIPE_SECRET_KEY

# Verify secrets
vercel env pull
cat .env.local | grep -E "KEY|SECRET|TOKEN"
```

## Cost Management

### Deployment Costs
- **Vercel**: $20/month (Pro plan)
- **Supabase**: Free tier (generous) then $25/month Pro
- **Monitoring**: $0-10/month

### Cost Optimization
- Enable caching headers
- Optimize images and assets
- Use CDN for static files
- Monitor usage weekly

## Sub-Agent Integration

### Pre-Deployment Analysis
```bash
@arch-review . --pre-deploy-audit
@tech-debt-finder-fixer . --critical-only
@perf-optimize . --validate
```

### Deployment Automation
```bash
@new-feature "deployment automation" --target .github/workflows/
@test-gen scripts/deploy.js --smoke-tests
```

## Success Metrics
- [ ] Zero-downtime deployment
- [ ] < 2 minute deployment time
- [ ] Automatic rollback capability
- [ ] 99.9% uptime achieved

## Deployment Schedule
- **Staging**: Continuous (every commit)
- **Production**: Tuesday/Thursday mornings
- **Hotfixes**: As needed with approval

## Documentation
- [ ] Deployment guide updated
- [ ] Runbook current
- [ ] Team trained on procedures
- [ ] Emergency contacts listed

## Deployment Procedures {#deployment-procedures}
<!-- Detailed deployment steps will be documented here -->

### Task Template
```markdown
#### Task [ID] - [Task Title]
*   **Status:** `To Do` | `In Progress` | `Done` | `Blocked` | `blocked-for-opus` | `blocked-for-user`
*   **Model Suitability:** `opus-only` | `sonnet-ready` | `either`
*   **User Action Required:** [If blocked-for-user, specify what's needed: deployment approval, credentials, DNS setup, etc.]
*   **Context:** [Why this task is necessary]
*   **Action Plan:** [What needs to be done]
*   **Validation:** [How to verify completion]
```

## Post-Deployment {#post-deployment}
<!-- Post-deployment verification and monitoring -->

## Rollback Procedures {#rollback-procedures}
<!-- Emergency rollback procedures documented above -->

## Progress Log {#progress-log}
<!-- APPEND new entries, don't replace -->
- [Date]: Deployment strategy planning started
- [Date]: CI/CD pipeline configured
- [Date]: First successful staging deployment
- [Date]: Production deployment completed

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