<div align="center">

# GTNH 繁體中文（台灣）語言包

**GT New Horizons · Traditional Chinese (Taiwan)**

讓物品、機器、任務書和手冊都用台灣玩家熟悉的中文呈現。

[![Release](https://img.shields.io/github/v/release/ZHENG2524/GTNH-Translations-zh_TW?include_prereleases&style=flat-square&label=%E6%9C%80%E6%96%B0%E7%89%88%E6%9C%AC&color=2563eb)](../../releases)
[![GTNH](https://img.shields.io/badge/GTNH-2.8.4-16a34a?style=flat-square)](https://www.gtnewhorizons.com/)
[![GregTech](https://img.shields.io/badge/GregTech-5.09.51.482-f59e0b?style=flat-square)](https://github.com/GTNewHorizons/GT5-Unofficial)
[![Stars](https://img.shields.io/github/stars/ZHENG2524/GTNH-Translations-zh_TW?style=flat-square&color=eab308)](../../stargazers)
[![Last commit](https://img.shields.io/github/last-commit/ZHENG2524/GTNH-Translations-zh_TW?style=flat-square&label=%E6%9C%80%E5%BE%8C%E6%9B%B4%E6%96%B0)](../../commits/main)

[**下載安裝**](#-安裝) · [**專案現況**](#-專案現況) · [**術語規範**](docs/TERMINOLOGY.md) · [**回報問題**](../../issues)

</div>

> [!NOTE]
> 這是非官方的社群翻譯，與 GTNH 團隊及各模組作者沒有官方關係。內容由簡轉繁與 AI 輔助產生，再依原文和程式逐批校對，並非全部經過遊戲實測。

## ✨ 特色

| | |
| :--- | :--- |
| 🧭 **涵蓋完整** | 299 個語言檔、約 17 萬條：GregTech、任務書、神秘研究、匠魂手冊、HEE 圖鑑等 |
| 📖 **任務書全讀** | 3,859 篇全數閱讀，有英文來源的逐篇對照 |
| 🇹🇼 **台灣用語** | 雷射、終界、核融合、電漿、權限等，術語規範公開可查 |
| 🔎 **NEI 可用繁中搜尋** | 物品與材料名稱皆為繁體中文 |
| 🧪 **機制也查證** | 英文與實際程式不符時，依安裝版本的位元碼判斷 |

## 🚀 安裝

1. 到 [**Releases**](../../releases) 下載最新版 ZIP。想用還沒發版的最新內容，改用 **Code → Download ZIP**。
2. **完整關閉遊戲**，並備份實例的 `config/` 與 `GregTech_zh_TW.lang`。
3. 把壓縮檔內的 `config/` 和 `GregTech_zh_TW.lang` 合併到實例的 `.minecraft`。
4. 啟動遊戲，語言選擇 **繁體中文（台灣）**。

> [!CAUTION]
> 請用合併的方式，**不要刪除原本的 `config` 資料夾**。`GregTech_zh_TW.lang` 可能含遊戲執行時新增的本機條目，覆蓋前請先備份。

## 📊 專案現況

更新日期：2026-11-01

| 範圍 | 狀態 |
| :--- | :--- |
| 語言檔補齊 | ✅ 整合包內建模組的主要內容已補齊，已用工具核對 |
| 任務書閱讀 | ✅ 3,859 篇讀完；版本差異項目保留原值待實測 |
| 神秘研究、匠魂手冊、CoreMod 物品 | ✅ 2026-11-01 補齊 1,825 條，**待遊戲實測** |
| HEE 終界圖鑑 | ✅ 2026-11-01 補齊 399 條，**待遊戲實測** |
| 術語規範 | ✅ 86 組，異體詞已統一 |
| LV／MV／HV 電壓提示 | ✅ 已遊戲實測 |
| 其餘文字的遊戲內顯示 | 🧪 尚待實測 |

`main` 分支可能比最新 Release 新。完整紀錄請看[持續校對進度](docs/TRANSLATION_PROGRESS.md)。

### 刻意保留英文的內容

指令語法、化學式、歌名、成就梗、Ztones 代號方塊名，以及神秘時代的拉丁源質名。這些不是漏譯。

## 🖥️ 伺服器

伺服器產生的歡迎訊息等文字，客戶端語言包改不了。請看獨立專案 [**GTNH-Server-zh_TW**](https://github.com/ZHENG2524/GTNH-Server-zh_TW)。

## 🤝 參與貢獻

看到不順或錯誤的翻譯，歡迎開 [Issue](../../issues) 或送 PR。請盡量附上：

- 遊戲畫面或文字，以及模組名稱
- 英文原文或語言檔的 key
- 你建議的台灣譯法

動手前請先看[術語規範](docs/TERMINOLOGY.md)。改完可用這兩個工具檢查：

```bash
python3 tools/verify_translation.py --base HEAD
```

```bash
python3 tools/check_key_coverage.py --game /path/to/.minecraft
```

## 📚 文件

| 文件 | 內容 |
| :--- | :--- |
| [術語規範](docs/TERMINOLOGY.md) | 譯名對照、例外與查證來源 |
| [持續校對進度](docs/TRANSLATION_PROGRESS.md) | 各批成果與待查清單 |
| [更新歷史](docs/HISTORY.md) | 早期批次與建置統計 |
| [AI 接續交接](HANDOFF_next_ai.md) | 協作者的操作背景 |

## ⚠️ 已知限制

- 寫死在模組程式碼裡的文字無法用語言檔翻譯。Extra Utilities 與 IronChest 有修補工具，見 `tools/`，模組更新後需重做。
- 部分字串因版本差異保留原值，需要實測才能判斷。

<details>
<summary><strong>📜 來源與授權</strong></summary>

## 來源與授權說明
### 翻譯來源
- **簡體中文來源**：[GTNewHorizons/GTNH-Translations](https://github.com/GTNewHorizons/GTNH-Translations) 的 `zh_CN`（例如 `GregTech_zh_CN.lang`），經 OpenCC `s2twp` 簡轉繁、用語調整（`tools/normalize_terms.py`）及 AI 輔助處理而來。本倉庫**不含**簡體中文原始檔，只含轉換後的繁體檔。
- **既有繁中**：沿用 GTNH 整合包內既有的 `zh_TW` 語言檔。
- **新增翻譯**：780 條剩餘字串與部分提示為 AI 翻譯，詳見[更新歷史](docs/HISTORY.md)。

### 授權
不同內容適用不同授權，**本倉庫不主張整個倉庫都能以同一授權自由使用**：

| 內容 | 原始授權 | 說明 |
|---|---|---|
| GTNH-Translations（簡體來源） | [GPL-3.0](https://github.com/GTNewHorizons/GTNH-Translations/blob/master/LICENSE) | 由其轉換而來的內容，應遵守 GPL-3.0 |
| GT New Horizons 整合包 | [CC BY-NC-SA 4.0](https://github.com/GTNewHorizons/GT-New-Horizons-Modpack/blob/master/LICENSE) | 整合包內既有語言檔 |
| GregTech 5 Unofficial | LGPL-3.0 | 原文字串來源 |
| 其他各模組 | 各自不同（MIT、LGPL、保留所有權利等） | 以各模組附帶的授權為準 |

- 本倉庫的 [LICENSE](LICENSE) 為 GPL-3.0，與簡體來源 GTNH-Translations 一致。原為 CC BY-NC-SA 4.0，已因兩者不相容而更換。
- **但既有繁中內容源自整合包的 `zh_TW` 語言檔（CC BY-NC-SA 4.0，含非商業條件），改用 GPL-3.0 無法消除這部分的限制。** 在釐清前，本倉庫不主張可商業使用，也不保證整個倉庫能以單一授權完整涵蓋。
- 若任何權利人認為本專案不符其授權條件，請開 issue，將立即調整或移除。
- 本專案免費提供。免費不代表第三方內容可不受原始授權限制。
- 遊戲原文及原始翻譯的著作權屬 GTNH 團隊、各模組作者及原翻譯貢獻者。

</details>

---

<div align="center">

由使用者與 [Claude Code](https://claude.com/claude-code) 協力製作

</div>
