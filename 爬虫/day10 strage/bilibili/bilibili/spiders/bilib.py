# -*- coding: utf-8 -*-
import scrapy
from bilibili.items import BilibiliItem

class BilibSpider(scrapy.Spider):
    name = 'bilib'
    allowed_domains = ['bilibili.com']
    start_urls = ['https://www.bilibili.com/ranking#!/all/0/0/7/']

    def parse(self, response):
        ul = response.xpath('//*[@class="rank-list"]')
        if not ul:
            # 信息获取失败输入日志
            self.log("----------------------%s" % response.url)
        else:
            # 信息获取成功，输出日志
            self.log("++++++++++++++++++++++%s" % response.url)

            # 根据li，获取li的list
            lis = ul[0].xpath('./li')
            items = []
            for bilibili in lis[0:]:
                bilibi_item = BilibiliItem()
                try:
                    #  编号
                    s_vnum = bilibili.xpath('./div[@class="num"]/text()').extract()[0]
                    bilibi_item['vnum'] = s_vnum
                    # 标题
                    s_title = bilibili.xpath('./div[@class="content"]/div[@class="info"]/a/text()').extract()[0]
                    bilibi_item['vtitle'] = s_title
                    # url地址
                    s_url = bilibili.xpath('./div[@class="content"]/div[@class="info"]/a/@href').extract()[0]
                    #s_pic = bilibili.xpath('div[@class="content"]/div[@class="img"]/a/div/img/@src').extract()[0]
                    bilibi_item['vurl'] = s_url
                    # 综合评分
                    s_pts = bilibili.xpath('./div[@class="content"]/div[@class="info"]/div[@class="pts"]/div/text()').extract()[0]
                    bilibi_item['vpts'] = s_pts
                    # s_author = bilibili.xpath('./div[@class="content"]/div[@class="info"]/div[@class="detail"]/a/span/@aid').extract()[0]
                    # bilibi_item['author'] = s_id
                    self.log('vnum=:'+bilibi_item['vnum'])
                    self.log('vtitle=:'+bilibi_item['vtitle'])
                    self.log('vurl=:'+bilibi_item['vurl'])
                    self.log('vpts=:'+bilibi_item['vpts'])
                    # print(bilibi_item)
                except IndexError as e:
                    # 如果有个别信息为空获取失败，则输出日志
                    self.log("!!!!!!!!!!!" + str(e))
                items.append(bilibi_item)

            yield items
