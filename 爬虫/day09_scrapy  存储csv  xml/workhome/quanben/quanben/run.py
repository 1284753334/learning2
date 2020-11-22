from scrapy import cmdline

name = "novels"
cmd = f"scrapy crawl {name}"
cmdline.execute(cmd.split())
