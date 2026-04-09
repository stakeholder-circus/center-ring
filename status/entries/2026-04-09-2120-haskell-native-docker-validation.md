# Haskell tranche validation entry

- Timestamp: `2026-04-09 21:20 CEST`
- Repo: `haskell-stakeholder`
- State: `classic-six-plus-modern-core-native-and-docker-validated-not-for-push`
- Native toolchain: `ghcup run --ghc 9.6.7 -- cabal build all` and `ghcup run --ghc 9.6.7 -- cabal test all`
- Native validation: `fourmolu -m check app src test`, `hlint .`, native build pass, native test pass (`14` tests including the deterministic property check)
- Docker validation: `docker build -t haskell-stakeholder .` passed, including in-image `cabal build all`, in-image `cabal test all`, and published runtime image assembly
- Docker runtime smokes: `--list-values`, representative classic-six JSON, representative modern-core JSON, deterministic same-seed comparison, and experimental-provider fail-fast all passed
- Publication state: local-only; publication remains blocked by the 10-full-rewrites guardrail
- Toolchain note: Homebrew `ghc` 9.14 was not a workable native baseline for this repo, so native validation is pinned through `ghcup` to `ghc-9.6.7`
- Nix note: `flake.lock` generation still waits on the official multi-user macOS Nix install, which requires a live sudo-authenticated Codex PTY or a user-run local installer session
