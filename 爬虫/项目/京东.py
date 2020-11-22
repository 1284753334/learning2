#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2020/11/10 23:35:06

@author: Json

        认真大胆      永无BUG
"""

from selenium import webdriver
import time
import random



url ='https://www.jd.com/'

options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome()
driver.maximize_window()  # 窗口最大化

driver.get(url)
# input = driver.find_element_by_css_selector('#key')
input = driver.find_element_by_css_selector('.text')
# input = driver.find_element_by_xpath('//input[@class="text"]')
btn = driver.find_element_by_class_name("button")

input.send_keys('保温杯')
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
    print('title:', title)
    price = info.find_element_by_css_selector('.p-price').text.strip()
    print('price:',price)
    shop = info.find_element_by_xpath('//a[@class="curr-shop hd-shopname"]')
    print('shop:',shop.text)
    comment_num = info.find_element_by_xpath('//div[@class="p-commit"]/strong')
    print('comment_num:',comment_num.text)
    # p_url = info.find_elements_by_xpath("//div[@class='p-name p-name-type-2']//a")
    # for a in p_url:
    #     # print(a)
    #     if a !=None:
    #         a = a.get_attribute("href")
    #     else:
    #         url = '空'
    #     # print('shop_url:',a)
    #     # 进入详情页
    #     # print('len:',len(p_url))
    #
    #     driver.get(a)
    #     title = driver.find_element_by_css_selector('.sku-name')
    #     print('sku_name:', title.text)
    #     try:
    #         weight = driver.find_element_by_xpath('//div[@id="summary-weight"]/div[2]')
    #         if weight != None:
    #             weight = weight.text
    #     except:
    #         weight = '网页未显示'
    #     print('weight:', weight)
    #     type1 = driver.find_element_by_xpath('//div[@class="dd"]//i')
    #     print(type(type1))
    #     # type = ''.join(type)
    #     print('型号有：', type1)
    #
    #     shop_name = driver.find_element_by_xpath('//div[@class="mt"]//a')
    #     print('shop_name:', shop_name.text)
    #     # goods_score = driver.find_element_by_xpath('//span[@class="score-detail"]/em')
    #     # print('goods_score:', goods_score.text)
    #     # score = driver.find_element_by_xpath('//a[@class="score-infor clearfix"]/div//em')
    #     # print(score)
    #     # print('goods_score:',score[0].text)
    #     # print('express_score:',score[1].text)
    #     # print('after_score:',score[2].text)
    #     # goods_comemnt = driver.find_element_by_xpath('//li[@class="current"]/s')
    #     # print('goods-comment：',goods_comemnt)
    #     # desc = driver.find_element_by_xpath('//ul[@class="parameter2 p-parameter-list"]//li/text')
    #     # print('desc:',desc)
    #
    #     print('=' * 40)
    #     # continue
driver.close()
        # driver.quit()







