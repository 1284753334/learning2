from scrapy import cmdline
name ='login'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())