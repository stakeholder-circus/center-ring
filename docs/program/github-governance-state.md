# GitHub governance state

## Topology
- `davidsupan/rust-stakeholder` is the only true GitHub fork of `giacomo-b/rust-stakeholder`.
- `davidsupan/stakeholder-core` is the private contract and fixture authority.
- `stakeholder-circus/center-ring` is the public umbrella meta-repo.
- Active language repos live under `stakeholder-circus/*-stakeholder` when they are ready for publication.

## 2026-06-07 GitHub audit state
- Local stakeholder workspace repos counted: 60.
- Active GitHub stakeholder repos counted: 60.
- Additional non-active archive repo counted separately: `davidsupan/java-stakeholder-private-archive`.
- Canonical planned language horizon remains 250 total languages.
- Missing active upstream repos were closed during this audit wave: 51 `stakeholder-circus/*` repos were created and pushed from clean local commits with their CI workflow baselines.
- Latest serial GitHub Actions audit found 60 active repos, 22 repos with all latest workflows complete and green, 0 repos with latest completed non-success workflows, and 191 latest workflows still pending in the GitHub Actions queue.
- Pending workflows are not treated as passing evidence; they remain an open audit item until GitHub completes them.
- Repo-local CI cleanup already applied in this wave includes actionlint workflow repair, unsupported CodeQL lane removal or note workflows, stale non-Rust Cargo Dependabot lane removal, Gleam CI toolchain setup, Crystal Docker-smoke YAML repair, and private-repo dependency-review guarding for `stakeholder-core`.
- Active PR cleanup already performed in this wave includes merging green Dependabot PRs, closing obsolete empty-diff CodeQL PRs, and closing the incompatible `.NET` runtime 10 Docker PR because the app still targets `net8.0`.
- Remaining open PR classes are dirty/conflicted Dependabot branches waiting on Dependabot rebase/recreate, and two intentional fix PRs waiting on GitHub queue completion: `stakeholder-circus/dotnet-stakeholder#13` and `stakeholder-circus/go-stakeholder#7`.

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
- `stakeholder-core` and `center-ring` keep MIT as the intended license family, but any standalone neutral contributors notice remains deferred to a later authorship-review tranche.

## Branch and repo policy
- `rust-stakeholder` stays on `master` to track upstream cleanly.
- Rust is still the canonical source of truth, but it is no longer treated as permanently frozen because it must also reach the full live-provider/runtime surface.
- Managed language repos and `center-ring` use `main`.
- Repo-level protections already applied on GitHub Free:
  - PRs required before merge
  - conversation resolution required
  - signed commits required
  - linear history required
  - squash merge only
  - no force pushes
  - no branch deletion
  - no admin bypass
- Exact required status checks are deferred until stable GitHub check contexts exist after the first post-publication CI pass.
- Planned first-push checks for `fsharp-stakeholder`:
  - `ci-native`
  - `docker-smoke`
  - `actionlint`
  - `dependency-review`
- Source CodeQL is intentionally not enabled for F# in this tranche because GitHub does not currently list F# as a supported CodeQL source language.

## Workspace-root artifact and routing policy
- `/Users/davidsupan/shareholder` is a coordination workspace, not a git repo.
- Workspace-level summaries are tracked canonically under `stakeholder-core/status/` and `stakeholder-core/docs/program/`, then mirrored under `center-ring/status/` and `center-ring/docs/program/`.
- Repo-level `STATUS.md` files remain repo-scoped and must not be used as a substitute for workspace summaries.
- `.migration/` is retained as intentional workspace audit material and stays outside repo sprint commits unless a specific artifact is explicitly promoted into a tracked repo.
- Transient root artifacts such as `erl_crash.dump` remain untracked workspace noise and must stay out of repo commits and baseline captures.

## Publication and toolchain gating
- Publication is held until at least 10 new full rewrites with tests are complete.
- The shared local toolchain baseline has advanced via Homebrew for `ghc`, `cabal-install`, `hlint`, `kotlin`, `gradle`, `opam`, `dune`, `nim`, `crystal`, `gleam`, `luarocks`, and `stylua`.
- `ocamlformat` is now installed locally via `opam`.
- `nix` is installed through the official multi-user macOS path, and `flake.lock` is normalized across the active repo set.
- Future repo-specific package-manager follow-ons are handled as each language tranche is promoted into the validated set.
- Rust already carries the expanded deterministic generator surface and canonical experimental provider models; the current Rust-specific gap is guarded live-provider runtime wiring rather than generator-family coverage.

## GitHub Free limitation
- Organization-level rulesets for `stakeholder-circus` are not enforceable on GitHub Free.
- The effective baseline is therefore repo-level protection, not org-wide policy enforcement.
- If the org upgrades to GitHub Team later, the repo-level baseline should be promoted into org rulesets rather than replaced with a weaker policy.

## Transitional cleanup already performed
- `davidsupan/java-stakeholder-private-archive` preserves the previous private Java repo.
- `stakeholder-java/java-stakeholder` is archived and remains read-only as a transitional artifact.

## Local hardening baseline
- Global git identity uses `david@supan.si`.
- SSH commit signing is configured and registered in GitHub.
- Signed commits and signed tags are enabled globally.
- Repo-local hooks enforce provenance trailers and pre-push discipline.
