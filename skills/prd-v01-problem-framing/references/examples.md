# Problem Statement Examples

Reference file for good and bad problem statement patterns.

## Good Examples

### Digital Signage (Tier 1 Evidence)

**Problem Statement**:
> SMBs with 1-10 display screens face a "sneakernet" problem: updating digital signage requires physically managing USB sticks per screen (15-30 min per update cycle), with no ability to schedule content dynamically or manage screens centrally. Existing solutions price for enterprise scale (100+ screens), creating a gap for SMBs who need simplicity at <$10/screen. [CFD-001]

| Element | Content | Evidence |
|---------|---------|----------|
| Who | SMBs with 1-10 screens (cafes, retail, gyms) | Countable segment |
| Pain | USB management, no scheduling, no centralization | CFD-001 |
| Cost | 15-30 min per update × 3 screens | Quantified time |
| Why now | Streaming devices ($30), post-COVID digital adoption | Market trigger |
| Impossible | Can't run flash promotions or daypart content | Opportunity cost |

**Why it works**: Specific persona, observable behavior, quantified cost, competitive gap, evidence-linked.

---

### Cold Email SaaS (Tier 1-2 Evidence)

**Problem Statement**:
> B2B founders need cold email outreach but face 2-4 week warmup delays before sending a single campaign [CFD-002], pricing that climbs 3x without notice [CFD-001], and feature bloat that overwhelms first-time users [CFD-007]. They're paying $47-147/month for tools they can't use for weeks.

| Element | Content | Evidence |
|---------|---------|----------|
| Who | B2B founders, micro-agencies (1-5 person) | Specific segment |
| Pain | Warmup delays, price creep, complexity | CFD-001, 002, 007 |
| Cost | $47-147/month + 2-4 weeks blocked | Money + time |
| Why now | Competitor bloat, deliverability failures | Market shift |
| Impossible | Can't launch campaigns when needed | Opportunity cost |

**Why it works**: Multi-dimensional pain, specific cost evidence, comparative context.

---

### Compliance Training (Tier 1 Evidence)

**Problem Statement**:
> SMB compliance training: 58% cite manual processes as biggest barrier [CFD-002]; healthcare requires 54 tasks/hire and 15-20 regulatory courses/role [CFD-003]. OSHA violations now reach $165K per incident [CFD-007]. Existing LMS tools are priced for enterprise or lack industry-specific content.

| Element | Content | Evidence |
|---------|---------|----------|
| Who | SMBs in healthcare, construction, insurance | Regulated industries |
| Pain | Manual tracking, volume of requirements | CFD-002, 003 |
| Cost | $165K per OSHA violation | Risk quantified |
| Why now | 2025 penalty increases, new regulations | Regulatory trigger |
| Impossible | Can't prove compliance in <60 seconds | Audit failure |

**Why it works**: Evidence-dense, quantified risk, regulatory urgency.

---

## Bad Examples

### Too Vague

❌ "Small businesses struggle with digital signage."

**Problems**:
- Which businesses? (restaurants? retail? gyms?)
- What struggle? (cost? complexity? time?)
- What's the cost?
- No evidence

✅ **Fix**: "SMBs with 1-10 screens spend 15-30 min per update managing USB sticks [CFD-001]"

---

### Solution Masquerading as Problem

❌ "Users need an AI-powered dashboard."

**Problems**:
- "Need X" is a solution, not a problem
- What can't they do today?
- What decision are they unable to make?
- No evidence of pain

✅ **Fix**: "Managers can't see equipment status across locations, causing 2-hour response delays [CFD-003]"

---

### No Evidence

❌ "We believe restaurant owners would benefit from easier menu updates."

**Problems**:
- "We believe" = Tier 5 speculation
- No CFD-ID
- No quantified cost
- No user voice

✅ **Fix**: Find a restaurant owner quote. "Updating my 3 menu boards takes 45 minutes every time we change prices" [CFD-001]

---

### Missing Cost

❌ "Updating menus is tedious."

**Problems**:
- "Tedious" is subjective
- No time quantification
- No comparison to alternatives
- Can't calculate ROI

✅ **Fix**: "Updating menus takes 45 min/week × $25/hr = $50/week in labor [CFD-001]"

---

### Feature Creep in Problem Statement

❌ "The problem is that our MVP needs to support real-time updates, multi-location sync, and AI-powered scheduling."

**Problems**:
- This is v0.4 (features), not v0.1 (problem)
- Mixing solution with problem
- No user pain articulated
- No evidence

✅ **Fix**: Stay on problem. Features come in v0.3-0.4.

---

## Pattern Summary

**Good problem statements have**:
1. Specific, countable "Who"
2. Observable behavior (not opinions)
3. Quantified cost (time, money, or risk)
4. CFD-ID evidence links
5. "Why now" trigger
6. Opportunity cost (what's impossible)

**Bad problem statements have**:
- Vague segments ("small businesses")
- Solutions disguised as problems ("need X")
- Speculation ("users might want")
- Missing costs ("tedious", "annoying")
- No evidence links
