
# 通过实例名（a ）添加实例属性
'''
class People:
    def __init__(self,name):          #   通过实例名（a ）添加实例属性   不安全
        self.name = name

    # __slots__ = ["name","age"]   #限制参数  即 只能传入这两个参数(name age )

a = People("小明明")#创建实例对象a
a.age = 18
a.gender = "男"
print(a.name)      #小明明
print(a.age)        # 18
print(a.gender)#AttributeError: 'People' object has no attribute 'gender'



#  限制传参，只能传这两个参数  22行   报错
class People:
    def __init__(self,name):          #   通过实例名（a ）添加实例属性   不安全
        self.name = name

    __slots__ = ["name","age"]   #限制参数  即 只能传入这两个参数(name age )

a = People("小明明")#创建实例对象a
a.age = 18
a.gender = "男"
print(a.name)      #小明明
print(a.age)        # 18
print(a.gender)#AttributeError: 'People' object has no attribute 'gender'

'''

'''
# 通过 类名（People ）添加  类  属性

class People:
    # 此方法不能限制 添加 类属性
    __slots__ = ["gender", "age",'name']
    def __init__(self,name):          #   通过实例名（a ）添加实例属性   不安全
        self.name = name

      #限制参数  即 只能传入这两个参数(name age )

# a = People()#创建实例对象a
a = People("小明明")#创建实例对象a
# 添加类属性
People.age = 18
People.gender = "男"
People.hobby = "睡觉"
# print(People.name)      #小明明
# print(People.age)
#  实例对象访问类属性
print(a.age)
# print(a.name)
# 类明访问类属性
print(People.gender)
print(People.hobby)

'''


'''

#   通过   实例对象    动态的添加实例方法 ytpes

# 通过types  模块添加  实例方法

import  types

class  People:

    def __init__(self,name):
        self.name = name

def sayHello(self):
    print('hello  hello')


p = People('小明明')
#  通过types 添加  实例方法   不加括号  传的是地址 ，，否则，调用方法  不是 函数
p._sayhello = types.MethodType(sayHello,p)

# 调用实例方法
p._sayhello()


'''




'''
# 动态 添加类方法  静态 方法 ————————》 通过 类名

#
#
class  People:

    def __init__(self):
        pass
        # self.name = name

@classmethod
def Hello(cls):
    print('hello  hello  类方法')

@staticmethod
def Hi():
    print('hi  hi  静态方法')





#   打印的是 内存地址
# print(Hello)
# # print('Hello')
# # print(Hi)

 #
 # 类的方法 名 叫 hello
 # 给的是内存地址
People.hello = Hello
#初始化实例对象
people = People()
people.hello()


#  同理添加 静态方法
# #
People.a = Hi
# #初始化实例对象
people = People()
people.a()

#  静态方法 不可以直接被调用
# Hi()

#  第二种调用

People.hi = Hi
# #初始化实例对象
# people = People()
People.hi()

People.hello = Hello
# #初始化实例对象
# people = People()
People.hello()

# 结果显示 4  第5行 报错，，已经删除 类方法
del People.hello
People.hello()

'''



class A:
    def __init__(self):
        pass

@classmethod
def Hello(cls):
    print('Hello  类方法')


@staticmethod
def Hi():
    print('Hi  静态方法')

#  第一种调用方法

# A.Hello = Hello
# a =A()
# a.Hello()
#
# A.Hi = Hi
# a.Hi()


#  第二种调用方法
A.Hello = Hello
# A.Hello()

# a = A()
# a.Hello()

class B(A):
    # 再调用 ，可以继承A 动态添加的 方法
    pass
    @staticmethod
    def Hello():
        print('自己添加的Hello')

B.Hello()

#   业可以被改写
# A.Hi = Hi
# A.Hi()


