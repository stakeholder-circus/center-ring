# 2026-04-09 17:12 CEST - F# first-push-bar validation

## Scope
- `fsharp-stakeholder`
- canonical and mirrored program-status surfaces

## Summary
- Closed the prior follower `modern-core` wave in the docs.
- Promoted the active wider-matrix lane to `fsharp-stakeholder`.
- Reached the local technical first-push bar for F# without publishing the repo.

## Validation evidence
- `python3 scripts/validate_scaffold.py`: pass
- `dotnet tool restore --tool-manifest .config/dotnet-tools.json`: pass
- `dotnet fantomas src tests --check`: pass
- `dotnet build src/FsharpStakeholder/FsharpStakeholder.fsproj`: pass
- `dotnet build tests/FsharpStakeholder.Tests/FsharpStakeholder.Tests.fsproj`: pass
- host `dotnet test`: blocked locally because only the .NET 10 runtime is installed
- Docker gate: pass
  - image build succeeded
  - .NET 8 test suite passed with `14` tests
  - `--list-values` smoke passed
  - representative focused-family JSON smokes passed
  - deterministic same-seed comparison passed
  - experimental-provider fail-fast behavior passed

## Guardrail
- `fsharp-stakeholder` remains local-only until publication is explicitly authorized.
