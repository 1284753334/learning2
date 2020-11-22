#                    _ooOoo_
#                   o8888888o
#                   88" . "88
#                   (| -_- |)
#                   O\  =  /O
#                ____/`---'\____
#              .'  \\|     |//  `.
#             /  \\|||  :  |||//  \
#            /  _||||| -:- |||||-  \
#            |   | \\\  -  /// |   |
#            | \_|  ''\---/''  |   |
#            \  .-\__  `-`  ___/-. /
#          ___`. .'  /--.--\  `. . __
#       ."" '<  `.___\_<|>_/___.'  >'"".
#      | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#      \  \ `-.   \_ __\ /__ _/   .-` /  /
# ======`-.____`-.___\_____/___.-`____.-'======
#                    `=---='
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#             佛祖保佑       永无BUG

from selenium  import webdriver
import time

# url = 'http://henan.chinatax.gov.cn/003/index.html?NVG=0&LM_ID=1'
# url = 'http://ewealth.abchina.com/fund/001713.htm'
driver = webdriver.Chrome()
driver.get(url)
#print(driver.page_source)
ls = driver.find_elements_by_xpath('//div[@id="m_tab1_bd"]/ul/li')
print('len:',len(ls))
results=[]
for item in ls:
    title = item.find_element_by_xpath('./a').get_attribute('title').strip()
    news_url = item.find_element_by_xpath('./a').get_attribute('href')
    pub_date = item.find_elements_by_xpath('.//span[@class="date"]/em')

    print('pub date len:', len(pub_date))
    if len(pub_date) >0:
        #print(pub_date[0].get_attribute('innerHTML'))
        #print(type(pub_date[0]))
        pub_date = pub_date[0].get_attribute('textContent')
    else:
        pub_date = item.find_element_by_xpath('.//span[@class="date"]').text.strip()

    print('title:',title)
    print('newsurl:',news_url)
    print('pub date:',pub_date)
    print('='*200)
    results.append([title,news_url,pub_date])

time.sleep(3)
driver.quit()


