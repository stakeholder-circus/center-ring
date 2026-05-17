# Next 20 wave

- Status: local scaffold prep is complete; tranches A, B, and C are closed locally; tranche D has `d-stakeholder`, `rescript-stakeholder`, and `php-stakeholder` validated with `fortran-stakeholder` and `bash-stakeholder` still pending.
- Publication dependency: GitHub authentication is available, but publication is intentionally gated through `stakeholder release ... --execute` after validation and CI checks.
- Selected 20 repos are prepared locally with no upstream tracking.
- Toolchain proofs are closed for `typescript`, `rescript`, `clojure`, `powershell`, `julia`, `r`, `tcl`, `d`, and `php`.
- Local tranche validations have landed for `ocaml-stakeholder`, `typescript-stakeholder`, `ruby-stakeholder`, `erlang-stakeholder`, `scala-stakeholder`, `clojure-stakeholder`, `c-stakeholder`, `cpp-stakeholder`, `powershell-stakeholder`, `perl-stakeholder`, `groovy-stakeholder`, `vbnet-stakeholder`, `julia-stakeholder`, `r-stakeholder`, `tcl-stakeholder`, `d-stakeholder`, `rescript-stakeholder`, and `php-stakeholder`.

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

- `ocaml-stakeholder`: `built-in` (implemented-local-validated)
- `typescript-stakeholder`: `repo-local-pnpm` (implemented-local-validated)
- `ruby-stakeholder`: `built-in-homebrew` (implemented-local-validated)
- `erlang-stakeholder`: `built-in` (implemented-local-validated)
- `scala-stakeholder`: `built-in` (implemented-local-validated)
- `clojure-stakeholder`: `brew` (implemented-local-validated)
- `c-stakeholder`: `built-in` (implemented-local-validated)
- `cpp-stakeholder`: `built-in` (implemented-local-validated)
- `powershell-stakeholder`: `built-in-plus-module` (implemented-local-validated)
- `perl-stakeholder`: `built-in` (implemented-local-validated)
- `groovy-stakeholder`: `built-in` (implemented-local-validated)
- `vbnet-stakeholder`: `built-in-dotnet10` (implemented-local-validated)
- `julia-stakeholder`: `brew` (implemented-local-validated)
- `r-stakeholder`: `brew` (implemented-local-validated)
- `tcl-stakeholder`: `brew` (implemented-local-validated)
- `d-stakeholder`: `brew` (implemented-local-validated)
- `rescript-stakeholder`: `repo-local-pnpm` (implemented-local-validated)
- `fortran-stakeholder`: `built-in` (scaffold-ready-local-only)
- `bash-stakeholder`: `built-in` (scaffold-ready-local-only)
- `php-stakeholder`: `brew` (implemented-local-validated)

## Current blockers
- `fortran-stakeholder` and `bash-stakeholder` still need deterministic first-tranche implementation and native plus Docker validation.
- Publication is no longer blocked by local `gh` authentication, but it remains intentionally gated through `stakeholder release ... --execute` after repo-local validation, remote/CI evidence, and required-check decisions.
- Full live-provider/runtime support remains deferred to the later provider rollout wave.
