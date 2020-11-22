

import json

import scrapy

from douyuspider.items import DouyuspiderItem




class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['http://capi.douyucdn.cn']
    #  limit  是下载的值
    start_urls = ['http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset=']

    #  定义一些属性
    def  __init__(self):
        self.offset = 0
        #  定义属性，后面拼接offset
        self.url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='



    def parse(self, response):
        #  获取网页源码
        data = json.loads(response.text)['data']
        '''
        name = scrapy.Field()  # 存储照片的名字
        imagesUrls = scrapy.Field()  # 照片的 url 路径
        '''
        for  each in data:
            item = DouyuspiderItem()
            item['nickname'] = each['nickname']
            item['imagesUrls'] = each['vertical_src']
            yield item
#       翻页
        self.offset +=20
        yield scrapy.Request(self.url+str(self.offset),callback=self.parse)



