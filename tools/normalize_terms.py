#!/usr/bin/env python3
"""Apply Taiwan-usage term normalization to lang values only (keys untouched).
Usage: normalize_terms.py <repo_root>   (edits files in place; use git to review/revert)"""
import sys, pathlib, collections

# 順序有意義：較長詞先換
RULES = [
    ("核聚變", "核融合"), ("聚變", "核融合"),
    ("鐳射", "雷射"),
    ("末影", "終界"),
    ("下界", "地獄"),
    ("反應堆", "反應爐"),
    ("巖", "岩"),
    ("吸 幹 抹 淨", "吸 乾 抹 淨"),
    ("等離子體", "電漿"), ("等離子", "電漿"),
    ("刻蝕", "蝕刻"),
    ("溼", "濕"), ("杆", "桿"),
    ("電子計算機機械方塊", "電腦機械方塊"), ("電子計算機械方塊", "電腦機械方塊"),
    ("計算機", "電腦"),
    ("資料訪問", "資料存取"), ("映象", "鏡像"),
    ("型別", "類型"), ("工作臺", "工作台"), ("平臺", "平台"),
    ("亞熒石", "亞螢石"), ("熒石", "螢光石"), ("熒光", "螢光"),
    ("滷水", "鹵水"), ("502膠水", "瞬間膠"), ("海晶參雜", "海晶摻雜"),
]

# 只套用在 GregTech_zh_TW.lang 的規則（其他模組的「快取」可能真的是 cache）
GT_ONLY_RULES = [("快取", "緩衝")]

# GregTech_zh_TW.lang 內逐 key 修正（材料名等，值完全取代）
KEY_FIXES = {
    "fluid.dimethyldichlorosilane": "二甲基二氯矽烷",
    "fluid.hexachlorodisilane": "六氯二矽烷",
    "fluid.hydrochloricacid_gt5u": "鹽酸",
    "bw.werkstoff.00043.tooltip": "你認真的嗎？",
    "bw.werkstoff.10022.tooltip": "熔融核心……",
    "bw.werkstoff.10025.tooltip": "還差得遠",
    "bw.werkstoff.10026.tooltip": "仍需加工",
    "bw.werkstoff.10027.tooltip": "誰需要它？",
    "bw.werkstoff.10035.tooltip": ">>> 危險 <<<",
    "bw.werkstoff.10039.tooltip": "第一步",
    "bw.werkstoff.10040.tooltip": "第一步（已踏出）",
    "bw.werkstoff.10041.tooltip": "六百億千瓦時",
    "bw.werkstoff.10042.tooltip": "六百億千瓦時（已耗用）",
    "bw.werkstoff.10046.tooltip": "力量勢不可擋",
    "bw.werkstoff.10047.tooltip": "力量不再勢不可擋",
    "bw.werkstoff.10048.tooltip": "擊落太陽",
    "bw.werkstoff.10049.tooltip": "擊落太陽（已完成）",
    "bw.werkstoff.10050.tooltip": "終點",
    "bw.werkstoff.10051.tooltip": "終點（字面上的）",
    "bw.werkstoff.10116.tooltip": "未來",
    "bw.werkstoff.10117.tooltip": "未來（已實現）",
    "Material.silicon": "矽",
    "fluid.molten.silicon": "熔融矽",
    "fluid.plasma.silicon": "矽電漿",
    "Material.nano": "奈米",
    "Material.piko": "皮米",
    "Material.hexachlorodisilane": "六氯二矽烷",
    "Material.dimethyldichlorosilane": "二甲基二氯矽烷",
    "Material.crudeoil": "原油",
    "Material.endstone": "終界石",
    "Material.hydrochloricacid_gt5u": "鹽酸",
    "fluid.enzymessollution": "酵素溶液",
    "fluid.molten.chrysotile": "熔融白石棉",
    "fluid.molten.mercassium": "熔融瑪卡斯",
    "fluid.molten.potin": "熔融鉛青銅",
    "fluid.potion.potatojuice": "馬鈴薯汁",
    "fluid.potion.rum": "蘭姆酒",
    "fluid.bastnasite rarer earth oxide suspension": "氟碳鑭鈰罕土氧化物懸濁液",
}

