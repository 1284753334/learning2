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

#   获取所有的城市
import requests
import json
from operator import itemgetter
import time
import random

headers = {'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}
#城市信息
url = 'https://flights.ctrip.com/itinerary/api/poi/get'
response = requests.get(url,headers=headers)
data = response.json()['data']
del data['热门']

city = {}
def dictParse(data):
    for key1 in data.keys():
        if isinstance(data[key1],dict):
            dictParse(data[key1])
        else:
            if isinstance(data[key1], list):
                for item in data[key1]:
                    temp = item['data'].split('|')
                    city[temp[-1]] = [temp[-2],item['display']]
                    #print(item['data'])

dictParse(data)
print(city)
with open('./data/city.json','w',encoding='utf-8') as file:
    json.dump(city,file)
print(city)



