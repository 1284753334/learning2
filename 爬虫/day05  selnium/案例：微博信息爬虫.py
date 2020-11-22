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

from selenium import webdriver
import time
import random


# loginname = '3414018462@qq.com'
# password = 'qikuedu9527'
loginname = '18790579029'
password = 'Hph6927962318'

def login():
    '''
    微博的登陆
    :return:
    '''
    driver = webdriver.Chrome()
    try:
        driver.maximize_window()
        # 加载登录页面
        # url = 'http://www.weibo.com/login.php'
        url = 'http://www.weibo.com/login.php'
        driver.get(url)
        time.sleep(2)
        print('输入用户名...')
        elem_user = driver.find_element_by_id("loginname")
        elem_user.clear()
        elem_user.send_keys(loginname)
        time.sleep(2)
        print('输入密码...')
        elem_pwd =driver.find_element_by_name("password")
        elem_pwd.clear()
        elem_pwd.send_keys(password)
        time.sleep(3)
        print('登陆微博...')
        login_btn = driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a')
        login_btn.click()
        time.sleep(10)
        print(driver.current_url)
        #driver.quit()
        return driver
    except Exception as e:
        print('login error.')
        return None
    return None


def weibo_crawl(driver,url):
    '''
    爬取指定的微博
    :param driver: 
    :param url: 
    :return: 
    '''
    try:
        driver.maximize_window()
        driver.get(url)
        # 返回滚动的高度
        last_height = driver.execute_script('return document.body.scrollHeight;')
        while True:
            print('加载页面...')
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
            # 等待随机的时间
            time.sleep(random.random()*10)
            # 计算新的高度，和原来的高度作比较
            new_height = driver.execute_script('return document.body.scrollHeight;')
            if new_height == last_height:
                break
            last_height = new_height
    except Exception as e:
        print('加载失败')
    print('页面加载结束...')
    # 数据提取
    print('数据提取...')
    ls = driver.find_elements_by_xpath('.//div[@class="WB_detail"]')
    print('len:',len(ls))
    for item in ls:
        name = item.find_element_by_xpath('.//div[@class="WB_info"]/a').text
        print('name:',name)
        pub_date = item.find_element_by_xpath('.//div[@class="WB_from S_txt2"]/a').text
        print('pub date:',pub_date)
        content = item.find_elements_by_xpath('.//div[@class="WB_text W_f14"]')
        if len(content)>0:
            content = content[0].text.strip()
        else:
            content = '空'
        print('content:',content)



if __name__ == '__main__':
    driver = login()
    # url = 'https://weibo.com/p/1003061826792401?is_all=1'
    url = 'https://weibo.com/u/1669879400?is_all=1'
    weibo_crawl(driver,url)

