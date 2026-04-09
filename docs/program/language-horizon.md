# 101-language horizon

This inventory is the long-range language roadmap for the stakeholder rewrite program.

- Total languages tracked: 101
- Ambitious future-wave candidates: 22
- Canonical structured source: `stakeholder-core/data/language-horizon.json`
- Concrete repo-backed implementation ledger stays in `stakeholder-core/data/language-matrix.json`.

## Tier 0: implemented now

- Count: 7
- Tier id: `tier-0`

| Language | Status | Focus | Target class | Why use | Promotion prerequisites |
| --- | --- | --- | --- | --- | --- |
| Rust | implemented | systems-minimalism, interop | canonical | Canonical systems baseline and source-of-truth runtime behavior. | Already canonical; promotion is not applicable. |
| Java | implemented | ecosystem-reach, interop | parity-target | Depth anchor on the JVM with the richest dedicated family coverage. | Already active as the depth anchor; keep provider hooks deferred until follower modern-core stabilizes. |
| C# | implemented | ecosystem-reach, interop | parity-target | Mainstream .NET parity lane for enterprise tooling and cross-platform CLI work. | Already active; next promotion is follower modern-core completion. |
| Go | implemented | systems-minimalism, ecosystem-reach | parity-target | Low-friction deterministic CLI baseline with strong operational ergonomics. | Already active; next promotion is follower modern-core completion. |
| JavaScript | implemented | interop, ecosystem-reach | reference-sidecar | Provider and web-terminal sidecar plus portable runtime reference. | Already active as the sidecar; do not promote it into the deterministic parity queue. |
| Python | implemented | ecosystem-reach, interop | parity-target | Readable scripting and data-oriented parity lane with broad ecosystem reach. | Already active; next promotion is follower modern-core completion. |
| Swift | implemented | systems-minimalism, ecosystem-reach | parity-target | Cross-platform Apple/server systems-adjacent lane with explicit value semantics. | Already active; next promotion is follower modern-core completion. |

## Tier 1: approved repo queue and scaffolds

- Count: 12
- Tier id: `tier-1`

| Language | Status | Focus | Target class | Why use | Promotion prerequisites |
| --- | --- | --- | --- | --- | --- |
| F# | scaffold-approved | correctness, ecosystem-reach | scaffold-target | Functional .NET contrast with immutable-first pipelines and exact-output parity against C#. | Needs a repo scaffold with imported Rust history, governance baseline, Nix flake, packet-refresh completion, and a clear first parity tranche before promotion into active implementation. |
| Zig | scaffold-approved | systems-minimalism, interop | scaffold-target | Explicit-allocation, no-surprises systems baseline for deterministic CLI execution. | Needs a repo scaffold with imported Rust history, governance baseline, Nix flake, packet-refresh completion, and a clear first parity tranche before promotion into active implementation. |
| Haskell | scaffold-approved | correctness, research | scaffold-target | Correctness oracle for a pure-core deterministic event pipeline. | Needs a repo scaffold with imported Rust history, governance baseline, Nix flake, packet-refresh completion, and a clear first parity tranche before promotion into active implementation. |
| Kotlin | scaffold-approved | ecosystem-reach, interop | scaffold-target | Null-safe JVM sibling to Java for parity and sealed-model comparisons. | Needs a repo scaffold with imported Rust history, governance baseline, Nix flake, packet-refresh completion, and a clear first parity tranche before promotion into active implementation. |
| Elixir | scaffold-approved | interop, research | scaffold-target | Actor-based message-passing lane for concurrency and pipeline stress. | Needs a repo scaffold with imported Rust history, governance baseline, Nix flake, packet-refresh completion, and a clear first parity tranche before promotion into active implementation. |
| OCaml | scaffold-approved | correctness, ecosystem-reach | scaffold-target | Compiler-style pragmatic FP lane with ADTs and exhaustive matching. | Needs a repo scaffold with imported Rust history, governance baseline, Nix flake, packet-refresh completion, and a clear first parity tranche before promotion into active implementation. |
| Nim | scaffold-approved | ecosystem-reach, interop | scaffold-target | Pragmatic compiled scripting with macros for boilerplate control. | Needs a repo scaffold with imported Rust history, governance baseline, Nix flake, packet-refresh completion, and a clear first parity tranche before promotion into active implementation. |
| Crystal | scaffold-approved | ecosystem-reach, interop | scaffold-target | Readable static-typed scripting lane for prototyping and Ruby comparison. | Needs a repo scaffold with imported Rust history, governance baseline, Nix flake, packet-refresh completion, and a clear first parity tranche before promotion into active implementation. |
| Dart | scaffold-approved | ecosystem-reach, interop | scaffold-target | Portable CLI lane with future UI adjacency and structured tooling. | Needs a repo scaffold with imported Rust history, governance baseline, Nix flake, packet-refresh completion, and a clear first parity tranche before promotion into active implementation. |
| Lua | scaffold-approved | embeddability, interop | scaffold-target | Embeddable lightweight full-parity target with explicit ordering discipline. | Needs a repo scaffold with imported Rust history, governance baseline, Nix flake, packet-refresh completion, and a clear first parity tranche before promotion into active implementation. |
| Gleam | scaffold-approved | correctness, interop | scaffold-target | Typed BEAM lane with simpler ergonomics than raw Erlang and explicit determinism. | Needs a repo scaffold with imported Rust history, governance baseline, Nix flake, packet-refresh completion, and a clear first parity tranche before promotion into active implementation. |
| Zeta | research-spike | research, systems-minimalism | spike-only | Ownership-plus-ADT research spike for future systems-language evaluation. | Needs toolchain viability proof, deterministic fixture compatibility, and a successful spike before any parity commitment. |

