''' yield   在函数运行时，没次遇到yield  都会暂停，知道遇到 next  函数
才会继续调用，接着 next 的 地方，开始 执行。

https://blog.csdn.net/mieleizhi0522/article/details/82142856/  有详细介绍


有 yield  并不会真正执行，，直到遇到  next  函数
'''

def  create_num(all_num):

    #a = 0
    # b = 1
    a,b = 0,1
    current_num = 0

    while current_num < all_num:
        # print(a)
        '''yield  出现在 函数中，，它就是一个 生成器 模板'''
        yield a

        a,b = b,a+b
        current_num +=1

    return  'ok'

obj2 = create_num(50)

while True:
    try:
        ret = next(obj2)
        print(ret)
    except Exception as ret:
        #  获取返回值
        print(ret.value)
        break




# for i in obj:
#     print(i)








