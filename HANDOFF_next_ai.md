# GTNH zh_TW 最新交接入口

更新：2026-10-31（漏譯補齊＋第2073–2162篇閱讀）。此文件可公開；不含私人路徑或憑證。

## 最新一批（接續入口）

- **任務書全部讀完**：第 2163–3859 篇由 43 個唯讀 agent 對照英文，主流程套用 192 條修正（見 `docs/PROOFREAD_2026-10-31_QUESTS2163-3859.md`，含 193 項待查）。第 HxQ 任務的 `[warn]…[/note]` 標籤已修成成對，驗證工具會對此報「protected tokens changed」，屬預期。備份 `backups/quests-rest-20261031/`。下方「下一篇第2163篇」已過期。

- **漏譯補齊**：全庫掃描無漢字的值（化學式、專有名詞、玩笑話、指令用法保留不譯）後，補譯 **162 條**真正漏譯的 GT 介面／機器提示／NAC 說明／諸神之鍛爐說明、EOH 配方頁、Hodgepodge、StructureLib、GuideNH 區域魔杖等。`[RegionWand]` 為受保護標記保留英文；`%s` 順序與原文一致（驗證工具會檢查）。
- **簡轉繁字詞殘留修正**（逐字串替換，只動值）：制作→製作 33、制造→製造 32、銷燬→銷毀 248、幹擾→干擾 11、松模式／鬆模式→鬆散模式 65（保留「寬鬆模式」）、后綴→後綴 6、球后→球後 5；任務標題「電流得到處都是」→「電流到處都是」，「辣雞」→「垃圾」（香辣雞翅不動）。
- **任務閱讀**：續讀第 **2073–2162** 篇（EU儲存／LESU／LSC／石油工業），未發現需改的語意錯誤，除上列字詞外未改任務內容。**下一篇：第 2163 篇**（依 `docs/quest-source-inventory-2026-10-31.json` 順序，仍餘約 1,697 篇未讀）。
- 仍為英文且**刻意保留**的類別：化學式 tooltip（`gt.blockores/metaitem/blockframes`）、Ztones／gtnhoverridenames 方塊名、Botania 成就與彩蛋、Chisel 專輯名、ServerUtilities／CoFH 等指令用法、任務標題中的歌名／梗。
- 未同步遊戲、未遊戲內實測；無 Release。備份：倉庫外 `backups/untranslated-fill-tr1/`、`backups/charfix-20261031/`。

---

# （以下為前一版最新入口，內容保留）

更新：2026-10-31。此文件可公開；不含私人路徑或憑證。以下是最新入口，後方各批內容為歷史。

## 現況

- 基準GTNH **2.8.4**／GregTech **5.09.51.482**。本批基準`d6c053b777eec7305ac6c0773d780341a24a7443`；實際HEAD及遠端以Git核實。
- 使用者已要求**完成剩下全部**，此目標仍未達成。不要再把來源盤點或已讀篇數當成全專案完成。
- 已連續閱讀到第**2072篇**。下一篇第**2073篇「EU的儲存與變壓」**，key `betterquesting.questline.AAAAAAAAAAAAAAAAAAAAIQ`。全部3,859篇，仍有**1,787篇未接續閱讀**。
- 本批1047–2072共**1,026篇**，787篇本機英文標題／正文對照、239篇缺來源保留；修改**138條／1個現行任務檔**，未覆寫舊副本。
- 所有本批文字**未同步遊戲、未遊戲內實測**；未改jar／設定／配方／伺服器，沒有Release。前批26條Tooltip保持原值；LV／MV／HV電壓維持使用者已實測狀態。

## 先讀

1. `docs/TRANSLATION_PROGRESS.md`、`docs/TERMINOLOGY.md`。
2. `docs/PROOFREAD_2026-10-31_QUESTS1047-2072.md`：成果及重要版本差異。
3. `tools/term_calibration_2026-10-31-quests1047-2072.json`：date/order=2026-10-31/4；1,574條來源與key、138修改、239缺來源、逐篇待查。
4. `docs/quest-source-inventory-2026-10-31.json`：逐篇閱讀與來源狀態。
5. 前批242–1046的位元碼特例及報告仍有效，見下方歷史入口。

## 本批已確認例外

- 第1827篇：感測的是**中子活化器**動能，條件`eV >= threshold`，再與`inverted`做XOR；已修正嚴格大於與加速器誤稱。
- 第1865篇：安裝版DEFC提供每超出配方一級一次perfect OC，**保留現行4/4中文**，不照錯誤舊英文改成耗時除級差。
- 第2010篇：目標是IC2 RTG與6個IC2靶丸，功率為`2^(n-1)`，本機效率1.0。已移除錯貼的GT++燃料表，改1～6靶丸對應1～32EU/t。第2011篇GT++版本保留。
- 以上jar/class雜湊與方法見`docs/verification-quests1047-2072-bytecode-2026-10-31.json`。來源JSON、IC2.ini及IC2 jar加入manifest雜湊保護。
- 新CropsNH、NAC、BEC、神鍛升級、玻璃用料、工業機器倍速及爆炸警告等有來源不足／版本差異，不用舊英文覆蓋現行機制。
- 第1533篇鑽石大板可能指匠魂部件，沒有足夠配方證據所以保留；不能只按泛稱Diamond plates刪去「大」。

