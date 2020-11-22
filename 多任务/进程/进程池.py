'''程序的创建和销毁  需要 花费 大量的时间

进程池 节省 开销
'''
import os
import random
from multiprocessing import Pool
import time

def worker(msg):
    time.sleep(1)
    t_start = time.time()
    print('%s开始执行，进程号为%d()'%(msg,os.getpid()))

    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg,'执行结束，耗时为%3.2f' % (t_stop-t_start))

if __name__ == '__main__':

    pool = Pool(processes = 3)

    # result = []

    for i in range(10):
        # msg = 'Hello %d world' % i
        r = pool.apply_async(func = worker,args = (i,))
        # result.append(r)

    print('---start---')
    #  关闭进程池
    pool.close()
    #  等你带进程池中，所有子进程完成，必须放在close之后
    pool.join()
    print('--end---')
    #
    # for i in result:
    #     print(i.get())










