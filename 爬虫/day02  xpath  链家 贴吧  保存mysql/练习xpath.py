from lxml import etree

text = '''
<div>
     <ul>
         <li class="item-0"> <a href="link1.html">first item</a> </li>
         <li class="item-1"> <a href="link2.html">second item</a> </li>
         <li class="item-inactive"> <a href="link3.html">third item</a> </li>
         <li class="item-1"> <a href="link4.html">fourth item</a> </li>
         <li class="item-0"> <a href="link5.html">fifth item</a>   # 注意，此
    处缺少一个 </li> 闭合标签
     </ul>
</div>

#利用 etree.HTML，将字符串解析为 HTML 文档
html = etree.HTML(text)
# 按字符串序列化 HTML 文档
result = etree.tostring(html).decode()
print(result)

'''

''''

还可以读取外部的html 文件，转成  str

# lxml_parse.py
from lxml import etree
# 读取外部文件 hello.html
#  元素对象
html = etree.parse('./hello.html')

print(type(html))
# result = etree.tostring(html, pretty_print=True).decode()
# print(result)

#  返回的结果是一个列表

result = html.xpath("//li")
print(result)
print(type(result))
print(len(result))

'''

''''
04
 <li class="item-0"> <a href="link1.html">first item</a> </li>
 <li class="item-1"> <a href="link2.html">second item</a> </li>
 <li class="item-inactive"><a href="link3.html"> <span
class="bold">third item</span> </a></li>
 <li class="item-1"><a href="link4.html">fourth item</a></li>
 <li class="item-0"><a href="link5.html">fifth item</a></li>
'''

from lxml import etree
html = etree.parse('./hello.html')

#

result = html.xpath('//li[1]/a')
# 获取文本内容
result1 = html.xpath('//li[3]/a/span/text()')
result2 = html.xpath('//li/a[@href ="link1.html"]/@href')
# result = html.xpath('//li/a[@class ="link1.html"]')
result3 = html.xpath('//span')
print(result)
# resul =
#  获取标签中的  标签   格式为 字符串
print(etree.tostring(result[0]).decode())
print(result1)
print(result2)
print(type(result))
print(type(result1))