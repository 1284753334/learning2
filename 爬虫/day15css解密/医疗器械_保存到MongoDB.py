'''

案例：医疗器械网爬虫(bs4):
http://www.chinamedevice.cn/
爬取大的分类
爬取产品名称，url，封面url，产品类别，批准文号，产品规格，产品说明，生产企业，联系人，联系电话，移动电话，手机，单位地址
数据保存到 mongodb 中



获取 标签中的 文本

.get_text()

'''


import re
#
import pymongo as pymongo
import requests
from bs4 import BeautifulSoup

# url = 'http://www.chinamedevice.cn/'
# def down(url):
#     # url = 'http://www.chinamedevice.cn/'
#     # http://www.chinamedevice.cn/product/1212/1/1.html
#     headers = {
#         'User-Agent': 'http://www.chinamedevice.cn/'
#     }
#
#     response = requests.get(url,headers = headers)
#     html = response.text
#     return  (html,response.url)
#
#
#
# '''
# 获取产品分类
# :return:
# '''
# html,current_url = down(url)
# soup = BeautifulSoup(html,'lxml')
# #  找对了 666   开心
#
# # ls =soup.select('body div.nr_4 div.type ul')
#
# ls =soup.select('body div.nr_4 div.type a.f12 ')
# print(len(ls))
#
#
# for li in ls:
#     #  获取产品分类
#     cate_url = url+li.attrs['href']
#     print('cate_url:',cate_url)
#     # name = li > b[0].string
#     html,current_url = down(cate_url)
#     soup = BeautifulSoup(html,'lxml')
#     '''
#     爬取产品名称，url，封面url，产品类别，批准文号，产品规格，产品说明，生产企业，联系人，联系电话，移动电话，手机，单位地址
#     数据保存到 mongodb 中
#     '''
#     list = soup.select('div.list > ul > li')
#     for plist in list:
#         #  获取详情页面的li标签
#         purl = plist.select('h3 > span > a')[0].get("href")
#         print('purl:',purl)
#         # name = plist.select('h3 > span > a')[0].string
#         # print('name:', name)
#         #  翻页  返回的时一个列表
#         new_page = soup.select('a.fno')
#         print('len:',len(new_page))
#         # lurl = 'http://www.chinamedevice.cn/product/1212/1/'
#         if len(new_page)>0:
#             #  分页
#             # 要匹配的对象1.html'
#             if new_page[0].string=='下一页':
#                 new_page =new_page[0].attrs['href']
#                 pat = re.compile(r'(\d+\.html)')
#                 new_page = pat.sub(new_page,current_url)
#                 print('new_page:',new_page)
#
#             html = down(new_page)
#             response = BeautifulSoup(html,'lxml')


# 运用函数  调用，，，处理 逻辑复杂的  爬虫

'''
爬虫写完后，封装成函数，或者类，要不然 不太容易懂
'''

def down(url):
    # url = 'http://www.chinamedevice.cn/'
    # http://www.chinamedevice.cn/product/1212/1/1.html
    headers = {
        'User-Agent': 'http://www.chinamedevice.cn/'
    }

    response = requests.get(url,headers = headers)
    html = response.text
    return  (html,response.url)

def get_cates():
    '''
    获取分类
    :return:
    '''
    url = 'http://www.chinamedevice.cn/'
    html, current_url = down(url)
    soup = BeautifulSoup(html, 'lxml')
    #  找对了 666   开心

    # ls =soup.select('body div.nr_4 div.type ul')

    ls = soup.select('body div.nr_4 div.type a.f12 ')
    print(len(ls))
    for li in ls:
        #  li.attrs   拼接分类的  url
        cate_url = url + li.attrs['href']
        print('cate_url:', cate_url)
        # 拼接后，再次下载，，进入详情页面。在下面
        get_products(cate_url)


