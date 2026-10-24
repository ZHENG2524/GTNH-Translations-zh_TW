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
    ("等離子體", "電漿"), ("等離子", "電漿"),
    ("刻蝕", "蝕刻"),
    ("溼", "濕"), ("杆", "桿"),
    ("電子計算機機械方塊", "電腦機械方塊"), ("電子計算機械方塊", "電腦機械方塊"),
    ("計算機", "電腦"),
    ("資料訪問", "資料存取"), ("映象", "鏡像"),
    ("型別", "類型"), ("工作臺", "工作台"), ("平臺", "平台"),
    ("亞熒石", "亞螢石"), ("熒石", "螢光石"), ("熒光", "螢光"),
]

# 只套用在 GregTech_zh_TW.lang 的規則（其他模組的「快取」可能真的是 cache）
GT_ONLY_RULES = [("快取", "緩衝")]

# GregTech_zh_TW.lang 內逐 key 修正（材料名等，值完全取代）
KEY_FIXES = {
    "Material.silicon": "矽",
    "fluid.molten.silicon": "熔融矽",
    "fluid.plasma.silicon": "矽電漿",
    "Material.nano": "奈米",
    "Material.piko": "皮米",
    "Material.hexachlorodisilane": "六氯二矽烷",
    "Material.dimethyldichlorosilane": "二甲基二氯矽烷",
    "Material.crudeoil": "原油",
    "Material.endstone": "終界石",
    "Material.hydrochloricacid_gt5u": "鹽酸",
}

def fix_value(v, stat, extra=()):
    for a, b in list(RULES) + list(extra):
        n = v.count(a)
        if n:
            stat[a] += n
            v = v.replace(a, b)
    return v

def process(path, stat):
    out, changed = [], False
    is_gt = path.name == "GregTech_zh_TW.lang"
    for line in path.read_text(encoding="utf-8").splitlines(keepends=True):
        if "=" in line and not line.lstrip().startswith("#"):
            k, v = line.split("=", 1)
            nv = fix_value(v, stat, GT_ONLY_RULES if is_gt else ())
            if is_gt:
                key = k.strip().removeprefix("S:").strip('"')
                if key in KEY_FIXES and v.rstrip("\n") != KEY_FIXES[key]:
                    nv = KEY_FIXES[key] + ("\n" if v.endswith("\n") else "")
                    stat["key:" + key] += 1
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
