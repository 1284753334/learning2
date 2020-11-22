# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field

class ProductItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    dp = Field()
    title = Field()
    price = Field()
    comment=Field()
    url=Field()
    type=Field()