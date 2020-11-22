"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/10/23'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛

在task 所在的目录下 同级目录，运行 celery tasks -A  worker  -l  INFO  -P  event

#  运行work
#
celery -A weather_worker worker -l INFO -P gevent -c 20

gevent   协程   开 20个
# 运行定时的模块 .bat  启动任务  任务会自动执行

# celery -A tasks beat

读取reds所有的结果

键值对存储的结果，就像一个字典，遍历字典就可以了
"""
import time

import redis
import json

r = redis.Redis(host='127.0.0.1',password='123456',port=6379,db=3)
#
keys = r.keys()
#print('\u79c0\u5c7f')
for key in keys:
    res = r.get(key)
    res = json.loads(res.decode('utf-8'))
    # t= time.time('%-%M-%d')
    # print (res)
    print (res.get('result'))

