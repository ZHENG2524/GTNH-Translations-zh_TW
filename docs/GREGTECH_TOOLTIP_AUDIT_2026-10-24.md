# GregTech 機器與電力 Tooltip 修復紀錄（2026-10-24）

## 結果與適用版本

本次修正 6 個 txloader 語言檔，共 26 條翻譯；只修改翻譯及其校驗／重現工具。沒有修改模組 jar、Mixin、伺服器或現有發布 ZIP；經使用者授權，另已備份並同步已安裝遊戲實例的 26 個修復鍵。

依本機 GTNH 2.8.4 實例的 `mods/gregtech-5.09.51.482.jar` 與 `mcmod.info` 核實 GregTech 5.09.51.482（Minecraft 1.7.10）。該 jar 內整合 GregTech GTNH、GT++、BartWorks、TecTech、KekzTech、Good Generator、KubaTech、GigaGramFab、GTNH Lanthanides、GT NEI Ore Plugin、Detrav Scanner、GTNH Intergalactic、Galactic Greg 等，不應以其他版本的獨立附屬模組版本推定本版本行為。另有本機 GTTweaker 2.3.1、TGregworks 1.0.28、VisualProspecting 1.4.8；本次已確認的錯誤均位於整合 jar 的語言覆蓋檔。

## 根本原因與正確行為

英文原始值：

```properties
gt.tileentity.eup_in=Voltage IN: §a%d (%s§a)§7
gt.tileentity.eup_out=Voltage OUT: §a%d (%s§a)§7
gt.tileentity.eup_store=Capacity: §9%d§7 EU
```

原繁中把輸入／輸出兩個參數縮減成單一 `%s`，導致程式傳入的第二個參數（等級縮寫）被忽略；容量另遺漏 EU 單位及原有顏色碼。這是翻譯與現行版本參數契約不一致，不是研磨機本身的程式錯誤。

核對安裝 jar 的 `gregtech.common.blocks.ItemMachines.addInformation` 位元碼：當 EU 容量大於零時，輸入／輸出電壓大於零的項目各傳入 `GTUtility.formatNumbers(voltage)` 與 `GTUtility.getColoredTierNameFromTier(GTUtility.getTier(voltage))`。容量傳入格式化後的容量字串。`GTUtility.getColoredTierNameFromTier` 使用 `GTValues.TIER_COLORS`、`GTValues.VN` 及重設碼；`GTValues.V[3] = 512`、`VN[3] = HV`，因此本版本的 512 對應 HV 已由本機程式核實。

新繁中維持中文全形冒號／括號，恢復兩個參數、原版顏色及 EU：

```properties
gt.tileentity.eup_in=電壓輸入：§a%d（%s§a）§7
gt.tileentity.eup_out=電壓輸出：§a%d（%s§a）§7
gt.tileentity.eup_store=容量：§9%d§7 EU
```

等級仍由模組計算，沒有硬編碼 HV 或任何數值對應表。影響範圍是共用上述物品 Tooltip 路徑且符合條件的加工機、發電機、變壓器、電池箱、儲能設備及能源／動力倉等，不只研磨機。

## 其他確認的翻譯錯誤

- 蟲洞發生器：`GT5U.infodata.wormhole_generator.transferred`／`received` 將時間插入第四位置，卻未使用索引，造成七個參數語意錯置，亦可能因整數／浮點型別不合產生格式錯誤。已使用明確索引，恢復原版 A/t，保留中文語序。
- ME 輸出倉／匯流排：兩個 filter.enable 鍵缺少設定內容參數，已恢復。
- NEI 燃料資訊：現行程式只傳一個參數，繁中多出第二個 `%s`，已移除。
- 加熱線圈：程式串接「前綴 + 溫度 + 單位」，繁中前綴卻包含 `%s` 和單位，已恢復為前綴；原版單位鍵 `gt.coilunittooltip` 仍回退至英文 Kelvin，本批未新增其他翻譯鍵。
- GT++ 機器提示：作者標示是直接取語言字串，沒有作者參數；已恢復原版作者與格式碼。量子操縱者流體模式的布林值由程式串接，已移除多出的 `%s`。無線充電器三條提示恢復原版 `%,d` 千分位格式；另修正鑿刻輸出槽的 `$7` 為 `§7`。
- TecTech 神鍛：核融合等級由程式串接冒號與數值，已移除語言檔多出的參數；兩條能量／電池升級說明直接讀取文字，已將誤用的 `%%` 改為 `%`，沒有更動其數值或機制說明。
- BartWorks 電路組裝線：壓印內容由程式串接，移除多出的參數／重複顏色碼。
- Detrav 勘探設備：耐久、範圍、成功率、流體名及流體儲量均由程式串接，移除五條翻譯多出的參數、重複單位／符號。

各鍵的英文、修改前後完整值見 [修復清單](../tools/gregtech_tooltip_fixes.json)。逐鍵規則已加入 `tools/normalize_terms.py`，避免後續重跑將修復撤回。

## 動態 Tooltip 與不應強制修改之處

