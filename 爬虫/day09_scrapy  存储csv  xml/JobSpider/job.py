#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2020/11/20 8:57:56

@author: Json

        认真大胆      永无BUG
"""

from selenium import webdriver
import time
import random

url ='https://www.jd.com/'
driver = webdriver.Chrome()
driver.maximize_window()  # 窗口最大化

driver.get(url)
input = driver.find_element_by_css_selector('#key')
btn = driver.find_element_by_class_name("button")

input.send_keys('无人机')
btn.click()

# 模拟下拉滚动条到浏览器的底部
for i in range(3):
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(random.random())

# 提取商品的名称和价格
goods_ls = driver.find_elements_by_css_selector('.gl-item')
print('len:',len(goods_ls))
for info in goods_ls:
    title = info.find_element_by_css_selector('.p-name.p-name-type-2 a').text.strip()
    price = info.find_element_by_css_selector('.p-price').text.strip()
    print('title:',title)
    print('price:',price)

driver.quit()
