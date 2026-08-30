# GitHub Governance State

Last updated: 2026-08-30 20:15 CEST

This page records verified GitHub governance and CI state. It distinguishes a passing check from missing or unsupported coverage.

## 2026-08-30 operational audit

- The estate contains 60 active GitHub repositories and 321 active workflows.
- The latest default-branch workflow state is 277 successful runs, 44 expected event-only or never-run workflows, and zero failures.
- The 44 no-run entries comprise 40 pull-request-only dependency-review workflows, two reusable `workflow_call` workflows, the Rust dynamic Dependabot workflow, and one stale Kotlin CodeQL workflow registry entry.
- The final Ruby Dependabot run completed successfully after the snapshot, so no workflow remained in progress.
- No open stakeholder pull request had failing checks when the audit closed.
- D, Fortran, Ruby, and Scala now pass `security-analysis` on their default branches after adding SARIF upload permission and Dependabot cooldown policy.

## Security posture

- Secret scanning, push protection, and Dependabot security updates remain enabled on the 59 public repositories.
- The audit found zero open Dependabot, code-scanning, or secret-scanning alerts in the queried estate.
- Dependabot alert APIs were available for all 60 repositories.
- Code-scanning APIs were available for 17 repositories and unavailable for 43. An unavailable endpoint is a coverage gap, not evidence that SAST passed.
- One secret-scanning endpoint was unavailable. This is recorded as unavailable coverage, not a passing result.
- External Actions in the hardened set are pinned to immutable SHAs, checkout credentials are not persisted, duplicate feature-branch push runs are removed, and Dependabot uses a seven-day cooldown where configured.
- Supported CodeQL and language-native analyzers remain authoritative. Unsupported languages must use documented alternative SAST rather than fake CodeQL coverage.
- Validated dependency and runtime updates include Erlang/OTP 29, Node 25 with an explicit pnpm bootstrap, Temurin 24 with required container tools, Ruby 4, PHP 8.5, GCC 16, Julia 1.12, Alpine 3.24, and current .NET test dependencies.
- One obsolete Rust CodeQL run remains a historical GitHub queue artifact; its replacement default-branch run passed.

## Required checks

- Stable required-check contexts are currently bound on 13 public repositories after successful remote runs proved their exact names.
- The remaining 46 public repositories stay on staged rollout. Required checks are bound only after their real default-branch contexts are stable.
- Typical gates are native format/lint/build/test, Docker smoke, dependency review, workflow security, and supported CodeQL analysis.
- F# source CodeQL remains unsupported in this program; its gate uses native, Docker, actionlint, dependency review, and workflow-security checks.

## Sonar policy

- Sonar remains intentionally unprovisioned until an organization, project mapping, host, token path, and quality gate are available.
- CodeQL plus language-native analyzers are authoritative in the meantime.
- Sonar must not be reported as passing while it is unavailable.

## Release policy

- GitHub mutations and publication actions remain explicit, gated operations.
- A clean repository, validated local tranche, successful remote CI, and stable check contexts are prerequisites for binding protection or publishing a release.
- Missing security tooling is recorded as a gap and never silently converted into a pass.
