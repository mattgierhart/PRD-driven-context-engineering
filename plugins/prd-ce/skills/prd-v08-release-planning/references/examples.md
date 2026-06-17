# Deployment Plan Examples

**Purpose**: Good and bad patterns for deployment planning (DEP-XXX entries).

---

## Good Example 1: Low-Risk Feature Deployment

### Context

- **Product**: SaaS project management tool
- **Change**: Add "Dark Mode" UI feature
- **Risk**: Low (UI only, no backend changes)
- **Traffic**: 50,000 requests/hour

---

### DEP-045: Dark Mode Feature Deployment

**ID**: DEP-045
**Type**: Release
**Environment**: Production
**Strategy**: Feature Flag
**Owner**: Frontend Team
**Created**: 2026-01-10
**Target Date**: 2026-01-12 14:00 UTC
**Status**: Planned

---

**Summary**:

**What**: Deploy dark mode UI toggle feature
**Why**: Top user request (CFD-089), improves accessibility
**Risk Level**: Low (CSS/UI only, no data/API changes)
**Deployment Window**: 2026-01-12 14:00 UTC (normal business hours, no downtime)
**Estimated Duration**: 15 minutes (code deploy)
**Rollback Estimated Duration**: < 1 minute (feature flag toggle)

---

**Changes Included**:
- [FEA-112]: Dark mode CSS theme
- [FEA-113]: Theme toggle in user settings (UI-005)

**Database Migrations**: None

**Dependencies**: None

---

**Pre-Deployment Checklist**:

**Code Quality**:
- [x] All tests passing (TEST-045, TEST-046)
- [x] Code review approved
- [x] Accessibility testing complete (WCAG AA compliance)

**Documentation**:
- [x] Help docs updated (dark mode instructions)
- [x] API documentation: N/A (no API changes)

**Infrastructure**:
- [x] CSS assets tested in staging
- [x] CDN cache invalidation tested

**Communication**:
- [x] Announced in product newsletter (launching this week)
- [x] Support team trained (how to enable dark mode)

**Rollback Plan**:
- [x] Rollback procedure: Toggle `dark_mode_enabled` flag OFF
- [x] Tested in staging: Yes

---

**Deployment Steps**:

**Step 1: Deploy Code with Flag OFF**
1. [x] Deploy v2.4.0 to production (dark mode code, flag OFF)
2. [x] Verify deployment successful (no errors)
3. [x] Dark mode code present but inactive (flag OFF)

**Success Criteria**: Deployment completes, no errors, users see no changes

---

**Step 2: Enable for Internal Users**
1. [x] Enable `dark_mode_enabled` flag for internal team (20 users)
2. [x] Internal team tests dark mode across browsers
3. [x] Verify no visual bugs

**Success Criteria**: Internal team confirms dark mode works

---

**Step 3: Enable for 10% of Users (Canary)**
1. [x] Enable flag for 10% of users (5,000 users)
2. [x] Monitor for 2 hours:
   - Error rate (expect: < 0.1%, same as baseline)
   - Page load time (expect: < 2s, same as baseline)
   - Support tickets (expect: < 5, mostly "how to find it")

**Success Criteria**: No increase in errors, support tickets manageable

**Rollback Trigger**: Error rate > 0.5% (indicates CSS breaking page functionality)

---

**Step 4: Enable for 100% of Users**
1. [x] Enable flag for 100% of users
2. [x] Monitor for 24 hours
3. [x] Send product update email ("Dark mode now available!")

**Success Criteria**: No issues reported, positive user feedback

---

**Rollback Plan**:

**Trigger**: Error rate > 0.5%, CSS breaking functionality, accessibility violations reported

**Procedure**:
1. Toggle `dark_mode_enabled` flag OFF (< 1 minute)
2. Verify users back to light mode
3. Investigate issue offline

**Estimated Rollback Time**: < 1 minute

---

**Why This is Good**:

✅ **Feature flag strategy** (instant rollback, no code deploy)
✅ **Gradual rollout** (internal → 10% → 100%)
✅ **Clear success criteria** (error rate, page load time)
✅ **Communication plan** (product newsletter, support trained)
✅ **Low risk acknowledged** (UI only, no backend/data changes)
✅ **Realistic timeline** (hours between stages, not minutes)

---

## Good Example 2: High-Risk Database Migration

### Context

- **Product**: E-commerce platform
- **Change**: Add "user_email_verified" column to support email verification feature
- **Risk**: High (database schema change, 10M user records)
- **Traffic**: 100,000 requests/hour

---

### DEP-067: User Email Verification Migration

