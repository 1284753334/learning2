# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings



class DouyuspiderPipeline:



    def process_item(self, item, spider):
        return item

#  图片下载  流程，，获取图片 的 href   发送请求，，获取response.content
#  导入要继承的类
#  你不努力，你会得不到想要的结果，，除非你比别人更加努力，要有危机感

class DouyusImagePipeline(ImagesPipeline):
    IMAGES_STORE = get_project_settings('IMAGE_STORE')


    def get_media_requests(self, item, info):
        imagesUrls =  item['imagesUrls']
        yield scrapy.Request(imagesUrls)

    def item_completed(self, results, item, info):
      print('result',results)
      print('info',info)