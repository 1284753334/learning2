# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import re

from itemadapter import ItemAdapter


class YangguangPipeline:
    def process_item(self, item, spider):
        item['content'] = self.process_content(item['content'])

        return item

    def process_content(self,content):
        content = [re.sub(r'\xa0content|\s','',i)for i in content]
        content = [i for i in content if len(i)>0 ]  # 去除列表中的空字符串
        return content


