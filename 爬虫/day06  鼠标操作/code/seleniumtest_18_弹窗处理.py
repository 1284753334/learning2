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
driver.get("http://sahitest.com/demo/alertTest.htm")
time.sleep(3)
driver.find_element_by_name("b1").click()
#time.sleep(3)
al = driver.switch_to_alert()
time.sleep(3)
al.accept()
time.sleep(3)
driver.close()






