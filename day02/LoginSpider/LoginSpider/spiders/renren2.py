# -*- coding: utf-8 -*-
import scrapy


class Renren2Spider(scrapy.Spider):
    name = 'renren2'
    allowed_domains = ['renren.com']
    start_urls = [
        "http://www.renren.com/PLogin.do",
    ]

    # 处理start_urls里的登录url的响应内容，提取登陆需要的参数（如果需要的话)
    def parse(self, response):
        # 提取登陆需要的参数
        #_xsrf = response.xpath("//_xsrf").extract()[0]

        # 发送请求参数，并调用指定回调函数处理
        yield scrapy.FormRequest.from_response(
                response,
                formdata = {"email" : "17752558702", "password" : "qikuedu9527"},#, "_xsrf" = _xsrf},
                callback = self.parse_page
            )

    # 获取登录成功状态，访问需要登录后才能访问的页面
    def parse_page(self, response):
        url = "http://www.renren.com/966745694/profile"
        yield scrapy.Request(url, callback = self.parse_newpage)

    # 处理响应内容
    def parse_newpage(self, response):
        with open("xiao.html", "w",encoding='utf-8') as filename:
            filename.write(response.body.decode('utf-8'))
