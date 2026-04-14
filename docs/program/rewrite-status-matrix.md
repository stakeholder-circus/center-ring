# Rewrite status matrix

Last updated: 2026-04-14 CEST

## Meaning
- `phaseTarget`: the committed role that the repo is currently expected to complete.
- `phaseState`: whether that committed role is complete, in progress, or not started.
- `phasePercent`: coarse phase completeness against the committed role.
- `programState`: the repo's eventual end-state in the wider rewrite program.
- `programPercent`: coarse eventual-program completeness.
- `rewritePercent` and `functionalityPercent` are retained as legacy coarse measures for continuity.

## Current matrix
| Repo | Phase target | Phase state | Phase % | Program state | Program % | Legacy rewrite % | Legacy functionality % | Default branch |
|---|---|---|---:|---|---:|---:|---:|---|
| `stakeholder-core` | `canonical-docs-and-contract-baseline` | `complete` | 100 | `canonical-docs-and-contract-authority` | 90 | 90 | 88 | `main` |
| `center-ring` | `mirrored-governance-and-workflow-baseline` | `complete` | 100 | `mirror-and-governance-baseline-active` | 82 | 82 | 76 | `main` |
| `rust-stakeholder` | `canonical-live-provider-runtime-lane` | `in-progress` | 78 | `canonical-full-generator-and-live-provider-target` | 92 | 88 | 84 | `master` |
| `java-stakeholder` | `co-equal-live-provider-runtime-lane` | `in-progress` | 88 | `full-generator-and-live-provider-target` | 96 | 98 | 94 | `main` |
| `javascript-stakeholder` | `live-provider-runtime-and-web-terminal-lane` | `in-progress` | 84 | `full-generator-and-live-provider-target` | 82 | 82 | 78 | `main` |
| `dotnet-stakeholder` | `validated-follower-modern-core-baseline` | `complete` | 100 | `follower-modern-core-validated` | 58 | 58 | 52 | `main` |
| `go-stakeholder` | `validated-follower-modern-core-baseline` | `complete` | 100 | `follower-modern-core-validated` | 58 | 58 | 52 | `main` |
| `python-stakeholder` | `validated-follower-modern-core-baseline` | `complete` | 100 | `follower-modern-core-validated` | 58 | 58 | 52 | `main` |
| `swift-stakeholder` | `validated-follower-modern-core-baseline` | `complete` | 100 | `follower-modern-core-validated` | 58 | 58 | 52 | `main` |
| `fsharp-stakeholder` | `first-push-ready-wider-matrix` | `complete` | 100 | `publication-held` | 54 | 54 | 48 | `main` |
| `zig-stakeholder` | `docker-validated-wider-matrix` | `complete` | 100 | `publication-held` | 26 | 26 | 18 | `main` |
| `haskell-stakeholder` | `native-and-docker-validated-wider-matrix` | `complete` | 100 | `publication-held` | 58 | 58 | 54 | `main` |
| `kotlin-stakeholder` | `native-and-docker-validated-wider-matrix` | `complete` | 100 | `publication-held` | 58 | 58 | 54 | `main` |
| `elixir-stakeholder` | `native-and-docker-validated-wider-matrix` | `complete` | 100 | `publication-held` | 58 | 58 | 54 | `main` |
| `nim-stakeholder` | `native-and-docker-validated-wider-matrix` | `complete` | 100 | `publication-held` | 58 | 58 | 54 | `main` |
| `ocaml-stakeholder` | `scaffold-ready-local-only` | `not-started` | 0 | `local-only` | 12 | 12 | 3 | `main` |
| `crystal-stakeholder` | `native-and-docker-validated-wider-matrix` | `complete` | 100 | `publication-held` | 58 | 58 | 54 | `main` |
| `dart-stakeholder` | `native-and-docker-validated-wider-matrix` | `complete` | 100 | `publication-held` | 58 | 58 | 54 | `main` |
| `lua-stakeholder` | `native-and-docker-validated-wider-matrix` | `complete` | 100 | `publication-held` | 58 | 58 | 54 | `main` |
| `gleam-stakeholder` | `native-and-docker-validated-wider-matrix` | `complete` | 100 | `publication-held` | 58 | 58 | 54 | `main` |
| `zeta-stakeholder` | `research-spike-local-only` | `not-started` | 0 | `spike-only` | 10 | 10 | 1 | `main` |

## Publication guardrail
- The `Default branch` column records the managed default branch; current local sprint work happens on repo-specific `codex/baseline-2026-04-13-*` branches.
- The first ten validated wider-matrix repos now meet the widening threshold.
- Widening pauses here; the next required work is the publication/governance wave for `fsharp-stakeholder`, `zig-stakeholder`, `haskell-stakeholder`, `kotlin-stakeholder`, `elixir-stakeholder`, `nim-stakeholder`, `crystal-stakeholder`, `lua-stakeholder`, `dart-stakeholder`, and `gleam-stakeholder`.
- Rust, JavaScript, and Java are the active live-provider/runtime lanes in canonical planning; deterministic CI remains provider-free.
- The local toolchain baseline has advanced via Homebrew for the shared language/tooling set, while `ghcup` now pins native Haskell validation and `nix` is installed.
- `ocamlformat` is installed locally via `opam`, and `flake.lock` is normalized across the active repo set with the intentional second lock shape preserved in `zig-stakeholder` and `haskell-stakeholder`.
- Exact GitHub required-check binding still waits for stable remote CI contexts after the first push.
- `zig-stakeholder` remains Docker-validated locally but host-native Zig build/test stays environment-blocked on this workstation.
- Rust now has local validation evidence for the guarded live-provider lane through `cargo fmt --check`, `cargo test`, `--list-values`, `local-demo`, and orphan flag fail-fast; API-backed and consumer-session hardening remain open.
