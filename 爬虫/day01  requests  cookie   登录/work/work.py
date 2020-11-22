'''

level
1:
1、阅读课件
2、 什么是
http
协议？
HTTP
超文本传输协议，是互联网上应用最为广泛的网络协议，是基于TCP / IP通信协议来传输数据，一个属于应用层的协议。

3、 http
和
https
的区别？
https
是http的安全版，在http下加入SSL层
SSL(安全套接层)
主要用于wab的安全传输协议，在传输层对网络连接进行加密，保障在internet上传输信息的安全
HTTP的端口号为
80
HTTPS的端口号为443

4、 如何审查页面元素？
可从浏览器中查看网页代码，在任意界面单击页面右键选择检查，也就是审查元素。
5、 get
方法和
pos
方法的区别？
1、在浏览器的域名栏，get请求显示请求的参数信息，而post请求不显示，参数信息显示在network
中data_form中
2、GET产生一个TCP数据包；POST产生两个TCP数据包。
3、GET请求在URL中传送的参数是有长度限制的，而POST么有。
4、对参数的数据类型，GET只接受ASCII字符，而POST没有限制。
6、 常见的状态码有哪些？
下面是常见的HTTP状态码：

200 - 请求成功
301 - 资源（网页等）被永久转移到其它URL
404 - 请求的资源（网页等）不存在
500 - 内部服务器错误

7、什么是爬虫？爬虫有哪些分类？
爬虫是按照一定的规则，自动地抓取互联网信息的程序或者脚本
分类
通用网络爬虫（抓取网页）
聚焦爬虫  （信息筛选）
增量式抓取  （维护网页集合）
深度爬虫    （递归爬取）
'''
'''

8、 数据爬取的步骤有哪些？
网页抓取，数据提取，数据存储
9、案例：百度模拟搜索“长城”
import requests

wd = {"wd": "长城"}
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
try:
    reponse = requests.get(url="http://baidu.com/s?", headers=head, timeout=0.45, params=wd)
except Exception as e:
    print(e)
# print(reponse.text)
print(reponse.content.decode(reponse.apparent_encoding))

10、案例：有道翻译模拟翻译
"Computer"
import requests
import json
import pprint

head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

form_data = {"i": "Computer",
             "from": "AUTO",
             "to": "AUTO",
             "smartresult": "dict",
             "client": "fanyideskweb",
             "salt": "15674273328128",
             "sign": "ea0289bbe84561c958aa9a6a4d9b9bdc",
             "ts": "1567427332812",
             "bv": "a4f4c82afd8bdba188e568d101be3f53",
             "client": "fanyideskweb",
             'doctype': 'json',
             "version": "2.1",
             'keyfrom': 'fanyi.web',
             'action': 'FY_BY_CLICKBUTTION',
             'typoResult': "false"
             }

reponse = requests.post(url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule", data=form_data,
                        timeout=0.5, headers=head)
print(reponse.content.decode(reponse.apparent_encoding), type(reponse.content.decode(reponse.apparent_encoding)))
dd = reponse.content.decode(reponse.apparent_encoding)
gg = reponse.json()
print(gg["translateResult"][0][0]["tgt"], gg)
'''

'''
level2:
https://tieba.baidu.com
1、范例： 批量爬取贴吧数据
输入贴吧名称，起始页码，结束页码，爬取贴吧数据，以‘第
x
页.html’命名， 保存为
html
文件
'''
import requests

a = 0
sum = 0
# http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=50
while a < 10:
    sum = sum + a * 50
    heads = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    vm = {'kw': 'python', 'ie': 'utf-8', 'pn': sum}
    # response = requests.get("https://b-ssl.duitang.com/uploads/item/201603/18/20160318232507_cFBfX.thumb.700_0.png", headers = heads)
    response = requests.get("http://tieba.baidu.com/f?", headers=heads)
    print(response.apparent_encoding)
    cc = response.content.decode()

    print(type(cc))
    with open(f'./html/baidu_{a}.html', 'w', encoding='utf-8') as file:
        file.write(cc)

    a = a + 1

'''
2、爬取https: // www.qq.com /
保存页面为，qq.html

#  url 中 不能有空格 
import  requests

url = 'https://www.qq.com/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    'Connection': 'close'
}

response = requests.get(url,headers=headers)
print(response.text)

'''

'''
3、爬取搜狗动漫
http: // kan.sogou.com / dongman /
保存页面为，dongman.html

level
3:
4、爬取4399
http: // www
.4399.com /?haoqqdh,
保存页面为，4399.
html

5、搜狐健康
http: // health.sohu.com /?spm = smpc.home.top - nav
.24
.1550453761461
Q0shOpW
保存页面为，sohuhealth.html

import requests

a = 0

list = ['https://www.qq.com', 'http://kan.sogou.com/dongman/', 'http://www.4399.com/?haoqqdh',
        'http://health.sohu.com/?spm=smpc.home.top-nav.24.1550453761461Q0shOpW', ]
name = ['qq', '搜狗动漫', '4399游戏', '搜狐健康', ]

while a < len(list):
    url = list[a]
    na = name[a]
    heads = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    vm = {'kw': 'python', 'ie': 'utf-8', 'pn': sum}
    # response = requests.get("https://b-ssl.duitang.com/uploads/item/201603/18/20160318232507_cFBfX.thumb.700_0.png", headers = heads)
    response = requests.get(url=url, )
    print(response.apparent_encoding)
    cc = response.content

    print(type(cc))
    with open(f'./html/baidu_{na}.html', 'wb', ) as file:
        file.write(cc)

    a = a + 1

    '''
