# -*- coding: utf-8 -*-
'''
CrawlSpider实现自动爬取
'''
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from SunSpider.items import SunspiderItem


class Sun3Spider(CrawlSpider):
    name = 'Sun3'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']

    # 翻页链接的提取规则
    page_link = LinkExtractor(restrict_xpaths=('//div[@class="pagination"]/a[text()=">"]',))
    # 帖子的详情链接的提取规则
    content_link = LinkExtractor(restrict_xpaths=('//a[@class="news14"]'))


    # 定义规则，实现提取连接后，继续爬取。1.提取连接的特征， 2. 对象交给谁来处理
    rules = [
        Rule(page_link,process_links="deal_link",follow=True),
        Rule(content_link,callback="parse_item"),
    ]

    def deal_link(self,links):
        for link in links:
            print('link:',link.url)
        return links

#  从详情页面 提取数据
    def parse_item(self, response):
        item = SunspiderItem()
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
