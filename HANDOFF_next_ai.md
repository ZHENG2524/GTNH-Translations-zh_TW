# 交接：GTNH zh_TW 後續處理（給下一個 AI）

> 本檔可公開，不含伺服器位址或個人資訊。最後更新：2026-10-24（提交前複核）。

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

## 材料名稱校對（`Material.*`，1,883 條）
- 2026-10-24 已通讀一遍。修正：`silicon` 生矽→矽、`nano`→奈米、`piko`→皮米、`endstone`→終界石、`crudeoil` 原油渣→原油、鹽酸、六氯二矽烷、二甲基二氯矽烷（`tools/normalize_terms.py` 的 `KEY_FIXES`）。
- 礦物名刻意不含「礦」（如斑銅、輝鉍），因為礦石名稱格式是 `%material礦石`，不要補。
- 機器名（`gt.blockmachines.*`，3,362 條）已合併等級後通讀 1,316 種基名。電壓等級用「超低壓…極上拓壓」、倉室用「倉」、各階用「基礎／進階／精英／終極／史詩」，彼此一致，未改。「泵」未改成「幫浦」（可再討論）。
- **仍待完整校對**：物品名稱格式樣板（已抽查常見約 70 種）、`bw.werkstoff.*` 名稱、`gtplusplus.material.*`、任務書。Werkstoff tooltip 與流體已有下方記錄的局部校對／首輪篩查，並非完全未處理。

## Werkstoff tooltip 校對（2026-10-24）
- 已檢視 `bw.werkstoff.*.tooltip` 445 條：18 條明確英文短句已校準，2 條語意不明（`bw.werkstoff.00096.tooltip`、`bw.werkstoff.10028.tooltip`）保留英文。更正已寫入 `GregTech_zh_TW.lang`，並加入 `tools/normalize_terms.py` 的逐 key 規則。
- 本批尚未遊戲內實測、未提交、未推送。接續校對 `fluid.*` 與任務書常見用語。

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

## 流體與任務介面校對（2026-10-24，接續 tooltip 批次）
- 實際主檔共有 1,310 條 `fluid.*`。本批逐條檢視前 137 條（從 `fluid.1,1dimethylhydrazine` 至 `fluid.dysprosium extracting nano resin`）；修正 `fluid.bastnasite rarer earth oxide suspension` 的「罕土」及 `fluid.dimethyldichlorosilane` 缺少的「二氯」。另外修正 `fluid.hexachlorodisilane`、`fluid.hydrochloricacid_gt5u`，與既有材料名「六氯二矽烷／鹽酸」一致。共改 4 條流體值，未宣稱全數完成。
- 通讀 BetterQuesting 主介面的前 180 行，校準其中 18 條常見介面用語（匯入、偵測／交付、全域、漸層、停用、隊伍管理與主題選單快捷鍵等）。修改檔為 `config/txloader/load/BetterQuesting[betterquesting]/lang/zh_TW.lang`；任務正文、說明頁與其他副本尚未全面校對。
- 流體規則加入 `KEY_FIXES`；介面規則以相對路徑限定的 `FILE_KEY_FIXES` 保存，避免影響其他模組。保留原有 18 條 tooltip 修改與 2 條待查英文。
- 下一步：從 `fluid.enriched naquadah goo` 接續逐條校對；再處理任務章節正文。介面說明頁 `betterquesting.help.page2` 有明顯不通順文字，應核對原文再修正。
- 未遊戲內實測、未提交、未推送。
- 本批編輯前備份：`/private/tmp/gtnh-fluid-quest-20261024-182827/`（含原有未提交修改）。檢查通過：新增 22 條的 key、行數、格式碼與佔位符不變；在暫存副本重跑規則不再產生差異，亦可由備份重現這 22 條修正；`git diff --check` 通過。

