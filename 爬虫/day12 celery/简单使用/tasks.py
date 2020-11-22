#tasks.py
from celery import Celery
uri = 'redis://:123456@127.0.0.1:6379/2'
#  celery 对象  任务对列，中间人的 设置
app = Celery('tasks', backend=uri, broker=uri) #配置好 celery 的 backend 和 broker




@app.task #普通函数装饰为 celery task
def add(x, y):
 return x + y






