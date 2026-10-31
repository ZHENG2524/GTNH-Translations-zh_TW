#!/usr/bin/env python3
"""2026-11-01 大陸用語殘留與待查項收尾：只改 .lang 的值，不改 key。可重跑（冪等）。"""
import collections, glob, re

R = [
    ('許可權', '權限'), ('土豆', '馬鈴薯'), ('大火箭', '火箭筒'), ('一號小行星', '穀神星'),
    ('遊戲的程序', '遊戲的進度'), ('脫氣機', '除氣機'), ('擠壓機', '壓模機'), ('資料棒', '快閃記憶體'), ('。。。', '…'),
]
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
