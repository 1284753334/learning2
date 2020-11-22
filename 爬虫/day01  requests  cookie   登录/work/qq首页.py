
# 2、爬取https: // www.qq.com /
# 保存页面为，qq.html

#  url 中 不能有空格
import  requests

url = 'https://www.qq.com/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    'Connection': 'close'
}

response = requests.get(url,headers=headers)
print(response.text)

