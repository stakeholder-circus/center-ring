# Stakeholder Job Status

Last updated: 2026-04-14 CEST
Owner: Codex agent

## Current status

- Program state: publication-governance wave; the phase/program completeness model is authoritative, `rust-stakeholder`, `javascript-stakeholder`, and `java-stakeholder` are the active live-provider/runtime lanes, and the locally validated wider-matrix set now includes `fsharp-stakeholder`, `zig-stakeholder`, `haskell-stakeholder`, `kotlin-stakeholder`, `elixir-stakeholder`, `nim-stakeholder`, `crystal-stakeholder`, `lua-stakeholder`, `dart-stakeholder`, and `gleam-stakeholder`.
- Completed in this slice:
  - moved the former workspace-root summary docs into tracked summary files under `stakeholder-core` and mirrored copies under `center-ring`
  - documented the workspace-root artifact policy, clarified default-branch reporting in the rewrite matrix, and normalized Rust docs metadata while keeping the Rust deterministic runtime unchanged
  - recut the canonical program target so Rust is no longer treated as permanently frozen and must also close the live-provider/runtime gap
  - reconciled canonical and repo-local provider-lane docs/status so Java and JavaScript now read as active in-progress live-provider lanes rather than closed sidecars or permanently complete exceptions
  - validated the Rust guarded live-provider lane locally with `cargo fmt --check`, `cargo test`, `--list-values`, `local-demo`, and orphan experimental flag fail-fast checks, and fixed the Rust config wiring issues that blocked the first pass
  - normalized follower README/GAPS wording in `.NET`, Go, Python, and Swift so those repos read as validated baselines with an open future live-provider lane rather than closed follower endpoints
  - stabilized repo-local status/toolchain wording across the validated wider-matrix repos so they consistently read as publication-held and reflect the installed Nix state
  - validated `lua-stakeholder` natively and through Docker, making it the eighth validated wider-matrix repo and shifting the next readiness-first tranche to `dart-stakeholder`
  - validated `dart-stakeholder` natively, through Docker, and through `nix run .#check`, making it the ninth validated wider-matrix repo and shifting the next readiness-first tranche to `gleam-stakeholder`
  - validated `gleam-stakeholder` natively, through Docker, and through `nix run .#check`, making it the tenth validated wider-matrix repo and closing the widening threshold
  - validated `scala-stakeholder` natively and through Docker, closing tranche A of the next-20 deterministic wave and promoting tranche B to the next active local lane
  - completed native validation for `clojure-stakeholder`; Docker validation remains blocked by the unavailable local Docker daemon
- Open in this slice:
  - execute the batch publication/governance wave for the ten validated wider-matrix repos once org access and authenticated tooling are available
  - run `clojure-stakeholder` Docker validation when Docker is available, then continue tranche B with `c-stakeholder`, `cpp-stakeholder`, `powershell-stakeholder`, and `perl-stakeholder`
  - keep hardening the API-backed and consumer-session live-provider/runtime paths across `rust-stakeholder`, `javascript-stakeholder`, and `java-stakeholder`
  - bind exact GitHub required-check contexts only after the first stable remote CI pass exists
  - keep `flake.lock` normalized as additional repos enter the active set after the publication wave

## Current blockers

- The ten-rewrite threshold is satisfied, but the publication/governance wave has not yet been executed.
- `nix` is installed locally through the official multi-user macOS installer.
- `flake.lock` is normalized across the active repo set; `zig-stakeholder` and `haskell-stakeholder` intentionally carry a second lock variant because their flakes depend on `flake-utils`.
- Tranche A of the next-20 deterministic wave is closed locally through `scala-stakeholder`; tranche B is next while publication remains externally blocked.

## Immediate next actions

1. Run the blocked Docker validation for `clojure-stakeholder` when Docker is available, then promote it to fully validated.
2. Resume the publication/governance wave for `fsharp-stakeholder`, `zig-stakeholder`, `haskell-stakeholder`, `kotlin-stakeholder`, `elixir-stakeholder`, `nim-stakeholder`, `crystal-stakeholder`, `lua-stakeholder`, `dart-stakeholder`, and `gleam-stakeholder` as soon as GitHub org access and authenticated tooling are available.
3. Keep hardening the API-backed and consumer-session live-provider/runtime paths across `rust-stakeholder`, `javascript-stakeholder`, and `java-stakeholder`.