# 依倉庫相對路徑限定的逐 key 修正，避免改到其他模組的同名 key。
FILE_KEY_FIXES = {
    "config/txloader/load/BetterQuesting[betterquesting]/lang/zh_TW.lang": {
        "betterquesting.editor.action.hex_color": "§c十六進位顏色§r",
        "betterquesting.editor.color_picker.hex": "十六進位顏色",
        "betterquesting.editor.action.gradient": "§b漸層色§r",
        "betterquesting.editor.color_picker.gradient": "漸層色",
        "betterquesting.btn.advanced": "進階設定",
        "betterquesting.btn.import": "匯入",
        "betterquesting.btn.detect_submit": "偵測／交付",
        "betterquesting.btn.hide_locked_quest_lines": "隱藏鎖定的任務章節",
        "betterquesting.btn.prereq_visbility.implicit": "僅在游標停留或按住 Shift 時顯示",
        "betterquesting.gui.closing_confirm": "本次修改的資料可能會遺失！",
        "betterquesting.tooltip.global_quest": "全域任務: %s",
        "betterquesting.tooltip.global_share": "全域共享: %s",
        "betterquesting.tooltip.shift_advanced": "按住 Shift 顯示進階資訊",
        "betterquesting.tooltip.cycle.true": "點選以停用",
        "betterquesting.tooltip.cycle.false": "點選以啟用",
        "betterquesting.tooltip.quest_link.click": "點選以前往",
        "key.betterquesting.party": "開啟隊伍管理",
        "key.betterquesting.themes": "開啟主題選單",
        "betterquesting.help.page1": "§l§n介面導覽%n§r%nBetter Questing 的任務介面可透過快捷鍵開啟，不必依賴容易遺失的物品或方塊。你可以在控制設定中查看或變更這個快捷鍵。%n%n在任務章節畫面中，你可以從列表選擇已開啟的章節，再拖曳任務圖，找到想要完成的任務。%n%n你可以在隊伍管理畫面中建立或編輯隊伍，也能設定是否共用極限模式的生命次數或任務獎勵。%n%n如果想改變任務介面的外觀，可以在主題選擇畫面中挑選已安裝的主題。",
        "betterquesting.help.page2": "§l§n提交站%n§r%n許多任務目標可以直接透過物品欄提交，流體也不例外，但有時你會需要自動化的方式。物品提交站（OSS）就是為此而設。你可以在內建介面中選擇支援 OSS 的任務目標。設定完成後，就能透過管線輸入物品與流體，或將物品放入介面的輸入欄位。如果尚未選擇任務目標，或目標已經完成，提交站不會銷毀物品或流體，因此較不容易意外損失資源。多個 OSS 也能同時處理同一任務中的不同子目標！",
        "betterquesting.help.page3": "§l§n製作任務%n§r%n若要製作任務與任務章節，請先執行編輯指令以啟用編輯模式（詳見指令說明）。接著，你就能新增或刪除任務章節；即使不建立章節，也能直接製作任務。這對製作能解鎖其他任務或章節的隱藏任務特別方便。%n%n編輯時需要熟悉幾個選單。與其他模組相比，起初可能比較難上手，但熟悉後就會容易許多。部分進階編輯畫面會直接修改原始任務資料，請謹慎操作，以免造成非預期結果；正常情況下不應導致資料損毀或遊戲崩潰。若發生這些問題，請立即回報開發者。",
        "betterquesting.help.page4": (
            "§l§n指令%n§r%n使用 Better Questing 時，只需熟悉少數幾個指令。它們分為所有玩家都能執行的玩家指令，以及僅限伺服器管理員執行的管理指令。%n%n§o/bq_user refresh%n§r%n手動"
            "將本機任務資料與伺服器重新同步，用於處理可能的同步問題。%n%n§o/bq_user help%n§r%n給玩家一本指南。%n%n§o/bq_admin edit%n§r%n開啟或關閉任務編輯模式。啟用後，管理員可以進"
            "入任務與任務章節的編輯選單。發布整合包或任務前，請記得關閉此模式。%n%n§o/bq_admin hardcore%n§r%n開啟或關閉極限模式的生命次數機制。生命耗盡時，玩家會被伺服器封鎖，或依原版極限模式的方式刪除其"
            "世界。%n%n§o/bq_admin reset [all|<quest_id>] [username|uuid]%n§r%n清除指定玩家的任務完成資料，適合在發布整合包前使用。%n%n§o/bq_admin defau"
            "lt [save|load]%n§r%n將目前的任務資料儲存至全域預設目錄，或從該目錄載入。設定預設資料後，新建的世界都會使用這組任務。儲存時也會保留完成進度、極限模式與編輯模式的狀態，因此執行前應先用其他相關指令調整這"
            "些設定。%n%n§o/bq_admin complete <quest_id> [username|uuid]%n§r%n強制完成指定玩家的任務。%n%n§o/bq_admin delete [all|<quest_id"
            ">]%n§r%n刪除指定任務及其進度資料，但不會刪除新世界使用的預設任務資料。%n%n§o/bq_admin lives [add|set|max|default] <value> [username]%n§r%n調整玩"
            "家的生命次數、初始生命次數或生命次數上限。"
        ),
        "betterquesting.help.page5": "§l§n匯入%n§r%n部分擴充套件提供其他任務模組的匯入工具，或讓整合包製作者下載線上的任務章節。你可以在任務章節編輯器中按下「匯入」按鈕來使用這些工具。Better Questing 預設不附匯入工具；若有需要，請尋找包含所需工具的擴充套件，或自行製作。",
        "betterquesting.help.page6": "§l§n主題%n§r%n不論你偏好特定的介面配色，或想讓整合包呈現獨特風格，都可以透過主題調整任務介面。主題能配合各種需求，呈現未來科技、魔法或經典 Minecraft 的風格。你可以透過資源包、資源目錄或擴充套件安裝主題。",
        "betterquesting.help.page7": "§l§n在地化%n§r%nBetter Questing 支援任務名稱與說明的完整在地化，讓你能將整合包提供給不同語言的玩家使用。若要開始翻譯任務，請先以唯一的翻譯鍵取代純文字，例如「§omypack.quest1.name§r」。接著，建立只包含各語言 .lang 翻譯檔的資源包。你也可以將這些檔案放在 Better Questing 的資源目錄中，方便隨整合包一同提供。",
        "betterquesting.help.page8": "§l§n資源%n§r%n若要自訂首頁、附加主題或新增在地化檔案，可以使用以下目錄：%n%n「§o/config/betterquesting/resources/<pack_name>/§r」%n%n這裡的資料夾會被視為未列出的資源包，可放入整合包個人化所需的各種資源。",
        "betterquesting.btn.help1": "介面導覽",
        "betterquesting.btn.help5": "匯入",
        "betterquesting.btn.help7": "在地化",
    },
    "config/txloader/load/BetterQuesting[bq_standard]/lang/zh_TW.lang": {
        "bq_standard.task.retrieval": "物品收集任務",
        "bq_standard.task.optional_retrieval": "選用任務",
        "bq_standard.title.edit_retrieval": "編輯物品收集任務",
        "bq_standard.trade_unlock": "關聯的自動販賣機兌換項目",
        "bq_standard.gui.undiscovered": "尚未發現",
    },
}

