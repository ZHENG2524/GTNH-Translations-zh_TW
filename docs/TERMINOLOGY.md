# 繁體中文術語規範（台灣）

更新：2026-10-25；基準 GTNH 2.8.4 / GregTech 5.09.51.482。

本表是後續校準的對照規範，**不是全倉庫套用完成清單**。每次只修改已確認的檔案與 key；未讀到原文、呼叫點或版本不符時，保留原值並記入 [進度與待查清單](TRANSLATION_PROGRESS.md)。簡轉繁與自動篩查不算人工語意校對。

## 決策與證據順序

1. 安裝版本 jar 的英文、程式呼叫點與任務 JSON；執行時 GregTech 英文檔可能含歷史 key，須搭配同版本原碼判斷。
2. 同版本上游原碼與遊戲實際用途；動態串接及跨行共用參數以呼叫契約為準。
3. 可信中文用語與既有遊戲名稱；Wiki 僅作術語參考，不能拿新版本配方覆蓋 2.8.4。
4. 有充分證據才改。既有特殊名稱、梗、模組名稱與縮寫不因字面相似而被替換。

## 對照表

「採用」表示可供已確認語境使用；「沿用」表示保留既有名稱；「待查」不得自動套用。這三種術語決策不等於各檔案的校對進度。

| 英文術語 | 繁中建議 | 語境、例外與狀態 |
|---|---|---|
| Laser | 雷射 | 採用；沿用既有台灣用語規則。 |
| The End | 終界 | 採用；維度名稱，不能把一般 end 一律替換。 |
| Nether | 地獄 | 採用；Minecraft 維度。 |
| Reactor | 反應爐 | 採用於核能等反應爐；Chemical Reactor 另列。 |
| Chemical Reactor | 化學反應釜 | 沿用 GregTech 機器與配方頁名稱；不因 Reactor 規則改為化學反應爐。 |
| Fusion | 核融合 | 採用於核融合；其他模組的普通融合／魔法融合須另核對。 |
| Voltage | 電壓 | 採用；不能與電流混用。NetworkAnalyzer 的歷史鍵待查版本。 |
| Current / Amperage | 電流 | 採用於 GT 電力；保留 A，勿以 EU/t 取代。current 表「目前」時不能譯電流。 |
| Voltage Tier | 電壓等級 | 採用；保留 LV、MV、HV 等縮寫，等級由程式產生。 |
| Transformer | 變壓器 | 採用於電力設備；既有譯名保留。 |
| Circuit | 電路 | 採用於分級電路及礦典電路需求；不能一律稱為電路板。 |
| Circuit Board | 電路板 | 採用於板材與基板物品；與 Circuit 區分。 |
| Battery Buffer | 電池箱 | 已核對 GT 實際設備與任務；不是電池快取／電池緩衝區。 |
| Macerator | 研磨機 | 已核對 GT LV～HV 與配方頁；其他模組同名設備另核對。 |
| Ore Washing Plant / Ore Washer | 洗礦機 | 已核對 GT 單方塊設備及配方分類；不可全域替換洗礦廠。 |
| Repurposed Laundry-Washer I-360 | 改裝洗衣機 I-360 | 已核對 IV 特殊名稱；保留洗衣機梗與型號。 |
| Industrial Ore Washing Plant | 工業洗礦廠 | 沿用多方塊專名；未套用單方塊改名規則。 |
| Centrifuge | 離心機 | 已核對 GT 機器與配方頁。 |
| Thermal Centrifuge | 熱力離心機 | 已核對；不能與普通離心機混稱。 |
| Electrolyzer | 電解機 | 已核對 GT 機器與配方頁。 |
| Electrolyzing | 電解 | 已核對；不譯為電離。 |
| Circuit Assembler | 電路組裝機 | 已核對 LV～HV 名稱與任務。 |
| Wiremill | 線材軋機 | 沿用本版本機器與配方分類名稱。 |
| Ore | 礦石 | 採用；材料基名不額外加礦，避免生成重複礦石名稱。 |
| Crushed Ore | 粉碎礦石／粉碎的…礦石 | 沿用礦物處理階段；不能誤稱一般粉末。 |
| Purified Ore / crushedPurified | 洗淨礦石／洗淨的…礦石 | 採用；與粉碎階段、純淨粉末區分。 |
| Centrifuged Ore / crushedCentrifuged | 離心礦石 | 沿用；不是普通離心機產出的所有物品的統稱。 |
| Impure Dust / dustImpure | 含雜粉 | 沿用；特定礦物處理階段。 |
| Purified Dust / dustPure | 潔淨粉 | 沿用既有生成名稱；純淨粉末等副本用語尚待逐鍵統一。 |
| Clean Dust / dust | 粉／潔淨粉末（依句子） | 普通粉末階段；不要與 dustPure 混為同一物品。 |
| Ingot | 錠 | 沿用；hot ingot 為熱錠。 |
| Plate | 板 | 沿用；保留雙重、緻密等前綴。 |
| Rod | 桿 | 沿用；stick 的其他模組語境另查。 |
| Screw | 螺絲 | 沿用；Bolt 為螺栓。 |
| Coil | 線圈 | 沿用；加熱線圈溫度依動態串接顯示。 |
| Wire | 導線 | 沿用 GT 材料名稱；敘述可用電線，不與線纜一律互換。 |
| Cable | 線纜 | 沿用 GT 既有名稱；其他模組電纜需逐鍵核對。 |
| Item Pipe | 物品管道 | 沿用 GT；其他模組 Conduit 的物品導管名稱另核對。 |
| Fluid Pipe | 流體管道 | 沿用 GT；不全域替換其他模組流體管線。 |
| Hatch | 倉 | 沿用既有輸入倉／輸出倉／能源倉，不改艙口。 |
| Input Bus / Output Bus | 輸入匯流排／輸出匯流排 | 沿用；Bus 與 Hatch 不混稱。 |
| Filter | 過濾器 | 沿用；覆蓋板、篩選配方及模組專名另核對。 |
| Rare Earth / Rarer Earth | 稀土／罕土 | 保留遊戲刻意區別；禁止將罕土全部改稀土。 |
| Buffer / Cache | 緩衝／快取 | 依用途；Battery Buffer 為電池箱，電腦 cache 保留快取。 |