- 電池箱充電槽、多方塊最大輸入等級、NEI 電壓、Waila 儲能、線纜等相關提示已比對；既有必要動態參數未因本批被移除。
- `GTTooltipDataCache.getAllLines` 會將同一組參數傳入每一行。因此 `GT5U.machines.stalled_stuttering.tooltip.1/.2` 將 `%1$s` 移到另一行是合法中文語序，未修改。
- `MTETransformer.getWailaBody` 由 `mWailaTransformerVoltageTier` 設定決定顯示等級或電壓數值；部分 Input/Output 文字直接寫在程式內。本次沒有強制開啟設定、翻改寫死字串或讓原版不顯示等級的路徑額外顯示等級。物品 Tooltip 與 Waila 不能視為同一顯示邏輯。
- `%d`／`%f` 與 `%s` 的差異須考慮 Minecraft 1.7.10 語言載入的數字格式轉換，不能將所有差異一律視為錯誤；`%,d` 仍須保留旗標。

## 檢查範圍與驗證

原始英文直接取自安裝 jar 的 15 個 assets 語言命名空間，覆蓋比對 11303 條既有繁中項目，其中 2171 條符合機器／電力／Tooltip 篩選。另對照執行時產生的 `GregTech.lang` 與專案 `GregTech_zh_TW.lang` 共 69,311 個共用鍵，包含 29,667 個篩選項；執行時檔可能含舊鍵，因此以現行 jar 呼叫點核實具體修復，未盲目覆蓋歷史條目。

- 299 個語言檔檢查：鍵順序、行數、未審查的變更檢查通過；變更恰為修復清單的 26 條。
- 修復值對照本機 jar 的英文來源，參數索引、型別、旗標、精度檢查通過；直接取字串／串接的鍵另按呼叫點處理。
- 以 Git HEAD 重跑既有標準化規則，可重現全部 299 個語言檔；第二次重跑不再變更內容。
- Java 格式化測試使用本機位元碼確認的參數型別，並模擬 1.7.10 的數字格式轉換；11 組範例通過。範例文字為「電壓輸入：512（HV）」、「容量：32,768 EU」；蟲洞測試的 20 秒、32,768 EU、64 A/t 與效率均對應正確。這是格式化測試，不是遊戲內渲染測試。
- `git diff --check` 通過。

可重跑檢查：

```sh
python3 tools/verify_gregtech_tooltips.py --game /path/to/.minecraft --base c2df426
```

機器可讀結果見 [驗證報告](verification-gregtech-tooltips.json)。舊工具 `verify_translation.py` 只允許與舊翻譯相同的保護符號，會將本次刻意恢復／移除的參數視為錯誤，因此本批另用來源比對與精確修復清單驗證，沒有放寬原工具。

## 尚未完成與遊戲內確認

修復已寫入專案，並經使用者授權備份、同步至本機遊戲的六個 txloader 語言檔；只更新本批 26 個修復鍵，保留遊戲檔其他內容。同步後逐鍵讀回確認一致。尚未重開遊戲或遊戲內實測，不能宣稱目前正在執行的遊戲畫面已恢復。完整重開後，請確認 HV 研磨機的 512／HV、其他等級加工機、發電機輸出、變壓器、電池箱及能源／動力倉；另確認線圈、無線充電器、神鍛及蟲洞資訊。

全專案語意校對未在本批完成。自動掃描剩餘的八個資產候選項已分類：兩條合法的跨行參數、兩條字面百分比誤判，以及三條生物實驗道具與一條 Vajra 工具模式文案的既有版本差異。最後四條與本次機器／電壓顯示修復無關，保持原樣；詳細鍵名保留於驗證報告，不能將候選清單視為全部已修正或全部都是錯誤。

## 實際修改的檔案

- `config/txloader/load/GregTech[gregtech]/lang/zh_TW.lang`：9 條。
- `config/txloader/load/GregTech[miscutils]/lang/zh_TW.lang`：7 條。
- `config/txloader/load/GregTech[tectech]/lang/zh_TW.lang`：3 條。
- `config/txloader/load/GregTech[goodgenerator]/lang/zh_TW.lang`：1 條。
- `config/txloader/load/GregTech[bartworks]/lang/zh_TW.lang`：1 條。
- `config/txloader/load/GregTech[detravscannermod]/lang/zh_TW.lang`：5 條。
- `tools/normalize_terms.py`：同步路徑限定的修復規則。
- `tools/gregtech_tooltip_fixes.json`：原文與修改前後對照。
- `tools/verify_gregtech_tooltips.py`：本批來源、參數、結構、重現與冪等性檢查。
- `docs/verification-gregtech-tooltips.json`、本紀錄：驗證結果與範圍說明。

編輯前備份位於專案外的 `備份/GregTech電壓修正-20261024-191915/project/`。本批已獲使用者授權提交並推送 GitHub；實際提交與推送結果以 Git 紀錄為準。

遊戲檔同步前備份：`備份/遊戲GregTechTooltip同步-20261024-192749/`（倉庫外，含六個原檔與雜湊／鍵數同步紀錄）。磁碟同步驗證通過，未主動重啟遊戲。
