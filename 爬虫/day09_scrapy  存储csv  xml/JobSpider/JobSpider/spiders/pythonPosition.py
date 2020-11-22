# -*- coding: utf-8 -*-

'''


51job升级反爬之后，职位还在页面中，只不过在 js  中，通过 使用
re 还是能够提取里面的一些信息的

'''

import json
import re
from random import random
from time import sleep

import scrapy
from JobSpider.items import JobspiderItem

class PythonpositionSpider(scrapy.Spider):
    name = 'pythonPosition'
    allowed_domains = ['51job.com']
    start_urls = ['https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']

    def  __init__(self):
        self.url = 'https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
        self.offset = 1


    def parse(self, response):
        self.log('start page parse....')
        html = response.text
        pat = re.compile('window.__SEARCH_RESULT__ =(.*)', re.M | re.S)
        data = pat.findall(html)
        print(data)
        pat1 = re.compile('{"type".*?}')
        # data = json.loads(data)
        data1 = pat1.findall(data[0])
        print(data1)
        print(type(data1))
        print(len(data1))

        item = JobspiderItem()
        t = 0
        for i in data1:
            # print(i)
            # print(type(i))
            i = json.loads(i)
            item['name'] = i["job_name"]
            print(item['name'])
            item['corp'] =i["company_name"]
            print(item['corp'])
            item['city'] = i["workarea_text"]
            print(item['city'])

            salary =  i["providesalary_text"]
            if salary == None:
                item['salary'] = '面议'
            else:
                item['salary']  =salary
            print(item['salary'])
            item['pub_date'] = i["updatedate"]
            print(item['pub_date'])
            t += 1
            print('当前数量：',t)

        # 把提取的数据提交给pipeline
        yield item

        if self.offset <= 4:
            self.offset += 1
            #  不加括号
            # print('new_url:',self.url)
            #  将提取到的链接 进行拼接，，再次发送请求
            url = 'https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,{}.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='

            yield scrapy.Request(url.format(self.offset), callback=self.parse)
            print('new_url:', url.format(i))
            sleep(random())



        print('46432`345')
        # print(response.body)
        # job_list = response.xpath('//div[@class="j_result"]/div[1]/div[2]/div[4]/div[1]/div[@class="e"]')
        # job_list = response.xpath('//div[@class="in"]/div[2]/div[4]/div[1]/div[@class="e"]')/
        # job_list = response.xpath('//div[@class="e"]')
        # job_list = response.xpath('//div[@class="j_joblist"]//dv')
        # job_list = response.xpath('/html/body/div[2]/div[3]/div/div[2]/div[4]/div[1]/div[@class="e"]')
        # job_list = response.xpath('/html/body/div[2]/div[3]/div/div[2]/div[4]/div[1]/div')
        # job_list = response.css('div.j_result div.j_joblist  div')
        # print('len:',len(job_list))
        # for each in job_list:
        #     name = each.xpath('./p/span/a/text()').extract()[0].strip()
        #     city = each.xpath('./span[@class="t3"]/text()').extract()[0].strip()
        #     corp = each.xpath('./span[@class="t2"]/a/text()').extract()[0].strip()
        #     pub_date = each.xpath('./span[@class="t5"]/text()').extract()[0].strip()
        #     salary = each.xpath('./span[@class="t4"]/text()').extract()
        #     if len(salary)>0:
        #         salary = salary[0]
        #     else:
        #         salary = '面议'
        #
        #     print('name:',name)
        #     print('city:', city)
        #     print('corp:', corp)
        #     print('pub_date:', pub_date)
        #     print('salary:', salary)
        #     print('='*200)
        #
        #     item = JobspiderItem()
        #     item['name'] = name
        #     item['corp'] = corp
        #     item['city'] = city
        #     item['salary'] = salary
        #     item['pub_date'] = pub_date
        #
        #     # 把提取的数据提交给pipeline
        #     yield item

        #
        #



