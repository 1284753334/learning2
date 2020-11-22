
'''
level 3:
案例：链家二手房
https://sh.lianjia.com/ershoufang/
提取标题，链接，单价，总价，基本信息，房源特色信息
保存到mysql数据库


'''
import codecs
import csv
import time
from random import random

import pymysql
import requests
from lxml import etree

start = int(input("请输入起始页码："))
last = int(input("请输入最后一页页码："))

for i in range(start, last + 1):
    if i == 1:
        url = 'https://sh.lianjia.com/ershoufang/'
    else:
        url = 'https://sh.lianjia.com/ershoufang/pg' + str(i)

    # download(url)


    # url = 'https://sh.lianjia.com/ershoufang/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    }


    def download(url):

        response = requests.get(url,headers=headers)
        # print(type(response))
        #  可以直接省略
        html =response.text
        # print(html)
        html = etree.HTML(html)
        return html

    '''
    #      数据保存：
    def save_mysql(*args):
        # 设置mysql连接
        connect = pymysql.connect(
        # IP为本地
        host='localhost',
        # 数据库名
        db='自己的数据库名',
        # 主机名
        user='root',
        # 密码，没有则用空字符串表示
        password='',)
        # 创建游标
        cursor = connect.cursor()
        # 编写数据库语句
        sql = "insert into yao(*args) VALUES (有多少个值就填写多少个%s))"
        # 　　例如：
        # sql = "insert into yao(title,price,store) VALUES(%s,%s,%s)"
        # 判断插入是否成功  参考如下代码
    #     try:
    #         cursor.execute(sql,(*args))
    # # 　　　　例如：
    #         cursor.execute(sql,(*args))
    #         connect.commit()
    #         cursor.close()
    #         connect.close()
    # 　　　　print('数据插入成功')
    # 　　except:
    # 　　　　print('数据插入失败')
    
    '''

    response = download(url)
    list = download(url).xpath('//div[@class = "info clear"]')
    print(len(list))
    t = 0
    for each in list:
        # 标题
        title = each.xpath('.//div[1]/a/text()')[0]
        print('tiele:',title)
        detail_url = each.xpath('.//div[1]/a/@href')[0]
        print('url:',detail_url)
        with codecs.open('./data/链家_' + ".csv", 'a', encoding='utf-8') as f:
            wr = csv.writer(f)
            wr.writerow([title + ',' + detail_url])

        html = download(detail_url)
        # /html/body/div[5]/div[2]/div[3]/span[1]
        # print(type(html))
        # total_price= html.xpath('//div[@class="content"/div[3]/span[1]/text()')
        # total_price= html.xpath('.//span[@class="total"/text()')
        # total_price= html.xpath('.//span[@class="total"/text()')
        #  想省事  直接浏览器 复制粘贴
        total_price= html.xpath('/html/body/div[5]/div[2]/div[3]/span[1]/text()')[0]
        unit= html.xpath('/html/body/div[5]/div[2]/div[3]/span[2]/span/text()')[0]
        print('total_price:',total_price+unit)
        unty_price = html.xpath('/html/body/div[5]/div[2]/div[3]/div[1]/div[1]/span/text()')[0]
        unty_price1 = html.xpath('/html/body/div[5]/div[2]/div[3]/div[1]/div[1]/span/i/text()')[0]

        print('单价：',unty_price+unty_price1)
        with codecs.open('./data/链家_' + ".csv", 'a', encoding='utf-8') as f:
            wr = csv.writer(f)
            wr.writerow([total_price+unit + ',' + unty_price+unty_price1])

        print('基本信息：')
        ls = html.xpath('.//div[@class="introContent"]/div[1]/div[2]/ul/li')
        # huxing = html.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[1]')
        for  ll in ls:
            content = ll.xpath('.//span/text()')[0]
            desc  = ll.xpath('./text()')[0]
            print(content+":"+desc)
            with codecs.open('./data/链家_' + ".csv", 'a', encoding='utf-8') as f:
                wr = csv.writer(f)
                wr.writerow([content + ',' + desc])
        # ls2 = html.xpath(".//div[@class = 'newwrap baseinform']/div[@class=introContent showbasemore]/[contains(@class,'clear')]")
        ls2 = html.xpath(".//div[@class = 'newwrap baseinform']/div[1]/div[contains(@class,'clear')]")
        # print("len:",ls2)
        print('房源特色')
        for e in ls2:
            if e == ls2[0]:
                desc = e.xpath(".//div[1]/text()")[0]
                # content = e.xpath(".//a[1]/text()")[0].strip()+' '+e.xpath(".//a[2]/text()")[0].strip()
                content = e.xpath(".//a/text()")[0].strip()
                print(desc+":"+content)
            else:
                desc = e.xpath(".//div[1]/text()")[0]
                content = e.xpath(".//div[2]/text()")[0].strip()
                print(desc + ":" + content)
                with codecs.open('./data/链家_' + ".csv", 'a', encoding='utf-8') as f:
                    wr = csv.writer(f)
                    wr.writerow([content + ',' + desc])
        print('*' * 20)
        t+=1
        print(t)
        # time.sleep(random())













