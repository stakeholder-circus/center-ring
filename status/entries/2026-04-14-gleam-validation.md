# 2026-04-14 - Gleam validation

- Repo: `gleam-stakeholder`
- Slice: wider-matrix local full rewrite tranche
- Native evidence: `python3 scripts/validate_scaffold.py`, `gleam deps download`, `gleam format --check src test`, `gleam test`, and `gleam run -- --list-values` all passed locally.
- Docker evidence: `docker build -t gleam-stakeholder .` passed; runtime smokes passed for `--list-values`, representative classic-six and modern-core JSON output, deterministic same-seed output, and explicit experimental-provider fail-fast.
- Nix evidence: `/nix/var/nix/profiles/default/bin/nix --extra-experimental-features 'nix-command flakes' flake lock` and `/nix/var/nix/profiles/default/bin/nix --extra-experimental-features 'nix-command flakes' run .#check` passed.
- Outcome: `gleam-stakeholder` is now the tenth validated wider-matrix repo, the widening threshold is met, and the next required wave is publication/governance before `ocaml-stakeholder`.
