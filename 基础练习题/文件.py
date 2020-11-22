'''



'''
import os

# print(os.path)
# print(os.name)

'''

#  执行删除操作
b = os.remove('D:/del.txt')
print(b)
'''

# #  重命名
# b = os.rename('D:/abc.txt','D:/del.txt')
# print(b)

#  创建文件夹
# c = os.mkdir('D:/abc')
# print(c)

# d = os.rmdir('D:/abc')
# print(d)


# print(os.listdir('D:/'))
print(os.getcwd())

#  创建多级文件夹
# os.makedirs('D:/1/2/3/4')

#  删除多级文件夹
# os.removedirs()


# os.path.isdir('E:\\学习资料\\第二阶段 数据库 + 前端\\随堂视频\\2019-07-15 函数 视图 索引')
# os.path.isfile('E:\\学习资料\\第二阶段 数据库 + 前端\\随堂视频\\2019-07-15 函数 视图 索引\\性能优化.txt')


def get(ph):
    t = os.listdir(ph)
    for name in t:
        #  拼接路径 和 名字  拼接 是 逗号，不是  +   不拼接  不能 深度遍历
        name_path = os.path.join(ph,name)
        #  判断 该路径下的 item 是文件 还是 文件夹，，不可写name,否则，无法二次遍历
        if os.path.isdir(name_path):
            print('{}是文件  夹'.format(name))
            get(name_path)

        else:
            #  否则，输出是 文件夹。然后 递归 自己。再次进行判断
            print('{}是文件'.format(name))

# ph = 'E:\\学习资料\\第二阶段 数据库 + 前端\\soft'
# .  或者 ./  表示 当前路径
# ph ='.'
# ph ='E:\\Program Files(X86)'
# get(ph)
def f2(ph):
    #获取指定路径下的文件夹和文件
    file_list=os.listdir(ph)
    #遍历file_list集合
    for f in file_list:
        file=ph+os.sep+f
        print('1:',file)
        #如果是文件,直接打印文件名称
        if os.path.isfile(file):
            print('这是一个文件:%s'%file)
        #如果是文件夹
        if os.path.isdir(file):
            print('这是一个文件夹:%s'%file)
            f2(file)
# f2(file)
# ph=input('请输入路径:')
ph='.'
f2(ph)

