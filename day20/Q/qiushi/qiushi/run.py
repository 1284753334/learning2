#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2020/11/19 8:52:20

@author: Json

        认真大胆      永无BUG
"""
from scrapy import cmdline

name = 'baike1'
cmd = 'scrapy crawl {} -o qiubai.csv'.format(name)
# cmd = 'scrapy crawl {}'.format(name)
cmdline.execute(cmd.split())




'''
持久化存储

持久化存储的类型只能为

 ('json', 'jsonlines', 'jl', 'csv', 'xml', 'marshal', 'pickle')
 
 cmd = 'scrapy crawl {} -o qiubai.csv'.format(name)\
 
 
 局限性，只能存为指定后缀的文件类型
 
 
 
 基于管道  item 
 解析数据：
 
 

'''