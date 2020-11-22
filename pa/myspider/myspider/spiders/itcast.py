import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#ajavaee']

    def parse(self, response):
        pass
        # 处理start_utl 地址对应的响应
        #  extract()  提取其中的文字
        # ret1 = response.xpath('//div[@class="maincon"]//h2/text()').extract()
        # print(ret1)
        #  分组

        li_list = response.xpath('//div[@class="maincon"]//li')
        print(len(li_list))
        for  li in li_list:
            item = {}
            item['name'] = li.xpath('.//h2/text()').extract_first()
            item['tilte'] = li.xpath('.//h2/span/text()').extract_first()
            # print(item)
            yield item

