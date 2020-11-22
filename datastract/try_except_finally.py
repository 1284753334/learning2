


import pymysql

conn =None
cursor = None
try:
    # 1、获取数据库连接
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', database='py1905')

    # 2、获取游标

    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 3、通过程序完成转帐过程 id= 2 转给 id= 3 的 100

    # 查询id=2 的余额
    cursor.execute('select blance from account where id = %s',args=2)

    #  获取结果[列表里面套字典]

    balance = cursor.fetchone()['blance']
    money = 100;
    fid = 2
    tid = 3

    if balance >= money:
        cursor.execute('update account set blance= blance- %s where id=%s',args=(money,fid) )

        cursor.execute('update account set blance= blance+ %s where id=%s',args=(money,tid))
        print("转账成功，你的余额为:",(balance-money))
    else:
        print('余额不足，转账失败')

        conn.commit()
except Exception as e:
    if conn:conn.rollback()
finally:
    #关闭资源

    if cursor:cursor.close()
    if conn:#(conn只要有值，它就不为None)
        conn.close()

















