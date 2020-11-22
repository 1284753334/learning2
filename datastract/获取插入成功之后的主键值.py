# import pymysql
# conn=pymysql.connect(
#     host= 'localhost',
#     port=3306,
#     user = 'root',
#     password = '',
#     database = 'py1905'
# )
#
# cursor = conn.cursor(pymysql.cursors.DictCursor)
#
# len = cursor.execute('insert into students (name,teacher_id) values (%s,%s)',args=('李磊',3))
#
# # 获取插入数据的id
#
# print(cursor.lastrowid)
#
# print(cursor.rowcount())
#
# conn.commit()
#
#
#
#
#
#
#
#
import datetime
import time

print(time.time())
# a = datetime.datetime.now()
# b = str(a).replace('-','')
# c = str(a).replace('-','').replace(' ','')
# d = str(a).replace('-','').replace(' ','').replace(':','')
e = str(datetime.datetime.now()).replace('-','').replace(' ','').replace(':','').split('.')[0]

print(e)
