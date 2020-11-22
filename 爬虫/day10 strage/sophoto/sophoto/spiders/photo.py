import scrapy
from scrapy.linkextractors import  LinkExtractor
from scrapy.spiders import Rule
from scrapy.utils import spider
from sophoto.items import SophotoItem
from scrapy.spiders import CrawlSpider
class PhotoSpider(CrawlSpider):
    name = 'photo'
    allowed_domains = ['photophoto.cn']
    start_urls = ['https://www.photophoto.cn/tag/%E6%B5%B7%E6%8A%A5/1-0-0-0-0-2-0-1.html']

    #  提取下一页
    next_page =LinkExtractor(restrict_xpaths=("//a[@class='pagenext']",))
    #  提取详情页
    # content_page = LinkExtractor(restrict_xpaths=('//div[@class="image"]/a'))

    rules = [
        # Rule(next_page,follow=True,callback='item_parse'),
        Rule(next_page,process_links='deal_link',follow=True,callback='item_parse'),
        # Rule(content_page,callback='item_parse'),
    ]

    # 提取下一页

    def deal_link(self, links):
        for link in links:
            print('link:',link.url)
        return links


    def item_parse(self, response):
        item = SophotoItem()
        li = response.xpath('//ul[@id="list"]//li')
        print(len(li))
        # li = response.xpath('/div[@id="list"]//li')
        for i in li:
            item['name'] = i.xpath('.//div[@class="image"]/a/@title').extract()[0]
            print('name:',item["name"])
            item['src'] = i.xpath('.//div[@class="image"]/a/img/@src').extract()[0]
            print('src:', item["src"])
            # item['url'] = i.xpath('//div[@class="image"]/a/@href').extract()
            # print('url:', item["url"])

            yield item




