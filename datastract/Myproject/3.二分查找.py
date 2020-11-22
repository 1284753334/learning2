#  二分查找必须是有序的
#
# def binary_search(li,val):
#     left = 0
#     right = len(li)-1
#     while left <= right:  # 候选区有值
#         mid = (left+right)//2
#         if li[mid] == val:
#             return mid
#         elif val < li[mid]:
#             #  为什么  加一  减一  都比这个值要小，所以 直接排除了
#             right = mid -1
#         else:
#             left = mid + 1
#     return None
#
# if __name__ == '__main__':
#     li=[1,2,3,4,5,6,7,8,9]
#     binary_search(li,3)
#     print(binary_search(li,8))



def  half(li,value):
    leftIndex= 0
    rightIndex= len(li)-1
    #  在这里  midindex 是一个常量  我们需要变量，在下面 在写一次
    midIndex = (leftIndex + rightIndex) // 2


    while  leftIndex <= rightIndex:

        if value == li[midIndex]:
            return midIndex
        elif value < li[midIndex]:
            rightIndex = midIndex-1
        else:
            leftIndex = midIndex+1
        midIndex = (leftIndex + rightIndex) // 2
    return  None

if __name__ == '__main__':
    li=[1,2,3,4,5,6,7]
    print(half(li, 5))



