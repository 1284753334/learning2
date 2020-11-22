

li = [1,2,3,4,5]
# index
b = li.index(4)
print(b)

print(max(li))
print(min(li))


#  追加到最后
# append
# +
# li.append(6)
# print(li)
# print(li.count(1))
# #  len(li)加到最后

# li.insert(88)
# print(li)

#  列表 合并  +   复制后 追加到末尾  + 和 *  效果 一样 末尾追加
#  +  存在三个 变量  extend  是  两个变量
# li.extend([22,222,333])
# print(li)

li += [22,222,333]
print(li)
#  修改
li[0] = 6


print(li)
#  删除列表最后一个元素 并返回 删除的值
print(li.pop())
print(li)
#  删除指定索引的 值
l = li.pop(0)
print(l)
print(li)
#  删除指定元素

del  li[4]

li.pop(li.index(222))
print(li)
# li.clear()
# print(li)

#  只删除 满足条件的 一个
li.remove(4)
print(li)
# 列表字符串  都可以遍历
s = '12345'
print(s[::2])



# del
# clear




# 遍历
#   for



