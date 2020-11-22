import scrapy


class HrSpider(scrapy.Spider):
    name = 'hr'
    allowed_domains = ['tencent.com']
    start_urls = ['https://careers.tencent.com/search.html']

    def parse(self, response):
        rep = response.xpath('/html/body/div[2]/div[2]/div[4]/div[1]/ul//li')
        print(len(rep))
