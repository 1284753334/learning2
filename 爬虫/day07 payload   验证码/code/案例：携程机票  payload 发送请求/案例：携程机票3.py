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
import json
from operator import itemgetter
import time
import random

with open('./data/city.json','r',encoding='utf-8') as file:
    #  字典格式的对象
    city = json.load(file)
print(city)

# 爬取机票   两个城市  代码 不能相同
date_str = '2019-09-20'
for fromcode,fromitem in sorted(city.items()): #根据字典中第一个字段来排序列表, key=itemgetter(0)
    for tocode,toitem in sorted(city.items()):
        if fromcode != tocode:
            count = 3
            while count > 0:
                try:
                    fromcity = fromitem[1]
                    fromid  = int(fromitem[0])
                    tocity = toitem[1]
                    toid = int(toitem[0])
                    print(fromcode,fromcity,fromid,tocode,tocity,toid)
                    url = 'https://flights.ctrip.com/itinerary/api/12808/products'
                    headers_post = {
                        'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)',
                        'content-type': 'application/json',
                        'referer': 'https://flights.ctrip.com/itinerary/oneway/%s-%s?date=%s'%(fromcode.lower(),tocode.lower(),date_str),
                        #'referer': 'https://flights.ctrip.com/itinerary/oneway/can-bjs?date=2019-07-31',
                        'cookie': '_abtest_userid=b4ae7640-4395-4a53-993c-fb8050a42cd6; _ga=GA1.2.1151191299.1563862790; _RSG=qY4K5rNxOc24d39glbz.X8; _RDG=2846d858a8b1952291180216ecf3c3f7e3; _RGUID=2998ed7d-4550-48b4-887e-f65bea2439c4; MKT_Pagesource=PC; __utma=1.1151191299.1563862790.1563863166.1563863166.1; __utmz=1.1563863166.1.1.utmcsr=flights.ctrip.com|utmccn=(referral)|utmcmd=referral|utmcct=/itinerary/oneway/can-ctu; appFloatCnt=1; _gid=GA1.2.163889431.1564276464; _RF1=182.127.11.52; _bfa=1.1563862787857.j8fg0.1.1564133792666.1564276461137.8.18; _bfs=1.2; _jzqco=%7C%7C%7C%7C1564276464134%7C1.1226247120.1563862790603.1564276462786.1564276475584.1564276462786.1564276475584.undefined.0.0.16.16; __zpspc=9.8.1564276462.1564276475.2%234%7C%7C%7C%7C%7C%23; _bfi=p1%3D10320673302%26p2%3D10320673302%26v1%3D18%26v2%3D17',
                    }
                    #print(headers_post)

                    payload_data = {
                        "flightWay": "Oneway",
                        "classType": "ALL",
                        "hasChild": False,
                        "hasBaby": False,
                        "searchIndex": 1,
                        "airportParams": [
                            {
                                "dcity": fromcode,
                                "acity": tocode,
                                "dcityname": fromcity,
                                "acityname": tocity,
                                "date": date_str,
                                }]
                    }
                    #print(payload_data) proxies = {}
                    response = requests.post(url, data=json.dumps(payload_data), headers=headers_post)
                    print(response.text)
                    file_path = './data/'+fromcode.lower()+"_"+tocode.lower()+'.txt'
                    print(file_path)
                    with open(file_path,'w',encoding='utf-8') as file:
                        file.write(response.text)
                    #time.sleep(random.random())
                    break
                except Exception as e:
                    print('error...')
                    count -= 1
                    continue

