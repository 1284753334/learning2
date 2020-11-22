 # 思想： 每次找一个最小的，放到一个新的列表中。

# 简单的选择排序  复杂度 remove O(N)2次方
# def select_sort(li):
#     new_list = []
#     for i in range(len(li)):
#         a = min(li)
#         # print(a)
#         new_list.append(a)
#         li.remove(a)
#
#
#     return new_list

# if __name__ == '__main__':
#     li = [9,8,7,6,5,3,4,2,1]
#     print(select_sort(li))



#  假如第i趟，数值最小，  复杂度O（n）的2次方
# def select_sort(li):
#     for i in range(len(li)-1): # i 是第几趟
#         min_loc= i
#         for j in range(i+1,len(li)):  # 无序区从哪看到哪
#             if li[j] < li[min_loc]:
#                 min_loc = j
#         li[i],li[min_loc] = li[min_loc],li[i]
#         print(li)
# li= [3,4,2,1,5,6,8,7,9]
# print(li)
# select_sort(li)

# print(li)



#
# # def select_sort(li):
# #     for i in range (len(li)-1):
# #         min_loc = i
# #         for j in range(i+1,len(li)):
# #             if li[j] < li[min_loc]:
# #                 min_loc = j
# #         li[i],li[min_loc] = li[min_loc],li[i]
# #
# # li= [1,3,5,2,4,7,8,9,6]
# # select_sort(li)
# # select_sort(li)
# # print(li)
#
#
# def select_insert(li):
#     for i in range(len(li)-1):
#         min_loc = i
#         for j in range(i+1,len(li)):
#             if li[j] < li[min_loc]:
#                 min_loc = j
#         li[i],li[min_loc] = li[min_loc],li[i]
# li = [3,4,1,2,8,9,6,5,7]
# select_insert(li)
# print(li)



def select_sort(li):
    for i in range(len(li)-1):
        min_loc = i
        for j in range(i+1,len(li)):
            if li[j] < li[min_loc]:
                tmp = j
        li[i],li[min_loc] = li[min_loc],li[i]
li=[1,5,4,3,2,6,7,0,8,9]
select_sort(li)
print(li)

















