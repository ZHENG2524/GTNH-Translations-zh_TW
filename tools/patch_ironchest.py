#!/usr/bin/env python3
"""Fix wrong Steel/Silver chest names in IronChest 6.1.6's bundled zh_TW.lang.
The mod labels the Steel chest as 銀箱 (silver). Usage: patch_ironchest.py <IronChest-6.1.6.jar> <output.jar>
(input is never modified)"""
import sys
import zipfile

LANG = 'assets/ironchest/lang/zh_TW.lang'
FIX = {
    'tile.ironchest:STEEL.name=銀箱': 'tile.ironchest:STEEL.name=鋼箱',
    'item.ironchest:COPPERSTEEL.name=銅箱升級成銀箱': 'item.ironchest:COPPERSTEEL.name=銅箱升級成鋼箱',
    'item.ironchest:STEELGOLD.name=銀箱升級成金箱': 'item.ironchest:STEELGOLD.name=鋼箱升級成金箱',
}


def patch(data):
    text = data.decode('utf-8')
    for old, new in FIX.items():
        if text.count(old + '\n') != 1:
            raise SystemExit(f'expected exactly one match: {old}')
        text = text.replace(old + '\n', new + '\n')
    return text.encode('utf-8')


def main():
    src, dst = sys.argv[1], sys.argv[2]
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, 'w') as zout:
        for info in zin.infolist():
            data = zin.read(info.filename)
            if info.filename == LANG:
                data = patch(data)
            zout.writestr(info, data)


if __name__ == '__main__':
    main()
