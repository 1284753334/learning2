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

#   获取一个城市的 航班信息

import requests
import json
import time
import random

headers = {'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}

# 爬取机票
url = 'https://flights.ctrip.com/itinerary/api/12808/products'
headers_post = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    #发送payload 类型的数据
    'content-type': 'application/json',
    'referer': 'https://flights.ctrip.com/itinerary/oneway/can-bjs?date=2019-09-22',
    'cookie': '_abtest_userid=b4ae7640-4395-4a53-993c-fb8050a42cd6; _ga=GA1.2.1151191299.1563862790; _RSG=qY4K5rNxOc24d39glbz.X8; _RDG=2846d858a8b1952291180216ecf3c3f7e3; _RGUID=2998ed7d-4550-48b4-887e-f65bea2439c4; MKT_Pagesource=PC; __utma=1.1151191299.1563862790.1563863166.1563863166.1; __utmz=1.1563863166.1.1.utmcsr=flights.ctrip.com|utmccn=(referral)|utmcmd=referral|utmcct=/itinerary/oneway/can-ctu; appFloatCnt=1; _gid=GA1.2.1057975377.1564131732; _RF1=123.160.227.225; _bfa=1.1563862787857.j8fg0.1.1563960998685.1564131728219.6.15; _bfs=1.2; _jzqco=%7C%7C%7C%7C1564131734766%7C1.1226247120.1563862790603.1564131732942.1564131841029.1564131732942.1564131841029.undefined.0.0.13.13; __zpspc=9.6.1564131732.1564131841.2%234%7C%7C%7C%7C%7C%23; _bfi=p1%3D10320673302%26p2%3D10320673302%26v1%3D15%26v2%3D14',
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
			"dcity": "can",
			"acity": "bjs",
			"dcityname": "广州",
			"acityname": "北京",
			"date": "2019-09-22"
		}
	],
	"selectedInfos": None,
	"army": False,
	"params": [
		{
			"dcity": "BJS",
			"acity": "CAN",
			"date": "2019-07-31",
			"dcityname": "北京",
			"acityname": "广州"
		}
	]
}

#print(payload_data)
response = requests.post(url, data=json.dumps(payload_data), headers=headers_post)
#print(response.text)
with open('./data/can-bjs.txt','w',encoding='utf-8') as file:
    file.write(response.text)
time.sleep(random.random())

# 机票信息的提取
with open('./data/can-bjs.txt','r',encoding='utf-8') as file:
    data = file.read()

ls=json.loads(data)['data']['routeList']
print(len(ls))
for item in ls:
    if 'flightId' in item['legs'][0]:
        flightId = item['legs'][0]['flightId']
        print('flightId:',flightId)
        flightNumber = item['legs'][0]['flight']['flightNumber']
        print('flightNumber:',flightNumber)
        airlineName = item['legs'][0]['flight']['airlineName']
        print('airlineName:', airlineName)
        airlineCode = item['legs'][0]['flight']['airlineCode']
        print('airlineCode:', airlineCode)
        craftTypeName = item['legs'][0]['flight']['craftTypeName']
        print('craftTypeName:', craftTypeName)
        craftTypeCode = item['legs'][0]['flight']['craftTypeCode']
        print('craftTypeCode:', craftTypeCode)
        craftKind = item['legs'][0]['flight']['craftKind']
        print('craftKind:', craftKind)
        craftTypeKindDisplayName = item['legs'][0]['flight']['craftTypeKindDisplayName']
        print('craftTypeKindDisplayName:', craftTypeKindDisplayName)
        departureCityTlc = item['legs'][0]['flight']['departureAirportInfo']['cityTlc']
        print('departureCityTlc:', departureCityTlc)
        departureCityName = item['legs'][0]['flight']['departureAirportInfo']['cityName']
        print('departureCityName:', departureCityName)
        departureAirportTlc = item['legs'][0]['flight']['departureAirportInfo']['airportTlc']
        print('departureAirportTlc:', departureAirportTlc)
        departureAirportName = item['legs'][0]['flight']['departureAirportInfo']['airportName']
        print('departureAirportName:', departureAirportName)
        departureTerminalId = item['legs'][0]['flight']['departureAirportInfo']['terminal']['id']
        print('departureTerminalId:', departureTerminalId)
        departureTerminalName = item['legs'][0]['flight']['departureAirportInfo']['terminal']['name']
        print('departureTerminalName:', departureTerminalName)
        departureTerminalShortName = item['legs'][0]['flight']['departureAirportInfo']['terminal']['shortName']
        print('departureTerminalShortName:', departureTerminalShortName)
        departureDate = item['legs'][0]['flight']['departureDate']
        print('departureDate:', departureDate)
        arrivalCityTlc = item['legs'][0]['flight']['arrivalAirportInfo']['cityTlc']
        print('arrivalCityTlc:', arrivalCityTlc)
        arrivalCityName = item['legs'][0]['flight']['arrivalAirportInfo']['cityName']
        print('arrivalCityName:', arrivalCityName)
        arrivalAirportTlc = item['legs'][0]['flight']['arrivalAirportInfo']['airportTlc']
        print('arrivalAirportTlc:', arrivalAirportTlc)
        arrivalAirportName = item['legs'][0]['flight']['arrivalAirportInfo']['airportName']
        print('arrivalAirportName:', arrivalAirportName)
        arrivalTerminalId = item['legs'][0]['flight']['arrivalAirportInfo']['terminal']['id']
        print('arrivalTerminalId:', arrivalTerminalId)
        arrivalTerminalName = item['legs'][0]['flight']['arrivalAirportInfo']['terminal']['name']
        print('arrivalTerminalName:', arrivalTerminalName)
        arrivalTerminalShortName = item['legs'][0]['flight']['arrivalAirportInfo']['terminal']['shortName']
        print('arrivalTerminalShortName:', arrivalTerminalShortName)
        arrivalDate = item['legs'][0]['flight']['arrivalDate']
        print('arrivalDate:', arrivalDate)
        cabinsList = item['legs'][0]['cabins']
        print(len(cabinsList))

        for item1 in cabinsList:
            cabinClass = item1['cabinClass']
            print('cabinClass:', cabinClass)
            price = item1['price']['price']
            print('price:', price)
            seatCount = item1['seatCount']
            print('seatCount:', seatCount)
        print('='*200)


