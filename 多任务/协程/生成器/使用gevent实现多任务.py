import time

import gevent


'''协程  利用暂停的时间   切换任务    

线程  依赖 进程   协程依赖 线程    

切换 资源  好比 调用函数 
'''
def f1(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # time.sleep(0.5)
        gevent.sleep(0.5)
def f2(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # time.sleep(0.5)
        gevent.sleep(0.5)
def f3(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # time.sleep(0.5)
        gevent.sleep(0.5)

print('-----1----')
g1 = gevent.spawn(f1, 5)
print('-----2----')
g2 = gevent.spawn(f2, 5)
print('-----3----')
g3 = gevent.spawn(f3, 5)
print('-----4----')
g1.join()
g2.join()
g3.join()
