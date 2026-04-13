# Stakeholder Job Status

Last updated: 2026-04-09 22:14 CEST
Owner: Codex agent

## Current status

- Program state: readiness-first threshold wave; the phase/program completeness model is authoritative, `javascript-stakeholder` and `java-stakeholder` remain the co-equal provider-runtime lanes, and the locally validated wider-matrix set now includes `fsharp-stakeholder`, `zig-stakeholder`, `haskell-stakeholder`, `kotlin-stakeholder`, `elixir-stakeholder`, and `nim-stakeholder`.
- Completed in this slice:
  - confirmed the official multi-user macOS Nix install is active through `/nix/var/nix/profiles/default/bin/nix`
  - normalized `flake.lock` across every active repo with `nix flake lock`
  - verified that the standard repos now share one lock shape while `zig-stakeholder` and `haskell-stakeholder` share a second `flake-utils`-aware lock shape
  - updated the canonical and mirrored program/status docs so they now point to `lua-stakeholder` as the next readiness-first queue tip
- Open in this slice:
  - keep publication held until at least 10 new full rewrites with tests are complete
  - keep `javascript-stakeholder` and `java-stakeholder` as co-equal provider-runtime lanes in canonical planning, with Java implemented and Docker-validated locally and JavaScript carrying explicit native plus Docker sidecar validation evidence
  - keep the validated wider-matrix repos local-only until the 10-rewrite publication threshold is met
  - bind exact GitHub required-check contexts only after the first stable remote CI pass exists
  - keep `flake.lock` normalized as additional active repos are promoted into the validated set

## Current blockers

- The publication threshold still blocks remote creation and push for the validated wider-matrix repos.
- `nix` is installed locally through the official multi-user macOS installer.
- `flake.lock` is normalized across the active repo set; `zig-stakeholder` and `haskell-stakeholder` intentionally carry a second lock variant because their flakes depend on `flake-utils`.
- The rest of the wider matrix remains intentionally unpublished until each repo is minimally real.

## Immediate next actions

1. Keep `fsharp-stakeholder`, `zig-stakeholder`, `haskell-stakeholder`, `kotlin-stakeholder`, `elixir-stakeholder`, and `nim-stakeholder` local until the 10-rewrite publication threshold is met.
2. Keep `crystal-stakeholder` held as the seventh validated wider-matrix repo while publication remains blocked.
3. Start `lua-stakeholder` as the next full local rewrite tranche.
4. Continue the readiness-first queue with `dart-stakeholder`, `gleam-stakeholder`, and `ocaml-stakeholder`.
4. Keep `flake.lock` normalized as additional active repos are promoted.
5. Bind exact GitHub required-check contexts after the first stable remote CI pass exists on published repos.
