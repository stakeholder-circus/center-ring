# Repo sequencing

Last updated: 2026-04-14 CEST

## Frozen anchors
- `rust-stakeholder` stays the canonical source on `master`, but it is no longer treated as permanently frozen because it must also reach the full live-provider/runtime surface.
- `stakeholder-core` stays the canonical status-model authority on `main`.
- `center-ring` stays the mirrored governance/status baseline on `main`.
- `javascript-stakeholder` stays in the provider and web-terminal lane and is validated locally through native Node checks plus Docker sidecar smokes.
- `java-stakeholder` stays a co-equal provider-runtime lane in canonical planning and is implemented and Docker-validated locally.

## Closed validated follower lane
The follower `modern-core` lane is closed and validated in:
1. `dotnet-stakeholder`
2. `go-stakeholder`
3. `python-stakeholder`
4. `swift-stakeholder`

These repos remain the validated follower baseline for the wider matrix.

## Locally validated wider-matrix repos
The locally validated wider-matrix set is now:
1. `fsharp-stakeholder`
2. `zig-stakeholder`
3. `haskell-stakeholder`
4. `kotlin-stakeholder`
5. `elixir-stakeholder`
6. `nim-stakeholder`
7. `crystal-stakeholder`
8. `lua-stakeholder`
9. `dart-stakeholder`
10. `gleam-stakeholder`

Current state by repo:
- `fsharp-stakeholder`: full classic-six plus full modern-core implemented locally; local first-push bar met; publication remains held until the publication/governance wave opens the batch push step.
- `zig-stakeholder`: local full classic-six plus modern-core implementation tranche; Docker validation lane passed locally; host-native `zig build` and `zig test` remain environment-blocked by a Homebrew Zig Darwin linker issue on this workstation.
- `haskell-stakeholder`: full classic-six plus full modern-core implemented locally; native validation passed through `ghcup run --ghc 9.6.7`; Docker image build, in-image test, and runtime smokes passed.
- `kotlin-stakeholder`: full classic-six plus full modern-core implemented locally; native Gradle validation and Docker runtime smokes passed.
- `elixir-stakeholder`: full classic-six plus full modern-core implemented locally; native Elixir validation and Docker runtime smokes passed.
- `nim-stakeholder`: full classic-six plus full modern-core implemented locally; native Nim validation and Docker runtime smokes passed.
- `crystal-stakeholder`: full classic-six plus full modern-core implemented locally; native Crystal validation and Docker runtime smokes passed.
- `lua-stakeholder`: full classic-six plus full modern-core implemented locally; native Lua validation and Docker runtime smokes passed.
- `dart-stakeholder`: full classic-six plus full modern-core implemented locally; native Dart validation, executable build, Docker runtime smokes, `flake.lock`, and `nix run .#check` passed.
- `gleam-stakeholder`: full classic-six plus full modern-core implemented locally; native Gleam validation, Docker runtime smokes, `flake.lock`, and `nix run .#check` passed.

## Active publication/governance lane
The next mandatory wave is the batch publication/governance step for:
- `fsharp-stakeholder`
- `zig-stakeholder`
- `haskell-stakeholder`
- `kotlin-stakeholder`
- `elixir-stakeholder`
- `nim-stakeholder`
- `crystal-stakeholder`
- `lua-stakeholder`
- `dart-stakeholder`
- `gleam-stakeholder`

## Queue after the publication/governance wave
1. `ocaml-stakeholder`

## Active live-provider/runtime lane
The active provider-runtime closure lane now spans:
- `rust-stakeholder`: canonical source, expanded deterministic families already present, canonical experimental provider models already present, and guarded runtime wiring now validated locally for `--list-values`, `local-demo`, and orphan flag fail-fast; API-backed and consumer-session hardening remain open.
- `javascript-stakeholder`: active live-provider and web-terminal lane with explicit native plus Docker validation evidence.
- `java-stakeholder`: active JVM-native live-provider lane with Docker-validated local runtime support.

JavaScript and Java remain co-equal provider/runtime lanes today, but the broader program target is that every language eventually reaches the same full live-provider/runtime surface.

## Zeta spike lane
`zeta-stakeholder` is tracked separately from the normal parity queue.
- It stays spike-only until toolchain viability, packaging, and deterministic fixture compatibility are proven.
- It is not allowed to block the parity queue.

## Publication rules
- The ten-rewrite threshold is now met, so widening pauses here.
- The next required work is the publication/governance wave for the ten validated wider-matrix repos.
- Exact GitHub required checks are bound only after the first stable CI pass on the pushed repo.
- Provider-runtime implementation work remains explicitly active in `rust-stakeholder`, `javascript-stakeholder`, and `java-stakeholder` during this tranche.
