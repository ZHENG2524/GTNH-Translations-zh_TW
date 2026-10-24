#!/usr/bin/env python3
"""Validate this version's Tooltip repairs against the installed jar and Git baseline.

Usage: python3 tools/verify_gregtech_tooltips.py --game /path/to/.minecraft
Read-only: never modifies the game, jar, or tracked translations.
The broad scan reports candidates, not semantic proof of every translation.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
FORMAT = re.compile(r'%(?:(\d+)\$)?([-#+ 0,(<]*)(\d*)(?:\.(\d+))?([a-zA-Z%])')
NUMERIC = re.compile(r'%(\d+\$)?[\d.]*[df]')
RELATED = re.compile(r'voltage|ampera|energy|\bEU\b|tier|battery|transformer|dynamo|capacitor|hatch|cable|tooltip|gt\.tileentity|GT5U\.infodata', re.I)


def entries(text, forge=False):
    result = {}
    for line in text.splitlines():
        if '=' not in line or line.lstrip().startswith('#'):
            continue
        key, value = line.split('=', 1)
        key = key.strip()
        if forge:
            if not key.startswith('S:'):
                continue
            key = key[2:].strip('"')
        result[key] = value
    return result


def signature(value):
    """Compare argument identity, flags and precision, allowing explicit reordering."""
    result, ordinary, previous = [], 0, None
    for match in FORMAT.finditer(value):
        index, flags, width, precision, conversion = match.groups()
        if conversion in ('%', 'n'):
            result.append((0, '', '', '', conversion))
            continue
        if '<' in flags:
            argument = previous
        elif index:
            argument = int(index)
        else:
            ordinary += 1
            argument = ordinary
        previous = argument
        result.append((argument, flags.replace('<', ''), width, precision or '', conversion))
    return sorted(result)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--game', type=Path, required=True)
    parser.add_argument('--base', default='HEAD')
    args = parser.parse_args()
    manifest = json.loads((ROOT / 'tools/gregtech_tooltip_fixes.json').read_text())
    jar = args.game / 'mods' / f"gregtech-{manifest['gregtech_version']}.jar"
    errors, candidates, coverage = [], [], {}
    repairs = manifest['fixes']
    with zipfile.ZipFile(jar) as archive:
        english = {}
        for name in archive.namelist():
            if not name.endswith('/lang/en_US.lang'):
                continue
            domain = name.split('/')[1]
            en = entries(archive.read(name).decode('utf-8-sig'))
            english[domain] = en
            coverage[domain] = {'english_keys': len(en), 'comparisons': 0, 'related_comparisons': 0}
            for path in ROOT.glob('config/txloader/**/*.lang'):
                folder = path.parent.parent.name
                if folder != domain and not folder.endswith(f'[{domain}]'):
                    continue
                for key, value in entries(path.read_text()).items():
                    if key not in en:
                        continue
                    coverage[domain]['comparisons'] += 1
                    if not RELATED.search(key + ' ' + en[key]):
                        continue
                    coverage[domain]['related_comparisons'] += 1
                    # Candidates include literal percentages and multi-line cache translations.
                    if signature(NUMERIC.sub(lambda m: '%' + (m[1] or '') + 's', en[key])) != signature(NUMERIC.sub(lambda m: '%' + (m[1] or '') + 's', value)):
                        candidates.append({'file': path.relative_to(ROOT).as_posix(), 'key': key,
                                           'english': en[key], 'translation': value, 'review': (
                                               'Outside this repair: biological item / tool mode text' if key.startswith('tooltip.labparts.') or key == 'gt.vajra.tooltip.silk_touch' else
                                               'Valid: same argument array is passed to each cached Tooltip line' if key.startswith('GT5U.machines.stalled_stuttering.tooltip.') else
                                               'Literal percentage text, not a formatter parameter' if key in ('fog.upgrade.text.19', 'gt.blockmachines.multimachine.em.transformer.desc.2') else
                                               'Requires call-site review')})
        for row in repairs:
            if english[row['domain']].get(row['key']) != row['english']:
                errors.append(f"English source changed: {row['key']}")
            current = entries((ROOT / row['file']).read_text()).get(row['key'])
            if current != row['after']:
                errors.append(f"Repair missing: {row['key']}")
            if row.get('call_mode') != 'literal' and signature(row['english']) != signature(row['after']):
                errors.append(f"Argument contract differs: {row['key']}")

    # Prove that changes are precisely the reviewed repairs and preserve structure.
    files = subprocess.check_output(['git', 'ls-files', '*.lang'], cwd=ROOT).decode().splitlines()
    allowed = {(r['file'], r['key']): r for r in repairs}
    changes = []
    with tempfile.TemporaryDirectory(prefix='gtnh-tooltip-check-') as temp:
        target = Path(temp)
        for rel in files:
            before = subprocess.check_output(['git', 'show', f'{args.base}:{rel}'], cwd=ROOT).decode()
            after = (ROOT / rel).read_text()
            destination = target / rel
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(before)
            if len(before.splitlines()) != len(after.splitlines()):
                errors.append(f'Line count changed: {rel}')
            old, new = entries(before), entries(after)
            if list(old) != list(new):
                errors.append(f'Key order changed: {rel}')
            for key in old.keys() & new.keys():
                if old[key] == new[key]:
                    continue
                changes.append((rel, key))
                row = allowed.get((rel, key))
                if row is None or (old[key], new[key]) != (row['before'], row['after']):
                    errors.append(f'Unreviewed change: {rel}: {key}')
        subprocess.run(['python3', str(ROOT / 'tools/normalize_terms.py'), temp], check=True, stdout=subprocess.DEVNULL)
        for rel in files:
            if (target / rel).read_text() != (ROOT / rel).read_text():
                errors.append(f'Normalization does not reproduce: {rel}')
        hashes = {rel: hashlib.sha256((target / rel).read_bytes()).hexdigest() for rel in files}
        subprocess.run(['python3', str(ROOT / 'tools/normalize_terms.py'), temp], check=True, stdout=subprocess.DEVNULL)
        if any(hashlib.sha256((target / rel).read_bytes()).hexdigest() != hashes[rel] for rel in files):
            errors.append('Normalization is not idempotent')

    generated = args.game / 'GregTech.lang'
    generated_counts = None
    if generated.exists():
        defaults = entries(generated.read_text(), forge=True)
        translated = entries((ROOT / 'GregTech_zh_TW.lang').read_text(), forge=True)
        common = defaults.keys() & translated.keys()
        generated_counts = {'compared_keys': len(common), 'related_keys': sum(bool(RELATED.search(k + ' ' + defaults[k])) for k in common),
                            'note': 'Runtime-generated defaults can contain historical keys; candidates need code verification.'}
    print(json.dumps({'jar_sha256': hashlib.sha256(jar.read_bytes()).hexdigest(),
                      'gregtech_version': manifest['gregtech_version'], 'language_files_checked': len(files),
                      'reviewed_repairs': len(repairs), 'changed_values': len(changes),
                      'coverage': coverage, 'generated_defaults': generated_counts,
                      'remaining_asset_candidates': candidates,
                      'errors': errors}, ensure_ascii=False, indent=2))
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(main())
