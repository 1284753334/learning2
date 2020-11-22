import time
from collections import Iterable

from collections import Iterator


class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)
        # 使Classmate 变成一个可迭代的对象

    def __iter__(self):
        '''使Classmate 变成一个 可迭代的对象  (可以使用for  那么必须使用 __iter__)   '''

        return ClassIterator()


#  通过 ClassIterator 创建的对象  当成是  上面 __iter__ 的返回值
class ClassIterator(object):
    def __iter__(self):
        pass

    def __next__(self):
        # pass
        return 11


classmate = Classmate()

classmate.add('老王')
classmate.add('老李')
classmate.add('老张')

#  判断 classmate 是否是可迭代的对象
# print('判断 classmate 是否是可迭代的对象：', isinstance(classmate, Iterable))
# classmate_iterator = iter(classmate)
#
# print('判断 classmate_iterator 是否是可迭代器：', isinstance(classmate_iterator, Iterator))
# iter(classmate)

# print(next(classmate_iterator))

for name in  classmate:
    print(name)
    time.sleep(1)

