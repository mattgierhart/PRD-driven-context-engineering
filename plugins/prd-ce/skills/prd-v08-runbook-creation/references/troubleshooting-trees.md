# Troubleshooting Decision Trees

**Purpose**: Structured decision tree patterns for diagnosing common production issues.

---

## How to Use Decision Trees

**Format**:
```
Symptom/Question
├─ [Condition 1] → Action/Next Question
├─ [Condition 2] → Action/Next Question
└─ [Else] → Fallback Action
```

**Guidelines**:
- Start with observable symptoms (alerts, user reports)
- Each branch should be quickly verifiable (< 2 minutes to check)
- Leaf nodes are actions (fix, escalate, investigate further)
- Include rollback as early option for recent changes

---

## Tree 1: High Error Rate

**Starting Symptom**: Error rate spike (> 1% when baseline is < 0.1%)

```
High Error Rate Detected
│
├─ Recent deployment (within 2 hours)?
│  ├─ YES → Correlate error spike with deploy time
│  │         ├─ Timing matches exactly? → ROLLBACK immediately
│  │         └─ Timing doesn't match → Continue to next check
│  └─ NO → Continue to next check
│
├─ Traffic spike (> 2x normal)?
│  ├─ YES → Check infrastructure capacity
│  │         ├─ CPU/Memory > 90%? → SCALE UP (add servers/containers)
│  │         ├─ Database connections exhausted? → INCREASE POOL SIZE
│  │         ├─ Rate limiting not triggered? → ENABLE RATE LIMITING
│  │         └─ Capacity OK → Continue (traffic spike but not capacity issue)
│  └─ NO → Continue to next check
│
├─ External dependency failing?
│  ├─ YES → Check third-party status pages
│  │         ├─ Known outage? → ENABLE FALLBACK/CACHE
│  │         │                  └─ Post update, wait for recovery
│  │         └─ No known issue → ESCALATE to vendor
│  └─ NO → Continue to next check
│
├─ Database issues?
│  ├─ Check database health
│  │   ├─ Deadlocks detected? → Go to Tree 5 (Database Deadlock)
│  │   ├─ Slow queries? → Go to Tree 4 (Slow Database Queries)
│  │   ├─ Connection pool exhausted? → INCREASE POOL, restart connections
│  │   └─ Database unresponsive? → ESCALATE to DBA (P0)
│  └─ Database OK → Continue
│
├─ Specific error pattern in logs?
│  ├─ YES → Group errors by type
│  │         ├─ 500 errors → Check application logs for stack traces
│  │         ├─ 502/503 errors → Load balancer or upstream service issue
│  │         ├─ 504 errors → Timeout issue (slow backend)
│  │         └─ Investigate specific error message
│  └─ NO → Scattered errors (harder to diagnose)
│
└─ UNKNOWN CAUSE
   └─ ESCALATE to senior engineer
      ├─ Start war room (if P0/P1)
      ├─ Capture evidence (logs, metrics, screenshots)
      └─ Continue systematic investigation
```

**Time Estimate**:
- Fast path (rollback): 5-10 minutes
- Medium path (scale/fallback): 10-20 minutes
- Unknown cause: 30+ minutes (requires escalation)

---

## Tree 2: High Latency / Slow Responses

**Starting Symptom**: p95 latency spike (> 2x baseline)

```
High Latency Detected (p95 > threshold)
│
├─ Recent deployment?
│  ├─ YES → Check if latency correlates
│  │         ├─ YES → ROLLBACK deployment
│  │         └─ NO → Continue
│  └─ NO → Continue
│
├─ Which layer is slow? (Use distributed tracing)
│  │
│  ├─ Database layer slow
│  │   ├─ Slow queries? → Go to Tree 4 (Slow Database Queries)
│  │   ├─ Connection pool exhausted? → INCREASE POOL
│  │   ├─ Replication lag? → INVESTIGATE replication (may need to promote replica)
│  │   └─ Lock contention? → KILL long-running transactions
│  │
│  ├─ External API slow
│  │   ├─ Third-party API timeout? → INCREASE TIMEOUT, ENABLE FALLBACK
│  │   ├─ Rate limiting by third-party? → REDUCE REQUEST RATE, CACHE
│  │   └─ Network latency? → CHECK NETWORK ROUTE, escalate to network team
│  │
│  ├─ Application code slow
│  │   ├─ CPU spike? → PROFILE CODE for hot paths
│  │   │              ├─ Inefficient algorithm? → OPTIMIZE or ROLLBACK
│  │   │              └─ Unexpected load? → SCALE UP
│  │   ├─ Memory pressure? → CHECK FOR MEMORY LEAK
│  │   │                     ├─ Leak detected? → RESTART SERVICES (temporary)
│  │   │                     └─ Fix leak and redeploy
│  │   └─ Synchronous blocking? → IDENTIFY blocking call, make async
│  │
│  └─ Load balancer / Network slow
│      ├─ Load balancer overloaded? → SCALE LOAD BALANCER
│      ├─ Network congestion? → ESCALATE to infrastructure team
│      └─ DNS issues? → CHECK DNS RESOLUTION, flush cache
│
└─ No clear bottleneck
   └─ DISTRIBUTED ISSUE (multiple small slowdowns)
      ├─ Check for resource contention (all services slightly slow)
      ├─ Check for cascading failure (one slow service slows others)
      └─ ESCALATE for architectural review
```

