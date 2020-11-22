from scrapy import cmdline

name='Sianblog'

cmd = 'scrapy crawl {}'.format(name)

cmdline.execute(cmd.split())