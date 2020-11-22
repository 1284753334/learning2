import pymysql

# 1、连接MySQL服务器、并获取连接对象
conn = pymysql.connect(host="192.168.0.107", port=3306, user="root", password="", database="py1905")

# 2、通过conn连接、获取游标对象
cursor = conn.cursor()

# 3、通过游标对象、操作数据库
dicts = {"name": "老六' or 1 = '1"}

# execute() 执行

print("select * from account where name ='%s'" % dicts["name"])
len = cursor.execute("select * from account where name = '%s'" % dicts['name'])
# len = cursor.execute("insert into  account (name,blance) values(%s,%s) %(dict['name'],dict['blance'])")
# len = cursor.execute("select * from account ")
# 获取查询结果
s = cursor.fetchall()

print(s)

# 4、对数据进行提交
conn.commit()
#
# # 5、关闭资源  (释放资源)
cursor.close()
conn.close()
