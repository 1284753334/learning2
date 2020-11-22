# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from quanben.items import QuanbenItem


class NovelsSpider(CrawlSpider):
    name = 'novels'
    allowed_domains = ['www.quanben.net']
    # start_urls = ['https://www.quanben.net/modules/article/articlelist.php?fullflag=1&page=1']
    start_urls = ['https://www.quanben.net/list/1_1.html']

    next_page = LinkExtractor(restrict_xpaths=("//a[@class='next']",))
    # detail = LinkExtractor(restrict_xpaths=('//ul[@class="item-con"]//li',))

    rules = [
        Rule(next_page, callback="deal_page", follow=True),
        # Rule(detail, callback="parse_item"),
    ]

    def deal_page(self, links):
        item = QuanbenItem()
        ls_list = links.xpath('//ul[@class="item-con"]//li')
        for ls in ls_list:
            """
                name = scrapy.Field()
                novel_url = scrapy.Field()
                sort = scrapy.Field()
                author = scrapy.Field()
                update_time = scrapy.Field()
                state = scrapy.Field()
            """
            item["name"] = ls.xpath('.//span[@class="s2"]/a/text()').extract()[0]
            item["novel_url"] = ls.xpath('.//span[@class="s2"]/a/@href').extract()[0]
            # item["sort"] = ls.xpath('.//span[@class="s1"]/text()').extract()[0]
            item["author"] = ls.xpath('.//span[@class="s3"]/text()').extract()[0]
            item["update_time"] = ls.xpath('.//span[@class="s4"]/text()').extract()[0]
            item["state"] = ls.xpath('.//span[@class="s5"]/text()').extract()[0]

            print(item["name"])
            print(item["novel_url"])
            # print(item["sort"])
            print(item["author"])
            print(item["update_time"])
            print(item["state"])
            print("=" * 100)
        return links
