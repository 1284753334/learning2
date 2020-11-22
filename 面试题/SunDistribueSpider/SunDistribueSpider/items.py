# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SundistribuespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  # 标题
    number = scrapy.Field()  # 编号
    detail_url = scrapy.Field()  # 链接
    author = scrapy.Field()  # 投诉者
    pub_date = scrapy.Field()  # 投诉时间
    content = scrapy.Field()  # 投诉内容
