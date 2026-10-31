#!/usr/bin/env python3
"""列出模組 en_US.lang 有、但倉庫與 jar 內 zh_TW 都沒有的 key（含 lang/ 子目錄，例如 HEE 圖鑑）。

掃描既有值只能找到「值是英文」的條目，找不到「整條不存在」的條目；後者要靠本工具。
結果可能含原版語言檔已涵蓋的 key，需再判斷。
Usage: python3 tools/check_key_coverage.py --game /path/to/.minecraft
"""
import argparse
import collections
from pathlib import Path
import re
import zipfile


def keys(text):
    return {line.split("=", 1)[0].strip().lstrip("﻿"): line.split("=", 1)[1]
            for line in text.splitlines() if "=" in line and not line.startswith("#")}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--game", required=True, type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    have = set()
    for path in root.rglob("*.lang"):
        for key in keys(path.read_text(encoding="utf-8", errors="replace")):
            have.add(re.sub(r'^S:"?|"$', "", key))
    english = collections.defaultdict(dict)
    for jar in (args.game / "mods").rglob("*.jar"):
        with zipfile.ZipFile(jar) as archive:
            for name in archive.namelist():
                lower = name.lower()
                if lower.endswith("zh_tw.lang"):
                    have.update(keys(archive.read(name).decode("utf-8", "replace")))
                elif lower.endswith("en_us.lang"):
                    english[jar.name].update(keys(archive.read(name).decode("utf-8", "replace")))
    for jar, entries in sorted(english.items()):
        missing = sorted(k for k, v in entries.items() if k not in have and v.strip())
        if missing:
            print(f"{len(missing):6} {jar}")
            for key in missing[:5]:
                print(f"       {key}")


if __name__ == "__main__":
    main()
