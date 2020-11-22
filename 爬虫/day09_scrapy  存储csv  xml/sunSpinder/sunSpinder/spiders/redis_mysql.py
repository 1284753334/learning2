'''
从redis  导出数据到 mysql


'''

import redis, json, time
from pymysql import connect

redis_client = redis.StrictRedis(host="127.0.0.1", port=6379, password="123456",db=0)  # redis数据库链接
mysql_client = connect(host="127.0.0.1", user="root", password="123456", database="DBsun", port=3306,
                       charset='utf8')  # mysql数据库链接
cursor = mysql_client.cursor()



'''
 title = scrapy.Field()
    detail_url = scrapy.Field()
    number = scrapy.Field()
    content = scrapy.Field()
    author = scrapy.Field()
    pub_time = scrapy.Field()
'''
def write_mysql():
    i = 0
    try:
        while True:
            print(i)
            start_time = time.time()
            time.sleep(0.01)
            source, data = redis_client.blpop(["Sun3:items"], timeout=30)
            item = json.loads(data.decode())
            sql = "insert into dbsun2_redis(num,title,author,pub_time,detail_url,content) values(%s,%s,%s,%s,%s,%s)"
            params = [item["title"], item["detail_url"], item["number"], item["author"],
                      item["author"], item["pub_time"] ]
            cursor.execute(sql, params)
            mysql_client.commit()
            i += 1
            end_time = time.time()
            print(end_time - start_time)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    write_mysql()