from scrapy import cmdline

name ='photo1'
cmd ='scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())


