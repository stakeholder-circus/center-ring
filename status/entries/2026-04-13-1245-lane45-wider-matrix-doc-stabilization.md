# 2026-04-13 12:45 CEST - Lane 4 and Lane 5 wider-matrix doc stabilization

## Scope
- Repo-local status and toolchain wording cleanup in `fsharp-stakeholder`, `zig-stakeholder`, `haskell-stakeholder`, `kotlin-stakeholder`, `elixir-stakeholder`, `nim-stakeholder`, and `crystal-stakeholder`
- No runtime changes
- No new validation runs for the wider-matrix repos in this slice

## Decisions
- The seven validated wider-matrix repos now use consistent "validated wider-matrix repo held for publication" language.
- Stale Nix and `flake.lock` wording was updated where the installed Nix state made the older text incorrect.
- The wider-matrix repos now describe live-provider work as an open future lane rather than a permanent exclusion.

## Follow-up
- Either return to the provider hardening lane or begin `lua-stakeholder` as the next rewrite tranche.
