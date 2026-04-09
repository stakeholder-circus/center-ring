# Repo sequencing

Last updated: 2026-04-09 21:47 CEST

## Frozen anchors
- `rust-stakeholder` stays the canonical baseline on `master`.
- `stakeholder-core` stays the canonical status-model authority on `main`.
- `center-ring` stays the mirrored governance/status baseline on `main`.
- `javascript-stakeholder` stays in the provider and web-terminal sidecar lane and is validated locally through native Node checks plus Docker sidecar smokes.
- `java-stakeholder` is now a co-equal provider-runtime lane in canonical planning and is implemented and Docker-validated locally.

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

Current state by repo:
- `fsharp-stakeholder`: full classic-six plus full modern-core implemented locally; local first-push bar met; publication remains held until the 10-rewrite threshold is met.
- `zig-stakeholder`: local full classic-six plus modern-core implementation tranche; Docker validation lane passed locally; host-native `zig build` and `zig test` remain environment-blocked by a Homebrew Zig Darwin linker issue on this workstation.
- `haskell-stakeholder`: full classic-six plus full modern-core implemented locally; native validation passed through `ghcup run --ghc 9.6.7`; Docker image build, in-image test, and runtime smokes passed; publication remains held until the 10-rewrite threshold is met.
- `kotlin-stakeholder`: full classic-six plus full modern-core implemented locally; native Gradle validation and Docker runtime smokes passed; publication remains held until the 10-rewrite threshold is met.
- `elixir-stakeholder`: full classic-six plus full modern-core implemented locally; native Elixir validation and Docker runtime smokes passed; publication remains held until the 10-rewrite threshold is met.

## Ready-first queue after the active wave
After `elixir-stakeholder`, the queue remains:
1. `nim-stakeholder`
2. `crystal-stakeholder`
3. `lua-stakeholder`
4. `dart-stakeholder`
5. `gleam-stakeholder`
6. `ocaml-stakeholder`

## Sidecar lane
`javascript-stakeholder` continues independently with:
- live-provider runtime
- encrypted local state
- local browser terminal surface
- consumer-session capture
- native Node validation and Docker sidecar smoke coverage

It does not become the parity template for follower deterministic depth.

## Zeta spike lane
`zeta-stakeholder` is tracked separately from the normal parity queue.
- It stays spike-only until toolchain viability, packaging, and deterministic fixture compatibility are proven.
- It is not allowed to block the parity queue.

## Publication rules
- No wider-matrix repo gets a remote or first push before it is minimally real.
- `fsharp-stakeholder`, `zig-stakeholder`, `haskell-stakeholder`, `kotlin-stakeholder`, and `elixir-stakeholder` remain unpublished because publication is intentionally deferred until at least 10 new full rewrites with tests are complete.
- Exact GitHub required checks are bound only after the first stable CI pass on the pushed repo.
- No provider-runtime implementation work is added outside `javascript-stakeholder` and `java-stakeholder` during this tranche.
