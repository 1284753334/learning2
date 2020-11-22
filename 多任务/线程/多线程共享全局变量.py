import threading
import time

g_num = 100

def test1():
    global g_num
    g_num +=10
    print('------in teat1----%d'%g_num)

def test2():
    print('------in teat2----%d'%g_num)


def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)
    t1.start()
    time.sleep(1)  
    t2.start()


if __name__ == '__main__':
    main()