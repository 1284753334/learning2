# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from blogCrawlSpider.items import BlogcrawlspiderItem

class Sinablog2Spider(CrawlSpider):
    name = 'SinaBlog2'
    allowed_domains = ['blog.sina.com.cn']
    start_urls = ['http://blog.sina.com.cn/s/articlelist_1525875683_0_1.html']

    # 规则：匹配翻页
    page_link = LinkExtractor(restrict_xpaths=('//li[@class="SG_pgnext"]/a',))
    # 规则：匹配详情链接   子节点和父节点相同  可以采用

    # //div[@class=article_blk]/div[2]/div/span/a
    content_link = LinkExtractor(restrict_xpaths=('//span[@class="atc_title"]/a',))
    rules = [
        Rule(page_link,follow=True),
        Rule(content_link,callback='parse_item')
    ]

    def parse_item(self, response):
        item = BlogcrawlspiderItem()
        item['blog_url'] = response.url
        title = response.xpath('//h2[@class="titName SG_txta"]/text()').extract()
        if len(title) > 0:
            title = title[0]
        else:
            title = '空'
        item['title'] = title
        content = response.xpath('//div[@id="sina_keyword_ad_area2"]//text()').extract()
        if len(content) > 0:
            content = ''.join(content).strip()
        else:
            content = '空'
        item['content'] = content
        yield item
