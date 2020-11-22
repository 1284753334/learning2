import time
from collections import Iterable

from collections import Iterator


class Fibonacci(object):
    def __init__(self,all_num):
        self.all_num = all_num
        self.current_num = 0
        self.a =0
        self.b =1

    def __iter__(self):
        '''使Classmate 变成一个 可迭代的对象  (可以使用for  那么必须使用 __iter__)   '''

        return self


#  通过 ClassIterator 创建的对象  当成是  上面 __iter__ 的返回值

    def __next__(self):
        # pass
        if self.current_num < self.all_num:
            # ret = self.names[self.current_num]
            ret = self.a
            self.a,self.b = self.b, self.a+self.b
            # self.current_num +=1
            return ret
        else:
            raise StopIteration

fib = Fibonacci(10)

for num in  fib:
    print(num)
    time.sleep(1)

