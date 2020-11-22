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
from datetime import timedelta
from celery.schedules import crontab

CELERYBEAT_SCHEDULE = {
# BEAT_SCHEDULE = {
    'ptask': {
        'task': 'tasks.period_task',
        'schedule': timedelta(seconds=5),
    },
}
#  6.0 以前
CELERY_RESULT_BACKEND = 'redis://:123456@127.0.0.1:6379/2'
# auth "yourpassword" 'redis://:123456@127.0.0.1:6379/2'
# RESULT_BACKEND = 'redis://:123456@127.0.0.1:6379/1'
CELERY_TIMEZONE = 'Asia/Shanghai'
# TIMEZONE = 'Asia/Shanghai'

# CELERY_ENABLE_UTC=True
