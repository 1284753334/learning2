import scrapy


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    def start_requests(self):
        url = 'http://www.renren.com/PLogin.do'
        yield scrapy.FormRequest(
            url=url,
            formdata={"email": "17752558702", "password": "qikuedu9527"},
            callback=self.parse_page)

    #  那么不认真，改一个地方  还弄错了   以后认真点，要不然 天天找bug
    def parse_page(self, response):
        print(response.body.decode('utf-8'))
        print(response.url)

        # 保存网页
        with open("./data/page_1.html", "w", encoding='utf-8') as filename:
            filename.write(response.body.decode('utf-8'))
    # def start_requests(self):
    #     url = 'http://www.renren.com/PLogin.do'
    #     # FormRequest 是Scrapy发送POST请求的方法
    #     yield scrapy.FormRequest(
    #         url=url,
    #         formdata={"email": "17752558702", "password": "qikuedu9527"},
    #         callback=self.parse_page)
    #
    # def parse_page(self, response):
    #     print(response.body.decode('utf-8'))
    #     print(response.url)
    #     with open("./data/page_1.html", "w", encoding='utf-8') as filename:
    #         filename.write(response.body.decode('utf-8'))
