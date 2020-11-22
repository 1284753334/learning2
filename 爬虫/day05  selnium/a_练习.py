'''


案例：提取京东商品的价格
https://item.jd.com/5089267.html
https://item.jd.com/100008348542.html

#  特点 网页源码（ctrl+u ）里 没有 价格标签,提取不到  动态加载的


'''
import re
import time
from time import sleep

from selenium import webdriver

'''
案例：农业银行国泰基金爬虫
https://ewealth.abchina.com/fund/150010.htm
提取基金名称，涨幅，周涨幅，月涨幅，季涨幅，年涨幅

#  同上个 一样，， 源码  看不到 数据

'''

'''
功能：测试环境配置是否成功
'''
'''

from selenium import webdriver

# browser = webdriver.PhantomJS()  #无头浏览器
browser = webdriver.Chrome()     # 谷歌浏览器
print(type(browser))

browser.get("http://www.baidu.com")  # 请求指定的网页
# 获取网页源码
html = browser.page_source

print(html)
# #   看到网页源码 ，忍不住 用正则  提取一下数据
#  google 浏览器可以请求到  无头浏览器 不可以
# pat = re.compile(r'<html xmlns="(.*?)">',re.S | re.M)
# obj = pat.search(html)
# print(obj.group(1))

browser.close()  # 关闭当前的标签页
browser.quit()  #退出

'''
'''
#  单个元素查找
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://www.taobao.com")
input_first = browser.find_element_by_id("q")
input_second = browser.find_element_by_css_selector("#q")
input_third = browser.find_element_by_xpath('//*[@id="q"]')
print(browser.page_source)
print(input_first)
print(input_second)
print(input_third)
browser.close()
'''


'''
#  多个元素查找
from selenium import webdriver

# 获取商品分类
browser = webdriver.Chrome()
browser.get("https://www.taobao.com")
# 返回的是一个列表
lis = browser.find_elements_by_css_selector('.service-bd li')
print(len(lis))
li_list = browser.find_elements_by_tag_name('li')
print(len(li_list))
class_list = browser.find_elements_by_class_name('service-bd')
print(len(class_list))
xpath_list = browser.find_elements_by_xpath('//div[@class="service J_Service"]')
print(len(xpath_list))
linktext_list = browser.find_elements_by_link_text('美妆')
print(len(linktext_list))
browser.close()

'''

#  获取元素属性
#
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# url = 'https://www.baidu.com/'
# browser.get(url)
# input = browser.find_element_by_id('kw')
# print(input)
# print(input.get_attribute('name'))
# print(input.get_attribute('class'))
# print(input.get_attribute('id'))
# print(input.get_attribute('maxlength'))
# print(input.get_attribute('autocomplete'))
#
# browser.close()



#   获取 文本

#  可见 文本 text
#  隐藏的文本   innerHTML
#  隐藏的文本   innerText

# 获取文本值
# 可见元素文本：text
# Selenium WebDriver 只会不可见元素交互，所以获叏隐藏元素的文本总是会返回空字符串。
# 要获叏隐藏元素的文本。这些内容可以使用
# element.get_attribute('innerHTML'), 会返回元素的内部 HTML， 包含所有的 HTML 标签。
# element.get_attribute('textContent'),只会得到文本内容，而丌会包含 HTML 标签。是

'''
from selenium import webdriver

browser = webdriver.Chrome()
url = 'https://www.baidu.com/'
browser.get(url)
html = browser.page_source
btn = browser.find_element_by_class_name("mnav c-font-normal c-color-t")
# btn = browser.find_element_by_name("tj_trnews")
print(type(btn))
# print(btn.text)
browser.close()
'''
'''
# 用于 获取截图
#  定位到所在的标签
url = 'https://www.baidu.com/'
browser = webdriver.Chrome()
html = browser.get(url)
# print(html)

logo = browser.find_element_by_css_selector('img#s_lg_img')

logo = browser.find_element_by_xpath('//div[@id="lg"]/img[@class="index-logo-src"]')
#  返回的是数字  内部id
print(logo.id)
print(logo.get_attribute('id'))
print(logo.tag_name)
print(logo.location)
print(logo.size)
browser.close()

'''


''''
# js 下滑到底部

# url = 'https://www.zhihu.com/'
url = 'https://www.taobao.com/'
from selenium import webdriver
browser = webdriver.Chrome()
# browser.get("http://www.zhihu.com/explore")
browser.get(url)
print(browser.page_source)
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')
browser.close()

'''

''''''

'''
#  截屏
# 长截屏
driver= webdriver.PhantomJS()
#   普通截屏
# driver= webdriver.Chrome()
driver.maximize_window()
# url = 'https://www.taobao.com/'
# url = 'https://www.baidu.com/'
url = 'https://www.csdn.net/'
driver.get(url)
driver.save_screenshot('./img/aap4.jpg')
'''


'''

# 百度自动化搜索
#   会有bug,提示找不到  标签
driver = webdriver.Chrome()

url = 'https://wwww.baidu.com/'
driver.get(url)
 # 获取搜索框  输入 搜索词
driver.find_element_by_id('kw').send_keys("长城")

sleep(2)
#  找到 搜索按钮 模拟点击
driver.find_element_by_id('su').click()
sleep(2)
# 截屏
driver.save_screenshot("./img/changcheng.jpg")

driver.close()


'''

#  微博登录









