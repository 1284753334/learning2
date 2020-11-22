'''

案例：贴吧爬虫
https://tieba.baidu.com
需求：制作爬虫爬取指定贴吧一定页码范围的的图片
输入：起始页码，结束页码，贴吧名称
提取帖子访问量，标题，链接，作者，保存到tieba.csv文件

'''
import codecs
import csv
import time
from random import random

import requests
from lxml import etree

url = 'https://tieba.baidu.com/f?'

headers  = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
}

name = input("请输入贴吧的名字：")
start_page = int(input("请输入起始页码："))
last_page = int(input("请输入最后一页页码："))
#

def download(url):

    return requests.get(url,params=params,headers=headers)

for page in range(start_page,last_page+1):
    pn = (page-1)*50
    params = {
        'kw':name,
        'ie':'utf-8',
        'tp':pn

    }

    response = download(url)
    #  解析网页源码
    html = response.text
    # print(html)
    # print('ok')
     # 将字符串类型的网页源码  转换为 Element  对象 进行 xpath  提取
    html = etree.HTML(html)
    '''
    案例：贴吧爬虫
    https://tieba.baidu.com
    需求：制作爬虫爬取指定贴吧一定页码范围的的图片
    输入：起始页码，结束页码，贴吧名称
    提取帖子访问量，标题，链接，作者，保存到tieba.csv文件
    '''
    #  '//li[contains(@class,"j_thread_list")]'
    ls =  html.xpath('//li[contains(@class,"j_thread_list")]')
    print(len(ls))
    t = 0
    for each in ls:
        nums = each.xpath(".//span[@class ='threadlist_rep_num center_text']/text()")[0]
        print ('nums:',nums)
        # 标题
        title = each.xpath(".//a[@class ='j_th_tit ']/text()")[0]
        print("title:",title)
        # url
        url1 = each.xpath(".//a[@class ='j_th_tit ']/@href")[0]
        detail_url = 'https://tieba.baidu.com/'+url1
        print('datail_url:',detail_url)
        #  作者
        writter = each.xpath(".//span[@class ='frs-author-name-wrap']/a/text()")[0]
        print('作者：',writter)
        print('*'*39)
        print("t:",t)
        time.sleep(random())
        with codecs.open('./data/tieba_'+name+".csv",'a',encoding='utf-8') as f:
            wr = csv.writer(f)
            wr.writerow([nums+','+title+','+detail_url+','+writter])
        #  进入详情页面

        detail_uri = download(detail_url).text
        html2 = etree.HTML(detail_uri)
        pictures = html2.xpath("//img[@class='BDE_Image']/@src")
        for image_datail in pictures:
        # list = html2.xpath('//div[@class="l_post j_l_post l_post_bright  "]')
        # print("len:",len(list))
        # # print("&"*50)
        # for  i in list:
        #     picture = i.xpath(".//img[@class='BDE_Image']/@src")
        #     if len(picture)>0:
        #         picture =picture[0]
        #     else:
        #         picture =0
        #     print('src:',picture)
            img = download(image_datail)

            with open('./data/img'+name+"_"+str(t)+'tieba.jpg','wb')   as  f:
                # wr = csv.writer(f)
                # wr.writerow([nums,title,detail_url,writter])
                f.write(img.content)
                t+=1
                print("&" * 50)

'''
第二次 请求的时候  直接找 含有 地址的列表，，然后 遍历列表，，，保存图片  

可不可以用到 第一次中呢   

'''




