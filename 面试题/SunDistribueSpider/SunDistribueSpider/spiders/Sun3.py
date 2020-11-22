# -*- coding: utf-8 -*-
import scrapy


class Sun3Spider(scrapy.Spider):
    name = 'Sun3'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/']

    def parse(self, response):
        pass
