# GTNH 繁體中文（台灣）語言包

GT: New Horizons 的 zh_TW 語言檔。涵蓋既有翻譯，加上補齊剩餘 780 條未翻譯字串（見 `tools/GTNH_remaining_translated.csv`，含 notes 欄）。

## 安裝
把 `config/` 與 `GregTech_zh_TW.lang` 複製到 GTNH 實例根目錄（與既有 `config/txloader/load/...` 合併），遊戲語言選「繁體中文（台灣）」。安裝前請備份。

## 2026-10-24 更新
- `GregTech_zh_TW.lang` 由約 2,900 行補齊到完整（約 6 萬 9 千行），缺漏條目由簡體 `GregTech_zh_CN.lang` 以 OpenCC `s2twp` 轉換而來。
- 補上 GTNH 本體（歡迎訊息等）與其他模組缺少的約 8,900 條繁中；修正 1,500 多條殘留簡體字；`BetterQuesting`、`Biomes O' Plenty` 與 `InGameInfo_zh_TW.xml`（F3 資訊面板）新增繁中。
- 這些新增內容為機器轉換，譯名未逐條校對，歡迎 PR。
- 少數提示（例如 Extra Utilities 的濾鏡說明）寫死在模組程式碼裡，無法用語言檔翻譯；可用 `tools/patch_extrautils.py <原jar> <輸出jar>` 產生修補後的 jar（僅適用 extrautilities-1.2.12，不會修改原檔，請先備份）。

## 伺服器端訊息
連線到伺服器時，歡迎訊息等是由伺服器用英文產生，客戶端改不了。伺服器管理員請見 [GTNH-Server-zh_TW](https://github.com/ZHENG2524/GTNH-Server-zh_TW)。

## 翻譯進度與品質說明
**大部分內容是機器簡轉繁，尚未逐條校對。** 目前狀況：

| 來源 | 條數（約） | 做法 | 校對 |
|---|---|---|---|
| 原有繁中（`zh_TW` 既有檔案） | 約 25 萬行 | 既有翻譯 | 未重新校對 |
| 補齊的 780 條剩餘字串（Blood Magic 書、GuideNH 等） | 780（譯 347、保留原文 421、截斷 6、待查譯名 47） | AI 翻譯，依術語表 | 未校對 |
| GregTech 主語言檔缺漏 | 約 6.8 萬 | 簡體 `zh_CN` 經 OpenCC `s2twp` 轉換 | 未校對 |
| 其他模組缺漏、任務書、Biomes O' Plenty | 約 2.4 萬 | 同上 | 未校對 |
| 殘留簡體字修正 | 約 1,500 | 同上 | 未校對 |

機器轉換可能出現的問題：用詞與台灣慣用不同（例如「倉」與「艙」）、同一個詞前後不一致、簡轉繁後語意不通順、專有名詞譯名與 GTNH 維基不符。

**接下來的計畫：** 逐條校對，優先處理玩家最常看到的內容（物品與材料名稱、機器提示、任務書）。校對完成度會更新在這裡，目前為 0%。

**發現錯誤請開 [issue](../../issues)**，請附上：遊戲內畫面或文字、對應的模組與條目名稱（如果知道）、你認為正確的譯法。

## 已知限制
- 部分字串刻意保留英文（指令、曲名、梗、Mod 名），或標為 TRUNCATED（原始字串被截斷，待從模組 jar 取完整字串）。
- notes 標 `TERM?` 的譯名未經 GTNH 維基核對，歡迎 PR。
- 本專案與 GTNH、各模組作者無官方關係；遊戲文字著作權屬原作者。授權條款尚待確認。

## 授權
本專案的翻譯內容以 [CC BY-NC-SA 4.0](LICENSE)（姓名標示－非商業性－相同方式分享）釋出，與 [GT New Horizons 模組包](https://github.com/GTNewHorizons/GT-New-Horizons-Modpack) 的授權一致。

- 原文（英文與簡體中文來源字串）著作權屬 GTNH 團隊及各模組作者；本專案僅提供繁體中文（台灣）翻譯。
- 各模組語言檔的原始授權可能不同（如 MIT、LGPL 或保留所有權利）。若任何作者要求移除，請開 issue，將立即處理。
- 僅限非商業使用。
