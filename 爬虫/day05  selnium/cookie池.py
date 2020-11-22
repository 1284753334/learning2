'''

cookie 池
'''
from selenium import webdriver
from fake_useragent import UserAgent
import time
import requests
import hashlib
import pymysql
import random
import json


class CookiesPool:
    def __init__(self):
        #self.ua = UserAgent()
        host = 'localhost'
        port = 3306
        dbname = 'dbproxy'
        user = 'root'
        pwd = '123456'
        try:
            self.conn = pymysql.connect(host=host,port=port,user=user,password=pwd,db=dbname,charset='utf8')
            self.cur = self.conn.cursor()
            self.id_list = []
            self.get_from_db()
        except Exception as e:
            print(e)
            self.close()
        # 使用谷歌浏览器
        self.driver = webdriver.Chrome()
    # 从数据库中读取已有的cookies信息，并检验其有效性
    def get_from_db(self):
        '''
        从数据库中读取已有的cookies信息，并检验其有效性
        :return:
        '''
        strsql = "select * from tbcookies"
        self.cur.execute(strsql)
        results = self.cur.fetchall()
        for item in results:
            username = item[1]
            cookies = item[3]
            home_url=item[4]
            if self.check_cookies(username,cookies,home_url):
                self.id_list.append(username)
            else:
                self.delCookies(username)
            time.sleep(2)
            print(len(self.id_list))
    #  selenium  模拟登录
    def gen_cookies(self,loginname,password):
        if loginname not in self.id_list:
            try:
                self.driver.delete_all_cookies()
                self.driver.maximize_window()
                #self.driver.set_window_size(1124, 850)  # 防止得到的WebElement的状态is_displayed为False，即不可见
                self.driver.get("http://www.weibo.com/login.php")
                # 自动点击并输入用户名
                time.sleep(2)
                self.driver.find_element_by_id('loginname').clear()
                self.driver.find_element_by_id('loginname').send_keys(loginname)
                # 自动点击并输入登录的密码
                time.sleep(2)
                self.driver.find_element_by_name('password').clear()
                self.driver.find_element_by_name('password').send_keys(password)

                # 点击登录按钮
                time.sleep(3)
                self.driver.find_element_by_xpath('//div[@id="pl_login_form"]/div/div[3]/div[6]/a').click()
                time.sleep(10)
                cookies = self.driver.get_cookies()
                print('cookies type:',type(cookies))
                print('cookies values:',cookies)
                home_url = self.driver.current_url
                print('url:',home_url)
                return (cookies,home_url)
                # pickle.dump(cookies, f)#序列化cookies对象
            except Exception as e:
                print("登录失败!", e)
                return None
        return None
    #   requests  请求网页源码，，查看状态码  返回一个bool 值
    def check_cookies(self,username,cookies,home_url):
        '''
        检验cookies是否有效
        :param
        :return:
        '''
        try:
            #  把字符串 反序列化  成 对象
            cookies = json.loads(cookies)
            print('cookies type:',type(cookies))
        except TypeError:
            print('Cookies不合法', username)
            self.delCookies(username)
            print('删除Cookies', username)
            return False

        #headers = {'User-Agent': self.ua.random}  # 定制请求头
        headers = {'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}
        try:
            print('check:', username)
            #url = "https://weibo.com/"#
            cookies = requests.utils.cookiejar_from_dict(cookies)
            print(cookies)
            response = requests.get(url=home_url, headers=headers, cookies = cookies, allow_redirects = False, timeout=5)
            print('code:',response.status_code)
            if response.status_code == 200:
                print('Cookies有效', username)
                return True
            else:
                print('Cookies失效', username)
                return False
        except:
            return False

    def save(self,username,password,cookies,home_url):
        '''
        cookies存储到数据库
        :param ip:
        :param port:
        :return:
        '''

        if username not in self.id_list:
            try:
                dict = {}
                for cookie in cookies:
                    dict[cookie['name']] = cookie['value']
                #      序列化 转换成 json 字符串
                cookies = json.dumps(dict)
                print("cookies:",cookies)
                print("cookies type:", type(cookies))
                print("cookies len:",len(cookies))
                strsql='insert into tbcookies VALUES(0,%s,%s,%s,%s)'
                params = (username,password,cookies,home_url)
                print('1111',params)
                result = self.cur.execute(strsql,params)
                print('222')
                self.conn.commit()

                self.id_list.append(username)
                print('save:', username)
            except Exception as e:
                print(e)
                self.close()

    def get_proxy(self):
        '''
        随机提取可用的cookies
        :return:
        '''
        if len(self.id_list)<=0:
            return None
        username = random.choice(self.id_list)
        strsql='select * from tbcookies where username="'+username +'"'
        self.cur.execute(strsql)
        result = self.cur.fetchone()
        if result != None:
            username = result[1]
            cookies = result[3]
            home_url = result[4]
            if self.check_cookies(username,cookies,home_url):
                try:
                    cookies = json.loads(cookies)
                    return cookies
                except TypeError:
                    print('Cookies不合法', username)
                    self.delCookies(username)
                    print('删除Cookies', username)
                    return self.get_proxy()
            else:
                self.delCookies(username)
                return self.get_proxy()
        else:
            return self.get_proxy()
        return None


    def delCookies(self,username):
        '''
        删除指定的无效cookies
        :param self:
        :param
        :return:
        '''
        strsql = 'delete from tbcookies where username="' + username + '"'
        self.cur.execute(strsql)
        self.conn.commit()
        self.id_list.remove(username)
        print('del cookies:',username)

    def close(self):
        try:
            self.cur.close()
            self.conn.close()
            self.driver.close()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    pool = CookiesPool()
    username = '3414018462@qq.com'
    password = 'qikuedu9527'
    print('start...')
    result = pool.gen_cookies(username,password)
    print('result:',result)
    if result != None:
        cookies = result[0]
        home_url = result[1]
        pool.save(username,password,cookies,home_url)
    print(pool.get_proxy())
    pool.close()