共 44 組對照；部分列含多個相近但不可混用的英文術語。

## 可重現的限定修改

- 舊規則保存在 `tools/normalize_terms.py`；舊有全域規則僅記錄歷史行為，**新增規則不得照抄成無條件全域替換**。
- 本批 159 條對照閱讀紀錄與 60 條修改存於 `tools/term_calibration_2026-10-25.json`，含路徑、key、英文來源、前後值、批次與限制。
- 新批次以路徑與 key 套用，只接受已審查的 before 或 after；遇到第三種新值直接報衝突，避免撤回別人的新翻譯。不能以刪除衝突檢查處理遠端更新。
- 保護 `%s`、索引、旗標、精度、`%material`、`§`、標記、跳脫換行、指令、URL 及 key。必要參數變更須另有程式呼叫點與精確驗證，不能為了通過檢查直接刪參數。
- 工具只證明結構、來源與重現性；遊戲渲染與配方機制需分別記錄。

## 來源索引

- 安裝包：GTNH 2.8.4、`mods/gregtech-5.09.51.482.jar` 的 `mcmod.info`、`assets/gregtech/lang/en_US.lang`、同實例 `GregTech_US.lang` 與 `config/betterquesting/DefaultQuests/Quests/`；來源精確值及 jar SHA-256 見本批 JSON。
- [5.09.51.482 機器註冊](https://github.com/GTNewHorizons/GT5-Unofficial/blob/5.09.51.482/src/main/java/gregtech/loaders/preload/LoaderMetaTileEntities.java)：單方塊洗礦機與 IV 洗衣機名稱。
- [5.09.51.482 OrePrefixes](https://github.com/GTNewHorizons/GT5-Unofficial/blob/5.09.51.482/src/main/java/gregtech/api/enums/OrePrefixes.java)：crushed、crushedPurified、crushedCentrifuged、dustPure 等不同階段。
- `bartworks.system.material.BWMetaGeneratedItems.addAdditionalToolTips`：本機 jar 位元碼確認 `purify.2` 用於 crushed，`nqgen` 才用於 Tiberium 燃料提示；英文值錯置不得照搬。詳見進度紀錄。
- 既有材料與中文 Wiki 依據、限制見 [2026-10-24 紀錄](PROOFREAD_2026-10-24.md)；本批未宣稱新增完成 Wiki 化學名校對。
