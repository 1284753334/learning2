'''

元组

'''

# 元组  不能修改   其他  按照   列表 处理

set = (1,2,3,9,6,7)
set2 = (4,5,6)
print(set+set2)

print(set[1])

#   +  *  生成了 一个  新的  对象
#  切片
# 切片 不改变元组
b = set[0:3]
print(b )

#  in  不能用于判断子集
#   只能判断 元素


li = [1,3]
li1 = [1,2,3]
print(li in li1)


#   利用 list  和 tuple  关键字
li = list(set)
print(li)

li3 = tuple(li)
print(li3)




