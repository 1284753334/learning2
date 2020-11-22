
# ls = [1,2,3,4,5,6,7,8,9]
# # ls.extend([2,3,])            #  extend 加的是列表 加中括号 []
# print(ls)
#
#
# lu = [2,3]
# v = ls + lu
# print(v)

#
# ls1 = ["a","b","c","d","e","f"]
# ls = [1,2,3,4,5,6,7,8,9]           #  ls 列表相加  a b c 为字符串 要加 ""  或者''
#
# c = ls + ls1
# print(c)


#
# ls1 = ["a","b","c","d","e","f"]
# print(ls1*2)


# ls = [1,2,3,4,5,6,7,8,9]
# # ls.sort()                  #升序排列
# ls.reverse()                  #升序排列
# print(ls)

# dict = {1:2,3:4,5:6 }
# dict[7] = 3
# print(dict)


# dict = {1: 2, 3: 4, 5: 6, 15: 123}
# dict.clear()                               # 清空字典里的键值    结果{}
# print(dict )

#
#
# test = None
# print( type(test) )
#
#
#
# test = False
# print( type(test) )


# #导入模块
# import keyword
# #打印关键字列表
# print(keyword.kwlist)
#
# def fun(x):
#     y=2
#     print("乘法的运行结果：",x*y)
# num1=1
# print("初始num1=",num1)
# fun(num1)
# print("y的值是：",y)



# def fun():
# #     num1=2
# #     print("函数内修改后num1=",num1)
# # num1=1
# # print("初始num1=",num1)
# # fun()
# # print("运行完函数后num1=",num1)


# def fun():
#     global num1
#     num1=2
#     print("函数内修改后num1=",num1)
# num1=1
# print("初始num1=",num1)
# fun()
# print("运行完函数后num1=",num1)

# a, b = 0, 1
# while b < 10:
#     print(b)
#     a,b = b, a+b
#     print(a,b)
#
# def fib2(n):
#     result = []
#     a, b = 0, 1
#     while a < n:
#         result.append(a)
#         a, b = b, a + b
#     return result
# f100 = fib2(100)
# f100









# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%d*%d=%d'%(i,j,i*j),end=' ')
#     print()


# print(x for x in range(6))


# list(range(6))


#
# pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
# # print(pairs[1])
# pairs.sort(key=lambda pair: pair[1])
#
# # print(key=lambda pair: pair[1])
#
# print(pairs)



# (seq)seq = [x**2 for x in range(10) ]
# # print

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# print([[row[i] for row in matrix] for i in range(4)])


# transposed = []
# for i in range(4):
#     transposed.append([row[i] for row in matrix])
#
# print(transposed)

# for row in matrix:
#     print(row[0])

#定义汽车
# class Car:
#     def __init__(self,brand):
#         self.brand=brand
#     def BeDrive(self,p):
#         print(p.name+"正在开车"+self.brand)
#
# #定义人
# class People:
#     def __init__(self,name):
#         self.name=name
#     def Drive(self,c):
#         c.BeDrive(self)
#
# c=Car("玛莎拉蒂")
# p=People("老张")
# #对象传递
# p.Drive(c)

# 定义一个父类
class A:
    def printA(self):
        print('----A----')


# 定义一个父类
class B:
    def printB(self):
        print('----B----')


# 定义一个子类，继承自A、B
class C(A, B):
    def printC(self):
        print('----C----')


obj_C = C()
obj_C.printA()
obj_C.printB()
# 运行结果:----A--------B----



print(5//2)







