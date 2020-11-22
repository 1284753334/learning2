"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/7/24'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(3) # seconds
first_url = 'http://www.baidu.com/'
driver.get(first_url)
time.sleep(2)
print(driver.title)  # 第一个页面
driver.find_element_by_link_text("新闻").click()
#driver.switch_to_window(driver.window_handles[0])
print(driver.title)  # 第一个页面
#browser.switch_to_window(browser.window_handles[1])
#browser.title  # 最后一个页面
time.sleep(2)
driver.back()  # 从百度新闻后退到百度首页
print(driver.title)  # 第一个页面
time.sleep(2)
driver.forward() # 百度首页前进到百度新闻
print(driver.title)  # 第一个页面
time.sleep(3)
driver.quit()



