from random import random
from time import sleep

import scrapy
from  scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from SunDistribute.items import SundistributeItem
#
# class Sun1Spider(CrawlSpider):
#     name = 'sun1'
#     allowed_domains = ['sun0769.com']
#     start_urls = ['http://wz.sun0769.com/political/index/politicsNewest?id=1&page=1']

class Sun1Spider(CrawlSpider):
    name = 'sun1'
    allowed_domains = ['sun0769.com']
    #  入口函数
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest']
    #
    # def  __init__(self):
    #     self.offset = 1

    # 翻页链接的提取规则
    page_link = LinkExtractor(restrict_xpaths=('//div[@class="mr-three paging-box"]/a[@class="arrow-page prov_rota"]',))
    # 帖子的详情链接的提取规则
    content_link = LinkExtractor(restrict_xpaths=('//a[@class="color-hover"]'))

    # 定义规则，实现提取连接后，继续爬取。1.提取连接的特征， 2. 对象交给谁来处理
    rules = [  # process_links  回调函数
        Rule(page_link, process_links="deal_link", follow=True),
        #  提取内容，这么重要。可不能出错。
        Rule(content_link, callback="item_parse"),
    ]

    # 这个写不写都可以的
    def deal_link(self, links):
        for link in links:
            print('link:', link.url)
        return links

    def item_parse(self, response):
        #   初始化 存储对象  extract() 序列化 得到一个列表
        item =  SundistributeItem()
        item['title'] = response.xpath('//p[@class="focus-details"]').extract()[0]
        item['title'] = response.xpath('//div[@class = "mr-three"]/p/text()').extract()[0]
        # print(item['title'])
        item['detail_url'] = response.url
        # print(item['detail_url'])
        item['pub_time'] = response.xpath('//div[@class="focus-date clear focus-date-list"]/span[2]/text()').extract()[0]
        item['number'] =response.xpath('//div[@class="focus-date clear focus-date-list"]/span[4]/text()').extract()[0].split('：')[-1]
        # item['author'] = response.xpath('//div[@class="focus-date clear focus-date-list"]/span[1]/text()').extract()[0].strip()
        item['author'] = response.xpath('//span[@class="fl details-head"]//text()').extract()[1].strip()
        item['content'] = response.xpath('//div[@class="details-box"]/pre/text()').extract()[0]
        #  提交给上面定义的 item
        #  不用print 内容，，日志会提示出来的
        yield item
        # sleep(random())