## 成批接續校對（2026-10-24，以上一節為基礎）
- 使用者明確表示可一次完成多項工作，不要反覆詢問。例行校對、備份、同步規則與檢查直接執行；有歧義的詞保留並記錄。本次沒有提交、推送、安裝到實例或修改伺服器。
- 本輪處理 72 條語言值，涵蓋 8 個 `.lang` 檔；加上規則、README 與本檔，目前共 11 個未提交檔案。已保留交接時的 18 條 tooltip 修改及兩條待查英文。
- 流體首輪篩查範圍已涵蓋全部 1,310 條：709 條一般流體閱讀檢視（含上一節前 137 條）；601 條熔融／電漿名稱（468／133）以腳本比對材料名，再閱讀不一致或缺少對應材料的條目。這是全量首輪篩查，不代表每條皆已核對英文語意或遊戲行為。
- 明確修正：酵素溶液、熔融白石棉、熔融瑪卡斯、熔融鉛青銅、馬鈴薯汁、蘭姆酒；材料名與任務文案中的「滷水／502膠水／海晶參雜」分別校準成「鹵水／瞬間膠／海晶摻雜」，規則只改值。
- **撤回上一節的一處修改**：`fluid.bastnasite rarer earth oxide suspension` 恢復「氟碳鑭鈰罕土氧化物懸濁液」。任務 `betterquesting.quest.AAAAAAAAAAAAAAAAAAAMCQ.desc` 明確說明 rarer earth 是比稀土更稀有的一組材料，因此須保留「罕土」來區分，不能全域取代成稀土。README 與規則已同步更正。
- 本機原文依據：`GregTech.lang`／`GregTech_US.lang`、`BetterQuesting-3.7.15-GTNH.jar` 內 `assets/betterquesting/lang/en_US.lang` 與 `assets/bq_standard/lang/en_US.lang`；未更動這些來源檔。
- BetterQuesting 的 8 頁內建說明全部依英文重譯，修正 OSS 可同時處理同一任務不同子目標的漏譯、`/bq_admin reset` 的清除完成資料功能、`default` 的儲存／載入說明等。保留指令、參數與資源目錄格式。上一批把 `Advanced` 保留為「全域設定」仍不準確，這輪依原文修正為「進階設定」。另外校準 3 個說明頁標題及標準任務模組的 5 條介面文字。
- 逐篇閱讀現行任務書前 24 篇正文，並比對 `load/betterquesting` 與 `load/minecraft` 的對應描述。僅改明確錯字與用語（如除去收集→出去收集、我麼→我們、自定義→自訂、土豆→馬鈴薯、任務語境的工作列→任務章節）；未將新版文字覆蓋舊版，保留斧頭／鏟子、木鎬／燧石鎬等版本差異。針對各 key 的片語規則保存在 `FILE_KEY_RULES`。
- 已閱讀的現行任務 ID（依檔案順序）：0、1、2、5、6、7、8、9、10、12、13、469、470、471、484、396、397、440、442、444、865、946、1204、1475。下一輪從現行任務檔第 25 篇正文接續，不要單用數字 ID 推斷閱讀順序。
- 待查而保留：15 條 `Filled ... Extracting Nano Resin` 的「滿溢的」應依吸附／再生流程確認；`White Metal` 的「白物質」、`Precious Metals Alloy` 的「稀有金屬合金」、`toluene tetramethyl diisocyanate` 的「PTMEG橡膠粗胚」及幾種熔融魔法材料名稱仍需核對來源。不要用字面 key 強改；本輪未宣稱解決。
- 本輪編輯前備份：`/private/tmp/gtnh-proofread-batch2-20261024-183255/`，含本輪更動前的語言檔、規則與說明文件，保留先前所有未提交內容。
- 驗證：所有變更的 key 與行數不變；一般詞條的格式碼、佔位符、BBCode 與 URL 不變；8 頁重譯說明的格式與指令／參數對照英文來源通過；全部語言檔的暫存副本重跑規則無差異。`git diff --check` 通過。尚未遊戲內實測、未提交、未推送。

