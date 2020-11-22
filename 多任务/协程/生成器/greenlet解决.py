from greenlet import greenlet
import time

def test1():
    while True:
        print('-----a-------')
        g2.switch()
        time.sleep(0.5)

def test2():
    while True:
        print('----B----')
        g1.switch()
        time.sleep(0.5)

g1 = greenlet(test1)
g2 = greenlet(test2)
g1.switch()