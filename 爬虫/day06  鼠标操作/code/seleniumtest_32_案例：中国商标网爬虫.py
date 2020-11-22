"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/8/27'
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
from selenium.webdriver.common.by import By
# WebDriverWait 库，负责循环等待
from selenium.webdriver.support.ui import WebDriverWait
# expected_conditions 类，负责条件触发
from selenium.webdriver.support import expected_conditions as EC
import time

url = 'http://sbgg.saic.gov.cn:9080/tmann/annInfoView/annSearch.html?annNum=1654'
browser = webdriver.Chrome()
wait = WebDriverWait(browser,30)
browser.get(url)
page = 1
while True:
    print('page:',page)
    elem = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="pages"]/table/tbody/tr/td[6]/span'))
    )

    elem = wait.until(
        EC.text_to_be_present_in_element((By.XPATH, '//tr[@class="evenBj"]/td[2]'),'1654')
    )
    # print(browser.page_source)

    ls = browser.find_elements_by_xpath('//tr[@class="evenBj"]')
    print('len:',len(ls))
    if len(ls)>0:
        for item in ls:
            #tds = item.find_elements_by_xpath('./td')
            num = item.find_element_by_xpath('./td[1]').text
            print('序 号:',num)
            ann_num = item.find_element_by_xpath('./td[2]/a').text
            print('公告期号:',ann_num)
            ann_date = item.find_element_by_xpath('./td[3]').text
            print('公告日期:',ann_date)
            reg_num = item.find_element_by_xpath('./td[5]').text
            print('注 册 号:',reg_num)
            company = item.find_element_by_xpath('./td[6]').text
            print('申 请 人:',company)
            brand = item.find_element_by_xpath('./td[7]/*').text
            print('商标名称:',brand)
    try:
        time.sleep(1)
        btn_next = browser.find_element_by_xpath('//*[@id="pages"]/table/tbody/tr/td[8]/a')
        btn_next.click()
        page +=1
    except Exception as e:
        print('over....')
        break;

time.sleep(3)
browser.close()
