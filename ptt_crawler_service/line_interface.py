## line_interface.py
from linebot import LineBotApi
from linebot.models import TextSendMessage
from typing import Optional
from config import Config

class LineInterface:
    def __init__(self, user_id: str, api_key: Optional[str] = None):
        self.user_id = user_id
        self.api_key = api_key if api_key is not None else Config().line_bot_api_key
        self.line_bot_api = LineBotApi(self.api_key)

    def send_message(self, message: str):
        self.line_bot_api.push_message(self.user_id, TextSendMessage(text=message))

    def receive_message(self, message: str):
        # This function should be implemented based on the actual LINE Messaging API webhook setup.
        # Here we just print the received message for simplicity.
        print(f"Received message: {message}")
