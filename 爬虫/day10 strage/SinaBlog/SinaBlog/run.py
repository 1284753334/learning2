from scrapy import cmdline

name = 'Blog'
# name = 'sina2'

cmd = 'scrapy crawl {0}'.format(name)

cmdline.execute(cmd.split())
