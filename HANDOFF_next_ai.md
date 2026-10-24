# 交接：GTNH zh_TW 後續處理（給下一個 AI）

> 本檔可公開，不含伺服器位址或個人資訊。最後更新：2026-10-24（v0.1.0 發布時）。

## 專案概況
- GTNH 2.8.4 的繁體中文（台灣）語言包；內容幾乎全是機器簡轉繁（OpenCC `s2twp`）+ AI 翻譯，**逐條校對進度仍很低**。
- 語言檔位置：`GregTech_zh_TW.lang`（GregTech 主檔，Forge Configuration 格式 `S:"key"=value`）、`config/txloader/load/<模組>[modid]/lang/zh_TW.lang`。
- 與 Claude 協力製作；commit 皆帶 `Co-Authored-By: Claude`。

## 技術注意事項
1. GregTech 有自己的語言檔，遊戲啟動時會改寫它。原本只有約 2,900 行，是遊戲中大量英文名稱的主因。
2. 寫死在程式碼裡的字串無法用語言檔翻譯，只能改 class（例：`tools/patch_extrautils.py`）。
3. 連線到伺服器時的歡迎訊息等由伺服器產生，客戶端改不了（見伺服器端倉庫）。
4. 把 `zh_TW.lang` 塞進模組 jar 對 StatCollector 類字串沒有效果，不要再試。
5. 沒有 opencc 指令時：`python3 -m venv v && v/bin/pip install opencc-python-reimplemented`，用 `s2twp`。

## 已完成
- 780 條剩餘字串（`tools/GTNH_remaining_translated.csv`）。
- GregTech 主檔補齊、各模組缺漏補齊、殘留簡體修正、BetterQuesting／Biomes O' Plenty／InGameInfo 新增。
- **第一輪用語校準**（`tools/normalize_terms.py`，只改值不改 key，可重跑）：

  | 原 | 改為 | 約處數 |
  |---|---|---|
  | 鐳射 | 雷射 | 820 |
  | 末影 | 終界 | 1,035 |
  | 下界 | 地獄 | 777 |
  | 反應堆 | 反應爐 | 1,527 |
  | 核聚變／聚變 | 核融合 | 918 |
  | 巖 | 岩 | 1,405 |
  | 等離子（體） | 電漿 | 1,264 |
  | 刻蝕 | 蝕刻 | 16 |
  | 溼 | 濕 | 425 |
  | 杆 | 桿 | 1,103 |
  | 熒石（Glowstone） | 螢光石 | 163 |

## 材料名稱校對（`Material.*`，1,883 條）
- 2026-10-24 已通讀一遍。修正：`silicon` 生矽→矽、`nano`→奈米、`piko`→皮米、`endstone`→終界石、`crudeoil` 原油渣→原油、鹽酸、六氯二矽烷、二甲基二氯矽烷（`tools/normalize_terms.py` 的 `KEY_FIXES`）。
- 礦物名刻意不含「礦」（如斑銅、輝鉍），因為礦石名稱格式是 `%material礦石`，不要補。
- **尚未做**：物品名稱格式樣板（`gt.metaitem.*` 的 `M粉/M板/M錠` 等，已看過常見的約 70 種，沒發現問題）、機器名（`gt.blockmachines.*`）、`bw.werkstoff.*`、`gtplusplus.material.*`、`fluid.*`、任務書。

## 刻意保留的決定（想改前先討論）
- Hatch／倉室：全檔統一用「**倉**」（輸入倉、能源倉，約 1,800 處），不改「艙口」，因為一致性比換字重要。Bus=匯流排。
- Naquadah=矽岩、Duranium=鏗鈾等沿用簡體來源的音／意譯，沒有維基繁中依據，未改。
- Casing 在 GregTech 檔內為「機械方塊」（約 1,500 處，沿用簡體來源譯法）。

## 待辦（依優先序）
1. 逐條校對：玩家最常看的物品／材料名、機器提示、任務書。注意一簡對多繁（发/髮、干/幹/乾、后/後、里/裡）。
2. 約 1,200 條仍為英文（Ztones 528、GregTech 155、ServerUtilities 106、CraftPresence 76、Botania 74…），多為專有名詞，需逐條判斷。
3. TRUNCATED 6 條、TERM? 47 條（見 `tools/GTNH_remaining_translated.csv` 的 notes 欄），需從 jar 取完整字串並查 GTNH 維基（gtnh.miraheze.org）。
4. 佔位符：與 zh_CN 對照 `%s/%d/%f` 後有約 100 處不同，抽查多為既有繁中來自較新版本（zh_CN 較舊）造成，尚未逐條確認；`§`、`\n`、`<BR>` 未做自動檢查。
5. 尚未掃描：jar 內自帶語言檔、`config` 底下其他設定檔、NEI／任務 JSON。
6. 模組更新後，Extra Utilities 補丁與 GregTech 語言檔需重做。

## 與使用者互動的偏好
- 使用者用繁體中文，回覆簡潔，說清楚動了哪些檔。
- 改使用者檔案前先備份；公開倉庫、改歷史、重啟伺服器前先確認。
- 不要把使用者本名、Gmail、伺服器位址放上 GitHub。commit 作者：`ZHENG2524 <347185527+ZHENG2524@users.noreply.github.com>`。
