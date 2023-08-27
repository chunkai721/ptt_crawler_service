from typing import List

class Config:
    def __init__(self,
                 line_bot_api_key: str = "YOUR_LINE_BOT_API_KEY",
                 line_user_id: str = "YOUR_LINE_USER_ID",  # 新增的 line_user_id 屬性
                 sqlite_db_path: str = "sqlite_db.db",
                 ptt_board: str = "Gossiping",
                 ptt_keywords: List[str] = None):
        self.line_bot_api_key = line_bot_api_key
        self.line_user_id = line_user_id  # 初始化 line_user_id 屬性
        self.sqlite_db_path = sqlite_db_path
        self.ptt_board = ptt_board
        self.ptt_keywords = ptt_keywords if ptt_keywords is not None else []

    def update_keywords(self, new_keywords: List[str]):
        self.ptt_keywords = new_keywords
