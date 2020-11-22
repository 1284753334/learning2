from scrapy import cmdline

name = 'dmoz1'
cmd = 'scrapy crawl {}'.format(name)

cmdline.execute(cmd.split())
