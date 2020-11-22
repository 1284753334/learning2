


def bubble_sort(li):
    for i in range(len(li)-1):  # 第i趟 ，只剩两个数的时候，最后一个数，不用排
        exchange = False
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
                exchange = True
        print(li)
        if not exchange:
            return

if __name__ == '__main__':
    li = [3,2,1,5,4,6,7,8,9]
    bubble_sort(li)
    print(li)

#
# def maopao(li):
#     for i in range(len(li)):
#         for j in range(1,len(li)-1-i):
#             if li[j] > li[j+1]:
#                 li[j],li[j+1] =li[j+1],li[j]
#     return li
#
#
# print(maopao([1, 4, 5, 6, 2, 3]))

#  最常用的排序：
# 冒泡           最简单      效率 最低          n** 2
#  选择         交换次数低     比较次数大       n**2
# 插入           最常用  好的选择              n**2
#  快速排序       数据量大  快排               n*lg(n)   时间复杂度 是 动态的    最好 n


'''

查找： 通用的查找算法，就是 for  循环遍历
'''

ls = []
#  若找到  ，返回索引，若找不到 返回-1

def  findInList(Is,value):

    for  index in range(len(ls)):
        item =ls[index]
        if item  == value:
            return True
    return -1

ret = findInList(ls,1)
print(ret)











