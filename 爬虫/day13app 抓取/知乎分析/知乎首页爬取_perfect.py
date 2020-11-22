import json
import urllib3
import requests
from lxml import etree


''''

拿到代码，使用的时候，需要  修改 cookie,  改为 登陆后的 cookie
封装成类方法，，方便理解，一类爬取 前六条，后一类，利用抓包，抓取后面的信息 



对于  抓取的字段，需要对其进行判断，可以先把 信息打印出来，然后再写判断条件

一步一步的  调试

'''
 # 直接请求 会让登录，增加的反爬
 # 可以使用抓包
url = 'https://www.zhihu.com/'
#  移除警告信息
requests.packages.urllib3.disable_warnings()
headers = {
    'Cookie' :'_zap=edb3b5be-3191-4b42-ad56-4946e51664e7; d_c0="ALAY9fOPtRGPTgI_JX0RYun9Bg5iu8XKeX8=|1597022216"; _ga=GA1.2.154495460.1597022218; _xsrf=ecbd3356-07c5-44ff-b339-e04ac060fc8c; q_c1=6adf5998f86243daa38cb5a8f9bae90e|1601564859000|1597035262000; tst=r; capsion_ticket="2|1:0|10:1604800279|14:capsion_ticket|44:OGJlN2QzZmM3N2QyNGRkZWFmMGJiZjIyMmI2OGZjMTA=|cbc3a01bc4fa34711bec37184b369db53d32a311e1af6aac4a1138586d883a73"; z_c0="2|1:0|10:1604800353|4:z_c0|92:Mi4xNDN1NURBQUFBQUFBc0JqMTg0LTFFU2NBQUFDRUFsVk5ZZHpPWHdDQ1RlXzMtSEhCX2VOQ29zUkxIcFdMU01Ia3JB|d6da98b92e24f8a01ab48af8c8117ede9ca1d7f394b2d2dc27ef7a7a3467a802"; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1604720871,1604731085,1604747340,1604816984; SESSIONID=Spa7sulsO8mGHOwYtJ5DK4SVqqgpKhH4vOVpCrQvJ6p; JOID=U1AQC0oUyQ4TkKxjLB0g38CrMN85TrRiLePQAlJb-G5Z0eMdeEpZrUWZqGMoT5TN7zNuN0rA6lr9nykLFxvq48o=; osd=Wl8dB0IdxgMfmKVsIREo1s-mPNcwQbluJerfD15T8WFU3esUd0dVpUyWpW8gRpvA4ztnOEfM4lPykiUDHhTn78I=; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1604819280; KLBRSID=cdfcc1d45d024a211bb7144f66bda2cf|1604822273|1604816977',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
}

class Index:
    def __init__(self):
        self.url = url
    def index_6(self):
        response = requests.get(self.url,headers=headers,verify=False)

        html = response.text

        html = etree.HTML(html)

        ls = html.xpath('//div[@class="Card TopstoryItem TopstoryItem--old TopstoryItem-isRecommend"]')
        print('len:',len(ls))
        t = -1
        li = ls[0:7]
        for  i in li:
            print(response.url)
            # 这是一个规律，下面的第一个a 标签的text()
            title= i.xpath('.//h2[@class="ContentItem-title"]//a/text()')[0]
            # if len(title)> 0:
            #     title= title[0]
            # else:
            #     title = '空'
            print('title:',title)
            brief = i.xpath('.//div[@class="RichContent-inner"]/span[1]/text()')
            # if len(content)> 0:
            #     content= content[0].strip()
            # else:
            #     content = '空'
            print('brief:', brief)
            url =i.xpath('.//h2[@class="ContentItem-title"]//a/@href')[0]
            # if len(url )> 0:
            #     url= url [0]
            # else:
            #     url  = '空'
            print('url:',url)
            t +=1
            print('t:',t+1)





class  Second:
    def __init__(self):
        self.page_number = 2
        self.after_id = 5



    def download_second(self):

        url = 'https://www.zhihu.com/api/v3/feed/topstory/recommend'
        for j in range(7,10):
            params = {
                'session_token':'0c6b49c566050fe0d287e449452685e3',
                'desktop':'true',
                'page_number':self.page_number,
                'limit':6,
                'action':'down',
                'after_id':self.after_id,
                'ad_interval':-1,
            }
            self.page_number +=1
            self.after_id +=6

            response = requests.get(url,params=params,headers=headers,verify = False)

            html = json.loads(response.text)['data']
            # print(html)
            for item in html:
                # print(item)
                title = '无'
                if 'target' in item:
                    if 'question' in item['target']:
                        if 'title' in item['target']['question']:
                            title = item['target']['question']['title']
                    elif 'title' in item['target']:
                        title = item['target']['title']
                elif 'title' in item:
                    title = item['title']
                print('title:',title)

                if 'target' in item:
                    if 'description' in item['target']:
                        brief = item['target']['description']
                    elif 'excerpt' in item['target']:
                        brief = item['target']['excerpt']
                print('brief:', brief)


if __name__ == '__main__':
    # url = 'https://www.zhihu.com/'
    Index().index_6()

    Second().download_second()













#
#
#
#
#
#

'''

#  知乎 微博需要登录  可以使用手机端免登录
from selenium import webdriver
import time
import random

url ='https://www.zhihu.com/'
driver = webdriver.Chrome()
driver.maximize_window()  # 窗口最大化

driver.get(url)
# input = driver.find_element_by_css_selector('#key')
# btn = driver.find_element_by_class_name("button")

# input.send_keys('无人机')
# btn.click()

# 模拟下拉滚动条到浏览器的底部
for i in range(3):
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(random.random())



# 提取商品的名称和价格
ls = driver.find_elements_by_css_selector('.Card TopstoryItem TopstoryItem--old TopstoryItem-isRecommend')
print('len:',len(ls))
# for info in ls:
#     title = info.find_element_by_css_selector('.p-name.p-name-type-2 a').text.strip()
#     price = info.find_element_by_css_selector('.p-price').text.strip()
#     print('title:',title)
#     print('price:',price)

driver.quit()

'''













