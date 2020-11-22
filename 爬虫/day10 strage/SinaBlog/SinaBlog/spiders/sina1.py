# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from SinaBlog.items import SinablogItem
from scrapy.utils import spider

'''
进入列表页  遍历提取  然后   翻页

spider.Spider  不会翻页  提取的是当前页

 CrawlSpider 会自动翻页，提取的是 下一页
'''
class SinaSpider( CrawlSpider):
    name = 'sina1'
    allowed_domains = ['blog.sina.com.cn']
    start_urls = ['http://blog.sina.com.cn/s/articlelist_1525875683_0_1.html']

    # 翻页链接的提取规则
    page_link = LinkExtractor(restrict_xpaths=("//li[@class='SG_pgnext']/a",))
    # 帖子链接地址的提取
    # content_url = LinkExtractor(restrict_xpaths=('//span[@class="atc_title"]/a',))
    #
    rules = [
        # Rule(page_link, process_links="deal_link", follow=True,callback="parse_item"),
        Rule(page_link, follow=True,callback="parse_item"),
        # Rule(content_url, callback="parse_item"),
    ]

    # def deal_link(self, links):
    #     for link in links:
    #         print("link:", link)
    #     return links
    def parse(self, response):
        item = SinablogItem()
        ls = response.xpath('//div[@class="articleCell SG_j_linedot1"]')
        for itm in ls:
            item['title'] = itm.xpath('.//span[2]/a/text()').extract()[0]
            print(item['title'])
            item['detail_url'] = itm.xpath('.//span[2]/a/@href').extract()[0]
            page_url = response.url
            print('page:', page_url)
            print(item['detail_url'])
            #  存储的保证
            yield item


    def parse_item(self, response):
        item = SinablogItem()
        # temp1 = response.xpath('//h2[@class="titName SG_txta"]/text()').extract()
        # temp2 = response.xpath('//h1[@class="h1_tit"]/text()').extract()
        # if len(temp1) == 0:
        #     item["title"] = temp2[0]
        # if len(temp2) == 0:
        #     item["title"] = temp1[0]
        # print(item["title"])
        # item["detail_url"] = response.url
        # print(item["detail_url"])
        # print("=" * 100)
        # yield item

#         2
        ls=response.xpath('//div[@class="articleCell SG_j_linedot1"]')
        for itm in ls:
            item['title'] = itm.xpath('.//span[2]/a/text()').extract()[0]
            print(item['title'])
            item['detail_url'] = itm.xpath('.//span[2]/a/@href').extract()[0]
            page_url = response.url
            print('page:',page_url)
            print(item['detail_url'])
            yield  item



