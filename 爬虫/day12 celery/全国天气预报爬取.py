
from celery import Celery
from lxml import etree
import requests

# from celery.schedules import crontab
uri1 = 'redis://:123456@127.0.0.1:6379/2'
uri2 = 'redis://:123456@127.0.0.1:6379/3'
app = Celery('tasks', broker=uri1,backend=uri2)

@app.tasks
def crawl(location,url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
        }

    response = requests.get(url,headers=headers)
    html = etree.HTML(response.content)
    temperature = html.xpath('//dd[@class="weather"]/p/b/text()')[0]+'"C'
    print(location,temperature)
    return [location,temperature]


