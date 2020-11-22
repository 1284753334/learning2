import scrapy


class Sun2Spider(scrapy.Spider):
    name = 'sun2'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/']

    def parse(self, response):
        pass