**Time Estimate**:
- Fast path (rollback): 5-10 minutes
- Medium path (database/external API): 15-30 minutes
- Application code issue: 30-60 minutes (may require code fix)

---

## Tree 3: Service Unavailable / Down

**Starting Symptom**: Service returning 503 or not responding

```
Service Unavailable
│
├─ Is service process running?
│  ├─ NO → CHECK CRASH LOGS
│  │       ├─ OOM (Out of Memory)? → INCREASE MEMORY LIMIT, restart
│  │       ├─ Crash loop (restarting repeatedly)? → CHECK LOGS for startup error
│  │       │                                        └─ Fix config, rollback, or escalate
│  │       └─ Manually killed? → INVESTIGATE who/why, restart if safe
│  └─ YES → Continue
│
├─ Is service reachable?
│  ├─ Health check failing?
│  │   ├─ Check health check endpoint directly
│  │   │   ├─ Endpoint responds? → Load balancer misconfigured
│  │   │   │                      └─ FIX load balancer config
│  │   │   └─ Endpoint fails? → INVESTIGATE health check logic
│  │   │                        ├─ Database dependency down? → Fix database
│  │   │                        └─ Other dependency? → Fix or remove from health check
│  │   └─ Health check timeout? → INCREASE TIMEOUT or optimize health check
│  │
│  └─ Network issue?
│      ├─ Can't reach from load balancer? → CHECK SECURITY GROUPS / FIREWALL
│      ├─ Can reach but slow? → Go to Tree 2 (High Latency)
│      └─ DNS not resolving? → CHECK DNS RECORDS
│
├─ Is service overwhelmed?
│  ├─ Connection limit reached? → INCREASE CONNECTION LIMIT, SCALE UP
│  ├─ Thread pool exhausted? → INCREASE THREAD POOL, SCALE UP
│  ├─ Request queue full? → SHED LOAD (reject requests), SCALE UP
│  └─ Resource exhaustion? → RESTART SERVICE (temporary), SCALE UP
│
└─ Service running but not responding
   ├─ Deadlock? → RESTART SERVICE
   ├─ Infinite loop? → KILL PROCESS, ROLLBACK deployment
   └─ Unknown → ESCALATE, prepare to restart/rollback
```

**Time Estimate**:
- Fast path (restart service): 2-5 minutes
- Medium path (configuration fix): 10-20 minutes
- Unknown cause: 20+ minutes (requires deeper investigation)

---

## Tree 4: Slow Database Queries

**Starting Symptom**: Database queries taking > 1 second (normally < 100ms)

