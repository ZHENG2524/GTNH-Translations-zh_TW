#!/usr/bin/env python3
"""2026-11-01 大陸用語殘留與待查項收尾：只改 .lang 的值，不改 key。可重跑（冪等）。"""
import collections, glob, re

R = [
    ('許可權', '權限'), ('土豆', '馬鈴薯'), ('大火箭', '火箭筒'), ('一號小行星', '穀神星'),
    ('遊戲的程序', '遊戲的進度'), ('脫氣機', '除氣機'), ('擠壓機', '壓模機'), ('資料棒', '快閃記憶體'), ('。。。', '…'),
    # 第二批：已對照 jar 英文與原版 zh_TW 的異體詞
    ('艙口', '倉'), ('幫浦', '泵'), ('能量倉', '能源倉'), ('耐久值', '耐久度'), ('萃取機', '提取機'),
    ('用戶端', '客戶端'), ('烈焰人', '烈焰使者'), ('粘', '黏'), ('生態域', '生物群系'),
    ('太陽能電池板', '太陽能板'), ('電鋸', '鏈鋸'), ('發動機', '引擎'),
    ('先進電路基板', '高階電路基板'), ('先進處理器基板', '高階處理器基板'),
]
RX = [
    (re.compile(r'(?<![冶精提熔])煉金(?!屬|錠|塊|粒)'), '鍊金'),  # 冶煉金屬等不是 alchemy
    (re.compile(r'(?<!亞)螢石'), '螢光石'),  # Fluorite 譯氟石，螢石皆指 Glowstone；亞螢石是專名
    (re.compile(r'(?<!蜘)蛛網'), '蜘蛛網'),
    (re.compile(r'(?<!渦輪)機殼'), '機械方塊'),  # Railcraft 蒸汽渦輪機殼是 Housing
]
LOOTING = re.compile(r'搶奪(?!的|者)')  # Looting；Infernal Mobs 的 Snagging 保留
KEEP_KEYS = {'botania.versioning.flavour33'}  # 工具欄梗：Ask Toolbar
REPORT = re.compile(r'(進行|請|向我們|向模組作者|github|Github)反饋')
KEY_R = {'betterquesting.quest.AAAAAAAAAAAAAAAAAAAMXQ.desc': [('氦離子', '氦電漿')]}
cnt = collections.Counter()
for f in glob.glob('**/*.lang', recursive=True):
    L = open(f, encoding='utf-8').read().split('\n')
    changed = False
    for i, l in enumerate(L):
        if '=' not in l or l.lstrip().startswith('#'):
            continue
        k, v = l.split('=', 1)
        nv = v
        if k.strip() not in KEEP_KEYS:
            nv = nv.replace('工具欄', '快捷欄')
        for rx, b in RX:
            nv = rx.sub(b, nv)
        nv = LOOTING.sub('掠奪', nv)
        for a, b in R + KEY_R.get(k.strip(), []):
            if a in nv:
                cnt[a] += nv.count(a)
                nv = nv.replace(a, b)
        if '反饋' in nv:
            nv = REPORT.sub(lambda m: m.group(1) + '回報', nv)
            cnt['反饋'] += nv.count('反饋')
            nv = nv.replace('反饋', '回饋')
        if nv != v:
            L[i] = k + '=' + nv
            changed = True
    if changed:
        open(f, 'w', encoding='utf-8').write('\n'.join(L))
print(dict(cnt))
