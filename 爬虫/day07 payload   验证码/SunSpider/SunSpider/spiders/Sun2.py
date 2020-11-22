# -*- coding: utf-8 -*-

'''
分两个页面提取的信息


包持一致，，携带一个 演示了  meta 的 用法；
'''

import scrapy
from SunSpider.items import SunspiderItem
import random
import time


class Sun2Spider(scrapy.Spider):
    name = 'Sun2'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']


    def __init__(self):
        self.url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='
        self.offset = 0


    def parse(self, response):
        ls = response.xpath('//div[@class="greyframe"]/table[2]//table//tr')
        print('len:',len(ls))
        for each in ls:
            item = SunspiderItem()
            item['title'] = each.xpath('./td[2]/a[2]/text()').extract()[0]
            item['detail_url'] = each.xpath('./td[2]/a[2]/@href').extract()[0]
            item['number'] = each.xpath('./td[1]/text()').extract()[0]
            item['author'] = each.xpath('./td[4]/text()').extract()[0]
            item['pub_date'] = each.xpath('./td[5]/text()').extract()[0]
            # 请求对象
            req = scrapy.Request(item['detail_url'],callback=self.parse_item)
            #  携带信息  将第一次爬取的信息 放到 meta中，再二次请求中，再拿出来
            req.meta['item'] = item
            yield req
            time.sleep(random.random())

        # 翻页，设置翻页条件
        if self.offset <= 8000:
            self.offset += 30
            print('next page url:', self.url + str(self.offset))
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
            time.sleep(random.random())

    def parse_item(self,response):
        item = response.meta['item']
        # 内容
        item['content'] = response.xpath('//div[@class="wzy1"]/table[2]//tr[1]/td[@class="txt16_3"]//text()').extract()
        item['content'] = ''.join(item['content']).strip()
        #
        yield item