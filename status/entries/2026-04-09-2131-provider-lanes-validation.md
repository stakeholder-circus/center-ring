# Provider lanes validation entry

- Timestamp: `2026-04-09 21:31 CEST`
- Repos: `javascript-stakeholder`, `java-stakeholder`, `stakeholder-core`, `center-ring`
- State: `co-equal-provider-runtimes-validated-locally-and-reconciled-in-ledgers`
- JavaScript native validation: `npm run lint`, `npm run build`, and `npm test` all passed after hydrating the declared local dependency set with `npm install --no-package-lock`
- JavaScript Docker validation: `docker build -t javascript-stakeholder .` and `npm run docker-test` passed, covering `--list-values`, deterministic JSON, SSE replay, experimental local-demo sessions, and encrypted runtime store/db round-trips
- Java Docker validation: `docker build -t java-stakeholder .` passed through `spotless:check`, `checkstyle:check`, `spotbugs:check`, `test`, and `package`; runtime smokes for `--list-values` and the local demo provider path passed
- Canonical sync: phase/program docs, validation ledgers, and root summaries were updated so JavaScript and Java are recorded as the co-equal provider-runtime lanes with explicit evidence
- Schema/docs validation: `python3 scripts/validate_schemas.py`, `python3 scripts/validate_program_docs.py`, `mkdocs build --strict`, and `center-ring/scripts/validate_program_docs.py` all passed after updating the execution-roadmap schema and re-syncing mirrored program docs
- Publication state: wider-matrix publication remains blocked until at least `10` new full rewrites with tests are complete
- Nix note: the official multi-user macOS installer remains blocked in this PTY because `sudo -n true` still requires a password, so `flake.lock` generation is still deferred
