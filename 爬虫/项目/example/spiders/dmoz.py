from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DmozSpider(CrawlSpider):
    """Follow categories and extract links."""
    name = 'dmoz'
    allowed_domains = ['dmoztools.net']
    start_urls = ['http://dmoztools.net/']
    print('1')

    # rules = [
    #     Rule(LinkExtractor(
    #         restrict_css=('.top-cat', '.sub-cat', '.cat-item')
    #     ), callback='parse_directory', follow=True),
    # ]
    # print('2')


    # def parse_directory(self, response):
    #     print('sdfsf...')
    #     print('3')
    #     for div in response.css('.title-and-desc'):
    #         yield {
    #             'name': div.css('.site-title::text').extract_first(),
    #             'description': div.css('.site-descr::text').extract_first().strip(),
    #             'link': div.css('a::attr(href)').extract_first(),
    #             # 'name': div.xpath('.//a//text()').extract_first(),
    #             # 'description': div.xpath('.//div[@site-descr]/font//text').extract_first().strip(),
    #             # 'link': div.xpath('.//a[1]/@href').extract_first(),
    #         }


    rules = (
        # follow all links
        Rule(LinkExtractor(), callback='parse_page', follow=True),
    )

    def parse_page(self, response):
        return {
            'name': response.css('title::text').extract_first(),
            'url': response.url,
        }

