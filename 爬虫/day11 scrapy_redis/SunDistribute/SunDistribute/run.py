from scrapy import cmdline

name = 'sun1'

cmd = 'scrapy crawl {}'.format(name)

cmdline.execute(cmd.split())