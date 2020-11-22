# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SundistributeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    detail_url = scrapy.Field()
    number = scrapy.Field()
    content = scrapy.Field()
    author = scrapy.Field()
    pub_time = scrapy.Field()

