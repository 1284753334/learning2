import os

# while True:
#     fname=input('./abc.txt')
#     if os.path.exists(fname):
#         print ("Error:'%s' already exists" %fname)
#     else:
#         break
#
# #下面两句才是最重点。。。。也即open函数在打开目录中进行检查，如果有则打开，否则新建
# fobj=open(fname,'w')
# fobj.close()


# 创建一个txt文件，文件名为mytxtfile,并向文件写入msg
def text_create(name, msg):
    # desktop_path = "C:\\Users\\Administrator\\Desktop\\"  # 新创建的txt文件的存放路径
    desktop_path = "\\"  # 新创建的txt文件的存放路径
    # desktop_path = "E:\\codeworkpace\\project\\learning\\爬虫\\day09_scrapy\\workhome\\Novel\\"  # 新创建的txt文件的存放路径
    full_path = desktop_path + name + '.txt'  # 也可以创建一个.doc的word文档
    file = open(full_path, 'w')
    file.write(msg)  # msg也就是下面的Hello world!
    # file.close()


text_create('abcfile', 'Hello world!')
# 调用函数创建一个名为mytxtfile的.txt文件，并向其写入Hello world!
