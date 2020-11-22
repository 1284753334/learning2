from random import random
from time import sleep

import scrapy

from sunSpinder.items import SunspinderItem

#  scrapy 提取文字 链接，使用 extract()[0]
class Sun1Spinder(scrapy.Spider):
    name = 'Sun1'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest?id=1&page=1']


    def  __init__(self):
        self.url = 'http://wz.sun0769.com/political/index/politicsNewest?id=1&page=1'
        self.offset = 1

    #  提取信息
    def parse(self, response):
        # 直接获取所有 50个   a的链接  提取链接 发生变化了
        li = response.xpath("//li[@class = 'clear']/span[3]/a/@href").extract()
        # li = response.xpath('//div[@class="width-12"]/ul[2]//li/a/@href').extract()[0]
        # print(li)
        ls = 'http://wz.sun0769.com'
        # print(ls)
        for link in li:
            #  再次发起新的 请求 详情解析页面
            yield scrapy.Request(ls+link,callback=self.item_parse)

    #          翻页设置
        url = 'http://wz.sun0769.com/political/index/politicsNewest?id=1&page='
        if self.offset <= 10:
            self.offset +=1
            #  不加括号
            # print('new_url:',self.url)
            #  将提取到的链接 进行拼接，，再次发送请求
            yield scrapy.Request(url +str(self.offset),callback=self.parse)
            print('new_url:',url +str(self.offset))

            sleep(random())



    # 进入详情页进行解析
    def item_parse(self,response):
        #   初始化 存储对象  extract() 序列化 得到一个列表
        print('123245')
        item =SunspinderItem()

        # item['title'] = response.css('p.focus-details')
        item['title'] = response.xpath('//p[@class="focus-details"]/text()').extract()[0]
        # item['title'] = response.xpath('//div[@class = "mr-three"]/p/text()').extract()[0]
        print(item['title'])
        item['detail_url'] = response.url
        print('url:',item['detail_url'])
        item['pub_time'] = response.xpath('//div[@class="focus-date clear focus-date-list"]/span[2]/text()').extract()[0]
        print('pub_time:',item['pub_time'])
        item['number'] = response.xpath('//div[@class="focus-date clear focus-date-list"]/span[4]/text()').extract()[0].split('：')[-1]
        print('number:',item['number'])
        item['author'] = response.xpath('//div[@class="focus-date clear focus-date-list"]/span[1]/text()').extract()[1].strip()
        # print('author:',item['author'])
        # item['author'] = response.xpath('//span[@class="fl details-head"]//text()').extract()[1].strip()
        print('author2:',item['author'])
        item['content'] = response.xpath('//div[@class="details-box"]/pre/text()').extract()[0]
        print('content:',item['content'])
        #  提交给上面定义的 item


        sleep(random())
