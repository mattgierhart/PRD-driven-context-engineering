# Security Policy

## What this repository is

PRD-Led Context Engineering is a methodology: markdown templates, Claude Code skills and hooks (bash and
Python), an installer script, and a readiness scorer. It runs locally in your repository and makes no
network calls of its own. The security-relevant surfaces are the installer (`install.sh`,
`scripts/prd-ce-init.sh`), the hooks under `.claude/hooks/`, and the generated plugin payload.

## Supported versions

The latest tagged release and the `main` branch receive fixes. Older template versions are upgraded
through `MIGRATION.md`, not patched in place.

## Reporting a vulnerability

Please **do not** open a public issue for a security problem. Use GitHub's private vulnerability
reporting on this repository ("Report a vulnerability" under the Security tab), or contact the maintainer
through https://www.gearheartai.org. Include the affected file(s), the version (`.claude/VERSION`), and a
reproduction. You will get an acknowledgement within a week and a fix or a stated decision as soon as the
issue is understood.

## Guidance for adopters

- Install from a **fresh, trusted checkout** of this repository; never treat an installed consumer repo
  as a distributor (`BLUEPRINT.md`).
- Review hooks before enabling them — they run on your machine on session and tool events.
- Keep secrets out of `SoT/`, `temp/`, and agent memory; the distribution tests refuse machine-local paths
  in distributable surfaces, but your product content is yours to guard.
