# !/usr/bin/env Python
# coding=utf-8
"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/8/22'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import lxml
import requests
from queue import Queue
import threading
import json
import re

from lxml import etree


class thread_crawl(threading.Thread):
    '''
    抓取线程类
    '''
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)',
        }

    def run(self):
        print("Starting " + self.threadID)
        self.crawl()
        print("Exiting ", self.threadID)

    def crawl(self):
        #  从队列 中 获取 全部   网页 源码    获取4  次
        #  空队列就 执行循环
        while not page_queue.empty():

            page = page_queue.get()
        # for page in page1:
            # url = 'https://www.neihan-8.com/article/index_' + str(page) + '.html'
            # 设置翻页 过程

            if page == 1:
                url = 'https://www.neihanba.com/dz/index.html'
            else:
                url = 'https://www.neihanba.com/dz/list_' + str(page) + '.html'
            print('spider:', self.threadID, ',page页码：：：:', str(page))
            # 多次尝试失败结束、防止死循环
            timeout = 4
            while timeout > 0:
                timeout -= 1
                try:
                    respose = requests.get(url, headers=self.headers,timeout=2.5)
                    data_queue.put(respose.content.decode(encoding='gbk'))
                    # data_queue.put(respose.content.decode())
                    # data_queue.put(respose.content.encoding(cchardet.detect(respose.content)['encoding']))
                    #print(content.text)
                    break
                except Exception as e:
                    print('spider', e)


class Thread_Parser(threading.Thread):
    '''
    页面解析类；
    '''
    def __init__(self, threadID, file):
        threading.Thread.__init__(self)
        self.threadID = threadID
        #  存储使用
        self.file = file

    def run(self):
        print('starting ', self.threadID)
        '''  exitFlag_Parser:  初始值为 False '''
        while not exitFlag_Parser:
            try:
                '''
                调用队列对象的get()方法从队头删除并返回一个项目。可选参数为block，默认为True。
                如果队列为空且block为True，get()就使调用线程暂停，直至有项目可用。
                如果队列为空且block为False，队列将引发Empty异常。
                '''
                #  获取网页源码
                # 非阻塞方式  从  队列 中  获取 网页 源码，，  参数 为False
                item = data_queue.get(False)
                if not item:
                    #  队列 为空，，重新去读取 。否则 解析
                    pass
                self.parse_data(item)
                data_queue.task_done() #提示线程join()是否停止阻塞

            #
            except:
                pass
        print('Exiting ', self.threadID)

    def parse_data(self, item):
        '''
        解析网页函数
        :param item: 网页内容
        :return:
        '''
        try:
            #   re.S  匹配任何字符，包括换行符
            # pat_item = re.compile(r'<div class="text-column-item box box-790">(.*?<div class="view".*?>.*?</div>)',re.M | re.S)
            # pat_item = re.compile(r'<li class="^piclist">(.*?<div class="view".*?>.*?</div>)',re.M | re.S)
            # pat_item = re.compile(r'<li class="^piclist">(.*?)<li>',re.M | re.S)
            # ls = pat_item.findall(item)
            html = etree.HTML(item)
            ls = html.xpath('//ul[@class="piclist longList"]//li')
            print('result len:',len(ls))
            # print('result len:',len(ls))
            # pat_title = re.compile(r'<h4>.*?<b.*?>(.*?)</b>', re.M | re.S)
            # pat_url = re.compile(r'<h4>.*?<a.*?href="(.*?)"', re.M | re.S)
            # pat_support = re.compile(r'<div.*?class="ding dinghover btn".*?>(.*?)</div>', re.M | re.S)
            # pat_against = re.compile(r'<div.*?class="cai caihover btn".*?>(.*?)</div>', re.M | re.S)
            # pat_views = re.compile(r'<div.*?class="view".*?>(.*?)</div>', re.M | re.S)
            # pat_desc = re.compile(r'<div.*?class="desc".*?>(.*?)</div>', re.M | re.S)
            # pat_title = re.compile(r'', re.M | re.S)
            base_url = 'https://www.neihan-8.com/'
            for item in ls:
                try:
                    pass
                    # title = pat_title.search(item).group(1).strip()
                    title = item.xpath('.//h4//text()')[1]
                    print('title:', title)
                    # url = base_url + pat_url.search(item).group(1).strip()
                    url = 'https://www.neihanba.com/'+item.xpath('.//h4/a/@href')[0]
                    print('url:', url)
                    # suport_nums = pat_support.search(item).group(1).strip()
                    suport_nums = item.xpath('.//div[@class="ding dinghover btn"]//span/text()')[0]
                    print('suport_nums:', suport_nums)
                    # against_nums = pat_against.search(item).group(1).strip()
                    against_nums = item.xpath('.//div[@class="cai caihover btn"]//span/text()')[0]
                    print('against_nums:', against_nums)
                    # views_nums = pat_views.search(item).group(1).strip()
                    views_nums = item.xpath('.//span[@class="view"]/em/text()')[0]
                    print('views_nums:', views_nums)
                    # desc = pat_desc.search(item).group(1).strip()
                    # desc = item.xpath('.//h4//div[1]/text()')
                    desc = item.xpath('.//div[@class="f18 mb20"]/text()')[0]
                    print('desc:', desc)
                    print('='*60)
                    data = {
                        'title': title,
                        'desc': desc,
                        'url': url,
                        'suport_nums':suport_nums,
                        'against_nums': against_nums,
                        'views_nums':views_nums,
                    }
                       # 获得锁，，保存文件

                    if mutex.acquire():
                        data = json.dumps(data,ensure_ascii=False)
                        print('save....',data)
                        self.file.write(data + "\n")
                        mutex.release()
                except Exception as e:
                    print('site in result', e)
        except Exception as e:
            print('parse_data', e)


def main():
    output = open('./data/neihanba.json', 'a',encoding='utf-8')
    #初始化网页页码page从2-11个页面
    # 设置   爬取多少页
    for page in range(1, 21):

        page_queue.put(page)
    #初始化采集线程
    crawlthreads = []
    crawlList = ["crawl-1", "crawl-2", "crawl-3"]
    for threadID in crawlList:
        thread = thread_crawl(threadID)
        thread.start()
        crawlthreads.append(thread)
    #初始化解析线程parserList
    parserthreads = []
    parserList = ["parser-1", "parser-2", "parser-3"]
    #分别启动parserList
    for threadID in parserList:
        thread = Thread_Parser(threadID, output)
        thread.start()
        parserthreads.append(thread)

    # 等待 网页队列 清空
    #  这个是主线程  队列不为空，它会一直等待
    while not page_queue.empty():
        pass

    # 等待所有线程完成
    for t in crawlthreads:
        t.join()


    while not data_queue.empty():
        pass

    # 通知线程是时候退出
    global exitFlag_Parser
    exitFlag_Parser = True

    for t in parserthreads:
        t.join()
    print("Exiting Main Thread")
    # 获得锁，把文件给关闭掉
    if mutex.acquire():
        output.close()


if __name__ == '__main__':

    data_queue = Queue()
    page_queue = Queue(50)
    exitFlag_Parser = False
    mutex = threading.Lock()

    main()




