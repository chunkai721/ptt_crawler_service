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
        # Handle the over 18 age check
        if "over18" in response.url:
            yield scrapy.FormRequest.from_response(
                response,
                formdata={'yes': 'yes'},
                callback=self.parse
            )
            return

        for post in response.css('.r-ent'):
            title = post.css('.title a::text').get()
            if any(keyword in title for keyword in self.keywords):
                yield {
                    'title': title,
                    'link': post.css('.title a::attr(href)').get(),
                    'date': post.css('.date::text').get(),
                    'author': post.css('.author::text').get()
                }

        next_pages = response.css('.btn-group-paging a::attr(href)').getall()
        if next_pages and len(next_pages) > 1:
            next_page = next_pages[1]
            yield response.follow(next_page, self.parse)
