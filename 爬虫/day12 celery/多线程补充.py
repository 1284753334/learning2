# # #!/usr/bin/env python
# # # -*- coding: utf-8 -*-
# # """
# # Created on 2020/11/16 13:40:41
# #
# # @author: Json
# #
# #         认真大胆      永无BUG
# # """
# #
# # #   使用多线程抓取翻页的时候，，可能出现重复抓取的现象
# #
# # import threading
# # import time
# #
# # def  sing():
# #     for  i in range(5):
# #         print('正在唱歌')
# #         time.sleep(1)
# #
# #
# #
# #
# # def  dance():
# #     for i in range(5):
# #         print('正在跳舞')
# #         time.sleep(1)
# # # 定义一个运行函数
# # def  main():
# #     #  target 当前运行哪个函数，注意不要加括号
# #     t1= threading.Thread(target=sing)
# #     t2= threading.Thread(target=dance)
# #     t1.start()
# #     t2.start()
# #     # 同时出现结果 简单的多线程
# #     # 多线程在任何场所都能使用吗 ？  非也
# #     # t1.join()
# #     # t2.join()
# # main()
# #
# #
#
# #  模拟 url
# from  queue import Queue
# import threading
#
# list_data = [1,2,3,4,5,6]
# def test():
#     for i in list_data:
#
#
#         # if not queue.isempty():
#         # 模拟发送请求
#         #  避免重复抓取 ，把 url  放到 队列里
#         # requests.get(url)
#             print(i)
#
# def main():
#     t1 = threading.Thread(target=test)
#     t2 = threading.Thread(target=test)
#
#     t1.start()
#     t2.start()
#
# main()
# #
#
#
#
import threading
from queue import Queue

# queue = Queue()
# for i in range(1, 6):
#     queue.put(i)
# # print(queue)
#
# def  test():
#     while  not queue.empty():
#         print(queue.get())
#
# t1 = threading.Thread(target=test)
# t2 = threading.Thread(target=test)
# t1.start()
# t2.start()
queue = Queue()
for i in range(1,13):
    url = 'https://www.qiushibaike.com/8hr/page/{}/'.format(str(i))
    queue.put(url)
def  test():
    while not queue.empty():
        print(queue.get())

t1 = threading.Thread(target=test)
t2 = threading.Thread(target=test)
t1.start()
t2.start()
