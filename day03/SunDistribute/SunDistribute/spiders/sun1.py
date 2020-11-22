import scrapy
from scrapy.spiders import CrawlSpider, Rule
#  只能手动导入
from scrapy.linkextractors import LinkExtractor

from day03.SunDistribute.SunDistribute.items import SundistributeItem


class Sun1Spider(CrawlSpider):
    name = 'sun1'
    allowed_domains = ['wz.sun0769.com']
    # start_urls = ['http://wz.sun0769.com/political/index/index']
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest']

    #  翻页  提取的是 一个标签  不是里面的href 属性  /html/body/div[2]/div[3]/div[3]/a[2]
    # page_link = LinkExtractor(restrict_xpaths=('http://wz.sun0769.com'+'//div[@class = "mr-three paging-box"]/a[-1]',))
    # page_link = LinkExtractor(restrict_xpaths=('http://wz.sun0769.com'+'/html/body/div[2]/div[3]/div[3]/a[2]',))
    page_link = LinkExtractor(restrict_xpaths=('//div[@class="mr-three paging-box"]/a[2]',))
    content_link = LinkExtractor(restrict_xpaths=('//span[@class="state3"]/a',))
    #  实现 翻页  详情页
    rules = [
        Rule(page_link,follow=True),
        Rule(content_link, callback='parse_item')

    ]


    #  进入详情页面进行提取数据
    def parse_item(self, response):
        item = SundistributeItem()
        #  标题编号
        item['title'] = response.xpath('//div[@class = "mr-three"]/p/text()').extract_first()
        if not  item['title']:
            item["title"] = '空'
        #  编号
        item['number'] = response.xpath('//div[@class = "mr-three"]/div/span[3]/text()').extract_first().split(' ')[1]
        if not  item['number']:
            item["number"] = '空'
        #  详情链接
        item['detail_url'] = response.url
        #  发布者
        item['author'] = response.xpath('//span[@class="fl details-head"]/text()').extract_first().strip()
        if not item['author']:
            item["author"] = '空'
        #  发布日期
        resp  = response.xpath('//span[@class="focus-date clear focus-date-list"]/span[2]/text()').extract_first()

        item['pub_date'] = response.xpath('//span[@class="fl details-head"]/a/text()').extract_first()
        if not  item['pub_date']:
            item["pub_date"] = '空'

        #  内容
        item['content'] = response.xpath('//span[@class="details-box"]/pre/text()').extract_first()
        item['content'] = ''.join(item['content']).strip()
        if not  item['content']:
            item["content"] = '空'
        yield  item
