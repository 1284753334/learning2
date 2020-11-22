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
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('http://sahitest.com/demo/mouseover.htm')

write = driver.find_element_by_xpath('//input[@value="Write on hover"]')  # 鼠标移动到此元素，在下面的input框中会显示“Mouse moved”
blank = driver.find_element_by_xpath('//input[@value="Blank on hover"]')  # 鼠标移动到此元素，会清空下面input框中的内容

result = driver.find_element_by_name('t1')

action = ActionChains(driver)
sleep(5)
action.move_to_element(write).perform()  # 移动到write，显示“Mouse moved”
print(result.get_attribute('value'))
sleep(5)
action = ActionChains(driver)
# action.move_to_element(blank).perform()
action.move_by_offset(10, 50).perform()  # 移动到距离当前位置(10,50)的点，与上句效果相同，移动到blank上，清空
print(result.get_attribute('value'))
sleep(5)
action = ActionChains(driver)
action.move_to_element_with_offset(blank, 10, -40).perform()  # 移动到距离blank元素(10,-40)的点，可移动到write上
print(result.get_attribute('value'))

sleep(5)
driver.quit()


