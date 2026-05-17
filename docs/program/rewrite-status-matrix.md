# Rewrite status matrix

Last updated: 2026-05-17 CEST

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
| `bash-stakeholder` | `native-and-docker-validated-next20-deterministic-tranche` | `complete` | 100 | `deterministic-publication-held` | 58 | 58 | 54 | `main` |
| `c-stakeholder` | `native-and-docker-validated-next20-deterministic-tranche` | `complete` | 100 | `deterministic-publication-held` | 58 | 58 | 54 | `main` |
| `center-ring` | `mirrored-governance-and-workflow-baseline` | `complete` | 100 | `mirror-and-governance-baseline-active` | 82 | 82 | 76 | `main` |
| `clojure-stakeholder` | `native-and-docker-validated-next20-deterministic-tranche` | `complete` | 100 | `deterministic-publication-held` | 58 | 58 | 54 | `main` |
| `cpp-stakeholder` | `native-and-docker-validated-next20-deterministic-tranche` | `complete` | 100 | `deterministic-publication-held` | 58 | 58 | 54 | `main` |
| `crystal-stakeholder` | `native-and-docker-validated-wider-matrix` | `complete` | 100 | `publication-held` | 58 | 58 | 54 | `main` |
| `d-stakeholder` | `native-and-docker-validated-next20-deterministic-tranche` | `complete` | 100 | `deterministic-publication-held` | 58 | 58 | 54 | `main` |
| `dart-stakeholder` | `native-and-docker-validated-wider-matrix` | `complete` | 100 | `publication-held` | 58 | 58 | 54 | `main` |
| `dotnet-stakeholder` | `validated-follower-modern-core-baseline` | `complete` | 100 | `follower-modern-core-validated` | 58 | 58 | 52 | `main` |
| `elixir-stakeholder` | `native-and-docker-validated-wider-matrix` | `complete` | 100 | `publication-held` | 58 | 58 | 54 | `main` |
| `erlang-stakeholder` | `native-and-docker-validated-next20-deterministic-tranche` | `complete` | 100 | `deterministic-publication-held` | 58 | 58 | 54 | `main` |
| `fortran-stakeholder` | `native-and-docker-validated-next20-deterministic-tranche` | `complete` | 100 | `deterministic-publication-held` | 58 | 58 | 54 | `main` |
| `fsharp-stakeholder` | `first-push-ready-wider-matrix` | `complete` | 100 | `publication-held` | 54 | 54 | 48 | `main` |
| `gleam-stakeholder` | `native-and-docker-validated-wider-matrix` | `complete` | 100 | `publication-held` | 58 | 58 | 54 | `main` |
| `go-stakeholder` | `validated-follower-modern-core-baseline` | `complete` | 100 | `follower-modern-core-validated` | 58 | 58 | 52 | `main` |
| `groovy-stakeholder` | `native-and-docker-validated-next20-deterministic-tranche` | `complete` | 100 | `deterministic-publication-held` | 58 | 58 | 54 | `main` |
| `haskell-stakeholder` | `native-and-docker-validated-wider-matrix` | `complete` | 100 | `publication-held` | 58 | 58 | 54 | `main` |
| `java-stakeholder` | `co-equal-live-provider-runtime-lane` | `in-progress` | 88 | `full-generator-and-live-provider-target` | 96 | 96 | 92 | `main` |
| `javascript-stakeholder` | `live-provider-runtime-and-web-terminal-lane` | `in-progress` | 84 | `full-generator-and-live-provider-target` | 82 | 82 | 78 | `main` |
| `julia-stakeholder` | `native-and-docker-validated-next20-deterministic-tranche` | `complete` | 100 | `deterministic-publication-held` | 58 | 58 | 54 | `main` |
| `kotlin-stakeholder` | `native-and-docker-validated-wider-matrix` | `complete` | 100 | `publication-held` | 58 | 58 | 54 | `main` |
| `lua-stakeholder` | `native-and-docker-validated-wider-matrix` | `complete` | 100 | `publication-held` | 58 | 58 | 54 | `main` |
| `nim-stakeholder` | `native-and-docker-validated-wider-matrix` | `complete` | 100 | `publication-held` | 58 | 58 | 54 | `main` |
| `ocaml-stakeholder` | `native-and-docker-validated-next20-deterministic-tranche` | `complete` | 100 | `deterministic-publication-held` | 58 | 58 | 54 | `main` |
| `perl-stakeholder` | `native-and-docker-validated-next20-deterministic-tranche` | `complete` | 100 | `deterministic-publication-held` | 58 | 58 | 54 | `main` |
| `php-stakeholder` | `native-and-docker-validated-next20-deterministic-tranche` | `complete` | 100 | `deterministic-publication-held` | 58 | 58 | 54 | `main` |
| `powershell-stakeholder` | `native-and-docker-validated-next20-deterministic-tranche` | `complete` | 100 | `deterministic-publication-held` | 58 | 58 | 54 | `main` |
| `python-stakeholder` | `validated-follower-modern-core-baseline` | `complete` | 100 | `follower-modern-core-validated` | 58 | 58 | 52 | `main` |
| `r-stakeholder` | `native-and-docker-validated-next20-deterministic-tranche` | `complete` | 100 | `deterministic-publication-held` | 58 | 58 | 54 | `main` |
| `rescript-stakeholder` | `native-and-docker-validated-next20-deterministic-tranche` | `complete` | 100 | `deterministic-publication-held` | 58 | 58 | 54 | `main` |
| `ruby-stakeholder` | `native-and-docker-validated-next20-deterministic-tranche` | `complete` | 100 | `deterministic-publication-held` | 58 | 58 | 54 | `main` |
| `rust-stakeholder` | `canonical-live-provider-runtime-lane` | `in-progress` | 78 | `canonical-full-generator-and-live-provider-target` | 92 | 88 | 84 | `master` |
| `scala-stakeholder` | `native-and-docker-validated-next20-deterministic-tranche` | `complete` | 100 | `deterministic-publication-held` | 58 | 58 | 54 | `main` |
| `stakeholder-core` | `canonical-docs-and-contract-baseline` | `complete` | 100 | `canonical-docs-and-contract-authority` | 90 | 90 | 88 | `main` |
| `swift-stakeholder` | `validated-follower-modern-core-baseline` | `complete` | 100 | `follower-modern-core-validated` | 58 | 58 | 52 | `main` |
| `tcl-stakeholder` | `native-and-docker-validated-next20-deterministic-tranche` | `complete` | 100 | `deterministic-publication-held` | 58 | 58 | 54 | `main` |
| `typescript-stakeholder` | `native-and-docker-validated-next20-deterministic-tranche` | `complete` | 100 | `deterministic-publication-held` | 58 | 58 | 54 | `main` |
| `vbnet-stakeholder` | `native-and-docker-validated-next20-deterministic-tranche` | `complete` | 100 | `deterministic-publication-held` | 58 | 58 | 54 | `main` |
| `zeta-stakeholder` | `research-spike-local-only` | `not-started` | 0 | `spike-only` | 10 | 10 | 1 | `main` |
| `zig-stakeholder` | `docker-validated-wider-matrix` | `complete` | 100 | `publication-held` | 26 | 26 | 18 | `main` |

## Publication guardrail
- The managed default branch may differ from the active local baseline branch.
- The original ten validated wider-matrix repos remain publication-held while guarded remote publication and CI binding are executed deliberately.
- The next-20 local deterministic first-tranche sprint is now 20/20 locally validated.
- All publication mutation must go through `stakeholder release ... --execute`; read-only manager status, horizon, and feature commands are safe across `all`.
- Full live-provider/runtime support remains the required second-pass wave for every language.
