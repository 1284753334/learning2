import requests

'''
#  参数为  wd  认真点看  别错了

kw = {'wd':'国庆节'}
headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
}

response = requests.get('https://www.baidu.com/s?',params=kw,headers = headers)
print(response.content.decode('utf-8'))
# print(response.text)
print(response.url)
#



'''


# # response = requests.get('https://www.12306.cn/mormhweb')
# headers = {
# 'Connection': 'close'
# }
# response = requests.get('https://kennethreitz.com',headers=headers,verify = False)
# print(response.text)
# # print(response.content.decode('utf-8'))

# 07
# import requests
# response = requests.get('https://kennethreitz.com', verify=True)
# print(response.text)




#  SSL  证书 验证错误 使用 verify= False
# 08.
import requests
import urllib3
urllib3.disable_warnings()
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',}
response = requests.get("https://www.12306.cn/mormhweb/",verify=True)
print(response.content.decode(response.apparent_encoding))