## 驗證

```sh
python3 tools/verify_term_calibration.py --game /path/to/.minecraft --manifest tools/term_calibration_2026-10-31-quests1047-2072.json
python3 tools/verify_translation.py --base d6c053b --reproduce
git diff --check
```

報告：`docs/verification-quests1047-2072-2026-10-31.json`、`docs/verification-quests1047-2072-structure-2026-10-31.json`。299檔／168,337條結構、26條Tooltip、138條修改重現及二次重跑需通過；既有56個重複條目與2,637空值保留。

例行備份、校對、規則同步、驗證與既有授權的提交推送成批完成，不需逐項詢問。遊戲同步、重啟及Release是不同範圍。歧義保留原值、列待查；不全域替換未核對術語、不改已實測電壓提示。新批次使用自己的baseline與manifest，後批before接前批after；`--skip-diff`只用於歷史檢查。寫完交接後讀回確認。

---

# 歷史交接紀錄

以下內容為歷史批次；目前狀態以上方最新交接與 `docs/TRANSLATION_PROGRESS.md` 為準。

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


## 2026-10-25 第二輪（最新入口）

- 第二輪清單 `tools/term_calibration_2026-10-25-continuation.json`：518條對照紀錄、130條修改、6個語言檔；另有1,706條樣板掃描，不能當逐材料語意校對。
- 現行第65–100篇標題及正文已對照閱讀，下一篇第101篇「鋅的來源」，key `betterquesting.quest.AAAAAAAAAAAAAAAAAAAHSg`。已讀79篇主題與連續任務中的版本差異仍見 `docs/PROOFREAD_2026-10-25_CONTINUATION.md`。
- 新增電力／電路、跨模組導管與過濾器規則；不要把IC2實際「一般／進階電子元件」與GT基板名稱混稱。本機Iguana設定26個加槽等級已配合位元碼核對，只改現行任務數字，保留舊副本版本差異。
- 硼玻璃命名策略已確認：遊戲簡稱保留，術語表並列硼矽酸鹽玻璃。礦物六階段命名及煉藥鍋產物已查原碼，不能把普通粉譯成dustPure。
- normalizer依date／order載入各批JSON，允許有證據的歷史值鏈，未知值或斷鏈一律在寫檔前報錯。第二輪完整diff用新manifest檢查；第一輪加 `--skip-diff` 仍核對來源／值，不能把舊批獨占diff的假設套到後續修改。
- 兩輪新文字均未同步遊戲。26條Tooltip修復保留，LV／MV／HV電壓仍已通過使用者實測。本輪授權延續commit、push main；沒有新增Release或遊戲安裝。


## 2026-10-31 接續（最新入口）

- 先讀 `docs/PROOFREAD_2026-10-31.md` 及持續進度。已同步遠端 README 的兩筆更新，以 `05ad872` 為基準；本批 71 條對照、30 條修改、3 檔，清單 `tools/term_calibration_2026-10-31.json`。
- 已閱讀第101–130篇；篇數是所有 `.desc` 檔案順序，含章節說明，不是純任務或ID。27篇有英文；第107、108篇與第112篇章節說明缺英文，保留待查。下一篇第131篇「太陽之力」，key `betterquesting.quest.AAAAAAAAAAAAAAAAAAAAPg`。
- 修正食物搜尋吃過／未吃過反轉、糖與仙人掌 Coke/Charcoal 混淆、已探明礦脈誤稱未開採、tiny/small粉末、蒸汽buffer與鍋爐倍數等。舊minecraft同ID鋁／鋅內容不同，未覆蓋舊配方。
- 來源、結構、基準重現及重跑檢查通過，26條Tooltip保留。本批未同步遊戲、未遊戲實測，前批待查仍有效；沒有新增Release。


## 2026-10-31 蒸汽收尾（最新入口）

- 本批基準 `41cb2d4`；清單 `tools/term_calibration_2026-10-31-steam.json`，207條對照、85條修改、3檔（現行38、舊BQ26、舊minecraft21）。先讀 `docs/PROOFREAD_2026-10-31_STEAM.md` 的版本差異與待查。
- 已閱讀第131–211篇，80篇有英文，第211篇地下晶洞缺來源保留。下一篇第212篇「第1階 - 低壓（LV）」，key `betterquesting.questline.AAAAAAAAAAAAAAAAAAAAAw`；第213篇「像Bo$$一樣處理資源 #1」，key `betterquesting.quest.53iZp0DzRzidBo4-kUsWGg`。篇數依所有`.desc`順序，含章節說明。
- 賽特斯石英鋒利強化24倍已對照安裝TConstruct程式註冊，現行4改24；Wrought Iron為鍛鐵，修正現行鑄鐵誤稱；電路／基板、漏斗抽取方向、背部槽位等已校準。術語表58組。
- 鋅曜鋼替代配方、地獄熔爐比較、作物模組移轉、匠魂歷史機制與第107／108／112／211篇缺來源仍待查。不把語意閱讀或部分位元碼檢視當作完整機制驗證。
- 299檔結構、重現與重跑檢查通過；26條Tooltip保留。未同步遊戲、未遊戲實測、沒有Release；延續既有驗證後提交推送的授權。


