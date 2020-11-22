# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#
#
# class BlogcrawlspiderPipeline(object):
#     def process_item(self, item, spider):
#         return item

#
# import pymysql
# from twisted.enterprise import adbapi
#
#
# class MysqlPipelineTwo(object):
#     def __init__(self, dbpool):
#         self.dbpool = dbpool
#
#     @classmethod
#     def from_settings(cls, settings):  # 函数名固定，会被scrapy调用，直接可用settings的值
#         """
#         数据库建立连接
#         :param settings: 配置参数
#         :return: 实例化参数
#         """
#         adbparams = dict(
#             host='127.0.0.1',
#             db='blog',
#             user='root',
#             password='',
#             port=3306,
#             cursorclass=pymysql.cursors.DictCursor  # 指定cursor类型
#         )
#         # 连接数据池ConnectionPool，使用pymysql或者Mysqldb连接
#         dbpool = adbapi.ConnectionPool('pymysql', **adbparams)
#         # 返回实例化参数
#         return cls(dbpool)
#
#     def process_item(self, item, spider):
#         """
#         使用twisted将MySQL插入变成异步执行。通过连接池执行具体的sql操作，返回一个对象
#         """
#         query = self.dbpool.runInteraction(self.do_insert, item)  # 指定操作方法和操作数据
#         # 添加异常处理
#         query.addCallback(self.handle_error)  # 处理异常
#
#     def do_insert(self, cursor, item):
#         # 对数据库进行插入操作，并不需要commit，twisted会自动commit
#         insert_sql = 'insert into blog2 (title,content) VALUES(%s,%s)'
#
#         cursor.execute(insert_sql, (item['title'], item['content']))
#
#     def handle_error(self, failure):
#         if failure:
#             # 打印错误信息
#             print(failure)


import pymysql
class MysqlPipelineTwo(object):
    def __init__(self):
        # 1. 建立数据库的连接
        self.connect = pymysql.connect(
	    # localhost连接的是本地数据库
            host='localhost',
            # mysql数据库的端口号
            port=3306,
            # 数据库的用户名
            user='root',
            # 本地数据库密码
            password='',
            # 表名
            db='blog',
            # 编码格式
            charset='utf8'
        )
        # 2. 创建一个游标cursor, 是用来操作表。
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        # 3. 将Item数据放入数据库，默认是同步写入。
        insert_sql = "INSERT INTO blog (title, content) VALUES ('%s', '%s')" %(item['title'], item['content'])
        self.cursor.execute(insert_sql)

        # 4. 提交操作
        self.connect.commit()

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()