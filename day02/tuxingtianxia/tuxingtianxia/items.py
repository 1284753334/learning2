# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TuxingtianxiaItem(scrapy.Item):
    # define the fields for your item here like:
    #  定义字段  名字  路径  url
    name = scrapy.Field()
    image_url = scrapy.Field()
    image_path = scrapy.Field()

