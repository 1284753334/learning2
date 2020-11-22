# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os

import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings

class DouyuspiderPipeline:
    def process_item(self, item, spider):
        return item


class DouyuImagePipeline(ImagesPipeline):
    #  不加s ,,结果不会保存
    IMAGES_STORE = get_project_settings().get('IMAGE_STORE')

    def get_media_requests(self, item, info):
        image_url = item['image_url']
        yield scrapy.Request(image_url)

    # 能够输出图片的信息
    def item_completed(self, results, item, info):
        # pipline image 不加s ,,结果不会保存  下面的不会打印
        print('result:',results)
        print('info:',info)
        if results[0][0] == True:
            #  原文件
            s_im_path= self.IMAGES_STORE +'/' +results[0]['path']
            #  目标路径
            d_im_path = self.IMAGES_STORE +'/'+ item['nickname']+'.jpg'
            os.rename(s_im_path,d_im_path)
            item['image_path'] = d_im_path
        return item




#         以下为输出的内容  result 为输出的结果
#         result: [(True, {'url': 'https://rpic.douyucdn.cn/asrpic/201103/8760451_1325.png/dy1', 'path': 'full/6f3524cf772a16fbc1d29e0ac18674b32757a727.jpg', 'checksum': '71fc383407ad51099fae186b401fc6ba', 'status': 'downloaded'})]
# info: <scrapy.pipelines.media.MediaPipeline.SpiderInfo object at 0x0000026DF93593D0>





