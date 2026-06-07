# 2026-04-13 11:45 CEST - Rust live-provider validation

## Scope
- Validate the guarded Rust live-provider/runtime lane through the rustup-managed toolchain
- Fix the Rust wiring errors uncovered by the first validation pass
- Record the resulting evidence in canonical status docs

## Evidence
- `cargo fmt --check`
- `cargo test`
- `cargo run -- --list-values`
- `cargo run -- --dev-type backend --project live-provider-check --complexity medium --seed 17 --output-format json --experimental-provider local-demo`
- orphan experimental flag fail-fast: `cargo run -- --experimental-model demo`

## Result
- Rust live-provider catalog exposure is working.
- The guarded local-demo runtime path is working and emits cache/provenance events.
- Orphan experimental flags fail fast with exit code `2`.
- Remaining work is API-backed and consumer-session hardening, not basic runtime wiring.
