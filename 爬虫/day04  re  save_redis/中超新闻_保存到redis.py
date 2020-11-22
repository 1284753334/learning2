
'''

案例：中超新闻爬虫(re)
http://sports.163.com/zc/
提取新闻标题，url，关键字，评论数
保存到redis中

遇到的问题：  不够细心
 # key_word 意外多了些  html  少了 一个问好  写成  贪婪匹配了
   #   取不到数据，，少写了一个点
'''
import json
import re

import redis
import requests

#  使用re  要使用 网页源码   .text

def  download(url):
    url ='http://sports.163.com/zc/'

    headers  = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    }

    response = requests.get(url,headers=headers)

    html = response.text
    return html
if __name__ == '__main__':
    for page in  range(1,2):
        try:
            #  保存数据 到 redis   建立一个链接
            r = redis.StrictRedis(host = 'localhost',port = 6379,password=123456)
            if page ==1:
                url = 'https://sports.163.com/zc/'
            else:
                if page <= 10:
                    str_page = '0'+str(page)
                else:
                    str_page = str(page)
                url = 'https://sports.163.com/special/00051C89/zc_' + str_page+'.html'
            html = download(url)
            # print(html)
            # str1 = '''<h3><a .*?>(.*?)</a>'''
            #   困难 re  匹配不到  先 匹配一个 items
            #   re.S | re.M  写在不同的位置，表达的意义  不同，，在对象中  这样匹配，尽量写在对象中
            # 获取新闻的条目
            pat_1 = re.compile(r'<div class="news_item">(.*?)<div class="share">',re.S | re.M)
            #title
            pat_2 = re.compile(r'<h3><a .*?>(.*?)</a>', re.S | re.M)
            # url  href 这里多了个空格   导致匹配不到
            pat_3 = re.compile(r'<h3><a href="(.*?)">', re.S | re.M)
            # pat_3 = re.compile(r'<h3>.*?<a href="(.*?)">', re.S | re.M)
            # key_word 意外多了些  html  少了 一个问好  写成  贪婪匹配了
            pat_4 = re.compile(r'<div class="keywords">.*?<a .*?>(.*?)</a>.*?<a .*?>(.*?)</a>', re.S | re.M)

            # comment_nums
            # pat_5 = re.compile(r'<span class="text">(\d+)</span>', re.S | re.M)
            #   取不到数据，，少写了一个点
            pat_5 = re.compile(r'<a.*?class="comment">.*?<span class="icon">(.*?)</span>', re.S | re.M)
            # pat_5 = re.compile(r'<a.*?class="comment">.*?<span.*?class="icon">(.*?)</span>', re.M | re.S)
            # <span class="text">跟帖&nbsp;1251</span>
            obj1 = pat_1.findall(html)
            print(len(obj1))
            for  item in obj1:
                title = pat_2.search(item)
                if title != None:
                    title= title.group(1)
                else:
                    title = None
                print('tit:', title)
                url = pat_3.search(item)
                if url != None:
                    url = url.group(1)
                else:
                    url = None
                print('url:', url)
                key_word = pat_4.search(item)
                if key_word != None:
                    # print("1:",key_word)
                    key_word = key_word.group(1)+','+key_word.group(2)
                else:
                    key_word = None
                print('key_word:', key_word)
                comment_num = pat_5.search(item)
                if comment_num != None:
                    comment_num = comment_num.group(1)
                else:
                    comment_num = 0
                print('comment_num:', comment_num)


                data = {
                    'title':title,
                    'url':url,
                    'key_word':key_word,
                    'url':url
                }
                #  把data  转换成可存储的格式
                #  序列化  成字符串   可存储
                data = json.dumps(data)

                #   插入到 redis
                r.lpush('zc',data)





        except Exception as e:
                print(e)
#
            #
            # pat_4 = re.compile(r'<div class="keywords">.*?<a.*?>(.*?)</a>.*?<a.*?>(.*?)</a>',re.M | re.S)
            # # 匹配跟帖数
            # pat_5 = re.compile(r'<a.*?class="comment">.*?<span.*?class="icon">(.*?)</span>',re.M | re.S)
            # ls = pat_1.findall(html)
            # print('len:',len(ls))
