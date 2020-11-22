# -*- coding: utf-8 -*-
import scrapy
from jdCrawl.items import JdcrawlItem
class JdcrawlSpider(scrapy.Spider):
    name = 'jdcrawl'
    allowed_domains = ['search.jd.com']
    base_url ='https://search.jd.com/Search?enc=utf-8&keyword='

    global a
    def start_requests(self):
        print('1')
        for key in self.settings.get('KEYWORDS'):
            print(key)
            for page in range(1,self.settings.get('MAX_PAGE')+1):
                print('page:',page)
                url = self.base_url+key
                yield scrapy.Request(url=url, meta={'page': page}, callback=self.parse, dont_filter=True)

    def parse(self, response):
        print(2)
        print(response.url)
        # products= response.xpath("//ul[@class='gl-warp clearfix']/li[1]").extract()
        products= response.xpath("//div[@id='J_goodsList']//li").extract()
        print('p_len:',len(products))
        print('-'*50)
        # print(products)
        # print(type(products))
        a=1
        for product in products:
            # print(3)
            print('item_num:',a)
            a+=1
            item = JdcrawlItem()
            productitem = scrapy.Selector(text=product)
            print(products)
            print(type(products))
            item['price']= productitem.xpath(".//div/div[3]/strong/i/text()").extract()
            print('price》:', item['price'])
            if len(item['price']) > 0:
                item['price'] = item['price'][0]
            else:
                item['price'] = 'kong'
            print('price:', item['price'])
            item['title'] = productitem.xpath(".//div/div[4]/a/em/text()").extract()[0]
            if len(item['title']) > 0:
                item['title'] = item['title']
            else:
                item['title'] = 'kong'
            print('title:',item['title'])
            item['comment'] = productitem.xpath(".//div/div[5]/strong/a/text()").extract()[0]
            print('comment:',item['comment'])
            item['shop'] = productitem.xpath(".//div/div[7]/span/a/text()").extract()[0]
            item['icons'] = productitem.xpath(".//div/div[8]/i/text()").extract()[0]
            if len(item['title']) > 0:
                item['icons'] = item['icons'][0]
            else:
                item['icons'] = 'kong'

            print('icon:',item['icons'])
            yield item
            print(4)

