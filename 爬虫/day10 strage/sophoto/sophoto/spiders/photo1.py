import scrapy
from scrapy.linkextractors import  LinkExtractor
from scrapy.spiders import Rule
from scrapy.utils import spider
from sophoto.items import SophotoItem
from scrapy.spiders import CrawlSpider
class PhotoSpider(spider.Spider):
    name = 'photo1'
    allowed_domains = ['photophoto.cn']
    start_urls = ['https://www.photophoto.cn/tag/%E6%B5%B7%E6%8A%A5/1-0-0-0-0-2-0-1.html']

    # #  提取下一页
    # next_page =LinkExtractor(restrict_xpaths=("//a[@class='pagenext']",))
    # #  提取详情页
    # # content_page = LinkExtractor(restrict_xpaths=('//div[@class="image"]/a'))
    #
    # rules = [
    #     Rule(next_page,process_links='deal_link',follow=True,callback='item_parse'),
    #     # Rule(content_page,callback='item_parse'),
    # ]

    # 提取下一页

    # def deal_link(self, links):
    #     for link in links:
    #         print('link:',links)
    #     return links


    def parse(self, response):
        item = SophotoItem()
        li = response.xpath('//ul[@id="list"]//li')
        print(len(li))
        # li = response.xpath('/div[@id="list"]//li')
        for i in li:
            # item['name'] = i.xpath('//div[@class="image"]/a/@title').extract()
            # print('name:',item["name"])
            # item['src'] = i.xpath('//div[@class="image"]/a/img/@src').extract()
            # print('src:', item["src"])
            # 一定加点，表示当前路径下 的
            url = i.xpath('.//div[@class="image"]/a/@href').extract()[0]
            # print('url:', url)


            yield scrapy.Request(url,callback=self.item_parse)
        global current_page
        current_page=response.url
        # print('current_page:', current_page)

    #     翻页
    #      不加extract  返回的是一个对象  加上之后  返回 列表
        next_page = response.xpath('//a[@class="pagenext"]/@href').extract()[0]
        if len(next_page)> 0:
            next_page = 'https://www.photophoto.cn'+next_page
            yield scrapy.Request(next_page,callback=self.parse)
            print('next:',next_page)



    #   b不进解析页面，可能是  域名存在问题，，修改一下

    def item_parse(self, response):
        item = SophotoItem()
        # print('12345676')
        item['name'] = response.xpath(".//div[@id='left11']/h1/text()").extract()[0]

        print('name:',item['name'])
        item['src'] = response.xpath('.//div[@id="photo"]/a/img/@src').extract()[0]
        print('src:',item['src'])

        yield item
        print('current_page:', current_page)








