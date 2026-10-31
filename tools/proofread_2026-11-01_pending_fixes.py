#!/usr/bin/env python3
"""Apply the reviewed fixes for the quest "pending" lists (idempotent).

Only values change. Item names were checked against the installed jars; items that
depend on unverified mechanics stay as they are, see docs/PROOFREAD_2026-11-01_PENDING.md.
Usage: python3 tools/proofread_2026-11-01_pending_fixes.py [repository]
"""
from pathlib import Path
import re
import sys

QUEST_FILES = (
    "config/txloader/load/betterquesting/lang/zh_TW.lang",
    "config/txloader/forceload/betterquesting/lang/zh_TW.lang",
    "config/txloader/load/minecraft/lang/zh_TW.lang",
)

# Every language file.
GLOBAL = (
    (r"傳送帶", "輸送帶"),
    (r"高階別", "高等級"),
)

# Quest text only.
QUEST = (
    (r"工作列", "分頁"),  # OpenCC turned 任务栏 (quest tab) into taskbar
    (r"%n譯者：？？？", ""),
    (r"最“後期“", "最“後期”"),
    (r"”多方塊結構“", "“多方塊結構”"),
    (r"您", "你"),
    (r"(?<!真)實時", "即時"),
    (r"實時騰空", "隨時清空"),
    (r"即時騰空", "隨時清空"),
    (r"嘛([？?])", r"嗎\1"),
    (r"好麼", "好嗎"),
    (r"想做就做唄", "想做就做吧"),
    (r"如果你是歐皇", "如果你運氣很好"),
    (r"如果你足夠歐", "如果你運氣夠好"),
    (r"如果你比較歐", "如果你運氣比較好"),
    (r"歐皇可以直接", "運氣好的話可以直接"),
    (r"凱夫拉", "凱芙拉"),
    (r"雪玲花", "雪鈴花"),
    (r"路由口管道", "路由介面管道"),
    (r"孵化器", "恆溫箱"),
    (r"鑿制", "鑿製"),
    (r"紅色合金錠", "紅石合金錠"),
    (r"龍芯圖紙", "龍之核心圖紙"),
    (r"可以相容這些活效能量的材料", "可以承受這些能量的材料"),
    (r"蕨的灌木", "荊棘灌木"),
    (r"開門水晶", "傳送水晶"),
    (r"煤炭蜂", "煤蜂"),
    (r"他的(§o)?覆蓋物", r"它的\1覆蓋物"),
    (r"這是純非", "這純屬運氣不好"),
    (r"同一只", "同一隻"),
    (r"得到一只", "得到一隻"),
    (r"煉獄(雄蜂|公主蜂)", r"地獄\1"),
    (r"自己做方柏霓多了", "自己做方便多了"),
    (r"4個終界錠可提升", "4個終末錠可提升"),
    (r"你有了臺電腦", "你有了一臺電腦"),
    (r"嘗試監控器顯示", "嘗試將監控器顯示"),
    (r"苯環發電", "苯發電"),
    (r"有某種蠟溢位了", "有多到用不完的蠟"),
    (r"它對於血液兵工廠（Blood Arsenal）來說是一個非常有用的工具", "它是血魔法師武器庫中不可或缺的工具"),
    (r"熱離以回收", "熱力離心以回收"),
    (r"將其熱離", "將其熱力離心"),
    (r"數以萬計的工業TNT", "上萬組工業TNT"),
    (r"睡鞋", "滲透鞋"),
    (r"你的護甲升級[，,]火焰保護和爆炸保護[！!]", "最好給護甲升級火焰保護和爆炸保護！"),
    (r"你需要用血腥神秘塊建造兩格高的柱子", "你需要再加一圈血符文，並在每個角落用血腥神秘塊建造兩格高的柱子"),
    (r"Time\.\.。”", "Time...”"),
    (r"中毒，被困住並失去生命值", "中毒、被向上拖、困住並失去生命值"),
    (r"可以用手破壞經過的岩穴藤蔓", "可以徒手破壞岩穴藤蔓"),
    (r"渦輪捕蟲網3000\.$", "渦輪捕蟲網3000。"),
    (r"%n§%n%n3\.", "%n3."),
    (r"AE2,你可以在控制器", "AE2，你可以在控制器"),
    (r"壓縮輸入匯流排", "超級輸入匯流排"),
    (r"光子晶元", "光學富集單晶矽"),
    (r"神秘4模組的神秘塊", "神秘4模組的神秘方塊"),
    (r"即可製成手杖", "即可製成權杖"),
    (r"將其裝備在手杖上", "將其裝備在權杖上"),
)

# Single keys: the same words mean something else elsewhere.
KEYS = {
    "betterquesting.quest.AAAAAAAAAAAAAAAAAAACwg.name": ((r"元素粉筆", "以太粉筆"),),
    "gt.NetworkAnalyzer.mode.topology": ((r"拓補", "拓撲"),),
    "gt.NetworkAnalyzer.mode.voltage": ((r"電流", "電壓"),),
    "gt.recipe.circuitassembler.description": ((r"易裝卸！", "到處都在取放！"),),
    "betterquesting.quest.TP2PEGHQRnGKgKYFziEjrg.desc": (
        (r"僅可用於(§.)*%n：", r"僅可用於：\1%n"),
    ),
}


def apply(rules, value):
    for pattern, replacement in rules:
        value = re.sub(pattern, replacement, value)
    return value


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    paths = sorted(root.glob("config/txloader/**/zh_TW.lang")) + [root / "GregTech_zh_TW.lang"]
    quest = {root / p for p in QUEST_FILES}
    total = 0
    for path in paths:
        raw = path.read_bytes().decode("utf-8")
        lines = raw.split("\n")
        changed = 0
        for i, line in enumerate(lines):
            if "=" not in line or line.lstrip().startswith("#"):
                continue
            ending = "\r" if line.endswith("\r") else ""
            key, value = line[:len(line) - len(ending)].split("=", 1)
            new = apply(GLOBAL, value)
            if path in quest:
                new = apply(QUEST, new)
            new = apply(KEYS.get(key.strip().removeprefix("S:"), ()), new)
            if new != value:
                lines[i] = f"{key}={new}{ending}"
                changed += 1
        if changed:
            path.write_bytes("\n".join(lines).encode("utf-8"))
            print(f"{changed:5d}  {path.relative_to(root)}")
            total += changed
    print(f"{total:5d}  total")


if __name__ == "__main__":
    main()
