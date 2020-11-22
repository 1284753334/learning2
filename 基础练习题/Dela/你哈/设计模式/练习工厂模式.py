'''

通过一个简单的小例子，掌握了 实例方法，类方法，静态方法的调用
'''



class Toy:
    def __init__(self,name):
        self.name = name

    def fun(self):
        pass


class Bobby(Toy):
    def __init__(self, name):
        super(Bobby, self).__init__(name)

    def fun(self):
        print('我是可爱的芭比')


class Brather(Toy):
    def __init__(self, name):
        super(Brather, self).__init__(name)

    def fun(self):
        print('妖怪，你哪里跑')


class Factory:

    #  通过类方法调用
    # @classmethod
    # def createtoy(cls,name):
    #
    #     if name == '芭比':
    #         return Bobby('芭比')
    #     elif name == '葫芦娃':
    #         return Brather('葫芦娃')

    # @staticmethod
    # #   静态方法  没有  明显的 参数   像 cls 等
    # def createtoy(name):
    #
    #     if name == '芭比':
    #         return Bobby('芭比')
    #     elif name == '葫芦娃':
    #         return Brather('葫芦娃')

    def createtoy(self,name):

        if name == '芭比':
            return Bobby('芭比')
        elif name == '葫芦娃':
            return Brather('葫芦娃')


f = Factory().createtoy('葫芦娃').fun()
    # createtoy().fun()



