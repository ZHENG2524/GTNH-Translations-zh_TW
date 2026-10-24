#!/usr/bin/env python3
"""伺服器端訊息繁中化：改寫伺服器 mods 資料夾內兩個 jar 的 en_US.lang（伺服器只讀 en_US）。
用法：patch_server_jars.py <伺服器 mods 資料夾> <輸出資料夾>   （原檔不會被修改，請自行備份後替換）
涵蓋：GTNewHorizonsCoreMod（歡迎訊息）、YAMCore（魔法護盾）。"""
import sys, os, glob, zipfile
T = {
 ('GTNewHorizonsCoreMod', 'assets/dreamcraft/lang/en_US.lang'): {
  'dreamcraft.welcome.welcome': '歡迎來到格雷科技：新視野',
  'dreamcraft.welcome.questbook': '任務書有快捷鍵，請檢查你的按鍵設定。',
  'dreamcraft.welcome.gtnh_wiki': 'GTNH 維基連結：',
  'dreamcraft.welcome.click_wiki': '點擊開啟維基！',
  'dreamcraft.welcome.report_bug': '請在 GitHub 上回報錯誤：',
  'dreamcraft.welcome.click_github': '點擊開啟 GitHub！',
  'dreamcraft.welcome.visitdiscord': '歡迎加入我們的 Discord：',
  'dreamcraft.welcome.click_discord': '點擊開啟 Discord！'},
 ('YAMCore', 'assets/yamcore/lang/en_US.lang'): {
  'yamcore.char.protection.give': '一道魔法護盾出現……',
  'yamcore.char.protection.remove': '你的魔法護盾消失了……'},
}
def apply(txt, tr):
    out = []
    for l in txt.split('\n'):
        k = l.split('=', 1)[0]
        out.append(k + '=' + tr[k] if k in tr and '=' in l else l)
    return '\n'.join(out)
mods, outdir = sys.argv[1:3]
os.makedirs(outdir, exist_ok=True)
for (prefix, entry), tr in T.items():
    for src in glob.glob(os.path.join(mods, prefix + '*.jar')):
        dst = os.path.join(outdir, os.path.basename(src))
        with zipfile.ZipFile(src) as zi, zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED) as zo:
            for it in zi.infolist():
                d = zi.read(it.filename)
                if it.filename == entry: d = apply(d.decode('utf-8'), tr).encode('utf-8')
                zo.writestr(it, d)
        print('patched', dst)
