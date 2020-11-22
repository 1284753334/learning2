"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/10/21'
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
from celery import Celery
from celery import Task

app = Celery('tasks', backend='redis://:123456@127.0.0.1:6379/1', broker='redis://:123456@127.0.0.1:6379/1')
app.config_from_object('celery_config')


@app.task(bind=True)
def period_task(self):
    print('period task done: {0}'.format(self.request.id))

