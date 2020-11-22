"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/9/19'
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

# coding: utf-8

from selenium import webdriver
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time
import requests
import hashlib
import pymysql
import random
import requests

class ProxyIpPool:
    def __init__(self, crawl=True):
        # self.ua = UserAgent()
        host = 'localhost'
        port = 3306
        dbname = 'dbproxyip'
        user = 'root'
        pwd = '123456'
        self.driver = None
        try:
            self.conn = pymysql.connect(host=host, port=port, user=user, password=pwd, db=dbname, charset='utf8')
            self.cur = self.conn.cursor()
            self.id_list = []
            self.get_from_db()
        except Exception as e:
            print('init:', e)
            # self.close()
        if crawl:
            # 使用谷歌浏览器
            self.driver = webdriver.Chrome()

    def get_from_db(self):
        '''
        从数据库中读取已有的代理ip
        :return:
        '''
        strsql = "select * from proxyippool"
        self.cur.execute(strsql)
        results = self.cur.fetchall()
        for item in results:
            id = item[1]
            idname = item[2]
            port = item[3]
            ip = item[4]
            protocal = item[4].lower()
            proxy = protocal + "://" + ip + ":" + port
            self.id_list.append(id)
            #print(len(self.id_list))

    def down_ips(self, url):
        '''
        下载代理IP
        :param url:
        :return:
        '''
        # 访问地址

        self.driver.get(url)
        # 得到html文件
        html = self.driver.page_source
        # print(html)
        # 建立bs对象
        bs = BeautifulSoup(html, 'lxml')
        ls = bs.select('#ip_list > tbody > tr')
        print(len(ls))
        ls.pop(0)

        for item in ls:
            ip= item.select('td')[1].get_text()
            # port = item.select('td')[2].get_text()
            protocal = item.select('td')[5].get_text()
            protocal = protocal.lower()
            proxy = protocal + "://" + ip
            print(proxy)
            if self.check_ip(proxy, protocal):
                print('valid ip.')
                self.save(ip, protocal)
            time.sleep(random.random())

    def down_ips2(self):
        url = 'http://dps.kdlapi.com/api/getdps'

        params = {
            'orderid': 'xxxccvcxv',
            'num': 200,
            'area': '北京,上海',
            'format': 'json',
        }

        response = requests.get(url, params=params)
        proxy_list = response.json()['data']['proxy_list']
        for proxy in proxy_list:
            ip = proxy.split(':')[0]
            port = proxy.split(':')[1]



    def check_ip(self, ip, protocal):
        '''
        检验ip是否有效
        :param ip:
        :return:
        '''
        # headers = {'User-Agent': self.ua.random}  # 定制请求头
        headers = {'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}
        proxies = {}
        proxies = {"http": ip}  # 代理ip
        if protocal == 'https':
            proxies = {"https": ip}  # 代理ip
        print('proxies:', proxies)
        try:
            print('check:', ip)
            url = "http://ip.27399.com/"
            url = "http://www.ip138.com/"
            code = requests.get(url=url, proxies=proxies, headers=headers, timeout=10).status_code
            if code == 200:
                return True
            else:
                return False
        except:
            return False

    def check_all(self):
        '''
        从数据库中读取已有的代理ip，并检验其有效性
        :return:
        '''
        strsql = "select * from proxyippool"
        self.cur.execute(strsql)
        results = self.cur.fetchall()
        for item in results:
            id = item[1]
            ip = item[2]
            port = item[3]
            protocal = item[4].lower()
            proxy = protocal + "://" + ip + ":" + port
            self.id_list.append(id)
            if self.check_ip(proxy,protocal):
                if id not in self.id_list:
                    self.id_list.append(id)
            else:
                self.delRecord(id)
            print(len(self.id_list))

    def save(self, ip, port, protocal):
        '''
        代理ip存储到数据库
        :param ip:
        :param port:
        :return:
        '''
        print('begin save...')
        proxy = ip + ":" + port
        h = hashlib.md5()
        h.update(proxy.encode())
        id = h.hexdigest()
        if id not in self.id_list:
            try:
                strsql = 'insert into proxyippool VALUES(0,%s,%s,%s,%s)'
                params = (id, ip, port, protocal)
                result = self.cur.execute(strsql, params)
                self.conn.commit()
                self.id_list.append(id)
                print('save:', proxy)
            except Exception as e:
                print('save:', e)
                self.close()

    def get_proxy(self):
        '''
        随机提取可用的代理ip
        :return:
        '''
        if len(self.id_list) <= 0:
            return None
        id = random.choice(self.id_list)
        print('id:', id)
        strsql = 'select * from proxyippool where idname="' + id + '"'
        self.cur.execute(strsql)
        result = self.cur.fetchone()
        if result != None:
            ip = result[2]
            port = result[3]
            protocal = result[4]
            print('protocal:', protocal)
            proxy = ip + ":" + port #protocal + "://" +
            #return protocal, proxy
            if self.check_ip(proxy, protocal):
                return protocal,proxy
            else:
                self.delRecord(id)
                self.get_proxy()
        else:
            self.get_proxy()

    def delRecord(self, id):
        '''
        删除指定的记录
        :param self:
        :param id:
        :return:
        '''
        strsql = 'delete from proxyippool where idname="' + id + '"'
        self.cur.execute(strsql)
        self.conn.commit()
        self.id_list.remove(id)
        print('del proxy:', id)

    def close(self):
        try:
            if self.driver:
                self.driver.close()
            self.cur.close()
            self.conn.close()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    #pool = ProxyIpPool()
    # for i in range(1,6):
    #     print('down page:',i)
    #     url = "http://www.xicidaili.com/nn/"+str(i)
    #     pool.down_ips(url)
    # pool.close()

    pool = ProxyIpPool(crawl=False)
    print(pool.get_proxy())
