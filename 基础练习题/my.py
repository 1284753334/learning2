'''
sys模块。操作系统模块
'''
import json
import math
import os
#  文件重命名
import time
from math import sin

old_path = './元组.py'
new_path ='./元组1.py'
# os.rename(old_path,new_path)


import sys
# 获取用户的输入
#  获取 额外的参数
# print(sys.argv)
#  获取 操作系统平台
#  不加小括号
print(sys.platform)

# 获取环境变量的值  程序运行时 加载的 路径
print(sys.path)

#  系统内置的模块
print(sys.builtin_module_names)


# print(sys.exit())

# 中途不要随意改变量名
#
# b = input("请输入一个字符:")
# while True:
#     if  b =="e":
#         sys.exit(-9)
#     b = input('请输入一个字符：')


#   数学模块
#
# print(sin(math.pi/2))


print(abs(-9.2))

print(math.fabs(-9.2))
#   求次方
print(pow(2,64))

#   求对数
print(math.log10(100))

print(math.sqrt(9))


str = time.time()
print('MATH',math.factorial(100))
str1 = time.time()


def  fun(x):
    sum = 1
    for i in range(1,x+1):
        sum *= i
    return sum


print('遍历：',fun(100))
#  使用 递归求阶乘
str2 = time.time()
def  fun(x):
    if x == 0:
        return 1
    else:
        x -=1
    return fun(x)*x

fun(100)
str3 = time.time()

print('str1',str1-str)
print('str2',str2-str1)
print('str3',str3-str2)


#  递归用的时间久


# 有序     无序  
# 序列化  ：  将  字典  列表  转换成  字符串

#   对象不能直接 写入 文件

# 字符串   不能还原成 原 列表
name = [['zhanngsan',0],['李四',0]]
print(type(name))
#   直接写  报错 。要求是字符串，不能是 列表
# with open('./1.txt','w',encoding='utf-8') as f:
#     f.write(name)

# name = json.dumps(name)
# with open('./1.txt','w',encoding='utf-8') as f:
#     f.write(name)


# with open('./1.txt','r',encoding='utf-8') as f_r:
#     t = f_r.read()
#     # t = json.loads(t)
#     print(type(eval(t)))
#     print(type(t))



i = 1213


s = 'hello'

def Abc():
    return 'hello'