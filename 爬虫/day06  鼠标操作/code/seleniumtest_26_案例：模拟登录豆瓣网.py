"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2019/1/13'
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
driver.maximize_window()
driver.get("http://www.douban.com")
#print(driver.page_source)
#driver.find_element_by_xpath('//li[@class="account-tab-account"]').click()

loginframe = driver.find_element_by_xpath('//div[@class="login"]/iframe')
print(driver.page_source)
driver.switch_to_frame(loginframe)

time.sleep(1)
driver.find_element_by_xpath('//li[@class="account-tab-account"]').click()
#输入账号密码
driver.find_element_by_name("username").send_keys("17752558702")
driver.find_element_by_name("password").send_keys("qikuedu9527")

# 模拟点击登录
driver.find_element_by_xpath('//div[@class="account-tabcon-start"]/div[@class="account-form"]/div[@class="account-form-field-submit "]').click()

# 等待3秒
time.sleep(5)

# 生成登陆后快照
driver.save_screenshot("./images/douban.png")
#print(driver.page_source)
with open("./data/douban.html", "w",encoding='utf-8') as file:
    file.write(driver.page_source)

driver.quit()



