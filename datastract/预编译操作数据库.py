import pymysql

# 1、连接MySQL服务器、并获取连接对象


conn = pymysql.connect(host="192.168.0.107", port=3306, user="root", password="", database="py1905")

# 2、通过conn连接、获取游标对象
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 3、通过游标对象、操作数据库
dicts = {"name": "老六"}

# execute() 执行

len = cursor.execute("select * from account where name= %s",args=dicts['name'] )

# 获取查询结果
s = cursor.fetchall()
# 获取查询的所有字段

print(s)

# 4、对数据进行提交
conn.commit()

# 5、关闭资源
cursor.close()
conn.close()
