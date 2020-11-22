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
import requests
from lxml import etree
from weather_worker import crawl


class Client:
    def __init__(self):
        self.urls = []
        self.base_url = 'https://www.tianqi.com'

    def getUrls(self):
        url = 'https://www.tianqi.com/chinacity.html'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        html = etree.HTML(response.content)
        ls = html.xpath('//div[@class="citybox"]//a')
        # ls2 = html.xpath('//div[@class="citybox"]//a/text()')
        for item in ls:
            url = self.base_url + item.xpath('@href')[0]
            location = item.text
            self.urls.append((location, url))
        print(self.urls)

    def task_manage(self):
        for url in self.urls:
            pass
            crawl.delay(url[0], url[1])
            # app.send_task('aqicn.crawl', args=(url[0],url[1],))


if __name__ == "__main__":
    client = Client()
    client.getUrls()
    client.task_manage()
