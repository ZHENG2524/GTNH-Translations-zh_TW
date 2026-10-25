# 2026-10-25 第二輪：電力、電路、運輸與第 65–100 篇任務

基準提交：`084ed7a2eb317e6cda1e80a5733b5759f7882ee6`。GTNH 2.8.4、GregTech 5.09.51.482；同版本上游 tag 對應原碼提交 `e48304dd8f49be6df8e395c835780002bfb4e898`。修改前已保存倉庫外 Git bundle，可回復基準。

## 實際完成範圍

- 共 **518 條檔案／key 對照紀錄**，修改 **130 條、6 個語言檔、3 批**。相同 key 在不同副本分別計數；保留原值也列入對照紀錄。
- 對照閱讀現行 **79 篇任務的標題與正文**，其中包括依現行檔案順序的第 **65–100 篇（36 篇）**，以及電力、電路與輸送主題任務。機制、譯者註與版本差異另列，不宣稱 79 篇的所有敘述均完成遊戲驗證。
- Ender IO 230 條導管／過濾器候選、LP 33 條相關候選對照英文；只修改已確認問題，未讀的模組其他內容仍屬尚未處理。
- 另以六組命名樣板掃描 **1,706 條**，零差異；這是樣板一致性檢查，不當成 1,706 條材料的人工語意校對。
- 新增 13 組、修訂 4 組術語，術語表由 44 組增至 **57 組**。
- 狀態：130 條新文字均為 **已修改但待遊戲實測**。未同步遊戲、未修改任何 jar 或遊戲邏輯；舊 26 條 Tooltip 修復保持原值，電壓等級維持已通過使用者實測。

## 三批修正

| 批次 | 修改數 | 具體內容 |
|---|---:|---|
| D：電力與電路 | 58 | 區分電路、電路基板及 IC2 內建物品專名；GT 優質電子／積體電路名稱、礦物辭典錯字、電池箱輸出損耗、能源倉功率說明、能量緩衝器與掃描器副本術語。 |
| E：跨模組運輸 | 46 | Ender IO 40：偽裝板／導管束／連接器、輸入輸出錯字、中繼資料、礦物辭典、輪流分配、耐久損耗邊界與速度升級；Logistics Pipes 6：儲罐、設定、部分請求及補充條件。 |
| F：第 65–100 篇任務 | 26 | 機率升級誤譯、本機強化槽數、GT 攻擊傷害誤稱耐久消耗、普通紅石粉階段、光照與發光混淆，以及物品提示、半磚、任務章節與明確錯字。含舊副本適用片語同步。 |

| 實際變更的語言檔 | 條數 |
|---|---:|
| GregTech 主檔 | 2 |
| 現行 forceload/betterquesting | 33 |
| 舊版 load/betterquesting | 27 |
| 舊版 load/minecraft | 22 |
| Ender IO | 40 |
| Logistics Pipes | 6 |

精確前後值、來源英文與限定範圍見 [本輪清單](../tools/term_calibration_2026-10-25-continuation.json)。若上表與未來提交有差異，以該次驗證報告及 Git diff 為準。

## 已確認的語境與保留決定

### 電力與電路

- GT `gt.metaitem.01.32702.name` 是 Good Electronic Circuit，採「優質電子電路」；`gt.metaitem.03.32079.name` 是 Good Integrated Circuit，採「優質積體電路」。它們是不同物品，不能因同為 MV 就互換名稱。
- Circuit Board 的基板條目保留「電路基板」。IC2 安裝 jar 的 `ic2/lang/zh_TW.properties` 使用「一般電子元件／進階電子元件」；明確指 IC2 物品的任務依此對齊，不直接把所有模組 Circuit 一律改名。
- Battery Buffer 教學的 loss when outputting 原本誤譯「接收 EU 時損失」，已改輸出；`BaseMetaTileEntity` 的輸出計算以含損耗的電壓扣能量，`MTEBasicBatteryBuffer` 以可充／可放電電池數決定安培數。本批不改 2A／1A 等既有數字。
- MV 能源倉說明原本把「功率超出單一 1A 容量」寫成「功率 1V」，現行文字改以 EU/t 表達配方功率及 2A 輸入需求。未修改工業高爐配方、電壓數值或能源倉邏輯。

### 礦物階段與生成樣板

本版本實際透過 `OrePrefixes.getDefaultLocalNameFormatForItem`、`MetaGeneratedItemX01`／`MetaGeneratedItemX32` 與 `Materials.getLocalizedNameForItem` 的 `%material` 替換生成名稱；BartWorks 使用 `bw.itemtype.*`。

| 英文樣板 | 保留的繁中樣板 | 共用鍵數 |
|---|---|---:|
| Crushed %material Ore | 粉碎的%material礦石 | 222 |
| Purified %material Ore | 洗淨的%material礦石 | 222 |
| Centrifuged %material Ore | 離心%material礦石 | 222 |
| Impure Pile of %material Dust | 含雜%material粉 | 228 |
| Purified Pile of %material Dust | 潔淨%material粉 | 219 |
| %material Dust | %material粉 | 593 |

- 本批 **已校對六類樣板與程式流程**，以上 1,706 條自動比對全部一致，無須改名。
- `MetaGeneratedItem01.onEntityItemUpdate` 確認：`dustImpure`／`dustPure` 在煉藥鍋中都轉為 `dust`；`crushed` 轉為 `crushedPurified`。所以紅石任務最後產物改「普通紅石粉」，不能誤導成 `dustPure`。
- 程式每次處理一個物品實體堆疊，只扣一格水位；一鍋三格水位可處理三個堆疊的現行中文說明因此保留。未把掃描結果當作其他材料配方也已核實。
- `gt.oreprefix.*` 候選在這個版本的英文檔與原碼中未找到相同 key，不能拿另一版模板覆蓋本版有效的 `bw.itemtype.*`／`gt.metaitem.*`。歷史鍵保留待定位，沒有大量刪除。

