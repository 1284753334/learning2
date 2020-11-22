# -*- coding: utf-8 -*-
import scrapy
from JobSpider.items import JobspiderItem

class PythonpositionSpider(scrapy.Spider):
    name = 'boss'
    allowed_domains = ['www.xxx.com']
    start_urls =['https://www.zhipin.com/job_detail/?query=java&city=101210100&industry=&position=']

    def parse(self, response):
        # print('123')
        self.log('start page parse....')
        print('text:',response.text)
        # print('body',response.body)
        # job_list = response.xpath('//div[@class="j_result"]/div[1]/div[2]/div[4]/div[1]/div[@class="e"]')
        # job_list = response.xpath('//div[@class="in"]/div[2]/div[4]/div[1]/div[@class="e"]')/
        # job_list = response.xpath('//div[@class="e"]')
        # job_list = response.xpath('//div[@class="j_joblist"]//dv')
        # job_list = response.xpath('/html/body/div[2]/div[3]/div/div[2]/div[4]/div[1]/div[@class="e"]')
        # job_list = response.xpath('/html/body/div[2]/div[3]/div/div[2]/div[4]/div[1]/div')
        # job_list = response.css('div.job-list  ul > li')
        # job_list = response.xpath('div[@class="job-list"]/ul//li')
        # job_list = response.xpath('//*[@id="main"]/div/div[3]/ul/li')
        # print('len:',len(job_list))
        #
        # for each in job_list:
        #     name = each.xpath('.//span[@class="job-name"]/a/text()').extract().strip()
        #     print(name)
        # #     city = each.xpath('./span[@class="t3"]/text()').extract()[0].strip()
        # #     corp = each.xpath('./span[@class="t2"]/a/text()').extract()[0].strip()
        # #     pub_date = each.xpath('./span[@class="t5"]/text()').extract()[0].strip()
        # #     salary = each.xpath('./span[@class="t4"]/text()').extract()
        # #     if len(salary)>0:
        # #         salary = salary[0]
        # #     else:
        # #         salary = '面议'
        # #
        # #     print('name:',name)
        # #     print('city:', city)
        # #     print('corp:', corp)
        # #     print('pub_date:', pub_date)
        # #     print('salary:', salary)
        # #     print('='*200)
        # #
        # #     item = JobspiderItem()
        # #     item['name'] = name
        # #     item['corp'] = corp
        # #     item['city'] = city
        # #     item['salary'] = salary
        # #     item['pub_date'] = pub_date
        # #
        # #     # 把提取的数据提交给pipeline
        # #     yield item
        #
        # #
        # #
        #
        #

