
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2020/11/12 13:04:54

@author: Json

        认真大胆      永无BUG
"""
import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


'''
filename = "./presidential_polls.csv"
data_arr1 = np.loadtxt(filename, #需要打开的文件名
    delimiter = "," ,#文件的分隔符
    skiprows = 1, #可以选择调过开头指定的行
    dtype=str, #数据是按编码后的字符串格式存储
    #  可以重零开始
    usecols = (3,17,18,19),#表示读取文件里的  列  的索引位置
    )

print(data_arr1)
# data_arr2 = np.loadtxt()
#  加载csv
#  csv 默认 逗号分割
#  加载报错。
#  遇到乱码  encoding= 'utf8'

filename = "./presidential_polls.csv"
data_arr1 = np.loadtxt(filename, #需要打开的文件名
    delimiter = "," ,#文件的分隔符
    skiprows = 1, #可以选择调过开头指定的行
    dtype=str, #数据是按编码后的字符串格式存储
    #  可以重零开始
    usecols = (3,17,18,19),#表示读取文件里的  列  的索引位置
    encoding= 'utf8'
    )

filename = "./presidential_polls.csv"
data_arr1 = np.loadtxt(open(filename,encoding='utf8'), #需要打开的文件名
    delimiter = "," ,#文件的分隔符
    skiprows = 1, #可以选择调过开头指定的行
    dtype=str, #数据是按编码后的字符串格式存储
    #  可以重零开始
    usecols = (3,17,18,19),#表示读取文件里的  列  的索引位置
    )




import numpy as np
filename = "./presidential_polls.csv"
# data_arr = np.genfromtxt(filename, #需要打开的文件名
data_arr = np.loadtxt(filename, #需要打开的文件名
    # skiprows=1,  不能跳过行数
    delimiter = "," ,#文件的分隔符
    dtype=str, #数据按字符串格式存储，不进行bytes编码
    usecols = (3,17,18,19),#表示读取文件里列索引位置
    )
print(data_arr)
print('数组维度：',data_arr.ndim)
print('数组大小：',data_arr.shape)
print('数组类型：',data_arr.dtype)

# arr = np.random.rand()

'''



# ndarray 数组的创建


# ndarray的随机创建
# import numpy as np
# # 生成指定维度大小（3行4列）的随机多维浮点型数据（二维），rand固定区间0.0 ~ 1.0
# arr = np.random.rand(3, 4)
# print(arr)
# print(type(arr))
#
# arr1 = np.random.randn(3, 4)
# print(arr1)
# print(type(arr1))
#
#
# arr2 = np.random.randint(0, 10,size=(4,2))
# print(arr2)
# print(type(arr2))
#
# arr3 = np.random.uniform(0,3,size=(2,2))
# print(arr3)
#
#

#  持久存储

# 1.csv  写入

import csv
import  codecs
'''
# 新建文件后在写入
def writecsv(data):
    #  判断文件是否存在，不存在就新建
    if not os.path.exists('ten.csv'):
        with open('ten.csv','w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([1,2,3,])
    file = codecs.open('ten.csv','a','utf-8')
    wr = csv.writer(file)
    wr.writerow(data)
    file.close()
data = ['name','pub_date','city','salary']
writecsv(data)

#  read  读取全部
# readlines  读取为一行
with open('data/ten.csv', 'r', encoding='utf-8') as f:
    t = f.read()
    print(t)



dict = {'1':'李白','2':'杜甫','3':'白居易'}
import  json

with codecs.open('test.excel','a',encoding='utf-8') as file:
    content = json.dumps(dict,ensure_ascii=False)+'\n'
    file.write(content)



with open('test.excel','r',encoding='utf-8') as f:
    t = f.read()
    print(t)
    # line = f.readline()
    # while line:
    #     d = json.loads(line)
    #     print(d)
    #     line = f.readline()
'''
#
# import pymysql
#
# try:
#     conn = pymysql.connect(host='localhost',port = 3306,db ='blog',user = 'root',password='123456',
#                            charset = 'utf8')
#     cur = conn.cursor()
#
#
#     strsql = "select * from blog"
#     cur.execute(strsql)
#     result = cur.fetchall()
#     for item in result:
#         id = item[1]
#
#         print('id',id)
#
#
#
# except Exception as e:
#     print(e)

#
# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.randn(3, 4))
# #Dataframe写入到csv文件
# df.to_csv('./data/b.csv', sep=',', header=True, index=True)
# #第一个参数是说把dataframe写入到D盘下的a.csv文件中，参数sep表示字段之间用’,’分隔，header表示是否需要头部，index表示是否需要行号。

#  #Dataframe写入到json文件
# df.to_json('./data/a.json')
#
# #Dataframe写入到html文件
# df.to_html('./data/a.html')
#
# #Dataframe写入到剪贴板中
# df.to_clipboard()
t = [[1,2],[3,4]]

for  i in t:
    print(i)