### 硼玻璃命名決策

GT 的材料與熔融流體、18 個有現行英文的 BartWorks 方塊條目都指向 Borosilicate Glass，本輪保留一致的「硼玻璃」。[教育部辭典](https://dict.revised.moe.edu.tw/dictView.jsp?ID=24205)收錄該詞；[臺大 CASE](https://case.ntu.edu.tw/blog/?p=43831)使用「硼矽酸鹽玻璃」。術語表採遊戲簡稱、化學全名並列，這是本專案的命名決策，不是宣稱兩種用法在所有玻璃文獻都可無條件互換。

較新名稱 `BW_TieredGlass.*`／`BW_ExtraGlass.*` 不因字面相似被宣稱完成本版來源核對；現有譯值保持。

### Ender IO 與 Logistics Pipes

- Facade 的英文說明含噴塗、覆蓋導管及持扳手時隱藏，採「導管偽裝板」，避免框架造成結構用途誤解。
- Ender IO 的 Extract／Insert 保持相連容器的提取／存入方向；沒有改變設定或遊戲行為。
- 舊耐久模式把 Damaged by 25% or more 寫成剩餘耐久「低於 75%」，漏掉正好 75% 邊界；改為「已損耗至少 25%」，50／75 同步。另核對本機 `FuzzyMode.compareQuarter` 位元碼：條件是 damage×4 ≥ maxDamage×quarter，確實包含等於邊界。
- `ModuleTypeFilterItemSink` 本機位元碼的 `prefixes` 是 `EnumSet<gregtech.api.enums.OrePrefixes>`，所以保留「礦物辭典字首過濾收納模組」的精確譯名，不因英文 Type Filter 較概括而刪掉功能資訊。

### 第 65–100 篇的機制核對

- 匠魂工具：Iguana 設定 `RandomBonuses=false`、`maxToolLevel=99`、`ModifiersAtLevels` 共 26 個等級；`LevelingLogic` 先按匹配等級寫入 Modifiers，再隨機選訊息。現行任務校正為到指定等級增加槽、升級共額外獲得 26 槽。只適用本機 2.8.4 設定；不以此改寫其他版本或舊副本數字。
- GT 屠刀：`MetaGeneratedTool.getToolCombatDamage` 回傳基礎傷害加材料品質；`getHarvestLevel` 也使用材料品質。因此原「GT 工具耐久消耗基於採掘等級」改為攻擊傷害與材料採掘等級有關。沒有修改武器數值。

## 仍需查證與尚未處理

1. **待查證**：第 66 篇牛戰利品的冷卻與掉落率、第 69 篇鑽石／綠寶石增益、第 76 篇 Forestry 揹包額外操作說明、第 90／92 篇工具強化一次可放數量。這些含未完整核實的譯者註或版本差異，不隨英文段落直接覆蓋。
2. **待查證**：掃描器任務現行中文省略英文的作物屬性偵測段落，可能與 CropsNH 移轉有關；本輪僅修正舊副本「HV 電路」術語，沒有補回可能過時機制。
3. **待查證**：HV 的 SMD 任務英文講所有表面黏著元件與聚乙烯，中文卻只講鉑與貼片二極體；先保留，需核對實際目標與配方版本，不以新英文全文替換。
4. **待查證**：LV 變壓器任務末段 `%%`、Ender IO 單行黏滯模式的 `|` 分行與中文句點差異。此次保護格式碼，未把它們當純文字任意刪改；後續查實際格式化與顯示呼叫。
5. **待查證**：舊副本仍記 20 個升級槽、舊版機率描述、無線充電器高於等級的譯者註、Electrotine Battery「空電池」、NetworkAnalyzer 歷史鍵及先前 White Metal 等歧義；詳見持續進度。
6. **尚未處理**：第 **101 篇「鋅的來源」**（`betterquesting.quest.AAAAAAAAAAAAAAAAAAAHSg`）起的連續任務；其他材料、機器與模組完整語意校對。
7. **待遊戲實測**：本輪所有新文字，尤其電路物品與任務名、導管偽裝板、物品過濾設定、強化槽說明。既有 LV／MV／HV 電壓實測狀態保留。

## 驗證與重現

```sh
python3 tools/normalize_terms.py /path/to/repository
python3 tools/verify_translation.py --base 084ed7a --reproduce
python3 tools/verify_term_calibration.py --game /path/to/.minecraft --manifest tools/term_calibration_2026-10-25-continuation.json
python3 tools/verify_term_calibration.py --game /path/to/.minecraft --skip-diff
git diff --check
```

- 全 299 個語言檔的 key、順序、行數、佔位符、顏色碼、標記、URL 與跳脫換行不變；既有空白與重複鍵未增加。
- 第二輪 518 條來源／值核對、130 條修改白名單、來源 jar 與補充設定雜湊、IC2 內建物品名、Iguana 指定等級及 1,706 條樣板比對通過。
- 從第二輪基準重現新改動，二次重跑零差異；另可從第一輪基準 `e24b6a4` 重現累計 190 條修改。
- 第一輪清單使用 `--skip-diff` 只略過歷史批次獨占 diff 的假設，仍檢查原 159 條來源／值及保護符號；本輪完整 diff 由新清單與全語言結構驗證把關。
- 所有 26 條既有 Tooltip 修復逐鍵保持；電壓等級仍為已使用者實測，本輪不宣稱新增遊戲實測。
- 檢查報告：`verification-continuation-2026-10-25.json`、`verification-continuation-structure-2026-10-25.json`。工具與紀錄不包含本機私人路徑。
