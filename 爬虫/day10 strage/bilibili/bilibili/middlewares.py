# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
from selenium import webdriver
from scrapy.http import HtmlResponse
from fake_useragent import UserAgent
import base64
from bilibili.proxyIPPool import ProxyIpPool

class WebDriverMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    def process_request(self, request, spider):
        # 加载驱动
        print('================process_request WebDriverMiddleware================')
        browser = webdriver.PhantomJS()
        browser.get(request.url)  # 加载网页
        data = browser.page_source  # 获取网页文本
        data = data.encode('utf-8')
        browser.quit()
        return HtmlResponse(request.url, body=data, encoding='utf-8', request=request)


class ProxyIpMiddleware(object):
    def __init__(self, user_agent=''):
        self.ip_ls = [
            {'ip_port': 'http://111.8.60.9:8123'},
            {'ip_port': 'http://101.71.27.120:80'},
            {'ip_port': 'http://122.96.59.104:80', 'user_passwd': 'user3:pass3'},
            {'ip_port': 'http://122.224.249.122:8088', 'user_passwd': 'user4:pass4'},
        ]
        self.pool = ProxyIpPool(crawl=False)

    def process_request(self, request, spider):
        print('===ProxyIpMiddleware process_request==')
        # 显示当前使用的useragent
        print("********Current ProxyIp:%s************")
        #proxy = random.choice(self.ip_ls)
        proxy = {'ip_port': 'http://'+self.pool.get_proxy()[1]}
        print(proxy)
        if proxy['user_passwd'] is None:
            # 没有代理账户验证的代理使用方式
            request.meta['proxy'] = proxy['ip_port']
        else:
            # 对账户密码进行 base64 编码转换
            base64_userpasswd = base64.b64encode(proxy['user_passwd'])
            # 对应到代理服务器的信令格式里
            request.headers['Proxy-Authorization'] = 'Basic ' + base64_userpasswd
            #设置代理IP
            request.meta['proxy'] = proxy['ip_port']


class UserAgentMiddleware(object):
    '''
    随机更换UA的值
    '''
    def __init__(self, user_agent=''):
        self.ua = UserAgent(verify_ssl=False)

    def process_request(self, request, spider):
        print('===UserAgentMiddleware process_request==')
        if self.ua:
            # 显示当前使用的useragent
            print("********Current UserAgent:%s************")
            custom_ua = self.ua.random
            print('custom_ua:',custom_ua)
            request.headers.setdefault(b'User-Agent', custom_ua)
