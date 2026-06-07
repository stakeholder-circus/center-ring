# Elixir tranche validation entry

- Timestamp: `2026-04-09 21:47 CEST`
- Repo: `elixir-stakeholder`
- State: `classic-six-plus-modern-core-native-and-docker-validated-not-for-push`
- Native validation: `python3 scripts/validate_scaffold.py`, `mix local.hex --force`, `mix local.rebar --force`, `mix deps.get`, `mix format --check-formatted`, `mix credo --strict`, and `mix test` all passed with `14` tests
- Docker validation: `docker build -t elixir-stakeholder .` passed and produced the runtime image
- Docker runtime smokes: `--list-values`, representative classic-six and modern-core JSON, deterministic same-seed comparison, and explicit `--experimental-provider` fail-fast all passed
- Traceability note: dedicated classic-six and modern-core families are recorded in `docs/traceability/first-push-families.md`
- Publication state: local-only; publication remains blocked by the 10-full-rewrites guardrail
- Queue effect: the validated wider-matrix count is now `5`, and `nim-stakeholder` is next in the readiness-first queue
- Nix note: `flake.lock` generation still waits on the official multi-user macOS Nix install, which remains blocked in this PTY because sudo is unavailable here
