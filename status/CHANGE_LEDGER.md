# Stakeholder Change Ledger

Append-only engineering ledger for active, uncommitted, and in-flight work.

## Entry format

1. `id`: stable entry id.
2. `timestamp`: local timezone timestamp.
3. `scope`: feature/fix/documentation area.
4. `repos`: affected repositories.
5. `changes`: what changed.
6. `validation`: commands/evidence run.
7. `next`: immediate follow-up.

---

### 2026-04-09-001

- id: `2026-04-09-001`
- timestamp: `2026-04-09 16:30 CEST`
- scope: `program audit surface + local matrix scaffolds`
- repos:
  - `stakeholder-core`
  - `center-ring`
  - `rust-stakeholder`
  - `javascript-stakeholder`
  - `fsharp-stakeholder`
  - `zig-stakeholder`
  - `haskell-stakeholder`
  - `kotlin-stakeholder`
  - `elixir-stakeholder`
  - `ocaml-stakeholder`
  - `nim-stakeholder`
  - `crystal-stakeholder`
  - `dart-stakeholder`
  - `lua-stakeholder`
  - `gleam-stakeholder`
  - `zeta-stakeholder`
- changes:
  - Added nearest-scope `AGENTS.md` guidance for canonical, umbrella, sidecar, and scaffold repos.
  - Created local scaffold repos with preserved Rust history, provenance docs, governance hooks/workflows, `flake.nix`, and explicit not-for-push guardrails.
  - Added canonical status surfaces: rewrite status matrix, per-repo `STATUS.md`, canonical `JOB_STATUS.md`, and separate next-100-languages backlog.
  - Updated `language-matrix.json` and `execution-roadmap.json` so follower repos and scaffolds reflect current local state.
- validation:
  - `path existence and content spot checks` for new `AGENTS.md`, scaffold docs, and generated `flake.nix` files
  - `program-doc manifest refresh` completed
- next:
  - validate follower modern-core repos and append the results as a new ledger entry
  - keep scaffold repos local until they are minimally implemented

### 2026-04-09-002

- id: `2026-04-09-002`
- timestamp: `2026-04-09 16:37 CEST`
- scope: `follower modern-core validation evidence`
- repos:
  - `dotnet-stakeholder`
  - `go-stakeholder`
  - `python-stakeholder`
  - `swift-stakeholder`
  - `stakeholder-core`
  - `center-ring`
- changes:
  - Ran the explicit validation lane for the four active follower repos after the local modern-core tranche landed.
  - Confirmed passing local validation in Go, Python, and Swift.
  - Confirmed that scaffold repos remain local-only and not for push, then corrected canonical roadmap wording to match that rule.
  - Recorded a real dotnet smoke-test failure rather than masking it behind the host .NET runtime mismatch.
- validation:
  - `dotnet-stakeholder`: `dotnet test` built successfully but host execution was blocked by missing .NET 8 runtime; Docker fallback `docker build -t stakeholder-dotnet-validate .` failed in `SmokeTests.ListValuesIncludesFull2026FamilyRegistry` with `KeyNotFoundException` at `tests/DotnetStakeholder.Tests/SmokeTests.cs:45`
  - `go-stakeholder`: `go test ./...` and `go build ./...`
  - `python-stakeholder`: temporary venv + `pip install -e '.[test,dev]'` + `python -m pytest`
  - `swift-stakeholder`: `swift test`
- next:
  - fix the dotnet `--list-values` smoke-test regression and rerun dotnet validation
  - keep scaffold repos local until they contain real implementation depth
  - bind exact required GitHub checks only after the first stable CI pass exists on the protected repos

### 2026-04-09-003

- id: `2026-04-09-003`
- timestamp: `2026-04-09 16:40 CEST`
- scope: `dotnet list-values regression fix + validation closure`
- repos:
  - `dotnet-stakeholder`
  - `stakeholder-core`
  - `center-ring`
- changes:
  - Restored the `rendererKey` field in dotnet `--list-values` generator-family output while keeping `renderer` for compatibility.
  - Closed the open follower modern-core validation failure in dotnet.
  - Updated canonical and mirrored validation/status ledgers so all four active follower repos now show passing validation evidence.
- validation:
  - `dotnet build`
  - `docker build -t stakeholder-dotnet-validate .`
- next:
  - keep scaffold repos local until they contain real implementation depth
  - bind exact required GitHub checks only after the first stable CI pass exists on the protected repos
  - generate `flake.lock` only after `nix` is available locally

### 2026-04-09-004

- id: `2026-04-09-004`
- timestamp: `2026-04-09 16:40 CEST`
- scope: `fsharp foundation promotion`
- repos:
  - `fsharp-stakeholder`
  - `stakeholder-core`
