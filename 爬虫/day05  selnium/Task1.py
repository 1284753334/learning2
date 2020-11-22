'''

案例：提取京东商品的价格
https://item.jd.com/5089267.html
https://item.jd.com/100008348542.html

'''

#  指定浏览器
from selenium import webdriver

browser = webdriver.Chrome()
url = 'https://item.jd.com/100008348542.html'
browser.get(url)
#  类名只能使用一个 类名，这里是两个 不能使用  类名
# btn = browser.find_element_by_class_name("price.J-p-100008348542")
# btn = browser.find_element_by_css_selector('span.price.J-p-100008348542')
btn = browser.find_element_by_xpath('//span[@class="price J-p-100008348542"]')
print("price:",btn.text)


browser.close()


