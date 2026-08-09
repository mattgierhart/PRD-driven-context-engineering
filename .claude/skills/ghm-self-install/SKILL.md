---
name: ghm-self-install
description: >
  Install the PRD-Driven Context Engineering methodology into a fresh OR existing
  repository from a fresh trusted methodology checkout — the subscription-native alternative
  to forking the whole repo. Runs an
  interactive wizard that seeds the framework (.claude/ hooks, skills, agents, rules,
  scripts) without clobbering product content. Triggers on "install the methodology",
  "adopt this into my repo", "self-install", "set up PRD lifecycle here", "onboard
  existing project". Outputs an installed framework + a verification report.
disable-model-invocation: true
context: fork
execution_modes:
  default: standard
  supports: [quick, standard, deep]
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash
---

# Source-Run Install

Install the methodology into a target repo from the **install manifest** in a fresh trusted
methodology source checkout. The source checkout supplies the operator and installer; the
consumer runtime deliberately receives neither. The workflow still runs inside your Claude Code
subscription — no API key, no metered calls, no service to stand up.

> **Two source-run paths, one manifest.** This skill is the interactive path. `install.sh` is the
> deterministic CLI path. Both exist only in the trusted source checkout and read its
> `.claude/install-manifest.yaml`, so they can't drift. Never run an installer copied from a
> previously installed consumer; use a fresh trusted checkout for each other repository.

## Consumes

- `.claude/install-manifest.yaml` — authoritative `framework` / `template_seed` /
  `never_touch` lists (the keystone; never hardcode file lists).
- `install.sh` — the deterministic installer this skill normally drives.
- The manifest's `never_touch` boundary — initial template seeds may create these paths,
  but reinstall must never overwrite `MEMORY.md`, `SoT/*`, `PRD.md`, or `README.md` content.

## Produces

- An installed framework in the target repo (no new SoT IDs — this skill *places* the
  engine, it doesn't author specs).
- A verification report (hooks exit successfully; non-empty stdout is valid JSON; `readiness.py` runs).

## Workflow

### Phase 1 — Preflight & mode detect
1. Confirm this operator is running from a fresh trusted methodology checkout, then confirm
   `git`, `python3`, and `awk` are present; warn if the target isn't a git repo. Verify
   `python3 -c 'import yaml'`; if it fails, plan to install the copied runtime requirements with
   `python3 -m pip install -r "<DIR>/scripts/requirements.txt"` before verification.
2. Detect mode: **greenfield** (no `.claude/`) vs **brownfield** (existing `.claude/`).
   Brownfield means *merge, never overwrite product*.
3. State the trade explicitly: this installs files only — it costs subscription tokens
   for the wizard turn, **zero API**.

### Phase 2 — Wizard questions
Ask only what changes the outcome (honor the execution mode's budget):
- **Target directory** (default: current repo).
- **Domain profile**: `product` (default) · `library` · `infrastructure` · `research`.

Subset installs are not supported by the deterministic manifest path; install the complete
runtime so the dependency closure remains verifiable.

### Phase 3 — Install (drive `install.sh`)
Run the deterministic installer from the trusted source checkout so behavior matches the CLI path
exactly:
```bash
bash install.sh --target <DIR> --profile <PROFILE>        # add --dry-run to preview
```
- Show the `--dry-run` plan first `[standard+]`, then execute.
- If a framework file shows **drift**, surface the diff and only re-run with `--force`
  after the user confirms (show the exact diff before any destructive framework refresh).
- Never overwrite anything in the manifest's `never_touch` list.

### Phase 4 — Verify (trust but verify)
1. Run each `.claude/hooks/*.sh` against representative input and require a successful exit. If a
   hook writes non-empty stdout, assert valid JSON; an intentional no-op may be silent.
2. Run `python3 "<DIR>/scripts/readiness.py" run --repo "<DIR>"`. Accept only documented gate
   exits `0`, `1`, or `2` (the generic empty scaffold should return BLOCK/`2`) and report the
   score. Exit `3` or any other runtime/dependency error fails verification.
3. Print next steps: customize `README.md` + `PRD.md`, then "Let's frame the problem".

## Anti-patterns

| Pattern | Fix |
|---------|-----|
| Hardcoding the file list in the skill | Read `.claude/install-manifest.yaml` |
| Overwriting a brownfield repo's `PRD.md`/`SoT` | Honor `never_touch`; seed templates once |
| Treating readiness BLOCK on a fresh scaffold as a bug | It's the gate working — report the score |
| Re-implementing copy logic instead of driving `install.sh` | One code path = no drift |
| Reusing an installer from a consumer repo | Clone or verify a fresh trusted methodology checkout for each target |