- changes:
  - Promoted `fsharp-stakeholder` from governance-only scaffold to a real local foundation slice.
  - Added a deterministic F# CLI foundation with normalized JSON output, full family registry exposure in `--list-values`, explicit experimental-provider fail-fast behavior, and dedicated foundation renderers for `code_analyzer` and `agent_workflows`.
  - Updated F# repo docs, flake contract, CI workflow, and per-repo status to reflect the new foundation state.
  - Updated canonical matrix and roadmap data so F# is no longer tracked as scaffold-only.
- validation:
  - not run in this slice; F# implementation was promoted without a validation pass because the active explicit validation request only covered the four follower repos
- next:
  - expand F# from foundation into broader classic-six and modern-core depth
  - keep F# local-only until it is minimally real enough for a first public push

### 2026-04-09-005

- id: `2026-04-09-005`
- timestamp: `2026-04-09 17:12 CEST`
- scope: `fsharp first-push-bar tranche + conservative MIT policy`
- repos:
  - `fsharp-stakeholder`
  - `stakeholder-core`
  - `center-ring`
- changes:
  - Recut the canonical and mirrored program docs so the follower `modern-core` wave is closed and the active wider-matrix lane is now `fsharp-stakeholder`.
  - Corrected the stale F# scaffold validator to match the split `ci-native` and `docker-smoke` workflow layout.
  - Fixed the remaining F# type-inference issues so the repo now builds cleanly and exposes full classic-six plus full modern-core dedicated coverage.
  - Updated F# repo docs, AGENTS guidance, provenance, and parity docs to reflect the conservative MIT attribution policy and the local first-push bar.
  - Updated validation, status, and coarse completion matrices so the audit surface reflects the actual F# validation evidence instead of the earlier foundation-only wording.
- validation:
  - `python3 scripts/validate_scaffold.py`
  - `dotnet tool restore --tool-manifest .config/dotnet-tools.json`
  - `dotnet fantomas src tests --check`
  - `dotnet build src/FsharpStakeholder/FsharpStakeholder.fsproj`
  - `dotnet build tests/FsharpStakeholder.Tests/FsharpStakeholder.Tests.fsproj`
  - host `dotnet test tests/FsharpStakeholder.Tests/FsharpStakeholder.Tests.fsproj` blocked because this workstation does not have the .NET 8 runtime installed
  - `docker build -t fsharp-stakeholder .` (includes `dotnet test` in the .NET 8 container; `14` tests passed)
  - Docker runtime smokes for `--list-values`, representative focused-family JSON output, deterministic same-seed output, and experimental-provider fail-fast behavior
- next:
  - keep `fsharp-stakeholder` local-only until publication is explicitly approved
  - use the validated F# slice as the implementation template for `zig-stakeholder`
  - bind `ci-native`, `docker-smoke`, `actionlint`, and `dependency-review` only after the first stable remote CI pass exists
  - generate `flake.lock` only after `nix` is available locally

### 2026-04-09-006

- id: `2026-04-09-006`
- timestamp: `2026-04-09 17:45 CEST`
- scope: `documentation/status sync + toolchain baseline + publication hold`
- repos:
  - `stakeholder-core`
  - `center-ring`
  - workspace root summary docs
- changes:
  - Updated the canonical and mirrored program/status surfaces to mark the follower `modern-core` wave closed and validated.
  - Marked `fsharp-stakeholder` as locally validated for the first-push bar but still held back from publication until at least 10 new full rewrites with tests are complete.
  - Recorded the Homebrew-updated toolchain baseline for `ghc`, `cabal-install`, `hlint`, `kotlin`, `gradle`, `opam`, `dune`, `nim`, `crystal`, `gleam`, `luarocks`, and `stylua`, with `nix` still pending.
  - Refreshed the root summary docs so the publication hold and pending toolchain follow-ons remain visible at workspace level.
- validation:
  - documentation and data update only; no runtime validation run
- next:
  - keep `fsharp-stakeholder` local until the 10-rewrite publication threshold is met
  - continue using the validated F# slice as the template for `zig-stakeholder`
  - install `nix` when available and generate `flake.lock` afterward

### 2026-04-09-007

- id: `2026-04-09-007`
- timestamp: `2026-04-09 17:55 CEST`
- scope: `zig tranche promotion + docs/status sync`
- repos:
  - `stakeholder-core`
  - `center-ring`
  - workspace root summary docs
- changes:
  - Recorded that `zig-stakeholder` has moved from scaffold-only to a local full classic-six plus modern-core implementation tranche.
  - Marked the Zig tranche as Docker-validated locally while preserving the host-native Zig Darwin linker blocker on this workstation.
  - Updated the canonical and mirrored program/status surfaces to keep the publication hold of at least 10 new full rewrites with tests visible.
  - Kept the documentation structure and append-only audit style intact rather than rewriting prior history.
- validation:
  - documentation and data update only; no runtime validation run