```
Slow Database Queries
│
├─ Check slow query log
│  ├─ Specific query slow?
│  │   ├─ Missing index?
│  │   │   ├─ YES → ADD INDEX (can do online in most DBs)
│  │   │   │       └─ Monitor query performance improvement
│  │   │   └─ NO → Continue
│  │   │
│  │   ├─ Table scan on large table?
│  │   │   ├─ YES → ADD INDEX or OPTIMIZE QUERY (add WHERE clause)
│  │   │   └─ NO → Continue
│  │   │
│  │   ├─ JOIN too many tables?
│  │   │   ├─ YES → DENORMALIZE or CACHE results
│  │   │   └─ NO → Continue
│  │   │
│  │   └─ Suboptimal query plan?
│  │       └─ REWRITE QUERY or UPDATE STATISTICS
│  │
│  └─ All queries slow (systemic issue)
│      │
│      ├─ Database CPU high (> 90%)?
│      │   ├─ YES → IDENTIFY expensive queries (slow query log)
│      │   │       ├─ Can optimize? → OPTIMIZE or KILL queries
│      │   │       └─ Can't optimize? → SCALE DATABASE (read replica or vertical scale)
│      │   └─ NO → Continue
│      │
│      ├─ Database disk I/O saturated?
│      │   ├─ YES → CHECK for full table scans or missing indexes
│      │   │       └─ UPGRADE to faster disk (SSD, provisioned IOPS)
│      │   └─ NO → Continue
│      │
│      ├─ Connection pool exhausted?
│      │   ├─ YES → INCREASE CONNECTION POOL SIZE
│      │   │       └─ Or KILL long-running queries hogging connections
│      │   └─ NO → Continue
│      │
│      ├─ Replication lag?
│      │   ├─ YES → CHECK replication status
│      │   │       ├─ Lag > 10 seconds? → STOP WRITES to replica, investigate
│      │   │       └─ Replica slow? → May need to scale replica or fix slow query
│      │   └─ NO → Continue
│      │
│      └─ Lock contention?
│          └─ Check for blocking queries → KILL long-running transactions
│             └─ Or go to Tree 5 (Deadlock)
│
└─ Unknown cause
   └─ ESCALATE to DBA
      ├─ Capture EXPLAIN PLAN for slow queries
      ├─ Capture database metrics (CPU, IOPS, connections)
      └─ Consider maintenance window for deeper investigation
```

**Time Estimate**:
- Fast path (add index): 5-15 minutes
- Medium path (kill queries, scale): 15-30 minutes
- Deep investigation: 60+ minutes (may require DBA)

---

## Tree 5: Database Deadlock

**Starting Symptom**: Errors in logs "Deadlock detected" or "Lock wait timeout exceeded"

```
Database Deadlock Detected
│
├─ IMMEDIATE ACTION: Kill long-running transactions
│  └─ Use: SHOW PROCESSLIST (MySQL) or pg_stat_activity (PostgreSQL)
│     └─ KILL [process_id] for transactions holding locks
│
├─ Identify deadlock pattern
│  ├─ Check deadlock log (MySQL: SHOW ENGINE INNODB STATUS)
│  │   └─ Which tables involved?
│  │   └─ Which transactions conflicting?
│  │
│  └─ Analyze transaction order
│      ├─ Transaction A locks Table 1 → Table 2
│      ├─ Transaction B locks Table 2 → Table 1
│      └─ DEADLOCK (circular dependency)
│
├─ Immediate fix (temporary)
│  ├─ Retry failed transactions (application should auto-retry)
│  ├─ Reduce transaction scope (lock fewer rows)
│  └─ Add timeout to prevent infinite wait
│
└─ Permanent fix (requires code change)
   ├─ REORDER TRANSACTIONS (always acquire locks in same order)
   │   └─ Always lock Table 1 → Table 2 (not 2 → 1)
   │
   ├─ REDUCE TRANSACTION SCOPE
   │   └─ Lock only necessary rows (add WHERE clause)
   │
   ├─ DECREASE TRANSACTION DURATION
   │   └─ Commit faster (don't hold locks during external API calls)
   │
   └─ ADD INDEX to reduce lock scope
      └─ Row-level locks instead of table locks
```

**Time Estimate**:
- Immediate mitigation (kill queries): 5 minutes
- Temporary fix (retry logic): 15 minutes
- Permanent fix (code change): Hours to days (requires deployment)

---

## Tree 6: Memory Leak / OOM (Out of Memory)

**Starting Symptom**: Service crashes with OOM error or memory usage steadily increasing

```
Memory Leak / OOM
│
├─ Is this a sudden spike or gradual increase?
│  │
│  ├─ SUDDEN SPIKE
│  │   ├─ Recent deployment? → ROLLBACK
│  │   ├─ Traffic spike? → SCALE UP memory
│  │   ├─ Large object created? → INVESTIGATE code (large file upload, data load)
│  │   │                         └─ INCREASE MEMORY LIMIT or OPTIMIZE code
│  │   └─ Unexpected data volume? → ADD PAGINATION or STREAMING
│  │
│  └─ GRADUAL INCREASE (Memory Leak)
│      │
│      ├─ IMMEDIATE: Restart service (temporary fix)
│      │   └─ Buys time to investigate
│      │
│      ├─ Profile application memory usage
│      │   ├─ Use heap dump / memory profiler
│      │   ├─ Identify objects not being garbage collected
│      │   └─ Find code path holding references
│      │
│      ├─ Common leak patterns
│      │   ├─ Event listeners not removed → REMOVE on cleanup
│      │   ├─ Caches without eviction → ADD TTL or SIZE LIMIT
│      │   ├─ Database connections not closed → FIX connection leaks
│      │   ├─ File handles not closed → USE try-finally or context managers
│      │   └─ Global variables accumulating data → CLEAR periodically
│      │
│      └─ Deploy fix
│         ├─ Test in staging (run for hours, monitor memory)
│         └─ Deploy to production with monitoring
│
└─ If memory leak unfixable immediately
   └─ WORKAROUND: Schedule periodic restarts (every 6-12 hours)
      └─ While working on permanent fix
```

