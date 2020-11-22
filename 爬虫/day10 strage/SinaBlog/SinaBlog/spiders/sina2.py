# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from SinaBlog.items import SinablogItem

'''
进入某一页进行爬取   翻页为前一页  后者 后一页  scrapy 会自动去重

, follow=True,,不添加  只能爬取两页，添加后 ，能爬取好多页
'''
class SinaSpider(CrawlSpider):
    name = 'sina2'
    allowed_domains = ['blog.sina.com.cn']
    start_urls = ['http://blog.sina.com.cn/s/blog_5af303e30102yj0s.html']

    # 翻页链接的提取规则
    #  没有反应 首先 重写 翻页的路径 xpath 表达式
    page_link = LinkExtractor(restrict_xpaths=("//div[@class='articalfrontback SG_j_linedot1 clearfix']/div/a",))
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

    def parse_item(self, response):
        item = SinablogItem()
        #  /text()  一定要加小括号
        item['title'] = response.xpath('//h2[@class = "titName SG_txta"]/text()').extract()
        if len(item['title']) > 0:
            item['title'] = item['title'][0]
        else :
            item['title'] = '空'
        print("item['title']:",item['title'])


        item['detail_url'] = response.url
        # item['content'] = response.xpath('.//div[@class="sina_keyword_ad_area2"]//p/text()')
        # 避免列表，，直接提取text()
        print('url:',item['detail_url'])
        #  id 还是 class  一定 要 看清楚 在写 写前 检查 一下
        item1 = response.xpath('//div[@class="articalContent   newfont_family"]//text()').extract()
        if len(item1) > 0:
            item1 = ''.join(item1)
        else :
            item1 = '空'
        print("item['content']", item1.strip())

        yield item





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

#  2  '''
# 进入某一页进行爬取   翻页为前一页  后者 后一页  scrapy 会自动去重
# '''
#         ls=response.xpath('//div[@class="articleCell SG_j_linedot1"]')
#         for itm in ls:
#             item['title'] = itm.xpath('.//span[2]/a/text()').extract()[0]
#             print(item['title'])
#             item['detail_url'] = itm.xpath('.//span[2]/a/@href').extract()[0]
#             page_url = response.url
#             print('page:',page_url)
#             print(item['detail_url'])

