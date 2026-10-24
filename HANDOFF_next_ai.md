# 交接：GTNH zh_TW 後續處理（給下一個 AI）

> 本檔可公開，不含伺服器位址或個人資訊。最後更新：2026-10-24（授權與進度更新）。

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
  | 型別 | 類型 | 1,749 |
  | 工作臺／平臺 | 工作台／平台 | 606 |
  | 計算機 | 電腦 | 309 |
  | 資料訪問 | 資料存取 | 52 |
  | 映象 | 鏡像 | 34 |
  | 快取（僅 GregTech 檔，Buffer） | 緩衝 | 80 |

- 本輪依台灣材料與工業用語，將材料／物品／任務文字中的白物質、黑物質、罕土等舊譯統一為白合金、黑金屬、稀土；並校準鹵水、哈氏合金等名稱。相關項目已更新 `GregTech_zh_TW.lang` 與對應模組、任務語言檔。

## 材料名稱校對（`Material.*`，1,883 條）
- 2026-10-24 已通讀一遍。修正：`silicon` 生矽→矽、`nano`→奈米、`piko`→皮米、`endstone`→終界石、`crudeoil` 原油渣→原油、鹽酸、六氯二矽烷、二甲基二氯矽烷（`tools/normalize_terms.py` 的 `KEY_FIXES`）。
- 礦物名刻意不含「礦」（如斑銅、輝鉍），因為礦石名稱格式是 `%material礦石`，不要補。
- 機器名（`gt.blockmachines.*`，3,362 條）已合併等級後通讀 1,316 種基名。電壓等級用「超低壓…極上拓壓」、倉室用「倉」、各階用「基礎／進階／精英／終極／史詩」，彼此一致，未改。「泵」未改成「幫浦」（可再討論）。
- `bw.werkstoff.*.name`（402 條）已逐筆做第一輪台灣用語校準，修正 44 條；包含「低純／高純」→「低純度／高純度」、「罕土」→「稀土」、「X精」→「X精礦」、「枯竭的」→「枯竭」、`carbonyl chloride`→「光氣」。另先翻譯 18 條可辨識的英文趣味 tooltip；化學式 tooltip 未逐條校對，少數語意不明的英文梗仍保留原文。
- GT++ 材料名（`gtplusplus.material.*`，325 條）已做第一輪逐筆校準；其中黑金屬、鹵水、哈氏合金、白合金、瞬間膠等名稱已修正並統一用語。這只是材料名稱校準，未涵蓋其他模組名與遊戲內顯示驗證。
- **尚未做**：物品名稱格式樣板（`gt.metaitem.*` 的 `M粉/M板/M錠` 等，已看過常見的約 70 種，沒發現問題）、化學式 tooltip、`fluid.*` 全檔、任務書。

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

## 進度更新（2026-10-24）
- 客戶端倉庫最新 commit 為 `3861541`；新增 246 個模組資料夾的授權初步核對表 `tools/MOD_LICENSES.csv`，README 已說明核對限制。伺服器端倉庫最新 commit 為 `f44c4d8`。
- `v0.1.1` 已標記，包含材料名稱與 `gt.blockmachines.*` 機器名稱校對及用語調整。以上兩類已完成；舊待辦中的「機器提示/機器名」不應再當作尚未處理。
- 授權來源問題仍未解決：既有繁中來源有 CC BY-NC-SA 4.0 條款，而簡體來源倉庫是 GPL-3.0；README 已明確保留此限制，尚未取得權利人答覆或完成拆分／重寫／移除。不要自行宣稱整包可商用或已解決授權，也不要替使用者聯絡第三方。本輪使用者指定優先逐行校準台灣用語。
- `tools/MOD_LICENSES.csv` 是依名稱搜尋 GitHub 倉庫授權檔的初步結果，不是法律結論；名稱匹配有誤可能。接著可抽查高風險及無明確授權項目，並記錄來源網址與判定依據。
- 本輪持續補校 `fluid.*`：修正 2-乙基-1-己醇、二甲基二氯矽烷、六氯二矽烷、鹽酸、中質油、黑金屬、馬鈴薯、光氣、墨魚汁、銅浮選泡沫等名稱；並將「氟滌／氦滌」改為氣體鼓泡處理的表述。`gtplusplus.material.Silicon` 的「矽晶」修正為「矽」，已加進 `tools/normalize_terms.py` 的 `KEY_FIXES`。
- 本輪逐筆校準 `bw.werkstoff.*.name` 402 條，精確修正 44 條：補「度」使純度詞自然、將誤用「罕土」統一為「稀土」、將選礦濃縮物名稱補成「精礦」、整理耗竭燃料標籤、用台灣常用「光氣」及「殘渣」等；另翻譯 18 條可辨識的英文趣味 tooltip。公式 tooltip 未逐條校對，少數語意不明的英文梗保留原文。曾發現這 44 條精確修正缺少 `=` 分隔符，已全部補正並檢查 70,537 條 `S:` 語言項目，格式錯誤為 0。`GregTech_zh_TW.lang` 修改前備份在 `/private/tmp/GregTech_zh_TW.lang.pre-bw-calibration-20261024`。
- 本輪也逐筆檢視 `gtplusplus.material.*` 325 個名稱，校準黑金屬、鹵水、哈氏合金、白合金、瞬間膠等詞，並將「哈斯特洛依合金」統一為台灣常用「哈氏合金」。相同材料名在 GregTech、GT++ 物品及任務描述中一併統一；另依既有校準表修正台灣常見用語。備份在 `/private/tmp/gtpp-terms-20261024/`；本批 GregTech 主檔另備份於 `/private/tmp/GregTech_zh_TW.lang.pre-gtpp-calibration-20261024`。
- 其他仍待做：化學式 tooltip、`fluid.*` 全檔、任務書/物品文字校對；仍為英文的值；780 條清單的 6 個 TRUNCATED、47 個 TERM?；與英文原文逐條檢查佔位符；掃描 jar 內語言檔及其他設定/任務資料。
- 開始後續翻譯校對前，先讀 README 的授權狀態與本交接檔的「刻意保留的決定」。避免重做已完成的 Material 與 `gt.blockmachines.*` 校對。尚未重新完整跑遊戲驗證用語變更。
