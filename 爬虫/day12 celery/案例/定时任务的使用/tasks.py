from celery import Celery
from celery import Task
app = Celery('tasks', backend='redis://:123456@127.0.0.1:6379/2',
broker='redis://:123456@127.0.0.1:6379/2')

app.config_from_object('celery_config')


@app.task(bind=True)
def period_task(self):
 print('period task done: {0}'.format(self.request.id))



#  运行work
# celery -A tasks worker -l info -P eventlet

# 运行定时的模块 .bat  启动任务  任务会自动执行

# celery -A tasks beat






