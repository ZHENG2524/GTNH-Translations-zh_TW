#!/usr/bin/env python3
"""Check structural regressions and normalization reproducibility against a Git revision.

These checks do not establish semantic correctness or in-game rendering.
Usage: python3 tools/verify_translation.py --base <revision> [--reproduce]
"""
import argparse
import collections
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tempfile


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args])


def entries(text):
    return [line.split("=", 1) for line in text.splitlines()
            if "=" in line and not line.lstrip().startswith("#")]


def protected(value):
    return {
        "placeholders": re.findall(
            r"%material|%%|%(?:\d+\$)?[-#+ 0,(]*\d*(?:\.\d+)?[a-zA-Z]", value),
        "format_codes": re.findall(r"§.", value),
        "tags": re.findall(r"\[[^\]\r\n]+\]|<[^>\r\n]+>", value),
        "urls": re.findall(r"https?://[^\s\[<>]+", value),
        "escaped_newlines": re.findall(r"\\n|\\r", value),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True)
    parser.add_argument("--reproduce", action="store_true")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    files = [p for p in git(root, "ls-files").decode().splitlines() if p.endswith(".lang")]
    errors, changes, corpus = [], {}, {}
    for rel in files:
        now = (root / rel).read_text(encoding="utf-8")
        before = git(root, "show", f"{args.base}:{rel}").decode("utf-8")
        old, new = entries(before), entries(now)
        counts = collections.Counter(k for k, v in new)
        corpus[rel] = {
            "entries": len(new),
            "duplicate_keys": sum(n - 1 for n in counts.values()),
            "empty_values": sum(not v.strip() for k, v in new),
        }
        if before == now:
            continue
        if len(before.splitlines()) != len(now.splitlines()):
            errors.append(f"{rel}: line count changed")
        if [k for k, v in old] != [k for k, v in new]:
            errors.append(f"{rel}: keys/order changed")
            continue
        count = 0
        for (key, a), (_, b) in zip(old, new):
            if a == b:
                continue
            count += 1
            if not b.strip():
                errors.append(f"{rel}: {key}: newly empty value")
            if protected(a) != protected(b):
                errors.append(f"{rel}: {key}: protected tokens changed")
        changes[rel] = count
    reproduced = None
    if args.reproduce:
        with tempfile.TemporaryDirectory(prefix="gtnh-normalization-") as tmp:
            temp = Path(tmp)
            for rel in files:
                dest = temp / rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(git(root, "show", f"{args.base}:{rel}"))
            command = ["python3", str(root / "tools/normalize_terms.py"), str(temp)]
            subprocess.run(command, check=True, stdout=subprocess.DEVNULL)
            for rel in files:
                # Normalize newline conventions the same way as normalize_terms.py.
                if (temp / rel).read_text() != (root / rel).read_text():
                    errors.append(f"{rel}: normalization did not reproduce current file")
            hashes = {rel: hashlib.sha256((temp / rel).read_bytes()).hexdigest() for rel in files}
            subprocess.run(command, check=True, stdout=subprocess.DEVNULL)
            for rel in files:
                if hashlib.sha256((temp / rel).read_bytes()).hexdigest() != hashes[rel]:
                    errors.append(f"{rel}: second normalization was not idempotent")
            reproduced = not errors
    report = {
        "base": git(root, "rev-parse", args.base).decode().strip(),
        "language_files": len(files),
        "entries": sum(v["entries"] for v in corpus.values()),
        "existing_duplicate_keys": sum(v["duplicate_keys"] for v in corpus.values()),
        "existing_empty_values": sum(v["empty_values"] for v in corpus.values()),
        "changed_values": changes,
        "total_changed_values": sum(changes.values()),
        "reproduction_and_idempotence": reproduced,
        "errors": errors,
        "scope": "Structural regression checks only; existing blanks/duplicates need separate review.",
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
