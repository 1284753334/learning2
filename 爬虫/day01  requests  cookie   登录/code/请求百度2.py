
'''
爬虫分类：

通用 / 聚焦 /   增量  / 深度 爬虫



爬虫步骤：
网页抓取  数据提取   数据存储


http协议：
应用层  协议     tcp/ip  4 层    7 层 的 是 osi 协议


https    s    位于 传输层


什么是 http 协议   面试题 ？

http协议： 基于 tcp/ip 协议，位于应用层。


https   s  位于传输层。  传输的是  密文。



Requests

原则上 不用 解码


post  get  区别


get  携带参数   ？  键值对


post  提交数据 两种数据
    1. form  地址栏 不显示
    2.  发送 json 数据  poload


数据量

get  有限

post  无限的


'''
# 基本Get 请求  先用response.text   response.content.encoding()

# response.apparent_encoding

import requests

kw = {'wd':'假期'}
headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
}
response = requests.get('https://www.baidu.com/s?',params=kw,headers=headers)
# 查看响应的类型
# print(type(response))
#  查看 内容 response.text，  返回的是Unicode 格式的数据
# 或者response.content  返回的是 字节流

#   非可靠，它是获取请求头里的编码信息，进行解码
# 使用中  先用 text,,,否则(请求头 不放解码信息)，使用 content
# print(response.text)
# response =requests.request('get','https:www.baidu.com/')
#返回页面的源码 是b 字符串  非直接看
# org_code = response.content
# print(org_code)
#  进行解码  同网页源码一致
print(response.content.decode('utf-8'))
viewable_code = response.content.decode('utf-8')
print(viewable_code)
#  获取 网页 编码方式
#  是从 响应头中 获取 编码方式
# print('encoding:',response.encoding)
# #  找不到信息  返回   ISO-8859-1
# #  调用 chardet.detect() 来识别文本编码
# print("appent:",response.apparent_encoding)
# # print(viewable_code)
# # 查看请求状态码
# print(response.status_code)
# # 查看请求 地址
print(response.url)
# #   查看 响应头
# # print(response.headers)
# #  查看请求头
# # print(response.request.headers)
#
# # import  requests




