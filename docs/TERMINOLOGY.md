# 繁體中文術語規範（台灣）

更新：2026-11-01；基準 GTNH 2.8.4 / GregTech 5.09.51.482。

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
| Conveyor | 輸送帶 | 2026-11-01 全語言檔統一，取代「傳送帶」。 |
| Tab（任務書） | 分頁 | 舊譯「工作列」是 taskbar 的誤轉，章節請稱分頁。 |
| Circuit（分級） | 電路板 | 使用者 2026-10-31 決定：EV電路板、高階電路板等一律如此；積體電路、邏輯電路、功率電路等晶片名與「電路設計／電路組」不改；IC2 內建物品專名另列。 |
| Circuit Board | 電路板／電路基板 | 採用於板材與基板物品；GT 既有進階／高階電路基板保持原名，與 Circuit 區分。 |
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
| Purified Dust / dustPure | 潔淨粉 | 已核對 OrePrefixes 與 BW 生成樣板；仍含可離心的副產物，煉藥鍋可轉為普通粉。 |
| Clean Dust / dust | 粉／普通粉末 | 已核對煉藥鍋產物是 dust；英文敘述中的 pure/clean 不一定代表 dustPure。 |
| Wrought Iron | 鍛鐵 | 已核對本機英文任務、GT 材料 304 與 Material.wroughtiron；與鑄鐵區分，只校準確認的任務條目。 |
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
| Ore Dictionary | 礦物辭典 | 採用；可簡稱礦典，不用錯字礦辭；保留 ore* 等礦典運算式。 |
| Programmed Circuit | 程式設計電路 | 沿用 GT 物品名稱；機器配方中的設定電路不是電路板。 |
| Good Electronic Circuit / Good Integrated Circuit | 優質電子電路／優質積體電路 | 已核對物品、任務與目標 ID；同階電路仍是不同物品，不互換名稱。 |
| Electronic Circuit / Advanced Circuit（IC2） | 一般電子元件／進階電子元件 | 使用安裝 IC2 zh_TW.properties 的實際名稱；一般語境的分級電路稱電路板。 |
| Borosilicate Glass | 硼玻璃；化學全名硼矽酸鹽玻璃 | 已核對 GT 材料、流體與現行 BartWorks 方塊；保留遊戲簡稱，避免同一物品多套譯名。 |
| Conduit | 導管 | 已核對 Ender IO；與 GT、LP 的物品／流體管道區分。 |
| Conduit Facade | 導管偽裝板 | 已核對 Ender IO：可噴塗並覆蓋導管，並非結構框架。 |
| Conduit Bundle / Conduit Connector | 導管束／導管連接器 | 依各英文 key 分別翻譯；原名均為導管介面，不再混稱。 |
| Round Robin | 輪流分配 | Ender IO 導管分配模式；不誤稱一般循環。 |
| Metadata / NBT | 中繼資料／NBT | 採用於物品過濾器；保留 NBT 縮寫，不將不同條件合併。 |
| Extract / Insert | 提取／存入 | Ender IO 設定描述相連容器的提取／存入；不擅自對調端口方向。 |
| Type Filter ItemSink Module | 礦物辭典字首過濾收納模組 | 已檢查 LP 1.4.24 位元碼，確實依 GT OrePrefixes 篩選，保留精確既有名稱。 |
| Modifier Slot / Upgrade Slot | 強化槽 | 匠魂工具語境；現行任務按本機 Iguana 指定升級等級增加，非隨機給槽，舊版副本數字另列版本差異。 |
| Casing | 機械方塊 | 沿用 GT；Railcraft 的 Steam Turbine Housing 保留蒸汽渦輪機殼。 |
| Extruder / Extruder Shape | 壓模機／模頭 | 已核對 GT 機器與 `gt.metaitem.01.3235x`；CoreMod 的 Extruder Shape 同用模頭。 |
| Extractor | 提取機 | 已核對 GT 機器類型提示。 |
| Data Stick | 快閃記憶體 | 沿用 `gt.metaitem.01.32708` 物品名。 |
| Advanced Circuit Board | 高階電路基板 | 對齊 GT 既有名稱；CoreMod 的同類處理器基板用高階處理器基板。 |
| Solar Panel | 太陽能板 | 採用；不用太陽能電池板。 |
| Engine | 引擎 | 採用；不用發動機。 |
| Chainsaw | 鏈鋸 | 採用；不用電鋸。 |
| Alchemy | 鍊金 | 採用；「冶煉金屬」等非 alchemy 語境不動。 |
| Glowstone / Fluorite | 螢光石／氟石 | 已核對：GT Fluorite 譯氟石，故「螢石」皆指 Glowstone；亞螢石為專名保留。 |
| Netherrack | 地獄岩 | 原版 1.7.10 為地獄石，已在 overridenames 覆寫以一致；地獄石英不受影響。 |
| Nether Wart | 地獄疣 | 原版 1.7.10 為地獄疙瘩，已覆寫。 |
| Cobblestone | 圓石 | 原版 1.7.10 為鵝卵石，已覆寫。 |
| Blaze | 烈焰使者 | 對齊原版實體名稱。 |
| Looting | 掠奪 | 對齊原版附魔名稱；Infernal Mobs 的 Snagging 為搶奪，是不同詞。 |
| Cobweb | 蜘蛛網 | 對齊原版方塊名。 |
| Biome | 生物群系 | 採用；不用生態域。 |
| Hotbar | 快捷欄 | 採用；Botania 的 Ask Toolbar 梗保留工具欄。 |
| Durability | 耐久度 | 採用；不用耐久值。 |
| Permission | 權限 | 採用；不用許可權。 |
| Feedback | 回饋／回報 | 訊號回饋、Feedback 按鈕用回饋；回報錯誤用回報。 |
| Wither / Spawn Egg | 凋零／生怪蛋 | v0.1.5 全域統一。 |
| Shulker Box / Shell | 界伏盒／界伏殼 | v0.1.5 全域統一。 |
| Space Suit | 太空衣 | v0.1.5 全域統一。 |
| Access | 存取 | v0.1.5 全域統一；Witchery 書的 `[url 末地石]` 連結文字不動。 |
| Projector / Network Card | 投影機／網路卡 | 全域統一。 |
| Screen / Floppy Disk | 螢幕／軟碟 | 全域統一。 |
| Clay / Sticky | 黏土／黏 | 全域以「黏」為準。 |

