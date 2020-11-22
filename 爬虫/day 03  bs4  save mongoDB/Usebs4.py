import re

from bs4 import BeautifulSoup
'''

from bs4 import BeautifulSoup
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
#创建 Beautiful Soup 对象  指定 解析器   否则会默认使用 pc 本地的解析器
soup = BeautifulSoup(html,"lxml")
print(type(soup))
#打开本地 HTML 文件的方式来创建对象
#soup = BeautifulSoup(open('index.html'))
#格式化  (方便 查阅)   输出 soup 对象的内容
#  格式化  补齐  闭合的标签

print(soup.prettify())

'''


'''
它将 Html  转换成一个 树形结构，节点 是   对象  共有 bs4  四大对象
  re   bs4    c 语言 写的 ，，速度快  
Tag（标签对象 ）

NavigableString  （  输出 ：标签文本）

BeautifulSoup  （文档）

Comment  （输出：注释 ）

'''
# 用 BeautifulSoup 来获取 Tags
from bs4 import BeautifulSoup
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their
names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie
--></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

'''
#创建 Beautiful Soup 对象
soup = BeautifulSoup(html,'lxml')
print(soup.prettify())
# 输出 文档的  title 字符串
print('soup.title:',soup.title)
# < title > TheDormouse's story</title>
print('soup.head:',soup.head)
#  返回第一个 a 标签
print('soup.a:',soup.a)
#  返回第一个 p 标签
print('soup.p:',soup.p)
print('type(soup.p):',type(soup.p))
# 可以利用 soup 加标签名轻松地获取这些标签的内容
#
# 注意，它查找的是在所有内容中的第一个符合要求的标签。
# 对于 Tag，它有两个重要的属性，是 name 和 attrs
# soup 对象本身比较特殊，它的 name 即为 [document]
print()

#  document  特殊的 标签对象
print('soup.name:',soup.name)
print(soup.head.name) #把 p 标签的所有属性打印输出了出来，得到的类型是一个字典。
# 获取标签内部的文本  子孙 元素的 文本
print(soup.head.string)
print(soup.p.attrs) #根据名称获取对应的属性值，类型为列表
print(soup.p['class'])
print(soup.p.get('class')) # 可以对这些属性和内容等等进行修改
soup.p['class'] = "newClass"
print(soup.p) # 删除属性
del soup.p['class']
'''



'''
#  遍历文档树

soup=BeautifulSoup(html,'lxml')
print(soup.prettify())
# 返回 一个  列表  反回子节点
print(soup.head.contents)
print(soup.head.contents[0])
# print(soup.head.contents[0])

print(soup.body.contents)

for child  in soup.body.contents:
    print(child)

'''

'''

# css 文档选择器
soup = BeautifulSoup(html,'lxml')
# 返回的是一个列表

#  获取列表里的对象 的 文本
#  通过 标签来查找
print(soup.select('title')[0].string)
# 通过类名查找 .
print(soup.select(' .sister')[1].string)
print(soup.select('a.sister')[0].string)
#  通过id 来查找  #
print(soup.select('#link2')[0].string)
#  select_one  获取的是 对象  可以直接  使用 .string
print(soup.select_one('#link2').string)
#   //
print(soup.select("p #link1"))
print(soup.select("body #link1"))

#  查找 子标签 >
print(soup.select("head > title"))
#  查找a 标签
print(soup.select("body > p > a"))
# 查找  id = 2的a 标签
print(soup.select("body > p > a#link2"))
print(soup.select("body > p > #link2"))
# 查找所有的 class=sisiter的元素
print(soup.select("body > p > .sister"))
#




# 按 属性查找

print(soup.select('a[class = "sister"]'))
print(soup.select('a.sister'))
# 指定href 的a 标签
print(soup.select('a[href = "http://example.com/lacie"]')[0])
# p 标签中 所有的  找不到 返回空
print(soup.select('p a[href = "http://example.com/lacie"]')[0])


#  属性获取
print(soup.select_one('a[class = "sister"]'))
tag = soup.select_one('a[class = "sister"]')
print(tag['class'])
print(tag.get('id'))
print(tag.attrs['href'])
'''






'''

' ' 空格   //
>   子节点  / 

'''

inputs = "hello 123 world 456 nihao 789"
_add111 = 111
replacedStr = re.sub("(\d+)",'_add111',inputs, 2)
print(replacedStr)

#  类名中 有 空格的 加 点 .
# By CSS
# <div id="food"><span class="dairy">milk</span><span class="dairy
# aged">cheese</span></div>
# 实现
# cheese = driver.find_element_by_css_selector("#food span.dairy.aged")
