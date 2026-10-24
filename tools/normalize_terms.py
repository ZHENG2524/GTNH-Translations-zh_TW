#!/usr/bin/env python3
"""Apply Taiwan-usage term normalization to lang values only (keys untouched).
Usage: normalize_terms.py <repo_root>   (edits files in place; use git to review/revert)"""
import sys, pathlib, collections

# 順序有意義：較長詞先換
RULES = [
    ("核聚變", "核融合"), ("聚變", "核融合"),
    ("鐳射", "雷射"),
    ("末影", "終界"),
    ("下界", "地獄"),
    ("反應堆", "反應爐"),
    ("巖", "岩"),
    ("吸 幹 抹 淨", "吸 乾 抹 淨"),
]

def fix_value(v, stat):
    for a, b in RULES:
        n = v.count(a)
        if n:
            stat[a] += n
            v = v.replace(a, b)
    return v

def process(path, stat):
    out, changed = [], False
    for line in path.read_text(encoding="utf-8").splitlines(keepends=True):
        if "=" in line and not line.lstrip().startswith("#"):
            k, v = line.split("=", 1)
            nv = fix_value(v, stat)
            if nv != v:
                changed = True
            line = k + "=" + nv
        out.append(line)
    if changed:
        path.write_text("".join(out), encoding="utf-8")

root = pathlib.Path(sys.argv[1])
stat = collections.Counter()
for p in list(root.glob("*.lang")) + list(root.glob("config/**/*.lang")):
    process(p, stat)
for k, n in stat.most_common():
    print(f"{k}: {n}")
