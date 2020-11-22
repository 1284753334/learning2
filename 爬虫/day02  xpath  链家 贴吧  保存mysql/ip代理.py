

#   代理IP的使用


import requests

headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
}
proxies = {
# 'http':'http://49.70.33.122:9999',
'https':'205.234.39.57:8080',

}
print("前")
# response = requests.get('https://www.baidu.com/',headers=headers)
response = requests.get('https://www.baidu.com/',proxies = proxies)
print('后')
print(response.text)
print(response)
print('能用')
