# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import codecs

from itemadapter import ItemAdapter


class SinablogPipeline:
    def process_item(self, item, spider):
        return item

class sinaPipeline(object):  #存储 为文本格式
    def __init__(self):
        self.f = codecs.open("SinaBlog.txt", "a", "utf-8")

    def process_item(self, item, spider):
        # print(item)
        # print(type(item))
        # rank_item = scrapy.Field()
        # title = scrapy.Field()
        # play = scrapy.Field()
        # view = scrapy.Field()
        # author = scrapy.Field()
        # score = scrapy.Field()
        #
        cont = item['title'] + ',' + item['detail_url'] + item['content'] + '\n'
        self.f.write(cont)
        # self.f.write()
        return item
