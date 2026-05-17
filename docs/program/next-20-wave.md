# Next 20 wave

- Status: local scaffold prep is complete and all four next-20 deterministic tranches are closed locally.
- Result: 20/20 selected next-20 repos have native plus Docker deterministic first-tranche validation evidence.
- Publication dependency: GitHub authentication is available, but publication is intentionally gated through `stakeholder release ... --execute` after validation and CI checks.
- Selected 20 repos are prepared locally with no upstream tracking.
- Full live-provider/runtime support remains deferred to the later provider rollout wave.

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
- `fortran-stakeholder`: `built-in` (implemented-local-validated)
- `bash-stakeholder`: `built-in` (implemented-local-validated)
- `php-stakeholder`: `brew` (implemented-local-validated)

## Current blockers
- No next-20 deterministic first-tranche implementation blocker remains.
- Publication is no longer blocked by local `gh` authentication, but it remains intentionally gated through `stakeholder release ... --execute` after repo-local validation, remote/CI evidence, and required-check decisions.
- Full live-provider/runtime support remains deferred to the later provider rollout wave.
