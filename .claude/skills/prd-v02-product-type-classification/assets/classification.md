# Product Type Classification Worksheet

**Product**: [Product Name]
**Date**: YYYY-MM-DD
**Analyst**: [Name]
**PRD Version**: v0.2

---

## Section 1: Evidence Inventory

Before classifying, list all evidence from v0.2 Competitive Landscape:

### Competitor Evidence
| Competitor | Price Point | Market Position | Key Weakness | Evidence ID |
|------------|-------------|-----------------|--------------|-------------|
| | $ | | | CFD-XXX |
| | $ | | | CFD-XXX |
| | $ | | | CFD-XXX |

### Platform Evidence (if applicable)
| Platform | Your Category Quality | Marketplace? | User Volume | Evidence ID |
|----------|----------------------|--------------|-------------|-------------|
| | Poor/Adequate/Good | Yes/No | | CFD-XXX |

### Price Gap Evidence
| Leader Price | Target Niche | Achievable Price | Gap % | Evidence ID |
|--------------|--------------|------------------|-------|-------------|
| $ | | $ | % | CFD-XXX |

### API/Integration Evidence (if applicable)
| Data Source | API Available? | Documentation Quality | Rate Limits | Evidence ID |
|-------------|---------------|----------------------|-------------|-------------|
| | Yes/No | Poor/Good/Excellent | | CFD-XXX |

---

## Section 2: Decision Tree Walkthrough

Answer each question with evidence:

### Q1: Horizontal Platform Check
**Is there a dominant horizontal platform doing many things?**
- [ ] Yes → Platform: _______________ | Evidence: CFD-XXX
- [ ] No → Skip to Q2

**If Yes: Does it do YOUR thing poorly?**
- [ ] Yes → **UNBUNDLE candidate** | Evidence: CFD-XXX
- [ ] No → Continue to Q2

---

### Q2: Single-Purpose Leader Check
**Is there a single-purpose leader with validated market?**
- [ ] Yes → Leader: _______________ | Revenue evidence: CFD-XXX
- [ ] No → Skip to Q3

**If Yes: Can you price 60%+ lower for a niche?**
- [ ] Yes → **UNDERCUT candidate** | Price math: CFD-XXX
- [ ] No → Continue below

**If No price gap: Can you execute better (speed/UX)?**
- [ ] Yes → **CLONE candidate** | Execution edge: _______________
- [ ] No → Continue to Q3

---

### Q3: Platform Ecosystem Check
**Does target customer live in a platform ecosystem?**
- [ ] Yes → Platform: _______________ | Evidence: CFD-XXX
- [ ] No → Skip to Q4

**If Yes: Does platform have app marketplace?**
- [ ] Yes → **SLICE candidate** | Marketplace URL: _______________
- [ ] No → Continue to Q4

---

### Q4: Integration Gap Check
**Is there a data/API integration gap between tools?**
- [ ] Yes → Tools: _______________ ↔ _______________ | Evidence: CFD-XXX
- [ ] No → Skip to Q5

**If Yes: Is the data accessible (API/scraping)?**
- [ ] Yes → **WRAPPER candidate** | API docs: _______________
- [ ] No → Continue to Q5

---

### Q5: Innovation Check (Last Resort)
**Are existing solutions fundamentally broken?**
- [ ] Yes → What's broken: _______________ | Evidence: CFD-XXX
- [ ] No → **STOP** - Reconsider market or revisit Q1-Q4

**If Yes: Is pain severe enough for education investment?**
- [ ] Yes → **INNOVATION candidate** | Pain severity evidence: CFD-XXX
- [ ] No → **STOP** - Market may not support new entrant

---

## Section 3: Classification Decision

### Primary Type Selected
**Type**: [ ] Clone [ ] Unbundle [ ] Undercut [ ] Slice [ ] Wrapper [ ] Innovation

**Confidence Level**: _____ %

