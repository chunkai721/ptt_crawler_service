import scrapy
from typing import List
from config import Config

class PttSpider(scrapy.Spider):
    name = "ptt_spider"
    allowed_domains = ["ptt.cc"]
    start_urls = [f"https://www.ptt.cc/bbs/{Config().ptt_board}/index.html"]

    def __init__(self, keywords: List[str] = None):
        self.keywords = keywords if keywords is not None else Config().ptt_keywords

    def parse(self, response):
        for post in response.css('.r-ent'):
            title = post.css('.title a::text').get()
            if any(keyword in title for keyword in self.keywords):
                yield {
                    'title': title,
                    'link': post.css('.title a::attr(href)').get(),
                    'date': post.css('.date::text').get(),
                    'author': post.css('.author::text').get()
                }

        next_page = response.css('.btn-group-paging a::attr(href)').getall()[1]
        if next_page is not None:
            yield response.follow(next_page, self.parse)