**Time Estimate**:
- Immediate mitigation (restart): 5 minutes
- Identify leak pattern: 30-120 minutes (requires profiling)
- Fix and deploy: Hours to days (depends on leak complexity)

---

## Tree 7: Payment Processing Failure

**Starting Symptom**: Payment transactions failing (critical for revenue)

```
Payment Processing Failure
│
├─ Is payment provider up?
│  ├─ Check status page (e.g., status.stripe.com)
│  │   ├─ Known outage? → POST STATUS UPDATE (external communication)
│  │   │                 └─ ENABLE RETRY QUEUE (process when provider recovers)
│  │   │                 └─ NOTIFY support team (expect customer inquiries)
│  │   └─ No known issue → Continue
│  │
│  └─ Test API directly (simple API call)
│      ├─ API responds normally? → Issue is in our integration
│      └─ API fails? → ESCALATE to payment provider support
│
├─ Is it all payments or specific patterns?
│  │
│  ├─ ALL PAYMENTS FAILING
│  │   ├─ API credentials invalid? → CHECK API keys (rotation? expiration?)
│  │   ├─ IP allowlist blocking us? → VERIFY IP allowlist with provider
│  │   ├─ Rate limiting? → CHECK rate limit headers, REDUCE REQUEST RATE
│  │   └─ Code bug? → Recent deploy? → ROLLBACK
│  │
│  └─ SPECIFIC PATTERNS FAILING
│      ├─ Specific payment method (credit card, bank transfer, etc.)?
│      │   └─ CHECK provider documentation for method-specific requirements
│      │
│      ├─ Specific amount range?
│      │   ├─ Very small amounts? → CHECK minimum transaction amount
│      │   └─ Very large amounts? → CHECK transaction limit
│      │
│      ├─ Specific currency?
│      │   └─ CHECK supported currencies, currency conversion
│      │
│      └─ Specific customer segment (country, account type)?
│          └─ CHECK regional restrictions, compliance requirements
│
├─ Check our payment processing pipeline
│  ├─ Database writes failing? → Transactions created but not saved
│  │   └─ Go to Tree 4 (Database Issues)
│  │
│  ├─ Idempotency key collision? → Duplicate transaction detection
│  │   └─ CHECK idempotency key generation logic
│  │
│  └─ Webhook processing failing? → Payment succeeded but webhook missed
│      ├─ CHECK webhook endpoint health
│      └─ CHECK webhook signature validation
│
└─ ESCALATION (Payment issues are P0)
   ├─ Notify leadership immediately (revenue impact)
   ├─ Notify finance team (for reconciliation)
   ├─ Notify support team (customer communication)
   └─ Post-mortem required regardless of resolution time
```

**Time Estimate**:
- Provider outage: 5-10 minutes (enable retry queue, communicate)
- Configuration issue: 10-20 minutes (fix API keys, settings)
- Code bug: 5-15 minutes (rollback)
- Complex integration issue: 30+ minutes (requires debugging)

---

## Tree 8: Authentication / Login Failure

**Starting Symptom**: Users can't log in

```
Authentication Failure
│
├─ All users affected or specific users?
│  │
│  ├─ ALL USERS (P0 - Critical)
│  │   ├─ Authentication service down? → CHECK service health
│  │   │   └─ Go to Tree 3 (Service Unavailable)
│  │   │
│  │   ├─ Database down? → User credentials can't be verified
│  │   │   └─ ESCALATE to DBA (P0)
│  │   │
│  │   ├─ Session store down (Redis, Memcached)? → Sessions can't be created
│  │   │   └─ RESTART session store or FAILOVER to backup
│  │   │
│  │   ├─ JWT secret rotated incorrectly? → Old tokens invalid
│  │   │   └─ ROLLBACK secret rotation or SUPPORT dual secrets
│  │   │
│  │   └─ Recent deployment? → ROLLBACK
│  │
│  └─ SPECIFIC USERS (P1/P2)
│      │
│      ├─ Password reset not working?
│      │   ├─ Email service down? → CHECK email provider status
│      │   └─ Reset token expired? → EXTEND expiration or resend
│      │
│      ├─ MFA / 2FA not working?
│      │   ├─ SMS not delivered? → CHECK SMS provider
│      │   ├─ Authenticator app codes rejected? → CHECK time sync
│      │   └─ Backup codes not working? → VERIFY backup code logic
│      │
│      ├─ Social login (OAuth) not working?
│      │   ├─ Provider down (Google, Facebook)? → CHECK provider status
│      │   ├─ OAuth redirect misconfigured? → VERIFY redirect URI
│      │   └─ OAuth token exchange failing? → CHECK API credentials
│      │
│      └─ Account locked?
│          └─ CHECK account status, UNLOCK if legitimate user
│
└─ COMMUNICATION CRITICAL
   ├─ Can't log in = users very frustrated
   ├─ Post status page update immediately
   └─ Provide ETA or workaround if possible
```

