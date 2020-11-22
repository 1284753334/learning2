"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/10/20'
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
"""
#报红也能执行
from tasks import add
import time

result = add.delay(4, 4) #不要直接 add(4, 4)，这里需要用 celery 提供的接口 delay 进行调用
while not result.ready():
    time.sleep(50)
print('task done: {0}'.format(result.get()))
