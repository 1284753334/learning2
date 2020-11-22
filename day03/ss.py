
# while True:
# #     score = float(input('请输入分数:'))
# #     if score >= 90:
# #         print('A')
# #     elif  score >80:
# #         print('B')
# #     elif  score >70:
# #         print('C')
# #     elif  score >60:
# #         print('D')
# #     else:
# # #         print('E')
#
# while True:
#     year = int(input('请输入年份:'))
#     if (year % 4  == 0 and  year % 100 != 0) or (year % 400 == 0) :
#         result = '闰年'
#     else:
#         result = '平年'
#     print(f"{result}")


#
# a = {1,2,3,4,5,6}
# # b = a.remove(7)
# b = a.discard(7)
#
# print(b)

# list_a = [6,7,8]
# def change(list):
#     list = [1,2,3]
#
#     print(list)
#
#
# change(list_a)
#
# def sumn (*args):
#     sum = 0
#     for i in args:
#         sum += i**3
#     return sum
# print(sumn(1,2,3))
a = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } , { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
for i in  a:
    for j in i.items() :
        print(j)


