---
title: "Visual Expression of the Eight Key Moments — Design-Research Report"
status: "Research input (PRD.md authority order, item 7) — commissioned by the owner, received 2026-08-13"
provenance: "Produced by an external deep-research agent from the key-moments canon artifact and the visual-expression research prompt (session prd-ce-v2, 2026-08-13). Vendored verbatim; consumed by docs/v2/V2_KEY_MOMENTS.md (v1.2: per-moment Visual expression blocks, §§2.1–2.3, §4)."
---

# Visual Expression of Eight Key Moments — A Design-Research Report

## TL;DR
- **Each moment has a native genre that experienced PMs already recognize, and the design job is to pick the genre that matches the moment's clarity anchor rather than the most impressive form:** Problem Framing → an evidence-footnoted sentence; Persona → behavioral cards (+ a negative persona); Commercial Model → a "how it lives in the customer's world" strip with pricing demoted to one clause; User Journeys → a journey map with an emotional-temperature band on a story-map backbone; Tech & Risk → an invest-vs-optimize map over a *sortable, quantified* risk register (**not** a 5×5 heat map); Build Sequencing → a pre-computed dependency DAG with a beta line; Go to Market → a launch one-pager with a coherence/reconciliation table; Launch Verdict → a target-vs-actual scorecard of bullet graphs with a grade and verdict.
- **Two established genres are wrong for this system and are departed from with argument:** the 5×5 risk heat map (mathematically discredited by Cox 2008 and Hubbard — replaced by a sortable register plus a tornado ranking) and the date-based Gantt roadmap (replaced for Build Sequencing by a dependency DAG; any GTM timeline kept in Now/Next/Later confidence horizons).
- **The eight pages become one family** through a shared, single-file-buildable system: a provenance chip (typed ID + evidence tier + confidence, borrowing GRADE/IPCC/C2PA), a "data as of" staleness stamp with a build fingerprint, loop-verb-only vocabulary, and sign-off ceremonies that read with weight (reserved color, literal-verb buttons, signer attribution, timestamp) drawn from DocuSign and GitHub PR review.

---

## Key Findings

**1. Every moment has a recognized native genre; match it to the clarity anchor.** Where the anchor is a *sentence* (M1, M3), the page should be an annotated sentence, not a dashboard. Where it is a *decision among typed options* (M3, M5), a side-by-side comparison. Where it is a *sequence* (M4, M6), a left-to-right map. Where it is a *reckoning* (M8), a scorecard that terminates in a verdict.

**2. Two genres are actively harmful.** Louis Anthony (Tony) Cox Jr., in "What's Wrong with Risk Matrices?" (*Risk Analysis* vol. 28, no. 2, 2008, pp. 497–512, doi:10.1111/j.1539-6924.2008.01030.x), lists as the first defect: "(a) Poor Resolution. Typical risk matrices can correctly and unambiguously compare only a small fraction (e.g., less than 10%) of randomly selected pairs of hazards," and "(b) Errors. Risk matrices can mistakenly assign higher qualitative ratings to quantitatively smaller risks." Douglas Hubbard titles his chapter on them "Worse Than Useless." For M5 we recommend a sortable register with quantified exposure and a tornado ranking. The date-based Gantt is a false-precision trap (Bastow/ProdPad; Cagan); for M6 the ordering rationale belongs in a dependency DAG, not a timeline.

**3. Judgment affordances have a documented visual grammar.** Acknowledgement ("I have seen/accept this") and decision ("I choose A over B") are different interactions — Material Design's confirmation-vs-acknowledgement guidance codifies the split, and Carbon reserves full ceremony for consequential/irreversible actions. Comparison tables serve decisions among fewer than 5–7 options because people then do "compensatory decision making" (NN/g). Sign-off ceremonies earn weight through a reserved signal color, literal-verb commitment buttons (never "OK"), staged friction, signer attribution, and immutable timestamps (DocuSign "Adopt and Sign / Agree and Finish"; GitHub PR "Approve / Request changes"; stage-gate go/hold/kill).

**4. Provenance can be shown without clutter by borrowing calibrated-language conventions from science.** GRADE rates a body of evidence high/moderate/low/very low; the IPCC AR5 Guidance Note (Mastrandrea et al., 2010) states "A level of confidence is expressed using five qualifiers 'very low,' 'low,' 'medium,' 'high,' and 'very high,'" and instructs authors to "lead with what you know"; C2PA Content Credentials use a small clickable badge that opens the full provenance chain. Together these give a proven, low-ink pattern: a compact chip that expands on demand.

**5. All expensive layout must be pre-computed in the pull script.** The single-file/no-library constraint rules out force-directed graphs and charting libraries. The substitute is Sugiyama-style layered layout (the standard for DAGs, used by Graphviz `dot`: layer assignment → crossing minimization → coordinate assignment) computed deterministically in the pull script and shipped as x/y coordinates in the JSON; the template only draws inline SVG paths.

---

## Details

Internal system vocabulary (planes, pack names, "Evidence/Intent/Reality plane") is used only in this analysis and marked **[non-UI]**. All recommended on-page copy uses only loop verbs (Explore, Shape, Decide, Build, Learn, Check) and ordinary PM language.

A shared provenance convention referenced by every moment: a **provenance chip** = `‹typed-ID›` + evidence-tier dot + confidence label. Evidence tiers borrow GRADE's four-level ladder (the canon already has tiers with a tier-5 reject); confidence borrows the IPCC's five qualifiers. Default render is the ID chip only; hover/click reveals tier + confidence + source, mirroring C2PA's "click the badge to inspect the full provenance chain."

---

### M1 · Problem Framing

**Clarity anchor:** the one-sentence spark formula — *[Who] faces [pain] costing [amount] because [root cause]; [trigger] creates urgency; current solutions [gap]* — every clause citing evidence.

**Recommended primary genre: the annotated / evidence-footnoted sentence** (close-reading / Genius-style annotation + legal redline conventions). **Alternate: the five-element problem table** (incl. "What's impossible" / "Why now").

