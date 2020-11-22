from scrapy import cmdline

name = 'douyu'
cmd = 'scrapy crawl {}'.format(name)
cmdline.execute(cmd.split())
