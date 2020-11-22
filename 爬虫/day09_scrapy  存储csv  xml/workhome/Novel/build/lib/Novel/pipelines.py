# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import codecs
import os

import pymysql
from itemadapter import ItemAdapter


# class NovelPipeline:
#     def process_item(self, item, spider):
#         return item

class NovelPipeline(object):  #存储 为文本格式
    def __init__(self):

        self.f = codecs.open("result.txt", "a", "utf-8")

    def process_item(self, item, spider):
        #     name = scrapy.Field()
        #     url = scrapy.Field()
        #     # type = scrapy.Field()
        #     author = scrapy.Field()
        #     pub_data = scrapy.Field()
        #     # statue = scrapy.Field()
        # self.log('txt_path:'+os.path.abspath('./'))
        cont = item['name'] + ',' + item['url'] + ',' + item['type'] + ','  + ',' + item['author'] +','+ item['pub_date'] + '\n'
        self.f.write(cont)
        # self.f.write()
        return item

    def close_spider(self, spider):
        self.f.close()


class dbNovelPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='172.17.65.49',port=3306,db='DBsun',user='root',password='123456',charset='utf8')
        self.cur = self.conn.cursor()
    def process_item(self, item, spider):
        sql = "insert into novel(name,url,type,author,pub_date,statue) value (%s,%s,%s,%s,%s,%s)"
        params = [item["name"],item["url"],item["type"],item["author"],item["pub_date"],item["statue"]]
        self.cur.execute(sql, params)
        self.conn.commit()
        return item

# curl http://localhost:6800/listspiders.json?project=JobSpider