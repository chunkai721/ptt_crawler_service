# ptt_crawler_service

這是一個專為台灣的PTT設計的爬蟲服務，可以通過LINE進行操作和配置，包括選擇板塊和追踪關鍵字。

## 目錄結構

.
├── .gitattributes
├── requirements.txt
├── docs
│ ├── api_spec_and_tasks.md
│ ├── prd.md
│ └── system_design.md
├── ptt_crawler_service
│ ├── config.py
│ ├── crawler.py
│ ├── database.py
│ ├── line_interface.py
│ └── main.py
└── resources


## 說明文件

### 1. api_spec_and_tasks.md
- 該文件列出了所需的Python第三方套件，如`scrapy`, `line-bot-sdk`和`sqlite3`。
- 定義了完整的API規範，包括開始和停止爬蟲服務的路徑。
- 提供了邏輯分析，描述了每個主要文件的功能。
- 列出了待完成的任務列表。

### 2. prd.md
- 描述了原始需求，產品目標和用戶故事。
- 進行了競爭分析，比較了不同的爬蟲工具。
- 定義了產品需求和UI設計草圖。

### 3. system_design.md
- 描述了實施方法，使用的技術和工具。
- 列出了主要的文件和數據結構。
- 提供了程序調用流程圖。

### 4. config.py
- 包含了應用程序的配置變量，如LINE bot API鍵，SQLite數據庫路徑，PTT板和關鍵字設置。

### 5. crawler.py
- 包含了爬蟲類，負責從PTT抓取數據。

### 6. database.py
- 包含了數據庫類，負責存儲和檢索數據。

### 7. line_interface.py
- 包含了LineInterface類，負責通過LINE發送和接收消息。

### 8. main.py
- 包含了應用程序的主入口點，初始化Crawler、LineInterface和Database對象，並處理開始和停止命令。

### 9. requirements.txt
- 列出了項目所需的所有Python套件。

