# Technical Decisions (SoT File)

> Fixture for scripts/asof.py — a worked supersession with valid-time stamps.
> ARC-001 was authoritative from v0.6, superseded by ARC-002 at v0.8.

## ARC-001 | Synchronous in-process request handling

**Status**: Superseded
**Valid From**: v0.6
**Valid To**: v0.8
**Invalidated By**: ARC-002

- **Decision**: Handle all inbound requests synchronously in-process.
- **Rationale**: Simplest path to MVP; no queue infrastructure to operate.
- **Alternatives Considered**: Message queue (premature for launch-scale traffic).

## ARC-002 | Queue-backed asynchronous processing

**Status**: Accepted
**Valid From**: v0.8
**Valid To**: —
**Supersedes**: ARC-001

- **Decision**: Offload long-running work to a durable queue.
- **Rationale**: Synchronous handling timed out under real load; a queue decouples request latency from work duration.
- **Alternatives Considered**: Larger sync timeouts (treats the symptom, not the cause).

## TECH-001 | Runtime: Node.js 20 LTS

**Status**: Accepted
**Valid From**: v0.5
**Valid To**: —

- **Decision**: Node.js 20 LTS for backend services.
- **Rationale**: Team expertise; strong HTTP ecosystem.
- **Alternatives Considered**: Go (smaller hiring pool), Python (slower hot paths).