### Evidence Chain
| Question | Answer | Evidence ID | Strength |
|----------|--------|-------------|----------|
| Q__ | | CFD-XXX | Tier 1/2/3 |
| Q__ | | CFD-XXX | Tier 1/2/3 |
| Q__ | | CFD-XXX | Tier 1/2/3 |

### Classification Rationale
Write 2-3 sentences explaining why this type fits:

> _____________________________________________________________________________
> _____________________________________________________________________________
> _____________________________________________________________________________

---

## Section 4: Hybrid Type Check

Sometimes products combine types. Check if applicable:

- [ ] **Clone + Undercut**: Copying model AND significantly cheaper
  - Primary: _______ | Secondary: _______
  
- [ ] **Unbundle + Undercut**: Extracting vertical AND cheaper than platform
  - Primary: _______ | Secondary: _______
  
- [ ] **Slice + Wrapper**: Platform extension AND connecting data
  - Primary: _______ | Secondary: _______

**If Hybrid**: Which type drives GTM constraints?
Primary type for constraints: _______________

---

## Section 5: Anti-Pattern Check

Verify you're not making common mistakes:

- [ ] **Not claiming Innovation when competitor has revenue**
  - Competitors with revenue: _______________ → If any, not Innovation
  
- [ ] **Undercut has price math validated**
  - Leader: $_____ | Target: $_____ | Gap: ____% | Sustainable margin: Yes/No
  
- [ ] **Slice has ecosystem confirmed**
  - Marketplace exists: Yes/No | Apps in category: _____
  
- [ ] **Wrapper has API confirmed**
  - API documented: Yes/No | Rate limits acceptable: Yes/No
  
- [ ] **Unbundle target is large enough**
  - Platform users: _____ | Category volume: _____

---

## Section 6: Output — BR Entries

### BR-XXX: Product Type Classification

```
Type: [Selected Type]
Confidence: [X]%
Primary Evidence: [CFD-XXX, CFD-XXX]
Classification Rationale: [Copy from Section 3]
```

### BR-XXX: GTM Constraints

```
Pricing Constraint: [From gtm-constraints-matrix.md]
- Anchor: [Specific reference]
- Range: [$X - $Y]
- Model: [Subscription/Usage/Seat/Flat]

Channel Constraint: [From gtm-constraints-matrix.md]
- Primary: [Channel]
- Secondary: [Channel]

Scope Constraint: [From gtm-constraints-matrix.md]
- Must Have: [Features]
- Must NOT Have: [Features]

Timeline Constraint: [From gtm-constraints-matrix.md]
- MVP Target: [X days]
```

---

## Section 7: Confidence Gate

### Confidence Assessment

| Factor | Score (1-5) | Notes |
|--------|-------------|-------|
| Evidence quantity | | |
| Evidence quality (Tier 1 vs 3) | | |
| Decision tree clarity | | |
| Anti-pattern check passed | | |
| **Total** | /20 | |

### Proceed Decision

- [ ] **≥17/20 (85%+)**: Proceed to v0.3 immediately
- [ ] **14-16/20 (70-84%)**: Proceed with documented assumptions
- [ ] **10-13/20 (50-69%)**: Gather more evidence before proceeding
- [ ] **<10/20 (<50%)**: Return to v0.2 Competitive Landscape

### If Not Proceeding — Evidence Gaps

List specific evidence needed:
1. _______________________________________________
2. _______________________________________________
3. _______________________________________________

---

## Section 8: Downstream Impact Summary

When proceeding to v0.3, these decisions are now constrained:

| v0.3 Decision | Inherited Constraint | Reference |
|---------------|---------------------|-----------|
| Pricing Model | [From type] | BR-XXX |
| Success Metrics | [From type] | BR-XXX |
| MVP Scope | [From type] | BR-XXX |
| GTM Channel | [From type] | BR-XXX |
| Timeline | [From type] | BR-XXX |

---

**Worksheet Complete**: [ ] Yes

**Ready for v0.3**: [ ] Yes [ ] No — Needs: _______________

**Reviewer Sign-off**: _______________ | Date: _______________
