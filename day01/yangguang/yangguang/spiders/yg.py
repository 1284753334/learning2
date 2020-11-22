import scrapy

from day01.yangguang.yangguang.items import YangguangItem


class YgSpider(scrapy.Spider):
    name = 'yg'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/political/index/index']

    def parse(self, response):
        # 分组
        tr_list = response.xpath('ul[@class = "title-state-ul"/li]')
        for tr in tr_list:
            item = YangguangItem()
            item['title'] = tr.xpath('./span[3]/text()').extract_first()
            item['href'] = tr.xpath('./span[3]/@src').extract_first()
            item['publish_date'] = tr.xpath('./span[4]/text()').extract_first()

            yield scrapy.Request(
                item['href'],
                callable= self.parse_detail,
                meta = {'item':item}
            )

            # 翻页

            next_url = response.xpath('//a[text()="<"/@href]').extract_first()
            if next_url is not None:
                yield  scrapy.Request(
                    next_url,
                    callback=self.parse

                )


#   处理详情页
    def parse_detail(self,response):
        item = response.meta['item']
        yield item