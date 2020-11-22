import scrapy

from 爬虫.day09_scrapy.workhome.Bilibili.Bilibili.items import BilibiliItem



''''
b站排行榜爬虫（scrapy）
https://www.bilibili.com/ranking#!/all/0/0/7/
爬取编号，标题，url，综合评分，播放量，评论数
存储到mysql数据库

'''
class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['https://www.bilibili.com']
    start_urls = ['https://www.bilibili.com/v/popular/rank/all']

    def parse(self, response):
        item = BilibiliItem()

        ls = response.xpath('//ul[@class="rank-list"]//li')
        # ls = response.xpath('//*[@id="app"]/div[2]/div[2]/ul//li')
        # ls = response.css('div.rank-list-wrap > ul  li')
        print(ls)
        print('len:',len(ls))
        for i in ls:
            # item['num'] = response.xpath('./li/div[1]/text()').extract()[0]
            item['number'] = i.xpath('./div[@class="num"]/text()').extract()[0]
            item['title'] = i.xpath('.//a[@class="title"]/text()').extract()[0]
            item['url'] = i.xpath('.//a[@class="title"]/@href').extract()[0]
            item['score'] = i.xpath('.//div[@class="pts"]/div/text()').extract()[0]

            item['broad_number'] = i.xpath('.//span[@class="data-box"]/text()').extract()[0].strip()

            # item['comment_num'] = i.xpath('.//div[@class="info"]/div[1]/div[2]/text()').extract()[0].strip()
            # item['comment_num'] = i.xpath('./div[@class="content"]//div[@class="detail"]/div[2]/text()').extract()
            # item['comment_num'] = i.xpath('.div[2]/div[2]/div[1]/div[2]/text()').extract()[0]
            item['comment_num'] = i.xpath('.//span[@class="data-box"]/text()').extract()[1].strip()

            yield  item



