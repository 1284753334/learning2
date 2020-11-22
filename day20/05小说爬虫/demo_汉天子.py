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
'''
小说爬虫，字体解密

addRule
'''
from selenium import webdriver
from lxml import etree
import re


url = 'https://g.hongshu.com/content/93416/13901181.html'
driver = webdriver.Chrome()
driver.get(url)
#   执行 script 语句  返回的是  数组，，查看它 的值是多少
words = driver.execute_script('return words;')
#  查看网页源码
html = driver.page_source
#  找到包含 content_kw 的span  形式为元组
pat1 = re.compile(r'(<span class="context_kw\d+">.*?</span>)')
# 提取对应的数字
pat2 = re.compile(r'class="context_kw(\d+)"')
def func(m):
    #  拿到span 的内容
    s = m.group(1)
    #  从part2 里查找这个  数字   #  返回数字的  整数值
    index = int(pat2.search(s).group(1))

    return words[index]

html = pat1.sub(func,html)
html = etree.HTML(html)
ls = html.xpath('//div[@class="rdtext"]/p//text()')
#  把列表  链接成一个字符串
content = '\n'.join(ls)
print(content)





#  流程

"""
查看网页源码   ctrl+ u   

另存到 桌面   复制到  ppycharm  

运行次网页源码，去掉url后面的参数，，保留到html前面的url     没有跳转   (本地的文件 )


再  查看  网页源码，  复制 此源码    到 浏览器      运行    发现跳转了    



说明页面里面  包含跳转的信息  


删除  多余的script   查看是否跳转， 是否影响显示  （html后，不带参数）


network   点击  <>  网页源码    open  in  paddel    

点击  {}   美化  页面 显示   

查找 addRule   添加断点  




字 和 content_kw 有一个映射关系，通过断点调试可以 发现 这个关系，，找到这个关系后，，利用seleniun

执行 script 语句，

location   


"""

#



# 爬取    脉脉


'''

把  目标json 的  url  拷贝 下来，，粘贴到  新建的  写字板中， 记下  json id   方便回溯 

一条一条  查找  json   直到  找到  我们 需要的  信息  


如果提取不到 相关的信息，有可能是  json 的 数据结构  不一致，，这时候需要 辨别 不同之处


例如，，通过 if  语句，，把各种情况考虑到，，然后  再提取信息。









'''
