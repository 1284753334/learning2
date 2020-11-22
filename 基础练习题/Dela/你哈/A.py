#
# import publicA
#
# # publicA.fuc1()
#
# # import  B.b1
# # B.b1.fun1()
#
# from B.b1 import fun1
# fun1()
#
# # import B.b1
# # B.b1.fun1()
#
# # 小结：
#
# # 不同  级别间的导包，需要 把  目标 py  当成一个 包（packaeg）,转化成包 即可。
#
# # reactor  vonverage to  python package
#
#
# #  即可导其中的函数  或者变量
# import sys
#
# print(sys.argv)


'''

单例模式：
'''


class Car:
    # 默认实例对象 没有创建
    # isinstance= None
    # def __new__(cls, *args, **kwargs):
    #     #  如果 类的实例不存在
    #     if Car.isinstance == None:
    #     # t =super().__new__(cls)
    #     # #返回内存地址
    #     # print(t)
    #         Car.isinstance = super().__new__(cls)
    #     return Car.isinstance
    createis = False
    isinstance = None
    def __new__(cls, *args, **kwargs):
        if Car.isinstance == None:
            Car.isinstance = super().__new__(cls)
        return Car.isinstance


    def __init__(self,brand,color,wheel):
        if Car.createis == False:
            self.brand =brand
            self.color =color
            self.wheel = wheel
            Car.createis  =  True

    def show(self):
        print(self.brand,self.color,self.wheel)

# car= Car('凯迪拉克','银灰',4)
# car.show()
# print(id(car))

car1= Car('兰博基尼','黑色',8)
car1.show()
print(id(car1))

car= Car('凯迪拉克','银灰',4)
car.show()
print(id(car))

# 单例模式。打印的地址 都一样



