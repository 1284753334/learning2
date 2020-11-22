import multiprocessing

q = multiprocessing.Queue(3)

q.put('111')
q.put(222)
q.put([11,222,3333])
q.put(1)
# q.put(2)
# q.put(3)
# q.put(4)




print(q.get())
print(q.get())
print(q.get())
# print(q.get_nowait())
print(q.full())
print(q.empty())
















