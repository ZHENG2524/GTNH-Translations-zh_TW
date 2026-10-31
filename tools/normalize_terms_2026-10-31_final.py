#!/usr/bin/env python3
"""2026-10-31 最終用語統一：只改 .lang 的值，不改 key。可重跑（冪等）。"""
import glob, collections
R = [
    ('末地', '終界'), ('刷怪蛋', '生怪蛋'), ('凋靈', '凋零'), ('擾亂棉花', '干擾棉花'),
    ('強化強化', '強化'), ('尖叫黑曜石', '哭泣黑曜石'), ('任務選項卡', '任務分頁'),
    ('馬里奧', '瑪利歐'), ('潛影貝', '界伏蚌'), ('潛影盒', '界伏盒'), ('潛影殼', '界伏殼'),
    ('潛影', '界伏'), ('宇航服', '太空衣'), ('宇航員', '太空人'), ('宇航裝備', '太空裝備'),
    ('宇航盔', '太空頭盔'), ('宇航褲', '太空褲'), ('宇航鞋', '太空靴'), ('訪問', '存取'),
]
cnt = collections.Counter()
for f in glob.glob('**/*.lang', recursive=True):
    L = open(f, encoding='utf-8').read().split('\n'); ch = False
    for i, l in enumerate(L):
        if '=' not in l or l.lstrip().startswith('#'): continue
        k, v = l.split('=', 1); nv = v
        for a, b in R:
            if a in nv: cnt[a] += nv.count(a); nv = nv.replace(a, b)
        if nv != v: L[i] = k + '=' + nv; ch = True
    if ch: open(f, 'w', encoding='utf-8').write('\n'.join(L))
print(dict(cnt))
