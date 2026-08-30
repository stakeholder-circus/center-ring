# Interactive runtime capabilities

The canonical machine-readable source is
[`data/runtime-capability-matrix.json`](https://github.com/davidsupan/stakeholder-core/blob/main/data/runtime-capability-matrix.json).
Interactive execution is a separate capability from deterministic parity or
program completeness: a language can be fully rewritten without yet having a
safe browser adapter.

## Placement policy

1. Run in a browser-native runtime when the repository contract can be
   preserved.
2. Use a WASM interpreter or WASI module when WebContainer is not suitable.
3. Use `stakeholder-proxy.s3n.si` only for a runtime that cannot practically run
   in the browser with the required CLI behavior.
4. Do not expose a target as interactive until its exact command allowlist,
   resource bounds, and evidence row are committed.

## Current lanes

| Target | Runtime | Placement | Comparison | Validation | Deployment |
| --- | --- | --- | --- | --- | --- |
| JavaScript | WebContainer | browser | ready | local PASS | pending |
| TypeScript | WebContainer | browser | ready | local PASS | pending |
| ReScript | WebContainer | browser | ready | local PASS | pending |
| Lua | Wasmoon 1.16.0 | browser WASM | ready | local PASS | pending |
| Python | Pyodide 314.0.6 | browser WASM | blocked by missing `--focus-family` | partial PASS (`--list-values`) | pending |
| PowerShell | Bubblewrap + systemd | native proxy | ready | local PASS | pending |

PowerShell is the sole current native residual. Ruby-WASM, PHP-WASM, and other
candidate runtimes are not admitted until an actual repository-level CLI proof
exists.

## Shared lease and abuse controls

- The global budget is **five concurrent sessions across the whole control
  room**, not five per language or runtime class.
- WebContainer, WASM, and native proxy adapters all acquire a lease from the
  same authority before execution.
- A lease is heartbeated every 15 seconds, expires after 45 seconds without a
  heartbeat, and has a hard maximum lifetime of 15 minutes.
- The proxy allows 30 lease requests per subject per minute. The frontend route
  adds a bounded 20 requests per minute per-instance defense.
- Requests, source archives, paths, arguments, process time, output bytes, and
  registry memory are bounded.

## Security boundary

The browser never receives the long-lived proxy control credential. Exact
origin checks, restrictive browser headers, same-origin source acquisition, and
short-lived random lease tokens protect the web boundary. The native residual
runs without network access or ambient capabilities in Bubblewrap, under a
resource-limited DynamicUser systemd unit. Deterministic target and argument
allowlists prevent arbitrary shell execution.

These controls reduce risk; they do not replace production verification.
Public TLS, origin, sixth-session rejection, and PowerShell runtime smokes remain
required after NixOS activation and before the private control-room deployment
is declared active.
