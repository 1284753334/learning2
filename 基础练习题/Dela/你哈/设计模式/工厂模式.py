'''

工厂模式

提供一个接口  来创建对象    提供一个类 ，创建  相应的对象


'''



#   芭比  奥特曼  变形金刚  葫芦娃
import json
import time


class Toy:
    def __init__(self,name):
        self.name = name

    # def feature(self):
    #     print('2124')


class Bobby(Toy):

    def __init__(self,name):
        # 继承父类的实例属性
        super(Bobby,self).__init__(name)

    def feature(self):
        print(self.name,'说:大家好，我是可爱的玩具')




class Ultraman(Toy):

    def __init__(self,name):
        # 继承父类的实例属性
        super(Ultraman,self).__init__(name)

    def feature(self):
        print(self.name,'说:怪兽打不过，飞回自己的星球')

class transformers(Toy):

    def __init__(self,name):
        # 继承父类的实例属性
        super(transformers,self).__init__(name)

    def feature(self):
        print(self.name,'说:汽车人变身')


class Brothers(Toy):

    def __init__(self,name):
        super(Brothers,self).__init__(name)

    def feature(self):
        print(self.name,'说:妖怪  还我  师傅')
#
# Brothers('葫芦娃').feature()
#
#
#
class Factory:
    @staticmethod
    def createToy(name):
        pass
        if name == '芭比':
            return Bobby('芭比')
        elif name == '奥特曼':
            return Ultraman('芭比')
        elif name == '变形金刚':
            return transformers('变形金刚')
        elif name == '葫芦娃':
            return Brothers('葫芦娃')

# Factory.createToy('葫芦娃').feature()



# with open('toy.txt','a',encoding='utf-8') as f:
#     f.write("\n奥特曼")
# Factory.createToy('葫芦娃').feature()
with open('toy.txt','r',encoding='utf-8') as f:
    t = f.readlines()
    #  存取多个对象，读取出来，格式有问题，不能生产.
    t = ['葫芦娃', '芭比', '变形金刚', '葫芦娃']
    for i in range(len(t)):
        print(t[i])
        print(type(t[i]))
        # print(type(x))
        Factory.createToy(t[i]).feature()
