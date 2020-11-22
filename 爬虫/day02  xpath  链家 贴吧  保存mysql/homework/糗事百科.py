'''
level 2:
案例：糗事百科爬虫
需求：http://www.qiushibaike.com/8hr/page/1
获取每个帖子里的用户头像链接、用户姓名、段子标题、点赞次数和评论次数


#  牛逼  plus
'''
import codecs
import csv
import time
from random import random

import  requests
from lxml import etree

url = 'http://www.qiushibaike.com/8hr/page/1'

headers = {
   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
}
for page in range(1,5):
    url = 'http://www.qiushibaike.com/8hr/page/'+str(page)
    response = requests.get(url,headers=headers)
    html = response.text

    # print(html)
    def  Elment(html):
        return etree.HTML(html)

    html = Elment(html)
    ls = html.xpath('//li[contains(@class,"item typs")]')
    # print(len(ls))
    i = 0
    for each in ls:
        #  头像链接
        icon_url = each.xpath(".//a[@class='recmd-user']/img/@src")[0]
        print('icon:',icon_url)
        #  用户名
        username= each.xpath(".//span[@class='recmd-name']/text()")[0]
        print('username:',username)
    #      段子标题、
        title = each.xpath(".//a[@class='recmd-content']/text()")
        if len(title)>0:
            title = title[0]
        else:
            title = None
        print('title:',title)
        # 点赞数
        trumb_nums = each.xpath(".//div[@class='recmd-num']/span[1]")[0]
        #  =
        # print(type(trumb_nums))
        result = etree.tostring(trumb_nums).decode()
        print(result)
        trumb_nums = Elment(result).xpath('.//span/text()')
        if len(trumb_nums)>0:
            trumb_nums = trumb_nums[0]
        else:
            trumb_nums=0
        print('trumb_num:',trumb_nums)
     #评论数
        try:
            comment_nums = each.xpath(".//div[@class='recmd-num']/span[4]")[0]
            result = etree.tostring(comment_nums).decode()
            comment_nums = Elment(result).xpath('.//span/text()')
            if len(comment_nums)>0:
                comment_nums = comment_nums[0]
            else:
                comment_nums = 0
        except:
            comment_nums = 0
        print('comment_nums',comment_nums)
        print("*"*40)
        time.sleep(random())
#        数据保存
        with codecs.open("./data/糗事.csv",'a',encoding='utf-8') as file:
            #  生成一个写的对象
            wr =csv.writer(file)
            # txt 是拼接   csv  是 列表
            wr.writerow([title,icon_url,username,trumb_nums,comment_nums])
            i = i + 1
            print(i)





'''
糗事百科 

难点 ，获取 好笑数 和 评论数   看起来获取的是 数字  
其实  打印的  是  lxml对象   需要 转换成 字符串  

然后 发现里面是 span  标签   在  转换 对象   xpath


再对 评论数 进行判断，，长度不为零 就获取，
否则  就为0   

'''