def get_products(cate_url):
    '''
    分类列表
    :param cate_url:
    :return:
    获取当前页面的url,为了拼接  新的url,进行解析
    '''
    html, current_url = down(cate_url)
    soup = BeautifulSoup(html, 'lxml')
    list = soup.select('div.list > ul > li')
    print(len(list))
    t = 0
    for plist in list:
        #  获取详情页面的li标签
        purl = plist.select('h3 > span > a')[0].get("href")
        print('purl:', purl)
        t +=1
        print(t)
        get_products_info(purl)


        #         翻页
        #  翻页  返回的时一个列表
    new_page = soup.select('a.fno')
    print(len(new_page))
    # print('len:', len(new_page))
    # lurl = 'http://www.chinamedevice.cn/product/1212/1/'
    if len(new_page) > 0:
        #  草率了  f12看到的 并一定 是  真的
        new_page = new_page[0]
        #  分页
        # 要匹配的对象1.html'   没有上一页
        #   多看几页，，第一页 没有上一页 ，，，，第二页有 上一页
        if new_page.string == '下一页':
            new_page = new_page.attrs['href']
            print('下一页：',new_page)
            pat = re.compile(r'(\d+\.html)')
            # re替换
            new_page = pat.sub(new_page, current_url)
            print('new_page:', new_page)
            get_products(new_page)




def get_products_info(url):
    '''
    获取指定类别的医疗器械
    不用简表，，系统会自动创建
    '''
    html, current_url = down(url)
    soup = BeautifulSoup(html, 'lxml')
    '''
    产品名称，url，封面url，产品类别，批准文号，产品规格，产品说明，生产企业，联系人，联系电话，移动电话，手机，单位地址
数据保存到 mongodb 中

    '''
    name = soup.select("div #main a")[1].get('title')
    print('name:',name)

    product_url = soup.select("div #main a")[1].get('href')
    print('href:',product_url)

    pic_url = soup.select("div #main  dd  a  ")[0].attrs['href']
    print('pic_href:', pic_url)

    product_type = soup.select('div.text01  li')[1].get_text()
    print('product_type:',product_type)
    # print(type(product_type))

    green_nums = soup.select('div.text01 li')[3].get_text()
    print('agreen_nums:',green_nums)

    product_size = soup.select('div.text01 li')[4].get_text()
    print('product_size:', product_size)
    # 产品说明  遇到问题了，格式不统一，有 div   有 p
    #  利用 content   遍历每一个 节点
    # desc = soup.select_one('dd.text03 > div').get_text()
    #  按照属性来查找，标签可以省略
    desc = soup.select_one('dd.text03').get_text()
    print('product_desc:',desc.strip())

    com = soup.select_one('.text04 li[class = "bgwhite pt"] a').get_text()
    print('com:',com)

    connecter = soup.select('.text04 li')[2].get_text()
    print('connecter:',connecter)
    phone = soup.select('.text04 li[class = "bgwhite"]')[1].get_text()
    print('phone:',phone)
    chuanzhen = soup.select('.text04 li')[6].get_text()
    print('chuanzhen:',chuanzhen)

    email = soup.select('.text04 li')[7].get_text()
    print('email:', email)

    web = soup.select('.text04 li')[8].get_text()
    print('web:',web)

    address = soup.select('.text04 li')[9].get_text()
    print('address:', address)
    print('*'*40)

    '''
    存储
    '''
    item = {}
    item['name'] = name
    item["product_url"] = product_url
    item["pic_url"] = pic_url
    item[" product_type"] = product_type
    item["green_nums "] = green_nums
    item["product_size"] = product_size
    item["desc"] =  desc
    item["com1"] = com
    item["connecter"] = connecter
    item[" phone"] =  phone
    item["chuanzhen "] = chuanzhen
    item["email"] = email
    item[" web1 "] =  web
    item["address"] = address
    collec_ylqx.insert_one(item)




def  get_collection():
    '''
      获取指定集合
    '''
    # 单词敲错，主机无法解析，无法保存s
    server = 'localhost'
    port = 27017
    #  若没有密码验证，可省略后三项

    '''
    dbname = ''
    user = ''
    pwd = ''
    '''
    client = pymongo.MongoClient(server, port)

    #     若需要密码验证（设置了密码）
    #     uri = 'mongodb://'+user+":"+pwd+'@'+server+":"+port+'/'+dbname
    #     client = pymongo.MongoClient(uri)
    #   指定数据库  不需要去创建集合
    mdb = client['dbylqx']

    collec_ylqx = mdb['dbylqx']

    return collec_ylqx

#
#
#
if __name__ == '__main__':
    collec_ylqx = get_collection()
    get_cates()


