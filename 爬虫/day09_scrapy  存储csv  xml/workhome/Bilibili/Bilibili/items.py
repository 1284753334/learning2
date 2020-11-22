# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
'''

爬取编号，标题，url，综合评分，播放量，评论数
'''
import scrapy


class BilibiliItem(scrapy.Item):
    # define the fields for your item here like:
    number = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    score = scrapy.Field()
    broad_number = scrapy.Field()
    comment_num = scrapy.Field()


