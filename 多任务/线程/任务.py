import threading
import time

from cal_time import timer


def sing():
    for i in range(5):
        print('-----正在唱歌')
        time.sleep(1)

def dance():
    for i in range(5):
        print('*******正在跳舞')
        time.sleep(1)

def  sdance():
    for i in range(5):
        print('&&&&&&喝水')
        time.sleep(1)

@timer
def main():
    # sing()
    # dance()

    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t3 = threading.Thread(target=sdance)
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    thread_num = len(threading.enumerate())
    print(f"线程数量是{thread_num}")


if __name__ == '__main__':
    main()
