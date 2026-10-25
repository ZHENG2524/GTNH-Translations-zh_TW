#!/usr/bin/env python3
"""Verify reviewed terminology against installed 2.8.4 sources and the saved baseline.

Read-only: never edits game files. Run alongside verify_translation.py --reproduce.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
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
    parser.add_argument('--manifest', type=Path, default=ROOT / 'tools/term_calibration_2026-10-25.json')
    parser.add_argument('--skip-diff', action='store_true',
                        help='Check historical sources/values without asserting that it is the only batch since its baseline')
    args = parser.parse_args()
    manifest = json.loads(args.manifest.read_text())
    errors, sources, current, baseline = [], {}, {}, {}
    changes = [r for r in manifest['rows'] if r['before'] != r['after']]
    expected = {(r['file'], r['key']) for r in changes}
    jar = args.game / 'mods' / f"gregtech-{manifest['gregtech_version']}.jar"
    if hashlib.sha256(jar.read_bytes()).hexdigest() != manifest['jar_sha256']:
        errors.append('Installed jar differs from reviewed 2.8.4 jar')
    for filename, digest in manifest.get('jars', {}).items():
        if hashlib.sha256((args.game / 'mods' / filename).read_bytes()).hexdigest() != digest:
            errors.append(f'Installed jar changed: {filename}')
    for filename, digest in manifest.get('supporting_files', {}).items():
        if hashlib.sha256((args.game / filename).read_bytes()).hexdigest() != digest:
            errors.append(f'Supporting configuration changed: {filename}')
    native = manifest.get('native_item_names')
    if native:
        with zipfile.ZipFile(args.game / 'mods' / native['jar']) as other:
            names = entries(other.read(native['entry']).decode('utf-8-sig'))
        for key, value in native['values'].items():
            if names.get(key) != value:
                errors.append(f'Native item name changed: {key}')
    leveling = manifest.get('tool_leveling')
    if leveling:
        config = (args.game / leveling['config']).read_text()
        levels = re.search(r'I:ModifiersAtLevels\s*<([^>]+)>', config)
        if levels is None or [int(x) for x in levels[1].split()] != leveling['extra_modifier_levels']:
            errors.append('Configured modifier levels changed')
        if f"I:maxToolLevel={leveling['max_level']}" not in config or 'B:RandomBonuses=false' not in config:
            errors.append('Configured max tool level or random bonuses changed')
    with zipfile.ZipFile(jar) as archive:
        for row in manifest['rows']:
            source = row['source']
            identity = json.dumps(source, sort_keys=True)
            if identity not in sources:
                if source['kind'] == 'jar':
                    if source.get('jar') and source['jar'] != jar.name:
                        with zipfile.ZipFile(args.game / 'mods' / source['jar']) as other:
                            sources[identity] = entries(other.read(source['entry']).decode('utf-8-sig'))
                    else:
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
    if not args.skip_diff:
        actual = set()
        for rel in subprocess.check_output(['git', 'ls-files', '*.lang'], cwd=ROOT).decode().splitlines():
            old = entries(subprocess.check_output(['git', 'show', manifest['baseline'] + ':' + rel], cwd=ROOT).decode())
            new = entries((ROOT / rel).read_text())
            for key in old.keys() | new.keys():
                if old.get(key) != new.get(key):
                    actual.add((rel, key))
        if actual != expected:
            errors.append(f'Unreviewed or missing changes: {sorted(actual ^ expected)}')
    ore_scan = []
    if manifest.get('ore_prefix_groups'):
        defaults = entries((args.game / 'GregTech_US.lang').read_text())
        translated = entries((ROOT / 'GregTech_zh_TW.lang').read_text())
        for group in manifest['ore_prefix_groups']:
            keys = [k for k, v in defaults.items() if v == group['english'] and k in translated]
            if len(keys) != group['count']:
                errors.append(f"Ore template coverage changed: {group['english']}")
            wrong = [k for k in keys if translated[k] != group['translation']]
            if wrong:
                errors.append(f'Ore template differs: {wrong}')
            ore_scan.append(dict(group, mismatches=len(wrong)))
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
        'ore_prefix_group_scan': ore_scan,
        'diff_checked': not args.skip_diff,
        'source_checks': 'Exact English values from installed jar, runtime defaults and quest JSON',
        'scope': manifest['scope'], 'errors': errors,
    }, ensure_ascii=False, indent=2))
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(main())