# 僅修正已校對的任務 key 內片語，保留各版本的配方、格式與連結。
FILE_KEY_RULES = {
    "config/txloader/forceload/betterquesting/lang/zh_TW.lang": {
        "betterquesting.quest.AAAAAAAAAAAAAAAAAAAAAA.desc": [['教程', '教學'], ['頻道里', '頻道裡'], ['定製版本', '客製版本']],
        "betterquesting.quest.AAAAAAAAAAAAAAAAAAAAAg.desc": [['除去收集', '出去收集']],
        "betterquesting.quest.AAAAAAAAAAAAAAAAAAAABQ.desc": [['空手擼樹', '徒手砍樹']],
        "betterquesting.quest.AAAAAAAAAAAAAAAAAAAABg.desc": [['抄出一堆種子', '搜出一堆種子']],
        "betterquesting.quest.AAAAAAAAAAAAAAAAAAAADQ.desc": [['教程', '教學']],
        "betterquesting.quest.AAAAAAAAAAAAAAAAAAAB1Q.desc": [['長大麼', '長大嗎']],
        "betterquesting.quest.AAAAAAAAAAAAAAAAAAABjA.desc": [['自定義', '自訂']],
        "betterquesting.quest.AAAAAAAAAAAAAAAAAAABjQ.desc": [['好幾周目', '好幾輪']],
        "betterquesting.quest.AAAAAAAAAAAAAAAAAAABug.desc": [['土豆', '馬鈴薯']],
    },
    "config/txloader/load/betterquesting/lang/zh_TW.lang": {
        "betterquesting.quest.AAAAAAAAAAAAAAAAAAAAAA.desc": [['教程', '教學'], ['生活質量', '生活品質']],
        "betterquesting.quest.AAAAAAAAAAAAAAAAAAAABQ.desc": [['空手擼樹', '徒手砍樹']],
        "betterquesting.quest.AAAAAAAAAAAAAAAAAAAABg.desc": [['抄出一堆種子', '搜出一堆種子']],
        "betterquesting.quest.AAAAAAAAAAAAAAAAAAAADQ.desc": [['教程', '教學']],
        "betterquesting.quest.AAAAAAAAAAAAAAAAAAAB1Q.desc": [['長大麼', '長大嗎']],
        "betterquesting.quest.AAAAAAAAAAAAAAAAAAABjA.desc": [['自定義', '自訂'], ['我麼建議', '我們建議']],
        "betterquesting.quest.AAAAAAAAAAAAAAAAAAABjQ.desc": [['研究出瞭如何', '研究出如何'], ['好幾周目', '好幾輪']],
        "betterquesting.quest.AAAAAAAAAAAAAAAAAAABug.desc": [['土豆', '馬鈴薯']],
        "betterquesting.quest.AAAAAAAAAAAAAAAAAAABvA.desc": [['用他們做', '用它們做']],
    },
    "config/txloader/load/minecraft/lang/zh_TW.lang": {
        "gtnh.quest5.desc": [['空手擼樹', '徒手砍樹']],
        "gtnh.quest6.desc": [['抄出一堆種子', '搜出一堆種子']],
        "gtnh.quest396.desc": [['自定義', '自訂']],
        "gtnh.quest440.desc": [['工作列', '任務章節'], ['有很多工欄', '有很多任務章節']],
        "gtnh.quest442.desc": [['土豆', '馬鈴薯']],
        "gtnh.quest444.desc": [['用他們做', '用它們做']],
        "gtnh.quest469.desc": [['長大麼', '長大嗎']],
    },
}

