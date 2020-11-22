'''
单字符匹配，多字符匹配，匹配分组，
对文本进行匹配查找的一系列方法
 match 方法：从起始位置开始查找，一次匹配
 search 方法：从任何位置开始查找，一次匹配
 findall 方法：全部匹配，返回列表
 finditer 方法：全部匹配，返回迭代器
 split 方法：分割字符串，返回列表
 sub 方法：替换
1 / 18



'''





import re
'''

# .匹配任意字符(除了\n)
#   返回 match  对象
#  只匹配第一个
ret = re.match(".","@b3=2@abc")
# print(type(ret))
# print(ret.group())

'''

'''

#  匹配列举的字符
ret = re.match("[hH]","hello Python")
print(ret.group())
ret = re.match("[a-zA-Z0-9]","Hello Python")
print(ret.group())

'''

'''

#  匹配数字
ret = re.match("嫦娥\d号","嫦娥3号发射成功")
print(ret.group())
ret = re.match("嫦娥\d号","嫦娥4号发射成功")
print(ret.group())
ret = re.match("嫦娥\d号","嫦娥5号发射成功")
print(ret.group())

ret = re.match("[0-9]","687Hello Python")
print(ret.group())
#  findall  返回一个列表 
ret = re.findall("[0-9]","687Hello Python")
print(ret)
# ['6', '8', '7']



'''


'''
# 匹配单词字符
ret = re.match('\w\w\w\w\w\w\w\w','Hello12_ world')
print(ret.group())

# Hello12_

'''

'''
#匹配非单词字符\W
ret = re.match('\W','#@Hello12_ world')
print(ret.group())
# #
'''


#匹配空白字符\s 在中间
# ret = re.match('\w\w\w\w\w\w\w\w\s\w\w\w\w\w','Hello12_ world')
# print(ret.group())
# str = '2018年12月18日，庆祝改革开放40周年大会在北京人[/p]'
# ret = re.search('2',str)
# print(ret.group())


'''

# * 匹配一个字符0到多次
#  第一个字母大写字母  第二个小写
#   贪婪 *  非贪婪  ？
ret = re.match("[A-Z][a-z]a*","China")
print(ret.group())
ret = re.match("[A-Z][a-z]*?a*","Chinaaaaaaa")
print(ret.group())
ret = re.match("[A-Z][a-z]*?a","Chinaaaaaaa")
print(ret.group())
ret = re.match("[A-Z][a-z]*a","Chinaaaaaaa")
print(ret.group())
# Ch  匹配至少两位
# C  第二位不匹配
# China
# Chinaaaaaaa


'''


'''
# + 匹配前一个元字符1到多次
ret = re.match("[a-zA-Z_]+","__init__")
print(ret.group())
'''


'''
#?匹配前一个元字符0到1次  匹配范围 0-99
ret = re.match("[1-9]?[0-9]","69")
print(ret.group())

'''

'''
#匹配前一个元字符m到n次
ret = re.match("[a-zA-Z0-9_-]{8,20}","2018-07-01")
print(ret.group())
ret = re.match("[a-zA-Z0-9_-]{8,}","2018-07-01")
print(ret.group())
ret = re.match("[a-zA-Z0-9_-]{,20}","2018-")
print(ret.group())
ret = re.match("[a-zA-Z0-9_-]{8,}","2018-")
print(ret.group())
'''




'''
#  边界
# 通过$来确定末尾  匹配邮箱
ret = re.match("^\w{4,20}@163\.com$", "xiaoWang@163.com")
print(ret.group())

ret = re.match("^[1-9]?[0-9]$","72")
print(ret.group())


'''

'''
#引用分组num匹配到的字符串
ret = re.match(r"<(\w+)><(\w+)>.+</\2></\1>", "<html><h1>www.baidu.com</h1></html>")
print(ret.group())

# 命名分组，引用别名为name的分组匹配到的字符串
# ret = re.match("<(?P<name1>\w+)><(?P<name2>\w+)>.*</(?P=name2)></(?P=name1)>", "<html><h1>www.baidu.com</h1></html>")
ret = re.findall("<html><h1>(.*)</h1></html>", "<html><h1>www.baidu.com</h1></html>")
print(ret[0])


'''


'''
模式
re.I 忽略大小写的匹配模式   Ignore
re.S '.' 可匹配任何字符，包括换行符   Space
re.X 冗余模式，忽略正则表达式中的空白和#号的注释  
re.M 多行模式 Muitiply  混合的 多的
'''



''''
s = 'hello World!'
# regex = re.compile("Hello world!", re.I)
# print(regex.match(s).group())

# regex = re.match('[a-zA-Z]*',"Hello world!")
# print(regex.group())  hello
'''