## Tier 2: near-term practical candidates

- Count: 25
- Tier id: `tier-2`

| Language | Status | Focus | Target class | Why use | Promotion prerequisites |
| --- | --- | --- | --- | --- | --- |
| C | planned | systems-minimalism, interop | parity-target | Native C-ABI baseline for FFI and deterministic low-level comparisons. | Needs a differentiated value beyond Tier 0 and Tier 1, a stable cross-platform CLI toolchain, and fixture-harness proof before scaffold promotion. |
| C++ | planned | systems-minimalism, interop | parity-target | Widespread systems and FFI coverage for performance-sensitive ecosystems. | Needs a differentiated value beyond Tier 0 and Tier 1, a stable cross-platform CLI toolchain, and fixture-harness proof before scaffold promotion. |
| TypeScript | planned | ecosystem-reach, interop | parity-target | Typed JavaScript contrast for CLI and tooling without abandoning the JS ecosystem. | Needs a differentiated value beyond Tier 0 and Tier 1, a stable cross-platform CLI toolchain, and fixture-harness proof before scaffold promotion. |
| PHP | planned | ecosystem-reach | parity-target | Ubiquitous server-side scripting coverage across legacy and modern web estates. | Needs a differentiated value beyond Tier 0 and Tier 1, a stable cross-platform CLI toolchain, and fixture-harness proof before scaffold promotion. |
| Ruby | planned | ecosystem-reach | parity-target | Expressive DSL-heavy scripting lane with strong readability pressure. | Needs a differentiated value beyond Tier 0 and Tier 1, a stable cross-platform CLI toolchain, and fixture-harness proof before scaffold promotion. |
| Scala | planned | correctness, ecosystem-reach | parity-target | Advanced JVM hybrid FP/OOP comparison for richer type-system tradeoffs. | Needs a differentiated value beyond Tier 0 and Tier 1, a stable cross-platform CLI toolchain, and fixture-harness proof before scaffold promotion. |
| Clojure | planned | correctness, interop | parity-target | Immutable Lisp on the JVM for data-first parity design experiments. | Needs a differentiated value beyond Tier 0 and Tier 1, a stable cross-platform CLI toolchain, and fixture-harness proof before scaffold promotion. |
| Erlang | planned | interop, research | parity-target | Raw BEAM baseline for fault-tolerant actor concurrency without Elixir abstractions. | Needs a differentiated value beyond Tier 0 and Tier 1, a stable cross-platform CLI toolchain, and fixture-harness proof before scaffold promotion. |
| Julia | planned | ecosystem-reach, research | parity-target | Scientific and numeric generation lane for analytical scenario families. | Needs a differentiated value beyond Tier 0 and Tier 1, a stable cross-platform CLI toolchain, and fixture-harness proof before scaffold promotion. |
| R | planned | ecosystem-reach | parity-target | Data reporting and statistical scripting lane for data-heavy output families. | Needs a differentiated value beyond Tier 0 and Tier 1, a stable cross-platform CLI toolchain, and fixture-harness proof before scaffold promotion. |
| Perl | planned | ecosystem-reach, interop | parity-target | Text-heavy scripting lineage for old-school ops and parsing comparisons. | Needs a differentiated value beyond Tier 0 and Tier 1, a stable cross-platform CLI toolchain, and fixture-harness proof before scaffold promotion. |
| PowerShell | planned | interop, ecosystem-reach | parity-target | Windows-native automation lane for enterprise CLI parity and ops workflows. | Needs a differentiated value beyond Tier 0 and Tier 1, a stable cross-platform CLI toolchain, and fixture-harness proof before scaffold promotion. |
| Bash | planned | interop, embeddability | parity-target | POSIX shell orchestration baseline for glue-layer and process-heavy interop. | Needs a differentiated value beyond Tier 0 and Tier 1, a stable cross-platform CLI toolchain, and fixture-harness proof before scaffold promotion. |
| D | planned | systems-minimalism, interop | parity-target | Pragmatic compiled systems hybrid with modern syntax and native tooling reach. | Needs a differentiated value beyond Tier 0 and Tier 1, a stable cross-platform CLI toolchain, and fixture-harness proof before scaffold promotion. |
| V | planned | systems-minimalism, research | parity-target | Simple compiled systems contender with low-ceremony syntax. | Needs a differentiated value beyond Tier 0 and Tier 1, a stable cross-platform CLI toolchain, and fixture-harness proof before scaffold promotion. |
| ReScript | planned | interop, ecosystem-reach | parity-target | Typed JS/OCaml pipeline for frontend-adjacent deterministic CLI experimentation. | Needs a differentiated value beyond Tier 0 and Tier 1, a stable cross-platform CLI toolchain, and fixture-harness proof before scaffold promotion. |
| Objective-C | planned | interop, ecosystem-reach | parity-target | Cocoa/C runtime legacy interop and Apple ecosystem breadth. | Needs a differentiated value beyond Tier 0 and Tier 1, a stable cross-platform CLI toolchain, and fixture-harness proof before scaffold promotion. |
| Groovy | planned | ecosystem-reach, interop | parity-target | JVM scripting lane with Gradle adjacency and dynamic metaprogramming. | Needs a differentiated value beyond Tier 0 and Tier 1, a stable cross-platform CLI toolchain, and fixture-harness proof before scaffold promotion. |
| Visual Basic .NET | planned | ecosystem-reach | parity-target | Conservative enterprise .NET coverage for long-tail organizational parity. | Needs a differentiated value beyond Tier 0 and Tier 1, a stable cross-platform CLI toolchain, and fixture-harness proof before scaffold promotion. |
| Ada | planned | correctness, systems-minimalism | parity-target | Safety-critical explicitness for high-assurance CLI/runtime design. | Needs a differentiated value beyond Tier 0 and Tier 1, a stable cross-platform CLI toolchain, and fixture-harness proof before scaffold promotion. |
| Fortran | planned | ecosystem-reach, research | parity-target | HPC and numerical lineage for deterministic batch and scientific workloads. | Needs a differentiated value beyond Tier 0 and Tier 1, a stable cross-platform CLI toolchain, and fixture-harness proof before scaffold promotion. |
| COBOL | planned | ecosystem-reach, interop | parity-target | Enterprise batch lineage for auditability and legacy integration scenarios. | Needs a differentiated value beyond Tier 0 and Tier 1, a stable cross-platform CLI toolchain, and fixture-harness proof before scaffold promotion. |
| Tcl | planned | embeddability, interop | parity-target | Embeddable glue scripting with a long history in tooling and automation. | Needs a differentiated value beyond Tier 0 and Tier 1, a stable cross-platform CLI toolchain, and fixture-harness proof before scaffold promotion. |
| Common Lisp | planned | research, embeddability | parity-target | Macro-rich dynamic systems lane for powerful code-generation and DSL work. | Needs a differentiated value beyond Tier 0 and Tier 1, a stable cross-platform CLI toolchain, and fixture-harness proof before scaffold promotion. |
| Raku | planned | ecosystem-reach, research | parity-target | Modern Perl-family expressiveness for text-rich and grammar-heavy experiments. | Needs a differentiated value beyond Tier 0 and Tier 1, a stable cross-platform CLI toolchain, and fixture-harness proof before scaffold promotion. |

