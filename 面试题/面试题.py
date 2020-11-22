a = 1
def fun(a):
    a = 2
fun(a)
# # 输出的是全局变量
# print(a)
#
'''

class A(object):
    def foo(self,x):
        print("executing foo(%s,%s)"%(self,x)


    @classmethod
    def class_foo(cls,x):
        print( "executing class_foo(%s,%s)"%(cls,x))


    @staticmethod
    def static_foo(x):
        print ("executing static_foo(%s)"%x)

a=A()
'''
# 实例方法只能被实例对象调用，静态方法(由@staticmethod装饰的方法)、类方法(由@classmethod装饰的方法)，可以被类或类的实例对象调用。


# 单例模式
# python的 模块，本身就是 天然的单例模式
#  实现方法
'''  装饰器    __new__    metaclass'''

#
# class MyClass(object):
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not cls._instance:
#             cls._instance = super(MyClass, cls).__new__(cls, *args, **kwargs)
#         return cls._instance
#
#
# class HerClass(MyClass):
#     a = 1

'''GIL'''
#   一个核只能在同一时间运行一个线程.


'''20  闭包'''
#  内置函数 返回外部函数的引用
#   1，，必须有内部函数
# 2.  内部函数 引用外部函数的变量
# 3.  外部函数的返回值是内部函数

''' 深拷贝 浅拷贝'''

# 1）直接赋值,默认浅拷贝传递对象的引用而已,原始列表改变，被赋值的b也会做相同的改变

# （2）copy浅拷贝，没有拷贝子对象，所以   原始数据改变，子对象会改变

# （3） 原始对象 和 子对象都不会改变h

'''26   is'''
# is  是对比地址，， ==  是 对比值

# # a = lambda x: x in range(10)
# for a in range(10):
#     print(a )


''' 46   Python和多线程（multi-threading）'''

# Python中有一个被称为Global Interpreter Lock（GIL）的东西，
# 它会确保任何时候你的多个线程中，只有一个被执行。
# 线程的执行速度非常之快，会让你误以为线程是并行执行的，但是实际上都是轮流执行


l1 = ['b','c','d','b','c','a','a']
l2 = {}.fromkeys(l1).keys()
print(l2)



'''new  实现单例模式'''

class  Myclass(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Myclass,cls).__new__(cls,*args,**kwargs)
        return cls._instance