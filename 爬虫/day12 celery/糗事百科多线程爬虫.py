import json
import threading
from queue import Queue
from lxml import etree
import requests
from fake_useragent import UserAgent
# headers = {
#     'User-Agent':UserAgent().random
# }
#
# print(headers)
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning


'''
在队列的使用过程中，empty()的使用，带括号


'''

disable_warnings(InsecureRequestWarning)

class Crawlinfo(threading.Thread):
    def __init__(self,url_queue,html_queue):
        threading.Thread.__init__(self)
        self.url_queue = url_queue
        self.html_queue = html_queue

    def run(self):
        #         爬虫代码
        ''''
        1.模拟浏览器
        2.请求
        3.数据请求
        4。保存数据
        '''
        headers= {
            'User-Agent':UserAgent().random
        }
        #如果队列不为空
        # print(url_queue)
        while self.url_queue.empty() == False:
            url = self.url_queue.get()
            # 加入 verify,否则会报错
            response = requests.get(url,headers=headers,verify= False )
            if response.status_code == 200:
                self.html_queue.put(response.text)
                # print(response.text)

class ParseInfo(threading.Thread):
    def __init__(self,html_queue):
        threading.Thread.__init__(self)
        self.html_queue = html_queue

    def run(self):
        while self.html_queue.empty() == False:
            e = etree.HTML(self.html_queue.get())
            content = e.xpath('//div[@class="content"]/span[1]')
            with open('duanzi.text','a',encoding='utf-8') as f:
                for span_content in content:
                    info = span_content.xpath('string(.)')
                    # info = json.dumps(info,ensure_ascii=False)
                    f.write(info+'\n')
                    print(info)


if __name__ == '__main__':
    #  创建url 队列
    url_queue = Queue()
    html_queue = Queue()
    base_url ='https://www.qiushibaike.com/text/page/{}/'
    for i  in range(1,14):
        new_url= base_url.format(i)
        url_queue.put(new_url)
    #  把爬虫类，加入到 列表中
    crawl_list = []
    for i in range(3):
        crawl = Crawlinfo(url_queue,html_queue)
        crawl_list.append(crawl)
        crawl.start()
        print('444')
    #  把爬虫解析类，等待一个任务完成，防止主线程退出，任务结束
    for crawl in crawl_list:
        crawl.join()
        # print(crawl.name)

    # 把爬虫解析类，加入到
    # 列表中
    parse_list = []
    for i in range(3):
        parse  = ParseInfo(html_queue)
        parse_list.append(parse)
        parse.start()
    #  join 使主线程阻塞，防止主线程退出，任务结束
    for parse in parse_list:
        parse.join()







#
# # a = []
# # def fun(a):
# #     a.append(1)
# # fun(a)
# # print(a)  # [1]
#
#
#
# # class Single:
# #     def __init__(self,name):
# #         self.name =name
# #     isinstance = None
# #     def __new__(cls, *args, **kwargs):
# #         if Single.isinstance == None:
# #             Single.isinstance = super().__new__(cls)
# #         return Single.isinstance
# #
# #
# # a = Single('校长')
# # b = Single('校')
# # print(a)
# # print(b)
#
#
# class A:
#     def __init__(self,name):
#         self.name = name
#
#     isinstance =None
#     def __new__(cls, *args, **kwargs):
#         if A.isinstance ==None:
#             A.isinstance = super().__new__(cls)
#         return A.isinstance
# a = A('123')
# b= A('124')
# print(id(a))
# # print(id(b))
# a = [i for i in range(10)]
# # print(a)
# A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
# print(A0)
# for s in A0:
#     print(s)
# A3 = [A0[s] for s in A0]
# # print(A3)
# b = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# for s in b:
#     print(s)

#
# class A(object):
#     def go(self):
#         print( "go A go!")
#     def stop(self):
#         print ("stop A stop!")
#     def pause(self):
#         raise Exception("Not Implemented")
#
# class B(A):
#     def go(self):
#         super(B, self).go()
#         print ("go B go!")
#
# class C(A):
#     def go(self):
#         super(C, self).go()
#         print ("go C go!")
#     def stop(self):
#         super(C, self).stop()
#         print ("stop C stop!")
#
# class D(B,C):
#     def go(self):
#         super(D, self).go()
#         print ("go D go!")
#     def stop(self):
#         super(D, self).stop()
#         print ("stop D stop!")
#     def pause(self):
#         print ("wait D wait!")
#
# class E(B,C): pass
#
# a = A()
# b = B()
# c = C()
# d = D()
# e = E()
#
# # 说明下列代码的输出结果
# #
# # a.go()
# # b.go()
# # c.go()
# d.go()
#   新式类 广度优先
# e.go()

# a.stop()
# b.stop()
# c.stop()
# d.stop()
# e.stop()
#
# a.pause()
# b.pause()
# c.pause()
# d.pause()
# e.pause()

