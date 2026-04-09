# Rewrite status matrix

Last updated: 2026-04-09 21:47 CEST

## Meaning
- `phaseTarget`: the committed role that the repo is currently expected to complete.
- `phaseState`: whether that committed role is complete, in progress, or not started.
- `phasePercent`: coarse phase completeness against the committed role.
- `programState`: the repo's eventual end-state in the wider rewrite program.
- `programPercent`: coarse eventual-program completeness.
- `rewritePercent` and `functionalityPercent` are retained as legacy coarse measures for continuity.

## Current matrix
| Repo | Phase target | Phase state | Phase % | Program state | Program % | Legacy rewrite % | Legacy functionality % | Branch |
|---|---|---|---:|---|---:|---:|---:|---|
| `stakeholder-core` | `canonical-docs-and-contract-baseline` | `complete` | 100 | `canonical-docs-and-contract-authority` | 90 | 90 | 88 | `main` |
| `center-ring` | `mirrored-governance-and-workflow-baseline` | `complete` | 100 | `mirror-and-governance-baseline-active` | 82 | 82 | 76 | `main` |
| `rust-stakeholder` | `canonical-runtime-baseline-frozen` | `complete` | 100 | `canonical-baseline-frozen` | 100 | 100 | 100 | `master` |
| `java-stakeholder` | `experimental-provider-lane` | `complete` | 100 | `co-equal-provider-runtime` | 98 | 98 | 94 | `main` |
| `javascript-stakeholder` | `provider-sidecar-baseline` | `complete` | 100 | `co-equal-provider-runtime` | 82 | 82 | 78 | `main` |
| `dotnet-stakeholder` | `validated-follower-modern-core-baseline` | `complete` | 100 | `follower-modern-core-validated` | 58 | 58 | 52 | `main` |
| `go-stakeholder` | `validated-follower-modern-core-baseline` | `complete` | 100 | `follower-modern-core-validated` | 58 | 58 | 52 | `main` |
| `python-stakeholder` | `validated-follower-modern-core-baseline` | `complete` | 100 | `follower-modern-core-validated` | 58 | 58 | 52 | `main` |
| `swift-stakeholder` | `validated-follower-modern-core-baseline` | `complete` | 100 | `follower-modern-core-validated` | 58 | 58 | 52 | `main` |
| `fsharp-stakeholder` | `first-push-ready-wider-matrix` | `complete` | 100 | `publication-held` | 54 | 54 | 48 | `main` |
| `zig-stakeholder` | `docker-validated-wider-matrix` | `complete` | 100 | `publication-held` | 26 | 26 | 18 | `main` |
| `haskell-stakeholder` | `native-and-docker-validated-wider-matrix` | `complete` | 100 | `publication-held` | 58 | 58 | 54 | `main` |
| `kotlin-stakeholder` | `native-and-docker-validated-wider-matrix` | `complete` | 100 | `publication-held` | 58 | 58 | 54 | `main` |
| `elixir-stakeholder` | `native-and-docker-validated-wider-matrix` | `complete` | 100 | `publication-held` | 58 | 58 | 54 | `main` |
| `ocaml-stakeholder` | `scaffold-ready-local-only` | `not-started` | 0 | `local-only` | 12 | 12 | 3 | `main` |
| `nim-stakeholder` | `scaffold-ready-local-only` | `not-started` | 0 | `local-only` | 12 | 12 | 3 | `main` |
| `crystal-stakeholder` | `scaffold-ready-local-only` | `not-started` | 0 | `local-only` | 12 | 12 | 3 | `main` |
| `dart-stakeholder` | `scaffold-ready-local-only` | `not-started` | 0 | `local-only` | 12 | 12 | 3 | `main` |
| `lua-stakeholder` | `scaffold-ready-local-only` | `not-started` | 0 | `local-only` | 12 | 12 | 3 | `main` |
| `gleam-stakeholder` | `scaffold-ready-local-only` | `not-started` | 0 | `local-only` | 12 | 12 | 3 | `main` |
| `zeta-stakeholder` | `research-spike-local-only` | `not-started` | 0 | `spike-only` | 10 | 10 | 1 | `main` |

## Publication guardrail
- Wider-matrix repos are intentionally local-only until they have meaningful implementation depth.
- `fsharp-stakeholder`, `zig-stakeholder`, `haskell-stakeholder`, `kotlin-stakeholder`, and `elixir-stakeholder` all meet their local technical validation bars, but publication remains intentionally deferred until at least 10 new full rewrites with tests are complete.
- JavaScript and Java are the co-equal provider-runtime lanes in canonical planning; deterministic CI remains provider-free.
- The local toolchain baseline has advanced via Homebrew for the shared language/tooling set, while `ghcup` now pins native Haskell validation and `nix` remains pending.
- `ocamlformat` is installed locally via `opam`, so `nix` remains the remaining major blocker, with any future repo-specific package-manager follow-ons handled as they arise.
- Exact GitHub required-check binding still waits for stable remote CI contexts after the first push.
- `zig-stakeholder` remains Docker-validated locally but host-native Zig build/test stays environment-blocked on this workstation.
