'''



类属性 （不在方法里的属性  也叫  成员变量） 与实例 属性：

单例模式：

工厂模式：

装饰器   模式

项目设计阶段
入门到精通


'''
import sys

'''



class People:
    gender = "男" #类属性/成员变量

    def __init__(self,name,age):#实例属性 /成员方法/*构造方法
        self.name = name
        self.age = age

    def run(self):#  实例方法
        print(self.name,"is running")

p  = People("小明明",18)#调用实例方法
p1 = People("小阳阳",16)
p.run()

print(People.gender)#方法1：通过类名 去调用类属性
print(p.gender)#方法2：通过实例对象   去调用类属性
print(p1.gender)#类属性不会因实例不同而发生改变
#print(People.age)#AttributeError: type object 'People' has no attribute 'age'
#类不可调用实例属性，实例属性是属于实例对象的，实例对象可以调用类属性
People("小明明",18).run()  #   不能调用
People.run(p)
# People.run() #   不能调用
People.gender="女"#可以通过类名去更改成员属性
print(People.gender)



'''
"""
类方法
"""
class People:
    def __init__(self,name):
        self.name = name

    def run(self):# 实例方法
        print(self.name,"is running")

     #类方法
    @classmethod
    def eat(cls):
        print("***",cls)
        print("该中午了，同学们都饿的抬不起头了")
        #类方法
    @classmethod
    def move(cls):
        pass

p = People("小明明")
People.eat()#方法1：通过类名去调用类方法
p.eat()##方法2：通过实例对象去调用类方法


def move():
    pass















