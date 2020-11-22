# 插入排序
# 复杂度  0（n）2次方
# def insert_sort(li):
#     for i in range(1,len(li)):
#         tmp = li[i]
#         j = i-1
# #         while j>=0 and li[j] > tmp:
# #             li[j+1] = li[j]
# #             j -= 1
# #         li[j+1] = tmp
# # li=[1,3,4,5,2,7,9,8]
# # insert_sort(li)
# # print(li)
#
#
#
# def insert_sort(li):
#     for i in range(1,len(li)):# i 表示摸到牌的下标
#         tmp = li[i]
#         j = i-1 #手里的牌的下标
#         while j >= 0 and li[j] > tmp:
#             li[j+1] = li[j] #向右移动一位
#             j -= 1 # 箭头左移
#         li[j+1] = tmp
#         print(li)
#
# li = [3,2,4,1,5,7,9,6,8]
# print(li)
# insert_sort(li)
# #
#
#
#
# def insert_sort(li):
#     for i in range(1,len(li)):
#         tmp = li[i]
#         j = i -1
#         while j >=0 and li[j]<tmp:
#             li[j+1] = li[j]
#             j -=1
#         li[j+1] = tmp



# def insert_sort(li):
#     for i in range(1,len(li)):
#         tmp = li[i]
#         j = i -1
#         while j >=0 and li[j] > tmp:
#             li[j+1] = li[j]
#             j -=1
#         li[j+1] = tmp
#
# li = [2,3,4,1,5,8,7,9,6,0]
# insert_sort(li)
# print(li)




# def insert_sort(li):
#     for i in range(1,len(li)):
#         tmp = li[i]
#         j = i -1
#         while j >= 0 and li[j]>tmp:
#             li[j+1] = li[j]
#             j -=1
#         li[j+1] =tmp
#
# li = [2,3,1,4,8,7,6,9,5]
# insert_sort(li)
# print(li)


# def select_sort(li):
#     for i in range(len(li)-1):
#         min_loc = li[i]
#         for j in range(i+1,len(li)):
#             if li[j] < li[min_loc]:
#                 min_loc = j
#         li[i],li[min_loc] = li[min_loc],li[i]
#
#
# li = [4,3,1,2,6,7,8,5,9]
# select_sort(li)
# print(li)

# def insert_sort(li):
#     for i in range(1,len(li)):
#         tmp = li[i]
#         j = i -1
#         while j>=0 and li[j] > tmp:
#              li[j+1]= li[j]
#              j -= 1
#         li[j+1] = tmp
#
#
# li = [4, 3, 1, 2, 6, 7, 8, 5, 9]
# insert_sort(li)
# print(li)


def insert_sort(li):
    for i in range(1,len(li)):
        tmp = li[i]
        j = i -1
        while j>=0 and li[j] >tmp:

            li[j+1] = li[j]
            j -=1
        li[j+1] = tmp
li = [4, 3, 1, 2, 6, 7, 8, 5, 9]
insert_sort(li)
print(li)