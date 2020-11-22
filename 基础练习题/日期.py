import calendar
import datetime

t1 = datetime.date(2020,10,3)
now = datetime.date.today()
count_day = now-t1
print(count_day)

'''

4.输入两个日期,获得两个日期相差几天，几小时，几秒


t2 = input('请输入年份：')
t3 = input('请输入月份：')
t4 = input('请输入年日期：')

t22 = input('请输入年份：')
t33 = input('请输入月份：')
t43 = input('请输入年日期：')

t5 = datetime.date(int(t2),int(t3),int(t4))
t55 = datetime.date(int(t22),int(t33),int(t43))
dif = abs(t5-t55)
print(dif)


'''

'''
1.输入一个日期，格式如：2010 10 24 ，判断这一天是这一年中的第几天。
# t2 = input('请输入年份：')
# t3 = input('请输入月份：')
# t4 = input('请输入年日期：')
#
# t5 = datetime.date(int(t2),int(t3),int(t4))
#
#
# t6 = datetime.date(int(t2),1,1)
#
# print(t5-t6)
#
# t7 = datetime.date(int(t2),1,1)
# print((t5-t6).days+1)


'''





# today = datetime.date.today().weekday()+1
# print(today)


# week = t5.weekday()+1
# print(week)

'''
2.已知2011年11月11日是星期五，输入日期 ，问YYYY年MM月DD日是星期几

t2 = input('请输入年份：')
t3 = input('请输入月份：')
t4 = input('请输入年日期：')
t5 = datetime.date(int(t2),int(t3),int(t4))


t6 = datetime.date(2011,11,11)
t7 = (t5-t6).days
t8 = abs(t7)%7
if t7 >0:
    t9 = t8+5
    if t9>7:
        print(t9%7)
    else:
        print(t9)

else:
    t10 = 5-t8
    if t10 < 1:
        if t10 == 0:
            print(7)
        elif t10 == -1:
            print(6)
    else:
        print(t10)

'''
b = calendar.weekday(2020,10,29)
print(b)