**ID**: DEP-067
**Type**: Migration
**Environment**: Production
**Strategy**: Rolling (multi-stage migration)
**Owner**: Backend Team
**Created**: 2026-01-05
**Target Date**: 2026-01-12 02:00 UTC
**Status**: Planned

---

**Summary**:

**What**: Add `user_email_verified` column to enable email verification feature
**Why**: Reduce spam accounts (BR-034), improve security (BR-089)
**Risk Level**: High (schema change, large table, backward compatibility required)
**Deployment Window**: 2026-01-12 02:00-04:00 UTC (low traffic window)
**Estimated Duration**: 90 minutes (migration + deployment)
**Rollback Estimated Duration**: 60 minutes (reverse migration + code rollback)

---

**Changes Included**:
- [DBT-023]: Add `user_email_verified` column (default FALSE)
- [FEA-145]: Email verification flow (behind feature flag)
- [API-056]: GET /users/:id returns `email_verified` field

**Database Migrations**:
- Add column `user_email_verified BOOLEAN DEFAULT FALSE` to `users` table (10M records)

**Dependencies**:
- Email service (SendGrid) already configured

---

**Migration Strategy** (Multi-Stage for Safety):

**Stage 1** (This deployment - DEP-067):
- Add `user_email_verified` column (default FALSE)
- Old code ignores column (backward compatible)
- New code reads column but doesn't require it

**Stage 2** (Future deployment - DEP-068, 1 week later):
- New code writes to `user_email_verified` column on new signups
- Backfill existing users (mark as verified if > 30 days old)

**Stage 3** (Future deployment - DEP-069, 2 weeks later):
- New code enforces email verification (requires verified=TRUE for actions)
- Feature fully launched

**Rollback**: Each stage backward compatible, safe to rollback

---

**Pre-Deployment Checklist**:

**Code Quality**:
- [x] All tests passing (TEST-067, TEST-068, TEST-069)
- [x] Migration tested in staging (10M test records)
- [x] Backward compatibility verified (old code works with new schema)

**Database**:
- [x] Migration runtime measured in staging (estimated: 45 minutes for 10M records)
- [x] Index performance tested
- [x] Reverse migration tested (can remove column safely)
- [x] Database backup scheduled (1:45 UTC, 15 min before migration)

