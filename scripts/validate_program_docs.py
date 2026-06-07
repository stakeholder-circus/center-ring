#!/usr/bin/env python3
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROGRAM = ROOT / 'docs' / 'program'
REQUIRED = [
    'index.md',
    'current-wave.md',
    'repo-sequencing.md',
    'language-horizon.md',
    'github-governance-state.md',
    'governance-overlays.md',
    'sync-manifest.json',
]
MIRRORED = [
    'current-wave.md',
    'repo-sequencing.md',
    'language-horizon.md',
    'github-governance-state.md',
]


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def main() -> int:
    errors = []
    for name in REQUIRED:
        if not (PROGRAM / name).exists():
            errors.append(f'missing program doc: {name}')

    manifest_path = PROGRAM / 'sync-manifest.json'
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text())
        expected = {entry['path']: entry['sha256'] for entry in manifest.get('mirroredDocs', [])}
        for name in MIRRORED:
            rel = f'docs/program/{name}'
            actual = sha256_bytes((PROGRAM / name).read_bytes())
            if expected.get(rel) != actual:
                errors.append(f'sync-manifest hash mismatch for {rel}')

    overlays = (PROGRAM / 'governance-overlays.md').read_text() if (PROGRAM / 'governance-overlays.md').exists() else ''
    for needle in ('../repo-topology.md', '../security-baseline.md', '../interop-roadmap.md', '../provenance.md'):
        if needle not in overlays:
            errors.append(f'governance-overlays.md missing required reference {needle}')

    if errors:
        for item in errors:
            print(item, file=sys.stderr)
        return 1

    print('center-ring program docs validated')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