## Tier 3: ecosystem-breadth candidates

- Count: 35
- Tier id: `tier-3`

| Language | Status | Focus | Target class | Why use | Promotion prerequisites |
| --- | --- | --- | --- | --- | --- |
| Scheme | future-wave | correctness, research | parity-target | Minimal Lisp semantics for a smaller functional baseline than Common Lisp. | Needs sustained ecosystem demand, a credible CI story, and a clear interop or paradigm payoff before entering the scaffold queue. |
| Standard ML | future-wave | correctness, research | parity-target | Classic typed FP baseline for ML-family comparisons beyond OCaml. | Needs sustained ecosystem demand, a credible CI story, and a clear interop or paradigm payoff before entering the scaffold queue. |
| Elm | future-wave | correctness, ecosystem-reach | parity-target | Frontend purity and compiler-guarantee lane for message/update discipline. | Needs sustained ecosystem demand, a credible CI story, and a clear interop or paradigm payoff before entering the scaffold queue. |
| PureScript | future-wave | correctness, interop | parity-target | Stronger typed FP path into JavaScript runtimes. | Needs sustained ecosystem demand, a credible CI story, and a clear interop or paradigm payoff before entering the scaffold queue. |
| Hack | future-wave | ecosystem-reach | parity-target | Typed PHP derivative for large web estates with stronger type discipline. | Needs sustained ecosystem demand, a credible CI story, and a clear interop or paradigm payoff before entering the scaffold queue. |
| Smalltalk | future-wave | research, ecosystem-reach | parity-target | Pure object-model lineage for message-sending and live-system contrasts. | Needs sustained ecosystem demand, a credible CI story, and a clear interop or paradigm payoff before entering the scaffold queue. |
| Prolog | future-wave | correctness, research | parity-target | Logic-programming contrast for rule-heavy generation and search workflows. | Needs sustained ecosystem demand, a credible CI story, and a clear interop or paradigm payoff before entering the scaffold queue. |
| Solidity | future-wave | interop, ecosystem-reach | parity-target | Smart-contract determinism and EVM execution model comparison. | Needs sustained ecosystem demand, a credible CI story, and a clear interop or paradigm payoff before entering the scaffold queue. |
| Move | future-wave | correctness, interop | parity-target | Resource-oriented smart-contract language for safer asset/state reasoning. | Needs sustained ecosystem demand, a credible CI story, and a clear interop or paradigm payoff before entering the scaffold queue. |
| Cairo | future-wave | research, interop | parity-target | zkVM-oriented language for proof-generation and constraint-system experiments. | Needs sustained ecosystem demand, a credible CI story, and a clear interop or paradigm payoff before entering the scaffold queue. |
| Motoko | future-wave | interop, research | parity-target | Actor-oriented Internet Computer language for distributed state-machine contrasts. | Needs sustained ecosystem demand, a credible CI story, and a clear interop or paradigm payoff before entering the scaffold queue. |
| Ballerina | future-wave | interop, ecosystem-reach | parity-target | Integration/API-first language for service choreography and schema-heavy workflows. | Needs sustained ecosystem demand, a credible CI story, and a clear interop or paradigm payoff before entering the scaffold queue. |
| Haxe | future-wave | interop, ecosystem-reach | parity-target | Multi-target typed tooling language for cross-runtime code generation. | Needs sustained ecosystem demand, a credible CI story, and a clear interop or paradigm payoff before entering the scaffold queue. |
| Vala | future-wave | interop, ecosystem-reach | parity-target | GObject/C interop lane for native desktop and GNOME-adjacent systems. | Needs sustained ecosystem demand, a credible CI story, and a clear interop or paradigm payoff before entering the scaffold queue. |
| AssemblyScript | future-wave | interop, embeddability | parity-target | TypeScript-to-Wasm path for WebAssembly parity and CLI embedding. | Needs sustained ecosystem demand, a credible CI story, and a clear interop or paradigm payoff before entering the scaffold queue. |
| GDScript | future-wave | ecosystem-reach, embeddability | parity-target | Godot-native scripting lane for developer-tooling and gameplay-style orchestration ideas. | Needs sustained ecosystem demand, a credible CI story, and a clear interop or paradigm payoff before entering the scaffold queue. |
| AngelScript | future-wave | embeddability, interop | parity-target | Embeddable gameplay scripting language for host-driven deterministic hooks. | Needs sustained ecosystem demand, a credible CI story, and a clear interop or paradigm payoff before entering the scaffold queue. |
| Squirrel | future-wave | embeddability, interop | parity-target | Lightweight embeddable VM language for scripting host integration. | Needs sustained ecosystem demand, a credible CI story, and a clear interop or paradigm payoff before entering the scaffold queue. |
| Wren | future-wave | embeddability, interop | parity-target | Small embeddable object language with a deliberately compact runtime. | Needs sustained ecosystem demand, a credible CI story, and a clear interop or paradigm payoff before entering the scaffold queue. |
| Janet | future-wave | embeddability, research | parity-target | Embeddable Lisp systems scripting lane with compact deployment characteristics. | Needs sustained ecosystem demand, a credible CI story, and a clear interop or paradigm payoff before entering the scaffold queue. |
| Io | future-wave | research, embeddability | parity-target | Prototype-based message-passing language for object-model research contrasts. | Needs sustained ecosystem demand, a credible CI story, and a clear interop or paradigm payoff before entering the scaffold queue. |
| Neko | future-wave | interop, research | parity-target | VM-oriented dynamic language with historical multi-target relevance. | Needs sustained ecosystem demand, a credible CI story, and a clear interop or paradigm payoff before entering the scaffold queue. |
| ABAP | future-wave | ecosystem-reach, interop | parity-target | SAP enterprise workflow coverage for long-tail business-system integrations. | Needs sustained ecosystem demand, a credible CI story, and a clear interop or paradigm payoff before entering the scaffold queue. |
| Apex | future-wave | ecosystem-reach, interop | parity-target | Salesforce-native enterprise workflow lane for cloud business platform parity. | Needs sustained ecosystem demand, a credible CI story, and a clear interop or paradigm payoff before entering the scaffold queue. |
| Delphi/Object Pascal | future-wave | ecosystem-reach | parity-target | RAD native lineage for Windows-heavy enterprise and legacy tooling. | Needs sustained ecosystem demand, a credible CI story, and a clear interop or paradigm payoff before entering the scaffold queue. |
| Forth | future-wave | systems-minimalism, research | parity-target | Stack-machine minimalism for extreme small-runtime and explicit execution experiments. | Needs sustained ecosystem demand, a credible CI story, and a clear interop or paradigm payoff before entering the scaffold queue. |
| Factor | future-wave | research, correctness | parity-target | Modern concatenative language with richer tooling than classic Forth. | Needs sustained ecosystem demand, a credible CI story, and a clear interop or paradigm payoff before entering the scaffold queue. |
| J | future-wave | research, ecosystem-reach | parity-target | Terse array programming lane for compact data transformations. | Needs sustained ecosystem demand, a credible CI story, and a clear interop or paradigm payoff before entering the scaffold queue. |
| APL | future-wave | research, correctness | parity-target | Dense array semantics for high-compression numeric and data transformation experiments. | Needs sustained ecosystem demand, a credible CI story, and a clear interop or paradigm payoff before entering the scaffold queue. |
| Wolfram Language | future-wave | ecosystem-reach, research | parity-target | Symbolic/reporting workflow coverage with a strong notebook heritage. | Needs sustained ecosystem demand, a credible CI story, and a clear interop or paradigm payoff before entering the scaffold queue. |
| ActionScript | future-wave | research, ecosystem-reach | parity-target | Event-driven VM lineage for historical tooling and runtime comparisons. | Needs sustained ecosystem demand, a credible CI story, and a clear interop or paradigm payoff before entering the scaffold queue. |
| CFML | future-wave | ecosystem-reach | parity-target | Legacy web platform coverage for long-tail server ecosystems. | Needs sustained ecosystem demand, a credible CI story, and a clear interop or paradigm payoff before entering the scaffold queue. |
| PostScript | future-wave | research, embeddability | parity-target | Document and graphics programming lineage with stack-based execution. | Needs sustained ecosystem demand, a credible CI story, and a clear interop or paradigm payoff before entering the scaffold queue. |
| Logo | future-wave | research, embeddability | parity-target | Educational and DSL lineage for command-style stateful generation patterns. | Needs sustained ecosystem demand, a credible CI story, and a clear interop or paradigm payoff before entering the scaffold queue. |
| ObjectScript | future-wave | ecosystem-reach, interop | parity-target | InterSystems enterprise/database language for healthcare and business-system reach. | Needs sustained ecosystem demand, a credible CI story, and a clear interop or paradigm payoff before entering the scaffold queue. |

