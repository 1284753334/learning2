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
'''
要 特别小心 
出现iframe  ,,,,直接获取标签，获取不到，，，先进入到 iframe

里面，然后 在获取网页源码


'''

from selenium import  webdriver
import time

#driver = webdriver.Chrome()
opt = webdriver.ChromeOptions() # 创建 chrome 参数对象
opt.set_headless()  # 把 chrome 设置成无头模式，不论 windows 还是 linux 都可以，自动适配对应参数
#options=opt
driver = webdriver.Chrome(chrome_options=opt) # 不制定 options 选项则是普通有头浏览器


driver.maximize_window()
# get方法会一直等到页面被完全加载，然后才会继续程序，通常测试会在这里选择 time.sleep(2)
driver.get("http://sahitest.com/demo/iframesTest.htm")
time.sleep(2)
print(driver.current_url)
#print(driver.page_source)

frames = driver.find_elements_by_tag_name("iframe")
driver.switch_to_frame(frames[0])
print('================================================')
print(driver.page_source)
print(driver.current_url)