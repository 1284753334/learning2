"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/10/24'
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
# cele.py
from celery import Celery
from celery.schedules import crontab

uri = 'redis://:123456@127.0.0.1:6379/2'
app = Celery('tasks', broker=uri)
# 每分钟执行一次
c1 = crontab()
# 每天凌晨十二点执行
c2 = crontab(minute=0, hour=0)
# 每十五分钟执行一次
c3=crontab(minute='*/15')
# 每周日的每一分钟执行一次
c4=crontab(minute='*',hour='*', day_of_week='sun')
# 每周三，五的三点，七点和二十二点没十分钟执行一次
c5 = crontab(minute='*/10',hour='3,17,22', day_of_week='thu,fri')


@app.task
def send(message):
    return message


app.conf.beat_schedule = {
    'send-every-10-seconds': {
        'task': 'tasks.send',
        # 每隔2秒输出一次
        # 'schedule': 2.0,
        # 每分钟
        'schedule':c1,
        'args': ('Hello World', )
    },
}

# celery -A  tasks worker -l INFO -P eventlet





