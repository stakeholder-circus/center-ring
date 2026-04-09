# GitHub governance state

## Topology
- `davidsupan/rust-stakeholder` is the only true GitHub fork of `giacomo-b/rust-stakeholder`.
- `davidsupan/stakeholder-core` is the private contract and fixture authority.
- `stakeholder-circus/center-ring` is the public umbrella meta-repo.
- Active language repos live under `stakeholder-circus/*-stakeholder` when they are ready for publication.

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

## Publication and toolchain gating
- Publication is held until at least 10 new full rewrites with tests are complete.
- The shared local toolchain baseline has advanced via Homebrew for `ghc`, `cabal-install`, `hlint`, `kotlin`, `gradle`, `opam`, `dune`, `nim`, `crystal`, `gleam`, `luarocks`, and `stylua`.
- `ocamlformat` is now installed locally via `opam`.
- `nix` remains the remaining major blocker, with any future repo-specific package-manager follow-ons handled as they arise.

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
