# from queue import Queue
#
# myqueue = Queue(maxsize=10)
#
# print('is empty:',myqueue.empty())
# print('is full:',myqueue.full())
#
#
# # 将一个 值 放到 队列中
#
# myqueue.put(10)
# # 没有返回值的
# print()
# print(myqueue.qsize())
#
# print('is empty:',myqueue.empty())
# print('is full:',myqueue.full())
#
#
# myqueue.put(8)
# print(myqueue.qsize())
#
# print('is empty:',myqueue.empty())
# print('is full:',myqueue.full())
#
# myqueue.put(8)
#
# print('is empty:',myqueue.empty())
# print('is full:',myqueue.full())
#
# print(myqueue.get())
# print(myqueue.get())
# print(myqueue.get())
# # print(myqueue.get())
#
# print('is empty:',myqueue.empty())
#
# print(myqueue.get(True,timeout=3))



#  用 几个线程  负责 页面的爬取，把  返回的 网页源码  放到队列中，，然后 另外的  线程  负责提取 信息
# from queue import Queue
# # #
# # # page_queue = Queue(100)
# # # while True:
# # #     print(page_queue.get())

for  i  in  range(1,8):
    print(i,type(i))