## 2026-10-31 前批242–1046入口（歷史）

# GTNH zh_TW 最新交接入口

更新：2026-10-31。此文件可公開；不含本機私人路徑、伺服器位置或憑證。**以下是目前接續入口，後面的各批舊入口只是歷史。**

## 現況與下一步

- 基準版本：GTNH **2.8.4** / GregTech **5.09.51.482**。工作分支main；本批基準`d795a602d8dd3fd845bbaeed17e191188e1415ca`。最新提交／遠端請用Git核實。
- 使用者要求繼續完成剩餘全部翻譯；**這個目標尚未完成**。不要因本次大批閱讀或完整來源盤點而宣稱全專案語意校對完成。
- 已連續閱讀至第1046篇。**下一篇：第1047篇「第10階 - 超極限壓（UEV）」**，key `betterquesting.questline.D_aFb1hFQH2PDkN0_KvAEQ`。按現行forceload檔全部`.desc`順序，含questline章節說明；不是數字ID順序。
- 本批242–1046篇共805篇；781篇有本機英文標題／正文對照，24篇缺來源保留。修改**187條語言值／1個現行任務檔**。沒有覆寫兩個舊任務副本。
- 全部任務3,859篇，尚有**2,813篇未接續閱讀**。完整自動來源清單定位3,494篇，365篇未定位；來源清點不是語意校對。
- 本批及10月25日、10月31日前三批新文字均**未同步遊戲、未遊戲內實測**。沒有新Release，未改jar／設定／配方／伺服器。
- 前批26條Tooltip修復保留。LV／MV／HV電壓等級維持使用者已實測通過狀態；其餘Tooltip未因此自動算實測。

## 先讀哪些檔案

1. `docs/TRANSLATION_PROGRESS.md`、`docs/TERMINOLOGY.md`。
2. `docs/PROOFREAD_2026-10-31_QUESTS242-1046.md`：本批成果、24篇缺來源與版本差異待查表。
3. `tools/term_calibration_2026-10-31-quests242-1046.json`：1,562條來源／key對照、187條修改、精確before/after。date/order＝2026-10-31/3。
4. `docs/quest-source-inventory-2026-10-31.json`：3,859篇來源與閱讀狀態；歷史241篇只指向前批紀錄，不重複宣稱已驗證。
5. 涉及前批問題時，再讀其LV／STEAM與更早報告。

## 已查證的重要例外

- 第355篇英文Flint Lens錯誤：本機`ScriptRailcraft.loadRecipes`是Diamond或Firestone透鏡，保留火石透鏡。
- 第784篇英文碘回收half錯誤：本機`RecipeLoader.loadGeneral`投入4粉／4000L，回收4000L；保留全部回收。
- 第862篇本機`BWMetaItems.init`使用高壓釜、576L焊料合金、75%機率，修正了雷射蝕刻機誤稱。
- 第396篇本機任務目標為12乙烯單元、84氧單元、125聚乙烯單元，已修正文案；不是完整配方驗證。
- 第281篇必要目標是ProjectRed emptybattery，保留空電池標題。第592篇目標為18鉑粒，正文改鉑粒。
- 第772篇本機投入11046硝酸獨居石浸出混合物，產物含11025二氧化鈰與11018濃縮液。不能按英文leached concentrate把投入物改錯。
- Nature's Compass本機按I18n翻譯後的搜尋鍵比對；不把中文鍵改成英文。
- `quest`和`questline`命名空間可能有同UUID token；**不能用任務英文冒充章節說明**。

位元碼、jar/class雜湊見`docs/verification-quests242-1046-bytecode-2026-10-31.json`。其他PBI跳過數量、Import/Export方向、CropsNH移轉、鍋爐燃料、維護倉共用、太空電梯槽數、異氙菌機率等仍見批次待查表。

## 本批驗證與接續規則

```sh
python3 tools/verify_term_calibration.py --game /path/to/.minecraft --manifest tools/term_calibration_2026-10-31-quests242-1046.json
python3 tools/verify_translation.py --base d795a60 --reproduce
git diff --check
```

報告：`docs/verification-quests242-1046-2026-10-31.json`與`docs/verification-quests242-1046-structure-2026-10-31.json`。299檔／168,337條結構、26條Tooltip、從基準重現187條修改及二次重跑都須通過；原有56個重複鍵多餘條目、2,637個空白值保留。

新批次要改用自己的baseline與manifest。規則按date/order載入，同key後批before必須接前批after。未知值或斷鏈應查證，不可刪衝突檢查。`--skip-diff`只用於歷史批次，不略過本批白名單檢查。

例行備份、校對、規則同步、驗證與既有授權的提交推送成批完成，不需逐項詢問。遊戲同步、重啟與Release仍是不同範圍。歧義保留原值、列待查；不全域替換未核對術語、不改已實測電壓提示。寫完交接後須讀回確認。
