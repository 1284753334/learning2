# import numpy as np
# a = np.array([[1,2,3],[4,5,6]])
# print(a)
#
#
# import numpy as np
# dt = np.dtype([('age',np.int8)])
# a = np.array([(10,),(20,),(30,)],dtype = dt)
# print(a)
#
#
# filename = "./条件分支.py"
# data_arr = np.loadtxt()
import calendar
import random
from datetime import datetime

''''
#  整数

a = random.randint(0,10)
# print(a)
'''

'''
# 0 -  1  之间的小数 
a = random.random()
if a <= 0.26:
    print("")
print(a)

'''




'''

#  随机选择一个列表中的数 
a = random.choice('tomorrow')
a = random.choice([0,1,2,3,4])
print(a)
'''


'''
#   随机打印一个奇数
a = random.randrange(1,100,2)
print(a)
'''

'''
# 指定生成随机 数量的随机字符  
b = 'zyxwvutsrqponmlkjihgfedcba'
a = random.sample(b, len(b))
print(a)
'''
'''
#  将顺序打乱 
a = [0,1,2,3,4,5,6,7,8,9]
random.shuffle(a)
print(a)


'''


import time
'''
a = time.time() # 1970 时间戳
a += 2 * 24 * 60 *60
print(a)
'''
#  可读的时间
# a = time.ctime()

# a = time.struct_time
# print(a.tm_year)


'''
# 结构化的时间
a = time.localtime() # 本地时间
print(a)
print(type(a))  #<class 'time.struct_time'>
# time.struct_time(tm_year=2020, tm_mon=10, tm_mday=29, tm_hour=8, tm_min=27, tm_sec=1, tm_wday=3, tm_yday=303, tm_isdst=0)
print(a.tm_yday,type(a.tm_yday)) #2019a.

'''

'''
#  当前日期时间
a =time.ctime()
print(a)
# Thu Oct 29 08:37:06 2020
'''

'''
a = time.timezone # 以秒为单位
print(a)
print(8 * 60 * 60)

print("---------------------------------")
# 待查。
a = time.tzname
print(a)
for i in a:
    print(i.encode('latin-1').decode('gbk'))
print("---------------------------------")
'''
'''
a = time.timezone
# 欧 亚洲时间 小于0
print(a)
'''
'''
# a= time.tzname
a= time.altzone
#  返回时区
# print(a/60/60)
#  把时间对象 转化成  可读的形式
b = time .asctime(time.localtime())
print(b)
'''

'''
#  python 3.84 可能不支持了
#  cpu 时间  性能分析
print(time.clock())
a = time.clock()
time.sleep(2)
b = time.clock()
print(b)
'''
'''
#  输出格林尼治天文台所在的时间 参数为0
a = time.gmtime(0)
print(a)
'''
'''
返回时区名字
a = time.tzname
print(a)
-28800
('中国标准时间', '中国夏令时')

'''

'''
#  把一个九位数的时间元组  转换成 可读的形式
tumple_time = (2020,10,29,10,4,32,2,3,0)
b = time.asctime(tumple_time)
print(b)

'''
'''
#  把一个九位数的时间元组  返回时间戳

tumple_time = (2020,10,29,10,4,32,2,3,0)
b = time.mktime(tumple_time)
print(b)

'''

'''
# 时间字符串 解析成  指定形式
tumple_time = (2020,10,29,10,4,32,2,3,0)
#   格式  在前  元组在后
c = time.strftime(format('%Y,%m,%d,%H,%M,%S'),tumple_time)
print(c)
#  注意标点 别 漏写了
#  把字符串 转化成 时间元组
d = time.strptime('2020 10 29 10:25:09','%Y %m %d %H:%M:%S')
print(d)

print(time.tzset())
'''
'''

#  日期模块
# 获取当前日期对象
d=datetime.now()
print(d)

# 获取指定日期对象
d=datetime(1990,2,3)
print(d)

'''

'''
#  日期  转  字符串 格式化
dt = datetime.now()
t = dt.strftime('%Y{y} %m{M} %d{d} %H:%M:%S').format(y='年',M='月',d='日')
print(t)

# 字符串  转  日期

d = datetime.strptime('2020 10 29 10:25:09','%Y %m %d %H:%M:%S')
print(d)
'''


#  日历
#  c 为  打印结果的 间距   w 每日间宽度  l  星期行数
# a = calendar.calendar(2020,w=3,l=1,c=6)
# print(a)

#  直接放到 引入包的下面 ，，set 从周几开始 显示
# calendar.setfirstweekday(0)
# calendar.setfirstweekday(0)
# a = calendar.calendar(2020,w=3,l=1,c=6)
# print(a)

#
# 判断是否闰年
def run(l):
    b= calendar.isleap(l)
    return b

# run(2005)

#  返回y1  y2 之间的 闰年 总数

#  遵循左闭右开原则
b = calendar.leapdays(2000,2004)
print(b)

#  打印当月的日历
a  = calendar.month(2020,10,w=1,l=1)
print(a)

#   列表显示
b = calendar.monthcalendar(2020,11)
print(b)
print()
#   返回 该月第一天 周几   共多少天
c = calendar.monthrange(2020,11)
print(c)
d = calendar.month(2020,11)
print(d)

e = calendar.calendar(1970,2,1,6)
print(e)

calendar.prcal(1970,2)





















