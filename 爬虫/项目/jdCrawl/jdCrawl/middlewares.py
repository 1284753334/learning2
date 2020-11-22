# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import time
from scrapy import signals
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from scrapy.http import HtmlResponse

class JdcrawlSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class JdcrawlDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    def __init__(self, timeout=None):
        self.timeout = timeout
        options = webdriver.ChromeOptions()
        # options.add_argument('-headless')
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        self.browser = webdriver.Chrome()
        self.browser.set_window_size(1380,700)
        self.browser.set_page_load_timeout(self.timeout)
        self.wait = WebDriverWait(self.browser,self.timeout)


    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        return cls(timeout=crawler.settings.get('TIMEOUT'))

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        # 设置 翻页   通过下方的 输入文本框  跳转 实现  翻页
        page = request.meta.get('page',1)
        try:
            self.browser.get(request.url)
            # input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.input-txt:nth-child(2)')))
            # # input = self.wait.until(EC.presence_of_element_located((By.XPATH, 'span[@class="p-skip//input"]')))
            # # submit = self.wait.until(EC.presence_of_element_located((By.XPATH, 'span[@class="p-skip//a"]')))
            # submit = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.btn:nth-child(4)')))
            # input.clear()
            # input.send_keys(page)
            # submit.click()
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            next_page = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="J_bottomPage"]/span[1]/a[9]')))
            next_page.click()

            # self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            print('t1')
            time.sleep(3)
            #  等待某个元素出现  等待 下一页 出现
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'li.gl-item:nth-child(60) > div:nth-child(1)')))
            # self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.pn-next')))

            return HtmlResponse(url=request.url,body=self.browser.page_source,request=request,encoding='utf-8',status=200)
        except TimeoutException:
            print('翻页请求错误, 正在重新执行...')
            return HtmlResponse(url=request.url,status=500,request=request)


    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
    #  销毁函数，销毁创建的实例对象
    def __del__(self):
        self.browser.close()