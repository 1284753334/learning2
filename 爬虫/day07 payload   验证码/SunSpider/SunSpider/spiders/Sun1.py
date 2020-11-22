# -*- coding: utf-8 -*-
import scrapy
from SunSpider.items import SunspiderItem
import random
import time


class Sun1Spider(scrapy.Spider):
    name = 'Sun1'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']


    def __init__(self):
        self.url = 'http://wz.sun0769.com/political/index/politicsNewest?id=1&page=1'
        self.offset = 0


    def parse(self, response):
        # 提取页面中所有投诉帖子的链接
        li = response.xpath("//li[@class = 'clear']/span[3]/a/@href").extract()[0]
        ls = 'http://wz.sun0769.com' + li
        # ls = response.xpath('//a[@class="news14"]/@href').extract()
        print('len:',len(ls))
        for link in ls:
            yield scrapy.Request(link,self.parse_item)  # 请求帖子详情页面
            time.sleep(random.random())

        # 翻页，设置翻页条件
        if self.offset <= 8000:
            self.offset += 30
            print('next page url:',self.url + str(self.offset))
            yield scrapy.Request(self.url + str(self.offset),callback=self.parse)
            time.sleep(random.random())


    def parse_item(self,response):
        item = SunspiderItem()
        # 标题
        # item['title'] = response.xpath('//div[@class="wzy1"]/table[1]//td[2]/span[1]/text()').extract()[0]
        # # URL
        # item['detail_url'] = response.url
        # # 编号
        # item['number'] = response.xpath('//div[@class="wzy1"]/table[1]//td[2]/span[2]/text()').extract()[0].split(':')[-1]
        # # 内容
        # item['content'] = response.xpath('//div[@class="wzy1"]/table[2]//tr[1]/td[@class="txt16_3"]//text()').extract()
        # item['content'] = ''.join(item['content']).strip()
        # # 作者
        # temp = response.xpath('//div[@class="wzy3_2"]/span/text()').extract()[0].strip()
        # temp = temp.split(' ')
        # item['author'] = temp[0].split('：')[-1]
        # # 投诉时间
        # item['pub_date'] = temp[1].split('：')[-1]+ ' '+ temp[2]
        item['title'] = response.xpath('//p[@class="focus-details"]')
        item['detail_url'] = response.url
        item['pub_time'] = response.xpath('//div[@class="focus-date clear focus-date-list"]/span[2]/text()').extract()
        item['number'] = response.xpath('//div[@class="focus-date clear focus-date-list"]/span[4]/text()').extract()[0].split(':')[-1]
        item['author'] = response.xpath('//div[@class="focus-date clear focus-date-list"]/span[1]/text()').extract()[0]
        item['content'] = response.xpath('//div[@class="details-box"]/pre/text()').extract()[0]
        yield item