**Departure flag (argued):** The established genre for problem framing in most tools is a canvas (Lean Canvas box, or a problem-statement card). I argue against defaulting to a canvas. The canon says the clarity anchor is *one sentence where every clause cites evidence*. A canvas scatters attention across boxes; it does not make the *sentence* the hero and cannot show clause-level provenance. The right artifact is the sentence itself, rendered large, with each clause as an interactive span that reveals its supporting evidence — exactly the affordance Genius annotations and marked-up legal contracts provide. This is a justified departure: the visual proposition *is* the charter ("clarity of what problem we are trying to solve").

**Named exemplars:**
- **Genius / close-reading annotation** — highlighted spans open a side panel of evidence. *Steal:* the "click a clause → see the citation" interaction, so the sentence stays clean but every claim is one tap from its proof.
- **Amazon PR/FAQ working-backwards** (Bryar & Carr, *Working Backwards*) — forces the problem/benefit into plain customer language before anything is built; "iterating on a press release is a lot less expensive than iterating on the product itself." *Steal:* the discipline that a claim which can't be written compellingly gets rejected — mirrors the canon's tier-5 reject and gap gate.
- **GRADE evidence grading** (BMJ / *J Clin Epidemiol*) — a body of evidence is rated high/moderate/low/very low. *Steal:* the tier ladder for each clause's citation, shown as a small dot, not prose.
- **IPCC calibrated language** — five confidence qualifiers, "lead with what you know." *Steal:* the register — state the confident clauses plainly, mark the weak ones honestly rather than hiding them.

**Information hierarchy:** *Hero:* the assembled spark sentence, set large, each clause an evidence-linked span. *Support:* the ranked pain list and five-element table below. *Detail-on-demand:* per-clause evidence cards (tier, source, upgrade condition).

**Judgment affordances (Review-dominant):** The human validates the "who," ranks the pains (drag-rank), rejects speculation (a clause flagged tier-5 reads struck-through, redline-style), and **accepts the statement**. Acceptance is a *decision* sign-off, not a checkbox: a literal-verb button ("Accept problem statement") in a reserved color, capturing signer + timestamp. Empty state is a *draft* sentence with clauses marked "needs evidence."

