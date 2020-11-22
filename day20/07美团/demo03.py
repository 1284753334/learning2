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
import base64
import zlib
import json
import datetime

#生成sign
def gen_sign(page):
    str1 = '"areaId=0&cateId=20004&cityName=深圳&dinnerCountAttrId=&optimusCode=10&originUrl=http://sz.meituan.com/meishi/c20004/&page={}&partner=126&platform=1&riskLevel=1&sort=&userId=&uuid=e2d479366fd240f98b32.1565785405.1.0.0"'
    str2 = '"areaId=0&cateId=20004&cityName=深圳&dinnerCountAttrId=&optimusCode=10&originUrl=http://sz.meituan.com/meishi/c20004/pn{}/&page={}&partner=126&platform=1&riskLevel=1&sort=&userId=&uuid=e2d479366fd240f98b32.1565785405.1.0.0"'

    if page == 1:
        s = str1.format(str(page))
    else:
        s = str2.format(str(page),str(page))
    # 二进制编码
    s = s.encode()
    # 二进制压缩
    s = zlib.compress(s)
    # base64编码
    s = base64.b64encode(s)
    # 转为字符串
    s = str(s, encoding='utf-8')
    return s

# 生成token
def gen_token(page):
     ts = int(datetime.datetime.now().timestamp() * 1000)
     token_dict = {
        'rId': 100900,
        'ver': '1.0.6',
        'ts': ts,
        'cts': ts + 100 * 1000,
        'brVD': [1920, 524],
        'brR': [[1920, 1080], [1920, 1040], 24, 24],
        'bI': ['http://sz.meituan.com/meishi/c20004/', ''],
        'mT': [],
        'kT': [],
        'aT': [],
        'tT': [],
        'aM': '',
        #'sign': 'eJyNj0tvozAUhf+Lt0GxeQWI1EXolAlBQADTJhl1QXhTINSYEKj63+uq7aK7ka50Pp97dHT9BoiZgDWPkIYQB64pAWvAL9FyBThAe7aRV7KiaitBZsCB+LenSBIHzuTxD1j/4zUBcYIqPX86PjO+HB6p6Jn7YYmxILH5TJksBApKuzWE/bxs0pIOUbuMLw1k3BcljAWEkAS7VoTsnv+LChCw8gazcqYv3xp9K/152+yjrLMv85ZRuhuTClPXmx88P0uD8TXUtGv/4h0sPSwfCrc45e0Q10avZlWc+mNNjrq1y/3zxiUGFg0jaxV9KlJoPt1c8+je8s1fOwwW+3Np0lfYrmA2C7DwUGd22hjs5x2GUh27tv+Etabig81UHByTKPh0LzpyaHWLySz1BtFpejR40qV5TWhWY+8SJuNJSe63gz1Qh9iXZmHzoeJHoVVdZ7EyyGHv3IwIlddkilTj7GyVeCsl8oGg0xGjVMyPlYb9/UK10VgGvL5plGysrGDw7sD7B7u5oTk='
         'sign':gen_sign(page)
    }
     #二进制编码
     encode = str(token_dict).encode()
     # 二进制压缩
     compress = zlib.compress(encode)
     # base64编码
     b_encode = base64.b64encode(compress)
     # 转为字符串
     token = str(b_encode, encoding='utf-8')
     return token

headers_1 = {
    #'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
    'Accept': 'application/json',
    #'Referer': 'http://sz.meituan.com/meishi/c20004/pn3/'
}

url = 'http://sz.meituan.com/meishi/api/poi/getPoiList'

for page in range(1,6):
    print('page:',page)
    headers_1 = headers_1.copy()
    headers_1['Referer']='http://sz.meituan.com/meishi/c20004/pn%s/'%(page)
    #print(headers_1)
    params = {
        'cityName': '深圳',
        'cateId': '20004',
        'areaId': 0,
        'sort': '',
        'dinnerCountAttrId': '',
        'page': 3,
        'userId': '',
        'uuid': 'e2d479366fd240f98b32.1565785405.1.0.0',
        'platform': 1,
        'partner': 126,
        'originUrl': 'http://sz.meituan.com/meishi/c20004/pn%s/'%(page),
        'riskLevel': 1,
        'optimusCode': 10,
        '_token': gen_token(page)
        #'_token': 'eJyNj0tvozAUhf+Lt0GxeQWI1EXolAlBQADTJhl1QXhTINSYEKj63+uq7aK7ka50Pp97dHT9BoiZgDWPkIYQB64pAWvAL9FyBThAe7aRV7KiaitBZsCB+LenSBIHzuTxD1j/4zUBcYIqPX86PjO+HB6p6Jn7YYmxILH5TJksBApKuzWE/bxs0pIOUbuMLw1k3BcljAWEkAS7VoTsnv+LChCw8gazcqYv3xp9K/152+yjrLMv85ZRuhuTClPXmx88P0uD8TXUtGv/4h0sPSwfCrc45e0Q10avZlWc+mNNjrq1y/3zxiUGFg0jaxV9KlJoPt1c8+je8s1fOwwW+3Np0lfYrmA2C7DwUGd22hjs5x2GUh27tv+Etabig81UHByTKPh0LzpyaHWLySz1BtFpejR40qV5TWhWY+8SJuNJSe63gz1Qh9iXZmHzoeJHoVVdZ7EyyGHv3IwIlddkilTj7GyVeCsl8oGg0xGjVMyPlYb9/UK10VgGvL5plGysrGDw7sD7B7u5oTk='
    }
    response = requests.get(url, params=params, headers=headers_1)
    print(response.status_code)
    print(response.text)
    print('='*600)
