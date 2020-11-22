'''

marshal

'''



import  marshal



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
# with open("task10.txt","wb") as f_w:
#     marshal.dump(userDict,f_w)
# #
# with open("task10.txt","rb") as f_r :
#     content  = marshal.load(f_r)
#     print(content)



# import marshal
#
# s = "hello hello"
# i =666
# f = 3.1415926537
# b = True
# l = [1,2,3,4,5,6]
# user = {"name":"Megan","age":22}
# x = [s,i,f,b,l,user]
#
# with open("task11.txt","wb") as f_w:
#     marshal.dump(len(x),f_w)
#     for dat in x:
#         marshal.dump(dat,f_w)
#
# with open("task11.txt","rb") as f_r:
#     num = marshal.load(f_r)
#     print(num)
#     for i in range(num):
#         cotent = marshal.load(f_r)
#         print(cotent)

# from sys import abc
#
# print(abc(1))
#
# import sys1
#
# print(sys1.s)


import my

print(my.Abc())