# 2026-10-24：第 25–64 篇任務與 2.8.4 萃取樹脂流程校對。
KEY_FIXES.update({'Material.filledceriumextractingnanoresin': '已吸附的鈰萃取奈米樹脂',
 'Material.filleddysprosiumextractingnanoresin': '已吸附的鏑萃取奈米樹脂',
 'Material.fillederbiumextractingnanoresin': '已吸附的鉺萃取奈米樹脂',
 'Material.filledeuropiumextractingnanoresin': '已吸附的銪萃取奈米樹脂',
 'Material.filledgadoliniumextractingnanoresin': '已吸附的釓萃取奈米樹脂',
 'Material.filledholmiumextractingnanoresin': '已吸附的鈥萃取奈米樹脂',
 'Material.filledlanthanumextractingnanoresin': '已吸附的鑭萃取奈米樹脂',
 'Material.filledlutetiumextractingnanoresin': '已吸附的鎦萃取奈米樹脂',
 'Material.filledneodymiumextractingnanoresin': '已吸附的釹萃取奈米樹脂',
 'Material.filledpraseodymiumextractingnanoresin': '已吸附的鐠萃取奈米樹脂',
 'Material.filledpromethiumextractingnanoresin': '已吸附的鉕萃取奈米樹脂',
 'Material.filledsamariumextractingnanoresin': '已吸附的釤萃取奈米樹脂',
 'Material.filledterbiumextractingnanoresin': '已吸附的鋱萃取奈米樹脂',
 'Material.filledthuliumextractingnanoresin': '已吸附的銩萃取奈米樹脂',
 'Material.filledytterbiumextractingnanoresin': '已吸附的鐿萃取奈米樹脂',
 'bw.werkstoff.11402.name': '已吸附的鑭萃取奈米樹脂',
 'bw.werkstoff.11404.name': '已吸附的鐠萃取奈米樹脂',
 'bw.werkstoff.11406.name': '已吸附的鈰萃取奈米樹脂',
 'bw.werkstoff.11408.name': '已吸附的釹萃取奈米樹脂',
 'bw.werkstoff.11410.name': '已吸附的鉕萃取奈米樹脂',
 'bw.werkstoff.11412.name': '已吸附的釤萃取奈米樹脂',
 'bw.werkstoff.11414.name': '已吸附的銪萃取奈米樹脂',
 'bw.werkstoff.11416.name': '已吸附的釓萃取奈米樹脂',
 'bw.werkstoff.11418.name': '已吸附的鋱萃取奈米樹脂',
 'bw.werkstoff.11420.name': '已吸附的鏑萃取奈米樹脂',
 'bw.werkstoff.11422.name': '已吸附的鈥萃取奈米樹脂',
 'bw.werkstoff.11424.name': '已吸附的鉺萃取奈米樹脂',
 'bw.werkstoff.11426.name': '已吸附的銩萃取奈米樹脂',
 'bw.werkstoff.11428.name': '已吸附的鐿萃取奈米樹脂',
 'bw.werkstoff.11430.name': '已吸附的鎦萃取奈米樹脂',
 'fluid.filled cerium extracting nano resin': '已吸附的鈰萃取奈米樹脂',
 'fluid.filled dysprosium extracting nano resin': '已吸附的鏑萃取奈米樹脂',
 'fluid.filled erbium extracting nano resin': '已吸附的鉺萃取奈米樹脂',
 'fluid.filled europium extracting nano resin': '已吸附的銪萃取奈米樹脂',
 'fluid.filled gadolinium extracting nano resin': '已吸附的釓萃取奈米樹脂',
 'fluid.filled holmium extracting nano resin': '已吸附的鈥萃取奈米樹脂',
 'fluid.filled lanthanum extracting nano resin': '已吸附的鑭萃取奈米樹脂',
 'fluid.filled lutetium extracting nano resin': '已吸附的鎦萃取奈米樹脂',
 'fluid.filled neodymium extracting nano resin': '已吸附的釹萃取奈米樹脂',
 'fluid.filled praseodymium extracting nano resin': '已吸附的鐠萃取奈米樹脂',
 'fluid.filled promethium extracting nano resin': '已吸附的鉕萃取奈米樹脂',
 'fluid.filled samarium extracting nano resin': '已吸附的釤萃取奈米樹脂',
 'fluid.filled terbium extracting nano resin': '已吸附的鋱萃取奈米樹脂',
 'fluid.filled thulium extracting nano resin': '已吸附的銩萃取奈米樹脂',
 'fluid.filled ytterbium extracting nano resin': '已吸附的鐿萃取奈米樹脂'})
