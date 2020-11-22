import threading
import time

g_num = 0


def test1(num):
    global g_num
    mutex.acquire()
    for i in range(num):
        g_num += 1
    mutex.release()
    print('------in teat1----%d' % g_num)


def test2(num):
    global g_num
    # 上锁
    mutex.acquire()
    for i in range(num):
        g_num += 1
    mutex.release()
    print('------in teat2----%d' % g_num)

#  创建一个互斥锁，默认是没有上锁的

mutex = threading.Lock()

def main():
    t1 = threading.Thread(target=test1, args=(100000,))
    t2 = threading.Thread(target=test2, args=(100000,))
    t1.start()
    t2.start()

    time.sleep(1)
    print('------in main threading----%d' % g_num)


if __name__ == '__main__':
    main()