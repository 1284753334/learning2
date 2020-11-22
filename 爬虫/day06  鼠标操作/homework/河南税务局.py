'''


案例：河南税务总局爬虫
http://henan.chinatax.gov.cn/003/index.html?NVG=0&LM_ID=1
爬取税务新闻，基层动态，媒体视点中标题，url，发布时间
'''
import re
from time import sleep

from selenium import webdriver

url = 'http://henan.chinatax.gov.cn/003/index.html?NVG=0&LM_ID=1'

browser = webdriver.Chrome()
browser.get(url)

sleep(2)
#  执行页面下拉动作
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# //*[@id="m_tab1"]/div[1]/ul/li[1]/a
browser.find_element_by_xpath("//div[@id='m_tab1']/div/ul/li/a").click()
# browser.find_element_by_xpath("//div[@id='m_tab1'/div[1]/ul/li[1]/a]").click()
sleep(2)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")


#  遇到问题，，不能点击页面下拉
# //*[@id="container"]/div[5]/div/div[3]/div/div[2]/ul
# item = browser.find_element_by_css_selector("div.class='db' > ul.class='m_news m_news_div' li]")
# item = browser.find_element_by_xpath("//ul[@class='m_news m_news_div'//li]")
item = browser.find_element_by_xpath("//*[@id='container']/div[5]/div/div[3]/div/div[2]/ul//li")
# item = browser.find_element_by_xpath("//*[@id='container']/div[5]/div/div[3]/div/div[2]/ul//li]")

# html = browser.current_url

#
# pat = re.compile(r'<ul class="m_news.f_pt30">*?>')
# item = pat.search(html)
print("len:",len(item))
# for li in item:
    # title = item.find_element_by_xpath()