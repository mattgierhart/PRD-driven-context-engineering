# User Journey Mapping Examples

## Good Example: Core Journey with Full Traceability

```
UJ-001: First Report Generation
Persona: PER-001 (Overwhelmed Ops Manager)
Type: Core
Trigger: User completes onboarding and sees empty dashboard prompt
Goal: Generate first automated report to prove time-saving value

Steps:
  1. Click "Create Report" button → FEA-003 (one-click reports)
  2. Select connected data source → FEA-001 (auto-sync)
  3. Choose from 5 template options → FEA-008 (templates)
  4. Preview report with actual data → FEA-003
  5. Click "Export PDF" → FEA-009 (export)

Pain Points:
  - Step 2: User may not have connected data yet (dependency on UJ-002)
  - Step 3: Decision paralysis if >5 templates shown

Moment of Value: Seeing completed report with their real data (not sample)
KPI Link: KPI-002 (activation rate)
Success Metric: Time from click to export ≤ 5 minutes; 70% Day-1 completion
Dependencies: UJ-002 (data source must be connected), BR-015 (data format rules)
```

**Why it's good:**
- Specific trigger ("sees empty dashboard prompt" not "opens app")
- Every step links to FEA-
- Pain points identified with mitigation hints
- Clear, measurable success metric
- Dependencies documented

---

## Good Example: Onboarding Journey

```
UJ-000: New User Onboarding
Persona: PER-001 (Overwhelmed Ops Manager)
Type: Onboarding
Trigger: User clicks "Sign Up" from landing page
Goal: Get to first value moment (seeing dashboard) in <3 minutes

Steps:
  1. Enter email + password → FEA-010 (auth)
  2. Verify email (click link) → FEA-010
  3. Complete 3-question profile → FEA-011 (personalization)
  4. Connect primary data source → FEA-001 (auto-sync)
  5. See personalized dashboard → FEA-007 (dashboard)

Pain Points:
  - Step 2: Email verification friction (consider magic link)
  - Step 4: OAuth complexity if source requires it

Moment of Value: Seeing dashboard populated with their actual data
KPI Link: KPI-001 (Time to First Value)
Success Metric: Signup → dashboard in ≤ 3 minutes; 60% complete Day 1
Dependencies: None (gates all other journeys)
```

---

## Bad Example: Feature-First Journey

```
UJ-001: Using the Product
Persona: Users
Type: Core
Trigger: Opens app
Goal: Use features

Steps:
  1. Use FEA-001
  2. Use FEA-002
  3. Use FEA-003
  4. Use FEA-004
  5. Use FEA-005

Pain Points: None identified

Moment of Value: Done using features
KPI Link: Engagement
```

**Why it's bad:**
- No specific persona
- "Opens app" is not a trigger
- Steps are features, not user actions
- No pain points = no UX insight
- "Engagement" is not a KPI- reference
- No success metric

---

## Bad Example: Mega-Journey

```
UJ-001: Complete User Flow
Steps:
  1. Sign up
  2. Verify email
  3. Complete profile
  4. Connect data source
  5. Create first report
  6. Share report
  7. Invite team member
  8. Set up automation
  9. Configure notifications
  10. Create dashboard
  11. Export data
  12. Set up integration
  13. Create second report
  14. Upgrade to paid
  15. Add payment method
```

**Why it's bad:**
- 15 steps = too many contexts
- Combines onboarding + core + expansion + purchase
- Impossible to design a screen flow for this

**Fix:** Split into:
- UJ-000: Onboarding (steps 1-4)
- UJ-001: First Report (steps 5-6)
- UJ-002: Team Expansion (step 7)
- UJ-003: Automation Setup (step 8-9)
- UJ-004: Upgrade Flow (steps 14-15)

---

## Recovery Journey Example

```
UJ-010: Password Reset
Persona: PER-001 (any persona)
Type: Recovery
Trigger: User clicks "Forgot Password" on login screen
Goal: Regain account access without support ticket

Steps:
  1. Enter email address → FEA-010 (auth)
  2. Receive reset email → FEA-010
  3. Click reset link → FEA-010
  4. Enter new password → FEA-010
  5. Auto-login to dashboard → FEA-010

Pain Points:
  - Step 2: Email may go to spam
  - Step 3: Link expiration confusion (15-min window)

Moment of Value: Successful login with new password
KPI Link: N/A (recovery, not growth)
Success Metric: Reset completion in <2 minutes; <5% support tickets for access
Dependencies: None
```
