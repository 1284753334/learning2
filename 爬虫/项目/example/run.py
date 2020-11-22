"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/7/2'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
from scrapy import cmdline
# name = 'dmoz'
# name = 'myspider_redis'
# name = 'sina_redis'
# name = 'mycrawler_redis'
name = 'Sina_redis.py'
cmd = 'scrapy crawl {0}'.format(name)

cmdline.execute(cmd.split())





