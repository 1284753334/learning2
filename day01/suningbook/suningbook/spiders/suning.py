import scrapy


class SuningSpider(scrapy.Spider):
    name = 'suning'
    allowed_domains = ['suning.com']
    start_urls = ['https://book.suning.com/']

    def parse(self, response):
        # li_list = response.xpath('//div[@class="menu-list"]/div[@class="menu-item"]')
        li_list = response.xpath('/html/body/div[6]/div/div[1]/div[1]/div[1]/div[1]/div[@class="menu-item"]')
        for li in li_list:
            item = {}
            item['b_cate'] = li.xpath("./dl/dt/h3/a/text()").extract_first()
            # 获取小分类标签
            a_list= li.xpath("./dl/dd/a")
            for a in a_list:
                item['s_href'] = a_list.xpath("./@href").extract_first()
                item['s_name'] = a_list.xpath("./text()").extract_first()
                yield scrapy.Request(
                    item['s_href'],
                    callback=self.parse_book_list(),
                    meta={'item':item}
                )


    def parse_book_list(self,response):
        item = response.meta['item']
            # 图书列表分页
        li_list = response.xpath("./div[@class='filter-results productMain clearfix  temporary']")