## Tier 4: ambitious future-wave candidates

- Count: 22
- Tier id: `tier-4`

| Language | Status | Focus | Target class | Why use | Promotion prerequisites |
| --- | --- | --- | --- | --- | --- |
| Idris 2 | future-wave | correctness, research | parity-target | Dependent-type language for stronger executable correctness claims. | Needs toolchain maturity, deterministic CLI viability, and a successful research spike before entering the scaffold queue. |
| Agda | future-wave | correctness, research | parity-target | Proof-oriented executable specification lane for formal semantics. | Needs toolchain maturity, deterministic CLI viability, and a successful research spike before entering the scaffold queue. |
| Lean 4 | future-wave | correctness, research | parity-target | Theorem-prover-to-program pipeline for highly formal correctness experiments. | Needs toolchain maturity, deterministic CLI viability, and a successful research spike before entering the scaffold queue. |
| Coq/Gallina | future-wave | correctness, research | parity-target | Proof assistant lane for verified extraction and behavioral specification. | Needs toolchain maturity, deterministic CLI viability, and a successful research spike before entering the scaffold queue. |
| ATS | future-wave | correctness, systems-minimalism | parity-target | Low-level systems language with theorem-backed types and explicit memory reasoning. | Needs toolchain maturity, deterministic CLI viability, and a successful research spike before entering the scaffold queue. |
| Roc | future-wave | correctness, research | parity-target | Modern functional effect-discipline language with strong UX ambitions. | Needs toolchain maturity, deterministic CLI viability, and a successful research spike before entering the scaffold queue. |
| Grain | future-wave | interop, research | parity-target | Typed WebAssembly-first language for Wasm runtime parity experiments. | Needs toolchain maturity, deterministic CLI viability, and a successful research spike before entering the scaffold queue. |
| Koka | future-wave | correctness, research | parity-target | Algebraic-effects research language for explicit effect tracking. | Needs toolchain maturity, deterministic CLI viability, and a successful research spike before entering the scaffold queue. |
| Unison | future-wave | research, interop | parity-target | Content-addressed code model for distributed semantics research. | Needs toolchain maturity, deterministic CLI viability, and a successful research spike before entering the scaffold queue. |
| Mercury | future-wave | correctness, research | parity-target | High-assurance logic/functional hybrid with strong mode and determinism systems. | Needs toolchain maturity, deterministic CLI viability, and a successful research spike before entering the scaffold queue. |
| Hare | future-wave | systems-minimalism, research | parity-target | Systems-simplicity language aiming at explicit safety and small runtimes. | Needs toolchain maturity, deterministic CLI viability, and a successful research spike before entering the scaffold queue. |
| Vale | future-wave | correctness, systems-minimalism | parity-target | Verified low-level systems programming lane with strong proof ambitions. | Needs toolchain maturity, deterministic CLI viability, and a successful research spike before entering the scaffold queue. |
| Dafny | future-wave | correctness, research | parity-target | Spec-first verified implementation language with solver-backed guarantees. | Needs toolchain maturity, deterministic CLI viability, and a successful research spike before entering the scaffold queue. |
| Futhark | future-wave | research, systems-minimalism | parity-target | Data-parallel compiler-oriented language for numeric and GPU-adjacent experiments. | Needs toolchain maturity, deterministic CLI viability, and a successful research spike before entering the scaffold queue. |
| Jakt | future-wave | systems-minimalism, research | parity-target | Safety-oriented systems-language experiment with modern toolchain ambitions. | Needs toolchain maturity, deterministic CLI viability, and a successful research spike before entering the scaffold queue. |
| Hylo | future-wave | systems-minimalism, research | parity-target | Ownership-and-effects next-wave systems design experiment. | Needs toolchain maturity, deterministic CLI viability, and a successful research spike before entering the scaffold queue. |
| P | future-wave | correctness, interop | parity-target | Protocol and state-machine correctness language for orchestration-heavy designs. | Needs toolchain maturity, deterministic CLI viability, and a successful research spike before entering the scaffold queue. |
| Pony | future-wave | correctness, interop | parity-target | Capability-safe actor concurrency language for strong isolation guarantees. | Needs toolchain maturity, deterministic CLI viability, and a successful research spike before entering the scaffold queue. |
| Carp | future-wave | research, systems-minimalism | parity-target | Lisp plus systems-style memory discipline for macro-heavy native experiments. | Needs toolchain maturity, deterministic CLI viability, and a successful research spike before entering the scaffold queue. |
| Kitten | future-wave | correctness, research | parity-target | Typed concatenative language with effects for stack-based correctness exploration. | Needs toolchain maturity, deterministic CLI viability, and a successful research spike before entering the scaffold queue. |
| Noir | future-wave | research, interop | parity-target | zk circuit language for deterministic proof-workflow experimentation. | Needs toolchain maturity, deterministic CLI viability, and a successful research spike before entering the scaffold queue. |
| Verse | future-wave | research, embeddability | parity-target | Ambitious simulation and semantics research target with unusual execution ideas. | Needs toolchain maturity, deterministic CLI viability, and a successful research spike before entering the scaffold queue. |
