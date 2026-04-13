# Current wave

Last updated: 2026-04-09 22:14 CEST
The active wave is `readiness-first-threshold-wave`. The phase/program completeness model remains authoritative, `javascript-stakeholder` and `java-stakeholder` remain the co-equal provider runtimes, the validated wider-matrix set now includes `crystal-stakeholder` as the seventh validated wider-matrix repo, `nix` is installed through the official multi-user macOS path, `flake.lock` is normalized across the active repo set, publication remains held until at least 10 new full rewrites with tests are complete, and the next repo queued for promotion is `lua-stakeholder`.

## Locked sequencing rules
- `rust-stakeholder` remains the canonical source of truth and stays frozen except for additive governance or status sync.
- `stakeholder-core` owns the canonical status-model migration and `center-ring` mirrors it.
- `javascript-stakeholder` and `java-stakeholder` are co-equal provider runtimes.
- The follower `modern-core` wave in `.NET`, Go, Python, and Swift is closed and validated.
- The validated wider-matrix set now includes `fsharp-stakeholder`, `zig-stakeholder`, `haskell-stakeholder`, `kotlin-stakeholder`, `elixir-stakeholder`, `nim-stakeholder`, and `crystal-stakeholder`.
- Wider-matrix repos remain local-only until each is minimally real and the publication hold is explicitly lifted.

## Active implementation lane
The readiness-first threshold wave is focused on producing additional fully validated local rewrites without breaking the publication hold:
- `javascript-stakeholder` and `java-stakeholder`: keep the co-equal provider-runtime lanes phase-complete and provider-free in deterministic CI.
- `dotnet-stakeholder`, `go-stakeholder`, `python-stakeholder`, `swift-stakeholder`: remain the validated follower baseline.
- `fsharp-stakeholder`, `zig-stakeholder`, `haskell-stakeholder`, `kotlin-stakeholder`, `elixir-stakeholder`, `nim-stakeholder`, `crystal-stakeholder`: remain the locally validated wider-matrix set held back only by the 10-rewrite publication guardrail.
- `crystal-stakeholder`: validated local full rewrite, seventh validated wider-matrix repo, and now held while `lua-stakeholder` becomes the next readiness-first tranche.

## Ready-first queue after the active wave
The next repos are promoted in this order:
1. `lua-stakeholder`
2. `dart-stakeholder`
3. `gleam-stakeholder`
4. `ocaml-stakeholder`

## Program framing
- `phase completeness` means complete for the repo's committed role.
- `program completeness` means complete for the eventual end-state in the larger rewrite program.
- Phase-complete repos can still have lower program completeness while later tranches remain open.

## Validation evidence on this workstation
- `javascript-stakeholder`: `npm run lint`, `npm run build`, `npm test`, `docker build -t javascript-stakeholder .`, and `npm run docker-test` passed locally after hydrating the declared Node dependencies.
- `java-stakeholder`: `docker build -t java-stakeholder .` passed locally through formatting, lint, tests, and package, and runtime smokes passed for `--list-values` plus the local demo provider path.
- `elixir-stakeholder`: `python3 scripts/validate_scaffold.py`, `mix local.hex --force`, `mix local.rebar --force`, `mix deps.get`, `mix format --check-formatted`, `mix credo --strict`, and `mix test` passed natively with `14` tests; Docker build plus runtime smokes passed for `--list-values`, representative classic-six and modern-core JSON, deterministic same-seed output, and explicit experimental-provider fail-fast.
- `nim-stakeholder`: `nimpretty --check`, `nim check src/stakeholder.nim`, `nim c src/stakeholder.nim`, `nimble test`, `docker build -t nim-stakeholder .`, and `docker run --rm nim-stakeholder --list-values` passed locally.
- `crystal-stakeholder`: `python3 scripts/validate_scaffold.py`, `crystal tool format --check src spec`, `crystal build src/crystal_stakeholder.cr -o bin/crystal-stakeholder`, and `crystal spec` passed natively; Docker build plus runtime smokes passed for `--list-values`, representative classic-six and modern-core JSON, deterministic same-seed output, explicit experimental-provider fail-fast, and `flake.lock` was generated through the active Nix install.

## Publication guardrail
- Publication remains held until at least 10 new full rewrites with tests are complete.
- Exact GitHub required-check binding remains deferred until the first stable remote CI pass exists.
- `nix` is installed through the official multi-user macOS installer and active in this environment.
- Deterministic CI remains provider-free; provider contract and live-integration work stay outside deterministic follower runs.
