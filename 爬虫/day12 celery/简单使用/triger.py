import time

from tasks import add
result = add.delay(4, 4) #不要直接 add(4, 4)，这里需要用 celery 提供的接口 delay 进行调用
#  判断是否准备好
while not result.ready():
    time.sleep(40)
print('task done: {0}'.format(result.get()))


'''
    运行 worker 
语法：
celery -A proj.task worker --loglevel=info
-A 是指对应的应用程序, 其参数任务文件名
worker 任务角色，，表明当前机器的身份；此时，就是启动了一个 worker
--loglevel=info 任务日志级别
在 tasks.py 所在目录下运行：


使用时 需要在命令行(切换到 该项目文件所在的目录 ) 使用命令   检测队列  ，然后触发函数  


#  win10 命令可以直接使用
#celery -A tasks worker -l INFO -P eventlet（win10 下）
#celery -A tasks worker --loglevel=info
-P eventlet：通过协程实现并发











    
    
    '''
