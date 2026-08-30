# Workspace Parity Status

Last updated: 2026-08-30 20:15 CEST

## Current interpretation

- Repository phase status describes the validated tranche currently promised by that repository.
- Program status describes progress toward full cross-language generator and provider parity.
- Deterministic behavior, normalized JSON, registry listing, same-seed stability, and explicit provider handling remain the common comparison contract.

## GitHub validation parity

- The 60-repository estate exposes 321 active workflows.
- Latest default-branch evidence is 277 successful workflows, 44 expected event-only or never-run workflows, and zero failures.
- Thirteen public repositories currently bind proven native, Docker, dependency, workflow-security, and supported SAST contexts as required checks.
- The remaining repositories receive required checks only after successful default-branch runs prove stable context names.
- GitHub code-scanning APIs are available for 17 repositories and unavailable for 43. Unsupported languages use language-native analyzers and explicit `N/A unsupported` evidence rather than fake gates.
- The queried estate has zero open Dependabot, code-scanning, and secret-scanning alerts, but a zero-alert result does not replace missing scanner coverage.

## Behavioral parity direction

- Rust remains the source audit anchor and must receive the same eventual generator expansion as every other language.
- Every language target is expected to implement all generator categories in the final program, including AI/provider behavior where the runtime can support it safely.
- Current deterministic-first tranches may use explicit fail-fast provider behavior, but that is an interim phase state rather than the final program state.
- Differences between implementations must remain traceable through canonical families, feature evidence, provenance, and documented gaps.

## Open parity risks

- Full generator depth is uneven across the wider language matrix.
- Live-provider implementation and secure credential/session handling are not yet uniform.
- Source SAST is unavailable or unproven for 43 repositories.
- Sonar coverage is not provisioned and must not be represented as complete.
- Remote runner and browser control-plane integration remain staged until the NixOS proxy is activated and verified.
