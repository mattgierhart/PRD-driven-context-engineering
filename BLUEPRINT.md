# BLUEPRINT — Source-Run Install the PRD-Driven Context Engineering Methodology

> **One trusted source checkout, not a binary.** This methodology installs from plain files, so it
> runs entirely inside your **Claude Code subscription** — no API key, no metered calls, no server
> to stand up. The source checkout supplies the installer; the consumer runtime does not.

This is the **adopt-into-an-existing-repo** path. (Prefer a clean start? Fork the repo
instead — see the README Quick Start.)

---

## The one-paste bootstrap

Open a fresh Claude Code session **in the repo you want to onboard** and paste:

```
Clone a fresh trusted copy of https://github.com/mattgierhart/prd-driven-context-engineering into a temp dir,
then run its `ghm-self-install` skill to install the methodology into THIS repository.
Detect whether I'm greenfield or brownfield, ask me for a domain profile, preview the
plan with --dry-run, then install and verify.
```

Claude reads `.claude/install-manifest.yaml`, drives `install.sh`, and verifies the
result — all on your subscription. For another target repository, start from another fresh trusted
checkout (or verify and refresh the source checkout); never reuse a consumer repo as the installer.

### Or the deterministic CLI

```bash
git clone https://github.com/mattgierhart/prd-driven-context-engineering /tmp/prd-method
cd /path/to/your/repo
bash /tmp/prd-method/install.sh --target . --profile product --dry-run   # preview
bash /tmp/prd-method/install.sh --target . --profile product             # install
```

---

## What the wizard does

1. **Preflight** — checks `git`/`python3`/`awk`, reports missing PyYAML with the exact bundled
   requirements command, and detects greenfield vs brownfield.
2. **Asks** — target dir and domain profile (`product` · `library` · `infrastructure` ·
   `research`). The deterministic path installs the complete dependency-closed runtime.
3. **Installs from the manifest** — framework files copied/updated; product templates
   seeded **once**.
4. **Verifies** — hooks exit successfully; non-empty hook stdout parses as JSON;
   `readiness.py` runs (a BLOCK score on an empty scaffold is the gate working, not an error).

## What it will and won't touch

| Class | Examples | On install |
|-------|----------|------------|
| **Framework** (engine) | `.claude/hooks`, `.claude/skills`, `.claude/rules`, allowlisted `scripts/*`, `CLAUDE.md` | Installed; updated on re-run (`--force` if locally drifted) |
| **Local template reference** | `README_template.md`, `PRD_template.md`, `SoT_template/` | Inert generic source carried for inspection/manual copying; not install authority |
| **Template seed** | `README.md` (from `README_template.md`), `PRD.md` (from `PRD_template.md`), `SoT/` (from `SoT_template/`), two consumer docs, EPIC templates, agent `MEMORY.md` | Seeded **once**, then yours |
| **Never touched** | your `PRD.md` body, `SoT/` entries, `EPIC-*.md`, agent `MEMORY.md` content | Protected — brownfield-safe |

Every mutable seed destination has a distinct immutable source path in the trusted checkout; a
consumer's customized docs, profile, memories, or epic guides are never reused as seed input.

The authoritative lists live in the trusted source checkout's
[`.claude/install-manifest.yaml`](.claude/install-manifest.yaml). Re-running that source installer
is **idempotent**: framework updates, product stays put. On brownfield repos
the installer **merges** its hooks into your existing `.claude/settings.json` instead of
overwriting it.

---

## Why subscription-native (the lesson we borrowed)

The design follows the `ZQadus/Xantham-system-blueprint` pattern: use a **trusted source blueprint a
fresh Claude Code session executes**, not a consumer-carried installer. Because every step is file
I/O the agent performs, all cost lands on your Pro/Max plan rather than the metered API.
We deliberately deferred Xantham's heavier hardening for this prototype:

- **Docker audit sandbox** — verify the blueprint in a container before host install.
- **Signed checksums** — a `CHECKSUMS.sha256` + verify script for tamper-evidence.
- **MCP-server distribution** — the knowledge graph as a queryable service.

These are proven, intentional next steps — not part of the v1 source-run install path.
