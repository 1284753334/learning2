import json

import scrapy

from day20.Q.qiushi.qiushi.items import QiushiItem


class BaikeSpider(scrapy.Spider):
    name = 'baike1'
    # allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        item = QiushiItem()
        ls = response.xpath('//div[@class="col1 old-style-col1"]/div')
        print(len(ls))
        all_data = []
        # for li in ls:
        #     #xpath 返回的是列表，列表元素是Select 类型的对象
        #     name = li.xpath('./div[1]/a[2]/h2/text()')[0].extract()\
        #     #  列表调用 extract  返回的还是列表
        #     text = li.xpath('./a[1]/div/span//text()').extract()
        #     text = ''.join(text)
        #     print(name)
        #     print(text)
        #     dict = {
        #         'author':name,
        #         'content':text
        #     }
        #     all_data.append(dict)
        # return  all_data
        #     # yield item
        for li in ls:
            # xpath 返回的是列表，列表元素是Select 类型的对象
            item['name'] = li.xpath('./div[1]/a[2]/h2/text()')[0].extract() \
                #  列表调用 extract  返回的还是列表
            text = li.xpath('./a[1]/div/span//text()').extract()
            item['text'] = ''.join(text)
            print(item['name'])
            print(item['text'])
            yield item

