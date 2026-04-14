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
| `bash-stakeholder` | `scaffold-ready-local-only` | `complete` | 100 | `selected-next20-scaffold` | 12 | 12 | 3 | `main` |
| `c-stakeholder` | `scaffold-ready-local-only` | `complete` | 100 | `selected-next20-scaffold` | 12 | 12 | 3 | `main` |
| `center-ring` | `mirrored-governance-and-workflow-baseline` | `complete` | 100 | `mirror-and-governance-baseline-active` | 82 | 82 | 76 | `main` |
| `clojure-stakeholder` | `scaffold-ready-local-only` | `complete` | 100 | `selected-next20-scaffold` | 12 | 12 | 3 | `main` |
| `cpp-stakeholder` | `scaffold-ready-local-only` | `complete` | 100 | `selected-next20-scaffold` | 12 | 12 | 3 | `main` |
| `crystal-stakeholder` | `native-and-docker-validated-wider-matrix` | `complete` | 100 | `publication-held` | 58 | 58 | 54 | `main` |
| `d-stakeholder` | `scaffold-ready-local-only` | `complete` | 100 | `selected-next20-scaffold` | 12 | 12 | 3 | `main` |
| `dart-stakeholder` | `native-and-docker-validated-wider-matrix` | `complete` | 100 | `publication-held` | 58 | 58 | 54 | `main` |
| `dotnet-stakeholder` | `validated-follower-modern-core-baseline` | `complete` | 100 | `follower-modern-core-validated` | 58 | 58 | 52 | `main` |
| `elixir-stakeholder` | `native-and-docker-validated-wider-matrix` | `complete` | 100 | `publication-held` | 58 | 58 | 54 | `main` |
| `erlang-stakeholder` | `scaffold-ready-local-only` | `complete` | 100 | `selected-next20-scaffold` | 12 | 12 | 3 | `main` |
| `fortran-stakeholder` | `scaffold-ready-local-only` | `complete` | 100 | `selected-next20-scaffold` | 12 | 12 | 3 | `main` |
| `fsharp-stakeholder` | `first-push-ready-wider-matrix` | `complete` | 100 | `publication-held` | 54 | 54 | 48 | `main` |
| `gleam-stakeholder` | `native-and-docker-validated-wider-matrix` | `complete` | 100 | `publication-held` | 58 | 58 | 54 | `main` |
| `go-stakeholder` | `validated-follower-modern-core-baseline` | `complete` | 100 | `follower-modern-core-validated` | 58 | 58 | 52 | `main` |
| `groovy-stakeholder` | `scaffold-ready-local-only` | `complete` | 100 | `selected-next20-scaffold` | 12 | 12 | 3 | `main` |
| `haskell-stakeholder` | `native-and-docker-validated-wider-matrix` | `complete` | 100 | `publication-held` | 58 | 58 | 54 | `main` |
| `java-stakeholder` | `co-equal-live-provider-runtime-lane` | `in-progress` | 88 | `full-generator-and-live-provider-target` | 96 | 96 | 92 | `main` |
| `javascript-stakeholder` | `live-provider-runtime-and-web-terminal-lane` | `in-progress` | 84 | `full-generator-and-live-provider-target` | 82 | 82 | 78 | `main` |
| `julia-stakeholder` | `scaffold-ready-local-only` | `complete` | 100 | `selected-next20-scaffold` | 12 | 12 | 3 | `main` |
| `kotlin-stakeholder` | `native-and-docker-validated-wider-matrix` | `complete` | 100 | `publication-held` | 58 | 58 | 54 | `main` |
| `lua-stakeholder` | `native-and-docker-validated-wider-matrix` | `complete` | 100 | `publication-held` | 58 | 58 | 54 | `main` |
| `nim-stakeholder` | `native-and-docker-validated-wider-matrix` | `complete` | 100 | `publication-held` | 58 | 58 | 54 | `main` |
| `ocaml-stakeholder` | `scaffold-ready-local-only` | `complete` | 100 | `selected-next20-scaffold` | 12 | 12 | 3 | `main` |
| `perl-stakeholder` | `scaffold-ready-local-only` | `complete` | 100 | `selected-next20-scaffold` | 12 | 12 | 3 | `main` |
| `php-stakeholder` | `scaffold-ready-local-only` | `complete` | 100 | `selected-next20-scaffold` | 12 | 12 | 3 | `main` |
| `powershell-stakeholder` | `scaffold-ready-local-only` | `complete` | 100 | `selected-next20-scaffold` | 12 | 12 | 3 | `main` |
| `python-stakeholder` | `validated-follower-modern-core-baseline` | `complete` | 100 | `follower-modern-core-validated` | 58 | 58 | 52 | `main` |
| `r-stakeholder` | `scaffold-ready-local-only` | `complete` | 100 | `selected-next20-scaffold` | 12 | 12 | 3 | `main` |
| `rescript-stakeholder` | `scaffold-ready-local-only` | `complete` | 100 | `selected-next20-scaffold` | 12 | 12 | 3 | `main` |
| `ruby-stakeholder` | `scaffold-ready-local-only` | `complete` | 100 | `selected-next20-scaffold` | 12 | 12 | 3 | `main` |
| `rust-stakeholder` | `canonical-live-provider-runtime-lane` | `in-progress` | 78 | `canonical-full-generator-and-live-provider-target` | 92 | 88 | 84 | `master` |
| `scala-stakeholder` | `scaffold-ready-local-only` | `complete` | 100 | `selected-next20-scaffold` | 12 | 12 | 3 | `main` |
| `stakeholder-core` | `canonical-docs-and-contract-baseline` | `complete` | 100 | `canonical-docs-and-contract-authority` | 90 | 90 | 88 | `main` |
| `swift-stakeholder` | `validated-follower-modern-core-baseline` | `complete` | 100 | `follower-modern-core-validated` | 58 | 58 | 52 | `main` |
| `tcl-stakeholder` | `scaffold-ready-local-only` | `complete` | 100 | `selected-next20-scaffold` | 12 | 12 | 3 | `main` |
| `typescript-stakeholder` | `scaffold-ready-local-only` | `complete` | 100 | `selected-next20-scaffold` | 12 | 12 | 3 | `main` |
| `vbnet-stakeholder` | `scaffold-ready-local-only` | `complete` | 100 | `selected-next20-scaffold` | 12 | 12 | 3 | `main` |
| `zeta-stakeholder` | `research-spike-local-only` | `not-started` | 0 | `spike-only` | 10 | 10 | 1 | `main` |
| `zig-stakeholder` | `docker-validated-wider-matrix` | `complete` | 100 | `publication-held` | 26 | 26 | 18 | `main` |

## Publication guardrail
- The managed default branch may differ from the active local baseline branch.
- The current ten validated wider-matrix repos remain publication-held until stakeholder-circus org access and authenticated GitHub tooling are available.
- The next-20 scaffold baseline is now prepared locally; implementation begins only after the publication/governance block is resolved or explicitly bypassed.
- Full live-provider/runtime support remains the required second-pass wave for every language.