共 86 組對照；部分列含多個相近但不可混用的英文術語。

## 暫不統一（語意不同或需逐條判斷）

- **進階／高階／先進**：GT 階級詞用「基礎／進階／精英／終極／史詩」；敘述中的 high-tier 可用高階。兩者語意不同，不全域替換。
- **感應器／感測器**：Sensor 用感測器；Vis 感應器、玩家感應器等既有模組物品名保留。
- **檢視／點選**：皆為可接受用語，不做全域替換。
- **配方／合成表**：配方機制與手動合成表語境不同，兩者並存。

## 可重現的限定修改

- 2026-11-01 用語收尾：`tools/normalize_terms_2026-11-01.py`（冪等）；原版名稱差異另寫入 `____gtnhoverridenames`。

- 舊規則保存在 `tools/normalize_terms.py`；舊有全域規則僅記錄歷史行為，**新增規則不得照抄成無條件全域替換**。
- 第一輪 159 條對照閱讀紀錄與 60 條修改存於 `tools/term_calibration_2026-10-25.json`，含路徑、key、英文來源、前後值、批次與限制。
- 第二輪清單見 `tools/term_calibration_2026-10-25-continuation.json`：518 條對照紀錄、130 條修改，另有 1,706 條六組礦物樣板掃描，不併入逐條語意校對數。
- 工具依 date／order 載入各批 `term_calibration_*.json`，同 key 的後續修訂必須以前一批 after 為 before，斷裂的歷史直接報錯，不能回滾成舊譯文。
- 新批次以路徑與 key 套用，只接受已審查的 before 或 after；遇到第三種新值直接報衝突，避免撤回別人的新翻譯。不能以刪除衝突檢查處理遠端更新。
- 保護 `%s`、索引、旗標、精度、`%material`、`§`、標記、跳脫換行、指令、URL 及 key。必要參數變更須另有程式呼叫點與精確驗證，不能為了通過檢查直接刪參數。
- 工具只證明結構、來源與重現性；遊戲渲染與配方機制需分別記錄。

## 來源索引

- 安裝包：GTNH 2.8.4、`mods/gregtech-5.09.51.482.jar` 的 `mcmod.info`、`assets/gregtech/lang/en_US.lang`、同實例 `GregTech_US.lang` 與 `config/betterquesting/DefaultQuests/Quests/`；來源精確值及 jar SHA-256 見本批 JSON。
- [5.09.51.482 機器註冊](https://github.com/GTNewHorizons/GT5-Unofficial/blob/5.09.51.482/src/main/java/gregtech/loaders/preload/LoaderMetaTileEntities.java)：單方塊洗礦機與 IV 洗衣機名稱。
- [5.09.51.482 OrePrefixes](https://github.com/GTNewHorizons/GT5-Unofficial/blob/5.09.51.482/src/main/java/gregtech/api/enums/OrePrefixes.java)：crushed、crushedPurified、crushedCentrifuged、dustPure 等不同階段。
- `bartworks.system.material.BWMetaGeneratedItems.addAdditionalToolTips`：本機 jar 位元碼確認 `purify.2` 用於 crushed，`nqgen` 才用於 Tiberium 燃料提示；英文值錯置不得照搬。詳見進度紀錄。
- 既有材料與中文 Wiki 依據、限制見 [2026-10-24 紀錄](PROOFREAD_2026-10-24.md)；本批未宣稱新增完成 Wiki 化學名校對。

## 第二輪補充來源（2026-10-25）

- [教育部：硼玻璃](https://dict.revised.moe.edu.tw/dictView.jsp?ID=24205)支持保留台灣既有詞；[臺大 CASE：玻璃種類](https://case.ntu.edu.tw/blog/?p=43831)提供硼矽酸鹽玻璃用語。本批採遊戲簡稱與化學全名並列的策略，不將兩頁視為 GT 配方依據。
- [5.09.51.482：MetaGeneratedItem01](https://github.com/GTNewHorizons/GT5-Unofficial/blob/5.09.51.482/src/main/java/gregtech/common/items/MetaGeneratedItem01.java)的煉藥鍋分支、[BWMetaGeneratedItems](https://github.com/GTNewHorizons/GT5-Unofficial/blob/5.09.51.482/src/main/java/bartworks/system/material/BWMetaGeneratedItems.java)建構子與[Materials](https://github.com/GTNewHorizons/GT5-Unofficial/blob/5.09.51.482/src/main/java/gregtech/api/enums/Materials.java)的 `%material` 替換流程。
- 安裝 Ender IO 2.9.28、Logistics Pipes 1.4.24、IC2 2.2.828 的英文與內建繁中；IguanaTweaksTConstruct 2.6.6 位元碼及實例設定。各來源 SHA-256 存於第二輪清單，驗證工具只讀來源。
