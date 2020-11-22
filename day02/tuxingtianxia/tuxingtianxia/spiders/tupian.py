import scrapy

from day02.tuxingtianxia.tuxingtianxia.items import TuxingtianxiaItem


class TupianSpider(scrapy.Spider):
    name = 'tupian'
    allowed_domains = ['photophoto.cn']
    start_urls = ['https://www.photophoto.cn/tag/%E6%B5%B7%E6%8A%A5']

    def __init__(self):

        self.offset = 1
        #  为了拼接url
        self.url = 'https://www.photophoto.cn/tag/%E6%B5%B7%E6%8A%A5'

    def parse(self, response):
        # p_list = response.xpath("//div[@class='lista']//li")
        # p_list = response.xpath("//*[@id='list']/li[1]/div[1]")
        #  定位的标签不一定是唯一的   能定位住就可以
        p_list = response.xpath("//div[@class='libg']")
        print(len(p_list))
        for list in p_list:
            item = TuxingtianxiaItem()
            name = list.xpath("./div[@class='image']/a/@title").extract_first()
            if not name:
                name = '空'
            url = list.xpath("./div[@class='image']/a/@href").extract_first()
            if not url:
                url = '空'
            print('detail',url)
            yield scrapy.Request(url, callback=self.parse_item)

            #  翻页
            next = response.xpath('//a[@class="pagenext"]/@href').extract_first()

            if len(next)>0:

                next_page_button = 'http://www.photophoto.cn' + next
                print('next:',next_page_button)

                yield scrapy.Request(next_page_button,callback=self.parse)



    def parse_item(self,response):
        print('response:',response.url)
        item = TuxingtianxiaItem()
        #  获取标题
        item['name'] = response.xpath("//div[@id='left11']/h1/text()").extract_first()
        if not item['name']:
            print('kong')
        #  获取src
        # item['image_url'] = response.xpath("//div[@id='photo']/a/img/@src").extract_first()
        item['image_url'] = response.xpath("//*[@id='photo']/a/@href").extract_first()
        # item['image_url'] = response.xpath("//div[@id='photo']/a/img/src").extract_first()
        # if not item['url']:
        #     print('kong')

        yield item

        # #         翻页   //*[@id="list"]/li[1]/div[1]/div[1]/img
        # if self.offset <= 20:
        #     self.offset += 2
        #     yield scrapy.Request(self.url + '1-0-0-0-0-2-0-' + str(self.offset) + '.html', callback=self.parse)
