# Lua validation

Timestamp: 2026-04-13 CEST

Lua is now recorded in the mirrored ledgers as the eighth validated wider-matrix local tranche.

## Evidence

- Native Lua checks were completed for the tranche.
- Docker build and runtime smoke coverage passed for the deterministic contract surface.
- Publication remains held until the 10-rewrite threshold is met.

## Effect on mirrored state

- `lua-stakeholder` moves to the validated local tranche set.
- The next readiness-first repo becomes `dart-stakeholder`.
