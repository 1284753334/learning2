#                    _ooOoo_
#                   o8888888o
#                   88" . "88
#                   (| -_- |)
#                   O\  =  /O
#                ____/`---'\____
#              .'  \\|     |//  `.
#             /  \\|||  :  |||//  \
#            /  _||||| -:- |||||-  \
#            |   | \\\  -  /// |   |
#            | \_|  ''\---/''  |   |
#            \  .-\__  `-`  ___/-. /
#          ___`. .'  /--.--\  `. . __
#       ."" '<  `.___\_<|>_/___.'  >'"".
#      | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#      \  \ `-.   \_ __\ /__ _/   .-` /  /
# ======`-.____`-.___\_____/___.-`____.-'======
#                    `=---='
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#             佛祖保佑       永无BUG

from queue import Queue

myqueue =Queue(maxsize = 10) #队列中能存放的数据个数的上限
print('is empty:',myqueue.empty())
print('is full:',myqueue.full())
#将一个值放入队列中
myqueue.put(10)
print(myqueue.qsize())
print('is empty:',myqueue.empty())
print('is full:',myqueue.full())
myqueue.put(8)
print(myqueue.qsize())
myqueue.put(6)
print(myqueue.qsize())
#将一个值从队列中取出
print(myqueue.get())
print(myqueue.get())
print(myqueue.get())
print('is empty:',myqueue.empty())
print(myqueue.get(block=True,timeout=5))



