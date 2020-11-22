# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import codecs


class SunspinderPipeline:
    #  定义数据库的链接
    def __init__(self):
        try:
            # 获取数据库链接
            self.conn = pymysql.connect(host = 'localhost',port = 3306,db = 'DBsun',user='root',password = '123456',charset='utf8')
            #  获取游标
            self.cur= self.conn.cursor()
        except Exception as e:
            print(e)

    #  保存数据
    def process_item(self, item, spider):

        try:
            strsql = 'insert into dbsun1(num,title,author,pub_time,detail_url,content) values(%s,%s,%s,%s,%s,%s) '
            params = [item['number'],item['title'],item['author'],item['pub_time'],item['detail_url'],item['content']]
            self.cur.execute(strsql,params)
            self.conn.commit()

        except Exception as e:
            print('err:',e)

        return item


    #  断开链接
    def close(self,spider):

        self.cur.close()
        self.conn.close()



#  必须新建文件，，，才能保存
import pymysql

# class SunspinderPipeline:
#     #  定义数据库的链接
#     def __init__(self):
#         try:
#             # 获取数据库链接
#             self.conn = pymysql.connect(host = 'localhost',port = 3306,db = 'DBsun',user='root',password = '123456',charset='utf8')
#             #  获取游标
#             self.cur= self.conn.cursor()
#         except Exception as e:
#             print(e)
#
#     #  保存数据
#     def process_item(self, item, spider):
#
#
#
#         '''
#             number = scrapy.Field()
#             title = scrapy.Field()
#             url = scrapy.Field()
#             score = scrapy.Field()
#             broad_number = scrapy.Field()
#             comment_num = scrapy.Field()
#
#         '''
#
#         try:
#             strsql = 'insert into dbsun(number,title,url,score,broad_number,comment_num) values(%s,%s,%s,%s,%s,%s) '
#             params = [item['number'],item['title'],item['url'],item['score'],item['broad_number'],item['comment_num']]
#             self.cur.execute(strsql,params)
#             self.conn.commit()
#
#         except Exception as e:
#             print('err:',e)
#
#         return item
#
#
#     #  断开链接
#     def close(self,spider):
#
#         self.cur.close()
#         self.conn.close()

#
import csv
#

class Save_csv(object):  #存储为csv文件，用于以下的数据分析处理
    #
    def __init__(self):
    # 新建一个文件夹就能生成了
        self.file=codecs.open('排行3.csv','w','utf-8')
        self.fr=csv.writer(self.file)
        self.fr.writerow(['number','title','url','score','broad_number','comment_num',])

    def process_item(self, item, spider):

        self.fr.writerow([item['number'],item['title'] , item['url'] , item['score'] , item[
            'broad_number'],item['comment_num']])

        return item

    def close_spider(self, spider):
        self.file.close()





class BibiPipeline(object):  #存储 为文本格式
    def __init__(self):
        self.f = codecs.open("bibi排行.txt", "a", "utf-8")

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
        cont = item['number'] + ',' + item['title'] + ',' + item['url'] + ',' + item['score'] + ',' + item[
            'broad_number'] +','+ item['comment_num'] + '\n'
        self.f.write(cont)
        # self.f.write()
        return item

    def close_spider(self, spider):
        self.f.close()
#