FILE_KEY_RULES.setdefault('config/txloader/forceload/betterquesting/lang/zh_TW.lang', {}).update({'betterquesting.quest.AAAAAAAAAAAAAAAAAAAHMg.desc': [('一格視窗', '一格窗口'), ('隔著視窗', '隔著窗口')],
 'betterquesting.quest.AAAAAAAAAAAAAAAAAAAHMw.desc': [('詞條', '特殊能力')],
 'betterquesting.quest.AAAAAAAAAAAAAAAAAAAHOQ.desc': [('一直跳著上下', '一直跳上跳下')],
 'betterquesting.quest.AAAAAAAAAAAAAAAAAAALOg.desc': [('為了避免機器（特別是多方塊機器）不會一齊罷工', '為了避免機器（特別是多方塊機器）突然爆炸'),
                                                      ('預設配置', '預設設定'),
                                                      ('修改配置', '修改設定'),
                                                      ('檢視tooltip', '查看物品提示')],
 'betterquesting.quest.U7JoxM0mRaWx0MYriD2LtQ.desc': [('能開啟GUI', '能開啟介面'), ('客戶端配置', '用戶端設定')],
 'betterquesting.quest.pcDIaSYHTkuVTBkdRwWWJw.desc': [('教程', '教學'), ('繫結', '設定')],
 'betterquesting.quest.AAAAAAAAAAAAAAAAAAAGdg.desc': [('快取', '緩衝'), ('多方塊蓄水器', '多方塊鐵製或鋼製儲罐'), ('教程', '教學')],
 'betterquesting.quest.AAAAAAAAAAAAAAAAAAALDw.desc': [('tooltip', '物品提示'),
                                                      ('GUI', '介面'),
                                                      ('快取', '緩衝'),
                                                      ('程序0%%', '進度0%%'),
                                                      ('禁用機器', '停用機器'),
                                                      ('原有配置', '原有設定')],
 'betterquesting.quest.ZM4oSqeWQRW1Y-zoE01ivg.desc': [('掉落池', '掉落物清單')],
 'betterquesting.quest.AAAAAAAAAAAAAAAAAAAAFg.desc': [('所有需要水的配方里', '大多數需要水的配方裡'),
                                                      ('線上上方', '線的上方'),
                                                      ('仙人掌衝到', '仙人掌沖到')],
 'betterquesting.quest.AAAAAAAAAAAAAAAAAAAAFw.desc': [('然而並沒有什麼卵用', '但完全行不通')],
 'betterquesting.quest.AAAAAAAAAAAAAAAAAAAAGA.desc': [('你剛才收集一大堆材料', '你剛才收集了一大堆材料')],
 'betterquesting.quest.AAAAAAAAAAAAAAAAAAAAGg.desc': [('多半隻會', '多半只會')],
 'betterquesting.quest.AAAAAAAAAAAAAAAAAAAAHQ.desc': [('焦煤', '焦炭')],
 'betterquesting.quest.AAAAAAAAAAAAAAAAAAAAIQ.desc': [('部件加工臺', '部件加工台')],
 'betterquesting.quest.AAAAAAAAAAAAAAAAAAAAJA.desc': [('電子表格', '試算表')],
 'betterquesting.quest.AAAAAAAAAAAAAAAAAAAAKA.desc': [('你繫結的快捷鍵', '你設定的快捷鍵'), ('高亮提示效果', '醒目提示效果')],
 'betterquesting.quest.AAAAAAAAAAAAAAAAAAAAKQ.desc': [('手套需要被要裝備在Baubles飾品欄內，左右手位置隨意',
                                                       '手套需要裝備在Baubles飾品欄的戒指欄位，放哪一格都可以')],
 'betterquesting.quest.AAAAAAAAAAAAAAAAAAAAKg.desc': [('文字里的', '文字裡的')]})