**Infrastructure**:
- [x] Database CPU/memory headroom confirmed (migration won't overload)
- [x] Replication lag monitored (ensure replicas keep up)

**Communication**:
- [x] On-call team scheduled (2 engineers, 1 DBA)
- [x] Database team on standby
- [x] Stakeholders notified (internal only, no customer impact expected)

**Rollback Plan**:
- [x] Reverse migration script tested (`ALTER TABLE users DROP COLUMN user_email_verified`)
- [x] Code rollback tested (old version works without column)
- [x] Database backup verified (can restore if corruption)

---

**Deployment Steps**:

**Step 1: Pre-Deployment Validation**
1. [x] Database backup completed (1:45 UTC)
2. [x] Baseline metrics recorded:
   - Database CPU: 35%
   - Database connections: 120/200
   - API latency p95: 180ms
3. [x] On-call team confirmed ready

**Success Criteria**: Backup complete, baselines recorded

---

**Step 2: Run Database Migration (Staging-Tested)**
1. [x] Put application in maintenance mode (2:00 UTC)
   - Display "Scheduled maintenance, back in 90 minutes"
2. [x] Run migration:
   ```sql
   ALTER TABLE users ADD COLUMN user_email_verified BOOLEAN DEFAULT FALSE;
   ```
3. [x] Monitor migration progress (estimated: 45 minutes)
4. [x] Verify migration complete:
   ```sql
   SELECT COUNT(*) FROM users WHERE user_email_verified IS NOT NULL;
   -- Expect: 10,000,000 (all users have column)
   ```

**Success Criteria**: Migration completes, all records have column

**Rollback Trigger**: Migration fails, database overloaded (CPU > 90%), replication lag > 10 minutes

**If Triggered**: Rollback migration, extend maintenance window, investigate

---

**Step 3: Deploy Application Code**
1. [x] Deploy v3.2.0 (reads `user_email_verified`, doesn't require it)
2. [x] Verify deployment successful
3. [x] End maintenance mode (3:30 UTC estimated)

**Success Criteria**: Application starts, health checks pass

**Rollback Trigger**: Application fails to start, error rate > 1%

---

**Step 4: Post-Deployment Validation**
1. [x] Run smoke tests:
   - User signup works
   - User login works
   - API returns `email_verified: false` for users
2. [x] Monitor for 30 minutes:
   - Error rate < 0.1%
   - Latency p95 < 200ms (same as baseline)
   - Database CPU < 50% (migration complete, back to normal)

**Success Criteria**: All tests pass, metrics normal

**Rollback Trigger**: Error rate > 0.5%, latency > 500ms, database issues

---

**Step 5: Monitoring Period**
1. [x] Monitor for 24 hours:
   - Database performance (query times, index usage)
   - API latency (ensure column doesn't slow queries)
   - Error rate

**Success Criteria**: No degradation after 24 hours

---

**Rollback Plan**:

**Scenario 1: Migration Fails**
- **Trigger**: Migration doesn't complete, database overloaded
- **Action**:
  1. Stop migration
  2. Restore database from backup (1:45 UTC backup)
  3. Extend maintenance window
  4. Investigate issue
  5. Reschedule deployment
- **Estimated Time**: 60 minutes (restore from backup)

**Scenario 2: Application Fails After Migration**
- **Trigger**: Application won't start, high error rate
- **Action**:
  1. Rollback code to v3.1.0 (old code, ignores new column)
  2. Verify application healthy
  3. Keep column (doesn't hurt, old code ignores it)
  4. Investigate code issue offline
- **Estimated Time**: 15 minutes (code rollback)

**Scenario 3: Performance Issues After Deployment**
- **Trigger**: Latency increased, database slow
- **Action**:
  1. Rollback code to v3.1.0
  2. Run reverse migration (drop column)
  3. Investigate performance issue (missing index?)
  4. Fix and reschedule
- **Estimated Time**: 60 minutes (code rollback + reverse migration)

---

**Communication Plan**:

**Before Deployment**:
- [x] Internal teams: "Scheduled maintenance 2026-01-12 02:00-04:00 UTC"
- [x] Status page: "Scheduled maintenance, application will be unavailable for up to 90 minutes"

**During Deployment**:
- [x] #deployments channel: Updates every 15 minutes
- [x] Status page: "Maintenance in progress, estimated completion 3:30 UTC"

**After Deployment**:
- [x] Status page: "Maintenance complete, all systems operational"
- [x] #deployments channel: "DEP-067 complete, monitoring for 24 hours"

**If Rollback**:
- [x] #incidents channel: "Rolling back DEP-067, reason: [X], ETA: [Y]"
- [x] Status page: "Maintenance extended, investigating issue"

---

**Why This is Good**:

✅ **Multi-stage migration** (backward compatible, safe to rollback at each stage)
✅ **Maintenance window** (acknowledged downtime for high-risk migration)
✅ **Low-traffic window** (2 AM UTC minimizes user impact)
✅ **Backup before migration** (can restore if catastrophic failure)
✅ **Migration tested in staging** (with 10M test records, realistic)
✅ **Multiple rollback scenarios** (migration fails, code fails, performance issues)
✅ **Detailed success criteria** (specific metrics, not vague)
✅ **Communication plan** (status page, internal updates)

---

## Bad Example 1: Vague Deployment Plan

### DEP-999: Deploy New Features (BAD)

**ID**: DEP-999
**Type**: Release
**Environment**: Production
**Strategy**: TBD
**Owner**: Engineering
**Target Date**: ASAP

---

**Summary**:

**What**: Deploy new stuff
**Why**: Need to ship
**Risk Level**: Normal

---

**Changes Included**:
- Some new features
- Bug fixes
- Performance improvements

---

**Deployment Steps**:
1. Deploy code
2. Test it
3. Hope it works

---

**Rollback Plan**: Roll back if it breaks

---

**Why This is Bad**:

❌ **No specific changes** (what features? which bugs?)
❌ **No strategy** (how are we deploying?)
❌ **No risk assessment** (is this breaking? database changes?)
❌ **No success criteria** (how do we know it works?)
❌ **No monitoring** (what metrics to watch?)
❌ **No communication plan** (who do we tell?)
❌ **Vague rollback plan** ("if it breaks" - what triggers rollback?)

**Fix**: Use DEP template, define specific changes, strategy, success criteria, rollback triggers

---

## Bad Example 2: No Rollback Plan

### DEP-888: Payment Processing Refactor (BAD)

**ID**: DEP-888
**Type**: Release
**Environment**: Production
**Strategy**: Big Bang
**Owner**: Backend Team
**Target Date**: 2026-01-15 14:00 UTC

---

**Summary**:

**What**: Refactor payment processing code (5000 lines changed)
**Why**: Technical debt cleanup
**Risk Level**: Medium

---

**Changes Included**:
- Refactored payment service
- New Stripe API integration
- Database schema changes (add `transaction_id` column)

---

**Deployment Steps**:
1. Deploy code to all servers at once
2. Run database migration
3. Monitor for issues

---

**Rollback Plan**: N/A (should be fine, we tested it)

---

**Why This is Bad**:

❌ **Big Bang strategy for high-risk change** (5000 lines, payment processing = revenue risk)
❌ **No rollback plan** ("should be fine" is not a plan)
❌ **Database migration with breaking change** (can't rollback code without reverse migration)
❌ **No gradual rollout** (all users get new payment flow at once)
❌ **Middle of day deployment** (14:00 UTC = peak hours for many regions)
❌ **No success criteria** (what metrics indicate success?)
❌ **No communication to finance/support** (payment changes affect revenue reporting)

**Fix**:
- **Change strategy to Canary or Feature Flag** (gradual rollout for high-risk change)
- **Define rollback plan** (feature flag toggle or reverse migration)
- **Deploy in low-traffic window** (2 AM UTC, not 2 PM)
- **Notify stakeholders** (finance, support, leadership know about payment changes)
- **Test thoroughly** (payment processing = revenue, can't afford bugs)

---

## Bad Example 3: No Monitoring Plan

### DEP-777: API Performance Optimization (BAD)

**ID**: DEP-777
**Type**: Release
**Environment**: Production
**Strategy**: Rolling
**Owner**: API Team
**Target Date**: 2026-01-18 10:00 UTC

---

**Summary**:

**What**: Optimize database queries for API endpoints
**Why**: Reduce latency
**Risk Level**: Low

---

**Changes Included**:
- Added database indexes
- Optimized N+1 queries
- Caching layer for frequent queries

---

**Deployment Steps**:
1. Deploy to 25% of servers
2. Wait 10 minutes
3. Deploy to 50%
4. Wait 10 minutes
5. Deploy to 100%

---

**Monitoring**: Check if it's faster

---

**Rollback Plan**: Rollback if slow

---

**Why This is Bad**:

❌ **No specific success criteria** ("faster" - how much faster? what latency target?)
❌ **No monitoring plan** (which metrics? which dashboard?)
❌ **Fixed wait times** (10 minutes - why? what if issue appears after 15 minutes?)
❌ **Vague rollback trigger** ("if slow" - slower than what?)
❌ **No baseline** (what's current latency? how do we know if it improved?)
❌ **Assumes "optimization" = safe** (optimization bugs can cause worse performance or errors)

**Fix**:
- **Define baseline**: Current p95 latency = 300ms
- **Define success criteria**: p95 latency < 200ms (33% improvement)
- **Define rollback trigger**: p95 latency > 400ms (worse than baseline)
- **Monitoring plan**: Watch API dashboard (MON-012), query performance dashboard (MON-034)
- **Dynamic wait times**: Wait until error rate stable for 15 minutes (not fixed 10 minutes)

---

## Good Pattern Summary

### Deployment Plan Checklist

A good deployment plan (DEP-XXX) has:

- [x] **Specific changes listed** (FEA-XXX, DBT-XXX, API-XXX)
- [x] **Risk level assessed** (Low/Medium/High/Critical)
- [x] **Strategy appropriate for risk** (Low = Rolling, High = Canary/Feature Flag)
- [x] **Deployment window chosen** (Low traffic for high-risk, normal hours for low-risk)
- [x] **Pre-deployment checklist complete** (tests, backups, communication)
- [x] **Success criteria defined** (specific metrics, not vague "works")
- [x] **Rollback triggers defined** (specific conditions: error rate > X%, latency > Yms)
- [x] **Rollback procedure documented** (step-by-step, tested)
- [x] **Monitoring plan** (which dashboards, which alerts, how long)
- [x] **Communication plan** (who to notify, when, what to say)
- [x] **Post-deployment review scheduled** (learn and improve)

---

## Bad Pattern Summary

### Common Deployment Plan Mistakes

Avoid these anti-patterns:

- ❌ **Vague changes** ("bug fixes", "improvements")
- ❌ **No strategy** (or strategy doesn't match risk)
- ❌ **No rollback plan** (or untested rollback)
- ❌ **No success criteria** (how do we know it worked?)
- ❌ **No monitoring** (or vague "check if it's working")
- ❌ **Fixed timelines regardless of metrics** ("wait 10 minutes" instead of "wait until error rate stable")
- ❌ **Deploying during peak hours** (high-risk changes at 2 PM)
- ❌ **No communication** (stakeholders surprised by changes)
- ❌ **Over-confidence** ("should be fine", "we tested it")
- ❌ **No post-deployment review** (don't learn from issues)

---

*Reference: Use these examples when creating deployment plans in `prd-v08-release-planning` skill.*
