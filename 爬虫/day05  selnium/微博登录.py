'''
微博爬虫  遇到的问题 ：
        需要验证码    或者 有弹窗  再次输入 账号 密码   倒是 网页源码 看不到 这些 代码


        无法定位
        只能 输入 验证码了


        动态加载

'''




from time import sleep

from selenium import webdriver
def login():
    loginname = '18790579029'
    password = 'Hph6927962318'
    browser = webdriver.Chrome()

    url = 'https://weibo.com/login.php'

    browser.get(url)

    sleep(1)

    browser.find_element_by_id('loginname').send_keys(loginname)
    sleep(2)
    browser.find_element_by_name('password').send_keys(password)
    sleep(3)
    browser.find_element_by_link_text('登录').click()

    sleep(10)

    try:
        browser.find_element_by_xpath("//div[@class='item.username.input_wrap']/input").send_keys(loginname)
        sleep(2)
        browser.find_element_by_xpath("//div[@class='item.password.input_wrap']/input").send_keys(password)
        sleep(3)
        browser.find_element_by_class_name('W_btn_a btn_34px').click()
    except Exception as e:
        print(e)
        sleep(8)
    browser.close()

login()
















