
import   requests
headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
}
response = requests.get('http://www.renren.com/966924492',headers=headers)
#  获取 Cookie 对象

cookie_obj = response.cookies

# 将cookie_obj 转换为 字典：
print(cookie_obj)


cookies = requests.utils.dict_from_cookiejar(cookie_obj)
print('dict',cookies)














