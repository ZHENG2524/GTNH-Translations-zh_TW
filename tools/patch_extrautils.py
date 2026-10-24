#!/usr/bin/env python3
"""Patch hardcoded English tooltips in Extra Utilities 1.2.12 (ItemNodeUpgrade.class) to zh_TW.
Usage: patch_extrautils.py <extrautilities-1.2.12.jar> <output.jar>   (input is never modified)"""
import sys, struct, zipfile
CLS = 'com/rwtema/extrautils/item/ItemNodeUpgrade.class'
TR = {
 'Right click to select items to filter': '右鍵點擊以選擇要過濾的物品',
 'Filters can be placed within other filters to create advanced behaviours': '濾鏡可放入其他濾鏡中，以建立進階行為',
 'Craft with': '合成時搭配',
 'Right-click to change Filter Program': '右鍵點擊以變更濾鏡程式',
 'Craft with a redstone torch to Invert': '與紅石火把一同合成可反轉',
 'Can be placed in normal filters to create advanced behaviours': '可放入一般濾鏡中，以建立進階行為',
 'Unspecified Frequency: You must name this upgrade in an anvil to choose a frequency': '未指定頻率：你必須在鐵砧中為此升級命名以選擇頻率',
 'You cannot use this upgrade until it has a frequency': '此升級在設定頻率之前無法使用',
 'Spectrum set to private': '頻譜已設為私人',
 'Spectrum set to public': '頻譜已設為公開',
}
def patch(data):
    out = bytearray(data[:10]); pos = 10
    count = struct.unpack('>H', data[8:10])[0]; i = 1; n = 0
    while i < count:
        tag = data[pos]
        if tag == 1:
            ln = struct.unpack('>H', data[pos+1:pos+3])[0]
            s = data[pos+3:pos+3+ln]
            try: t = TR.get(s.decode('utf-8'))
            except UnicodeDecodeError: t = None
            if t: b = t.encode('utf-8'); out += b'\x01' + struct.pack('>H', len(b)) + b; n += 1
            else: out += data[pos:pos+3+ln]
            pos += 3+ln
        else:
            size = {3:5,4:5,5:9,6:9,7:3,8:3,9:5,10:5,11:5,12:5,15:4,16:3,18:5}[tag]
            out += data[pos:pos+size]; pos += size
            if tag in (5, 6): i += 1
        i += 1
    out += data[pos:]
    return bytes(out), n
src, dst = sys.argv[1:3]
with zipfile.ZipFile(src) as zi, zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED) as zo:
    for it in zi.infolist():
        d = zi.read(it.filename)
        if it.filename == CLS:
            d, n = patch(d); print('patched strings:', n)
        zo.writestr(it, d)
