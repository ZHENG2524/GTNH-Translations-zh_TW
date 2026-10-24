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
    ("哈斯特洛依合金", "哈氏合金"),
    ("滷水", "鹵水"),
    ("白物質", "白合金"),
    ("黑物質", "黑金屬"),
    ("罕土", "稀土"),
    ("氫氯酸", "鹽酸"),
    ("土豆", "馬鈴薯"),
    ("氟滌", "氟氣鼓泡處理的"), ("氦滌", "氦氣鼓泡處理的"),
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
    "fluid.2-ethyl-1-hexanol": "2-乙基-1-己醇",
    "fluid.dimethyldichlorosilane": "二甲基二氯矽烷",
    "fluid.hexachlorodisilane": "六氯二矽烷",
    "fluid.hydrochloricacid_gt5u": "鹽酸",
    "fluid.liquid_medium_oil": "中質油",
    "fluid.molten.blackmetal": "熔融黑金屬",
    "fluid.potion.potatojuice": "馬鈴薯汁",
    "fluid.froth.copperflotation": "銅泡沫",
    "fluid.phosgene": "光氣",
    "fluid.squidink": "墨魚汁",
    "gtplusplus.material.Silicon": "矽",
    "gtplusplus.material.BlackMetal": "黑金屬",
    "gtplusplus.material.WhiteMetal": "白合金",
    "gtplusplus.material.EthylCyanoacrylateSuperGlue": "氰基丙烯酸乙酯（瞬間膠）",
    "Material.blackmetal": "黑金屬",
    "bw.werkstoff.00047.name": "鉑族金屬",
    "bw.werkstoff.00049.name": "鉑族金屬渣",
    "bw.werkstoff.00060.name": "浸出殘渣",
    "bw.werkstoff.10004.name": "鈾基流體燃料（枯竭）",
    "bw.werkstoff.10008.name": "釷基流體燃料（枯竭）",
    "bw.werkstoff.10012.name": "鈽基流體燃料（枯竭）",
    "bw.werkstoff.10040.name": "矽岩基流體燃料-MkI（枯竭）",
    "bw.werkstoff.10042.name": "矽岩基流體燃料-MkII（枯竭）",
    "bw.werkstoff.10047.name": "矽岩基流體燃料-MkIII（枯竭）",
    "bw.werkstoff.10049.name": "矽岩基流體燃料-MkIV（枯竭）",
    "bw.werkstoff.10051.name": "矽岩基流體燃料-MkV（枯竭）",
    "bw.werkstoff.10056.name": "低純度矽岩乳液",
    "bw.werkstoff.10058.name": "低純度矽岩溶液",
    "bw.werkstoff.10062.name": "高純度矽岩溶液",
    "bw.werkstoff.10069.name": "高純度富集矽岩溶液",
    "bw.werkstoff.10074.name": "低純度磷酸超能矽岩",
    "bw.werkstoff.10075.name": "高純度超能矽岩溶液",
    "bw.werkstoff.10076.name": "低純度硫酸超能矽岩",
    "bw.werkstoff.10077.name": "低純度硫酸超能矽岩",
    "bw.werkstoff.10117.name": "矽岩基流體燃料-MkVI（枯竭）",
    "bw.werkstoff.11031.name": "獨居石稀土沉澱",
    "bw.werkstoff.11038.name": "磷酸釷精礦",
    "bw.werkstoff.11045.name": "海藻副產品",
    "bw.werkstoff.11113.name": "氟碳鑭鈰稀土氧化物",
    "bw.werkstoff.11114.name": "氮化氟碳鑭鈰稀土氧化物",
    "bw.werkstoff.11115.name": "氟碳鑭鈰稀土氧化物懸浮液",
    "bw.werkstoff.11116.name": "釤稀土精礦",
    "bw.werkstoff.11117.name": "釹稀土精礦",
    "bw.werkstoff.11446.name": "鑭精礦",
    "bw.werkstoff.11447.name": "鐠精礦",
    "bw.werkstoff.11449.name": "釹精礦",
    "bw.werkstoff.11450.name": "鉕精礦",
    "bw.werkstoff.11451.name": "銪精礦",
    "bw.werkstoff.11452.name": "釓精礦",
    "bw.werkstoff.11453.name": "鋱精礦",
    "bw.werkstoff.11454.name": "鏑精礦",
    "bw.werkstoff.11455.name": "鈥精礦",
    "bw.werkstoff.11456.name": "鉺精礦",
    "bw.werkstoff.11457.name": "銩精礦",
    "bw.werkstoff.11458.name": "鐿精礦",
    "bw.werkstoff.11459.name": "鎦精礦",
    "bw.werkstoff.11467.name": "含雜質氯化鑭",
    "bw.werkstoff.11472.name": "稀土殘渣",
    "bw.werkstoff.29905.name": "光氣",
    "bw.werkstoff.00043.tooltip": "你是認真的嗎？",
    "bw.werkstoff.10022.tooltip": "熔融核心……",
    "bw.werkstoff.10025.tooltip": "遠遠不夠",
    "bw.werkstoff.10026.tooltip": "還需要加工",
    "bw.werkstoff.10027.tooltip": "誰需要這個？",
    "bw.werkstoff.10035.tooltip": ">>> 危險 <<<",
    "bw.werkstoff.10039.tooltip": "第一步",
    "bw.werkstoff.10040.tooltip": "第一步（已踏出）",
    "bw.werkstoff.10041.tooltip": "六百億千瓦時",
    "bw.werkstoff.10042.tooltip": "六百億千瓦時（已耗盡）",
    "bw.werkstoff.10046.tooltip": "力量壓倒一切",
    "bw.werkstoff.10047.tooltip": "力量不再壓倒一切",
    "bw.werkstoff.10048.tooltip": "擊落太陽",
    "bw.werkstoff.10049.tooltip": "擊落太陽（已完成）",
    "bw.werkstoff.10050.tooltip": "結束",
    "bw.werkstoff.10051.tooltip": "結束（字面上）",
    "bw.werkstoff.10116.tooltip": "未來",
    "bw.werkstoff.10117.tooltip": "未來（已實現）",
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