FILE_KEY_RULES.setdefault('config/txloader/load/betterquesting/lang/zh_TW.lang', {}).update({'betterquesting.quest.AAAAAAAAAAAAAAAAAAAHMw.desc': [('詞條', '特殊能力')],
 'betterquesting.quest.AAAAAAAAAAAAAAAAAAALOg.desc': [('為了避免機器（特別是多方塊機器）不會一齊罷工', '為了避免機器（特別是多方塊機器）突然爆炸'),
                                                      ('預設配置', '預設設定'),
                                                      ('修改配置', '修改設定'),
                                                      ('檢視tooltip', '查看物品提示')],
 'betterquesting.quest.U7JoxM0mRaWx0MYriD2LtQ.desc': [('能開啟GUI', '能開啟介面'), ('客戶端配置', '用戶端設定')],
 'betterquesting.quest.AAAAAAAAAAAAAAAAAAAGdg.desc': [('快取', '緩衝'), ('多方塊蓄水器', '多方塊鐵製或鋼製儲罐'), ('教程', '教學')],
 'betterquesting.quest.AAAAAAAAAAAAAAAAAAALDw.desc': [('tooltip', '物品提示'), ('GUI', '介面')],
 'betterquesting.quest.ZM4oSqeWQRW1Y-zoE01ivg.desc': [('掉落池', '掉落物清單')],
 'betterquesting.quest.AAAAAAAAAAAAAAAAAAAAFg.desc': [('線上上方', '線的上方')],
 'betterquesting.quest.AAAAAAAAAAAAAAAAAAAAFw.desc': [('然而並沒有什麼卵用', '但完全行不通')],
 'betterquesting.quest.AAAAAAAAAAAAAAAAAAAAIQ.desc': [('部件加工臺', '部件加工台')],
 'betterquesting.quest.AAAAAAAAAAAAAAAAAAAAKQ.desc': [('手套需要被要裝備在Baubles飾品欄內，左右手位置隨意',
                                                       '手套需要裝備在Baubles飾品欄的戒指欄位，放哪一格都可以')],
 'betterquesting.quest.AAAAAAAAAAAAAAAAAAAAKg.desc': [('文字里的', '文字裡的')]})
