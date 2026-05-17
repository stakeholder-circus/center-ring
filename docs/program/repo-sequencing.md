# Repo sequencing

## Current requirement
- Use `stakeholder-manager` for read-only all-target status, horizon, and feature views.
- Run publication/governance dry-runs for the original ten validated wider-matrix repos before any push.
- Publish only through explicit `stakeholder release ... --execute` actions after validation and CI evidence.
- Do not widen beyond the next-20 set until publication governance and second-pass provider planning are deliberate.

## Next 20 implementation order
1. `ocaml-stakeholder`
2. `typescript-stakeholder`
3. `ruby-stakeholder`
4. `erlang-stakeholder`
5. `scala-stakeholder`
6. `clojure-stakeholder`
7. `c-stakeholder`
8. `cpp-stakeholder`
9. `powershell-stakeholder`
10. `perl-stakeholder`
11. `groovy-stakeholder`
12. `vbnet-stakeholder`
13. `julia-stakeholder`
14. `r-stakeholder`
15. `tcl-stakeholder`
16. `d-stakeholder`
17. `rescript-stakeholder`
18. `fortran-stakeholder`
19. `bash-stakeholder`
20. `php-stakeholder`

## Current next-20 state
- Validated locally: 20 of 20.
- Remaining deterministic implementation targets: none.
- Publication mutation is not a default action; it requires the guarded manager release command with `--execute`.

## Reserve replacements
- `objective-c-stakeholder`
- `v-stakeholder`
- `common-lisp-stakeholder`
- `ada-stakeholder`
