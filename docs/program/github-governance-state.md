# GitHub governance state

## Topology
- `davidsupan/rust-stakeholder` is the only true GitHub fork of `giacomo-b/rust-stakeholder`.
- `davidsupan/stakeholder-core` is the private contract and fixture authority.
- `stakeholder-circus/center-ring` is the public umbrella meta-repo.
- The active GitHub estate contains 60 stakeholder repos: 58 under `stakeholder-circus`, plus `davidsupan/rust-stakeholder` and `davidsupan/stakeholder-core`.
- The canonical research horizon remains 250 total languages; horizon entries are plans, not existing repos.

## 2026-08-20 operational audit
- Local stakeholder repos counted: 60.
- Active GitHub stakeholder repos counted: 60.
- Public repos counted: 59. The private repo is `davidsupan/stakeholder-core`.
- Every active repo uses `main`; Rust was renamed from `master` to `main` and its workflow/docs references were updated.
- A workflow-level default-branch audit found no latest completed failures among workflows that had run. Expected no-run records are PR-only dependency review and reusable workflows.
- Work proceeds on human-named `security/*`, `ci/*`, and `governance/*` branches. `codex/*` branches are not used.
- Local builds and Docker are avoided during the stabilization wave; GitHub Actions is the authoritative build, test, Docker, and SAST execution environment.

## Security and CI hardening
- Actions default permissions are read-only and Actions may not approve pull requests in all 60 repos.
- Secret scanning, push protection, and Dependabot security updates are enabled on all 59 public repos.
- Vulnerability alerts are enabled on all 60 repos.
- All 59 public repos have repo-level `main` branch protection with pull requests, admin enforcement, signed commits, linear history, conversation resolution, and force-push/deletion prevention.
- Stable required checks are currently bound on 13 public repos: center-ring, Rust, Java, JavaScript, C, C++, .NET, Go, Python, Swift, Kotlin, PHP, and PowerShell.
- External Actions in the hardened set are pinned to immutable SHAs, checkout credentials are not persisted, duplicate feature-branch push runs are removed, and Dependabot uses a seven-day cooldown.
- CodeQL or language-native SAST is required only where the scanner and check context have been proven on GitHub.
- The audited CodeQL set currently has zero open alerts. The JavaScript `js/stack-trace-exposure` alert was fixed on 2026-08-20.
- Rust and Java currently have zero open Dependabot alerts after validated `quinn-proto`, `rand`, and `jackson-databind` updates.
- One obsolete Rust CodeQL run remains stuck in GitHub's queue and returns HTTP 500 when cancellation is requested. A replacement run on `main` completed successfully, so the stale run is an external operational artifact rather than failed validation.

## Required-check rollout
- Required checks are bound only after a real PR and default-branch run establish stable context names.
- The remaining 46 public repos keep the common protection baseline while CI/SAST hardening proceeds in small, resource-bounded tranches.
- Typical required gates are native format/lint/build/test, Docker smoke, dependency review, workflow security, and supported CodeQL analysis.
- F# source CodeQL remains unsupported in this program; its gate uses native, Docker, actionlint, dependency review, and workflow-security checks instead.
- Live credentialed provider automation remains opt-in and non-blocking. Deterministic CI stays provider-free.

## Sonar policy
- No `stakeholder-circus` SonarCloud organization, projects, `SONAR_TOKEN`, or `SONAR_HOST_URL` configuration currently exists.
- Sonar is therefore `N/A pending provisioning`, not a passing gate.
- CodeQL plus language-native analyzers are authoritative until a Sonar organization and secret-management path are deliberately provisioned.
- A future Sonar rollout must use committed project configuration, pull-request decoration, quality gates, and non-secret repository variables. No workflow may be added merely to report a synthetic green result.

## Attribution and provenance model
- Derivative language repos are created from imported upstream Rust history, not `git init`.
- Original Rust commits and author metadata remain intact.
- Rewrite and extension commits are layered on top with explicit provenance docs and commit trailers.
- Public repo descriptions, README banners, `AI_DISCLOSURE.md`, `PARITY.md`, and `GAPS.md` keep Codex/manual-review provenance visible.

## Conservative MIT policy for derivative repos
- MIT remains the license baseline for fork-derived language repos.
- Derivative repos keep the upstream MIT notice exactly as imported, including `Copyright (c) 2025 giacomo-b`.
- No second David copyright line is added to derivative repos during the current tranche.
- AI/human authorship nuance is carried in provenance docs rather than by modifying the MIT text.
- `stakeholder-core` and `center-ring` keep MIT as the intended license family, while a standalone neutral contributors notice remains deferred to a later authorship review.

## Branch and repo policy
- All active repos use `main`.
- Rust remains the canonical behavioral source but must also reach the full generator and live-provider/runtime end-state.
- Squash merge is the default integration method for validated PRs.
- Local divergent commits in Java and JavaScript are preserved non-destructively until their provider-lane reconciliation tranche.
- No remote mutation is performed by `stakeholder-manager` without an explicit `release ... --execute` action.

## Workspace-root artifact and routing policy
- `/Users/davidsupan/shareholder` is a coordination workspace, not a git repo.
- Workspace-level summaries are tracked canonically under `stakeholder-core/status/` and `stakeholder-core/docs/program/`, then mirrored under `center-ring/status/` and `center-ring/docs/program/`.
- Repo-level `STATUS.md` files remain repo-scoped and must not replace workspace summaries.
- `.migration/` remains intentional workspace audit material outside repo commits unless explicitly promoted.
- Transient root artifacts such as `erl_crash.dump` stay outside commits and baseline captures.

## Publication and toolchain gating
- The original ten-rewrite threshold has been satisfied and the active GitHub estate now exists.
- The next-20 deterministic first tranche is 20/20 locally validated, but deterministic phase completion is not full program completion.
- Further widening and provider rollout remain governed by per-repo validation, security hardening, and the guarded manager release flow.
- Homebrew remains the default toolchain source where appropriate; Nix uses the official multi-user macOS installer and active repos carry normalized lock files.
- Docker remains authoritative where host-native toolchains are unreliable, including the documented Zig Darwin linker case.

## GitHub Free limitations
- Organization-level rulesets are not enforceable for `stakeholder-circus` on GitHub Free, so repo-level protection is the effective baseline.
- Branch protection and private-repo secret scanning are unavailable for `davidsupan/stakeholder-core` on the current plan. Vulnerability alerts and least-privilege Actions settings remain enabled there.
- If the organization upgrades later, repo-level protections should be promoted into organization rulesets without weakening existing gates.

## Transitional and local hardening state
- `davidsupan/java-stakeholder-private-archive` preserves the previous private Java repo.
- `stakeholder-java/java-stakeholder` is archived and read-only.
- Global git identity uses `david@supan.si`; SSH commit signing and signed tags are enabled.
- Repo-local hooks enforce provenance trailers and pre-push discipline.
