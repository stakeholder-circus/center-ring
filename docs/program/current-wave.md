# Current wave

Last updated: 2026-04-09 21:47 CEST
The active wave is `readiness-first-threshold-wave`. The phase/program completeness model remains authoritative, `javascript-stakeholder` and `java-stakeholder` remain the co-equal provider runtimes, the validated wider-matrix set now includes `elixir-stakeholder`, publication remains held until at least 10 new full rewrites with tests are complete, and the next repo queued for promotion is `nim-stakeholder`.

## Locked sequencing rules
- `rust-stakeholder` remains the canonical source of truth and stays frozen except for additive governance or status sync.
- `stakeholder-core` owns the canonical status-model migration and `center-ring` mirrors it.
- `javascript-stakeholder` and `java-stakeholder` are co-equal provider runtimes.
- The follower `modern-core` wave in `.NET`, Go, Python, and Swift is closed and validated.
- The validated wider-matrix set now includes `fsharp-stakeholder`, `zig-stakeholder`, `haskell-stakeholder`, `kotlin-stakeholder`, and `elixir-stakeholder`.
- Wider-matrix repos remain local-only until each is minimally real and the publication hold is explicitly lifted.

## Active implementation lane
The readiness-first threshold wave is focused on producing additional fully validated local rewrites without breaking the publication hold:
- `javascript-stakeholder` and `java-stakeholder`: keep the co-equal provider-runtime lanes phase-complete and provider-free in deterministic CI.
- `dotnet-stakeholder`, `go-stakeholder`, `python-stakeholder`, `swift-stakeholder`: remain the validated follower baseline.
- `fsharp-stakeholder`, `zig-stakeholder`, `haskell-stakeholder`, `kotlin-stakeholder`, `elixir-stakeholder`: remain the locally validated wider-matrix set held back only by the 10-rewrite publication guardrail.
- `nim-stakeholder`: next readiness-first full rewrite tranche.

## Ready-first queue after the active wave
The next repos are promoted in this order:
1. `nim-stakeholder`
2. `crystal-stakeholder`
3. `lua-stakeholder`
4. `dart-stakeholder`
5. `gleam-stakeholder`
6. `ocaml-stakeholder`

## Program framing
- `phase completeness` means complete for the repo's committed role.
- `program completeness` means complete for the eventual end-state in the larger rewrite program.
- Phase-complete repos can still have lower program completeness while later tranches remain open.

## Validation evidence on this workstation
- `javascript-stakeholder`: `npm run lint`, `npm run build`, `npm test`, `docker build -t javascript-stakeholder .`, and `npm run docker-test` passed locally after hydrating the declared Node dependencies.
- `java-stakeholder`: `docker build -t java-stakeholder .` passed locally through formatting, lint, tests, and package, and runtime smokes passed for `--list-values` plus the local demo provider path.
- `elixir-stakeholder`: `python3 scripts/validate_scaffold.py`, `mix local.hex --force`, `mix local.rebar --force`, `mix deps.get`, `mix format --check-formatted`, `mix credo --strict`, and `mix test` passed natively with `14` tests; Docker build plus runtime smokes passed for `--list-values`, representative classic-six and modern-core JSON, deterministic same-seed output, and explicit experimental-provider fail-fast.

## Publication guardrail
- Publication remains held until at least 10 new full rewrites with tests are complete.
- Exact GitHub required-check binding remains deferred until the first stable remote CI pass exists.
- `nix` remains pending through the official multi-user macOS installer.
- Deterministic CI remains provider-free; provider contract and live-integration work stay outside deterministic follower runs.