#  参考如下

#   小结 ：：

# 遇到  提取  一个标签下  要提取 俩个 标签的内容 ，可以使用  //


# 字段 要 一个一个 提取 否则  保存麻烦
'''

import requests
from lxml import etree
import pymysql

def down(url):

    # 请求指定地址的页面
    # :param url:
    # :return:

    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'
    }
    response = requests.get(url,headers=headers)
    return response.content


if __name__ == "__main__":
    conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='123456',db='dblianjia1905')
    cur = conn.cursor()
    for page in range(1,2):
        if page == 1:
            url = 'https://sh.lianjia.com/ershoufang/'
        else:
            url = 'https://sh.lianjia.com/ershoufang/pg'+str(page)+'/'
        print('url：',url)
        html = down(url)
        #print(html.decode('utf-8'))
        html = etree.HTML(html)
        ls = html.xpath('//li[@class="clear LOGVIEWDATA LOGCLICKDATA"]//div[@class="title"]/a/@href')
        print('len:',len(ls))
        for each in ls:
            print('detail url:',each)
            detail_html = down(each)
            detail_html = etree.HTML(detail_html)
            # 数据提取
            title = detail_html.xpath('//h1[@class="main"]/text()')[0]
            print('title:',title)
            total_price = detail_html.xpath('//div[@class="price "]/span[@class="total"]/text()')[0]
            print('total price:',total_price)
            total_unit = detail_html.xpath('//div[@class="price "]/span[@class="unit"]/span/text()')[0]
            print('total unit:',total_unit)
            unit_price = detail_html.xpath('//span[@class="unitPriceValue"]/text()')[0]
            print('unit price:',unit_price)
            unit = detail_html.xpath('//span[@class="unitPriceValue"]/i/text()')[0]
            print('unit:',unit)
            name = detail_html.xpath('//a[@class="info "]/text()')[0]
            print('name:',name)
            region = detail_html.xpath('//div[@class="areaName"]/span[@class="info"]//text()')
            region = ''.join(region)
            print('region:',region)
            bases = detail_html.xpath('//div[@class="base"]/div[@class="content"]//li')
            print('bases lens:',len(bases))
            roomtype = bases[0].xpath('./text()')[0]
            print('roottype:',roomtype)
            floor = bases[1].xpath('./text()')[0]
            print('floor:', floor)
            area = bases[2].xpath('./text()')[0]
            print('area:', area)
            roomstruct = bases[3].xpath('./text()')[0]
            print('roomstruct:', roomstruct)
            withinarea = bases[4].xpath('./text()')[0]
            print('withinarea:', withinarea)
            buildingtype = bases[5].xpath('./text()')[0]
            print('buildingtype:', buildingtype)
            rootdir = bases[6].xpath('./text()')[0]
            print('rootdir:', rootdir)
            buildstruct = bases[7].xpath('./text()')[0]
            print('buildstruct:', buildstruct)
            decorate = bases[8].xpath('./text()')[0]
            print('decorate:', decorate)
            elvator = bases[9].xpath('./text()')[0]
            print('elvator:', elvator)
            hasevlator = bases[10].xpath('./text()')[0]
            print('hasevlator:', hasevlator)
            interest = bases[11].xpath('./text()')[0]
            print('interest:', interest)
            print('='*200)
            # 数据存储
            strsql = 'insert into tblianjia VALUES (0,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            params = [title,each,total_price,total_unit,unit_price,unit,name,region,roomtype,floor,area,roomstruct,withinarea,buildingtype,rootdir,buildstruct,decorate,elvator,hasevlator,interest]
            cur.execute(strsql,params)
            conn.commit()

    cur.close()
    conn.close()





'''