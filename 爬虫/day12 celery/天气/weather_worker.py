"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/10/23'
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
'''
先获取一个地方的气温
'''
from celery import Celery
from lxml import etree
import requests

uri1 = 'redis://:123456@127.0.0.1:6379/3'
uri2 = 'redis://:123456@127.0.0.1:6379/4'
app = Celery('tasks',  backend=uri1, broker=uri2) #配置好celery的backend和broker

@app.task
def crawl(location, url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    html = etree.HTML(response.content)
    #print(etree.tostring(html, pretty_print=True).decode())
    temperature = html.xpath('//dd[@class="weather"]/p/b/text()')[0] + '℃'
    print(location,temperature)
    return [location,temperature]



