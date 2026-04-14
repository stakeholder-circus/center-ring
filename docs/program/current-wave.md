# Current wave

Last updated: 2026-04-14 CEST
The active wave is `publication-governance-wave`. The phase/program completeness model remains authoritative, `rust-stakeholder`, `javascript-stakeholder`, and `java-stakeholder` are the active live-provider/runtime lanes, the validated wider-matrix set now includes `gleam-stakeholder` as the tenth validated wider-matrix repo, `nix` is installed through the official multi-user macOS path, `flake.lock` is normalized across the active repo set, the 10-rewrite widening threshold has been reached, and the next required program move is the publication/governance wave before `ocaml-stakeholder` begins.

## Locked sequencing rules
- `rust-stakeholder` remains the canonical source of truth, but it is no longer treated as permanently frozen because it must also reach the full live-provider/runtime surface.
- `stakeholder-core` owns the canonical status-model migration and `center-ring` mirrors it.
- `rust-stakeholder`, `javascript-stakeholder`, and `java-stakeholder` are the active live-provider/runtime lanes.
- The follower `modern-core` wave in `.NET`, Go, Python, and Swift is closed and validated.
- The validated wider-matrix set now includes `fsharp-stakeholder`, `zig-stakeholder`, `haskell-stakeholder`, `kotlin-stakeholder`, `elixir-stakeholder`, `nim-stakeholder`, `crystal-stakeholder`, `lua-stakeholder`, `dart-stakeholder`, and `gleam-stakeholder`.
- Wider-matrix repos remain local-only until publication/governance work explicitly opens the batch push wave.

## Active implementation lane
The publication-governance wave is focused on converting the first ten validated local rewrites into a governed publication batch without re-opening widening:
- `rust-stakeholder`, `javascript-stakeholder`, and `java-stakeholder`: continue provider-runtime hardening while deterministic CI stays provider-free.
- `.NET`, `go-stakeholder`, `python-stakeholder`, `swift-stakeholder`: remain the validated follower baseline.
- `fsharp-stakeholder`, `zig-stakeholder`, `haskell-stakeholder`, `kotlin-stakeholder`, `elixir-stakeholder`, `nim-stakeholder`, `crystal-stakeholder`, `lua-stakeholder`, `dart-stakeholder`, and `gleam-stakeholder`: form the ten-repo publication-held batch. `gleam-stakeholder` is the threshold-closing tranche.

## Queue after the publication/governance wave
1. `ocaml-stakeholder`

## Program framing
- `phase completeness` means complete for the repo's committed role.
- `program completeness` means complete for the eventual end-state in the larger rewrite program.
- Phase-complete repos can still have lower program completeness while later tranches remain open.

## Validation evidence on this workstation
- `javascript-stakeholder`: `npm run lint`, `npm run build`, `npm test`, `docker build -t javascript-stakeholder .`, and `npm run docker-test` passed locally after hydrating the declared Node dependencies.
- `java-stakeholder`: `docker build -t java-stakeholder .` passed locally through formatting, lint, tests, and package, and runtime smokes passed for `--list-values` plus the local demo provider path.
- `rust-stakeholder`: `cargo fmt --check`, `cargo test`, `cargo run -- --list-values`, `cargo run -- --experimental-provider local-demo --output-format json`, and the orphan experimental flag fail-fast path all passed locally through the rustup-managed toolchain.
- `elixir-stakeholder`: `python3 scripts/validate_scaffold.py`, `mix local.hex --force`, `mix local.rebar --force`, `mix deps.get`, `mix format --check-formatted`, `mix credo --strict`, and `mix test` passed natively with `14` tests; Docker build plus runtime smokes passed for `--list-values`, representative classic-six and modern-core JSON, deterministic same-seed output, and explicit experimental-provider fail-fast.
- `nim-stakeholder`: `nimpretty --check`, `nim check src/stakeholder.nim`, `nim c src/stakeholder.nim`, `nimble test`, `docker build -t nim-stakeholder .`, and `docker run --rm nim-stakeholder --list-values` passed locally.
- `crystal-stakeholder`: `python3 scripts/validate_scaffold.py`, `crystal tool format --check src spec`, `crystal build src/crystal_stakeholder.cr -o bin/crystal-stakeholder`, and `crystal spec` passed natively; Docker build plus runtime smokes passed for `--list-values`, representative classic-six and modern-core JSON, deterministic same-seed output, explicit experimental-provider fail-fast, and `flake.lock` was generated through the active Nix install.
- `lua-stakeholder`: `python3 scripts/validate_scaffold.py`, `stylua --check bin lua spec`, `luacheck lua bin spec`, and `busted` passed natively; Docker build plus runtime smokes passed for `--list-values`, representative classic-six and modern-core JSON, deterministic same-seed output, explicit experimental-provider fail-fast, and `flake.lock` was generated through the active Nix install.
- `dart-stakeholder`: `python3 scripts/validate_scaffold.py`, `dart pub get`, `dart format --set-exit-if-changed .`, `dart analyze`, `dart test`, `mkdir -p build && dart compile exe bin/stakeholder.dart -o build/stakeholder`, `docker build -t dart-stakeholder .`, Docker runtime smokes, `nix ... flake lock`, and `nix ... run .#check` all passed locally.
- `gleam-stakeholder`: `python3 scripts/validate_scaffold.py`, `gleam deps download`, `gleam format --check src test`, `gleam test`, `gleam run -- --list-values`, `docker build -t gleam-stakeholder .`, Docker runtime smokes, `nix ... flake lock`, and `nix ... run .#check` all passed locally.

## Publication guardrail
- The widening threshold is now satisfied at ten validated wider-matrix repos.
- No additional widening starts until the publication/governance wave for those ten repos is closed.
- Exact GitHub required-check binding remains deferred until the first stable remote CI pass exists.
- `nix` is installed through the official multi-user macOS installer and active in this environment.
- Deterministic CI remains provider-free; provider contract and live-integration work stay outside deterministic follower runs even as Rust, JavaScript, and Java advance the live-provider/runtime lane.