**Time Estimate**:
- Service down: 5-15 minutes (restart, rollback)
- Configuration issue: 10-30 minutes
- Provider outage: Wait for provider (communicate clearly)

---

## Tree 9: Data Inconsistency / Corruption

**Starting Symptom**: Data doesn't match expectations (reports wrong, user data incorrect)

```
Data Inconsistency Detected
│
├─ STOP THE BLEEDING (prevent further corruption)
│  ├─ Recent migration or data update? → PAUSE migration immediately
│  ├─ Buggy code writing bad data? → ROLLBACK deployment or DISABLE feature
│  └─ Manual data operation? → STOP operation, assess damage
│
├─ Assess scope of corruption
│  ├─ How many records affected?
│  │   ├─ Sample records → QUERY database for pattern
│  │   └─ Count affected → Use COUNT query with corruption criteria
│  │
│  ├─ When did corruption start?
│  │   ├─ Check created_at/updated_at timestamps
│  │   └─ Correlate with deployment or operation time
│  │
│  └─ Is data recoverable?
│      ├─ Recent backup available? → NOTE backup timestamp
│      ├─ Soft deletes (data still in DB)? → Can restore from deleted records
│      └─ Audit log available? → Can reconstruct from history
│
├─ Prevent further damage
│  ├─ Put affected feature in READ-ONLY mode
│  ├─ Or disable feature entirely (feature flag)
│  └─ Communicate to users (if customer-facing data affected)
│
├─ Recovery strategy
│  │
│  ├─ FEW RECORDS AFFECTED (< 100)
│  │   └─ Manual fix (SQL UPDATE statements)
│  │      ├─ TEST fix on staging first
│  │      ├─ Run in transaction (can rollback)
│  │      └─ Verify fix before committing
│  │
│  ├─ MANY RECORDS AFFECTED (100-10,000)
│  │   └─ Write data migration script
│  │      ├─ TEST on staging with production-like data
│  │      ├─ DRY RUN on production (log what would change)
│  │      ├─ BACKUP database before running
│  │      ├─ RUN migration
│  │      └─ VERIFY fix (sample records)
│  │
│  └─ MASSIVE CORRUPTION (> 10,000 or complex)
│      └─ Restore from backup
│         ├─ Calculate data loss window (last backup to corruption start)
│         ├─ Communicate downtime and data loss to users
│         ├─ RESTORE from backup to separate instance
│         ├─ VERIFY restored data
│         ├─ REPLAY changes if possible (from audit log)
│         └─ CUTOVER to restored database
│
└─ Post-recovery
   ├─ Add validation to prevent recurrence
   ├─ Add monitoring to detect corruption earlier
   ├─ Post-mortem required (data corruption = serious)
   └─ Consider legal/compliance implications (if customer data)
```

**Time Estimate**:
- Stop bleeding: 5-15 minutes (rollback, disable)
- Small fix: 30-60 minutes (manual SQL)
- Large fix: 2-4 hours (migration script)
- Restore from backup: 4-12 hours (depends on database size)

---

## Creating Custom Decision Trees

**When to Create**:
- After handling same incident type 3+ times
- Complex issue with multiple investigation paths
- New team members frequently ask "what do I check?"

**Structure**:
1. **Start with observable symptom** (what alert fired, what users reported)
2. **Branch on quickly verifiable conditions** (< 2 min to check each)
3. **Include rollback as early option** (fast mitigation for recent changes)
4. **Leaf nodes are actions** (fix, escalate, investigate)
5. **Include time estimates** (sets expectations)

**Test Your Tree**:
- Walk through with team
- Simulate incident in staging, follow tree
- Update based on what was unclear or missing

---

*Reference: Use these decision trees when creating RUN-XXX runbooks in `prd-v08-runbook-creation` skill.*