FILE_KEY_RULES.setdefault('config/txloader/load/minecraft/lang/zh_TW.lang', {}).update({'gtnh.quest2874.desc': [('預設配置', '預設設定'), ('修改配置', '修改設定'), ('檢視tooltip', '查看物品提示')],
 'gtnh.quest1654.desc': [('快取', '緩衝')],
 'gtnh.quest2831.desc': [('tooltip', '物品提示'), ('GUI', '介面')],
 'gtnh.quest22.desc': [('線上上方', '線的上方')],
 'gtnh.quest23.desc': [('然而並沒有什麼卵用', '但完全行不通')],
 'gtnh.quest42.desc': [('文字里的', '文字裡的')]})

# 萃取流程說明同步名稱；其餘任務內容未在本批全面校對。
FILE_KEY_RULES.setdefault('config/txloader/forceload/betterquesting/lang/zh_TW.lang', {}).update({'betterquesting.quest.LzCq9t0cT4-_TizIr_Iq_A.desc': [['滿溢的', '已吸附的'], ['將他們投入', '將它們投入'], ['迴圈往復', '循環往復']]})
FILE_KEY_RULES.setdefault('config/txloader/load/betterquesting/lang/zh_TW.lang', {}).update({'betterquesting.quest.LzCq9t0cT4-_TizIr_Iq_A.desc': [['滿溢的', '已吸附的'], ['將他們投入', '將它們投入'], ['迴圈往復', '循環往復']]})

def fix_value(v, stat, extra=()):
    for a, b in list(RULES) + list(extra):
        n = v.count(a)
        if n:
            stat[a] += n
            v = v.replace(a, b)
    return v

def process(path, stat):
    out, changed = [], False
    is_gt = path.name == "GregTech_zh_TW.lang"
    relative_path = path.relative_to(root).as_posix()
    file_fixes = FILE_KEY_FIXES.get(relative_path, {})
    file_rules = FILE_KEY_RULES.get(relative_path, {})
    for line in path.read_text(encoding="utf-8").splitlines(keepends=True):
        if "=" in line and not line.lstrip().startswith("#"):
            k, v = line.split("=", 1)
            nv = fix_value(v, stat, GT_ONLY_RULES if is_gt else ())
            if is_gt:
                key = k.strip().removeprefix("S:").strip('"')
                if key in KEY_FIXES and v.rstrip("\n") != KEY_FIXES[key]:
                    nv = KEY_FIXES[key] + ("\n" if v.endswith("\n") else "")
                    stat["key:" + key] += 1
            nv = fix_value(nv, stat, file_rules.get(k.strip(), ()))
            if k.strip() in file_fixes:
                nv = file_fixes[k.strip()] + ("\n" if v.endswith("\n") else "")
                if nv != v:
                    stat["key:" + k.strip()] += 1
            if nv != v:
                changed = True
            line = k + "=" + nv
        out.append(line)
    if changed:
        path.write_text("".join(out), encoding="utf-8")

root = pathlib.Path(sys.argv[1])
stat = collections.Counter()
for p in list(root.glob("*.lang")) + list(root.glob("config/**/*.lang")):
    process(p, stat)
for k, n in stat.most_common():
    print(f"{k}: {n}")
