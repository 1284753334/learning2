# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#   pipline  格式不正确，，系统不会报错

# useful for handling different item types with a single interface
import codecs
import json

# import csv
#
#
# def write_to_csv(item):
#    writer = csv.writer(open(settings.bibibi3.csc, 'a'), lineterminator='\n')
#    writer.writerow([item[key] for key in item.keys()])
#
# class WriteToCsv(object):
#     def process_item(self, item, spider):
#         write_to_csv(item)
#         return item

import csv

#
class BilibiliPipeline(object):

    def process_item(self, item, spider):

        '''
         with codecs.open('./data/tieba_'+name+".csv",'a',encoding='utf-8') as f:
            wr = csv.writer(f)
            wr.writerow([nums+','+title+','+detail_url+','+writter])

        :param item:
        :param spider:
        :return:
        '''
        # f = file('./zhuanti.csv', 'a+')
        with codecs.open('./data.csv', 'a', 'utf-8') as f:

            writer = csv.writer(f)

            writer.writerow([ item['number']  ,item['title'] ,item['url'] , item['score'] , item['broad_number'] , item['comment_num'] ])

        return item

    import csv
    #

class Save_csv(object):  # 存储为csv文件，用于以下的数据分析处理
    #
    def __init__(self):
        # 新建一个文件夹就能生成了
        self.file = codecs.open('排行3.csv', 'w', 'utf-8')
        self.fr = csv.writer(self.file)
        self.fr.writerow(['number', 'title', 'url', 'score', 'broad_number', 'comment_num', ])

    def process_item(self, item, spider):
        self.fr.writerow([item['number'], item['title'], item['url'], item['score'], item[
            'broad_number'], item['comment_num']])

        return item

    def close_spider(self, spider):
        self.file.close()

class BibiPipeline(object):  # 存储 为文本格式
    def __init__(self):
        self.f = codecs.open("113排行.txt", "w", "utf-8")

    def process_item(self, item, spider):
        # print(item)
        # print(type(item))
        # number = scrapy.Field()
        # title = scrapy.Field()
        # url = scrapy.Field()
        # score = scrapy.Field()
        # broad_number = scrapy.Field()
        # comment_num = scrapy.Field()

        #
        cont = item['number'] + ',' + item['title'] + ',' + item['url'] + ',' + item['score'] + ',' + item['broad_number'] + ',' + item['comment_num'] + '\n'
        self.f.write(cont)
        # self.f.write()
        return item

    def close_spider(self, spider):
        self.f.close()


