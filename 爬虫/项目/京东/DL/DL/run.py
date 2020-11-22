#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2020/11/11 11:04:21

@author: Json

        认真大胆      永无BUG
"""
from scrapy import cmdline

name = 'search'
cmd = 'srapy crawl {}'.format(name)
cmdline.execute(cmd.split())

