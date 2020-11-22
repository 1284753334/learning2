import pymysql

dicts = {'host':"192.168.0.107", 'port':3306, 'user':"root", 'password':"", 'database':"py1905"}

conn = pymysql.connect(**dicts)

cursor = conn.cursor(pymysql.cursors.DictCursor)

# 调用存储过程
moeny = 100
msg = None
cursor.callproc("exchange", args=(2, 3, moeny, msg))

# 获取 通过select 返回的结果
print(cursor.fetchall())

cursor.execute("select @_exchange_2 money , @_exchange_3 msg")

print(cursor.fetchone())

conn.commit()
# 在程序中、获取OUT参数的值

cursor.close()
conn.close()





