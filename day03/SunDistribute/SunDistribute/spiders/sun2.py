import random
import time

import scrapy
from scrapy_redis.spiders import RedisSpider

from day03.SunDistribute.SunDistribute.items import SundistributeItem


class Sun2Spider(RedisSpider):
    name = 'sun2'
    # allowed_domains = ['wz.sun0769.com']
    # start_urls = ['http://wz.sun0769.com/']
    redis_key = 'sun2:start_urls'

    def __init__(self,*args,**kwargs):
        domain = kwargs.pop('domain','')
        self.allowed_domains = filter(None,domain.split(","))
        super(Sun2Spider, self).__init__(*args,**kwargs)
        self.url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='
        self.offset = 0

    def parse(self, response):
        # 提取页面中所有投诉帖子的链接
        ls = response.xpath('//a[@class="news14"]/@href').extract()
        print('len:', len(ls))
        for link in ls:
            yield scrapy.Request(link, self.parse_item)  # 请求帖子详情页面
            time.sleep(random.random())

        # 翻页，设置翻页条件
        if self.offset <= 8000:
            self.offset += 30
            print('next page url:', self.url + str(self.offset))
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
            time.sleep(random.random())



    def parse_item(self,response):
        item = SundistributeItem()
        # 标题
        item['title'] = response.xpath('//div[@class="wzy1"]/table[1]//td[2]/span[1]/text()').extract()[0]
        # URL
        item['detail_url'] = response.url
        # 编号
        item['number'] = response.xpath('//div[@class="wzy1"]/table[1]//td[2]/span[2]/text()').extract()[0].split(':')[-1]
        # 内容
        item['content'] = response.xpath('//div[@class="wzy1"]/table[2]//tr[1]/td[@class="txt16_3"]//text()').extract()
        item['content'] = ''.join(item['content']).strip()
        # 作者
        temp = response.xpath('//div[@class="wzy3_2"]/span/text()').extract()[0].strip()
        temp = temp.split(' ')
        item['author'] = temp[0].split('：')[-1]
        # 投诉时间
        item['pub_date'] = temp[1].split('：')[-1]+ ' '+ temp[2]
        yield item

