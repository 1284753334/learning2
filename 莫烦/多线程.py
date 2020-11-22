import threading
import time

def thread_job():
    # print('this ia an added Thread,number iS %s' % threading.current_thread())
    print('T1 start\n')
    for i in range(10):
        time.sleep(0.1)
    print("T1 finish\n")
def t2_job():
    print('T2 start\n')
    print('T2 finish\n')

def main():

    add_thread = threading.Thread(target=thread_job,name='T1')
    # 激活的线程
    # print(threading.active_count())
#     # 遍历 激活的线程
    print(threading.enumerate())
# #  当前线程
#     print(threading.current_thread())
    thread2 = threading.Thread(target=t2_job,name='T2')
    add_thread.start()
    thread2.start()
    thread2.join()
    #  线程完成再执行 all  done
    add_thread.join()
    #
    print('all done\n')

if __name__ == '__main__':
    main()