- next:
  - keep `zig-stakeholder` local until the 10-rewrite publication threshold is met
  - use the Zig tranche as the next template after F# for the remaining wider-matrix repos
  - generate `flake.lock` after `nix` becomes available locally

### 2026-04-09-008

- id: `2026-04-09-008`
- timestamp: `2026-04-09 17:58 CEST`
- scope: `toolchain baseline refresh + docs/status sync`
- repos:
  - `stakeholder-core`
  - `center-ring`
  - workspace root summary docs
- changes:
  - Recorded that `ocamlformat` is now installed locally via `opam`.
  - Updated the canonical and mirrored program/status surfaces so `nix` is now the remaining major blocker, with future repo-specific package-manager follow-ons called out as they arise.
  - Kept the 10-full-rewrites publication hold and the zig Docker-validated/native-host-blocked status intact.
  - Refreshed the root summary docs to match the narrower blocker set.
- validation:
  - documentation and data update only; no runtime validation run
- next:
  - keep the 10-rewrite publication hold in force
  - treat `nix` as the remaining major blocker until installed
  - add future repo-specific package-manager follow-ons only when new language repos require them

### 2026-04-09-009

- id: `2026-04-09-009`
- timestamp: `2026-04-09 21:16 CEST`
- scope: `status-model migration + co-equal provider-lane framing`
- repos:
  - `stakeholder-core`
  - `center-ring`
  - `javascript-stakeholder`
  - `dotnet-stakeholder`
  - `go-stakeholder`
  - `python-stakeholder`
  - `swift-stakeholder`
  - `fsharp-stakeholder`
  - `zig-stakeholder`
  - `haskell-stakeholder`
  - `kotlin-stakeholder`
- changes:
  - Reframed the active wave around phase/program completeness instead of a single coarse completion score.
  - Marked `javascript-stakeholder` and `java-stakeholder` as co-equal provider-runtime lanes in canonical planning, while leaving the `java-stakeholder` repo itself untouched in this slice.
  - Corrected repo-local status drift for the validated follower repos and validated wider-matrix repos so their status files now match the canonical ledger again.
  - Updated canonical and mirrored program docs, status docs, and root summaries to reflect the active-repo completion wave framing and the unchanged 10-rewrite publication guardrail.
- validation:
  - documentation and data update only; no runtime validation run
- next:
  - keep publication held until at least 10 new full rewrites with tests are complete
  - continue the readiness-first queue with `elixir-stakeholder` next
  - install `nix` through the official multi-user macOS installer once a live sudo-authenticated Codex PTY or separate user-run terminal session is available


### 2026-04-09-010

- id: `2026-04-09-010`
- timestamp: `2026-04-09 21:16 CEST`
- scope: `java provider-runtime docs/status sync`
- repos:
  - `stakeholder-core`
  - `center-ring`
  - workspace root summary docs
- changes:
  - Updated canonical and mirrored planning/status surfaces to record `java-stakeholder` as implemented and Docker-validated locally.
  - Recorded the JVM-native experimental provider runtime facts in the canonical ledgers: encrypted local state, prompt assets/versions, personalization profiles, cache/provenance, consumer-session import/replay, external bootstrap-command capture, local demo provider, OpenAI-compatible and Anthropic adapters, nonsecret contract tests, and an opt-in live integration harness.
  - Kept deterministic CI provider-free, left the 10-rewrite publication hold unchanged, and documented that `nix` is still blocked in this PTY because sudo is unavailable here.
- validation:
  - documentation and data update only; no runtime validation run
- next:
  - keep the publication hold unchanged
  - leave `java-stakeholder` repo files untouched in this slice
  - continue the readiness-first queue with `elixir-stakeholder` next


### 2026-04-09-011

- id: `2026-04-09-011`
- timestamp: `2026-04-09 21:31 CEST`
- scope: `provider-lanes validation and phase/program reconciliation`
- repos:
  - `javascript-stakeholder`
  - `java-stakeholder`
  - `stakeholder-core`
  - `center-ring`
  - workspace root summary docs
- changes:
  - Added explicit validation evidence for `javascript-stakeholder` so the co-equal provider-sidecar lane is represented alongside Java in the canonical and mirrored ledgers.
  - Removed the stale Java experimental-provider deferral from the execution roadmap and updated the active-wave narrative to reflect completed Java and JavaScript provider-lane evidence.
  - Updated the execution-roadmap schema for the phase/program completeness fields and re-synchronized the mirrored program docs and hash manifest.
- validation:
  - `javascript-stakeholder`: native Node lint/build/test plus Docker sidecar smokes passed
  - `java-stakeholder`: Docker build/test/package and runtime smokes passed
  - `stakeholder-core`: schema validation, program-doc validation, and `mkdocs build --strict` passed
  - `center-ring`: program-doc validation passed
