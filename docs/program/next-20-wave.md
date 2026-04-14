# Next 20 wave

- Status: local scaffold prep and bounded toolchain proofs are complete; tranche A is in progress with `ocaml`, `typescript`, `ruby`, and `erlang` already validated locally
- Publication dependency: current publication/governance wave is blocked on missing stakeholder-circus org access and unauthenticated gh
- Selected 20 repos are prepared locally with no upstream tracking
- Toolchain proofs are closed for `typescript`, `rescript`, `clojure`, `powershell`, `julia`, `r`, `tcl`, `d`, and `php`
- Local tranche validations already landed for `ocaml-stakeholder`, `typescript-stakeholder`, `ruby-stakeholder`, and `erlang-stakeholder`

## Tranches
### Tranche A

- `ocaml-stakeholder`
- `typescript-stakeholder`
- `ruby-stakeholder`
- `erlang-stakeholder`
- `scala-stakeholder`

### Tranche B

- `clojure-stakeholder`
- `c-stakeholder`
- `cpp-stakeholder`
- `powershell-stakeholder`
- `perl-stakeholder`

### Tranche C

- `groovy-stakeholder`
- `vbnet-stakeholder`
- `julia-stakeholder`
- `r-stakeholder`
- `tcl-stakeholder`

### Tranche D

- `d-stakeholder`
- `rescript-stakeholder`
- `fortran-stakeholder`
- `bash-stakeholder`
- `php-stakeholder`

## Reserves

- `objective-c-stakeholder`: Use Xcode clang and Foundation tooling; first reserve.
- `v-stakeholder`: Install via Brew vlang if needed.
- `common-lisp-stakeholder`: Use existing clisp or upgrade to sbcl if promoted.
- `ada-stakeholder`: Do not auto-promote on this machine; no workable GNAT path is confirmed.

## Toolchain sources

- `ocaml-stakeholder`: `built-in`
- `typescript-stakeholder`: `repo-local-pnpm`
- `ruby-stakeholder`: `built-in-homebrew`
- `erlang-stakeholder`: `built-in`
- `scala-stakeholder`: `built-in`
- `clojure-stakeholder`: `brew`
- `c-stakeholder`: `built-in`
- `cpp-stakeholder`: `built-in`
- `powershell-stakeholder`: `built-in-plus-module`
- `perl-stakeholder`: `built-in`
- `groovy-stakeholder`: `built-in`
- `vbnet-stakeholder`: `built-in-dotnet10`
- `julia-stakeholder`: `brew`
- `r-stakeholder`: `brew`
- `tcl-stakeholder`: `brew`
- `d-stakeholder`: `brew`
- `rescript-stakeholder`: `repo-local-pnpm`
- `fortran-stakeholder`: `built-in`
- `bash-stakeholder`: `built-in`
- `php-stakeholder`: `repair-brew`

## Current blockers
- `stakeholder-circus` org access is not available via the GitHub connector in this environment.
- `gh` is installed but unauthenticated, so remote creation is blocked.
- Publication remains the only external blocker; local tranche-A implementation is proceeding in parallel.
