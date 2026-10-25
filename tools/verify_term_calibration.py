#!/usr/bin/env python3
"""Verify reviewed terminology against installed 2.8.4 sources and the saved baseline.

Read-only: never edits game files. Run alongside verify_translation.py --reproduce.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import subprocess
import zipfile
from verify_translation import protected

ROOT = Path(__file__).resolve().parents[1]


def entries(text):
    result = {}
    for line in text.splitlines():
        if '=' in line and not line.lstrip().startswith('#'):
            key, value = line.split('=', 1)
            result[key.strip().removeprefix('S:').strip('"')] = value
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--game', required=True, type=Path)
    args = parser.parse_args()
    manifest = json.loads((ROOT / 'tools/term_calibration_2026-10-25.json').read_text())
    errors, sources, current, baseline = [], {}, {}, {}
    changes = [r for r in manifest['rows'] if r['before'] != r['after']]
    expected = {(r['file'], r['key']) for r in changes}
    jar = args.game / 'mods' / f"gregtech-{manifest['gregtech_version']}.jar"
    if hashlib.sha256(jar.read_bytes()).hexdigest() != manifest['jar_sha256']:
        errors.append('Installed jar differs from reviewed 2.8.4 jar')
    with zipfile.ZipFile(jar) as archive:
        for row in manifest['rows']:
            source = row['source']
            identity = json.dumps(source, sort_keys=True)
            if identity not in sources:
                if source['kind'] == 'jar':
                    sources[identity] = entries(archive.read(source['entry']).decode('utf-8-sig'))
                elif source['kind'] == 'runtime':
                    sources[identity] = entries((args.game / source['file']).read_text())
                elif source['kind'] == 'quest':
                    data = json.loads((args.game / 'config/betterquesting/DefaultQuests' / source['file']).read_text())
                    props = data['properties:10']['betterquesting:10']
                    sources[identity] = props['name:8' if source['field'] == 'english_name' else 'desc:8']
                else:
                    raise ValueError(f'Unsupported source: {source}')
            english = sources[identity]
            if isinstance(english, dict):
                english = english.get(row['key'])
            if english != row['english']:
                errors.append(f"English changed: {row['file']}: {row['key']}")
            rel = row['file']
            if rel not in current:
                current[rel] = entries((ROOT / rel).read_text())
                baseline[rel] = entries(subprocess.check_output(
                    ['git', 'show', manifest['baseline'] + ':' + rel], cwd=ROOT).decode())
            if current[rel].get(row['key']) != row['after']:
                errors.append(f"Reviewed value differs: {rel}: {row['key']}")
            if baseline[rel].get(row['key']) != row['before']:
                errors.append(f"Baseline differs: {rel}: {row['key']}")
            if protected(row['before']) != protected(row['after']):
                errors.append(f"Protected tokens differ: {rel}: {row['key']}")
    # Reject every language delta outside the reviewed list, including in other files.
    actual = set()
    for rel in subprocess.check_output(['git', 'ls-files', '*.lang'], cwd=ROOT).decode().splitlines():
        old = entries(subprocess.check_output(['git', 'show', manifest['baseline'] + ':' + rel], cwd=ROOT).decode())
        new = entries((ROOT / rel).read_text())
        for key in old.keys() | new.keys():
            if old.get(key) != new.get(key):
                actual.add((rel, key))
    if actual != expected:
        errors.append(f'Unreviewed or missing changes: {sorted(actual ^ expected)}')
    # P0: all 26 previous repairs remain byte-for-byte at the reviewed values.
    prior = json.loads((ROOT / 'tools/gregtech_tooltip_fixes.json').read_text())['fixes']
    for row in prior:
        if entries((ROOT / row['file']).read_text()).get(row['key']) != row['after']:
            errors.append(f"Prior Tooltip repair changed: {row['key']}")
    print(json.dumps({
        'baseline': manifest['baseline'], 'gtnh_version': manifest['gtnh_version'],
        'reviewed_entries': len(manifest['rows']), 'changed_values': len(changes),
        'changed_language_files': len({r['file'] for r in changes}),
        'batches': dict(Counter(r['batch'] for r in changes)),
        'previous_tooltip_repairs_preserved': len(prior),
        'source_checks': 'Exact English values from installed jar, runtime defaults and quest JSON',
        'scope': manifest['scope'], 'errors': errors,
    }, ensure_ascii=False, indent=2))
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(main())