'''
#匹配换行
# s = 
#'''
# first line
# second line
# third line
# '''

#
# regex = re.compile(".+")
# print(type(regex))
# #   未换行，，匹配的是 包含 三个元素的列表
# print(regex.findall(s))
# print(regex.match(s).group())


# <class 're.Pattern'>
# ['first line', 'second line', 'third line']
# first line


# re.S
# regex_dotall = re.compile(".+", re.S)
#
# print(regex_dotall.findall(s))
# # 换行匹配   等于  findall
# print(regex_dotall.match(s).group())

# ['first line\nsecond line\nthird line']
# first line
# second line
# third line


'''


'''
# 高级使用


# 编译模式 生成一个  对象，像函数一样 可以重复 使用
'''

import re
# 将正则表达式编译成 Pattern 对象
pattern = re.compile(r'\d+')
'''
'''
# matcch
import re
pattern = re.compile(r'\d+') # 用于匹配至少一个数字
m = pattern.match('one12twothree34four') # 查找头部，没有匹配
print(m)
m = pattern.match('one12twothree34four', 2, 10) # 从'e'的位置开始匹配，没有
# 匹配
print(m)

m = pattern.match('one12twothree34four', 3, 10) # 从'1'的位置开始匹配，正好
# 匹配
print(m) # 返回一个 Match 对象

print(m.group()) # 可省略 0
print(m.start(0)) # 可省略 0
print(m.end(0)) # 可省略 0
print(m.span(0)) # 可省略 0
# Match 对象



import re
pattern = re.compile(r'\d+') # 用于匹配至少一个数字
m = pattern.match('one12twothree34four') # 查找头部，没有匹配
# print(m)
# m = pattern.match('one12twothree34four', 2, 10) # 从'e'的位置开始匹配，没有
# # 匹配
# print(m)

'''

'''
# search  任意位置     match   起始位置  没有匹配成功  返回 None

import re
pattern = re.compile('\d+')
m = pattern.search('one12twothree34four') # 这里如果使用 match 方法则不匹配
print(m.group())
m = pattern.search('one12twothree34four', 10, 30) # 指定字符串区间
print(m.group())
print(m.span())  # 跨度  即索引，显示  开始 索引，，最后索引  + 1

'''
'''
#  findall 返回列表
import re
pattern = re.compile(r'\d+') # 查找数字
result1 = pattern.findall('hello 123456 789')
result2 = pattern.findall('one1two2three3four4', 0, 10)
result3 = pattern.findall('one1two2three3four4')
print(result1)
print(result2)
print(result3)
'''


'''
import re
pattern = re.compile(r'\d+')
result_iter1 = pattern.finditer('hello 123456 789')
result_iter2 = pattern.finditer('one1two2three3four4', 0, 10)
print(type(result_iter1))
print(type(result_iter2))
print(result_iter2)
print('result1...')
for m1 in result_iter1: # m1 是 Match 对象
 print('matching string: {}, position: {}'.format(m1.group(), m1.span()))
print('result2...')
for m2 in result_iter2:
 print('matching string: {}, position: {}'.format(m2.group(), m2.span()))
'''

#
#
# #  sub  替换
# import re
# #  空格不能省
# p = re.compile(r'(\w+) (\w+)') # \w = [A-Za-z0-9]
# # p = re.compile(r'\d+') # \w = [A-Za-z0-9]
# s = 'hello 123, hello 456'
# print(p.sub(r'hello world', s)) # 使用 'hello world' 替换 'hello 123' 和
# 'hello 456'
# print(p.sub(r'\2 \1', s)) # 引用分组
# def func(m):
#     return 'hi' + ' ' + m.group(2)
# print( p.sub(func, s))
# print (p.sub(func, s, 1)) # 最多替换一次
#
#
# #  sub 的使用
# new_page = '3.html'
# print('下一页：', new_page)
# pat = re.compile(r'(\d+\.html)')
# # re替换
# current_url= 'www.baidu.com?tirba=电影1.html'
# new_page = pat.sub(new_page, current_url)
# print('new_page:', new_page)


'''
import re
str = 'abbbc'
# 贪婪模式
pattern = re.compile(r'ab*') # * 决定了尽可能多匹配 b,结果是 abbb
result = pattern.match(str)
print(result.group())
# 非贪婪模式
pattern = re.compile(r'ab*?') # *? 决定了尽可能少匹配 b，结果是 a
result = pattern.match(str)
print(result.group())
#   re  默认是贪婪的
pattern = re.compile(r'ab+?') # *? 决定了尽可能少匹配 b，结果是 ab
result = pattern.match(str)
print(result.group())
'''

