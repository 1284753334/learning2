# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class BilibiliPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',port=3306,db='aaa',user='root',password='',charset='utf8')
        self.cur = self.conn.cursor()
    def process_item(self, item, spider):
        sql = "insert into aa(number,title,url,grade,play_number,comments) value (%s,%s,%s,%s,%s,%s)"
        params = [item["number"],item["title"],item["url"],item["grade"],item["play_number"],item["comments"]]
        self.cur.execute(sql, params)
        self.conn.commit()
        return item
