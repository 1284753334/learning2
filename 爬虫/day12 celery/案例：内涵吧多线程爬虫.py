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
import requests
from queue import Queue
import threading
import json
import re

class thread_crawl(threading.Thread):
    '''
    抓取线程类
    '''
    def __init__(self, threadID):# 重写构造函数
        threading.Thread.__init__(self) # 调用线程底层的方法
        self.threadID = threadID
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)',
        }

    def run(self):
        print("Starting " + self.threadID)
        self.crawl()
        print("Exiting ", self.threadID)

    def crawl(self):
        while not page_queue.empty():
            page = page_queue.get()
            url = 'https://www.neihan-8.com/article/index_' + str(page) + '.html'
            print('spider:', self.threadID, ',page:', str(page))
            # 多次尝试失败结束、防止死循环
            timeout = 4
            while timeout > 0:
                timeout -= 1
                try:
                    respose = requests.get(url, headers=self.headers,timeout=2.5)
                    data_queue.put(respose.content.decode())
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
        self.file = file

    def run(self):
        print('starting ', self.threadID)
        while not exitFlag_Parser:
            try:
                '''
                调用队列对象的get()方法从队头删除并返回一个项目。可选参数为block，默认为True。
                如果队列为空且block为True，get()就使调用线程暂停，直至有项目可用。
                如果队列为空且block为False，队列将引发Empty异常。
                '''
                item = data_queue.get(False)
                if not item:
                    pass
                self.parse_data(item)
                data_queue.task_done() #提示线程join()是否停止阻塞
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
            pat_item = re.compile(r'<div class="text-column-item box box-790">(.*?<div class="view".*?>.*?</div>)',re.M | re.S)
            ls = pat_item.findall(item)
            print('result len:',len(ls))
            pat_title = re.compile(r'<h3>.*?<a.*?>(.*?)</a>', re.M | re.S)
            pat_url = re.compile(r'<h3>.*?<a.*?href="(.*?)"', re.M | re.S)
            pat_support = re.compile(r'<div.*?class="good".*?>(.*?)</div>', re.M | re.S)
            pat_against = re.compile(r'<div.*?class="bad".*?>(.*?)</div>', re.M | re.S)
            pat_views = re.compile(r'<div.*?class="view".*?>(.*?)</div>', re.M | re.S)
            pat_desc = re.compile(r'<div.*?class="desc".*?>(.*?)</div>', re.M | re.S)
            # pat_title = re.compile(r'', re.M | re.S)
            base_url = 'https://www.neihan-8.com/'
            for item in ls:
                try:
                    title = pat_title.search(item).group(1).strip()
                    print('title:', title)
                    url = base_url + pat_url.search(item).group(1).strip()
                    print('url:', url)
                    suport_nums = pat_support.search(item).group(1).strip()
                    print('suport_nums:', suport_nums)
                    against_nums = pat_against.search(item).group(1).strip()
                    print('against_nums:', against_nums)
                    views_nums = pat_views.search(item).group(1).strip()
                    print('views_nums:', views_nums)
                    desc = pat_desc.search(item).group(1).strip()
                    print('desc:', desc)
                    print('='*60)
                    data = {
                        'title': title,
                        'url': url,
                        'suport_nums':suport_nums,
                        'against_nums': against_nums,
                        'views_nums':views_nums,
                        'desc': desc,
                    }

                    if mutex.acquire():
                        data = json.dumps(data, ensure_ascii=False)
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
    for page in range(2, 12):
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

    # 等待队列清空
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
    if mutex.acquire():
        output.close()


if __name__ == '__main__':

    data_queue = Queue()
    page_queue = Queue(50)
    exitFlag_Parser = False
    mutex = threading.Lock()

    main()




