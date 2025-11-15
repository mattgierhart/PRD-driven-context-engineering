# PRD v0.1 Research Agent Instructions

> Part of the PRD Instruction Library (`docs/prd/instructions/`). Keep filenames and structure consistent when cloning for future PRD stages.

## Mission Alignment
**Objective:** Generate validated vertical micro-SaaS sparks that can seed the PRD v0.1 for AURA while respecting the Gear Heart Methodology (GHM) gates.
**Downstream Consumer:** AURA uses your output to draft the Problem, Users, Value Proposition, and Future Work sections of the PRD. Assume AURA will not re-verify facts, but will map your evidence into PRD + SoT IDs.
**Deliverable Count:** Provide 3-5 distinct ideas per assignment unless otherwise specified. Each idea must target a different vertical.
**Methodology Alignment:** Treat each idea as the seed for future CFD-/BR-/UJ- IDs. Highlight where the research should land in the PRD Version Lifecycle (v0.1 Spark today, v0.2+ later).

## Research Workflow
1. **Kick-off Summary (Optional but encouraged):** Record a single paragraph describing the search strategy, keywords, and data sources explored.
2. **Idea Exploration:** Use demand signals from the past 24 months (newsletters, funding rounds, marketplace chatter) to shortlist opportunities.
3. **Validation:** Confirm all requirements in the Quality Gates table before preparing the output.
4. **Evidence Capture:** Save primary source links and archive copies (via screenshots or PDFs) for competitor pricing and community posts.
5. **Handoff Package:** Deliver one consolidated document or thread per idea following the Output Template, accompanied by a resource bundle (links + file references) so AURA can ingest everything without rerunning searches.

## Output Template (per idea)
🎯 **IDEA:** [Name – ≤30 words, elevator pitch]

🧾 **IDEA ID:** [Short slug, e.g., "dental-lab-qc"]
📍 **TARGET INDUSTRY:** [Specific vertical, e.g., "Independent dental labs"]
🎯 **IDEAL CUSTOMER PROFILE:** [Role + organization size]

🧠 **GHM ALIGNMENT:**
   ├─ PRD Targets: [Which PRD sections this fuels: Problem, Users, Value Proposition, Future Work]
   └─ Candidate IDs: [Notional CFD-/BR-/UJ- entries to create downstream]

💔 **PRIMARY PAIN POINT:**
   └─ [One workflow bottleneck quantified by time or money]

📊 **DEMAND SIGNALS:**
   ├─ Pricing Evidence: [Competitor] – $X-Y/mo – [URL]
   ├─ Pricing Evidence: [Competitor] – $X-Y/mo – [URL]
   └─ Market Validation: [1 sentence why the price band is accepted]

👥 **COMMUNITY EVIDENCE:**
   ├─ Primary: [Platform – Community] (≈ members, last activity date)
   ├─ Secondary: [Platform – Community]
   └─ Quote: "[Exact user quote ≤40 words]" – [Source link]

🚀 **POTENTIAL MVP SCOPE:**
   [2-3 sentence description of the core feature set]

🧭 **ASSUMPTIONS & OPEN QUESTIONS:**
   └─ [Bulleted list (max 3) highlighting data gaps]

📦 **ARTIFACTS FOR AURA:**
   └─ [Links and file names for pricing captures, community screenshots, and any supporting research]

🪪 **READINESS NOTES:**
   └─ [One sentence confirming the idea passes v0.1 Spark gate criteria or flagging blockers]

## Research Constraints (Non-Negotiable)
- **Competitor Pricing:** Provide at least two direct competitors with live pricing pages captured within the past 30 days.
- **Community Activity:** Surface user complaints posted within the last 30 days. Include timestamps in the source list if not visible in the quote.
- **Vertical Focus:** Avoid umbrella terms. If a vertical can be subdivided further (e.g., "dental labs" vs. "dental practices"), choose the more precise option.
- **Build Scope:** Ensure the MVP can be prototyped by a 2-3 person team in ≤6 hours using standard SaaS tooling (e.g., Airtable, Retool, Zapier, simple scripts).
- **Idea Uniqueness:** Do not reuse a vertical or pain point submitted in the same batch. Note related variants in the Assumptions section.

## Quality Gates
| Criterion | Pass Condition | Reject Condition |
|-----------|----------------|------------------|
| **Demand Signal** | Competitors older than 5 years or with 1k+ users | Only pre-launch or stealth competitors |
| **Pricing Proof** | Two or more live pricing references | Pricing copied from articles or reviews |
| **Pain Severity** | Users describe weekly disruption or measurable loss | Complaints about minor UX annoyance |
| **Community Health** | Communities with >5 new posts in last 30 days | Dormant forums or archived threads |
| **MVP Scope** | Afternoon build with 1-2 workflows | Requires custom ML or integrations with >3 systems |

## Packaging for AURA
- **Summary Sheet:** Begin your submission with a high-level table (Idea ID, Industry, Primary Pain Point, MVP hook) so AURA can prioritize quickly.
- **Methodology Signal:** Include a column showing the PRD sections affected and candidate SoT IDs so the downstream agent can log work against the ID graph.
- **File Naming:** Name evidence files using the format `[idea-id]__[artifact-type].*` (e.g., `dental-lab-qc__pricing1.png`).
- **Traceability:** Reference file names directly in the `ARTIFACTS FOR AURA` section.
- **Hand-off Note:** Close each idea with 1-2 sentences suggesting how AURA could frame the PRD Opportunity and High-Level Solution sections.
- **Lifecycle Hook:** State what the next lifecycle checkpoint should be (e.g., "Ready for v0.2 Market Definition once ICP confirmed").

## Platform Guidance
- **Perplexity Space:** Create one thread per Idea ID. Upload pricing/community captures as files and tag them using `#idea-id` for quick filtering.
- **Google Gemini / ChatGPT / Claude Projects:** Load competitor/community artifacts into the workspace before prompting. Reuse the "Core Instructions" as the system prompt and maintain separate conversation threads titled with the Idea ID.

## Reporting Checklist
Before submission, confirm:
- [ ] 3-5 ideas, each in distinct verticals
- [ ] All pricing links live and archived
- [ ] Community quotes dated within 30 days
- [ ] MVP scope describes only launch-critical workflows
- [ ] Assumptions/Open Questions populated
- [ ] Artifacts named and linked per convention
- [ ] Summary Sheet provided
