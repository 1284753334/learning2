#                    _ooOoo_
#                   o8888888o
#                   88" . "88
#                   (| -_- |)
#                   O\  =  /O
#                ____/`---'\____
#              .'  \\|     |//  `.
#             /  \\|||  :  |||//  \
#            /  _||||| -:- |||||-  \
#            |   | \\\  -  /// |   |
#            | \_|  ''\---/''  |   |
#            \  .-\__  `-`  ___/-. /
#          ___`. .'  /--.--\  `. . __
#       ."" '<  `.___\_<|>_/___.'  >'"".
#      | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#      \  \ `-.   \_ __\ /__ _/   .-` /  /
# ======`-.____`-.___\_____/___.-`____.-'======
#                    `=---='
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#             佛祖保佑       永无BUG

import requests
import datetime
import json
from lxml import etree

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
}

def parse(html):
    '''
    数据解析
    :param html:
    :return:
    '''
    html = etree.HTML(html)
    ls = html.xpath('//div[@class="pagelibox"]/div//a[@class="down jsDown jsSeeOriginImage"]/@originurl')
    print('len:', len(ls))
    for link in ls:
        image = requests.get(link, headers=headers).content
        image_name = './images/haibao/' + link.split("/")[-1]
        print('image name:', image_name)
        with open(image_name, 'wb') as file:
            file.write(image)


# 爬取当前页面中的图片
url = 'http://pic.haibao.com/hotimage/'
html = requests.get(url,headers=headers).text
parse(html)


# 模拟ajax请求，进一步的爬取图片
url = 'http://pic.haibao.com/ajax/image:getHotImageList.json'
skip = len(ls)
#skip = 76
page = 1
while page<=10:
    #stamp: Mon Sep 09 2019 09:09:03 GMT 0800 (中国标准时间)
    GMT_FORMAT ='%a %b %d %Y %H:%M:%S GMT 0800'
    stamp = datetime.datetime.utcnow().strftime(GMT_FORMAT)
    stamp += ' (中国标准时间)'
    print('stamp:',stamp)
    new_url = url + '?stamp='+stamp
    data = {
        'skip':skip
    }
    print('page:',page)
    data = requests.post(new_url,data=data,headers=headers).json()
    skip = data['result']['skip']
    html = data['result']['html']
    parse(html)


