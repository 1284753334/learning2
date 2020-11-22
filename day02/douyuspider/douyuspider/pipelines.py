# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings
import os


class DouyuspiderPipeline(object):
    def process_item(self, item, spider):
        return item


class DouyuImagePipeline(ImagesPipeline):

    IMAGES_STORE = get_project_settings().get('IMAGES_STORE')

    def get_media_requests(self, item, info):
        image_url = item['image_url']
        yield scrapy.Request(image_url)


    def item_completed(self, results, item, info):
        print('results:',results)
        print('info:', info)
        if results[0][0] == True:
            s_img_path = self.IMAGES_STORE + '/' + results[0][1]['path']
            d_img_path = self.IMAGES_STORE + '/' + item['nickname'] + '.jpg'
            os.rename(s_img_path,d_img_path)
            item['image_path'] = d_img_path
        return item

