


import pymysql


# 1、获取数据库连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', database='py1905')

# 2、获取游标

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 3、通过程序完成转帐过程 id= 2 转给 id= 3 的 100

# 查询id=2 的余额

# list = [
#     ('aaa',100),
#     ('bbb',100),
#     ('ccc',100),
# ]

list = [
    {'name':'eee','b':500},
    {'name':'fff','b':500},
    {'name':'ggg','b':500},


]
# len = cursor.executemany('insert into account (name,blance) values (%s,%s)',args=list)
len = cursor.executemany('insert into account (name,blance) values (%(name)s,%(b)s)',args=list)

print(len)
conn.commit()

cursor.close()
conn.close()




















