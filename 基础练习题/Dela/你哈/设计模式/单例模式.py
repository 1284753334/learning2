'''
第一次写：
    在  实例方法里面 写  new  方法》  犯错：
    第二次  代码 有问题  有个点 没理解好
    代码一样，还是有问题，，重写该方法后，，没有问题
'''

class Car:
    # 成员变量
    isinstance =None
    createis = None
    def __new__(cls, *args, **kwargs):
        if Car.isinstance == None:
            Car.isinstance = super().__new__(cls)
 # 最终都会执行这个结果
        return Car.isinstance



    def __init__(self,brand,color,wheel):
        if Car.createis == None:
            self.brand = brand
            self.color = color
            self.wheel = wheel
            Car.createis = True



    def  Show(self):
        print('{}说：我是{}的，有{}个轮子'.format(self.brand,self.color,self.wheel))

car = Car('奔驰','褐色',4)
car.Show()
print(id(car))
#
car1 = Car('奥迪','红色',5)
car1.Show()
print(id(car1))



