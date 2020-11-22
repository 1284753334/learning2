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



loginname = '18790579029'
password = 'Hph6927962318'
# loginname = '3414018462@qq.com'
# password = 'qikuedu9527'


def login():
    '''
    微博的登陆
    :return:
    '''
    driver = webdriver.Chrome()
    try:
        driver.maximize_window()
        # 加载登录页面
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
        driver.quit()
    except Exception as e:
        print('login error.')


if __name__ == '__main__':
    login()

