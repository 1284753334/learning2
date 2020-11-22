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
import time
from selenium import webdriver

browser = webdriver.Chrome()
#  打开百度页面
browser.get('https://www.baidu.com')
#  打开空白标签页

# 2
browser.execute_script('window.open()')
print(browser.window_handles)
#  进入第一个标签页
browser.switch_to_window(browser.window_handles[1])
browser.get('https://www.taobao.com')
time.sleep(2)
# 切换到百度页面
#  1
browser.switch_to_window(browser.window_handles[0])
time.sleep(2)
browser.get('https://python.org')

