# 交接：GTNH zh_TW 後續處理（給下一個 AI）

## 目前狀態
- 原始清單 `GTNH_untranslated_remaining.csv`（780 條）已全部處理，結果在 `tools/GTNH_remaining_translated.csv`（欄位 file,key,english_value,zh_tw,notes）。
- 譯文已寫回對應的 `config/txloader/load/<Mod>/lang/zh_TW.lang`（CSV 的 file 欄是 zh_CN.lang，對應改為 zh_TW.lang），780 條皆成功套用、無缺檔缺 key；16 條重複 key 兩處都已替換。尚未進遊戲實測。
- 本倉庫已 git init 並有一次 commit；**尚未推送 GitHub**，授權條款未定（使用者要先確認）。
- 原始 `GTNH_zh_TW.zip` 未被修改；完整成品為桌面 `GTNH_zh_TW_full.zip`。

## 統計
- 已翻譯 347 條（Blood Magic 書 239 條）；保留原文 421 條（指令、函式簽名、曲名／專輯、`<IMG>`、連結、Email、base64、Mod／玩家名、梗）；TRUNCATED 6 條；TERM? 47 條。

## 待辦（依優先序）
1. **TRUNCATED（6 條，保留英文，勿猜測）**：從模組 jar 取完整字串後再翻。
   - `modularui2.config.smooth_progress_bar.tooltip`
   - `aw.entries.spells.simpleEffects.10`
   - `gt.blockmachines.multimachine.FOG.upgradeinfotext.3`
   - Witching Gadgets 的 `witchinggadgets_research_page.GEMCUT_TABLE.1`、`GEMCUT_STEP.1`、`GEMCUT_ROSE.1`（結尾 "The table cut is" 疑似截斷，為我的判斷）。
2. **TERM?（47 條，notes 欄含 `TERM?`）**：查 GTNH 維基（gtnh.miraheze.org）核對譯名。**上一輪沒有連線查維基**，譯名是參考既有 zip 的詞彙（線軸、線束、皮米、量子、普朗克尺度、機架、切條X板 等）推出。主要是 `gt.circuitcomponent.*`、Thaumcraft 自訂元素（Aequalitas 等）、Manifold Bud、Bedrockium、Pseudostable Black Hole Containment Field、Cooper's Mallet、蜂種名。
3. **維基核對**：notes 標「沿用既有 zh_TW 譯名；未連線查維基」者（鍋爐、艙口、淨化單元等）。
4. **遊戲內實測**：載入後確認無亂碼、`\n`／`%n`／`[br]`／`[url ...]` 顯示正常。
5. **授權與公開**：確認授權後由使用者提供空倉庫網址再推送；這台機器沒有 `gh`，未登入 GitHub。

## 已確定的決定（請沿用）
- 規則見桌面 `HANDOFF_sonnet_GTNH_zh_TW.md` 與術語表（儀式、印記、符文、試劑、血球、血祭壇…）。
- Blood Magic 書：Tiberius、Magus、Vlad、Demir、Bella、Sinferrous、Tartarus、Conglomeration 等人名地名保留英文；試劑名（Aether、Terrae…）保留拉丁文；印記／符文／儀式名沿用既有 guide 標題與物品名（速掘印記、增容符文、轉位符文、獻祭匕首、羽刃、滿春儀式等）。
- 下界用「下界」、終界用「終界」、Ghast 用「地獄幽靈」，與既有 zip 一致。
- 第 252 條（Witchery 書）`[url power]` 等連結目標刻意保留英文，避免連結失效。
- `gui.floodlights:true/false` 譯為「是／否」（推測）。
- `tc.research_page.GLYPHSTONE.1` 在別的檔案另有不同內容的中文，本檔依英文翻譯。
- 檢查用 OpenCC s2twp：僅剩台灣用詞變體差異（綁定／繫結、台／臺 等），無簡體字；已改過運行→運作、設置→架設／建立、打開→開啟、優化→最佳化。

## 檔案
- `tools/GTNH_remaining_translated.csv`：譯文與 notes。
- `config/…`、`GregTech_zh_TW.lang`：可直接使用的語言檔。
- `README.md`：安裝說明與已知限制。
