# -*- coding: utf-8 -*-
import scrapy
# b站排行榜爬虫（scrapy）
# https://www.bilibili.com/ranking#!/all/0/0/7/
# 爬取编号，标题，url，综合评分，播放量，评论数
# 存储到mysql数据库

from bilibili.items import BilibiliItem
class BilichongSpider(scrapy.Spider):
    name = 'bilichong'
    allowed_domains = ['bilibili.com']
    start_urls = ['https://www.bilibili.com/ranking#!/all/0/0/7/']

    def parse(self, response):
       item =BilibiliItem()
       list = response.xpath('//ul[@class="rank-list"]/li')
       print("len:",len(list))
       for i in list:
           item["number"] = i.xpath('./div[@class="num"]/text()').extract()[0]
           print(type(item["number"]))
           item["title"] = i.xpath('.//div[@class="info"]/a/text()').extract()[0]
           url = i.xpath('.//div[@class="info"]/a/@href').extract()[0]
           item["url"] = url.split("//")[-1]
           item["grade"] = i.xpath('.//div[@class="pts"]/div/text()').extract()[0]
           item["play_number"] = i.xpath('.//div[@class="detail"]/span[1]/text()').extract()[0]
           item["comments"] = i.xpath('.//div[@class="detail"]/span[2]/text()').extract()[0]
           yield item
