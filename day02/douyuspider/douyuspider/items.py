# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuspiderItem(scrapy.Item):
    # define the fields for your item here like:
    nickname = scrapy.Field() # 主播昵称
    image_url = scrapy.Field()  # 图片的地址
    image_path = scrapy.Field()  # 照片本地存储位置

