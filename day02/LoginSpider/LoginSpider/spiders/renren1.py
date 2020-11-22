# -*- coding: utf-8 -*-
import scrapy


class Renren1Spider(scrapy.Spider):
    name = 'renren1'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    def start_requests(self):
        url = 'http://www.renren.com/PLogin.do'
        # FormRequest 是Scrapy发送POST请求的方法
        yield scrapy.FormRequest(
                url=url,
                formdata={"email": "17752558702", "password": "qikuedu9527"},
                callback=self.parse_page)

    def parse_page(self, response):
        print(response.body.decode('utf-8'))
        print(response.url)
        with open("./data/page_1.html", "w",encoding='utf-8') as filename:
             filename.write(response.body.decode('utf-8'))
