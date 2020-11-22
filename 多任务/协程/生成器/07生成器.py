
#   生成器 是 特殊的 迭代器   yield
# 列表推导式
# nums = {i*2 for i in range(10)}
#  生成器   可以使用 for
nums = (i*2 for i in range(10))
# print(type(nums))
for  i in nums:
    print(i)




