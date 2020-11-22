# -*- coding: utf-8 -*-
import scrapy


class Renren3Spider(scrapy.Spider):
    name = 'renren3'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/966924492']
    strcookies = 'anonymid=jru48ifmt3j3si; _r01_=1; jebe_key=757177d7-4364-40db-be6b-cdd5b17c1d81%7C077a3e2b1c00096d5c13732ceee74ce5%7C1549513361097%7C1%7C1551858470234; Hm_lvt_bfc6c23974fbad0bbfed25f88a973fb0=1553336590; ln_uact=17752558702; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; depovince=ZGQT; _de=32B20555AD3784A6BF2D3D01B72FE013; jebecookies=7f06576a-13ec-432a-9645-76332172a27a|||||; ick_login=3b091491-880b-4864-81b8-01ad83cbbd02; p=b6e161b79998cb0f09e004e4a5d444452; first_login_flag=1; t=4362f9091f44508d6464b829cf937b3f2; societyguester=4362f9091f44508d6464b829cf937b3f2; id=966924492; xnsid=a01c2fde; ver=7.0; loginfrom=null; JSESSIONID=abcj60nMq-Obe8ej94FXw; jebe_key=757177d7-4364-40db-be6b-cdd5b17c1d81%7C077a3e2b1c00096d5c13732ceee74ce5%7C1564976866103%7C1%7C1564976866981; wp_fold=0'
    cookies = {item.split('=')[0]:item.split('=')[1] for item in strcookies.split(';')}

    # 可以重写Spider类的start_requests方法，附带Cookie值，发送POST请求
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, cookies=self.cookies, callback=self.parse_page)
            #yield scrapy.FormRequest(url, cookies=self.cookies, callback=self.parse_page)


    # 处理响应内容
    def parse_page(self, response):
        print("===========" + response.url)
        with open("./data/page_3.html", "w", encoding='utf-8') as filename:
            filename.write(response.body.decode('utf-8'))