'''


import re
# 贪婪模式
str = "aa<div>test1</div>bb<div>test2</div>cc"
pattern = re.compile(r'<div>.*</div>') #* 决 定 了 尽 可 能 多 匹 配 b, 结 果 是
# <div>test1</div>bb<div>test2</div>
result = pattern.search(str)
print('1:',result.group())
# 非贪婪模式
str = "aa<div>test1</div>bb<div>test2</div>cc"
pattern = re.compile(r'<div>.*?</div>') # *? 决定了尽可能少匹配 b，结果是<div>test1</div>
result = pattern.search(str)
print(result.group())

'''
'''

#  title 标签抓取
from urllib import request
import re
import chardet
def down(url):
     head = {}
     #写入 User Agent 信息
     head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19'
     #创建 Request 对象
     req = request.Request(url, headers=head)
     response = request.urlopen(req)
     html = response.read()
     charset = chardet.detect(html)
     #print(charset)
     #print(charset['encoding'])
     html = html.decode(charset['encoding'])
     return html

if __name__ == "__main__":

    #print('hello')
    html = down("https://fanyi.baidu.com/")
    pat = r'<title>(.*?)</title>'
    ex = re.compile(pat, re.M|re.S) #只取中间的文字
    obj = re.search(ex, html)
    #  获取分组1   加括号就是使用分组了
    title = obj.group(1)
    print(title)

'''


#   抓取  tr  td  中间的数据
# import re
#
#
# if __name__ == "__main__":
#     content = '''
#         <html>
#     <head><title>表格</title></head>
#     <body>
#         <table  border=1>
#             <tr><th>学号</th><th>姓名</th></tr>
#             <tr><td>1001</td><td>李白</td></tr>
#             <tr><td>1002</td><td>杜甫</td></tr>
#         </table>
#     </body>
#     </html>'''
#
#     # 获取<tr></tr>间内容
#     pat_1 = re.compile(r'<tr>(.*?)</tr>')
#     # pat_1 = re.compile(r'<tr>(.*?)</tr>')
#     texts = pat_1.findall(content, re.S | re.M)
#     for m in texts:
#         print(m)
#
#     # 获取<th></th>间内容
#     pat_2 = re.compile(r'<th>(.*?)</th>')
#     m_th = pat_2.findall(content, re.S | re.M)
#     for t in m_th:
#         print(t)
#
#     # 直接获取<td></td>间内容
#     pat_3 = re.compile(r'<td>(.*?)</td><td>(.*?)</td>')
#     texts = pat_3.findall(content, re.S | re.M)
#     print(texts)
#     for m in texts:
#         print(m[0], m[1])
#


#   标签中的属性
# import re
#
# content = '''
# <a href="http://map.baidu.com" name="tj_trmap" class="mnav">地图</a>
# <a href="http://v.baidu.com" name="tj_trvideo" class="mnav">视频</a>
# <a href="http://news.baidu.com" name="tj_trnews" class="mnav">新闻</a>
# <a href="http://www.hao123.com" name="tj_trhao123" class="mnav">hao123</a>
# '''
# # re.S  |  re.M  写模式里面  或者 最后都行
#
# # pat = re.compile(r'<a.*?>()</a>')
# pat = re.compile(r'<a.*?href="(.+?)"', re.S | re.M)
# # pat = re.compile(r'<a.*?href="(.+?)"', re.S | re.M)
# urls = pat.findall(content,re.S | re.M)
# print(urls)
# for url in urls:
#     print('1:',url)
#
# #res = r"href=\"(.+?)\"|href=\'(.+?)\'"


#  抓取图片的超链接
import re

content = '''<img alt="Python" src="http://www..csdn.net/eastmount.jpg" />'''
pat = re.compile(r'src="(.*?)"')
urls = pat.search(content).group(1)
print(urls)

#  获取url 的 中文名

#  切分 列表 取值
import re
#
# urls = 'http://www.csdn.net/eastmount.jpg'
# name = urls.split('/')[-1]
# print(name)


#
# str = '[img=145x167]1749b890df794c2.png[/img]'
# pat = re.compile(r'[img.*?](.*?)[')
# content =pat.search(str)
# print(content.group())

# str = "aa<div>test1</div>bb<div>test2</div>cc"


# str = "aa<div>test1</div>"
str = '[img=145x167]1749b890df794c2.png[/img]'
# pattern = re.compile(r'<div>(.*?)</div>') # *? 决定了尽可能少匹配 b，结果是<div>test1</div>
pattern = re.compile(r'\[img.*?\](.*)\[/img\]') # *? 决定了尽可能少匹配 b，结果是<div>test1</div>
result = pattern.search(str)
print(result.group(1))


# pattern = re.compile(r'[img.*](.*)[/img]') # *? 决定了尽可能少匹配 b，结果是<div>test1</div>
# result = pattern.search(str)
# print(result.group(1))
