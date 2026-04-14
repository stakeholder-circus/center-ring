# Program documentation

This section is the mirrored planning surface for the stakeholder rewrite program.

## Canonical data
- `stakeholder-core/data/execution-roadmap.json`
- `stakeholder-core/data/language-matrix.json`
- `stakeholder-core/data/rewrite-status-matrix.json`
- `stakeholder-core/data/program-doc-hashes.json`

## Current sequencing
1. Rust stays canonical and is no longer treated as permanently frozen; it must also reach the full live-provider/runtime surface.
2. `stakeholder-core` owns the canonical phase/program status model and `center-ring` mirrors it.
3. `rust-stakeholder`, `javascript-stakeholder`, and `java-stakeholder` are the active live-provider/runtime lanes, with Rust already carrying the expanded deterministic generator surface and experimental provider models but still missing guarded runtime wiring.
4. `.NET`, Go, Python, and Swift remain the closed and validated follower baseline.
5. `fsharp-stakeholder`, `zig-stakeholder`, `haskell-stakeholder`, `kotlin-stakeholder`, `elixir-stakeholder`, `nim-stakeholder`, and `crystal-stakeholder` are the locally validated wider-matrix set, all held back from publication.
6. Readiness-first queue after the active-repo completion wave: `lua-stakeholder`, `dart-stakeholder`, `gleam-stakeholder`, `ocaml-stakeholder`.
7. Publication remains held until at least 10 new full rewrites with tests are complete.

## Model
- `phase completeness` means complete for the repo's committed role.
- `program completeness` means complete for the eventual end-state in the larger rewrite program.
- Phase-complete repos can still have lower program completeness while later tranches remain open.

## Toolchain baseline
- Homebrew advanced the local baseline for `ghc`, `cabal-install`, `hlint`, `kotlin`, `gradle`, `opam`, `dune`, `nim`, `crystal`, `gleam`, `luarocks`, and `stylua`.
- `ghcup` pins Haskell validation to `ghc-9.6.7`.
- `nix` is installed through the official multi-user macOS installer and `flake.lock` is normalized across the active repo set.
- The standard lock shape is shared by `stakeholder-core`, `center-ring`, `javascript-stakeholder`, `java-stakeholder`, `.NET`, Go, Python, Swift, `fsharp-stakeholder`, `kotlin-stakeholder`, and `elixir-stakeholder`; `zig-stakeholder` and `haskell-stakeholder` intentionally carry a second shared lock shape because their flakes depend on `flake-utils`.

## Detailed entry points
- [`current-wave.md`](current-wave.md)
- [`repo-sequencing.md`](repo-sequencing.md)
- [`language-horizon.md`](language-horizon.md)
- [`github-governance-state.md`](github-governance-state.md)
- [`interop-roadmap.md`](interop-roadmap.md)
- [`rewrite-status-matrix.md`](rewrite-status-matrix.md)
- [`next-100-languages.md`](next-100-languages.md)

## Tracked workspace summaries
- [`WORKSPACE_STATUS.md`](/Users/davidsupan/shareholder/center-ring/status/WORKSPACE_STATUS.md)
- [`WORKSPACE_NEXT_STEPS.md`](/Users/davidsupan/shareholder/center-ring/status/WORKSPACE_NEXT_STEPS.md)
- [`WORKSPACE_PARITY_STATUS.md`](WORKSPACE_PARITY_STATUS.md)
- [`WORKSPACE_COMPLETE.md`](WORKSPACE_COMPLETE.md)

## Mirror
This umbrella mirror must remain synchronized with `stakeholder-core/docs/program/`.
