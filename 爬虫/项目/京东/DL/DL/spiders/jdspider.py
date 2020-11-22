# import scrapy
#
#
# class JdspiderSpider(scrapy.Spider):
#     name = 'jdspider'
#     allowed_domains = ['jd.com']
#     start_urls = ['http://jd.com/']
#
#     def parse(self, response):
#         pass

# search.py
# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
import time
class SearchSpider(scrapy.Spider):
    name = 'search'
    search_page_url_pattern = "https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&page={page}&enc=utf-8"
    start_urls = ['https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8']

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        self.browser = webdriver.Chrome(chrome_options=chrome_options, executable_path='/usr/local/bin/chromedriver')
        super(SearchSpider, self).__init__()
    def closed(self,reason):
        self.browser.close()        # 记得关闭

    def parse(self, response):
        total_page = response.css('span.p-skip em b::text').extract_first()
        if total_page:
            for i in range(int(total_page)):
                next_page_url = self.search_page_url_pattern.format(page=2*i + 1)
                yield scrapy.Request(next_page_url, callback = self.parse_page)
                time.sleep(1)

    def parse_page(self, response):
        book_info_list = response.css('div.p-name a')
        for item in book_info_list:
            phone_name = item.css('a::attr(title)').extract_first()
            phone_href = item.css('a::attr(href)').extract_first()

            yield dict(name=phone_name, href=phone_href)