- next:
  - keep publication held until at least 10 new full rewrites with tests are complete
  - start `elixir-stakeholder` as the next readiness-first full local rewrite tranche
  - install `nix` through the official multi-user macOS path once a live sudo-authenticated PTY is available


### 2026-04-09-012

- id: `2026-04-09-012`
- timestamp: `2026-04-09 21:47 CEST`
- scope: `elixir wider-matrix tranche validation`
- repos:
  - `elixir-stakeholder`
  - `stakeholder-core`
  - `center-ring`
  - workspace root summary docs
- changes:
  - Promoted `elixir-stakeholder` from scaffold-only into a full local classic-six plus modern-core rewrite tranche with deterministic normalized JSON output and grouped fallback for later families.
  - Added native Elixir validation, Docker build/runtime smoke coverage, traceability rows, CI workflows, and updated toolchain/provenance docs.
  - Updated the canonical and mirrored ledgers so the validated wider-matrix set now includes `elixir-stakeholder` and the readiness-first queue now points at `nim-stakeholder`.
- validation:
  - `elixir-stakeholder`: scaffold validation, native Elixir format/lint/test, Docker build, deterministic Docker runtime smokes, and explicit experimental-provider fail-fast all passed
  - `stakeholder-core`: canonical docs/data were updated to reflect the fifth validated wider-matrix repo
- next:
  - keep publication held until at least 10 new full rewrites with tests are complete
  - start `nim-stakeholder` as the next readiness-first full local rewrite tranche
  - install `nix` through the official multi-user macOS path once a live sudo-authenticated PTY is available

### 2026-04-09-013

- id: `2026-04-09-013`
- timestamp: `2026-04-09 21:59 CEST`
- scope: `nix activation + flake lock normalization`
- repos:
  - `stakeholder-core`
  - `center-ring`
  - `javascript-stakeholder`
  - `java-stakeholder`
  - `dotnet-stakeholder`
  - `go-stakeholder`
  - `python-stakeholder`
  - `swift-stakeholder`
  - `fsharp-stakeholder`
  - `zig-stakeholder`
  - `haskell-stakeholder`
  - `kotlin-stakeholder`
  - `elixir-stakeholder`
  - workspace root summary docs
- changes:
  - Confirmed `nix` 2.34.5 is active through `/nix/var/nix/profiles/default/bin/nix` after the official multi-user macOS install.
  - Ran `nix flake show` against `stakeholder-core` and normalized `flake.lock` across every active repo in scope.
  - Recorded the resulting lock-shape split explicitly: the standard repos share `e473fbd5c12b739a9918a72fccf58b0279a8b8c163b1c81d52cc077a499ae173`, while `zig-stakeholder` and `haskell-stakeholder` share `cdd2219292f4ac15f1856c5fbdafe5acdd14936710508edc47701c6aec423177` because their flakes depend on `flake-utils`.
  - Updated canonical, mirrored, and root status surfaces so they no longer claim Nix is blocked or pending.
- validation:
  - `/nix/var/nix/profiles/default/bin/nix --version` -> `nix (Nix) 2.34.5`
  - `/nix/var/nix/profiles/default/bin/nix --extra-experimental-features 'nix-command flakes' flake show` in `stakeholder-core`
  - `/nix/var/nix/profiles/default/bin/nix --extra-experimental-features 'nix-command flakes' flake lock` in each active repo
  - post-run lock verification via `shasum -a 256 */flake.lock` for the active repo set
- next:
  - keep the publication hold unchanged until at least 10 new full rewrites with tests are complete
  - keep `flake.lock` normalized as additional active repos are promoted
  - continue the readiness-first queue with `nim-stakeholder` next

### 2026-04-09-014

- id: `2026-04-09-014`
- timestamp: `2026-04-09 22:14 CEST`
- scope: `nim local full rewrite validation + status sync`
- repos:
  - `nim-stakeholder`
  - `stakeholder-core`
  - `center-ring`
  - workspace root summary docs
- changes:
  - Promoted `crystal-stakeholder` from scaffold-only into the seventh validated wider-matrix repo with local full classic-six plus modern-core depth.
  - Updated the canonical, mirrored, and root status surfaces so the readiness-first queue now tips at `lua-stakeholder` while the 10-rewrite publication hold remains unchanged.
  - Recorded the nim tranche as a validated local full rewrite and kept the shared Nix/flake normalization state visible in the planning docs.
- validation:
  - `nimpretty --check`
  - `nim check src/stakeholder.nim`
  - `nim c src/stakeholder.nim`
  - `nimble test`
  - `docker build -t nim-stakeholder .`
  - `docker run --rm nim-stakeholder --list-values`
- next:
  - keep `crystal-stakeholder` local-only for publication until the 10-rewrite threshold is met
  - start `lua-stakeholder` as the next readiness-first full local rewrite tranche
