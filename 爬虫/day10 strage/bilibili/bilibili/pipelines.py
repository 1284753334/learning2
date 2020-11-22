# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import  pymysql


class BilibiliPipeline(object):

    def process_item(self, item, spider):
        print("item:",item)
        DBKWARGS = spider.settings.get('DBKWARGS')
        con = pymysql.connect(**DBKWARGS)
        cur = con.cursor()
        sql = "insert into " \
              "tbB (vnum , vtitle , vurl ,vpts ,inTime )  " \
              "VALUE (%s  ,%s ,%s ,%s , now())"
        lis = (item['vnum'],item['vtitle'],item['vurl'],item['vpts'])
        try:
            cur.execute(sql,lis)
        except Exception as e:
            print ("Insert error:", e)
            con.rollback()
        else:
            con.commit()
        cur.close()
        con.close()
        return item