# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from SinaBlog.items import SinablogItem


class SinaSpider(CrawlSpider):
    name = 'sina'
    allowed_domains = ['blog.sina.com.cn']
    start_urls = ['http://blog.sina.com.cn/s/articlelist_1525875683_0_1.html']

    # 翻页链接的提取规则
    page_link = LinkExtractor(restrict_xpaths=("//li[@class='SG_pgnext']/a",))
    # 帖子链接地址的提取
    content_url = LinkExtractor(restrict_xpaths=('//span[@class="atc_title"]/a',))
    rules = [
        Rule(page_link, process_links="deal_link", follow=True),
        Rule(content_url, callback="parse_item"),
    ]

    def deal_link(self, links):
        for link in links:
            print("link:", link)
        return links

    def parse_item(self, response):
        item = SinablogItem()
        temp1 = response.xpath('//h2[@class="titName SG_txta"]/text()').extract()
        temp2 = response.xpath('//h1[@class="h1_tit"]/text()').extract()
        if len(temp1) == 0:
            item["title"] = temp2[0]
        if len(temp2) == 0:
            item["title"] = temp1[0]
        print(item["title"])
        item["detail_url"] = response.url
        print(item["detail_url"])
        print("=" * 100)
        yield item