## 提交前複核與本機更新（2026-10-24）
- 已重新審核本批全部未提交修改，將說明頁「給玩家一本本指南」修成「給玩家一本指南」，同步校準規則；並修正上方過時的「尚未做」進度敘述與 README 的「校對 0%」舊說法。歧義術語仍依前節保留，未宣稱全專案校對完成。
- 驗證範圍：全部本批語言修改的 key、順序、行數、佔位符、格式與連結；8 頁說明另比對本機英文來源的格式碼及指令；以提交前 HEAD 的語言檔重跑規則，確認可重現整批修改，再跑一次確認無差異。
- 使用者已授權將複核後的修改提交並推送 GitHub，以及備份並更新本機遊戲翻譯。只同步 8 個有差異的翻譯檔；GregTech 檔另保留遊戲執行時新增的 26 個 key，避免覆蓋掉本機獨有條目。遊戲正在執行，磁碟更新不代表已載入，需重新啟動遊戲。
- 本節記錄本次發布與安裝範圍；前方的「未提交／未推送」描述均為各批當時的歷史狀態。實際提交與同步結果以 Git 紀錄及本次回覆為準。
- 最終複核涵蓋本次提交的 109 條語言值、8 個語言檔；299 個語言檔的校準重現與二次重跑檢查通過。


## Wiki 核對與接續發布批次（2026-10-24，最新）
- 使用者授權繼續校對並於核對後發 Release；本批沿用既有測試版定位，版本 v0.1.2，不宣稱全部翻譯正確。
- 開始時確認 HEAD 為 c98b39c6、工作樹乾淨；遊戲 7 個一般檔與倉庫一致，GregTech 主檔差異只有先前保留的 26 個執行時 key。本批未寫入遊戲目錄。
- 修改前已在倉庫外的備份目錄保存完整基準 ZIP 與提交 ID。
- 接續閱讀現行任務第 25–64 篇，共 40 篇；38 篇找到本機英文 JSON，2 篇僅檢視繁中。修改 83 條語言值、4 個語言檔；45 條為 15 種已吸附樹脂的三組名稱，另 38 條為任務描述（含兩份萃取流程術語同步）。
- 第 32、37 篇未找到本機英文來源。第 25、31、35、48、60、63 篇有版本差異或待核實細節，不能視為機制已完全確認。完整術語來源、決定與限制見 docs/PROOFREAD_2026-10-24.md。
- 罕土仍須保留。稀有金屬合金與 PTMEG 橡膠粗胚找到 Wiki 對應而保留；白物質只有索引線索，尚未確認英文對應。兩條歧義 tooltip 仍保留英文。
- 新增 tools/verify_translation.py；299 個語言檔、168,337 個條目完成結構掃描，本批保護字串不變，規則可由基準重現且二次重跑不變。既有 56 個重複鍵條目、2,637 個空白值已記錄，並非本批新增。4 組進階感測卡重複鍵有值衝突，後續待查。
- 下一輪從現行任務第 65 篇正文接續，並回查上述未解項目。尚未遊戲內實測；本批未安裝到遊戲。Release 結果以 GitHub 與最後回覆為準。

## 2026-10-25 接續入口（目前狀態）

- 先讀 `docs/TRANSLATION_PROGRESS.md`、`docs/TERMINOLOGY.md`；舊段落保留歷史背景，最新狀態以上述兩檔為準。
- 使用者明確確認 LV／MV／HV 電壓等級提示已通過遊戲實測，不需重改。其他 Tooltip 不因這項回報一律標為實測完成；本次逐鍵保留全部 26 條舊修復。
- 本次對照 159 條檔案／key 紀錄，3 批修改 60 條、5 個語言檔；精確 before／after／英文來源見 `tools/term_calibration_2026-10-25.json`。新規則已納入 `normalize_terms.py`，遇到第三種未審查值會報衝突。
- 完成單方塊洗礦機、電解說明、電路／電路板、電池箱及熱力離心輸入名稱校準；17 篇主題式任務閱讀只涵蓋術語，連續任務校對仍從第 65 篇接續。
- 不要照錯的英文改 `GT5U.tooltip.purify.2`：本機程式實際用於 crushed 洗淨提示。NetworkAnalyzer 電壓／拓樸候選在本機版本找不到來源，保留待查。
- 本次使用者已授權通過驗證後 commit、push main，無需再次逐項請示；未要求 Release、遊戲安裝或重啟，本次僅更新專案與 GitHub。
