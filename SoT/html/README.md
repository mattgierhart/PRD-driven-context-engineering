# SoT HTML Companion Library

Human-review views of the `SoT/*.md` knowledge graph. The markdown files remain the
**authoritative Source of Truth**; these HTML pages re-express the same entries in the format the
natural reviewer of each artifact type already expects — journey maps for journeys, an API
reference for endpoints, an adoption curve for adoption data.

Open [`index.html`](index.html) in any browser (works from `file://`, no build step, no JS).

---

## Design contract

1. **One HTML page per SoT file**, named in parallel (`SoT.BUSINESS_RULES.md` ↔ `SoT.BUSINESS_RULES.html`).
2. **Every entry's anchor equals its unique ID** — `SoT.BUSINESS_RULES.html#BR-001` is a stable deep
   link, mirroring how IDs are cited in markdown (`SoT.BUSINESS_RULES.md#br-001-rule-name`).
3. **Every cross-reference is a hyperlink** styled as an ID chip (`a.id`), so a reviewer can walk the
   knowledge graph by clicking.
4. **Italic dashed-underline `{placeholders}`** (`span.ph`) mark template slots — they make unfilled fields
   visually loud during review, the HTML equivalent of `{Rule name}` in the markdown templates.
5. **Shared stylesheet** [`assets/sot.css`](assets/sot.css) carries the design tokens, badges,
   and per-view components. No page defines its own colors. The visual language is editorial —
   warm paper, ink hairlines and heavy rules, serif headlines (Plantin/Georgia stack) with
   letterspaced grotesque labels, ochre as the single spot color — in the manner of a printed
   briefing magazine. Each page opens with a numbered kicker line ("The Source-of-Truth
   Review · № 0X — Section").
6. Each page's top nav links back to the Atlas and to its **markdown source of truth**.

### Keeping HTML in sync with markdown

The markdown entry is written first (per rule 03, SoT before/during code). When an entry is added
or changed, duplicate the matching `<article class="entry" id="PREFIX-XXX">` block in the
companion page and fill the placeholders. The HTML is a *render*, never the place a decision is
first recorded.

### Refreshing the screenshots

The root `README.md` embeds screenshots from [`assets/screenshots/`](assets/screenshots/). They are
generated, not hand-made — whenever the pages change (new entries replacing placeholders, style
changes, a new page), regenerate them:

```bash
# one-time setup
pip install playwright && python3 -m playwright install chromium

# refresh everything
python3 SoT/html/screenshot.py

# refresh one shot / see what's configured
python3 SoT/html/screenshot.py adoption
python3 SoT/html/screenshot.py --list
```

What gets captured is defined in the `SHOTS` list at the top of
[`screenshot.py`](screenshot.py) — a page plus an optional CSS selector (capture one entry card)
or `None` (capture the page top with masthead and headline). Adding a new page to the library?
Add a line to `SHOTS` and embed the image in the root README's companion section. Commit the
regenerated PNGs together with the HTML change that caused them.

---

## Angle 1 — Schema per unique ID type

What each ID type captures, distilled from the markdown templates. Bold fields are the ones a
review cannot proceed without.

| ID | Owned by | Core fields | Relational fields (graph edges) |
|----|----------|-------------|--------------------------------|
| **CFD** | customer_feedback | **Verbatim quote**, category, status (New→Analyzed→Actioned/Declined), priority, reporter count + segment + tier, current vs expected behavior, pain level, **product decision** + rationale + decision maker | affected UJ, related BR, addressing FEA (PRD) |
| **PER** | USER_JOURNEYS | **Role**, goals, pain points, tech comfort, status | primary UJ |
| **UJ** | USER_JOURNEYS | Category (Core/Feature/Admin/Error), **user goal, trigger, success criteria**, ordered steps (action → response) | PER, SCR, API, BR, DES, TEST |
| **SCR** | USER_JOURNEYS | **Purpose**, key elements, status | containing UJ, DES components |
| **BR** | BUSINESS_RULES | **Imperative rule statement**, category (numbering band), **severity**, rationale (driver + UX impact), enforcement location + timing, **error contract** (code, user message, recovery) | enforcing API, applying UJ, backing DBT, validating TEST |
| **API** | API_CONTRACTS | **Method + path + auth**, category (numbering band), purpose, request params/body, response shape + **status codes**, lifecycle incl. sunset date when deprecated | UJ, BR, DBT, INT, TEST |
| **DBT** | DATA_MODEL | **Purpose, typed columns** (+required), key indexes, **foreign keys both directions**, category (Core/Feature/Junction/View) | API, UJ, BR, TEST |
| **TECH** | TECHNICAL_DECISIONS | ADR triple: **context, decision, rationale** (chosen-because / alternatives / trade-offs), decision date, last reviewed, supersession chain | API, BR, INT |
| **ARC** | TECHNICAL_DECISIONS | ADR triple + consequences + optional **conformance rule** (rule / check / computed verdict from devgraph) | TECH, DBT, UJ |
| **ENV** | TECHNICAL_DECISIONS | Purpose, CLIs, project packages, config files, scripts, **verification commands**, troubleshooting | TECH, ARC, DEP |
| **INT** | INTEGRATIONS | Provider, category, **rate limits, cost model, SLA**, env vars, prod/sandbox endpoints, migration guide when deprecated | API, BR, DEP, TECH |
| **TEST** | TESTING | Category (numbering band), priority, **Given/When/Then**, implementing file + `@verifies` tag | validates BR, API, UJ, DBT |
| **DEP** | DEPLOYMENT | Category, purpose, **steps (prepare/deploy/verify)**, **rollback** | TEST, MON, SEC |
| **RUN** | DEPLOYMENT | Category (Incident/Maintenance/Recovery), **trigger conditions**, steps (assess/mitigate/resolve) | triggering MON |
| **MON** | DEPLOYMENT | **What is measured, warning + critical thresholds**, category | breach RUN, SLA BR |
| **SEC** | DEPLOYMENT | Name, category, environments, **storage location (never values)**, owner, **last rotated**, rotation procedure | DEP, RUN |
| **LL** | LESSONS_LEARNED | **Rule (one line), why (the story), how to apply (activation condition)**, source, verified date | any related IDs |
| **ADO-STAGE** | ADOPTION | **Stage on Moore curve, evidence, confidence 1–5**, implications, append-only history | CFD, GTM, KPI |
| **ADO-BEACHHEAD** | ADOPTION | Segment, **strict in/not-in criteria**, rationale, target (closed-won + timeframe), confidence | PER, CFD, ADO-STAGE |
| **ADO-WHOLE** | ADOPTION | Gap type, description, **severity (Blocker/Serious)**, evidence CFDs, **owner + target close date**, confidence | FEA, EPIC, ADO-BEACHHEAD |
| **ADO-REF** | ADOPTION | Customer, beachhead fit, story strength, **consent scope**, target placement, confidence | CFD, GTM-CASE, ADO-BEACHHEAD |

Common to all types: stable never-reused ID, status lifecycle (Active/Deprecated/Planned or
domain-specific), created/updated dates, staleness flag after 90 unverified days, deprecation with
pointer to replacement.

## Angle 2 — View per reviewer persona

Why each page looks the way it does. Each format is the established convention its reviewer
already reads fluently, so review effort goes into the content, not decoding the layout.

| Page | Reviewer | Rendered as | Convention it borrows |
|------|----------|-------------|----------------------|
| `index.html` | Anyone entering the graph | Atlas: registry table, ID anatomy, graph patterns, staleness bands | Documentation hub / site map |
| `SoT.customer_feedback.html` | PM, researcher | Insight cards: quote-first, pain gauge, decision stamp; board table | Research repository (Dovetail-style), VOC board |
| `SoT.USER_JOURNEYS.html` | UX designer, PM | Horizontal journey map (trigger → steps → value moment) with pain callouts; persona profile cards; screen wireframe thumbnails | NN/g journey map, persona one-pagers, lo-fi wireframes |
| `SoT.BUSINESS_RULES.html` | PM, compliance, backend | Policy register: severity-flagged rule cards, enforcement matrix, error contract block | Compliance/policy register, rules engine docs |
| `SoT.API_CONTRACTS.html` | Integrating engineer | Method badge + monospace path, request/response panels, status-code table | OpenAPI / Swagger UI / Redoc |
| `SoT.DATA_MODEL.html` | Data engineer, DBA | DB-table entity cards (🔑 PK / 🔗 FK), column matrix, FK relationship map | ER diagram, dbdocs / pgAdmin schema browser |
| `SoT.TECHNICAL_DECISIONS.html` | Architect, tech lead | ADRs (Context → Decision → Rationale → Consequences), blueprint topology diagram, conformance verdict badges | Nygard ADRs, C4-ish container diagram |
| `SoT.INTEGRATIONS.html` | Platform engineer | System-context map + vendor cards leading with rate limit / cost / SLA; vendor inventory table | C4 system context, vendor risk register |
| `SoT.DESIGN_COMPONENTS.html` | Designer, frontend | Specimen on checkerboard canvas, variants/states, token swatches | Storybook / design-system docs |
| `SoT.TESTING.html` | QA engineer, reviewer | Given/When/Then cards, coverage gauges, traceability table, `@verifies` snippet | BDD specs, CI coverage report |
| `SoT.DEPLOYMENT.html` | SRE, on-call | Environment + secrets inventory tables, pipeline stage flow, numbered runbooks with rollback, threshold gauges | Ops wiki / incident runbook page |
| `SoT.LESSONS_LEARNED.html` | Team lead, every agent | Retro cards: rule one-liner → story → activation condition, freshness flags | Retro board / engineering playbook |
| `SoT.ADOPTION.html` | Founder, GTM strategist | Moore bell curve SVG with chasm + "you are here", beachhead in/out checklist, gap tracker, reference pipeline, star confidence | Crossing-the-Chasm board-deck slide |

---

## Extending the library

Adding a new SoT file (via `ghm-sot-builder`)? Add a matching HTML page:

1. Copy the page whose persona is closest to your new artifact's reviewer.
2. Keep the contract: ID anchors, `a.id` chips for every cross-reference, `span.ph` for slots,
   topnav source link, footnote naming the authoritative markdown.
3. Ask "what does this artifact's reviewer already read all day?" and borrow that format —
   don't invent a new one.
4. Register the page in `index.html`'s library table and the topnav of adjacent pages.
