# Repo sequencing

## Current requirement
- Use `stakeholder-manager` for read-only all-target status, horizon, and feature views.
- Use [language-horizon.md](language-horizon.md) as the 250-language research horizon and [next-20-wave.md](next-20-wave.md) as the concrete batch source.
- Run publication/governance dry-runs for the original ten validated wider-matrix repos before any push.
- Publish only through explicit `stakeholder release ... --execute` actions after validation and CI evidence.
- Do not widen beyond the next-20 set until publication governance and second-pass provider planning are deliberate.
- Select future 20-repo batches from reviewed horizon candidates only after factory dry-run evidence is accepted.
- Treat the first horizon scaffold batch as local-only scaffold evidence, not deterministic runtime validation.

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

## First horizon scaffold batch
- State: scaffolded local-only, not runtime-validated.
- Runtime validation claim: none; these repos have local baseline scaffolds only.
- Repo/language ids:
  1. `v`
  2. `objective-c`
  3. `ada`
  4. `cobol`
  5. `common-lisp`
  6. `raku`
  7. `scheme`
  8. `sml`
  9. `elm`
  10. `purescript`
  11. `hack`
  12. `smalltalk`
  13. `prolog`
  14. `solidity`
  15. `move`
  16. `cairo`
  17. `motoko`
  18. `ballerina`
  19. `haxe`
  20. `vala`
