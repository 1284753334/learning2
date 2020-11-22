from celery import Celery
from celery.schedules import crontab
uri = 'redis://:123456@127.0.0.1:6379/2'
app = Celery('tasks', broker=uri)
# 每分钟执行一次
c1 = crontab()


# 每天凌晨十二点执行
c2 = crontab(minute=0, hour=0)
# 每十五分钟执行一次  对15 取整  为 ，，即每15 分钟  执行一次
crontab(minute='*/15')
# 每周日的每一分钟执行一次
crontab(minute='*',hour='*', day_of_week='sun')
# 每周三，五的三点，七点和二十二点没十分钟执行一次
crontab(minute='*/10',hour='3,17,22', day_of_week='thu,fri')

@app.task
def send(message):
    return message

app.conf.beat_schedule = {
 'send-every-10-seconds': {
 #      执行send 任务
 #  task.send  task 为文件名
 'task': 'task.send',
 #      定时时间，每隔10秒 执行一次
 'schedule': 10.0,
 #'schedule':c1,
 'args': ('Hello World', )
 },
}


# celery  -A task worker -l INFO -P event
'''
上面的示例配置了一个每十秒执行一次的周期任务，任务为 tasks.send，参数为 ‘Hello 
World’。
这种配置的方式可以支持多个参数
task： 指定任务的名字
schedule : 设定任务的调度方式，可以是一个表示秒的整数，也可以是一个 timedelta 对
象，或者是一个 crontab 对象（后面介绍），总之就是设定任务如何重复执行
args： 任务的参数列表
kwargs：任务的参数字典
options：所有 apply_async 所支持的参数
8 / 14
'''
