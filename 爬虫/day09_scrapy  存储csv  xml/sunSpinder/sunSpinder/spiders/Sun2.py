from random import random
from time import sleep

import scrapy

from sunSpinder.items import SunspinderItem


class Sun2Spider(scrapy.Spider):
    name = 'Sun2'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest']

    def __init__(self):
        self.offset = 1

    def parse(self, response):
        # ls = response.xpath('//div[class="public-content"]/div[3]/ul[2]/li/span[3]/a')
        ls = response.xpath('//div[@class="width-12"]/ul[2]/li')
        #  css  空格 表示 子标签
        # ls = response.css('ul.title-state-ul li a')
        print('1:', len(ls))
        item = SunspinderItem()
        for  it in ls:
            item['title']=response.xpath('./span[3]/text()').extract()[0]
            print(item['title'])
            detail_url = response.xpath('./span[3]/@href').extract()[0]
            item['detail_url'] = 'http://wz.sun0769.com' + detail_url
            item['number'] = response.xpath('./pan[1]/text()').extract()[0]
            item['pub_time'] = response.xpath('./span[5]/text()').extract()[0]

            req = scrapy.Request(item['detail_url'],callback=self.item_parse)
            req['item'] = item
            yield  req


        url = 'http://wz.sun0769.com/political/index/politicsNewest?id=1&page='
        if self.offset <= 10:
            self.offset += 1
            #  不加括号
            # print('new_url:',self.url)
            #  将提取到的链接 进行拼接，，再次发送请求
            yield scrapy.Request(url + str(self.offset), callback=self.parse)
            print('new_url:', url + str(self.offset))
            sleep(random())

    def item_parse(self,response):
        item = response.meta['item']
        item['author'] = response.xpath('//div[@class="focus-date clear focus-date-list"]/span/text()').extract()[0]
        item['content'] = response.xpath('//div[@class = "details-box"]/pre/text()').extract()[0]



        # http://wz.sun0769.com/political/index/politicsNewest?id=1&page=2