**Data binding:** `Tiered evidence` → clause evidence cards and the tier dot on each span; `problem-statement draft` → the hero clause slots; `upgrade conditions` → the "what would raise this tier" line inside each card. **Computed:** the gap gate / testability status (spark-exit checks **[non-UI]**) renders as a readiness strip. **Slots/states:** each clause iterates over its `evidence[]`; at n=0 evidence for a clause it renders in a "needs Explore" state (amber, not red — it's a gap, not an error); at n=1 a single citation; the sentence template is fixed (six clauses); overflow is per-clause evidence collapsed to "top source + N more."

**Emotional register:** Quietly authoritative — the thesis of the whole product; confident where evidence is strong, visibly hedged where it is not (IPCC discipline). Not dramatic, not plain — *weighted*.

**Anti-patterns:** (1) Fill-in-the-blank Mad Libs that read as bureaucratic rather than a claim. (2) Hiding weak evidence — the page must show the tier-5/gap honestly. (3) Letting the five-element table upstage the sentence.

```
┌───────────────────────────────────────────────────────────┐
│ PROBLEM FRAMING                        data as of · ⟲ fresh │
│                                                             │
│  [Who]¹ faces [pain]² costing [amount]³                     │
│  because [root cause]⁴; [trigger]⁵ creates urgency;         │
│  current solutions [gap]⁶.                                  │
│   └ click any clause → evidence card (tier ● confidence)    │
│                                                             │
│  Ranked pains:  ▓▓▓ 1  ▓▓ 2  ▓ 3   (drag to re-rank)        │
│  Five-element table ▸ (What's impossible / Why now)         │
│                                                             │
│           [ Accept problem statement ]  ← signer · time     │
└───────────────────────────────────────────────────────────┘
```

---

### M2 · Persona

**Clarity anchor:** the persona card — behavioral, evidence-linked, pains ranked — plus the **negative persona**.

**Recommended primary genre: the behavioral persona card set** (Cooper/Goodwin goal-directed personas). **Alternate: a behavioral-segment matrix** (segments × behavioral attributes) for the Intake path; JTBD framing is a lens layered on the card, not a replacement.

**Reasoning:** Goodwin's method (per *Designing for the Digital Age*) builds personas from goals and behaviors, not demographics. As Cooper's goal-directed method puts it: "Unlike user segments, personas don't rely heavily on demographics or purchasing trends to define users. Instead, they identify patterns in people's behavior—focusing on the purpose a product should serve based on user needs." The canon demands behavioral, evidence-linked cards with ranked pains — the card genre exactly. The **negative persona** is the distinctive requirement and has no equivalent in the segment-matrix genre, so the card set wins.

**Competing-genre trade-off (card set vs behavioral-segment matrix vs JTBD):** The matrix scales better at many segments and is better for *comparison*; the card set is better for *empathy and evidence-linking* and is what PMs recognize as "a persona." Since the anchor is the card (with the negative persona) and the cap is ≤5, the card set is correct; the matrix is the alternate/Intake authoring view. JTBD ("when I…, I want to…, so I can…") is best as a field *on* the card, reconciling the Gothelf/Cooper debate rather than picking a side.

**Named exemplars:**
- **Cooper/Goodwin goal-directed persona** — end goals + experience goals, 3–4 memorable goals each; "roles defined by tasks, not titles." *Steal:* goals-over-demographics structure. (The same source notes Notion's three user segments each drive a different onboarding — feeding M7.)
- **Indi Young mental-model / behavioral segments** — segmentation by behavior/thinking. *Steal:* evidence-linked behavioral claims rather than invented biography.
- **Rob Fitzpatrick, *The Mom Test* (confidence ladder)** — distinguishes real evidence from compliments. *Steal:* a confidence indicator on each behavioral claim (observed behavior vs flattering interview).

**Information hierarchy:** *Hero:* the ≤5 persona cards in a row, each with name, one behavioral sentence, ranked pains. *Support:* the **negative persona** card, styled as a muted "not for" boundary. *Detail-on-demand:* interview record IDs, segment signals, confidence per claim.

**Judgment affordances (Review + Intake):** Review — the human **ranks/merges** candidates (drag to merge; cap enforced at 5) and **confirms behavioral claims against evidence** (accept/reject toggle per claim). Intake — founder-known segments authored via a guided card. Terminal *decision*: accepting the set incl. the negative persona; sign-off captures who accepted. Merging is the signature interaction — it should feel like consolidating, with a visible count against the 5-max cap.

**Data binding:** `Interview records` → evidence chips on each claim; `persona candidates + evidence links` → the cards; the negative persona emits as a boundary statement **[non-UI]**. **Computed:** the evidence-requirements matrix and 5-max cap (experience-coverage **[non-UI]**) render as a "3 of 5 personas · all claims evidenced" strip. **Slots/states:** cards iterate over `personas[]`; n=0 → "no personas yet, start from interviews or add a founder-known segment"; n=1 → single card, still shows the negative-persona slot; n>5 → cap warning forces merge/cut; a claim with missing evidence renders "unverified" (amber) and blocks accept.

**Emotional register:** Warm but disciplined — real humans, every warm detail earning its place with evidence. The negative persona reads deliberately cool/subtractive — a line drawn.

**Anti-patterns:** (1) Demographic stock-photo personas with no behavioral spine (the classic Cooper/Goodwin failure). (2) Too many personas — the cap exists because focus is the value. (3) Omitting or burying the negative persona, the sharpest decision on the page.

---

### M3 · Commercial Model

**Clarity anchor:** the **engagement-model statement** — how the product lives in the customer's world (frequency of use, ecosystem it plugs into, what it replaces and what the switch costs) — plus the type and the price. The owner is explicit: *the engagement model is the sentence; pricing is a clause.*

**Recommended primary genre: an engagement-model statement with a "day/week-in-the-life" frequency strip + ecosystem/context diagram + switching-cost bar, with product-type options compared side by side.** **Alternate: a type-comparison decision matrix** (types × guardrails/evidence).

**Departure flag (argued, and the owner pre-authorizes it):** Most commercial-model templates (pricing pages, business-model canvas) over-weight *pricing*. The canon says pricing is one clause. I recommend **demoting the pricing table** from hero to a single locked clause, and promoting three under-served visuals to the hero zone: (a) a **frequency strip** (daily/weekly/occasional use, a "day-in-the-life" band); (b) an **ecosystem/context diagram** (what it plugs into); (c) a **switching-cost / behavioral-inertia bar** ("your real competitor is a spreadsheet"). This directly serves the charter's own words.

**Named exemplars:**
- **April Dunford, *Obviously Awesome*** — five components incl. competitive alternatives ("often Excel"). *Steal:* name the real alternative honestly (spreadsheet/DIY), which is exactly the switching-cost hero.
- **Geoffrey Moore positioning statement** (*Crossing the Chasm*) — "For [target] who [need], the [product] is a [category] that [benefit]. Unlike [alternative]…" *Steal:* the sentence-with-a-clause structure; the engagement statement can rhyme with this so PMs recognize it.
- **NN/g comparison tables** — columns = options, rows = attributes; best for compensatory decisions under 5–7 options. *Steal:* the side-by-side type comparison with only differing attributes shown; a single "recommended" column highlighted.
- **Pricing-table "recommended column" convention** (NN/g "explicit differences"; UX Planet) — highlight exactly one option with contrast + a "recommended/best value" label; "communicate differences, not similarities." *Steal:* the single-highlight discipline for the type choice — and deliberately *not* applying that visual energy to price.

**Information hierarchy:** *Hero:* the engagement sentence + frequency strip + ecosystem diagram + switching-cost bar. *Support:* the type choice as a comparison with guardrail previews; the price as a single clause with a "locked behind WTP gate" state. *Detail-on-demand:* competitive records, quantified switching-cost inventory, WTP signals, SMB-penalty calc.

**Judgment affordances (Review-dominant):** Types compared side by side with evidence and guardrail previews. Terminal *decision*: the product-type + engagement-model adjudication **[non-UI: emitted as a Change record]**. Pricing is a **gated decision**: the price clause is visibly *locked* until the WTP gate clears — a padlock affordance that becomes editable/acceptable only when evidence exists (making "wtp-before-price-lock" **[non-UI]** legible without naming it). Sign-off captures type + engagement statement + KPI targets.

**Data binding:** `type candidates + guardrail previews` → the comparison columns; `switching-cost inventory` → the switching-cost bar (length = quantified switch cost); `WTP signals` → the price-clause lock state; `competitive records` → the ecosystem diagram nodes and the named alternative. **Computed:** SMB-penalty and guardrail inheritance render as annotations. **Slots/states:** type comparison iterates over `types[]` (six-type taxonomy); n=1 type → no comparison, just the statement; frequency strip needs a `frequency` field — if missing, "usage frequency: unknown (Explore)"; switching-cost bar at n=0 → "not yet quantified"; price clause with no WTP evidence → locked.

**Emotional register:** Confident and concrete — a strategic claim about how the product *lives*. The switching-cost bar can carry mild drama (the honest reckoning with inertia). The price clause reads deliberately understated to enforce "pricing is a clause."

**Anti-patterns:** (1) Pricing table as hero (the exact failure the owner calls out). (2) A decorative ecosystem cloud with no named systems. (3) Comparing types on attributes that are all the same — NN/g: highlight only what differs, or the comparison misleads.

---

### M4 · User Journeys

**Clarity anchor:** the **journey map with emotional temperature** — missions → steps → screens, delight and deliberately-utilitarian stretches marked as design decisions, the "money shot" named. The delight-vs-utilitarian axis rhymes with an internal surface-mode pattern (Persuade vs Operate) **[non-UI]**.

**Recommended primary genre: a journey map with an emotional-temperature band** (Kalbach alignment diagram + NN/g emotional curve), on a story-map backbone. **Alternate: a service blueprint** (Shostack line-of-visibility).

**Competing-genre trade-off (classic journey map vs service blueprint vs story map):** All three are alignment diagrams (Kalbach). The **classic journey map** foregrounds emotion — exactly the clarity anchor — so it is primary. The **story map** (Patton: backbone of activities across the top, stories hanging below, the "walking skeleton" as first end-to-end slice) is the better *structure* for missions→steps→screens and scope-slicing, so we borrow its backbone. The **service blueprint** adds the line of visibility and back-stage processes — richer than needed for the delight axis, better for M5/M7 operational readiness; offer as the alternate. Recommendation: journey-map emotion band *on* a story-map backbone.

**Contradiction surfaced (per instruction):** The canon's species mix says M4 is **both** Intake (the journey builder) and Review (coverage/scope sign-off). That implies **two surfaces, not one**. Naming it honestly: I recommend one template with **two explicit modes** (a "build" mode and a "decide" mode) sharing one data model and layout, rather than pretending a single static view serves both. If forced to one, the Review/decide view is the money-shot moment and should win, with authoring as an inline editing affordance.

**Named exemplars:**
- **Jim Kalbach, *Mapping Experiences*** — alignment diagrams; emotion as a contextual layer. *Steal:* the emotion band as a first-class row.
- **Jeff Patton, *User Story Mapping*** — backbone + walking skeleton; a flat backlog is "a bag of context-free mulch." *Steal:* the backbone (missions) with stories/screens below, and horizontal slices as scope cuts.
- **NN/g journey mapping** — emotion plotted as a single line of ups and downs; label assumptions vs evidence. *Steal:* the curve and the discipline of marking assumption-based emotion as hypothesis.
- **Money-shot / hero-screen convention** — the one screen that sells the product, named on the map. *Steal:* an explicit money-shot marker so the team agrees which screen must be exceptional.

**Information hierarchy:** *Hero:* the map — missions (backbone) → steps → screens, with the emotional-temperature band beneath and the money-shot screen elevated. *Support:* the recognizable-feature cut (parity/delta) and delight-vs-utilitarian markings. *Detail-on-demand:* per-screen records, coverage-matrix cells, dead-end warnings.

**Judgment affordances (both):** Intake — build the journey; mark each stretch delight ▲ or utilitarian ▬ as a *decision* (a labeled tag), not a mood. Review — the coverage + scope sign-off (the money shot): accept scope against the <15-screen cap and confirm coverage. Sign-off captures scope acceptance.

**Data binding:** `Features` → feature-parity/delta chips on screens; `journey/screen drafts` → backbone/steps/screens; emotion value per step → the temperature band height/color (dual-encode: height + label, never color alone). **Computed:** the feature↔journey↔screen coverage matrices, dead-end check, screen caps (experience-coverage **[non-UI]**) — the matrix is a computed CSS-grid; dead-ends render as flagged steps. **Slots/states:** backbone iterates over `missions[]`, each over `steps[]`, each over `screens[]`; n=0 → "no missions yet (Shape)"; a mission with 0 screens → dead-end flag; >15 screens → cap-breach warning that blocks scope sign-off; missing emotion value → band shows an "unmarked" gap.

**Emotional register:** The page *allowed* warmth and drama — the emotional band is the point. Delight moments can glow; utilitarian stretches read calm by design (Persuade vs Operate **[non-UI]**). The money shot is the emotional peak of the whole document.

**Anti-patterns:** (1) The journey map as **wallpaper** — beautiful, wall-sized, never used for a decision (NN/g practitioners warn to focus on key moments, not every interaction). (2) An aspirational-fiction emotional curve — mark assumption vs evidence. (3) Mistaking the map for a backlog (Patton's warning).

---

### M5 · Technology & Development Risk

**Clarity anchor:** the **invest-vs-optimize map** — where quality is bought and where cost is deliberately optimized — on top of the risk register and architecture picture.

**Recommended primary genre: a deliberate-tradeoff invest-vs-optimize map as hero, over a sortable, quantified risk register.** **Alternate: a tornado / ranked-exposure chart** for the risk portion.

**Departure flag (the strongest in the report):** The default risk genre is the **5×5 heat map**, and it is *wrong*. Cox (2008, *Risk Analysis*) proved matrices "can correctly and unambiguously compare only a small fraction (e.g., less than 10%) of randomly selected pairs of hazards" and that they "can mistakenly assign higher qualitative ratings to quantitatively smaller risks"; Hubbard (*The Failure of Risk Management*) calls the relevant chapter "Worse Than Useless"; range compression means a $100M and a $10B consequence can share a cell. For a system whose premise is *clarity of expression*, shipping a genre that mathematically misranks is indefensible. **Replacement:** a sortable risk register (rank by a status-weighted score computed in the pull script) with likelihood, impact, and — where available — a quantified exposure range; a **tornado view** ranks risks by impact magnitude honestly (longest bar = biggest driver). This survives scale far better than a matrix (5 vs 50 risks is just more sortable rows).

**Second departure (argued):** Should the invest-vs-optimize map be the hero above the register? Yes — the charter's core question is where to invest for a good experience vs where to optimize cost/complexity, a deliberate-tradeoff statement best served by an effort/impact-style quadrant or a labeled "buy quality here / buy cheap here" map (rhyming with Kano and cost-of-quality thinking). The register and architecture are the *evidence* beneath that decision.

**Named exemplars:**
- **Tony Cox, "What's Wrong with Risk Matrices?"** (*Risk Analysis*, 2008) — the citable proof against heat maps. *Steal:* the justification to sort/quantify instead of coloring cells.
- **Douglas Hubbard, *The Failure of Risk Management*** — quantitative alternatives, ordinal-scale critique. *Steal:* replace multiplied ordinal scores with ranges/exposure.
- **Tornado diagram / sensitivity analysis** (PMBOK quantitative risk analysis) — ranks variables by impact, biggest at top. *Steal:* the ranked-bar honesty for "which risk moves the outcome most."
- **Michael Nygard ADR** (Status/Context/Decision/Consequences) — the most-used decision-record format. *Steal:* the structure for each build-buy-reuse decision and risk disposition (accept/mitigate + early-warning signal); "no orphan decisions."

**Information hierarchy:** *Hero:* the invest-vs-optimize map. *Support:* the sortable risk register (ranked) and the architecture picture with conformance rules; each high risk shows its response. *Detail-on-demand:* risk record (likelihood/impact/exposure, owner, early-warning signal), ADR-style decision cards, API/DBT contract drafts.

**Judgment affordances (Review):** Two already-designed deliverables — **risk ranking** (sort/adjust; every high risk must have a response or it's flagged) and **architecture map sign-off**. Build/buy/reuse dispositions read as ADR cards with an accept action. Terminal *decision*: risk dispositions + architecture sign-off, captured with signer + timestamp. The "no high risk without a response" rule (risk-register/contract-closure **[non-UI]**) renders as a blocking readiness strip.

**Data binding:** `Risk register` → register rows; **computed status-weighted scores** → sort order and tornado bar lengths; `brownfield assets` → 80%-reuse annotations on architecture; `architecture/contract drafts` → the architecture picture and contract cards. **Slots/states:** register iterates over `risks[]`; n=0 → "no risks logged (Explore red-team)"; n=5 vs n=50 → same table, sortable/filterable, "top N + rest collapsed"; a high risk with no response → red "response required" flag that blocks sign-off; missing exposure → row still ranks by status-weighted score, tornado bar shows "qualitative."

**Emotional register:** **Sober** — the most plain and serious page; gravity from honesty (quantified exposure, named owners, early-warning signals), not from red cells. Severity must never be color-only (WCAG) — use rank position + label + magnitude.

**Anti-patterns:** (1) The 5×5 heat map hiding severity via range compression. (2) Orphan decisions — a TECH choice with no rationale, a high risk with no response. (3) An invest-vs-optimize map with no *deliberate* cheap side (if everything is "invest," it's a wish list, not a tradeoff).

---

### M6 · Build Sequencing

**Clarity anchor:** the **sequencing map** — bodies of work in order, each annotated with *why this order* (risk retired, dependency unlocked, test emphasis), with the **beta line** drawn on it.

**Recommended primary genre: a pre-computed dependency DAG (left-to-right, layered) with per-unit "why this order" annotations and a beta gate line.** **Alternate: a story-map backbone with release slices** (Patton).

**Competing-genre trade-off (DAG vs Gantt vs Now/Next/Later vs story-map backbone):**
- **Gantt** encodes dates, manufacturing false precision and reading as a commitment (Bastow/ProdPad: "no false precision"; Cagan) — *rejected* as primary.
- **Now/Next/Later** is excellent for *external* roadmap confidence horizons but too coarse for build-order rationale and dependency logic — better suited to M7.
- **Story-map backbone** slices by user value and gives a natural walking skeleton — a strong alternate that rhymes with M4.
- **Dependency DAG** is the only genre that shows *why this order* structurally (what unlocks what, what risk each unit retires); it wins because the human's judgment here is precisely "the why." **Constraint-respecting build:** compute a **Sugiyama layered layout** (the DAG standard, used by Graphviz `dot`) in the pull script and emit node x/y coordinates + edge paths into the JSON; the template draws inline SVG — no library, no in-browser layout.

**Named exemplars:**
- **Jeff Patton walking skeleton** — the smallest end-to-end slice first. *Steal:* the beta gate as "the earliest real users touch it," analogous to the walking skeleton.
- **Janna Bastow / ProdPad Now/Next/Later** — "the commitment lives in the OKR, not the roadmap timeline." *Steal:* the anti-Gantt stance and the honesty that order ≠ date.
- **Sugiyama layered graph drawing** (Graphviz `dot`) — layer assignment → crossing minimization → coordinate assignment. *Steal:* the deterministic offline layout shipped as coordinates.
- **Release-engineering phased rollout / test pyramid (60/30/10)** — functional + non-functional emphasis per unit. *Steal:* per-unit test-emphasis annotations and the phased beta.

**Information hierarchy:** *Hero:* the DAG, left-to-right, with the **beta line** drawn vertically across it (everything left of it ships before real users touch it). *Support:* per-unit annotations (why this order, risk retired, dependency unlocked, test emphasis). *Detail-on-demand:* unit sizing, test-coverage map, contract references.

**Judgment affordances (Review):** The sequence is drafted mechanically from the dependency graph; the human **judges the *why*** — accepts/adjusts what's first, where beta lands, what risk each unit retires. Terminal *decision*: accepting the sequence + rationale. Moving the beta line is the signature interaction — it defines the earliest user contact. Sign-off captures the accepted sequence.

**Data binding:** **computed dependency DAG** → nodes (units) + edges (dependencies) with pre-computed coordinates; **computed unit sizing** (3–5 APIs / 2–4 tables / 3–7 units) → node size/labels; **computed test-coverage map** → per-unit test-emphasis chips; `beta criteria` → the beta line position + gate card. **Slots/states:** DAG iterates over `units[]` and `edges[]`; n=1 → single node, beta trivially after it; n=0 → "no work units yet (Build)"; a cycle in dependencies → the layout flags it (Sugiyama breaks cycles by back-edge reversal; surface the reversed edge as "review this dependency"); large graphs → group into layers/phases, collapse detail.

**Emotional register:** Purposeful, engineering-calm; mild satisfaction at the beta line (getting it into users' hands fast). Otherwise plain and structural.

**Anti-patterns:** (1) A roadmap mistaken for a commitment — any date invites the misread; keep it order + rationale. (2) An unreadable DAG hairball — Sugiyama crossing-minimization + layering is mandatory. (3) A beta line drawn as an afterthought — it's a first-class decision.

---

### M7 · Go to Market

**Clarity anchor:** the **launch one-pager** — goals, first-users plan, channel mix with reasons, onboarding needs, and the **feedback contract** — each traceable to the engagement model (M3).

**Recommended primary genre: a launch one-pager with a reconciliation table** (positioning, offer, channels, metrics must not contradict). **Alternate: a positioning canvas** (Dunford) for the positioning sub-decision, and Now/Next/Later for any launch timeline.

**Competing-genre trade-off (positioning canvas vs one-pager vs reconciliation table):** The **positioning canvas** (Dunford) is right for *deriving* positioning but too narrow for the whole page. The **one-pager** (Amazon PR/FAQ lineage) is the recognizable launch artifact and should be the frame. The **reconciliation table** is the distinctive requirement — the machine face is coherence: positioning, offer, channels, metrics must not contradict **[non-UI]** — so a table putting these four in columns and flagging contradictions is the decision engine. Recommendation: one-pager as the readable artifact, reconciliation table as its spine, positioning canvas as a drill-in.

**Named exemplars:**
- **Amazon PR/FAQ** (Bryar & Carr) — customer-language launch narrative that kills weak ideas early. *Steal:* the one-pager discipline and plain-language launch goals.
- **April Dunford positioning** — "every message should trace back to the positioning document." *Steal:* channel/offer decisions traceable back to positioning and M3's engagement model.
- **NN/g comparison table for channels** — channels compared on fit floors/economics. *Steal:* channel mix as a comparison against fit floors, chosen mix highlighted.
- **Now/Next/Later** (Bastow) — for launch phasing without false dates. *Steal:* express any launch timeline as confidence horizons.

**Information hierarchy:** *Hero:* the one-pager — launch goals + first-users plan + channel mix with reasons. *Support:* the reconciliation table (positioning · offer · channels · metrics, with contradiction flags) and the feedback contract (which analytics instrumentation + direct channels exist at launch). *Detail-on-demand:* channel economics (CAC tiers, $500×3 testing cadence), onboarding-needs capture, runbooks.

**Judgment affordances (Review + Intake):** Review — channel mix against **fit floors**, positioning against guardrails; the reconciliation table surfaces any contradiction as a blocking flag. Intake — onboarding-needs capture. Terminal decisions: positioning + offer, channel-mix with fit rationale, launch goals, feedback contract. Sign-off captures the coherent launch plan. The contradiction flag turning green across the table is the "we are coherent" moment.

**Data binding:** `positioning/offer/channel candidates + fit scores` → the channel comparison and reconciliation columns; `launch goals` → the goals block; `feedback contract` → the instrumentation + direct-channel list; each row carries a trace link to M3. **Computed:** the reconciliation/coherence check **[non-UI]** → contradiction flags; channel fit-floor pass/fail. **Slots/states:** channel comparison iterates over `channels[]`; n=0 → "no channels evaluated (Shape)"; a channel below fit floor → flagged, excluded by default; a reconciliation contradiction (e.g., enterprise positioning + self-serve channel) → red flag that blocks launch sign-off; missing feedback contract → "no feedback instrumentation defined" warning.

**Emotional register:** Energized but accountable — a launch you'd stake your name on (PR/FAQ confidence), tempered by the sober reconciliation table that refuses internal contradictions. The feedback contract reads as a promise, not a footnote.

**Anti-patterns:** (1) Positioning that doesn't trace to anything (Dunford's drift warning). (2) A channel list with no fit reasoning ("we'll do everything"). (3) Omitting the feedback contract — launching blind is the failure the charter guards against.

---

### M8 · Launch Verdict

**Clarity anchor:** the **launch scorecard** — targets vs actuals, the grade, the verdict, and the reasoning that will stop a future session from re-litigating it.

**Recommended primary genre: a target-vs-actual scorecard using bullet graphs, with a computed drift column and a single grade + verdict.** **Alternate: a drift/variance waterfall** or a compact dashboard for multi-metric launches.

**Competing-genre trade-off (scorecard vs dashboard vs drift/variance waterfall):** A **dashboard** is a monitoring surface (many live metrics, no verdict) — wrong, because the moment *terminates in a verdict*. A **drift/variance waterfall** explains *why* actuals diverged and is the right alternate. The **scorecard** — targets vs actuals with a grade — carries a verdict and matches the canon's A–F grading and go/no-go/pivot/kill taxonomy. **Bullet graphs (Stephen Few)** are the ideal per-metric encoding: per *Information Dashboard Design* (2006), "Bullet graphs were developed to overcome the fundamental issues of gauges and meters: they typically display too little information, require too much space, and are cluttered with useless and distracting decorations." Recommendation: scorecard of bullet graphs + computed drift + one grade + one verdict.

**Named exemplars:**
- **Stephen Few bullet graph** — a measure vs target within qualitative ranges, replacing gauges. *Steal:* one bullet graph per KPI (actual bar, target marker, qualitative bands).
- **OKR grading (Google re:Work)** — "The sweet spot for OKRs is somewhere in the 60-70% range… the expectation is to get an average of 0.6 to 0.7," with aspirational-OKR bands "0.7 to 1.0 = green… 0.4 to 0.6 = yellow… 0.0 to 0.3 = red." *Steal:* the grade scale, the RAG bands (dual-encoded), and the "a perfect score means the goal was too easy" framing.
- **Amazon PR/FAQ (as the target baseline)** — the launch goals set in M7 are what actuals are judged against. *Steal:* judge reality against the exact goals M7 committed.
- **ADR/Nygard reasoning** (Status/Context/Decision/Consequences). *Steal:* record the verdict's *reasoning* so a future session can't re-litigate it (the canon's explicit requirement).

**Information hierarchy:** *Hero:* the grade + the verdict (scale / iterate / pivot / kill), stated plainly. *Support:* the scorecard of bullet graphs (KPI: target vs actual, with computed drift). *Detail-on-demand:* per-KPI reasoning, week-1 early-warning records, feedback records, superseded intent.

**Judgment affordances (Review):** The scorecard arrives **computed**; the human **owns the verdict**. This is the heaviest sign-off in the system — a *decision* with consequences (kill/pivot/scale) — deserving the fullest ceremony: a reserved color, a literal-verb button per verdict ("Record verdict: Pivot"), signer + timestamp, and recorded reasoning. Distinguish from acknowledgement: not "I've seen the numbers," but "I decide what we do."

**Data binding:** `KPI targets vs Reality actuals` → each bullet graph (target marker + actual bar); **computed drift** → the drift column/delta and direction; `scorecard grade` → the hero grade. **Computed:** drift deltas and the roll-up grade (launch-validation **[non-UI]**). **Slots/states:** scorecard iterates over `kpis[]`; n=0 actuals → "no measured outcomes yet (Learn)"; a KPI with target but no actual → "not yet measured" (not a zero); missing target → the metric can't be graded, flagged; grade can't compute until a threshold of KPIs report → "provisional."

**Emotional register:** Consequential and honest — the reckoning; weighty, like reading a verdict. Measured pride where results are good, deliberate plainness and no spin where bad (the page exists to stop re-litigation, so it must read as fair). The emotional bookend to M1's opening thesis.

**Anti-patterns:** (1) A dashboard with no verdict — endless metrics, no decision. (2) Gauges/speedometers instead of bullet graphs (Few's exact critique). (3) A grade with no recorded reasoning — guaranteeing the future re-litigation the charter is trying to prevent.

```
┌───────────────────────────────────────────────────────────┐
│ LAUNCH VERDICT              GRADE: B−    data as of · ⟲     │
│ Verdict: ITERATE                                            │
│                                                             │
│ Activation  target│——————◆———actual▉▉▉▉   +8%  ▲           │
│ Retention   target│————◆ actual▉▉         −22% ▼ (miss)    │
│ CAC         target│——◆——— actual▉▉▉        on band         │
│  (bullet graphs: ◆ = target, ▉ = actual, bands = qual.)    │
│                                                             │
│ Reasoning ▸ (recorded so we don't re-litigate)             │
│    [ Record verdict: Scale | Iterate | Pivot | Kill ]      │
│                                        signer · timestamp   │
└───────────────────────────────────────────────────────────┘
```

---

## Cross-Cutting: The One-Family System

The eight pages must feel like one family while each genre stays distinct (a journey map must not look like a risk register). The family lives in the *chrome, tokens, and shared components*, not in the hero visuals.

**Design tokens (buildable with no external fonts/CDNs):**
- **Type:** one system font stack (`system-ui, -apple-system, Segoe UI, Roboto, sans-serif`) — no web fonts (file:// constraint). A modest ~6-step type scale, each page's hero at the top step.
- **Color:** a restrained neutral base + one accent per *loop verb* (Explore/Shape/Decide/Build/Learn/Check) so a page signals where in the loop it sits. Severity/grade encodings are **dual-channel** (position/label + color) to satisfy WCAG — never color alone (critical for M5/M8).
- **Spacing:** an 8px grid; CSS-grid for all matrices (M4 coverage, M3 comparison, M5 register) so they scale by data.

**ID-chip + evidence-tier + confidence pattern (the family signature):** every fact carries a **provenance chip**: `‹typed-ID›` always visible; **evidence tier** (GRADE-style four-level dot) and **confidence** (IPCC-style qualifier — "very low / low / medium / high / very high") revealed on hover/click, C2PA-style ("click the badge to inspect the provenance chain"). Confidence is also written where it matters (IPCC "lead with what you know"). This one component appears on all eight pages and is the strongest unifier.

**Staleness / "data as of" indicator:** each page embeds its **data-model fingerprint** and shows a "data as of ⟲" stamp. A Check pass compares the embedded fingerprint against a fresh pull; a stale surface renders a visible "may be out of date — rebuild" banner (Grafana/Datadog-style freshness cue). Staleness is a finding, not a surprise — consistent placement top-right on every page.

**Navigation between moments:** a persistent, ordered rail M1→M8 (Problem → Persona → Commercial → Journeys → Tech & Risk → Sequencing → GTM → Verdict), each showing its own freshness dot, so the eight read as one narrative arc from thesis (M1) to reckoning (M8).

**Sign-off ceremony (shared component, weight-calibrated):** every terminal adjudication uses the same grammar, drawn from DocuSign and GitHub PR review: (1) a **reserved signal color** for the commit action; (2) a **literal-verb button**, never "OK" — per IBM Carbon, "Both the title and the button should reflect the action that will occur… Use descriptive words for the actions such as Add, Delete, and Save. Avoid vague words like Done or OK"; (3) **staged friction** proportional to consequence (M8's kill/pivot heaviest; M2's persona-accept lighter); (4) **signer attribution + immutable timestamp**; (5) **binding to a data state**, so a sign-off goes stale if underlying records change (GitHub dismisses PR approval when a new commit lands — the same rule re-opens an accepted M1 statement if its evidence changes). Distinguish **acknowledgement** (low friction: "I've seen this") from **decision** (full ceremony: "I choose/accept") per Material Design's confirmation-vs-acknowledgement guidance.

**Comparison affordance (shared):** M3 (types), M7 (channels), and M5 (build/buy) reuse one comparison component — columns = options, rows = only the attributes that *differ* (NN/g "explicit differences"), single highlighted "recommended" column with a badge and elevation. Weighted-matrix drill-ins expose weights and per-criterion scores so rankings are traceable, not asserted.

**Print/PDF behavior:** a print stylesheet expands all detail-on-demand (provenance chips print as footnotes with tier + confidence + source; DAG/journey render at full width; the sign-off block prints signer + timestamp as a record). No interactivity assumed on paper.

**Light/dark support:** CSS custom properties with a `prefers-color-scheme` switch; because there are no external assets and severity is dual-encoded, both themes work without a second asset set. Inline SVG inherits `currentColor` so DAGs/journey maps theme automatically.

**Where the family conflicts with individual moments (named, not papered over):**
- **M4's two-species tension** (Intake builder + Review sign-off) resists the "one page per moment" family rule — resolved as two modes of one template, but a genuine seam.
- **M5's sobriety vs the per-verb accent colors** — the risk page wants restraint; the family's Decide-accent must be muted there so severity encoding isn't drowned out.
- **M1/M3 sentence-heroes vs the data-density of M5/M6** — the family must tolerate very different ink densities; the shared chrome carries the family feeling so hero zones can diverge sharply.

---

## Recommendations (staged)

**Stage 1 — Build the family shell first (before any single moment).** Implement the provenance chip, the "data as of" fingerprint/staleness stamp, the loop-verb token set, the sign-off ceremony component, and the comparison component. These five carry the "one family" feeling and are reused everywhere. *Benchmark to proceed:* the chip renders ID-only by default and reveals tier+confidence on demand; the staleness stamp flips when the fingerprint mismatches.

**Stage 2 — Build the two "sentence" moments (M1, M3) and the scorecard (M8).** Lowest-risk to render single-file (no graph layout); they validate the departures (annotated sentence; pricing-as-clause; scorecard-not-dashboard). *Benchmark:* a non-author PM reaches every M1 clause's evidence in one click; M3 reads engagement-first with price visibly demoted.

**Stage 3 — Build the map moments (M4 journey, M6 DAG).** These need the pull script to emit pre-computed layout (emotion-band coordinates; Sugiyama DAG coordinates). *Benchmark:* the DAG renders with zero edge-crossing hairballs at n=20 units and redraws identically from the same JSON (determinism); the journey map marks money-shot and delight/utilitarian as labeled decisions.

**Stage 4 — Build the register/decision moments (M5, M2, M7).** M5 is the flagship departure — ship the sortable quantified register + tornado, *not* a heat map, with the invest-vs-optimize map on top. *Benchmark:* M5 has no 5×5 grid anywhere; every high risk has a response or is blocked from sign-off; the register is legible at n=50.

**Thresholds that would change these recommendations:**
- If the target audience turns out to *demand* a heat map for familiarity, keep the sortable register as the source of truth and offer a heat map as a clearly-labeled, non-authoritative "overview" view with the Cox caveat visible — do not let it drive ranking.
- If M4's two-species tension causes real confusion in testing, split it into two pages and update the "one page per moment" rule.
- If quantified risk exposure is rarely available in practice, the tornado view degrades to a status-weighted ranked list (still better than a matrix).

---

## Open Questions (first-class)

1. **M4 is two moments wearing one name.** The Intake builder and the Review sign-off are different jobs; the canon's "both" species mix is unresolved as a single artifact. *Confidence this is a real tension: High.* Resolve with a usability test of the two-mode template vs two pages.
2. **Does M1's one sentence deserve a whole page?** I argue yes (the annotated-sentence departure), but this is the most contestable call. *Confidence: Medium.* Raise it with a prototype test of the annotated sentence vs a compact five-element table for author trust and speed.
3. **How much quantification will M5/M8 actually have?** The tornado and drift visuals are strongest with numbers; if the corpus is mostly qualitative they degrade to ranked lists/RAG. *Confidence the degraded forms still beat a heat map/dashboard: High.*
4. **Sign-off staleness semantics.** Binding a sign-off to a data state (GitHub-style dismissal) is powerful but could be disruptive if records churn constantly — re-opening accepted decisions too often erodes the ceremony's weight. *Confidence this needs a tuning policy: Medium.* Raise it with a churn analysis of how often each moment's records change post-sign-off.
5. **Emotional-register calibration across the family.** M4 wants warmth, M5 wants sobriety, M8 wants gravity — the shared token set must stretch across all three without feeling incoherent. *Confidence achievable: Medium-High*; would rise with a built style-tile spanning the extremes.
6. **The "money shot" and "negative persona" have no computed check** — they are human declarations. If the machine face can't verify them, the page must make their *absence* visible (a "no money shot named" flag). *Confidence this is needed: High.*

## Challenges to the Canon's Framing

- **The 5×5 heat-map instinct must be rejected; any matrix is a departure-to-avoid, not a default.** This holds up — Cox and Hubbard are decisive.
- **M3's "engagement model is the sentence, pricing is a clause" is a strong, correct premise** — most templates violate it, and the design should visibly enforce it (locked/understated price). It holds up as a visual proposition.
- **M1's "sentence with citations as a designed artifact" is the shakiest premise** — a sentence is a thin thing to hang a page on. I back the departure but flag that if authoring speed suffers, the five-element table should take over as hero. Surfaced as a finding, not resolved silently.

*Overall confidence in the genre recommendations: **High.** Confidence in the two departures (M5 heat-map rejection, M6 Gantt rejection): **Very High** — both backed by primary, well-cited sources. Confidence in the M1 annotated-sentence departure: **Medium**; what would raise it: a prototype test with 3–5 experienced PMs.*

---

### Source notes on quality
Primary/authoritative sources anchor the strongest claims: Cox (2008, *Risk Analysis*, peer-reviewed) and Hubbard (*The Failure of Risk Management*) for the risk-matrix departure; Google re:Work and the IPCC AR5 Guidance Note (Mastrandrea et al., 2010) for grading/confidence language; NN/g for journey mapping, service blueprints, and comparison tables; Kalbach, Patton, Torres, Dunford, Moore, Cooper/Goodwin, Shostack, Few, and Nygard as named framework originators. Sign-off/comparison UI details were corroborated across primary design-authority sources (Material Design, IBM Carbon, GitHub docs) plus DocuSign's own support materials; pricing-table and decision-matrix "best practice" conventions come from practitioner sources and are reliable for conventions but are not empirical studies — the NN/g articles are the research backbone there. Where a 2026-dated secondary source restated a framework (e.g., OST/story-mapping explainers), I relied on it only for uncontested definitional facts and attributed substantive claims to the originators.