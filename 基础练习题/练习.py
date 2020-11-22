'''
函数 可以有多个返回值
函数高级
可以有多个返回值  用 逗号隔开
接收的时候，打包成元组，元组不能修改

'''
import sys

#
# def  fuc(a,b,c):
#     return 1,2,3,a,b,c
#
#
# print(fuc(4, 5, 6))
# print(type(fuc(4, 5, 6)))

'''
#  可变元组参数
# 遍历的时候，不带*
def func1(*args):
    sum = 0
    for i in args:
        sum +=i
    return sum


print(func1(1, 2, 3))
'''

'''
def func1(name,age,**kwargs):
    return name,age,kwargs


print(func1('站内高三', 18, gender='男'))






# 匿名函数
#  不使用 匿名函数
# ls = []
# def fun(item):
#     return item.name
#
# ls.sort(key=)


# 使用匿名函数

class student:
    def __init__(self,age):
        self.age = age

ls = [student(14),student(24),student(21),student(22),]
# def fun(item):
# #     return item.name


#  调用对象的age,,根据 age  进行排序
ls.sort(key=lambda item: item.age)
print(ls)
for i in ls:
    print(i.age)


#  参数为 三个参数的函数 类型
def MyLambda(func):
    ret = func(1,2,3)
    print(ret)

#  冒号后 作为函数的表达值的  返回值

#  func = lambda
MyLambda(lambda a,b,c:a+b+c)
'''
#  获取递归深度
print(sys.getrecursionlimit())

#  设置 递归深度

print(sys.setrecursionlimit())



#    系统模块
'''
从低层次到高层次

if/ for/ while /: 带有缩进语句内的语句

if / for / while

函数

类

模块（模块所在的路径）
全局： 控制台下：python 命令运行程序  +  路径名 

系统



'''
# 写项目的时候，关注层次






















