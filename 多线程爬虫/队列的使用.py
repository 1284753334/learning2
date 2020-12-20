# from queue import Queue
#
# myqueue = Queue(maxsize=10)
#
# print('is empty:',myqueue.empty())
# print('is full:',myqueue.full())
#
#
# # 将一个 值 放到 队列中
#
# myqueue.put(10)
# # 没有返回值的
# print()
# print(myqueue.qsize())
#
# print('is empty:',myqueue.empty())
# print('is full:',myqueue.full())
#
#
# myqueue.put(8)
# print(myqueue.qsize())
#
# print('is empty:',myqueue.empty())
# print('is full:',myqueue.full())
#
# myqueue.put(8)
#
# print('is empty:',myqueue.empty())
# print('is full:',myqueue.full())
#
# print(myqueue.get())
# print(myqueue.get())
# print(myqueue.get())
# # print(myqueue.get())
#
# print('is empty:',myqueue.empty())
#
# print(myqueue.get(True,timeout=3))



#  用 几个线程  负责 页面的爬取，把  返回的 网页源码  放到队列中，，然后 另外的  线程  负责提取 信息
# from queue import Queue
# # #
# # # page_queue = Queue(100)
# # # while True:
# # #     print(page_queue.get())

# for  i  in  range(1,8):
#     print(i,type(i))

#
# a = 4
# b = 8
# if b > a:
#     print(True)
import os
import time

from fishbase.fish_object import DeserializeInstance

logpath = os.path.join(os.getcwd(), "log")
# if not os.path.exists(logpath):
#     os.mkdir(logpath)
print(logpath)

# logpath = os.path.join(os.getcwd(), "log")
# if not os.path.exists(logpath):
#     os.mkdir(logpath)
# # log_abs_filename = get_abs_filename_with_sub_path('log', log_file_name)[1]
# # set_log_file(log_abs_filename)


'''




from pathlib import Path

p = Path('.')
# # print(p)
#  打印父级目录的文件夹
#  输出x ,当x  in
print([x for x in p.iterdir() if x.is_dir()])

#以下是获取该目录下所有py文件的路径：
path=Path.cwd()
pys = path.glob('*.py')#pys是经过yield产生的迭代器
for py in pys:
  print(py)
#  获取当前路径下的 .py 文件
print(list(p.glob('**/*.py')))



'''
'''
cookies_str = "PHPSESSID=r9r8cgomqe61q3ndu6e0; GUIDE_MAP:=1594190653;Hm_lvt_83efb6da7f0d183ee8ad0d78f0=1594115801,1594170658,1594189409,1594190655; acw_tc=2760825615941934039125236e771ed80ecc64edf96b346e78c; Hm_lpvt_83efb6da7f0d18d3ee8ad0d78f0=1594194025"

cookies_dict = {}
for cookie in cookies_str.split('; '):
    cookies_dict[cookie.split('=')[0]] = cookie.split('=')[-1]

print(cookies_dict)

'''
'''
fishbase 简介
fishbase 是由我们自主开发和整理的一套 Python 基础函数库，将我们平时在开发 Python 项目时候的各类工具函数汇聚到一起，方便集中管理和使用。

fishbase 当前版本为 v1.2，支持 Python 3.5-3.8，绝大部分函数也能工作在 Python 2.7 下，但是我们不推荐使用 Python 2.7 。

自 2016/3 初次发布以来，我们坚持不断更新，先后发布了 20 余个版本。近一年来，我们逐步形成每月更新 1 到 2 个版本的频率，抽象出了很多通用的方法，主要分为以下模块：

# https://fishbase.readthedocs.io/en/latest/index.html
'''
''''


print('--- gen_random_bank_card demo ---')
print(gen_random_bank_card())
print(gen_random_bank_card('中国银行', 'CC'))
print(gen_random_bank_card('中国银行', 'DC'))
print('---')
'''
# classfish_object.DeserializeInstance(obj_dict):
#     pass
# print(time.localtime(0))
# from fishbase.fish_random import gen_random_id_card
# #  # 随机生成一个身份证号
# # print(gen_random_id_card())
# # ['3101091986******47']
# from fishbase.fish_random import gen_random_bank_card
# # 随机生成一个中国银行的信用卡卡号
# print(gen_random_bank_card('中国银行', 'CC'))
# # 625907379******1
#
#
# import os
# from fishbase.fish_project import init_project_by_yml
# package_yml = '''
# project: hellopackage
# tree:
# #  不能有空格
#
#  # - README.md  否则报错
# - README.md
# - requirements.txt
# - setup.py
# '''
# # 通过 yml 文件创建一个项目结构
# init_project_by_yml(package_yml, '.')
# print(os.listdir('./hellopackage'))
# # ['requirements.txt', 'README.md', 'setup.py']
# # 更新记录
#

'''

from fishbase import RMBConversion
print('--- RMBConversion demo ---')
chinese_amount = RMBConversion.an2cn('12345.67')
print('RMBConversion an2cn:', chinese_amount)
print('RMBConversion cn2an:', RMBConversion.cn2an(chinese_amount))
print('---')
'''
'''
print('--- DeserializeInstance demo ---')
temp_dict = {'user': {'name': {'last_name': 'zhang', 'first_name': 'san'}, 'address': 'Beijing'}}
new_obj = DeserializeInstance(temp_dict)
print('last_name is: ', new_obj.user.name.last_name)
print('first_name is: ', new_obj.user.name.first_name)
print('address is: ', new_obj.user.address)
#返回的是一个对象
print('address is: ', new_obj.user.name)
print('---')

'''

from fishbase.fish_logger import *
from fishbase.fish_file import *

log_abs_filename = get_abs_filename_with_sub_path('log', 'fish_test.log')[1]

set_log_file(log_abs_filename)

logger.info('test fish base log')
logger.warn('test fish base log')
logger.error('test fish base log')

print('log ok')