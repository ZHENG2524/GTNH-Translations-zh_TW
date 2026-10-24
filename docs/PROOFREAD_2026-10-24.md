# 2026-10-24 接續校對與術語核對

本批基準：`c98b39c6ffbf12013fc327f78478f4294816e2fe`。對應遊戲 GTNH 2.8.4、GregTech `5.09.51.482`。

## 本批完成範圍

- 依現行 `forceload/betterquesting` 語言檔順序閱讀第 25–64 篇正文，共 40 篇；不是依數字任務 ID 排序。
- 本機 DefaultQuests 英文 JSON 找到其中 38 篇可供對照；第 32 篇（指南）與第 37 篇（靈魂繫結）未找到本機英文來源，因此這兩篇僅作繁中可讀性檢視，不能算原文語意校對完成。
- 修正 83 條語言值，分布於 4 個語言檔：GregTech 主檔 45、現行任務 20、舊版任務 12、舊版 minecraft 任務 6。同步規則於 `tools/normalize_terms.py`。
- 其中 45 條為 15 種已吸附萃取樹脂的材料、Werkstoff 與流體名稱；任務正文另修正 36 條，並同步兩份萃取流程描述的同名術語（該流程任務其餘內容未全面校對）。
- 明確修正包括：煤炭加工產物 coal coke 譯為「焦炭」、能量／蒸汽 buffer 譯為「緩衝」、手套放在飾品戒指欄、區塊載入說明的雙重否定與漏譯爆炸風險，以及「線上上方／多半隻會／手套需要被要」等錯字。
- 舊版對應條目只套用適用的片語修正，不用新版全文覆蓋舊文。

## 術語採用依據

繁中原則：先確認英文所指的遊戲物件，再參照中文 Wiki 的既有名稱，最後調整台灣用語。不能只對英文 key 逐字直譯，也不能將 Wiki 的新版配方當作 2.8.4 的事實。

| 英文或遊戲術語 | 本批繁中決定 | 證據與限制 |
|---|---|---|
| Filled … Extracting Nano Resin | 已吸附的…萃取奈米樹脂 | 2.8.4 原始碼：樹脂經萃取變成 Filled，電解後回收原樹脂並取出金屬；「已吸附」表達負載狀態，避免「滿溢」暗示溢出。不主張配方模擬了現實樹脂的精確飽和度。 |
| Precious Metals Alloy | 保留「稀有金屬合金」 | 中文 Wiki 的匠魂工具表與調律源金配方都能對應此英文；2.8.4 原碼成分是六種鉑族金屬。這是沿用遊戲譯名，不是將 precious 在一般化學語境翻成「稀有」。 |
| Toluene Tetramethyl Diisocyanate | 保留「PTMEG橡膠粗胚」 | Wiki 頁面列出相同英文與化學式，本機英文及 2.8.4 原碼也相符。但 Wiki 本頁有資料庫錯誤，只能作遊戲譯名佐證，不能視為標準化學名稱已確認。 |
| White Metal | 暫保留「白物質」，待查 | Wiki 材料索引有「白物質」，但未取得該頁英文對應，頁面直接存取回應 403。不能因此宣稱 White Metal 的譯名已獲確認。 |
| rarer earth / rare earth | 保留「罕土／稀土」區分 | 沿用現行任務對兩類材料的刻意區分。 |
| GUI / tooltip / buffer（本批已讀任務） | 介面／物品提示／緩衝 | 依語境調整；未對全專案進行無條件替換。電腦 cache 仍應是「快取」。 |

中文 Wiki 本次檢索結果包含 2.9.0 資料。部分直接頁面存取回應 403；有取得搜尋索引內容的頁面僅用作上述有限佐證，未假稱已讀到完整頁面。

來源（查詢日 2026-10-24）：

- [中文 Wiki：萃取奈米樹脂流程](https://gtnh.huijiwiki.com/wiki/萃取纳米树脂)
- [中文 Wiki：匠魂工具](https://gtnh.huijiwiki.com/wiki/匠魂工具)
- [中文 Wiki：調律源金](https://gtnh.huijiwiki.com/wiki/调律源金)
- [中文 Wiki：PTMEG 橡膠粗胚](https://gtnh.huijiwiki.com/wiki/PTMEG橡胶粗胚)
- [中文 Wiki：材料分類](https://gtnh.huijiwiki.com/wiki/分类:材料)
- [GT5-Unofficial 5.09.51.482：萃取與電解配方](https://github.com/GTNewHorizons/GT5-Unofficial/blob/5.09.51.482/src/main/java/gtnhlanth/loader/RecipeLoader.java)（例如 1763–1771、2403–2413 行，15 種樹脂均有對應循環）
- [同版本：樹脂與 PTMEG 相關材料](https://github.com/GTNewHorizons/GT5-Unofficial/blob/5.09.51.482/src/main/java/gtnhlanth/common/register/WerkstoffMaterialPool.java)
- [同版本：稀有金屬合金與 Atomic runoff 上下文](https://github.com/GTNewHorizons/GT5-Unofficial/blob/5.09.51.482/src/main/java/goodgenerator/items/GGMaterial.java)

## 尚未解決的來源差異

- 第 25 篇：現行中文為 Concussion Creeper，本機英文 JSON 為 Ender Creeper；保留現行名稱，待查實際生物與版本。
- 第 31 篇：本機英文有舊 Battlegear 欄位移轉警告，現行中文刪除了該歷史說明；不直接補回。
- 第 35 篇：物品過濾覆蓋板段落在中英文來源間不同，保留現行版本，尚未核實所有覆蓋板行為與原文提到的 bug。
- 第 48 篇：現行中文為 108 塊磚，本機英文為 104；流體輸出說明也不同。未改配方數字與設備機制。
- 第 60 篇：英文自身混用 Brass 與 Bronze，現行中文也混用黃銅／青銅；先保留，待對照任務目標與冶煉爐實際合金流程。
- 第 63 篇的譯者註含掉落率與冷卻時間，並非英文正文內容，尚未核對程式碼。
- `The break in the line` 仍無法確定梗義。`Atomic runoff` 原碼上下文是具毒性與放射性的矽岩瀝青，但精確雙關未確認，繼續保留英文。

## 自動檢查與品質界線

執行：

```sh
python3 tools/verify_translation.py --base c98b39c6 --reproduce
git diff --check
```

- 299 個語言檔共 168,337 個鍵值條目完成 UTF-8 解碼及結構掃描；本批 key、順序、行數、格式碼、佔位符、標記、連結與跳脫換行皆保持不變。
- 以基準版本重跑現行校準規則，可重現全部語言檔；再次重跑無差異。
- 全倉庫既有重複 key 多出 56 個條目，其中 4 組同 key 的值不一致，均在 GregTech 模組檔的進階感測卡說明；本批未修改，後續應核對實際載入順序與英文。
- 既有空白值 2,637 個，不能直接認定為漏譯。GregTech 主檔佔 2,563 個；其中 2,528 個在本機英文也是空白／空格，35 個在本機英文找不到 key，沒有發現英文有實質文字卻被本批留空的項目。其他檔案的空白值仍待逐一核對。
- 本批未新增空白或重複 key。上述檢查證明沒有這些結構退化，**不能證明全部翻譯語意正確**。
- 未遊戲內實測。未確認遊戲是否重新啟動載入前一批內容。本批沒有更新遊戲檔案。
- 授權範圍仍依 README 的既有說明，尚未釐清；不宣稱整包已完成授權確認。

下次從現行任務第 65 篇正文接續；第 32、37 篇與上述來源差異仍需回查。
