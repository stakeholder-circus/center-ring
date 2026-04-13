# Nix activation and flake-lock normalization entry

- Timestamp: `2026-04-09 21:59 CEST`
- Repos: `stakeholder-core`, `center-ring`, `javascript-stakeholder`, `java-stakeholder`, `dotnet-stakeholder`, `go-stakeholder`, `python-stakeholder`, `swift-stakeholder`, `fsharp-stakeholder`, `zig-stakeholder`, `haskell-stakeholder`, `kotlin-stakeholder`, `elixir-stakeholder`
- State: `nix-active-active-repo-locks-normalized`
- Nix activation: `/nix/var/nix/profiles/default/bin/nix --version` returned `nix (Nix) 2.34.5`, confirming the official multi-user macOS install is active in this environment
- Flake verification: `/nix/var/nix/profiles/default/bin/nix --extra-experimental-features 'nix-command flakes' flake show` succeeded in `stakeholder-core`
- Lock normalization: `nix flake lock` completed across every active repo in scope
- Lock-shape split: `stakeholder-core`, `center-ring`, `javascript-stakeholder`, `java-stakeholder`, `dotnet-stakeholder`, `go-stakeholder`, `python-stakeholder`, `swift-stakeholder`, `fsharp-stakeholder`, `kotlin-stakeholder`, and `elixir-stakeholder` now share `e473fbd5c12b739a9918a72fccf58b0279a8b8c163b1c81d52cc077a499ae173`; `zig-stakeholder` and `haskell-stakeholder` share `cdd2219292f4ac15f1856c5fbdafe5acdd14936710508edc47701c6aec423177` because their flakes depend on `flake-utils`
- Status sync: canonical, mirrored, and workspace-root docs were updated so Nix is no longer tracked as blocked or pending
- Publication state: wider-matrix publication remains blocked until at least `10` new full rewrites with tests are complete
- Next queue: `nim-stakeholder` remains next in the readiness-first queue
