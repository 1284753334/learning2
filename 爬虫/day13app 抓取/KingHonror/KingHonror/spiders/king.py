import scrapy,json


class KingSpider(scrapy.Spider):
    name = 'king'
    allowed_domains = ['gamehelper.gm825.com']
    start_urls = ['url =http://gamehelper.gm825.com/wzry/hero/list?channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=13.0.1.0&version_code=13010&cuid=44C3690762340774AF1D756FCF34D366&ovr=5.1.1&device=Xiaomi_MI+6&net_type=1&client_id=qnBmQaRbJAMjU156zvFhGg%3D%3D&info_ms=BoQNGP4oiZNOWbfiRN9Swg%3D%3D&info_ma=9Sd6B3yFa6H%2BrHMXokRBPcq6E6VtiMQOSOlR1rkPfm0%3D&mno=0&info_la=FAsrk6drpuYLlcCG3Se3lQ%3D%3D&info_ci=FAsrk6drpuYLlcCG3Se3lQ%3D%3D&mcc=0&clientversion=13.0.1.0&bssid=P8uGiTbIO5ybiSlLCZMYHypHQYJHAUvaqhJd6MFHkuM%3D&os_level=22&os_id=3c970ee709c44800&resolution=900_1600&dpi=320&client_ip=192.168.43.253&pdunid=ee709c448003c970']

    def parse(self, response):
        html = response.json()['list']
        # data = response.text.json()
        print()
