# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


'''


全本小说（CrawlSpider）
https://www.quanben.net/modules/article/articlelist.php?fullflag=1&page=1
爬取小说名称，url，类别，作者，更新时间，状态
'''




import scrapy


class NovelItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    url = scrapy.Field()
    type = scrapy.Field()
    author = scrapy.Field()
    pub_date = scrapy.Field()
    statue = scrapy.Field()

    # name = scrapy.Field()
    # novel_url = scrapy.Field()
    # sort = scrapy.Field()
    # author = scrapy.Field()
    # update_time = scrapy.Field()
    # state = scrapy.Field()




    # name = scrapy.Field()
    # novel_url = scrapy.Field()
    # # sort = scrapy.Field()
    # author = scrapy.Field()
    # update_time = scrapy.Field()
    # # state = scrapy.Field()
