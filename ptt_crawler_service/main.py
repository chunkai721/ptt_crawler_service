from crawler import PttSpider
from line_interface import LineInterface
from database import Database
from config import Config
from scrapy.crawler import CrawlerProcess

class Main:
    def __init__(self):
        self.config = Config()
        self.database = Database(self.config.sqlite_db_path)
        self.line_interface = LineInterface(self.config.line_user_id, self.config.line_bot_api_key)
        self.crawler_process = None

    def start_crawler(self):
        self.crawler_process = CrawlerProcess()
        self.crawler_process.crawl(PttSpider, self.config.ptt_keywords)
        self.crawler_process.start()

    def stop_crawler(self):
        if self.crawler_process:
            self.crawler_process.stop()

    def receive_message(self, message: str):
        self.line_interface.receive_message(message)

    def send_message(self, message: str):
        self.line_interface.send_message(message)

    def update_keywords(self, new_keywords: list):
        self.config.update_keywords(new_keywords)
        self.stop_crawler()
        self.start_crawler()

if __name__ == "__main__":
    main = Main()
    main.start_crawler()
