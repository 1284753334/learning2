from scrapy import cmdline

name = 'novel'
cmd = 'scrapy crawl {0}'.format(name)

cmdline.execute(cmd.split())




