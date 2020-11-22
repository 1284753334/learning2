from scrapy import cmdline
name = 'bilibili'
cmd = 'scrapy crawl {0}'.format(name)
# cmd = 'scrapy crawl   {0} -o 排行榜.xml -s FEED_EXPORT_ENCODING=UTF-8'.format(name)
cmdline.execute(cmd.split())

#scrapy crawl xiao -o xiaoshuo.txt -s FEED_EXPORT_ENCODING=UTF-8


# 一，命令行 直接生成 csv ,  不支持xml




'''
scrapy crawl basic -o items.json
$ cat items.json
[{"price": ["334.39"], "address": ["Angel, London"], "description": ["website court ... offered"], "image_urls": ["../images/i01.jpg"], "title": ["set unique family well"]}]

$ scrapy crawl basic -o items.jl$ 
cat items
.jl{"price": ["334.39"], "address": ["Angel, London"], "description": ["website court ... offered"], "image_urls": ["../images/i01.jpg"], "title": ["set unique family well"]}

$ scrapy crawl basic -o items.csv$ 
cat items.csvdescription,title,url,price,spider,image_urls..."...offered",set unique family well,,334.39,,../images/i01.jpg

$ scrapy crawl basic -o items.xml
$ cat items.xml

<?xml version="1.0" encoding="utf-8"?><items><item><price><value>334.39</value></price>...</item></items>

'''

