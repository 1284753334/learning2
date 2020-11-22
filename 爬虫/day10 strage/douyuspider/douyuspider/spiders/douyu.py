import json

import scrapy

from douyuspider.items import DouyuspiderItem

#
class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['capi.douyucdn.cn']
    start_urls = ['http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset=']


    def __init__(self):
        self.offset = 0
        self.url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='

    def parse(self, response):

        data = json.loads(response.text)['data']
        for each in data:
            item = DouyuspiderItem()
            item['nickname'] = each['nickname']
            item['image_url'] = each['vertical_src']
            yield item

        # 翻页

        self.offset += 20
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)

