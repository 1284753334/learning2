# import os
# def f2(ph):
#  #获取指定路径下的文件夹和文件
#  file_list=os.listdir(ph)
#  #遍历file_list集合
#  for f in file_list:
#     file=ph+os.sep+f
#  #如果是文件,直接打印文件名称
#  if os.path.isfile(file):
#     print('这是一个文件:%s'%file)
#  #如果是文件夹
#  if os.path.isdir(file):
#     print('这是一个文件:%s'%file)
# # f2(file)
# ph=input('请输入路径:')
# f2(ph)
#  新建文件
# f = open('test.txt', 'w')
# # 关闭这个文件　
# f.close()
#
# with open("os.txt",'w') as f:
# #     f.read()
import pickle
#字典序列化  字符产
dic = {'age': 23, 'job': 'student'}
byte_data = pickle.dumps(dic)
# out -> b'\x80\x03}q\x00(X\x03\x00\x00\...'
print(byte_data)
print(type(byte_data))

#字典反序列化
obj = pickle.loads(byte_data)
print(obj)

# import pickle
# 序列化
# import pickle
#
# with open('abc.txt', 'wb') as f:
#  dic = {'age': 23, 'job': 'student'}
#  pickle.dump(dic, f)
# # 反序列化  字典
# with open('abc.txt', 'rb') as f:
#  aa = pickle.load(f)
#  print(aa)
#  print(type(aa)) # <class 'dict'>