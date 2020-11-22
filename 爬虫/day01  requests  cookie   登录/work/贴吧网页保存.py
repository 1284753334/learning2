''''
1、范例： 批量爬取贴吧数据
输入贴吧名称，起始页码，结束页码，爬取贴吧数据，以‘第
x页.html’命名保存为html文件
'''

# https://tieba.baidu.com/f?kw=python&ie=utf-8&pn=450


#
import time
import  requests
from lxml import etree
import csv,codecs


name = input('请输入贴吧名称：')
start = input('请输入起始页码：')
end = input('请输入结束页码：')
# url =f'https://tieba.baidu.com/f?kw={name}&ie=utf-8&pn='
url ='https://tieba.baidu.com/f?'

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
}
for page in range(int(start),int(end)+1):

    pn = (page-1)*50
    params = {
        'kw': name,
        'ie': 'utf-8',
        'pn':pn,
    }


    # # request = requests.get(url+'sum',headers = headers)
    # request=requests.get(url,params=params,headers = headers)
    # html =request.text

    response = requests.get(url,params=params,headers=headers)
    html = response.text
    #把 字符产 转为 Element  对象



    #  会员置顶： class=" j_thread_list thread_top j_thread_list clearfix"

    #  置顶：     class=" j_thread_list thread_top j_thread_list clearfix"

    # li   class " j_thread_list clearfix"
    # html = etree.HTML(response)
    # ls = html.xpath('//li[contains(@class,"j_thread_list clearfix")]')
    # print('len:',len(ls))
    # print(html)



    # 文件保存
    # # time.sleep(5)
    # filname =f'第{page}页'
    # #  不一定有 这个参数
    # 
    # with open("./page/%s_%s.html"%(filname,name),'w',encoding='utf-8') as f:
    #     n = 1
    #     chunk_size = 1024
    #     for chunk in request.iter_content(chunk_size):
    # 
    #         f.write(chunk)
    #         # loaded_rated = round(loaded * 100, 2)
    #         # print('已经下载{0:}'.format(loaded_rated))
    #         # # time.sleep(5)
    # print('下载完成')

    html = etree.HTML(html)
    ls = html.xpath('//li[contains(@class,"j_thread_list clearfix")]')

    print('len:', len(ls))

    for li in  ls:
        # 标题 链接 作者 时间  回复次数  102
        #   xpath   尽可能的短  ，，，从 目的出发，，精度 很高  一一对应 ，，保证 不会出错
        title = li.xpath('.//a[@class="j_th_tit "]/@title')[0]
        print("title:",title)
       # 链接
        url1 = li.xpath('.//a[@class="j_th_tit "]/@href')[0]
        url = 'https://tieba.baidu.com'+url1
        print("url",url)
      # 作者  102 找父节点
      #   尽量找 a 标签里的数值
        writter1 = li.xpath('.//span[@class="frs-author-name-wrap"]/a/text()')[0]
        print('writter:',writter1)
       # 时间
        pub_time = li.xpath('.//span[@class="pull-right is_show_create_time"]/text()')[0]
        print('time:',pub_time)
        #  回复数
        num = li.xpath('.//div[@class="col2_left j_threadlist_li_left"]/span/text()')[0]
        print('回复:', num)

        print('*'*30)


#  数据存储

# 方式一：txt
        filename = './data/tieba_'+name+".txt"
        # a  添加一次 保存一次 append  追加
        with open(filename,'a',encoding='utf-8') as f:
            f.write(title+","+url+","+writter1+','+num+'\n')

    #  .CSV
        csvfilename = './data/tieba_'+name+".csv"
        with codecs.open(csvfilename,'a',encoding='utf-8') as f:
            #生成一个写的对象
            wr = csv.writer(f)
            wr.writerow([title,url,writter1,num])









'''

import requests
import time
import random
from lxml import etree
import csv
import codecs

headers = {
    'User-Agent':'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'
}

url = 'http://tieba.baidu.com/f'
headers = {
    'User-Agent':'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'
}
# 网页爬取
tiebar_name = input('请输入贴吧名称：')
start_page = int(input('请输入起始的页码：'))
end_page = int(input('请输入结束的页码：'))
# http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=50
for page in range(start_page,end_page+1):
    pn = (page-1)*50
    params = {
        'kw':tiebar_name,
        'ie':'utf-8',
        'pn':pn
    }
    response = requests.get(url,params=params,headers=headers)
    html = response.text
    #print(response.apparent_encoding,response.encoding)
    #html = response.content.decode(response.apparent_encoding,errors='ignore')
    #print(html)
    # filename = './data/第'+str(page)+'页.html'
    # print('保存文件：',filename)
    # with open(filename,'w',encoding='utf-8') as file:
    #     file.write(html)
    # 数据的提取
    
    html = etree.HTML(html)
    ls = html.xpath('//li[contains(@class,"j_thread_list clearfix")]')
    print('len:',len(ls))

'''

