import json

# userDict = {
#     "user1":{
#         "username":"刘梦阳","password":"123",
#     },
#     "user2":{
#          "username":"张三","password":"456",
#     }
#
# }
#
#
# # with open("task3.txt","w",encoding="utf-8") as f_w:
# #     # 替换 f_w.write(name)  直接写入了
# #     #  写入的 内容   文件夹
# #     json.dump(userDict,f_w)
#
# with open("task3.txt","r",encoding="utf-8") as f_r:
#     content = json.load(f_r)
#     print(content)
#
#
# import pickle
#
# userDict = {
#     "user1":{
#         "username":"刘梦阳","password":"123",
#     },
#     "user2":{
#          "username":"张三","password":"456",
#     }
#
# }
#
# with open("task5.txt","wb") as f_w:
#     pickle.dump(userDict,f_w)
#
# with open("task5.txt","rb") as f_r :
#     content  = pickle.load(f_r)
#     print(content)

# import pickle
#
# s = "hello hello"
# i = 666
# f = 3.1415926537
# b = True
# l = [1, 2, 3, 4, 5, 6]
# user = {"name": "Megan", "age": 22}
# x = [s, i, f, b, l, user]
#
# with open("./task3.txt","wb") as f_w:
#     #  多数据 的存入，。需要 这一步，，二次 序列化
#     #  写入列表
#     pickle.dump(len(x),f_w)
#     #  对列表的元素序列化
#     for dat in x:
#         pickle.dump(dat,f_w)
# #
# with open("task3.txt", "rb") as f_r:
#     # 问件传入  返回的是一个数字
#     num = pickle.load(f_r)
#     print('2:',num)
#     for i in range(num):
#         print('I:',i)
#         cotent = pickle.load(f_r)
#         print(cotent)


import shelve

s = "hello hello"
i =666
f = 3.1415926537
b = True
l = [1,2,3,4,5,6]
user = {"name":"Megan","age":22}

file = shelve.open("task5.txt")

file["s"] = s
file["f"] = f


print(file["s"])

