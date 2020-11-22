from scrapy import cmdline

# name = 'Sianblog'
name = 'Sun2'
cmd =  'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())
