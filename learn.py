import re
from functools import reduce


def bubble_sort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-i-1):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]







# if __name__ == '__main__':
    # li=[3,4,5,7,6,1,2,8,9]
    # bubble_sort(li)
    # print(li)

# a = 1
# def fun(a):
#     a = 2
# fun(a)
# print(a)



# 单例模式
# class Singleton(object):
#     def __new__(cls, *args, **kw):
#         if not hasattr(cls, '_instance'):
#             orig = super(Singleton, cls)
#             cls._instance = orig.__new__(cls, *args, **kw)
#         return cls._instance
#
# class MyClass(Singleton):
#     a = 1

# print(reduce(lambda x, y: x * y, range(1, 6)))


# 深拷贝，浅拷贝
import copy
# a = [1, 2, 3, 4, ['a', 'b']]
#原始对象
# b = a#赋值，传对象的引用
# c =copy.copy(a)#对象拷贝，浅拷贝
# d = copy.deepcopy(a)#对象拷贝，深拷贝
# a.append(5)#修改对象a
# a[4].append('c')#修改对象a中的['a', 'b']数组对象
# print('a = ', a)
# print('b = ', b)
# print('c = ', c)
# print('d = ', d)


# a =  [1, 2, 3, 4, ['a', 'b', 'c'], 5]
# b =  [1, 2, 3, 4, ['a', 'b', 'c'], 5]
# c =  [1, 2, 3, 4, ['a', 'b', 'c']]
# d =  [1, 2, 3, 4, ['a', 'b']]
#
# A0 = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
# for s in A0:
#   print(A0[s],end=' ')


def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)
#
# f(1)
# f(1)
# f(2)
# f(3)
# f(3,[3,2,1])
# f(3)
# f(4)
# f(5)
# print(re.match('super','superstition').span())


# def f1(lIn):
#     l1 = sorted(lIn)
#     l2 = [i for i in l1 if i<0.5]
#     return [i*i for i in l2]


for i in range(5,0,-1):
    print(i)

