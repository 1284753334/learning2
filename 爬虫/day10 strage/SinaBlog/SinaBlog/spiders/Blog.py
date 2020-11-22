import scrapy
from scrapy.spiders import CrawlSpider, Rule

from  scrapy .linkextractors import LinkExtractor
#
from SinaBlog.items import SinablogItem
class BlogSpider(CrawlSpider):
    name = 'Blog'
    allowed_domains = ['blog.sina.com.cn']
    start_urls = ['http://blog.sina.com.cn/s/articlelist_1525875683_0_1.html']

    # # 翻页链接的提取规则
    # page_link = LinkExtractor(restrict_xpaths=("//li[@class='SG_pgnext']/a",))
    # # 帖子链接地址的提取
    # content_url = LinkExtractor(restrict_xpaths=('//span[@class="atc_title"]/a',))
    # rules = [
    #     Rule(page_link, process_links="deal_link", follow=True),
    #     Rule(content_url, callback="parse_item"),
    # ]
    #
    # def deal_link(self, links):
    #     for link in links:
    #         print("link:", link)
    #     return links

    #     标签一定不能错  别出错   全是 bug

    # next_page =LinkExtractor(restrict_xpaths=('//li[@class="SG_pgnext"]/a'))
    # next_page =LinkExtractor(restrict_css=('li.SG_pgnext > a',))
    #  使用 正则 改 参数  为 allow
    #   翻页 匹配的是 页码  地址栏 地址
    #   http://blog.sina.com.cn/s/articlelist_1525875683_0_2.html
    next_page =LinkExtractor(allow=('http://blog.sina.com.cn/s/articlelist_1525875683_0_\d+\.html',))
    content_page = LinkExtractor(restrict_xpaths=('//span[@class="atc_title"]/a',))
    #  这两个很重要 名字 不能出错  链接地址 不能错
    rules = [
        Rule(next_page,process_links='deal_link',follow=True),
        Rule(content_page,callback='parse_item')
    ]

    def deal_link(self, links):
        for link in links:
            print('current:',link.url)

        return links

    def parse_item(self, response):
        item = SinablogItem()

        t= response.xpath("//h2[@class='titName SG_txta']/text()").extract()

        if len(t)==0:
            item['title'] =response.xpath("//h1[@class='h1_tit']/text()").extract()[0]
            print('title:', item["title"])
        else:
            item['title'] = t[0]
            print('title:',item["title"])
        item['detail_url'] = response.url
        print('url:', item["detail_url"])
        x  = response.xpath("//div[@id='sina_keyword_ad_area2']//p")
        content = x.xpath('string(.)').extract()
        if len(x.extract())==0:
            x  = response.xpath("//div[@class='BNE_cont']//p")
            content1 = x.xpath('string(.)').extract()
            content2 = [str(i) for i in content1]
            # content = ''.join(content2)
            # item['content'] = response.xpath("//div[@class='articalContent   newfont_family']//p/text()").extract()
        else:
            # content = x.xpath('string(.)').extract()
            content1 = x.xpath('string(.)').extract()
            content2 = [str(i) for i in content1]
        content = ' '.join(content2)
        # content = ' '.join(content)
        item['content'] = content.strip()
        print('content:', item["content"])
        print('type:', type(item["content"]))


        yield item
