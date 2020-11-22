from random import random
from time import sleep

import scrapy
from scrapy_redis.spiders import RedisSpider

from sunSpinder.items import SunspinderItem
'''
lpush Sun5:start_urls http://wz.sun0769.com/political/index/politicsNewest
'''

class Sun5Spider(RedisSpider):
    name = 'Sun5'
    redis_key = 'Sun5:start_urls'
    # allowed_domains = ['sun0769.com']
    # start_urls = ['http://wz.sun0769.com/political/index/politicsNewest']

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(Sun5Spider, self).__init__(*args, **kwargs)
        # self.url = 'http://wz.sun0769.com/political/index/politicsNewest?id=1&page=1'
        self.offset = 1

        #  提取信息

    def parse(self, response):
        # 直接获取a的链接  提取链接 发生变化了
        li = response.xpath("//li[@class = 'clear']/span[3]/a/@href").extract()
        # li = response.xpath('//div[@class="width-12"]/ul[2]//li/a/@href').extract()[0]
        # print(li)
        ls = 'http://wz.sun0769.com'
        # print(ls)
        for link in ls:
            #  再次发起新的 请求 详情解析页面
            yield scrapy.Request(ls + link, self.item_parse)

        #          翻页设置
        url = 'http://wz.sun0769.com/political/index/politicsNewest?id=1&page='
        if self.offset <= 10:
            self.offset += 1
            #  不加括号
            # print('new_url:',self.url)
            #  将提取到的链接 进行拼接，，再次发送请求
            yield scrapy.Request(url + str(self.offset), callback=self.parse)
            print('new_url:', url + str(self.offset))

            sleep(random())

        # 进入详情页进行解析

    def item_parse(self, response):
        #   初始化 存储对象  extract() 序列化 得到一个列表
        item = SunspinderItem()
        item['title'] = response.xpath('//p[@class="focus-details"]').extract()[0]
        # item['title'] = response.xpath('//div[@class = "mr-three"]/p/text()').extract()[0]
        print(item['title'])
        item['detail_url'] = response.url
        print(item['detail_url'])
        item['pub_time'] = response.xpath('//div[@class="focus-date clear focus-date-list"]/span[2]/text()').extract()[0]
        item['number'] = response.xpath('//div[@class="focus-date clear focus-date-list"]/span[4]/text()').extract()[0].split(':')[-1]
        item['author'] =response.xpath('//div[@class="focus-date clear focus-date-list"]/span[1]/text()').extract()[0]
        item['content'] = response.xpath('//div[@class="details-box"]/pre/text()').extract()[0]
        #  提交给上面定义的 item
        yield item
        # sleep(random())

    # http://wz.sun0769.com/political/index/politicsNewest?id=1&page=2