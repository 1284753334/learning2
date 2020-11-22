# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from blogCrawlSpider.items import BlogcrawlspiderItem

class Sinablog1Spider(CrawlSpider):
    name = 'SinaBlog1'
    allowed_domains = ['blog.sina.com.cn']
    start_urls = ['http://blog.sina.com.cn/s/blog_5af303e30102yff6.html']

    # 定义翻页的规则  re  相对简单一点
    rules = [
        #  进入文章详情，获取上一页，下一页的  连接
        # Rule(LinkExtractor(restrict_xpaths=('//div[@class="articalfrontback SG_j_linedot1 clearfix"]/div/a',)),callback='parse_item',follow=True)
        # Rule(LinkExtractor(restrict_css=('div.articalfrontback.SG_j_linedot1.clearfix > div > a',)),callback='parse_item', follow=True)
        # re  匹配的是 地址栏的  url
        # Rule(LinkExtractor(allow=(r'http://blog.sina.com.cn/s/blog_.*?\.html',)),callback='parse_item', follow=True)
        Rule(LinkExtractor(allow=(r'/s/blog_.*?\.html',)), callback='parse_item', follow=True)

    # //div[@class='articalTitle']/h2/text()
    # 标题
    #     //h2[@class='titName SG_txta']/text()

    ]

    def parse_item(self, response):
        item = BlogcrawlspiderItem()
        item['blog_url'] = response.url
        # 有可能返回的为空   下面加判断
        title = response.xpath('//h2[@class="titName SG_txta"]/text()').extract()
        if len(title)>0:
            title = title[0]
        else:
            title = '空'
        item['title'] = title
        content = response.xpath('//div[@id="sina_keyword_ad_area2"]//text()').extract()
        #   结果为列表
        # content = response.xpath('//div[@id="sina_keyword_ad_area"]//text()').extract()
        # content = response.xpath('//div[@id="sina_keyword_ad_area2"]//text()').extract()
        if len(content)>0:
            content = ''.join(content).strip()
        else:
            content = '空'
        item['content'] = content
        yield item

