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

import json
import os


headers = {'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}

path = './data'
f_list = os.listdir(path)
#print(f_list)
for filename in f_list:
    # 机票信息的提取
    filepath = './data/'+filename
    #filename='./data/xcjp.txt'
    print('file path:',filepath)
    with open(filepath,'r',encoding='utf-8') as file:
        data = file.read()

    data=json.loads(data)['data']
    if 'routeList' in data:
        ls = data['routeList']
        if ls != None:
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

