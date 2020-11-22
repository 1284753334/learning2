# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class SunspiderPipeline(object):
    def __init__(self):
        try:
            # self.conn = pymysql.connect(host='localhost',port=3306,db='dbsun1905',user='root',password='123456',charset='utf8')
            self.conn = pymysql.connect(host='localhost', port=3306, db='DBsun', user='root', password='',charset='utf8')

            self.cur = self.conn.cursor()
        except Exception as e:
            print('conn error...',e)


    def process_item(self, item, spider):
        try:
            strsql = 'insert into tbsun(title,detail_url,number,content,author,pub_date) VALUES (%s,%s,%s,%s,%s,%s)'
            params = [item['title'],item['detail_url'],item['number'],item['content'],item['author'],item['pub_date']]
            self.cur.execute(strsql,params)
            self.conn.commit()
        except Exception as e:
            print('insert error...',e)

        return item


    def close_spider(self,spider):
        self.cur.close()
        self.conn.close()
