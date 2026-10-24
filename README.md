# GTNH 繁體中文（台灣）語言包

> 本專案由使用者與 [Claude](https://claude.com/claude-code)（Anthropic）協力製作：大部分翻譯為機器簡轉繁加 AI 翻譯，再由人工與 AI 逐步校對。

GT: New Horizons 的 zh_TW 語言檔。涵蓋既有翻譯，加上補齊剩餘 780 條未翻譯字串（見 `tools/GTNH_remaining_translated.csv`，含 notes 欄）。

## 安裝
把 `config/` 與 `GregTech_zh_TW.lang` 複製到 GTNH 實例根目錄（與既有 `config/txloader/load/...` 合併），遊戲語言選「繁體中文（台灣）」。安裝前請備份。

## 用語校準（v0.1.0）
統一為台灣常用說法：鐳射→雷射、末影→終界、下界→地獄、反應堆→反應爐、核聚變→核融合、巖→岩（`tools/normalize_terms.py`，可重跑）。「倉」（Hatch）維持全檔一致，暫不改「艙口」。

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
| 原有繁中（`zh_TW` 既有檔案，含 GregTech 主檔 2,867 行） | 約 10.3 萬行 | 既有翻譯 | 未重新校對 |
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
- 本專案為非官方的社群繁體中文（台灣）語言包，與 GTNH 團隊、各模組作者無官方關係，也未獲其認可或背書。

## 來源與授權說明
### 翻譯來源
- **簡體中文來源**：[GTNewHorizons/GTNH-Translations](https://github.com/GTNewHorizons/GTNH-Translations) 的 `zh_CN`（例如 `GregTech_zh_CN.lang`），經 OpenCC `s2twp` 簡轉繁、用語調整（`tools/normalize_terms.py`）及 AI 輔助處理而來。本倉庫**不含**簡體中文原始檔，只含轉換後的繁體檔。
- **既有繁中**：沿用 GTNH 整合包內既有的 `zh_TW` 語言檔。
- **新增翻譯**：780 條剩餘字串與部分提示為 AI 翻譯，詳見上方「翻譯進度與品質說明」。

### 授權
不同內容適用不同授權，**本倉庫不主張整個倉庫都能以同一授權自由使用**：

| 內容 | 原始授權 | 說明 |
|---|---|---|
| GTNH-Translations（簡體來源） | [GPL-3.0](https://github.com/GTNewHorizons/GTNH-Translations/blob/master/LICENSE) | 由其轉換而來的內容，應遵守 GPL-3.0 |
| GT New Horizons 整合包 | [CC BY-NC-SA 4.0](https://github.com/GTNewHorizons/GT-New-Horizons-Modpack/blob/master/LICENSE) | 整合包內既有語言檔 |
| GregTech 5 Unofficial | LGPL-3.0 | 原文字串來源 |
| 其他各模組 | 各自不同（MIT、LGPL、保留所有權利等） | 以各模組附帶的授權為準 |

- 本倉庫的 [LICENSE](LICENSE) 為 GPL-3.0，與簡體來源 GTNH-Translations 一致。原為 CC BY-NC-SA 4.0，已因兩者不相容而更換。
- **但既有繁中內容源自整合包的 `zh_TW` 語言檔（CC BY-NC-SA 4.0，含非商業條件），改用 GPL-3.0 無法消除這部分的限制。** 在釐清前，本倉庫不主張可商業使用，也不保證整個倉庫能以單一授權完整涵蓋。
- 若任何權利人認為本專案不符其授權條件，請開 issue，將立即調整或移除。
- 本專案免費提供。免費不代表第三方內容可不受原始授權限制。
- 遊戲原文及原始翻譯的著作權屬 GTNH 團隊、各模組作者及原翻譯貢獻者。
