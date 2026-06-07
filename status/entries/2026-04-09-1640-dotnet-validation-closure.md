# Validation entry: dotnet closure

- timestamp: `2026-04-09 16:40 CEST`
- scope: `dotnet-stakeholder`
- summary:
  - restored `rendererKey` in dotnet `--list-values` generator-family output
  - preserved `renderer` for compatibility
  - closed the open follower modern-core validation regression
- validation:
  - `dotnet build`
  - `docker build -t stakeholder-dotnet-validate .`
- note:
  - host-side `dotnet test` is still not a reliable path on this workstation because the .NET 8 runtime is absent locally
