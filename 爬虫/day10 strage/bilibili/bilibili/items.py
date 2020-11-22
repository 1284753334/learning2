# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibiliItem(scrapy.Item):
    #  编号
    vnum = scrapy.Field()
    # 标题
    vtitle = scrapy.Field()
    # url地址
    vurl = scrapy.Field()
    # 综合评分
    vpts = scrapy.Field()
