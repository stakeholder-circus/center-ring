# Validation entry: follower modern-core

- timestamp: `2026-04-09 16:37 CEST`
- scope: `dotnet-stakeholder`, `go-stakeholder`, `python-stakeholder`, `swift-stakeholder`
- summary:
  - `go-stakeholder` passed `go test ./...` and `go build ./...`
  - `python-stakeholder` passed `python -m pytest` in a temporary validation venv after host `pytest` absence
  - `swift-stakeholder` passed `swift test`
  - `dotnet-stakeholder` built locally, but host execution is blocked by missing .NET 8 runtime and Docker-backed test execution exposed a real smoke-test regression
- dotnet detail:
  - failing test: `DotnetStakeholder.Tests.SmokeTests.ListValuesIncludesFull2026FamilyRegistry`
  - failure type: `System.Collections.Generic.KeyNotFoundException`
  - failing location: `tests/DotnetStakeholder.Tests/SmokeTests.cs:45`
- follow-up:
  - fix the dotnet `--list-values` output/test expectation mismatch
  - rerun dotnet validation after the fix
