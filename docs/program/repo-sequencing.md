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
- State: scaffolded local-only as a batch.
- Small-tranche native validation: `v-stakeholder` has the deterministic first tranche implemented and validated with V 0.5.1 using `-gc none` (`python3 scripts/validate_scaffold.py`, `make compiler-proof`, `make test`); `objective-c-stakeholder` has the deterministic first tranche implemented and validated with Apple clang plus Foundation (`python3 scripts/validate_scaffold.py`, `make compiler-proof`, `make test`); `common-lisp-stakeholder` has the deterministic first tranche implemented and validated with CLISP (`python3 scripts/validate_scaffold.py`, `make compiler-proof`, `make test`); `scheme-stakeholder` has the deterministic first tranche implemented and validated with Chibi Scheme (`python3 scripts/validate_scaffold.py`, `make compiler-proof`, `make test`); `prolog-stakeholder` has the deterministic first tranche implemented and validated with GNU Prolog (`python3 scripts/validate_scaffold.py`, `make compiler-proof`, `make test`); `haxe-stakeholder` has the deterministic first tranche implemented and validated with Haxe plus Neko (`python3 scripts/validate_scaffold.py`, `make compiler-proof`, `make test`); `sml-stakeholder` has the deterministic first tranche implemented and validated with Poly/ML (`python3 scripts/validate_scaffold.py`, `make compiler-proof`, `make test`); `raku-stakeholder` has the deterministic first tranche implemented and validated with Rakudo/MoarVM (`python3 scripts/validate_scaffold.py`, `make compiler-proof`, `make test`); `vala-stakeholder` has the deterministic first tranche implemented and validated with Vala plus GLib (`python3 scripts/validate_scaffold.py`, `make compiler-proof`, `make test`); `cobol-stakeholder` has the deterministic first tranche implemented and validated with GnuCOBOL (`python3 scripts/validate_scaffold.py`, `make compiler-proof`, `make test`); `elm-stakeholder` has the deterministic first tranche implemented and validated with Elm plus Node port runner (`python3 scripts/validate_scaffold.py`, `make compiler-proof`, `make test`); `purescript-stakeholder` has the deterministic first tranche implemented and validated with PureScript plus Node runner (`python3 scripts/validate_scaffold.py`, `make compiler-proof`, `make test`); `smalltalk-stakeholder` has the deterministic first tranche implemented and validated with GNU Smalltalk (`python3 scripts/validate_scaffold.py`, `make compiler-proof`, `make test`); `solidity-stakeholder` has the deterministic first tranche implemented and validated with solc plus Node runner (`python3 scripts/validate_scaffold.py`, `make compiler-proof`, `make test`); `ballerina-stakeholder` has the deterministic first tranche implemented and validated with Ballerina plus OpenJDK 21 (`python3 scripts/validate_scaffold.py`, `make compiler-proof`, `make test`); `motoko-stakeholder` has the deterministic first tranche implemented and validated with repo-local npm Motoko parser plus Node runner (`python3 scripts/validate_scaffold.py`, `make compiler-proof`, `make test`).
- Remaining runtime validation claim: none for the other 5 repos; they still have local baseline scaffolds only.
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
