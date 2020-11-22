#  2020   21：24
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from Novel.items import NovelItem

'''


全本小说（CrawlSpider）
https://www.quanben.net/modules/article/articlelist.php?fullflag=1&page=1
爬取小说名称，url，类别，作者，更新时间，状态

未进入详情页面提取
'''
class NovelSpider(CrawlSpider):
    name = 'novel'
    #  不加http  或者  https
    allowed_domains = ['quanben.net']
    start_urls = ['https://www.quanben.net/list/1_1.html']

    print('3')

    # 翻页链接的提取规则
    #   刚开始 class='next' 忘加引号了  一直没看出来
    page_link = LinkExtractor(restrict_xpaths=('//a[@class="next"]',))
    # page_link = LinkExtractor(restrict_xpaths=('//div[@id="pagelink"]/a[text()="下一页"]',))
    # 帖子的详情链接的提取规则
    # content_link = LinkExtractor(restrict_xpaths=('//span[@class="s2"]/a'))
    #
    # # 定义规则，实现提取连接后，继续爬取。1.提取连接的特征， 2. 对象交给谁来处理
    rules = [  # process_links  回调函数
        Rule(page_link, callback="deal_page", follow=True),
        #  提取内容，这么重要。可不能出错。
        # Rule(content_link, callback="item_parse"),
    ]
    #


    # # def deal_link(self, links):
    # #     for link in links:
    # #         print('page:',link)
    # #     return links
    #
    # # 爬取小说名称，url，类别，作者，更新时间，状态
    def deal_page(self, link):
        print(1243455)
        item = NovelItem()
        # ls = links.xpath('//ul[@class="item-con]//li')
        ls = link.xpath('//ul[@class="item-con"]//li')
        # ls = links.xpath('//*[@id="content"]/div/div[2]/ul//li')
        print('len:',len(ls))
        # print(ls)
        for link in ls:
            item['name'] = link.xpath('.//span[@class="s2"]/a/text()').extract()[0]
            print('name:',item['name'])
            item['url'] = 'https://www.quanben.ne'+link.xpath('.//span[@class="s2"]/a/@href').extract()[0]
            print('url:',item['url'])
            item['type']= link.xpath('.//span[@class="s1"]/text()').extract()[0]
            print('type:', item['type'])
            item['author'] = link.xpath('.//span[@class="s3"]/text()').extract()[0]
            print('author:', item['type'])
            item['pub_date'] = link.xpath('.//span[@class="s4"]/text()').extract()[0]
            print('pub_date:', item['pub_date'])
            item['statue'] = link.xpath('.//span[@class="s5"]/text()').extract()[0]
            print('statue:', item['statue'])

            yield item

        return link

#
#
#
# class NovelsSpider(CrawlSpider):
#     name = 'novel'
#     allowed_domains = ['www.quanben.net']
#     start_urls = ['https://www.quanben.net/modules/article/articlelist.php?fullflag=1&page=1']
#     start_urls = ['https://www.quanben.net/list/1_1.html']
#
    # next_page = LinkExtractor(restrict_xpaths=("//a[@class='next']",))
    # detail = LinkExtractor(restrict_xpaths=('//ul[@class="item-con"]//li',))
    #
    # rules = [
    #     Rule(next_page, callback="deal_page", follow=True),
    #     # Rule(detail, callback="parse_item"),
    # ]

    #
    # def deal_page(self, links):
    #     item = NovelItem()
    #     ls_list = links.xpath('//ul[@class="item-con"]//li')
    #     for ls in ls_list:
    #         """
    #             name = scrapy.Field()
    #             novel_url = scrapy.Field()
    #             sort = scrapy.Field()
    #             author = scrapy.Field()
    #             update_time = scrapy.Field()
    #             state = scrapy.Field()
    #         """
    #         item["name"] = ls.xpath('.//span[@class="s2"]/a/text()').extract()[0]
    #         item["novel_url"] ='https://www.quanben.net/'+ ls.xpath('.//span[@class="s2"]/a/@href').extract()[0]
    #         item["sort"] = ls.xpath('.//span[@class="s1"]/text()').extract()[0]
    #         item["author"] = ls.xpath('.//span[@class="s3"]/text()').extract()[0]
    #         item["update_time"] = ls.xpath('.//span[@class="s4"]/text()').extract()[0]
    #         item["state"] = ls.xpath('.//span[@class="s5"]/text()').extract()[0]
    #
    #         print(item["name"])
    #         print(item["novel_url"])
    #         print(item["sort"])
    #         print(item["author"])
    #         print(item["update_time"])
    #         print(item["state"])
    #         print("=" * 100)
    #     return links


'''
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from 爬虫.day09_scrapy.workhome.Novel.Novel.items import NovelItem


class NovelsSpider(CrawlSpider):
    name = 'novel'
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
        item = NovelItem()
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
            # item["state"] = ls.xpath('.//span[@class="s5"]/text()').extract()[0]

            print(item["name"])
            print(item["novel_url"])
            # print(item["sort"])
            print(item["author"])
            print(item["update_time"])
            # print(item["state"])
            print("=" * 100)
        return links
'''

