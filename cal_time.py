# import time
# #装饰器函数timer,其中function为你想要装饰的函数
# def timer(function):
# 	def wrapper(*args,**kwargs):
# 		time_start = time.time()
# 		function()
# 		time_end = time.time()
# 		cost_time = time_end - time_start
# 		print("花费时间：{}秒".format(cost_time))
# 	return wrapper
# #对Time函数进行装饰器的添加，@timer引用timer装饰器函数
# # @timer
# # def Time():
# # 	time.sleep(1)
# # print('hello')
# #
# # if __name__ == '__main__':
# # 	Time()
# li2 = [5,6,7]
# l1 = [1,2,3,4]
# for i in l1:
# 	if l1[1] == 1:
# 		print(li2[0])
# 	print()
#
#
#
#
#
# # for

#
# dict = {"2622476": ["32.5%", "1"], "2518007": ["80.49%", "2"], "2071898": ["33.92%", "0"], "2516932": ["81.08%", "3"], "2543782": ["41.29%", "3"], "2646815": ["63.48%", "0"], "2518011": ["33.73%", "1"], "2516547": ["85.35%", "2"], "2524168": ["51.68%", "0"], "2071888": ["39.92%", "2"], "2516543": ["47.1%", "1"], "2524173": ["29.75%", "0"], "2532607": ["43.38%", "1"], "2510248": ["20.99%", "0"], "2510245": ["36.29%", "3"]}
# for key in dict.keys():
# 	print(key)
# 	print(type(key))
# 	# print(key,dict[key])
import re

str = '【解析】[p]本题考查马克思主义哲学。[/p][p]“只要你想象得到，你就能做到；[/p]只要你能梦[/p]见，你就能实现”强调了正确意识对实践的指导'


# pat = re.compile(r'\[.*?\]')
# obj = pat.sub('',str)
# print(obj)

li = ['A','B','C','D']
li2 = [1,2,3,4]
li3 = dict(zip(li2,li))

print(li3.items())
for  k,v in li3.items():
	print(k,v)