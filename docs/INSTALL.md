# Install — three ways to adopt the methodology

The methodology is **fork-native**: everything runs from files in your repo, inside your Claude Code
subscription — no API key, no server, no lock-in. Pick the path that matches where you are.

| You are… | Path | Status |
|---|---|---|
| Starting a new product | **1. Use this template** (fork-style) | Available |
| Adding the method to an existing repo | **2. Source-run install** (`install.sh` / the one-paste bootstrap) | Available — prototype |
| Running Claude Code and want the engine delivered live | **3. Claude Code plugin** (`prd-ce`) | Payload exists; public marketplace install **unverified** end to end |

## Prerequisites

- **Claude Code** (the skills, hooks, and agents are written for it; `.claude/` can be replaced with another agent's structure).
- **Python 3.10+** and `pip` (readiness scoring, ID validation): `python3 -m pip install -r scripts/requirements.txt`.
- `git`, `bash`, `awk` (the installer's preflight checks these).
- Optional: Playwright + Chromium if you want to regenerate the HTML review-layer screenshots (`pip install playwright && python3 -m playwright install chromium`).

## 1. Use this template (new product)

Click **Use this template** on GitHub, or:

```bash
gh repo create my-product --template mattgierhart/PRD-driven-context-engineering --clone && cd my-product
```

Then make it yours — the generic seeds replace this repository's own dashboard, product definition,
and memory (this repo's `README.md`, `PRD.md`, and `SoT/` describe the methodology itself, not your product):

```bash
cp README_template.md README.md          # your product dashboard
cp PRD_template.md PRD.md                # your product definition, starting at v0.1
rm -rf SoT && cp -R SoT_template SoT     # a clean Source-of-Truth graph (replace, don't merge)
python3 -m pip install -r scripts/requirements.txt
python3 scripts/readiness.py run         # the repo scores itself: are you ready for v0.2?
```

Open the repo in Claude Code — the `SessionStart` hook loads the read order — and say
*"Let's frame the problem"*: the `prd-v01-problem-framing` skill produces `CFD-` evidence IDs and fills
`PRD.md` v0.1. From there each stage's skills consume the previous stage's IDs, the readiness score tells
you when to advance, and the knowledge graph grows with every decision.

## 2. Source-run install into an existing repo (prototype)

You don't have to fork. The **source-run install path** drops the framework into a fresh *or* existing
repo without clobbering product content. Start from a fresh trusted methodology checkout; the consumer
runtime does not receive the installer, manifest, or install operators. (The pattern is borrowed from
[`ZQadus/Xantham-system-blueprint`](https://github.com/ZQadus/Xantham-system-blueprint): ship a blueprint a
fresh Claude Code session executes, so all cost lands on your Pro/Max plan, not the metered API.)

**One-paste bootstrap** — open a fresh Claude Code session in the repo you want to onboard and paste the
prompt from [`BLUEPRINT.md`](../BLUEPRINT.md); the `ghm-self-install` wizard drives the installer and
verifies the result.

**Deterministic CLI:**

```bash
git clone https://github.com/mattgierhart/PRD-driven-context-engineering /tmp/prd-method
cd /path/to/your/repo
bash /tmp/prd-method/install.sh --target . --profile product --dry-run   # preview
bash /tmp/prd-method/install.sh --target . --profile product             # install
```

Both paths read the trusted checkout's [`.claude/install-manifest.yaml`](../.claude/install-manifest.yaml)
(framework vs. product file classes), are **idempotent**, and **merge** into an existing
`.claude/settings.json` rather than overwriting it. Re-running preserves your `README.md`, `PRD.md`,
`SoT/`, EPICs, and agent memory. Use a fresh trusted checkout for each repository; never treat an
installed consumer as a distributor.

## 3. Claude Code plugin (`prd-ce`) — payload available, marketplace install unverified

The repo carries a generated plugin payload at [`plugins/prd-ce/`](../plugins/prd-ce/) (skills, agents,
hooks, scripts, templates) and a marketplace manifest at `.claude-plugin/marketplace.json`, regenerated
from `.claude/` by `scripts/package-plugin.sh` and drift-checked in CI. In plugin-native mode the engine
is delivered live and `/prd-ce:init` seeds only the consumer-owned files (`PRD.md`, `SoT/`, `epics/`,
`.claude/domain-profile.yaml`, agent `MEMORY.md` starters). A public, end-to-end marketplace install has
**not yet been verified**, so this page does not list an install command for it; the fork and source-run
paths work end to end today. Watch the repo's Releases for the verified plugin path.

## Upgrading a product repo

`MIGRATION.md` carries the version-to-version checklists and `CHANGELOG.md` the release notes; the
`ghm-template-sync` operator (source-checkout only) applies them. For a drift assessment before an
upgrade, use [`MODERNIZATION_ASSESSMENT_PROMPT.md`](MODERNIZATION_ASSESSMENT_PROMPT.md).

## Still on the roadmap

- **MCP server** — the knowledge graph as a queryable service (look up any ID, traverse cross-references,
  pull readiness scores from any MCP-capable agent without loading files into context).
- **Verified plugin release** — the marketplace path above, proven end to end.
