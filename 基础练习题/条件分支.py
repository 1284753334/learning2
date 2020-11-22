#  序号为对应练习题的  excel  标号
'''
3.模仿Hello world案例，写一个方法向控制台输出字符串"Hello Unity5"。


print('hellO Unity5')
'''
import random
import time

'''
4.在你的方法中定义变量，用这些变量存储游戏中一个敌人应该有的一些属性（比如用户名，等级，经验值，血量，魔法值等），定义尽可能多的变量。



class Boy:
    def  __init__(self,name,grade,exp,blood,magic_value):
        self.name=name
        self.grade = grade
        self.exp = exp
        self.exp = blood
        self.exp = magic_value
        
'''
'''
 补充 ：__init__  方法的使用
class Box:

    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def getVolume(self):
        return self.width * self.height * self.depth

b = Box(10, 20, 30)
print(b.getVolume())

'''

''' 
5.提示用户输入籍贯，当用户输入籍贯后，向用户显示"欢迎您来到某某" ，某某是用户输入的籍贯地。
a = input('请输入您的籍贯地：')

b= '欢迎您的到来，您的籍贯为%s'%a

print(b)

'''

'''
6.编写一个控制台应用程序，要求用户输入4个int值，并显示他们的乘积。


class multipy:
    def __init__(self,a,b,c,d,):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
    def ji(self):
        return self.a*self.b*self.c*self.d

a = int(input('请输入第一个数字：'))
b = int(input('请输入第二个数字：'))
c = int(input('请输入第三个数字：'))
d = int(input('请输入第四个数字：'))

b = multipy(a,b,c,d)

print(b.ji())


'''

'''
7.让用户分别输入姓名，语文，数学，英语 三门课的成绩，然后给用户显示：XX，你的总成绩为XX分，平均成绩为XX分。


d = input('请输入你的姓名：')
a = int(input('请输入你的语文成绩：'))
b= int(input('请输入你的数学成绩：'))
c= int(input('请输入你的英语成绩：'))

print('{}:你的总成绩为：{}，平均成绩为{}'.format(d,a+b+c,(a+b+c)/3))


'''

'''
8.编写一个程序，输入梯形的上底 下底 和高 ，计算出来梯形的面积并显示出来。梯形的面积=（上底+下底）*高 /2

a = int(input('请输入上底：'))
b = int(input('请输入上下底：'))
c = int(input('请输入高：'))

print('该梯形的面积为：%d'%((a+b)*c/2))

'''

'''
9.编程实现计算指定的天数(如46天)是几周零几天。由用户输入天数 
a = int(input('请输入一个要查询的数字：'))
print('这是第%d周 第%d天'%(math.ceil(a/7),a%7))

'''

'''
10.接受用户输入的两个整数，存储到两个变量里面，交换变量存储的值。
1.临时变量
2.求和法

1）
a = int(input('请第一个数：'))
b = int(input('请第二个数：'))
c= a
a = b
b= c
print(a,b)



2).

a = b +a
b = a-b
a = a-b

print(a,b)
'''

#


'''
11.从键盘输入一个三位的正整数，把百位十位个位数字的相反顺序输出。


#  取商   //   取模 %  
a = int(input('请第一个三位正整数：'))
b = a//100
c =a % 100//10
d = a % 100 %10
print(d,c,b)

'''

'''
12 "写一个方法，传递两个参数，分别代表年份和月份，计算这个月的天数（可选）。
注：闰年的 2 月有 29 天；能被 4 整除同时不能被 100 整除即为闰年；如果能被 400 整除的是闰年，除此两种条件，其他都是非闰年。"



class Days:
    def __init__(self,year,month):
        self.year = year
        self.month = month
    def day(self):
        if self.year %4  == 0 and self.year % 100 !=0 or (self.year %  400 ==0) :
            if self.month ==2:
                print(29)
            elif self.month== 1 or self.month== 3  or self.month== 5  or self.month==7 or self.month== 8  or self.month== 10  or self.month== 12:
                print(31)
            else:
                print(30)

        else:
            if self.month ==2:
                print(28)
            elif self.month== 1 or self.month== 3  or self.month== 5  or self.month==7 or self.month== 8  or self.month== 10  or self.month== 12:

                print(31)
            else:
                print(30)


a = int(input('请输入年份:'))
b = int(input('请输入月份:'))



d = Days(a,b)
#  别忘了调用此方法
d.day()


小结：  回国头来看看  当时写的代码  就是 牛逼   类方法  ，，，就想不到 这样写  __init__
'''

'''
13 让用户输入一个月份，判断这个月是哪个季节？假定3到4月是春季，5到8月是夏季，9到10是秋季，11、12、1、2月是冬季。



while True:
    a = int(input('请输入月份:'))
    if 3<= a <= 4:
        print('春季')
    elif 5<= a <= 8:
        print('夏季')
    elif 9<= a <= 10:
        print('秋季')
    elif 11<= a <= 12 or 1<= a <=2:
        print('冬季')
    else:

        a = int(input('请输入月份:'))

'''

'''
14
让用户输入小强的语文、数学和英语成绩，输出以下判断是否正确，正确输出true，错误输出false
a.语文、英语和数学成绩都大于85分；
b.语文、英语和数学至少有一门大于95分；
c.语文和英语至少有一门大于90分且数学不低于80分。


yuwen = int(input("请输入小强的语文成绩："))
math = int(input("请输入小强的数学成绩："))
English = int(input("请输入小强的英语成绩："))


if (yuwen &  math & English) > 85:
    print(True)
else:
    print(False)
#
if (yuwen  | math | English) > 85:
    print(True)
else:
    print(False)
if (yuwen  | English > 90) & (math >= 80):
    print(yuwen,math,English)
    print(True)
else:
    print(False)
'''

"""

15.
使用switch语句完成一个简单的计算器程序，用户输入两个数字，
用四则运算符计算结果并显示在控制台上。


num1 = int(input("请输入第一个数字:"))
num2 = int(input("请输入第二个数字:"))
a = num1 + num2
b = num1 - num2
c = num1 * num2
d = num1 / num2
print("和为%s,差为%s,积为%s,商为%s,"%(a,b,c,d))

"""

"""
16.
请用户输入两次，每次输入一个数字，如果用户输入的第一个数大就输出第一个数，
如果用户输入的第二个数大就输出第二个数

while True:
    a=int(input("请输入一个数字:"))
    b=int(input("请再输入一个数字:"))
    if a>b:
        print("%s" % (b))
    elif a<b:
        print("%s" % (b))
    else:
        print("请重新输入")


"""

'''
17.
随机产生一个0-5之间的数：(switch)
随机产生的数：0：输出：进入战斗
随机产生的数：1：输出：捡到宝箱
随机产生的数：2：输出：捡到武器
随机产生的数：3：输出：捡到弹药
随机产生的数：4：输出：踩到陷阱
随机产生的数：5：输出：无事件"""
# import random
# num = random.randrange(0,6)
 # print(num)
# if num==0:
#     print("进入战斗")
# elif num==1:
#     print("捡到宝箱")
# elif num==2:
#     print("捡到武器")
# elif num==3:
#     print("捡到弹药")
# elif num==4:
#     print("踩到陷阱")
# elif  num==5:
#     print("无事件")

    # for a in range (1,11):
    #     print(a)


'''

'''
18.
""""随机产生一个0-5之间的数：(switch)
随机产生的数：0：输出：进入战斗
随机产生的数：1：输出：捡到宝箱
随机产生的数：2：输出：捡到武器
随机产生的数：3：输出：捡到弹药
随机产生的数：4：输出：踩到陷阱
随机产生的数：5：输出：无事件"""
# import random
# num=input("")
 a=num in range(0,6)
 print(a)
# if num==0:
#     print("进入战斗")
# elif num==1:
#     print("捡到宝箱")
# elif num==2:
#     print("捡到武器")
# elif num==3:
#     print("捡到弹药")
# elif num==4:
#     print("踩到陷阱")
# elif  num==5:
#     print("无事件")

    # for a in range (1,11):
    #     print(a)
'''

'''
19.
"""老师问学生,这道题你会做了吗?如果学生答"会了(y)",
则可以放学.如果学生不会做(n),则老师再讲一遍"""
while True:
    print("这道题你会了吗")
    a=input("请输入y或n:")
    if a=="y":
        print("放学")
    elif a=="n":
        print("再讲一遍")
    else:
        print("输入非法,")
'''

""""

20.
提示用户输入年龄，如果大于等于18，则告知用户可以查看，如果小于10岁，
则告知不允许查看，如果大于等于10岁并且小于18，
则提示用户是否继续查看（yes、no），如果输入的是yes则提示用户请查看，
否则提示"退出,你放弃查看"。
while True:
    print("请输入年龄:")
    a=int(input( ))
    if a>=18:
        print("请继续观看")
    elif 10 <=a <18:
        print("是否(yes or no )继续观看:")
        b=input( )
        if b=="yes":
            print("请继续查看")
        elif b=="no":
            print("退出，你已放弃查看")
        else:
            print("你的输入非法")

    elif a<10:
        print("不允许查看")
    else:
        print("重新输入")

"""

'''
36 .韩信带兵不足百人，三人一行多一人，七人一行少两人，五人一行正好，求韩信点了多少兵？

解题思路：不足百人   100，。。x-1   % =0,  % 取模  
for i in range(100):
    if (i-1) % 3 == 0 and (i+2)%7 == 0 and (i%5) ==0:
        print(i)
print(6/3)
#  2.0

print(6%3)
# 0
print(6.2/2)
# 3.1

print(6.2//2)
# 3.0  取整
print(6.2%2)
#  取余 
#0.2.0000000018


'''

'''
37 
编程实现如下图列出的图形。
*
***
*****
*******

1 3 5 7
1 2 3 4 

i= 1
while i<=4:
    print('*'*(2*i-1))
    i+=1

# i=1
# while i<8:
#  print('*'*i)
#  i+=2


'''

'''
38
让用户输入一个数显示下面内容。
*******       
******        
*****          
****           
***            
**             
* 


7 6 5 4 3 2 1 
1 2 3 4 5 6 7 

i = 7
while i > 0:
    print(i*'*')
    i -=1

'''

'''
39
编程实现如下图列出的图形。

    *      
   ***        
  *****    
 ******* 
 
 思路 ： 找规律 循环 
 
 空格 3 2 1 0     i  0 1 2 3 
 星号 1 3 5 7 
 
 for i in range(4):
    print(' '*(3-i),end=' ')
    print('*'*(2*i+1))
--------------------------------------------------------------------------------------[p******* 
'''

'''
40 
编程实现如下图列出的图形。
   *
  ***
 *****
*******
 *****
  ***
   *

空格  3 2 1 0 1 2 3  
                          i  0  1  2 3 4 5 6 
星号 1 3 5 7 5 3 1  
2i-

5 0 
3 1 
1 2 
     
     
for i in range(4):
    print(' ' * (3 - i), end=' ')
    print('*' * (2 * i + 1))
for i  in range(3):
    print(' ' *(i+1),end=' ')
    print('*' * (2 * (2-i) + 1))     


'''

'''
41
鸡兔同笼，从上面看有35个头，从下面看有94只脚，请问鸡有几只，兔有几只？

for  i in range(35):
    if 2*i+4*(35-i) == 94:
        print(i,35-i)

'''
'''

42

玩家进来以后要买筹码；
在每次掷骰子前，
    要下注（50~手里剩余的筹码）;
    接着要选择买大小；
    程序要模仿掷骰子，产生一个1~6的随机数
    根据掷骰子的结果，判断玩家的输赢，改变玩家的手里的筹码
        如果买大，4~6是赢，1~3是输
        如果小，1~3是赢，4~6是输
        如果赢了，玩家的筹码+=下注金额
        如果输了，玩家的筹码-=下注金额    
    提示玩家是否要退出游戏
    玩家手里的筹码小于最小下注金额，要强制玩家退出
注意 ：先理清楚思路，从宏观上考虑流程，不要考虑每个步骤的细节。流程搞清楚以后，再琢磨每个步骤的细节。然后写代码。


简单版：
b = 50
a = int(input('请输入下注金额：'))
if a<= b :
    a = int(input('请输入大小：'))
    result = random.randrange(0,7)
    print('结果为：',result)
    if result<=2 and a == '2':
        b +=a

    elif 2<= result <= 6  and a == '1':
        b +=a
    else:
        b -=a
print(b)



'''

'''
43.    获取一个用户输入的3位数字，若用户输入的不是数字，提示重新输入，直到数值合理。

自己思路：
# print(type(3))

# a = input("请输入一个三位数:")
#
# if  not  type(a) =='int':
#     # while True:
#         print('请重新输入')
#     else:
#
#
#     break


# while  type(b) == 'int':
#      a = input("请输入一个三位数:")
#      b = type(a)
#      global b

方法一：

# while True:
#     ten=input("x:")
#     try:
#         x=eval(ten)
#         if type(x)==int:
#             break
#     except:
#         pass

方法二：
while True:
    ten=None
    try:
        ten=int(input("x:"))
    except:
        pass
    if type(ten)==int:
     
        break
        
    总结 ：  循环  加  try: except:
'''

'''
44."根据用户输入的行数，输出下面的效果：
#
#
##
###
#####
######## 以此类推"


有关fib 的 帖子
https://www.cnblogs.com/areyouready/p/8979973.html


nterms = int(input("你需要几项:"))
count = 2
n1 =0
n2 =1
if nterms < 0 :
    print("请输入一个正整数:")
elif nterms == 1:
    print("斐波那契数列：")
    print(n1)
else:
    print("斐波那契数列：")
    print(n1,n2,end=',')
    while count < nterms:
        nth = n1+n2
        print(nth)
        n1 = n2
        n2 = nth
        count +=1



法二：（最简单的）  第几个 数
def fib(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a
print(fib(10))


#  指定个数的函数   列表追加 最简单的  列表

def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[i] for i in fibs:
print(fib(2))


# 使用 yield 关键字
def Fibonacci_Yield_tool(n):
    a, b = 0, 1
    while n > 0:
        yield b
        a, b = b, a + b
        n -= 1

    return b


print(Fibonacci_Yield_tool(10))


终极版：
def Fibonacci_Loop_tool(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
        print(a*'*')
    # return a
b = int(input("请输入行数"))
print(Fibonacci_Loop_tool(b))


'''

# n = input("请输入行数：")
# a1 = 1
# a2 = 1
# count = 2


'''

45
"计算出1-1000中完全数的个数。
完全数：完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。如果一个数恰好等于它的因子之和，则称该数为“完全数”。"


思路：

# sum = 0
# title=0
# for i in range(1,1001):
#     for j in range(1,i+1):
#         if i % j == 0:
#             # print(i)
#             sum += i
#     # print('sum:',sum)
#     if sum == i :
#         print('i:',i)
#         title +=1
# print('title:',title)



#
#  获取一个指定数的所有 因子   不包含该数本身
# sum =0
# j = int(input('请输该数：'))
# 不包含该数本身
# for i in range(1,j):
#     if j % i ==0:
#         print(i)
#         sum  += i
# print('sum:',sum)


#最终结果 



title = 0
for j in range(1,1001):
    sum = 0
    for i in range(1, j):
        if j % i == 0:

            # print(i)
            sum += i


    #
    # print('j:', j)
    # print('sum:', sum)
    if sum == j:
        title += 1
        print('sum:',sum)

print('title:', title)

sum: 6
sum: 28
sum: 496
title: 3
'''

''' 
46  怪物boss血量10000，玩家使用某武器进行攻击，武器伤害值在100-212之间（随机产生伤害），求玩家攻击了多少次，怪物倒下。

blood = 10000

output = random.randrange(100,212)

title = 0
#  只要不为0，就攻击  等于 很考验细节
while  blood >=0:
    blood = blood -output
    title +=1
print('title1:',title)

'''

'''
47 .持续获取用户输入，直到用户输入的字符串一半是字母一半是数字。


title = 0
# while title *2 != b:

# a = input('请输入内容:')
# # b = len(a) + 1
# for i in a:
#     if type(i) == int:
#         print(i)
#         title += 1
# print(title)
title =0
a = '1234qw9e'
for i in a:
    # print(i)
    try :
        if int(i)  in range(0,11):
         print(i)
    except  :



    # if type(i)=="int"



'''

'''

48 .请输出33-250之间的最小素数和最大素数的和。


# li = []
# for  i in range(33,250):
#     for j in range(2,i):
#         if i %j == 0 :
#             continue
#
#         li.append()
# li.sort()
# print(li)

for  i in range(1,101):
    for j in range(2,i):
        if i%j ==0:
            continue(错误)
            
            
最终结果：
li = []
for  i in range(33,250+1):
    for j in range(2,i):
        if (i %j )== 0 :
           #   break  终止循环j，进入下一轮j+1
           break
    else:
        print(i)
        li.append(i)


print(li)
print('sum',li[1]+li[-1])
'''

# li = []
# for  i in range(1,101):
#     for j in range(2,i):
#         if i%j ==0:
#             print("i非质数")
#
#     continue
# li.append(i)
# li.sort()
# print(li)
'''
49."向控制台输出像下面显示的图形（行数由用户输入指定）
*
***
*****
*******
*********"

答案：
a = int(input("请输入一个数字："))
for  i  in range(1,a+1):
    if i %2 != 0:
        print("*"*i)


'''

'''
50.   请依次输出0-99之间能把99整除的数字。

# 易错点： 0 不能做除数
for i in range(1,99):
    if 99 % i == 0:
        print(i)

'''

'''
51."根据用户输入的行数打印出类似下面的图形：
   *
  **
 ***
****
 ***
  **
   *"
分析：   
         行数 ：1 2 3 4 5 6 7
         空格 ：3 2 1 0 1 2 3 
         星号： 1 2 3 4 3 2 1
         
 不足： 只能是奇数行 
         
a = int(input("请输入行数："))
b = (a+1)//2
for i in range(1,b+1):
    print(' '*(b-i),end = ' ')
    print("*"*i)
for i in range(1,a-b+1):
    print(" "*(i),end= " ")
    print("*"*(b-i))



'''

'''  
52.现有列表[1,2,3,4,5,6,7],编写代码使得列表变为[2,4,6,8,10,12,14]，打印列表的所有元素


# li = [1,2,3,4,5,6,7]
# # li[i] = lambda 2*a:for a in li:
# 
# for i in li:
#     # print(i)
#     # print(type(i))
#     for i in range(len(li)):
#         del li[i]
#         li.append(li[i]*2)
# print(li)




#  知识点  ： 列表推导式


参考程序：https://www.cnblogs.com/nxf-rabbit75/p/9997931.html

# a=[1,2,3]
# b=[4,5,6]
# c=[a[i]*2 for i in range(min(len(a),len(b)))]
# c=[a[i]+b[i] for i in range(min(len(a),len(b)))]
# print(c)


答案：

li = [1,2,3,4,5,6,7]
b = len(li)
# print(b)
c = [li[i]*2 for  i in range(b)]
print(c)

'''

'''
53."现有列表[1,2,3,4]和列表[4,3,2,1]，编写代码使得两个列表对应下标的
元素相加，并赋值给一个新的列表，打印新列表的所有元素。"

li1 = [1,2,3,4]
li2 = [4,3,2,1]
li3 = []
# for  i in li1:
#     pass
# for j in li2:
#     pass
# li3.append(i+j)
# print(li3)
print(li1+li2)


答案：

li1 = [1,2,3,4]
li2 = [4,3,2,1]

c = [li1[i]+li2[i] for i in range(len(li1))]
print(c)



'''

'''
54.   输入5个数保存至列表中，求其中最小值，打印出来。

li =[]
i =0
while i<5 :
    a = int(input('请输入一个数字：'))
    li.append(a)
    i +=1
print(min(li))
print(max(li))


'''

'''
55.让用户输入5个长方形的长和宽保存在列表中，然后显示出所有长方形的周长和面积

i= 0
li = []

while i <= 4:
    a = int(input('请输入长:'))
    b = int(input('请输入宽:'))
    li.append(a)
    li.append(b)
    i +=1

print(li)

# for i in range(1,6):
#     for b in len(li+1):
#         if b%2 ==1:
#             zhouchang = 2*(li[b]+li[b+1])
#             squire= li[b]*li[b+1]
#
#             print("zhoouchang %d" %i,zhouchang )
#             print("squire %d" %i,squire )

# li =  [1,2,3,4,5,6,7,8,9,0]
li1 = li[::2]
li2 = li[1::2]
print(li1)
print(li2)
for i in range(0,5):
    zhouchang = (li1[i]+li2[i])*2
    squire = li1[i] * li2[i]
    print("zhouchang %d:"%i,zhouchang)
    print("squire %d:" %i,squire)


'''

'''
56.   编写一个程序，判断用户输入的a、b、c值，能否构成一个三角形,可以输出true 反之false？

a = int(input("请输入a:"))
b = int(input("请输入b:"))
c = int(input("请输入c:"))
if (a+b >c ) or (a+c>b) or (b+c >a):
    print(True)
else:
    print(False)

'''

'''
57.   打印输出1000以内可被3整数除的正整数，每行显示10个数  换行  print('\n')


n = 0
for i in range(1000):
    if i %3 == 0 :
        # for j in range(10):
            n +=1
            print(i,end = ",")
            if  n %10 == 0:
                print('\n')
print('\n')
print('n:',n)

'''

'''
58.   循环接收N个整数，直到用户输入0结束。打印出这些数里的最大数和最小数。

补充:  break  跳出当前循环
break  :
li = []    
while True:
    a =int(input('请输入数字：'))
    li.append(a)
    if a == 0:
        break

print('max:',max(li))
print('min:',min(li))
'''

#  附加
'''
判断用户输入的是否是纯数字

def readInput(input):
#     # input 是字符串。c是input内的某个字符，"0" <= c ，= "9"
#     allDig  = isDigStr(input)
# 
#     if allDig == True :
#         return int(input)
#     else:
#         print("请重新输入")
# 
# # 判断字符串是否是纯数字
# def isDigStr(string):
#     for c in string:
#         if not ('0' <= c <= '9'):
#             return False
# 
#     return True
# 
# readInput(input("请输入数字："))
'''

'''
2.查找两个整数中的最大值

#   需要打印返回值的时候，，，需要使用  print输出 

def  max(num1,num2):
    if num1> num2:
        return  num1
    else:
        return  num2

b = max(2,3)
print(b)

'''

'''
列表求和

def sum (li):
    sum1 = 0
    for i in li :
        sum1 +=i
    return sum1


s = sum ([1,2,3,4,5,6,7,8,9])
print(s)

'''

'''
59:
   接收学生分数判断区间，学生分数必须在0-100之间，如果不满足，则提醒用户输入，直到输入一个正确的分数为止。


while True:
    score  = int(input("请输入学生分数："))
    if not  0<score<100:
        pass
    else:
        break
        
        
总结： 考查  对  break 的  使用
'''
'''
60,
   接收6个整数，计算其中正整数的总和，如果其中用户输入999则循环结束。
   
   参考答案：
i = 0
sum = 0
while  i <=5:
    a = int(input("请输入数字："))
    sum +=a
    i +=1
    if a == 999:
        break
print(sum-999)


小结： 999  作为结束标识，，求和不算其中 
'''

'''
61.
   求1-100之间个位数字不是2，3，4，7，并且不能被3整除的整数之和

参考代码：https://zhidao.baidu.com/question/812530844778299412.html
#  根据 Java 程序代码 改写为 python
sum =  0
for i in range(1,101):
    if (i % 10 == 2 )|( i % 10 ==3 )|(i % 10 ==4 )|(i % 10 ==7 )|(i % 3 == 0):
        continue
    # elif i == 100:
    #     print(i + '=' + sum)
    else:
        sum += i
        print(i)

print(sum)

'''

'''
62    输出1900 到今年之间所有的闰年，并且统计个数（能被 4 整除 但是不能被100整除 或者能被四百整除）

from datetime import datetime

currentYear = datetime.now().year


# print(currentYear)
# print(type(currentYear))
# n = 0
# for i in range(1900,currentYear+1):
#     if (i % 4 != 0 and i % 100 !=0 ) or (i % 400 ==0):
#         continue
#     else:
#         n +=1
#         print(i)
# print(n)

#  结果 包含 1900  没有 2000 ，  刚好相反  

# 改进    里面是闰年，，前面加 not  跳过  
n = 0
for i in range(1900,currentYear+1):
    if not ((i % 4 == 0 and i % 100 !=0 ) or (i % 400 ==0)):
        continue
    else:
        n +=1
        print(i)
print(n)

'''

'''
63.   将一个列表逆序 然后遍历输出

li= [1,2,3,4,5,6,7,8,9,0]
li.reverse()
print(li)
for i in li:
    print(i)
'''

'''
64 .
   输入列表,元素不会重复，最大的与第一个元素交换，最小的与最后一个元素交换，输出列表


# #  实验  换位
# li = [1,2,3,4,5,6]
# a= li.index(max(li))
# b = li.index(min(li))
# li[a],li[b] = li[b],li[a]
# # print()
# print(li)

#  引用
def swap(li):
    # li.index('max(li)'),li[0]=max(li)[0],
    #  a， b  为 索引 
    a = li.index(max(li))
    b = li.index(min(li))
    # li[a], li[b] = li[0], li[-1]
    # 隐藏  其实是 4 个数字  两两 换位置  分 两组

    li[a], li[0] = li[0], li[a]
    li[b], li[-1] = li[-1], li[b]
    return li

# li = []
print(swap([2, 3, 1, 4, 5]))


'''

'''
65.
   青年歌手参加歌曲大奖赛，有5个评委进行打分，试编程求这位选手的平均得分（去掉一个最高分和一个最低分）

def avg(li):
    sum = 0
    for i in range (len(li)):
        sum += li[i]
    sum  = sum -max(li)- min(li)
    print(sum)
    avg = sum /3
    return avg

li =[81,82,83,84,85]
print(avg(li))

# 优化后   拿走直接使用

def avg(li):
    sum = 0
    for i in range (len(li)):
        sum += li[i]
    sum  = sum -max(li)- min(li)
    print('总分为:',sum)
    avg = sum /3
    print('平均分为:',avg)

# li =[81,82,83,84,85]
i = 0
li = []
while i <= 4:
    a = int(input("请输入第%d个分数："%(i+1)))
    li.append(a)
    i +=1

avg(li)

'''
'''
66.
   定义一个长度为5的float型列表，并赋初值[5,3,7,6,8]，将第4个元素的值修改为原来的3倍，然后分别打印下标是奇数的元素。

#
# def fun2(li):
#     li[3]= li[3]*3
#     for i in range(len(li)):
#         if i%2 ==0:
#             continue
#         else:
#             print(li[i])
#
#
# li = [5,3,7,6,8]
# fun2(li)

#  先实现  三倍 打印
li = [5,3,7,6,8]
# print(li[2])
# li[2] = li[2]*3
# print(li)




#  最终结果
li = [5,3,7,6,8]
li2 = []
i = 0
#  
while i <4 :
    for i in range(len(li)):
        if not  i == 3:
            print(li[i])
            continue
        else:
            li[i] =li[i]*3
            print(li)

def odd(li) :
    for i in range(len(li)):
        if  not i % 2== 0:
            continue
        else:
            li2.append(li[i])
    return li2


print(odd(li))

'''
'''
68.
   列表[1,2,4,4,5,7,8]，编写代码删掉列表中的所有4

思路： 列表转集合  去重 

再删除 一个 4 


def fun(li1):
    for  i in range(len(li1)):
        print(li1[i])
        if not li1[i] ==4:
            continue
        else:
            li.remove(4)
    return li

li = [1,2,4,4,5,7,8]
li = set(li)
li1 = []
for i in li:
    li1.append(i)
# print(type(li1))
# print(li1)
print(fun(li1))


'''

'''
69.   去除字符串中的重复字符，重复的字符只保留一个

思路： 转集合    再遍历出结果 
不足： 不像列表一样，可以追加，然后 在 拎出来 

str = 'asdfdbfddfsas'
str = set(str)
for i in str:
    print(i,end='')

'''

'''
70.
   随机产生1000次1-6之间的数，求其中重复次数最多的数，输出该数和其重复的次数
   
   参考答案： https://blog.csdn.net/shaonianlang75/article/details/80986179
   
import random
# 随机数产生100个整数(0-100),放入一个列表中,统计出现次数最多的数字.
# 1.存放随机数列表
number = []
# 2.循环100次
for i in range(0, 100):
    # 3.生成随机数
    num = random.randint(0,100)
    # 4.添加到列表中
    number.append(num)
print(number)

# 5.统计每一个数字出现的次数
result = {}
# 5.1 把数字作为key,出现的次数作为值
# 循环遍历每一个数字
for num in number:
    # 判断字典中是否有num这个key
    if num in result.keys():
        # 让数字对应的次数+1
        result[num] += 1
    else:
        # 以数字作为key,值为1次
        result[num] = 1
# 获取出现最多的次数
max_num = max(result.values())
print(max_num)
# 根据次数(value)找到对应的数字(key)
for item in result.items():
    # 判断item中的value是否和max_num一致   item  类型为 元组  这样色的 {1，2}
    if item[1] == max_num:
        print('出现次数最多的数字为:%s  次数为:%s' % (item[0], item[1]))
#       item[1] 本身类型为   没看懂   item[0]  怎么来的 


补充：
result= {1:2,3:4,5:6}

print(result.items())
# dict_keys([1, 3, 5])
print(type(result.items()))

# dict_items([(1, 2), (3, 4), (5, 6)])
# <class 'dict_items'>

print(result.keys())
# dict_keys([1, 3, 5])

print(type(result.keys())) 
# <class 'dict_keys'>

print(result.values())
print(type(result.values()))

for item in result:
    print(item)
    print(type(item))    #<class 'int'>

答案一：
import  random
li = []
for  i in range(1000):
    b = random.randrange(1,6)
    li.append(b)
    # print(li,i)
print(li)



result = {}
for i in li:
    if  i in result.keys():
        result[i] += 1
    else:
        result[i]  = 1

max_num = max(result.values())
print(max_num)
#  由值找键
c = [k for k,v in result.items() if v == max_num ]


print("出现最多的数字是:%d,次数是%d" %(c[0],max_num))
print('你好%d'%c[0])




#  思路  列表推导式
# c = [i for i  in range(1,6)]
# print(c)
import  random
li = []
for  i in range(1000):
    b = random.randrange(1,6)
    li.append(b)
    # print(li,i)
print(li)
for i in range(len(li)):
    b= li.count(li[i])

    # li = set(li)
    # li1 = []
    # for i in li :
    #     li1.append(i)
    # for i in li:

    print(b,li[i])


# 自己想要的结果  每个数字都有统计的结果 

        和 为 1000， 并显示最大的数字  和 它的 次数 

import  random
li = []
for  i in range(1000):
    b = random.randrange(1,6)
    li.append(b)
    # print(li,i)
print(li)
li1 = []
for i in range(len(li)):
    b= li.count(li[i])
    li1.append(b)
print(li1)

b = dict(zip(li,li1))
print(b)

for k,v in b.items():
    print(k,v)

max_value = max(b.values())
num = [k for k,v in b.items() if v==max_value]
print('出现最多的数字是%d,次数为%d'%(num[0],max_value))


# '''

# for i in result.items():
#     if i[0] == max_num:
#         print(i[0])


# for i in range(len(li)):
#     b= li.count(li[i])
# li = [1,2,3,4,1,1]
# for i in range(len(li)):
#     print(li.count(li[i]))


'''
71."反转字符串中的指定部分的字符序列。
例：
“12345”,2,3=>”12435”"
知识点：  利用  字符串的索引知识 

str = '12345'
# print('字符串的长度为:',len(str))
#
# print('查找索引为3 的字符串：',str[3])
# print('2的索引：',str.index('2'))
# str = '12345'
def  swap(a,b):
    # 此处 c d  代表  索引
    c = str.index(a)
    d = str.index(b)
    str[c],str[d] = str[d],str[c]
    print(str)

swap(1, 5)

'''

'''
72.
   声明一个长度为100的整型列表，为列表的每一个索引位置赋值，赋值要求：1-100之间的随机数，可以重复，
   赋值完毕后，求50这个数字是不是在列表中出现。若出现输出true，否则输出false


import random


li = []
for i in range(100):
    b = random.randrange(1,100)
    li.append(b)
print(li)
if li.count(50)>0:
    print(True)
else:
    print(False)

'''

'''
73.
   有一个长度为62的字符列表，请为这个列表随机赋值(a-z A-Z 0-9)要求每个下标位置的字符都不重复

思路：
把 每一个下标  放到 列表中，统计 出现的次数，随机取 到 值后，放到 列表中，如果，有 出现 2 次的   ，说明重复

在 随机取 ，，再比较 

或者 用 ASCII  码 

不足：  用数字转换 字符时  会出现重复的情况，，但是  纯数字不会有重复的出现，，，可能本身判断机制   不是 太好吧，


等待 大神 解决，，或者  给出  合理的解释  
import random
li=[]
t = 0
for i in range(48,58):
    li.append(i)
    t +=1
#  t 计算完后  还是全局变量   可以直接使用

for i in range(65,91):
    li.append(i)
    t +=1


for i in range(97,123):
    li.append(i)
    t += 1


print(t)
# li.sort()
# li2 = []
# for i in li:
#     li2.append(chr(i))

print(li)

li3=[]
i = 0
while i < 62:
    a = random.choice(li)
    if not a in li3:
        b = chr(a)
        print(a,end=',')
        li3.append(b)
        i += 1

    else:
        continue



print(i)
li3.sort()
print(li3)




'''

#   把 字符对应的ASCII码 加到一个列表中


# li = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]
# li2 = []
# for i in li:
#     li2.append(chr(i))
# print(li2)

'''
74."
   有一个长度为30的整型列表，请按照下面的规律为其进行赋值：
1、1、2、3、5、8、13、21、34......
思路：
    参考  斐波那契 数列  
        写一个 循环的 斐波那契 数列  追加到 列表 中   应该 就算 完成了  

def Fibonacci_Loop_tool(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
        print(a*'*')
    # return a
b = int(input("请输入行数"))
print(Fibonacci_Loop_tool(b))


a= 0
b = 1
n = 0
li = []
while n < 5:
    a,b = b,a+b
    n+=1
    print(a)
    
    
#     li.append(a,end=',')
# print(li)
'''

'''
75.
假设有n个人坐成一圈，从某个人开始报数，数到m的人出圈，接着从出圈的下一个人开始重新报数，
数到m的人再次出圈，如此反复，直到所有人都出圈，请列出出圈顺序。"



  https://blog.csdn.net/seer_520/article/details/105186293
n=int(input("请输入总人数："))
m=int(input("请规定报到数字几的人退出圈子："))
circle=[]
for i in range(1,n+1):
    circle.append(i)
num=1
while len(circle)!=1:
    circle.append(circle.pop(0)) #把已报数的人取出放到队尾，以此实现围成圈循环往复
    num+=1
    if num==m:
        del circle[0] #把报到规定数字的人踢出圈子
        num=1 #重新从1开始报数
print("最后留下的人是原来第{}号的人".format(*circle))


# http://www.voidcn.com/article/p-rajawedp-pb.html
from itertools import cycle
def demo(lst, k):
    #切片，以免影响原来的数据
    t_lst = lst[:]
    #游戏一直进行到只剩下最后一个人
    while len(t_lst)>1:
        #创建cycle对象
        c = cycle(t_lst)
        #从1到k报数
        for i in range(k):
            t = next(c)
        #一个人出局，圈子缩小
        index = t_lst.index(t)
        t_lst = t_lst[index+1:] + t_lst[:index]
        #测试用，查看每次一个人出局之后剩余人的编号
        print(t_lst)
    #游戏结束
    return t_lst[0]
    
lst = list(range(1,11))
print(demo(lst, 3))



"""
无穷迭代器 cycle()
"""
# from itertools import cycle
#
# c = cycle('ABCD')
# for i in range(10):
#     print(next(c), end=',')


"""
无穷迭代器 repeat()
"""
from itertools import repeat

r = repeat(1, 6)
for i in range(6):
    print(next(r), end=',')

'''

# li= [1,2,3,4,5]
# print(li[:])


'''
76.
   编写方法，用户输入三个整数，将最大数和最小数输出

思路： 放到列表中   利用  max  min 

勉强实现了  但是  这个方法不太好 
def fun(li):
    print(max(li))
    print(min(li))
i = 1
li = []
while i<4:
    a = int(input('请输入第%d个数：'%i))
    li.append(a)
    i +=1

fun(li)

'''
'''
77.
   编写方法将1~200末位数为5的整数求和返回

思路：  末位  是 5  ，能被 5 整除 %   0  
def  fun ():
    sum = 0
    for  i in range(1,201):
        if i % 5 ==0 :
            # print(i)
            sum += i
            print(i)
    # print(sum)
    return sum


print(fun())
结果：4100

验证结果：
5  10 15 20    50
5+ 20 = 25  10+15 =25  
20 /5 = 4   
4/2 = 2 

同理 可得：

sum = 20* （200+5） =  4100


'''

'''
78.
   输入学员的语文、数学和英语三门课的成绩，计算平均成绩输出。
   
   def avg(a,b,c):
    avg = (a+b+c)/3
    return avg
i = 0
while i <1:
    a = int(input('请输入语文成绩：'))
    b = int(input('请输入数学成绩：'))
    c = int(input('请输入英语成绩：'))
    i+=1
print(avg(a, b, c))

拓展：

    加上 大循环 while True:
    
    实现  一直 循环 计算  

'''

'''
79.    输入一个圆的半径(int),并且输出这个圆的面积

def  squire(r):
    return  3.14*r*r

a = int(input("请输入圆的半径："))
print(type(a))
print(squire(a))
# print(3.14*9)

不足：  出现了 多位小数  下面的例子没有出现这种情况 
'''

'''
" 80.
  企业发放的奖金根据利润提成。利润(I)低于或等于1万元时，奖金可提10%；利润高于1万元，低于2万元时，
  低于1万元的部分按10%提成，高于1万元的部分，可提成7.5%；2万到4万之间时，高于2万元的部分，可提成5%；
  4万到6万之间时高于4万元的部分，可提成3%；6万到10万之间时，高于6万元的部分，可提成1.5%，高于10万元时，
  超过10万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？编写相应的方法？"

def money(I):

    if I<=10000:
        red = I*0.1
    elif 10000<I<=20000:
        red  = 10000*0.1 +(I-10000)*0.075
    elif 20000 < I <= 40000:
        red = 10000 * 0.1 + 10000 * .075+(I-20000)*0.05
    elif 40000 < I <= 60000:
        red = 10000 * 0.1 + 10000 * .075 + (I - 20000) * 0.05 + (I - 40000) * 0.03
    elif 60000 < I <= 100000:
        red = 10000 * 0.1 + 10000 * .075 + 20000* 0.05 +  20000 * 0.03+ (I - 60000) * 0.015
    elif 100000 <I :
        red = 10000 * 0.1 + 10000 * .075 + 20000 * 0.05 + 20000 * 0.03 + 40000 * 0.015 + (I - 100000) * 0.010
    return red
while True:
    a = int(input("请输入利润数："))
    print(money(a))

小结： 这也太繁琐了吧   能有人简化一下吗
'''

'''
81."   超市收银系统规定，消费满500元的可以打9.8折，消费满800元可以打9.5折，消费满1000元可以打9折，
先要求输入消费数额，显示应收金额及折扣金额——“您合计收费***元 本次收***元 为您节省***元”"


答案：
# while True:
def appy(totle):
    if 500 <= totle <= 800:
        totle1 = totle *0.98
        save = totle * 0.02
    elif 800 <= totle <= 1000:
        totle1 = totle * 0.95
        save = totle * 0.15
    elif 1000 <= totle :
        totle1 = totle * 0.9
        save = totle * 0.1
    return "您合计收费%d元，本次收%d元，为您节省%d元" %(totle,totle1,save)


a = int(input("请输入消费金额："))
print(appy(a))

'''

'''
82.    本金10000元存入银行，年利率是千分之三。每过1年，将本金和利息相加作为新的本金。计算5年后，获得的本金是多少？


思路： 复利问题
while True:
    def sum (n):
        sum = 10000 *(1+0.003)**n
        return sum
    n = int(input("请输入存款年数："))
    print(sum(n))
    
    1. 10000*(1+0.003)                       1
    2. 10000*(1+0.003)*(1+0.003)             2
    3.10000*(1+0.003)*(1+0.003)*(1+0.003)     3
    4.10000**(1+0.003)**4
    5. 10000*(1+0.003)**5
    
'''

'''
83.
"   编写一个游戏级别评分器，循环录入每一局（共10局）的游戏得分，显示输出游戏级别。评分标准：
10局中如果90%达到80以上，为一级，如果60%达到80之上为二级，其余为三级。"

答案：


def score(li):
    li.sort()
    if (li[0]<80 <li[1] )| (li[0]>80):
        print('一级')
    elif li[3]<80 <li[4]:
        print("二级")
    else:
        print("三级")
i = 1
li = []
while i<=10:
    a = int(input('请输入第%d局分数:'%i))
    i+=1
    li.append(a)
score(li)
'''
'''
84.
"   登录QQ时，QQ号和密码必须正确并且匹配才能够登录成功。假设最多只允许用户输入三次，中间任何一次输入正确，
则给出提示：登录成功。如第一次输入信息有误，则给出提示：QQ号或密码输入有误，请重新输入，您还有2次机会。
第二次还输入有误，则给出：QQ号或密码输入有误，请重新输入，您还有1次机会。
第三次如输入还有误，则给出提示：您三次输入都有误，请与管理员联系。"


答案：
def login():
    t= 0
    for i in range(3):
        b = random.randrange(0,2)
        # print(b)
        if not b == 1:
            t +=1
            if not t ==3:
                print('QQ号或密码输入有误，请重新输入，您还有%d次机会' % (2 - i))
            else:
                print('您三次输入都有误，请与管理员联系')

        else:
            print("login success")
            break

login()
'''

''''

打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%d\t' %(j,i,i*j) ,end='')
    #  输出换行  外层执行结束后，输出 空格 默认 换行
    print()

'''

# str = '12345'
# str1=str[0:-1]
# print(str1)
# while True:
#     if
#     a = input('请输入要查询的字母数字或者符号：')
#     print(ord("a"))
# print(ord("A"))

'''
85.
   编写方法从键盘输入2016年的某个月份，得到当月的天数
   
   def days(month):
    if month in [1,3,5,7,8,10,12]:
        print("查询结果为：%d月有 31 天"%month)
    elif month in [4,6,9,11]:
        print("查询结果为：%d月有 30 天"%month)
    else:

        print('查询结果为： %d月有 29 天" % month')

    return
a = int(input('请输入要查询的月份：'))
days(a)
'''
'''
86.
   编写方法输入两个数m和n，分别输出这两个数的最大公约数和最小公倍数

思路：
最大公约数：

 1.  先找 各自的约数  第 一个数  m%n = 0  n 的范围  range(1，m+1)  
    然后放到一个列表中 
    2， 同理 另一个数的 公约数     再放到 列表中 
    3， 取 两个列表的  公有 元素  到 新的列表中    取完全 
    4.   在新的列表中 取 最后一个元素  即 最大 公约数  
    ps： 在 遍历 放数据的时候   从小到大   追加 都是 有顺序的，，最后的 最大 
    
最小公倍数：
1.  先判断  两个元素 是否 是 倍数 关系  是 则  出 结果 
否则：如下  
    1   如果 一大 一小   大 的 数   从 1   开始 乘    一致到 被乘数 是  另一个数 
      c= m* 1  c2 = m * 2  .。。。 cn = m *n 
      把 c 放到 一个列表 l1 中
    2，  同理
     把 另一个数 的   同样乘积的 式子 d 放到 另一个 列表 l2 中
    3.列表 很可能  一大一小（通常）  或者  等长  
    4，  取 最小 公倍数    遍历   短列表的 元素   如果  该元素 in 另一个 列表中    立马 取 出来
    同样 有序   肯定是   最小公倍数  
     
    

li1 = []
li2 = []
li3 = []
li4 = []
li5 = []
def fun(m,n):
    for i in range(1,m+1):
        if m % i == 0:
            li1.append(i)
        else:
            continue
    for j in range(1,n+1):
        if n % j == 0 :
            li2.append(j)
        else:
            continue
    if len(li1) > len(li2):
        #  把  长度 短的 列表中的元素( 条件  包含在 另一个列表中的) 放到 新的 列表中 
        for  i in range (len(li2)):
            if li2[i] in li1 :
                li3.append(li2[i])
    else:
        for i in range (len(li1)):
            if li1[i] in li2 :
                li3.append(li1[i])
    #      公约束 已经 有序 放到 一个新的 列表中了  取 最后一个   即  最大 公约数 
    print('最大公约数为：%d'%li3[-1])
#         最小公倍数
    if m > n:
        if m % n == 0 :
            print('%d与%d的最小公倍数为：%d'%(m,n,m))
        else:
            #    m >  n
            #  c = m* 1  c =  m*2    c = m*3  ... c =  m*n
            for i in range(1,len(n+1)):
                c = m * i
                li4.append(c)
            for j in range(1,len(m+1)):
                d = n * j
                li5.append(d)
        #  m > n   len(li4)< len(li5)
        for i in range(len(li4)):
            if li4[i] in li5:
                print('%d与%d的最小公倍数为：%d' % (m, n, li4[i]))
            else:
                continue
    else:
        #  m < n  n 大于 m
        if n % m == 0 :
            print('%d与%d的最小公倍数为：%d'%(m,n,n))
        else:
            #    n >  m
            #  c = n* 1  c =  n*2    c = n*3  ... c =  n*m
            for i in range(1,m+1):
                c = n * i
                li4.append(c)
            for j in range(1,n+1):
                d = m * j
                li5.append(d)
        #  n > m    len(li4)< len(li5)
        for i in range(len(li4)):
            if li4[i] in li5:
                print('%d与%d的最小公倍数为：%d' % (m, n, li4[i]))
            else:
                continue
a = int(input("请输入第一个数："))
b = int(input("请输入第二个数："))
fun(a,b)
'''
'''
87.
   写一个方法void PrintArray(int[] arr)，在方法内依次打印出列表arr每个元素的值。

def fun(li):
    for i in li:
        print(i)
fun([1,2,3,4,5,6])
'''

'''
88.
   写一个方法int Sum(int[] arr)，计算列表arr所有元素的和(注意返回值)。

def sum(li):
    sum = 0
    for i in li:
        sum += i
    return  sum
print(sum([1, 2, 3, 4, 5, 6, 7, 8, 9]))
'''
'''
89.
   写一个方法int OddSum(int[] arr)，计算列表arr所有奇数下标元素的和(注意返回值)。
   
   
def odd_sum(li):
    sum = 0
    for i in range(len(li)):
        if  i % 2 ==  0 :
            # print(li[i])
            sum += li[i]
        else:
            continue
    return sum


print(odd_sum([1, 2, 3, 4, 5]))
'''

'''
89.   写一个方法int EvenSum(int[] arr)，计算列表arr所有偶数下标元素的和(注意返回值)。


def odd_sum(li):
    sum = 0
    for i in range(len(li)):
        if not  i % 2 ==  0 :
            # print(li[i])
            sum += li[i]
        else:
            continue
    return sum


print(odd_sum([1, 2, 3, 4, 5]))



'''

'''
91.   写一个方法可以计算两个数的和，想想这个方法有哪些参数，返回值是什么类型。

def sum(a,b=5):
    return  a+b
print(sum(3,88))
print(type(sum(3)))
# 参数： a b  int

'''

'''
92.
   写一个方法可以计算两个数的商(分母不能为0)，想想这个方法有哪些参数，返回值是什么类型。
答案：
def division(a,b):
    return a//b


print(division(9, 3))
print(type(division(9, 3)))
#  小结： 类型  取决于  符号 是 /  还是 //  前者 float   后者  是 int
'''

'''
93.
"   写一个方法将传入的天、小时、分钟、秒的总和转换为秒，比如0天、2小时、5分、7秒，他们代表的总秒数为2*3600+5*60+7=7507秒。
想想这个方法有哪些参数，返回值是什么类型。"

def seconds(days,hours,minuites,seconds):
    return days*24*3600+hours*3600+minuites*60+ seconds


print(seconds(0, 4, 5, 30))
print(type(seconds(0, 4, 5, 30)))
#   返回 类型 为  int

'''

'''
94.
   写一个方法交换整型列表中两个指定下标元素的值。想想这个方法有哪些参数，返回值是什么类型。
def  swap(li,a,b):
    li[a],li[b] = li[b],li[a]
    return li


print(swap([1, 2, 3, 4, 5], 4, 2))
返回  int 类型 
'''
'''
95.
   写一个方法计算整型列表中所有能被3整除元素的个数。想想这个方法有哪些参数，返回值是什么类型。


def  be3dvision(li):
    n = 0
    for i in range(len(li)):
        if li[i] % 3 == 0 :
            n += 1
    return  n


print(be3dvision([1, 2, 3, 4, 5, 6, 7, 8, 9]))

'''
'''
96.
"   写一个方法将整型数字(int)转换为格式化的字符串(string)，现要求如下：
   a.可以指定转换后[字符串的长度];
   b.当数字的长度不足指定的长度，让这个字符串右对齐，指定[左边补的字符(char)];
   例如，假设现在将指定的数字转换为固定长度为8的字符串，如果长度不足，左边补'0'，那么27这个数字就会转换为字符串""00000027""。
   根据要求，想想这个方法有哪些参数，返回值是什么类型。"

补充：
#  两个列表求和  生成一个新 的 列表   首推 列表 生成式 
li1=[1,2,3,4,5]
li2= [6,7,8,9,10]
li3 = [li1[i]+li2[i] for i in range(len(li1))]
# c = sum[li1,li2]
print(li3)

'''

'''
97.
    "   用方法实现找出一个int类型列表中最大值和最小值 
   void  FindNumber(int[]nums,out int max,out int min)"


def  fun(li):
    print(max(li), min(li))
    return
fun([1,2,3,4,5])
'''

'''
98.
   编写方法将24的所有因子求积、求和

答案：
def fun(a):
   sum = 0
   multiply  = 1
   for i in range(1,a+1):
       if a % i == 0 :
           print(i)
           # sum += i
           multiply *= i
   print(sum,multiply)


fun(24)
'''
'''
99.
   判断一个数是否是质数(素数)？该如何声明方法？

def  zhishu(a):
    if a > 1:
        for i in range(2,a):
            if a % i == 0:
                print('%d不是质数'%a)
                break
            # else 忽略
        print('%d是质数' % a)
    else:
        print('%d不是质数' % a)
zhishu(5)
'''

'''
100.
   写一个方法将传入的秒数转变为几小时几分几秒返回。
   
   def transform(seconds):
    hour = seconds//3600
    minute = (seconds%3600)//60
    second = (seconds%3600)%60
    print('%d秒 转换为 %d 时 %d 分 %d 秒' %(seconds,hour,minute,second))

transform(3800)

 '''

'''
101
   使用Random类给一个列表的所有元素赋随机初值（不重复）
   
   
   理解错了；  列表的所有元素
   
   li= [0,0,0,0,0,0,0]
def fun(li):
    t=0
    while t < len(li):
        # print(i,end='')
        b = random.randrange(100)
        if b in li:
            continue
        else:
            print(b,end='，')
            li.append(b)
        t += 1
    print(t)
    # li.sort()
    return li
li =[0,0,0,0,0,0]
print(fun(li)) 



标准答案：


    import random

def init(ls):
    for i in range(0, len(ls)):
    #前半部分 列表    用于判断是否重复 
    
    # 调用 getNum 函数  li[0:1] 列表的前半部分
        ls[i] = getNum(ls[0:i], 1, 15)

# 生成一个随机数，要求与preLs列表中的数据都不相同 
def getNum(preLs, min, max):
    isChongfu = True
    while isChongfu:
        value = random.randint(min, max)
        # 遍历第i位之前的列表位置，依次与value比较，若发现相等，则需要重新随机
        isChongfu = False
        for item in preLs:
            if item == value: 
                isChongfu = True
                break
    #   最终结果是   返回 一个 不重复的 数 ，，然后  给  li[i]
    return value

ls = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
init(ls)
print(ls)
  
小结：  
  li[i ] = 0  
  直接修改列表的某个值
  
  
  参考答案：https://blog.csdn.net/qq_42707739/article/details/106505455
  
import random


def fuzhi(num):
    len = 0  ##记录列表中元素的个数
    ls = []  ##空列表
    while len <= num:
        a = random.randint(0, num)
        if ls.count(a) == 0:  ##判断生成的这个随机数是否在列表中，不在则添加，在则跳过，通过count值来判断
            ls.append(a)
            len += 1
        else:
            continue
    print(ls)


num = int(input("请输入需要创建的列表长度："))
fuzhi(num)



'''
'''
102.
"   写一个方法用于判断一个整型列表是否是对称的。所谓对称就是第一个元素等于最后一个元素，第二个元素等于倒数第二个元素，
依次类推，例如【7，3，1，3，7】就是对称的"

参考：  https://blog.csdn.net/qq_42707739/article/details/106505455
def duichen(ls):
    i = 0
    j = len(ls)-1
    flag = True
    for k in range(0,len(ls)//2):
        if ls[i] != ls[j]:
            flag = False
            break
        i += 1
        j -= 1
    return flag
    
ls = [1,2,3,4,5,6,5,4,3,2,1,]
if duichen(ls):
    print("{}是对称的".format(ls))
else:
    print("{}是不对称的".format(ls))
    
    
    
    
def  duichen(li):
    i = 0
    k = len(li)
    flag1 = True
    for j in  range(0,k//2):
        #  当使用 索引时    末尾 索引 为  长度 减一
        if not li[i] == li[k-1]:
            flag1 = False
            break
        i += 1
        k -= 1
    return flag1

li = []
while True:
    flag = None
    try:
        a = int(input("请输入列表元素："))
    except:
        pass
    if not a == 0:
        li.append(a)
        print(li)
    else:
        break



print(duichen(li))

if duichen(li):
    print("%s对称" %li)
else:
    print("%s不对称" % li)
    
    
    小结：  return  返回值 是 最终结果，，通过调用函数 可 直接得到  
'''

# def get_houzhui(s):
#     print("后缀名是:",s[s.rfind(".")+1:])
# s = input("请输入需要获取文件后缀的路径:")
# get_houzhui(s)
# s = '1213.py'
# t = s.rfind(".")
# #  t 返回的是  从前往后的  索引  ，
# print(t)

'''

103.     打印一个列表内的所有素数的值


答案：

def  sushu(li):
    t = 0
    for i in range(len(li)):
        flag = True
        for j in range(2,li[i]):
            if li[i] % j == 0 :
                flag = False
                break
        if flag & (li[i] != 1):
            print(li[i],end=',')
            t +=1
    print(t)

li = [x for x  in  range(1,101)]
sushu(li)



def  sushu(li):

    for i in range(len(li)):
        if li[i] <=1:
            pass
            # print('不是质数%d'%li[i])
        else:
            for  j in range(2,li[i]):
                if li[i] % j == 0:
                    # print('不是质数%d' % li[i])
                    break
                else:
                    print('是质数%d'%li[i])
                    break



sushu([1,2,3,4,5,6,7])


小结：  两个答案 都对，，在对1  进行判断时，方法不同  
参考：

from math import sqrt
def sushu(number):
    li=[2]
    for n in range(2, number):
        j = 2
        while j < n:
            if n % j == 0:
                break
            j += 1
            if j >= n:
                li.append(n)
        j += 1
    print(li)
sushu(10)



参考二：
# import math
# l = [x for x in range(1,101) if 0 not in [x%y for y in range(2,int(math.sqrt(x))+1)]]
# print(len(l))
# print(l)
'''

'''
104:
   查找一个列表中某个值是否存在，如果存在返回这个值的索引，否则返回-1。


def find(li,a):
    flag = False
    if a in li:
        flag = True
    return flag

li = [1, 2, 3, 4, 5]
a = 6
b = find(li, a)
if b:
    print(li.index(a))
else:
    print('-1')
#    上面  可以修改参数  代码太多 

简洁

def find (li,a):
    if a in li:
        print(li.index(a))
    else:
        print(-1)
li = [1,2,3,4,5]
b = 3
find(li,b)
    
    
'''

'''
105.
      将一个列表某一部分反转过来，比如【2，3，1，4，7】转换为【2，4，1，3，7】 

def  swap(li,a,b):
    a_index = li.index(a)
    b_index = li.index(b)
    li[a_index],li[b_index] = li[b_index],li[a_index]
    return li
li = [1,2,3,4,5,6,7]
print(swap(li, 4, 6))

'''

'''
106.
   求一个列表的第二大的值

def sec_max(li):
    li.sort()
    sec_max = li[-2]
    return sec_max
li= [1,2,3,4,5]
print(sec_max(li))
'''
'''
107.
   写一个方法，实现在列表中指定的的位置前插入一个值

def insert(li,index,obj):
    li.insert(index,obj)
    return  li
li = [x for x in range(11,16)]
print(li)
print(insert(li, 3, "e"))
'''

'''
108.
   写一个方法，删除列表中指定位置的元素

def fun(li,index):
    del li[3]
    # li.remove(index)
    return li
li = [x for x in range(22,28)]
print(li)
print(fun(li, 4))
'''

'''
109.
"猜数游戏
1.随机出现一个数(范围自定义) 作为答案
2.提示用户输入并根据答案和用户输入的大小关系输出大了? 小了?
3.5次机会
4.可以重复玩
5.根据猜对的次数进行评价
6.无论对错 请告知答案"

while True:
    def game():
        a = random.randint(0,6)
        print(a)
        i = 5
        t = 0
        while i >0:

            if t == 1:
                print('游戏开始了')
            time.sleep(1)
            b = int(input("请输入你数值："))
            i -= 1
            try:
                if a > b:
                    t += 1
                    # print("小了")
                    # t  +=1
                    if t <5:
                        print('小了','你还有%d次机会'%(5-t) )
                    else:
                        print('很遗憾，结果为%d' % a)

                elif a < b:
                    t += 1
                    if t <5:
                        print('大了','你还有%d次机会'%(5-t) )
                    else:
                        print('很遗憾，结果为%d' % a)



                else:
                    t += 1
                    if t ==  1 :
                        print('恭喜你1次就答对了，结果为%d'%a)
                    else:
                        print('猜了%d次,结果为%d' % (t,a))


                        if t <=2:
                            print("评级为：A")

                        elif 2<t<=4:
                            print("评级为：B")

                        else:
                            print("评级为：C")



                    break
            except:
                pass
    # break

    game()



总结：  没什么思路，，看着效果改代码
'''

'''
110.
"   写一个方法，参数为字符串类型，返回值也为字符串类型，方法内对传入的字符串进行遍历，
找出所有的大写字母并连接成新的字符串，遍历结束后将新连接成的字符串返回。"

思路： 每个字符 对应的都有  ASCII 码，以此  为 线索，，作为 转换的  依据   展开  做题


def  bianli(str):
    str1 = ''
    for i in range(len(str)):
        if 65 <= ord(str[i]) <= 90:
            # print(ord(str[i]),str[i])
            str1 = str1+str[i]
    return str1
str='ABCDZabcdz'
print(bianli(str))
print(type(bianli(str)))

# for i in range(len(str)):
#     print(str[i],ord(str[i]))

# print(chr(90))  Z   结果为  字符串

输出也为  字符串   

'''

'''
111.
   持续获取用户输入，直到用户输入的字符串中既有字母又有数字。

'''

# def func(str):
#     while True:
#         try:
#
#             a = input('请开始输入：')
#             str += a
#             print(str)
#         except:
#             pass
#
#         if str.isalnum():
#             break
#
#     return str
#
# str=''
# print(func(str))

# while True:
#     str1 = ''
#     # ten = None
#     try:
#       ten = int(input("x:"))
#       str1 += ten
#
#       print(str1)
#     except:
#         pass
#     # if type(ten) == int:
#     if str1.isalnum():
#         break


'''
112.
   写一个方法将整型数字(int 不含0)转换为汉字大写格式。例：111=>壹佰壹拾壹

    
'''
'''
113.
"根据用户输入的行数打印出类似下面的图形：
例：4行
   *
  **
 ***
****"


def fun(n):
    t = 1
    while n > 0:
        print(' '*(n-1),end='')
        print('*'*(t))
        n -= 1
        t +=1
fun(6)

'''

'''
114.
   写一个方法传入字符串参数，获取字符串中所有的数字。
# print(chr(65))
print(ord('0'))
print(ord('9'))


答案：

def num(str):
    for i in range(len(str)):
        if 48<=ord(str[i]) <= 57:
            print(str[i],end='')


str = '1qr2s3f4sfg5'
num(str)
'''

'''
115.
   写一个方法，传入两个整型列表，方法将两个列表进行合并，并返回合并后的列表。

def fun(li1,li2):
    # li1+=li2
    li1.extend(li2)
    return li1
li1 = [1,2,3]
li2 = [4,5,6]
print(fun(li1, li2))

小结： +  和 extend   效果一样，，extend  更 节省内存，，+   实质上 开辟了 一块新的 内存 
'''

'''
116.
"编写一个程序，输入两个字符串存储到2个字符串变量中，交换两个字符串的首尾两个字符并显示结果
例: abc ojk =>obk ajc"


'''
#
# #
# # def swap(str1,str2):
# #     print(str1)
# #     print(str2)
# #     # str1.index(str[0]),str2.index(str[0]) = str2.index(str[0]), str1.index(str[0])
# #     # str1.index(str[-1]),str2.index(str[-1]) = str2.index(str[-1]), str1.index(str[-1])
# #     str1.index(str1[0]),str2.index(str2[0]) = str2.index(str2[0]), str1.index(str1[0])
# #     str1.index(str1[-1]),str2.index(str2[-1]) = str2.index(str2[-1]), str1.index(str1[-1])
# #
# #     print(str1)
# #     print(str2)
# str1 = '123'
# str2 = 'abc'
# print(str1[0])
# a = str1[0]
# b = str1[0]
# c = str1[0]
# d = str1[0]
#
# del a
# del b
# del c
# del d
# str1.
#
# # str1.replace(str1[0],str2[0])
# # str2.replace(str2[0],str1[0])
# # str1.replace(str1[-1],str2[-1])
# # str2.replace(str2[-1],str1[-1])
#
# print(str1,str2 )
#
# # swap(str1,str2)


'''
117.
持续获取用户输入，直到用户输入的字符串全由字母组成。


str = '123'
print(str.isalnum())
#  返回一个bool 值

def fun():
    while True:
        str = input('请输入字符串：')
        if  not str.isalpha():
            pass
        else:
            break


fun()


'''

'''
118.
列出1-100之间的相邻质数的所有差值(相同得差值只显示一次)。

'''

# def diff():
#     li = []
#     for i in range(2,101):
#         for j in range(2,i):
#             if not i % j == 0:
#                 li.append(i)
#                 break
#     print(li)

# diff()
# def  zhishu(li):
#     li1 = []
#     for i in range(len(li)):
#         if li[i] > 1:
#             for j in range(2,li[i]):
#                 if li[i] % j == 0:
#                     # print('%d不是质数'%li[i])
#                     break
#                 # else 忽略
#             print('%d是质数' % li[i])
#             li1.append(li[i])
#
#         else:
#             # print('%d不是质数' % li[i])
#             pass
# c = [x for x in range(1,101)]
# zhishu(c)
# print([x for x in range(1,1)])


'''
119.
为一个长度为100的字符列表随机赋值(a-z A-Z 0-9),然后判断’q’’i’’k’’u’这个字符序列是否在随机产生的列表中



#  进行判断 
def fun(li):
    flag = False
    if ('q'in li)&('i' in li )&('k' in li)&("u" in li):
        flag = True
    return flag


#   生成 列表
b = [x for x in [x for x in range(48,58)]+[x for x in range(65,91)]+[x for x in range(97,123)]]
t = 0
li = []
li2 = []
while t<100:
    t+=1
    a = random.choice(b)
    li.append(chr(a))
    # 把 小写字母放到 一个 列表中  方便 人工核验 
    if 97<=a < 123:
        li2.append(chr(a))



# 调用函数  
print(fun(li))
# print(a)
# print(chr(a))
# print(b)
print(li)
print(li2)
# print('a' in li)
# print(t)


#实验   生成  一个 符合要求的表  
# print([x for x in range(58, 68)] + [x for x in range(65, 91)] + [x for x in range(97, 123)])
#
# b= [58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]
# a = random.choice(b)
#
# print(a)
# print(chr(a))
'''

'''
120.
验证一个字符列表的字符序列是否出现在另外一个字符列表中。

def yanzheng(li1,li2):
    if len(li1)<len(li2):
        smaller = li1
        bigger = li2
    else:
        smaller = li2
        bigger = li1
    for i in range(len(smaller)):
        flag = False
        if smaller[i] in bigger:
            flag = True
    return flag
    
    
li1= ['a','b','c','d']
li2 = ['a','b']
print(yanzheng(li1, li2))


'''

'''
121.
   写一个方法将一个列表合并到另外一个列表中的指定位置。
   知识点： list.insert(index,obj)
def fun(li1,li2,index):
    #  把 li2 插入到 li1的 指定位置 
    li1.insert(0,li2)
    return li1
li1 = [1,2,3]
li2 = ['a','b','v']
print(fun(li1, li2, 0))

'''

'''
122.
"银行账户管理系统（BAM）
写一个账户类(Account)：
字段: id:账户号码 长整数
password:账户密码
name:真实姓名
personId:身份证号码 字符串类型
email:客户的电子邮箱
balance:账户余额
方法:
Deposit: 存款方法,参数是double型的金额
Withdraw:取款方法,参数是double型的金额
构造方法:
有参和无参,有参构造方法用于设置必要的字段值"

老师答案：

class Account:
    id = ""
    password = ""
    name = ""
    personId = ""
    email = ""
    __balance = 0 # 账户余额

    def __init__(self, id, password, name, personId = "默认pid"):
        self.id = id
        self.password = password
        self.name = name
        self.personId = personId
        #self.email = email
        self.__balance = 0


    # 存钱
    def deposit(self, money):              #money为参数 意为存款金额
        self.__balance += money

    # 取钱
    def withdraw(self, money):            # 期款 同上
        self.__balance -= money

    def getBalance(self):
        return self.__balance

#id, password, name, personId, email, balance
acc1 = Account("1", "123", "abc", "985996u494")
#acc1.balance = 100000000000
acc2 = Account("12", "123", "abc", "985996u494")
acc1.deposit(100)
print(acc1.getBalance())
print(acc2.getBalance())

自己写：
 class Account:
#     def __init__(self, id, account, password, name, personId, email, blance):
#         self.id = id
#         self.account = account
#         self.password = password
#         self.name = name
#         self.personId = personId
#         self.email = email
#         self.blance = blance
#
#     def  Deposit(self,a):
#         self.blance += a
#
#     def  Withdraw(self,b):
#         self.blance -= b
#
#     def   getblance(self):
#         return self.blance
#
# a = Account(1,122,123,"zhangsan",789,"12@zhangsan.com",500)
# a.blance = 500
# v = a.Deposit(1000)
# print(a.blance)
# print(a.getblance())
# # w = a.Deposit(400)
# # print(a.blance)
# # print(a.getblance())

@property： 放在函数 头上 可以把定义的方法 变为 属性，可以像调用变量一样调用  该函数，，不用加 括号 

@property.setter   可以为 函数  赋值，，就像成员 变量一样   


'''
'''
继承：  

        继承父类的成员方法 和 成员变量
        
        不能继承  __inin__ 方法
        
        3.  可以重新 赋值   父类的 方法，，调用对象  不同，，，  结果 不同 
class Animal:
    # def __init__(self,color):
    color = 'red'


class Person(Animal):
    color = '黑色'


p = Person()

print(p.color)
'''

'''

'''

#
# for  i in range (1,100):
#     print(i)
#     if i >= 55:
#
#         continue
#
# print('循环结束')

'''
逢七过

for  i in range(1,100):

    if (i % 7 == 0) | ('7' in str(i)):
        print('%d过'%i)
        continue
    print(i)
'''

'''
输出100内的所有素数

t = 0
for i  in range(2,101):
    flag = True
    for  j  in range(2,i):
        if i % j == 0 :
            flag =  False
            # print('%d 不是素数'%i)
            break
    if flag == True:
        t +=1
        print('%d 是素数'%i)

print(t)
'''

#
'''
103.
打印一个列表内的所有素数的值


def  sushu(li):
    t = 0
    for i in range(len(li)):
        flag = True
        for j in range(2,li[i]):
            if li[i] % j == 0 :
                flag = False
                break
        if flag & (li[i] != 1):
            print(li[i],end=',')
            t +=1
    print(t)

li = [x for x  in  range(1,101)]
sushu(li)


法二：
def  sushu(li):

    for i in range(len(li)):
        if li[i] <=1:
            pass
            # print('不是质数%d'%li[i])
        else:
            for  j in range(2,li[i]):
                if li[i] % j == 0:
                    # print('不是质数%d' % li[i])
                    break
                else:
                    print('是质数%d'%li[i])
                    break
'''


'''
122.
"银行账户管理系统（BAM）
编写管理账号的几个方法（和Main同级的方法）：
1.用户开户,需要的参数:id,密码,密码确认,姓名,身份证号码,邮箱,账户类型(int),返回新创建的Account对象
2.用户登录,参数:id,密码 返回Account对象,提示 用s1.equals(s2)判断s1和s2两个字符串内容是否相等
3.用户存款,参数:id,存款数额,返回修改过的Account对象
4.用户取款,参数:id,取款数额,返回修改过的Account对象
用户会通过调用以上的方法来操作自己的账户,请分析各个方法需要的参数"


答案：

class Account:
    def __init__(self,id=0,password=110,comfirm_password=110,name='zhangsan',ID=123,email="zhangsan@qq.com",type=int,balance =0 ):
        self.id= id
        self.password = password
        self.confirm_password = comfirm_password
        self.name = name
        self.ID = ID
        self.email = email
        self.type = int
        self.__balance = 0

    def login(self,id):
        password = int(input("请输入密码:"))
        if password == self.password:
            print('登陆成功')
        else:
            print("密码错误")

    def deposit(self,id,money):
        self.__balance +=money
        return self.__balance

    def withdraw(self,id,money):
        self.__balance -=money
        return self.__balance
    @property
    def  getmoney(self):
        return  self.__balance


zhangsan = Account()
zhangsan.set_account()
# zhangsan.login(1)
# zhangsan.getmoney
zhangsan.deposit(1,40)
print(zhangsan.getmoney)
zhangsan.withdraw(1,10)
print(zhangsan.getmoney)

'''
'''
123.
    "银行账户管理系统（BAM）
编写管理账号的几个方法（和Main同级的方法）：
1.用户开户,需要的参数:id,密码,密码确认,姓名,身份证号码,邮箱,账户类型(int),返回新创建的Account对象
2.用户登录,参数:id,密码 返回Account对象,提示 用s1.equals(s2)判断s1和s2两个字符串内容是否相等
3.用户存款,参数:id,存款数额,返回修改过的Account对象
4.用户取款,参数:id,取款数额,返回修改过的Account对象
用户会通过调用以上的方法来操作自己的账户,请分析各个方法需要的参数"

'''




'''
124.
创建一个学员类，并设计三个字段用于表示学生的成绩（语文、数学、英语）；然后定义一个列表表示一个班的学生（10人），
依次输入每个学生的信息和成绩，输入的同时将学员的每科成绩划分等级（100-90：A 89-80：B 79-70：C 69-60：D 60以下：E）最后输出所有学员的信息


#   不足：  未能显示 学员信息 
class Student:
    def __init__(self,yuwen=60,shuxue=60,yingyu=60):
        self.__yuwem = yuwen
        self.shuxue = shuxue
        self.yingyu = yingyu


    def input_score(self):
        a= int(input("请输入语文成绩："))
        self.grade(a)
        b= int(input("请输入数学成绩："))
        self.grade(b)
        c= int(input("请输入英语成绩："))
        self.grade(c)

    def list(self):
        for i in range(3):
            self.input_score()
        return 

    def grade(self,score):
        if score>=90:
            print("等级为:A")
        elif score >= 80:
            print("等级为:B")
        elif score>=70:
            print("等级为:C")
        elif score>=60:
            print("等级为:D")
        else:
            print("等级为:E")

student = Student()
student.list()

'''
'''
125.
"编一个关于求多个某门功课总分和平均分的程序。
1.每个学生信息包括姓名和某门功课成绩。
2.假设5个学生。
3.类和对象的处理要合理"


未完成：
    class Fun:
    def __init__(self,name='',yuwen=60,shuxue=60,yingyu=60):
        self.name = name
        self.yuwen = yuwen
        self.shuxue = shuxue
        self.yingyu = yingyu
        
        
        
        
    def input_score(self):
        sum1, sum2, sum3, avg = 0, 0, 0, 0
        a = int(input("请输入语文成绩："))
        b = int(input("请输入数学成绩："))
        c = int(input("请输入英语成绩："))
        sum1 += a
        print(sum1)



    # def score(self):
    #     for i in range(3):
    #         self.input_score()

    def score(self,score):
        # sum1 ,sum2,sum3,avg =0,0,0,0
        for i in range(3):
            self.input_score()
            # sum1 += score
            # sum2 += score
            # sum3 += score
        avg = score/3
        print('总分为：%d'%score)
        print('平均分为：%d'%avg)

fun =Fun()
fun.score(1)



'''
'''
126.
    尝试写一个学员类，想一想都应该有些什么变量和方法，并产生5个对象来表示你自己及身边的四位同学吧，
    你觉得程序中的对象和你们是什么关系？学员类和你们又是什么关系？

class Student:
    #  变量
    def __init__(self,name,age=18,sex ='男'):
        self.name = name
        self.age = age
        self.sex = sex

#      方法
    def speak(self):
        print(self.name+'说 你好')

    def walk(self):
        print(self.name+"在散步")

zhangsan = Student('zhangsan')
print(zhangsan.age)
zhangsan.speak()

lisi = Student('lisi')
lisi.walk()


'''

'''
127.
"员工类：字段：名字、工号、部门、工资 方法：涨工资
请写出测试方案"

class Emplyee:
    def __init__(self,name = '',id= '',part='',salary = ''):
        self.name = name
        self.id = id
        self.part = part
        self.salary = salary

    def up_salary(self):
    
        #  被谁调用 ，，谁说
        print(self.name+'说：涨工资')

zhangsan = Emplyee('zhangsan')
zhangsan.up_salary()

'''

'''
128.
电脑类：字段：牌子，主板，cpu，内存，显示器，显卡等，方法：运行


class Computer:
    #  设为空   默认 程序 也 可以运行， 方便 省时间
    def __init__(self,brand='联想',zhuban='',cpu='',neicun='',screen='',xianka=''):
        self.brand = brand
        self.zhuban = zhuban
        self.cpu = cpu
        self.neicun = neicun
        self.screen = screen
        self.xianka = xianka
    def run(self):
        print(self.brand+'电脑在运行')

computer = Computer()
computer.run()
'''


'''
129.
"BAM系统续集:
1.将Account类作成完全封装,注意:要辨别每个属性的是否需要公开
2.添加新的银行的客户类：储蓄账户(SavingAccount)和信用账户(CreditAccount),区别在于储蓄账户不允许透支,
而信用账户可以透支,并允许用户设置自己的透支额度.
注意:CreditAccount需要多一个属性 ceiling 透支额度"


class Account:
    def __init__(self,id=0,password=110,comfirm_password=110,name='zhangsan',ID=123,email="zhangsan@qq.com",type=int,balance =0,card_type='SavingAccount',ceiling =20):
        self.id= id
        self.password = password
        self.confirm_password = comfirm_password
        self.name = name
        self.ID = ID
        self.email = email
        self.type = type
        self.__balance = balance
        self.card_type = card_type
        self.ceiling = ceiling

    def login(self,id):
        password = int(input("请输入密码:"))
        if password == self.password:
            print('登陆成功')
        else:
            print("密码错误")

    def deposit(self,id,money):
        self.__balance +=money
        return self.__balance

    def withdraw(self,id,money):
        self.__balance -=money
        return self.__balance
    @property
    def  getmoney(self):
        return  self.__balance


zhangsan = Account()
zhangsan.ceiling = 700
print(zhangsan.ceiling)

# zhangsan.set_account()
# zhangsan.login(1)
# zhangsan.getmoney
# zhangsan.deposit(1,40)
# print(zhangsan.getmoney)
# zhangsan.withdraw(1,10)
# print(zhangsan.getmoney)


'''

'''
130.
"编写Bank类
属性:
1.当前所有的账户对象的集合,存放在列表中
2.当前账户数量
3.当前登录用户

方法:
1.用户开户,由用户输入需要的参数:id,密码,密码确认,姓名,身份证号码,邮箱,账户类型(int),将新创建的Account对象放入账户列表中
2.用户登录,从用户输入中获取:id,密码 提示 检测用户列表内是否有此用户，若登录成功，将匹配到的对象放入当前登录用户中
3.用户存款,判断用户是否登录，若登录，输入:存款数额,修改当前登录的Account对象，若未登录，提示登录
4.用户取款,判断用户是否登录，若登录，输入:取款数额,修改当前登录的Account对象，若未登录，提示登录
5.统计银行所有账户余额总数

用户会通过调用Bank对象以上的方法来操作自己的账户,请分析各个方法需要的参数

写个主方法测试你写的类"

   """
编写Bank类
属性:
1.当前所有的账户对象的集合,存放在列表中
2.当前账户数量
3.当前登录用户

方法:
1.用户开户,由用户输入需要的参数:id,密码,密码确认,姓名,身份证号码,邮箱,账户类型(int),
将新创建的Account对象放入账户列表中
2.用户登录,从用户输入中获取:id,密码 提示 检测用户列表内是否有此用户，
若登录成功，将匹配到的对象放入当前登录用户中
3.用户存款,判断用户是否登录，
若登录，输入:存款数额,修改当前登录的Account对象，若未登录，提示登录
4.用户取款,判断用户是否登录，
若登录，输入:取款数额,修改当前登录的Account对象，若未登录，提示登录
5.统计银行所有账户余额总数

用户会通过调用Bank对象以上的方法来操作自己的账户,请分析各个方法需要的参数

写个主方法测试你写的类
"""

class Bank:
    AllAccounts = [None,None,None,None,None] # 存放Account对象的列表
    AccountNum = 0 # 已开户账户数量
    CurAccount = None # 当前登录到银行系统的账户对象

    #开户：创建一个Account对象，存入self.AllAccounts列表中
    def CreateAccount(self, id, password, passwordRepeat, name, pId, email, accountType):
        # id不能和老id重复
        for oldAcc in self.AllAccounts:
            if oldAcc != None and oldAcc.id == id:
                return False
        # 两次输入的密码必须一致
        if password != passwordRepeat:
            return False
        # 开户数量不能大于5
        if self.AccountNum >= 5:
            return False

        # 正常开户
        acc = Account()
        acc.id = id
        acc.password = password
        acc.name = name
        acc.pId = pId
        acc.email = email
        acc.accountType = accountType
        acc.balance = 0

        self.AllAccounts[self.AccountNum] = acc
        self.AccountNum += 1
        return True

    # 用户登录:输入账户和密码，在self.AllAccounts列表中 找到对应的账户对象，
    # 保存到self.CurAccount中
    def Login(self, id, password):
        # 在银行中找账户（acc.id == id）
        acc = None
        for oldAcc in self.AllAccounts:
            if oldAcc == None:
                continue
            if oldAcc.id == id:
                acc = oldAcc
                break
        if acc == None:
            return False
        # 判断password == acc.password
        if acc.password == password:
            # 若登录成功，acc保存到self.CurAccount 中
            self.CurAccount = acc
            return True
        else:
            return False


    # 存钱
    def SaveMoney(self, money):
        if self.CurAccount == None:
            print("请先登录")
            return False

        self.CurAccount.balance += money
        return True

    # 取钱
    def GetMoney(self, money):
        if self.CurAccount == None:
            print("请先登录")
            return False

        self.CurAccount.balance -= money
        return True

    # 银行内所有账户的余额之和
    def TotalMoney(self):
        sum = 0
        for acc in self.AllAccounts:
            if acc == None:
                continue
            sum += acc.balance

        return sum

# 账户类
# id,密码,密码确认,姓名,身份证号码,邮箱,账户类型(int),账户余额
class Account:
    id = ""
    password = ""
    name = ""
    pId = ""
    email = ""
    accountType = 0
    balance = 0

def test():
    b = Bank()
    if b.CreateAccount("1", "1", "1", "1", "1", "1@1.com", 0) == False:
        print("开户失败")
        return
    if b.CreateAccount("2", "2", "2", "2", "2", "2@2.com", 0) == False:
        print("开户失败")
        return

    if b.Login("2", "2") == False:
        print("登录失败")
        return

    if b.SaveMoney(1000) == False:
        print("存钱失败")

    if b.GetMoney(500) == False:
        print("取钱失败")


    print("银行总余额：%s"%(b.TotalMoney()))

test() 
'''

'''
131.
    "定义一个人类Person：
1)定义一个方法SayHello()，可以向对方发出问候语“hello,my name is XXX”
2)有三个属性：名字、身高、体重
3)通过构造方法，分别给三个属性赋值
4)在Program类，Main方法里面：
1、创建两个对象，分别是zhangsan，1.73，55；lishi，1.80，65
2、分别调用对象的SayHello()方法。"

class  Person:
    #  构造方法  __init__
    def __init__(self,name='zhangsan',hight='166cm',weight='50kg'):
        self.name = name
        self.hight = hight
        self.weight = weight
    def SayHello(self):
        print('hello,my name is '+self.name)

class Program:
    def Main(self):
        person1 = Person('zhangsan',1.73,55)
        person2 = Person('lishi',1.80,65)

        person1.SayHello()
        person2.SayHello()

        return

p = Program()
p.Main()


'''

'''
132.
"定义一个矩形类Rectangle：
1)定义三个方法：GetArea()求面积、GetPer()求周长，ShowAll()分别在控制台输出长、宽、面积、周长。
2)有2个字段：长length、宽width
3)通过构造方法Rectangle(int width, int length)，分别给两个属性赋值"

#  小结：  不用 传参  使用 self.length   self.width


class Rectangle:
    def __init__(self,width= 5,length = 6 ):
        self.width  = width
        self.length = length

    def GetArea(self):
        Area = self.width*self.length
        return Area
    def GetPer(self):
        Per = (self.width+self.length)*2

        return Per

    def ShowAll(self):
        print('宽是：%d'% self.width)
        print('长是：%d'% self.length)
        print('面积是：%d'%self.GetArea())
        print('周长是%d'%self.GetPer())


rectangle = Rectangle()
rectangle.ShowAll()

'''

'''
133.
"定义一个普通用户类
普通用户类具备的字段：用户名、密码、权限
普通用户类具备的方法：登录、注册
注意：请详细测试该类"

class  User:
    def __init__(self,username='',password='',auth=''):
        self.username = username
        self.password = password
        self.__auth = auth
        
        
    def login(self):
        print('现在开始登录')
        time.sleep(1)
        password = input("请输入用户名：")
        password = input("请输入密码：")
        if self.password == password:
            time.sleep(1)
            print('登录成功')
        else:
            print('密码错误，请重新登录')

    def register(self):
        print('现在开始注册')
        time.sleep(1)
        self.username = input('请输入用户名：')
        self.password = input('请输入密码：')
user = User()
user.register()
user.login()


'''

'''
134.
"编写一个时间类MyTime，包含一个三个参数的构造方法，3个成员变量hour,minute,second,
再加上一个转换成字符串的方法ToString。
注意：请注意时分秒的取值范围"


class Mytime:
    def __init__(self,hour,minute,second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def ToString(self):

'''

'''
135.
"编写一个日期类MyDate，包含一个构造方法，3个成员变量year,month,day，再加上一个转换成字符串的方法ToString。

请注意月和日的取值范围"


class MyDate:
    def __init__(self,year,month,day):
        self.hour = year
        self.minute = month
        self.second = day

    def ToString(self):
'''

'''
136.
"模拟简单的计算器。
定义名为Number的类，其中有两个整型数据成员n1和n2，声明为公有。编写构造方法，赋予n1和n2初始值，
再为该类定义加（Addition）、减（Subtration）、乘（Multiplication）、除（Division）等公有成员方法，
分别对两个成员变量执行加、减、乘、除的运算。
在Main方法中创建Number类的对象，调用各个方法，并显示计算结果。"

class Number:
    n1 = ''
    n2 = ''
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2
    def Addition(self):
        sum = self.n1 +self.n2
        return sum

    def Subtration(self):
        dif = self.n1 -self.n2
        return dif

    def Multiplication(self):
        ji = self.n1 *self.n2
        return ji
    def Division(self):
        s = self.n1 /self.n2
        return s

def Main():
    number = Number(3,4)
    print(number.Addition())
    print(number.Subtration())
    print(number.Multiplication())
    print(number.Division())

Main()
'''

'''
137 .
 请用类的派生方式来组织下列动物实体与概念：动物，鱼纲，鸟纲。编写代码实现

#  派生  即继承

class Animal:
    color = '动物的颜色'

class Flash(Animal):
    color= '鱼 银白色'

class  Bird(Animal):
    color = '灰色'

flash = Flash()
print(flash.color)

bird = Bird()
print(bird.color)
'''

'''
138.
定义商品类及其多层的派生类。以商品类为基类。第一层派生出服装类、家电类、车辆类。
第二层派生出衬衣类、电视类、自行车类。要求给出基本属性和派生过程中增加的属性。
提示：按题意没有操作,所以只列出数据成员,也不再检验。


class  Goods:
    des = '商品'

class Costumer(Goods):
    name = '服装类'
class Electry(Goods):
    name = '家电类'
class Cars(Goods):
    name = '车辆类'
class Chenyi(Costumer):
    color = 'white'
class TV (Electry):
    brand = '小米'

class Bicycle(Cars):
    name = '自行车'
costumer = Costumer()
print(costumer.name)
print(costumer.des)
'''
'''
139.
"定义一个Person类，它包含数据成员age, name和gender。
从Person中派生一个类Employee,在新类中添加一个数据成员，存储个人的number.
再从Employee中派生一个类Executive,每个派生类都应该定义一个函数，
来显示相关的信息（名称和类型，如”Fred Smith is an Employee”）。
编写一个Main()函数，生成一个列表，包含3个Executive对象，2个一般的Employee对象，然后显示它们的信息。"


class Person:
    def __init__(self,name='',age='',gender=''):
        self.age = age
        self.name = name
        self.gender = gender


class Employee(Person):
        number = ''
        
        def fun(self):
            return self.name +' is an Employee'

class Executive(Employee):

    def fun1(self):
        return self.name+'是贴心小管家'


def Main():
    exe1 = Executive('zhangsan')
    print(exe1.fun1())
    exe2 = Executive('lisi')
    print(exe2.fun1())
    exe3 = Executive('王五')
    print(exe3.fun1())

    emp1 = Employee('杨过')
    print(emp1.fun())
    emp = Employee('谢霆锋')
    print(emp.fun())

Main()     


#   可以使用super() 继承 父类的构造函数

super():
    1. super() 继承父类的成员变量（属性），继承父类的成员方法（函数）
    2，继承父类的构造函数（def__init__()函数 ）
    3.super().可以传参，，默认是 父类  ，即 传  指定 类的  子类，，后一代
    
    
    向上转型，，，isinstance(4,int)   返回一个布尔值，，判断 是否是  后面 一个类的  实例 
    
    高级类型：；传递   实例对象  类 ，，，判断 是否  是  类的  对象  继承  关系 
    
    判断 类型   判断  继承  
    
    issubclass()  :  传两个类   判断  1  是否为  2 的  子类  
    
    
    
    
    多态..多种 状态 ，，多种 类型    列表 中  放 不同类型的 对象 ，，遍历 列表，，调用  他们 的 同名 方法
    
    
    就是多态   
    
            6.6   task  作业2   鸭子类型 。。遍历一个列表，， 结果 为   三种 不同的结果
    这样使得  python  语言  更为 灵活，
    
    多态：  提高程序的  扩展性 
    
    继承 。  重复性 
   
   def  sum(a,b):
    return a+b

#  这是一个简单的调用
print(sum(3, 4))
 
'''




'''
140.
设计一个图书管理系统,基类为类Book,要求有书名和作者属性， 由Book类派生子类AudioBook(有声书，需要具有演说者属性)，
对于Book和AudioBook进行合理的属性及行为的抽象，同时实现该类的控制台打印函数

class  Book:
    def __init__(self,name,writer):
        self.name = name
        self.writer = writer
    def fun(self):
        return '我是普通书籍'

class AudioBook(Book):
    speak = '郭德纲'
    def fun1(self):
        return '我是 有声书籍'

book=Book('传奇','莫言')
print(book.fun())
print(book.writer)

audiobook = AudioBook('三大白骨精','罗贯中')
print(audiobook.fun1())
print(audiobook.writer)

'''

'''

示例：
某枪战游戏中：
角色类：Role
属性:
    血量
    枪支库：考虑用什么类型存储
    当前选择的枪支
方法：
    更换枪支
    开火

枪支类：
属性：
    range射程  
    hurt伤害值
方法：
    开火:Fire
        
手枪 类 PistolGun
来福枪类：RifleGun
激光枪：LaserGun


class  Role:
    hp = 100
    Allgun = [None,None,None]
    curgun = " "

    def  __findgunindex(self,gun):
        index = -1
        for  guninlist in  self.Allgun:
            index += 1
            if  gun == guninlist:
                return index
    #   如果没有走 return   它会返回 None


    def changegun(self):

        index = self.__findgunindex(self.curgun)
        if  index == None:
            print('切枪失败')

        if index == len(self.Allgun)-1:
            index = 0
        else:
            self.curgun = self.Allgun[index+1]







    def fire(self):
        self.curgun.fire()


class  gun:
    name = ''
    range = 0
    hurt = 0

    def fire(self):
        print('我是%s枪，射程是%s'%(self.name,self.range))

class PostolGun(gun):
    range = 100
    hurt = 10
    name = '手枪'


class  RifileGun(gun):
    range = 100
    hurt = 10
    name = '来福'


class  LaserGun(gun):
    range = 100
    hurt = 10
    name = '激光枪'



def  test():
    role = Role()
    role.Allgun[0] = PostolGun()
    role.Allgun[1] = RifileGun()
    role.Allgun[2] = LaserGun()

    role.curgun = role.Allgun[1]
    role.fire()


t = test()


老师答案：

"""
示例：
某枪战游戏中：
角色类：Role
属性:
    血量
    枪支库：考虑用什么类型存储
    当前选择的枪支
方法：
    更换枪支
    开火

枪支类：
属性：
    range射程
    hurt伤害值
方法：
    开火:Fire

手枪 类 PistolGun
来福枪类：RifleGun
激光枪：LaserGun
"""

class Role:
    Hp = 100
    AllGuns = [None,None,None] # 身上所有的枪支
    CurGun = None # 当前使用的枪支

    # 查找枪的索引号，返回从0开始的索引号
    def __findGunIndex(self, gun):
        index = -1
        for gunInList in self.AllGuns:
            index += 1
            if gun == gunInList:
                return index

    # 循环切换枪支
    def Exchange(self):
        index = self.__findGunIndex(self.CurGun)
        if index == None:
            print("切枪失败")
            return

        # 考虑最后一把枪
        index = (index + 1) % len(self.AllGuns)
        self.CurGun = self.AllGuns[index]

        return self.CurGun

    def Fire(self):
        self.CurGun.Fire()

# 枪支的基类
class GunBase:
    range = 0
    hurt = 0
    name = ""

    def Fire(self):
        print("%s开火，射程：%s，伤害：%s"%(self.name, self.range, self.hurt))

class PistolGun(GunBase):
    range = 50
    hurt = 50
    name = "手枪"


class RifleGun(GunBase):
    range = 30
    hurt = 70
    name = "来福枪"


class LaserGun(GunBase):
    range = 100
    hurt = 30
    name = "激光枪"

def test():
    role = Role()
    role.AllGuns[0] = PistolGun()
    role.AllGuns[1] = RifleGun()
    role.AllGuns[2] = LaserGun()

    role.CurGun = role.AllGuns[0]

    while True:
        ip = input("请输入操作：1，切枪；f,开火；e,退出")
        if ip == "1":
            curGun = role.Exchange()
            print("当前枪支：" + curGun.name)
        elif ip == "f":
            role.Fire()
        elif ip == "e":
            break
        else:
            print("请输入正确的操作")

test()
'''
'''
141.
以点（point）类为基类，重新定义矩形类和圆类。点为直角坐标点，矩形水平放置，
由左下方的顶点和长宽定义。圆由圆心和半径定义。派生类操作判断任一坐标点是在图形内，
还是在图形的边缘上，还是在图形外。缺省初始化图形退化为点。要求包括拷贝构造函数。
编程测试类设计是否正确。


class  Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
     def panduan(self ,x1,y1):
        line1 = self.x
        line2 = self.y
        line3 = self.x+self.length
        line4 = self.y+self.width
        if (line1 < x1 < line3) & (line4 < y1 < line1):
            print('该点%d在矩形内'%(x1,y1))

        elif (x1==self.line1) &( self.line2<=y1<=self.line4 ) | (x1==self.line3) &( self.line2<=y1<=self.line4 )|(y1==self.line2) &( self.line1<=x1<=self.line3 )|(y1==self.line3) &( self.line1<=x1<=self.line3 )

            print('该点%d在矩形边缘上' % (x1, y1))
        else:
            print('该点%d在矩形  外' % (x1, y1))




class Reactangle(Point):
    def __init__(self,x,y,length,width):
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        


class Circle(Point):

    def __init__(self, x, y,dian,r):
        super.__init__(x,y)
        self.dian = dian
        self.r = r

c 语言版：
#include <iostream>
#include <cmath>
using namespace std;
const double PI=3.1415926535;
class Point{
private:
	double x,y;
public:
	Point(){x = 0; y = 0; }
	Point(double xv,double yv){x = xv;y = yv;}
	Point(Point& pt){ x = pt.x; y = pt.y; }
	double getx(){return x;}
	double gety(){return y;}
	double Area(){return 0;}
	void Show(){cout<<"x="<<x<<' '<<"y="<<y<<endl;}
};
class Circle :public Point{
	double radius;
public:
	Circle(){radius = 0;}
	Circle(double xv,double yv,double vv):Point(xv,yv){radius = vv;}
	Circle(Circle& cc):Point(cc){radius = cc.radius;}  //拷贝构造函数	
	double Area(){return PI*radius*radius;}
	void Show(){//注意怎样访问基类的数据成员
		cout<<"x="<<getx()<<'\t'<<"y="<<gety()<<'\t'<<"radius="<<radius<<endl; 
	}
	int position(Point &pt){
	double distance = sqrt((getx()-pt.getx())*(getx()-pt.getx())
		                    +(gety()-pt.gety())*(gety()-pt.gety()));
    double s=distance-radius;
	if(s==0) return 0;                      //在圆上
	else if(s<0) return -1;					//在圆内
	else return 1;							//在圆外
	}
};
class Rectangle:public Point{
	double width,length;
public:
	Rectangle(){width=0; length=0; }
	Rectangle(double xv,double yv,double wv,double lv):Point(xv,xv)	{
		width = wv;
		length= lv;
	}
	Rectangle(Rectangle& rr):Point(rr){
		width = rr.width;
		length = rr.length;
	}
	double Area(){return width*length;}
	void Show(){
		cout<<"x="<<getx()<<'\t'<<"y="<<gety()<<'\t';		cout<<"width="<<width<<'\t'<<"length="<<length<<endl;
	}
	int position(Point &pt);
};
int Rectangle::position(Point &pt){
	double s1,s2;
	s1 = (pt.getx()-getx()); s2=(pt.gety()-gety());
	if(((s1==0||s1==width)&&s2<=length)||((s2==0||s2==length)&&s1<=width)) return 0; 
else if(s1<width&&s2<length) return -1;			//0在矩形上，-1在矩形内
		else return 1;									//1在矩形外
}
int main(){
	Circle cc1(3,4,5),cc2,cc3(cc1);
	Rectangle rt1(0,0,6,8),rt2,rt3(rt1);
	Point p1(0,0),p2(6,8),p3(3,3),p4(8,4),p5(8,8);
	cc1.Show();
	cc2.Show();
	rt1.Show();
	rt2.Show();
	cout<<"点p1:";
	p1.Show();
	cout<<"矩形rt3:"<<'\t';
	rt3.Show();
	switch(rt3.position(p1)){
	case 0:cout<<"在矩形上"<<endl;break;
	case -1:cout<<"在矩形内"<<endl;break;
	case 1:cout<<"在矩形外"<<endl;break;
	}
	cout<<"圆cc3:"<<'\t';
	cc3.Show();
	switch(cc3.position(p1)){
	case 0:cout<<"在圆上"<<endl;break;
	case -1:cout<<"在圆内"<<endl;break;
	case 1:cout<<"在圆外"<<endl;break;
	}
	cout<<"点p2:";
	p2.Show();
	cout<<"矩形rt3:"<<'\t';
	rt3.Show();
	switch(rt3.position(p2)){
	case 0:cout<<"在矩形上"<<endl;break;
	case -1:cout<<"在矩形内"<<endl;break;
	case 1:cout<<"在矩形外"<<endl;break;
	}
	cout<<"圆cc3:"<<'\t';
	cc3.Show();
	switch(cc3.position(p2)){
	case 0:cout<<"在圆上"<<endl;break;
	case -1:cout<<"在圆内"<<endl;break;
	case 1:cout<<"在圆外"<<endl;break;
	}
	cout<<"点p3:";
	p3.Show();
	cout<<"矩形rt3:"<<'\t';
	rt3.Show();
	switch(rt3.position(p3)){
	case 0:cout<<"在矩形上"<<endl;break;
	case -1:cout<<"在矩形内"<<endl;break;
	case 1:cout<<"在矩形外"<<endl;break;
	}
	cout<<"圆cc3:"<<'\t';
	cc3.Show();
	switch(cc3.position(p3)){
	case 0:cout<<"在圆上"<<endl;break;
	case -1:cout<<"在圆内"<<endl;break;
	case 1:cout<<"在圆外"<<endl;break;
	}
	cout<<"点p4:";
	p4.Show();
	cout<<"矩形rt3:"<<'\t';
	rt3.Show();
	switch(rt3.position(p4)){
	case 0:cout<<"在矩形上"<<endl;break;
	case -1:cout<<"在矩形内"<<endl;break;
	case 1:cout<<"在矩形外"<<endl;break;
	}
	cout<<"圆cc3:"<<'\t';
	cc3.Show();
	switch(cc3.position(p4)){
	case 0:cout<<"在圆上"<<endl;break;
	case -1:cout<<"在圆内"<<endl;break;
	case 1:cout<<"在圆外"<<endl;break;
	}
	cout<<"点p5:";
	p5.Show();
	cout<<"矩形rt3:"<<'\t';
	rt3.Show();
	switch(rt3.position(p5)){
	case 0:cout<<"在矩形上"<<endl;break;
	case -1:cout<<"在矩形内"<<endl;break;
	case 1:cout<<"在矩形外"<<endl;break;
	}
	cout<<"圆cc3:"<<'\t';
	cc3.Show();
	switch(cc3.position(p5)){
	case 0:cout<<"在圆上"<<endl;break;
	case -1:cout<<"在圆内"<<endl;break;
	case 1:cout<<"在圆外"<<endl;break;
	}
	return 0;
}


'''
'''
142.
"对平面形体有长和面积，对立体有表面积和体积，对几何图形基类，周长、面积和体积应怎样计算（用什么函数）?
对平面图形面积怎样计算（用什么函数）？对立体图形周长怎么计算（用什么函数）?要求实现运行时的多态性。请编程，并测试。
Shape
正方形(Square) 长方形(Rectangle) 圆形(Circle) 圆环(Annulus)
方体(Cube) 圆柱(Cylinder)"

c 语言：
#include <iostream>
#include <cmath>
using namespace std;
const double PI=3.1415926535;
class Geometric_shape{//几何图形
public:
	virtual double perimeter()=0;	//周长
	virtual double area()=0;		//面积
	virtual double volume()=0;		//体积
	virtual void Show(){};
};
class Circle :public Geometric_shape{//圆
	double radius;
public:
	Circle(){radius = 0; }
	Circle(double vv){radius = vv;}
	double perimeter(){return 2.0*PI*radius;}	//周长
	double area(){return PI*radius*radius;}		//面积
	double volume(){return 0;}		//体积
	void Show(){cout<<"radius="<<radius<<endl;}
};
class Rectangle:public Geometric_shape{//矩形
	double width,length;
public:
	Rectangle(){width=0; length=0;}//长宽
	Rectangle(double wid,double len){
		width = wid;
		length= len;
	}
	Rectangle(Rectangle& rr){
		width = rr.width;
		length = rr.length;
	}
	double perimeter(){return 2.0*(width+length);}	//周长
	double area(){return width*length;}		//面积
	double volume(){return 0;}		//体积
	void Show(){cout<<"width="<<width<<'\t'<<"length="<<length<<endl;}
};
class Triangle:public Geometric_shape{//三角形
	double a,b,c;
public:
	Triangle(){a=0;b=0;c=0;}
	Triangle(double v1,double v2,double v3){a = v1;b = v2;c = v3;}
	double perimeter(){return a+b+c;}	//周长
	double area(){
		double s=(a+b+c)/2.0;
		return sqrt(s*(s-a)*(s-b)*(s-c));
	}		//面积
	double volume(){return 0;}		//体积
	void Show(){cout<<"a="<<a<<'\t'<<"b="<<b<<'\t'<<"c="<<c<<endl;}
};
class Box:public Rectangle{//长方体
	double height;
public:
	Box(){height=0;}
	Box(double wid,double len,double heg):Rectangle(wid,len){height=heg;}

	double volume(){return area()*height;}		//体积
};
class Cylinder:public Circle {//圆柱体
	double height;
public:
	Cylinder(){height=0;}
	Cylinder(double vv,double heg):Circle(vv){height=heg;}
	double volume(){return area()*height;}		//体积
};
class Cone: public Circle {//圆锥
	double height;
public:
	Cone(){height=0;}
	Cone(double vv,double heg):Circle(vv){height=heg;}
	double volume(){return area()*height/3;}		//体积
};
class T_pyramid:public Triangle{//三棱锥
	double height;
public:
	T_pyramid(){height=0;}
	T_pyramid(double v1,double v2,double v3,double heg):Triangle(v1,v2,v3){height=heg;}
	double volume(){return area()*height/3;}		//体积
};
class T_prism:public Triangle{//三棱柱
	double height;
public:
	T_prism(){height=0;}
	T_prism(double v1,double v2,double v3,double heg):Triangle(v1,v2,v3){height=heg;}
	double volume(){return area()*height;}		//体积
};
int main(){
	Geometric_shape * gs;
	Circle cc1(10);
	Rectangle rt1(6,8);
	Triangle tg1(3,4,5);
	Box bx1(6,8,3);
	Cylinder cl1(10,3);
	Cone cn1(10,3);
	T_pyramid tpy1(3,4,5,3);
	T_prism tpr1(3,4,5,3);

	cc1.Show();//静态
	cout<<"圆周长："<<cc1.perimeter()<<'\t';
	cout<<"圆面积："<<cc1.area()<<'\t';
	cout<<"圆体积："<<cc1.volume()<<endl;
	gs=&rt1;//动态
	gs->Show();
	cout<<"矩形周长："<<gs->perimeter()<<'\t';
	cout<<"矩形面积："<<gs->area()<<'\t';
	cout<<"矩形体积："<<gs->volume()<<endl;
	gs=&tg1;//动态
	gs->Show();
	cout<<"三角形周长："<<gs->perimeter()<<'\t';
	cout<<"三角形面积："<<gs->area()<<'\t';
	cout<<"三角形体积："<<gs->volume()<<endl;
	gs=&bx1;//动态
	gs->Show();
	cout<<"长方体底周长："<<gs->perimeter()<<'\t';
	cout<<"长方体底面积："<<gs->area()<<'\t';
	cout<<"长方体体积："<<gs->volume()<<endl;
	gs=&cl1;//动态
	gs->Show();
	cout<<"圆柱体底周长："<<gs->perimeter()<<'\t';
	cout<<"圆柱体底面积："<<gs->area()<<'\t';
	cout<<"圆柱体体积："<<gs->volume()<<endl;
	gs=&cn1;//动态
	gs->Show();
	cout<<"圆锥体底周长："<<gs->perimeter()<<'\t';
	cout<<"圆锥体底面积："<<gs->area()<<'\t';
	cout<<"圆锥体体积："<<gs->volume()<<endl;
	gs=&tpy1;//动态
	gs->Show();
	cout<<"三棱锥底周长："<<gs->perimeter()<<'\t';
	cout<<"三棱锥底面积："<<gs->area()<<'\t';
	cout<<"三棱锥体积："<<gs->volume()<<endl;
	gs=&tpr1;//动态
	gs->Show();
	cout<<"三棱柱底周长："<<gs->perimeter()<<'\t';
	cout<<"三棱柱底面积："<<gs->area()<<'\t';
	cout<<"三棱柱体积："<<gs->volume()<<endl;
	return 0;
}

'''
'''
143.
"某公司雇员（Employee）包括经理（Manager），技术人员（Technician）和销售员（Salesman）。
以Employee类为基类派生出Manager，Technician和Salesman类；
Employee类的属性包括姓名、职工号、工资级别，月薪（实发基本工资加业绩工资）。
操作包括月薪计算函数（Pay()），该函数要求输入请假天数，扣去应扣工资后，
得出实发基本工资。
Technician类派生的属性有每小时附加酬金和当月工作时数，及研究完成进度系数。
业绩工资为三者之积。也包括同名的Pay()函数，工资总额为基本工资加业绩工资。

Salesman类派生的属性有当月销售额和酬金提取百分比，业绩工资为两者之积。也包括同名的Pay()函数，
工资总额为基本工资加业绩工资。Manager类派生属性有固定奖金额和业绩系数，业绩工资为两者之积。
工资总额也为基本工资加业绩工资。编程实现工资管理。"

class  Employee:
    def __init__(self,name='',id='',salary_grade='',salary=''):
        self.name = name
        self.id = id
        self.salary_grade = salary_grade
        self.salary = salary
    #     Employee类的属性包括姓名、职工号、工资级别，
    # 月薪（实发基本工资加业绩工资）。操作包括月薪计算函数（Pay()），该函数要求输入请假天数，扣去应扣工资后，
    # 得出实发基本工资。
    def  Pay(self):
        num_day = int(input("请输入请假天数"))
        # shifa_salary = self.salary -num_day*(self.salary/30)


    pass
class Manager(Employee):
    # Manager类派生属性有固定奖金额和业绩系数，业绩工资为两者之积。
    # 工资总额也为基本工资加业绩工资
    def __init__(self, name='', id='', salary_grade='', salary='',gudingjine = 0,yejixishu = 0):
        self.name = name
        self.id = id
        self.salary_grade = salary_grade
        self.salary = salary
        self.gudingjine = gudingjine
        self.yejixishu = yejixishu
        
    def pay(self):
        # salary =
        pass
        
        
class Technician(Employee):
    # Technician类派生的属性有每小时附加酬金和当月工作时数，及研究完成进度系数。
    # 业绩工资为三者之积。也包括同名的Pay()函数，工资总额为基本工资加业绩工资。
    def __init__(self, name='', id='', salary_grade='', salary='',jiabanfei =0,work_hour_totle =0,jinduxishu = 0):
        self.name = name
        self.id = id
        self.salary_grade = salary_grade
        self.salary = salary
        self.jiabanfei =  jiabanfei
        self.work_hour_totle = work_hour_totle
        self.jinduxishu = jinduxishu

    def pay(self):
        pass


# salary =
        
        
class Salesman(Employee):
# Salesman类派生的属性有当月销售额和酬金提取百分比，业绩工资为两者之积。也包括同名的Pay()函数，
    def __init__(self, name='', id='', salary_grade='', salary='',xiaoshoujne = 0, choujinproperty = 0 ):
        self.name = name
        self.id = id
        self.salary_grade = salary_grade
        self.salary = salary
        self.xiaoshoujine = xiaoshoujne
        self.choujinproperty = choujinproperty


    def pay(self):
        salary = self.xiaoshoujine*self.choujinproperty
        

'''


'''
144.
"定义一个人的类
属性有名字，年龄。
写一个能输出各个属性值的方法ShowInfo（）
定义一个学生类（属性有性别）
学生继承人类 要求：
（1）父类的属性赋值用构造方法来实现（分别用有参数构造方法和无参数构造方法实现）
（2）子类的属性也用构造方法来赋值。
（3）在子类中隐藏父类的ShowInfo（）方法
（4）声明学生类的对象，调用学生的显示信息的方法。"



class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def ShowInfo(self):
        return  self.name,self.age

class Student(Person):
    def __init__(self,name,age,sex):
        super().__init__(name,age)
        self.sex = sex

    def ShowInfo(self):
        return self.name, self.age,self.sex


studen= Student('zhangsan',18,'男')
print(studen.ShowInfo())

('zhangsan', 18, '男')
'''
'''
145.
"请编码实现动物世界的继承关系：
动物（Animal）具有行为：吃（eat）、睡觉（sleep）
动物包括：兔子（Rabbit），老虎（Tiger）
这些动物吃的行为各不相同（兔子吃草，老虎吃肉）
但睡觉的行为是一致的。
请通过继承实现以上需求，并编写测试类进行测试。"

class Animal:
    def eat(self):
        return 'eat'

    def sleep(self):
        return 'sleep'

class Tiger(Animal):
    def eat(self):
        return '老虎吃肉'

class Rabbit(Animal):

    def eat(self):
        return '兔子吃草'





def Test():
    tiger = Tiger()
    print(tiger.sleep())
    print(tiger.eat())
    rabbit = Rabbit()
    print(rabbit.eat())
    print(rabbit.sleep())

t = Test()


'''

'''
146.
"定义一个“曲调类”Note，value成员表示声音的高低
Note的三个子类分别表示高音、低音和中音
定义一个“乐器类”Instrument
具有Play()方法
子类：
“管乐器类”Wind
“敲击乐器类”Percussion
“弦乐器类”Singed
“铜管类”Brass
“木管类”Woodwind
只写一个方法传入乐器和音调实现：
Wind演奏高音
Percussion演奏中音
铜管演奏中音
木管演奏低音
弦乐器演奏高音
敲击乐器演奏低音"

class Note:
    def __init__(self,name = '',value= ' '):
        self.name =name
        self.value = value

class High(Note):
    # 方法  重写  和 父类 保持 一致
    def __init__(self, name='', value=' '):
        self.name = '高音'
        self.value = value

class Middle(Note):
    def __init__(self, name='', value=' '):
        self.name = '中音'
        self.value = value


class Low(Note):
    def __init__(self, name='', value=' '):
        self.name = '低音'
        self.value = value

'''
# 定义一个“乐器类”Instrument
# 具有Play()方法
# 子类：
# “管乐器类”Wind
# “敲击乐器类”Percussion
# “弦乐器类”Singed
# “铜管类”Brass
# “木管类”Woodwind
'''
class Instrument:
    name = ''
    def play(self,h):
        # return '乐器'
        print(self.name+"在演奏"+ h.name)
class Wind(Instrument):
    # def __init__(self,name=''):
    name = '管乐类'

class Percussion(Instrument):
    name = '敲击乐'

class Singed(Instrument):
    name = '弦乐'

class Brass(Instrument):
    name = '管铜乐'

class Woodwind(Instrument):
    name = '木管乐'
'''
# 只写一个方法传入乐器和音调实现：
# Wind演奏高音
# Percussion演奏中音
# 铜管演奏中音
# 木管演奏低音
# 弦乐器演奏高音
# 敲击乐器演奏低音"
# '''
#
# def  test():
#         # instrument = Instrument()
#
#         # note =Note()
#
#         high = High()
#         middle = Middle()
#         low = Low()
#
#         wind = Wind()
#         wind.play(high)
#
#         percussion = Percussion()
#         percussion.play(middle)
#
#
# t = test()





'''
147.
    "1).
编写健身器类
字段：名称、价格、是否是电力驱动。皆为受保护类型
方法:
Use()无参无返回值，负责打印“被使用中”
Info()无参无返回值，负责打印设备的所有信息

2).
编写跑步机类，继承健身器类，
在构造函数中修改默认为电力驱动
i. 隐藏Use方法，打印“跑步机被使用中”
ii. 添加字段：品牌

3).
编写哑铃，继承健身器类
隐藏Use方法，打印“哑铃被使用中”

4).在测试类中：
创建健身器列表，存放不同类型的健身器，依次执行每个元素的Use方法"


class Fit:
    def __init__(self,name = '',price= '',electronic= ''):
        self._name = name
        self._price = price
        self._electronic = electronic

    def User(self):
        print(self._name+'被使用中')

    def  Info(self):
        print(self._name,self._price,self._electronic)


class Runner(Fit):
    def __init__(self, _name='', _price='', _electronic='',_brand=''):
        self._name = '跑步机'
        self._price = ''
        self._electronic = 'Yes'
        self._brand = ''

class Yaling(Fit):
    def __init__(self, _name='', _price='', _electronic='', _brand=''):
        self._name = 'yaling'
        self._price = ''
        self._electronic = 'Yes'
        self._brand = ''


def Test():

    runer = Runner()
    # runer.User()
    yaling = Yaling()
    # yaling.User()
    list =[runer,yaling]
    for obj in list:
        time.sleep(1)
        obj.User()
t = Test()

'''

'''
148.
"有2个类：
员工类：属性：名字、工号、部门、工资 方法：涨工资
经理类继承自员工类 并多了一个属性：奖金
问题：
1).某公司有员工3人 经理2名 请用一个列表来管理他们 请自行产生这些对象
2.请输出所有员工的信息 格式：工号\t部门\t名字\t工资
3.请统一的为所有员工涨一次工资 员工涨10% 经理比员工多涨10%
4.请输出所有员工涨工资后的信息 格式：工号\t部门\t名字\t工资"


class Emplyee:
    def __init__(self,name='',id='',department='',salary=0):
        self._name = name
        self._id = id
        self._department = department
        self._salary = salary

    def Up_salary(self):
        self._salary = self._salary*(1+0.1)
        print('涨工资')


class Manager(Emplyee):
    def __init__(self,name='',id='',department='',salary=0,bonus=0):
        self._name = name
        self._id = id
        self._department = department
        self._salary = salary
        self._bonus = bonus
    def Up_salary(self):
        self._salary = self._salary*(1+0.1)**2
        print('涨工资')
        return self._salary

# 1
emp1 = Emplyee('张三',1,'销售部',3000)
emp2 = Emplyee('李四',2,'销售部',3000)
emp3 = Emplyee('王五',3,'销售部',3000)
manager1 = Manager('王力',4,'人事部',5000)
manager2 = Manager('丁强',5,'技术部',5000)

list =[emp1,emp2,emp3,manager1,manager2]
# 2
for obj in list:
    print(obj._id)
    print(obj._department)
    print(obj._name)
    print(obj._salary)

# 涨工资

for obj in list:
    obj.Up_salary()

    print(obj._id)
    print(obj._department)
    print(obj._name)
    print(obj._salary)


# emp3.Up_salary()


'''


'''
149.
    计算1+2^2+3^3+4^4+...+n^n的值(^表示幂);


class  Mi:
    def mimi(self,a):
        return a**2

mi = Mi()

list = [x for x in range(1,4)]
# list = [1,2,3]
sum = 0

for  i in list:
    b = mi.mimi(i)
    sum +=b
print(sum )
'''


'''
150.
"求10000以下的水仙花数;
水仙花数是指一个 n 位数 ( n≥3 )，它的每个位上的数字的 n 次幂之和等于它本身。（例如：1^3 + 5^3+ 3^3 = 153）"

#  小结： 差点理解为 都是 3 次方 

#   不足： 没使用 多态的知识

for i in range(1,10000):

    if 100<= i< 1000:
        a = i // 100
        b =i % 100 // 10
        c =i % 100% 10
        # print(i,a,b,c)
        if i == a**3+ b**3 + c**3:
            print(i,end = ',')
    if 1000<= i < 10000:
        # print(i)
        a = i // 1000
        b = i % 1000 // 100
        c = i % 1000%100//10
        d = i % 1000%100%10
        # print(i)
        if i == a**4+ b**4 + c**4 + d**4:
            # pass
            print(i,end=",")


'''

'''
151.
"编写一个学生类：
学生类包括：
字段：名字、年龄、所属省份、所属市
属性：请封装上述字段
题目要求：
11.1编写一个学生列表，长度为3，放入不同省市的3个学生对象。名字和年龄自定义即可。
11.2根据省份输出列表中该省份的所有学生信息。
11.3根据所属市输出列表中该市的所有学生信息。"

class  Student:
    def __init__(self,name ='',age = '',province = '',city = ''):
        self.name = name
        self.age = age
        self.province = province
        self.city = city

# 11.1
student1 = Student('张三',22,'浙江','杭州')
student2 = Student('王丽',24,'浙江','湖州')
student3 = Student('赵小宝',32,'黑龙江','鹤岗')
list = [student1,student2,student3]
# 2
for obj in list:
    # li1 = []
    # city = obj.city
    # li1.append(city)
    if  obj.province == '浙江':
        print(obj.name)
        print(obj.age)
        print(obj.province)
        print(obj.city)
#3 
for obj in list:
    if obj.city == '杭州':
        print('*' * 10)
        print(obj.name)
        print(obj.age)
        print(obj.province)
        print(obj.city)

'''
'''
152.
"创建一个玩家类，玩家有名称、生命值、魔法值、攻击力、生存状态5个属性；
生命值、魔法值、攻击力、生存状态属性都是只读的；生命值、魔法值、攻击力的初值分别为800、100、50；
玩家类有一个攻击方法：public void Attack(Player player)。
玩家类有两个子类：野蛮人和魔法师。野蛮人每次攻击造成的伤害在[攻击力-10] 到[攻击力+10]之间
（这个伤害值是一个随机值），另外野蛮人有一个被动技能（不消耗魔法），
有25%的几率产生1次暴击（每4次攻击随机产生1次暴击），每次暴击产生的伤害是原来的3倍；

魔法师每次攻击造成的伤害在攻击力的80%~100%之间（也是一个随机数），魔法师每次攻击消耗18点魔法，
它会额外减少对方12%的生命值。现在分别创建一个野蛮人、魔法师对象，让他们进行PK，就是你打我一下，
我打你一下，直到有一方死亡为止；野蛮人先攻击。"


#  试调试  留有bug 未修改  
class Player:
    def __init__(self, name='', life_value=800, magic_value=100, attack_power=50, Exists_statue=''):
        self.name = name
        self.__life_value = life_value
        self.__magic_value = magic_value
        self.__attack_value = attack_power
        self.__exists_statue = Exists_statue

    def public_void_Attack(self):
        def __init__(self, name='', life_value=800, magic_value=100, attack_power=50, Exists_statue=''):
            self.name = name
            self.__life_value = life_value
            self.__magic_value = magic_value
            self.__attack_value = attack_power
            self.__exists_statue = Exists_statue

        return '攻击'


class Wilder(Player):

    def __init__(self, name='', life_value=800, magic_value=100, attack_power=50, Exists_statue=''):
        self.name = name
        self.__life_value = life_value
        self.__magic_value = magic_value
        self.__attack_power = attack_power
        self.__exists_statue = Exists_statue

    def Attack1(self, a):
        attacker = random.randrange(-10, 10)
        a = random.choice([1, 2, 3, 4])
        # 野人的攻击力
        print('自身的攻击力:', attacker)
        #  自身的生命值 为 它本身的  --  对方的 攻击
        self.__life_value -= a.Attack2()
        print(self.__life_value)
        if a == 1:
            attacker = 3 * attacker

        return attacker

    # print(Attack())


class Magicer(Player):

    def Attack2(self, b):
        attacker = random.randrange(0.8, 1) * 50
        self.__magic_value -= 18
        c = self.__life_value * (1 - 0.12)
        self.__life_value == self.Attack1()
        # 魔法师的攻击力
        print(attacker)
        # 野人的魔法值
        print('野人的魔法值：',self.__magic_value)
        # 对方的伤害
        print()

        return c


def Test():
   while True:
        a = input("请选择输入：1 野人攻击，0魔法师攻击,esc,退出游戏")

        wilder = Wilder()
        magic = Magicer()
        if a == '1':
            wilder.Attack1(magic)
            print('野人发起攻击')
        elif a == '0':
            print('魔法师发起攻击')
            magic.Attack2(wilder)
        elif a == 'Esc':
            break
        else:
            pass

t = Test()

'''



'''
153.
"写一个Ticket类,有一个距离属性(本属性只读,在构造方法中赋值),不能为负数,有一个价格属性,价格属性只读,并且根据距离计算价格(1元/公里):
0-100公里 票价不打折
101-200公里 总额打9.5折
201-300公里 总额打9折
300公里以上 总额打8折
有一个方法,可以显示这张票的信息.
测试上面的类."


class Ticket:
    def  __init__(self,distance='',prince = 0):
        self.distance = distance
        self.__prince = prince
    def prince(self,dis):
        if dis <= 0:
            print('距离不能为负数，请重新输入!')
        elif dis <=100:
            print('票价为:%.2f'%(dis*1))
        elif 101<=dis<=200:
            print('票价为:%.2f' % (dis * 1*0.95))
        elif 201<=dis<300:
            print('票价为:%.2f' % (dis * 1*0.9))
        elif 300<=dis:
            print('票价为:%.2f' % (dis * 1*0.8))



ticket = Ticket()
a=int(input('请输入目的地：'))
ticket.prince(a)


用范围，， 要不然会出 Bug
'''
'''
154.
    "定义一个Vehicle汽车类，类中包含一个Person类型的数据成员拥有者owner、车轮数、车重、品牌等；
    定义一个Car类，它是Vehicle的子类，其中添加字段：核载人数和实载人数。
定义VehicleManage汽车管理这个类：
该类包含一个字段：管理的车辆列表
该类包含两个方法：
1.获取到某个人拥有的所有车辆，并显示其名下所有车辆的信息
2.查看某车是否超载，并显示车辆和车主信息。
测试方案：测试汽车管理类中的方法"

class Vehicle:
    def __init__(self,owner='',wheel=4,weight=2,brand='奔驰'):
        self.owner = owner
        self.wheel = wheel
        self.weight = weight
        self.brand = brand


class Car(Vehicle):
    def __init__(self,hezai='',shizai='',owner='', wheel=4, weight=2, brand='奔驰'):
        # super().__init__(owner='', wheel=4, weight=2, brand='奔驰')
        self.owner = owner
        self.wheel = wheel
        self.weight = weight
        self.brand = brand
        self.hezai = 5
        self.shizai = shizai

class  Person:
    def __init__(self,name):
        self.name = name

car1 = Car(owner='zhangsan')
car2 = Car(owner='zhangsan')
car3 = Car(owner='王凯', shizai=5)



class VehicleManager:


    # 1
    def All_car(self,a):
        list = [car1, car2, car3]

        for obj in list:
            # print(obj.owner)
            if a ==  obj.owner:
                print(obj.owner)
                print(obj.brand)
                print(obj.wheel)
                print(obj.weight)

    #  2
    def check_over_weight(self,a):
        if a.shizai > a.hezai:
            print('您已超载！')
            print(a.owner)
            print(a.brand)
            print(a.weight)
        else:
            print('核载正常，祝你旅途愉快！')


def  Test():
    car3 = Car(owner='王凯',shizai = 5)
    manage = VehicleManager()
    manage.All_car('zhangsan')
    #  超载
    manage.check_over_weight(car3)

t = Test()

'''
# print('hello python')




'''
186.
当用户输入“T”或“t”时,人为抛出一个自定义异常,处理方式为打印出错信息

异常 举例：

#  异常
try:
    print(1/0)
except:
    print('err')

try:
    li =[0]
    print(li[1])
except:
    print("er")

try:
    str = '123q'
    print(str[6])
except:
    print('err')

try:
    str = '123q' + 2.3
    print(int(str))
except:
    print('err')

补充：
# try:
#     str = '123q' + 2.3
#     print(int(str))
# except:
#     print('err')


# raise 执行后， 它后面的代码不在执行，和retrun  相似，，
#  直接跳转到  exception


#  自定义异常类 必须继承 Exception

# class   MyException(Exception):
#     def __init__(self,line_num,msg):
#         self.line_num = line_num
#         self.msg = msg
#
#
# try:
#     if 3<4:
#         obj = MyException(2,'自定义异常')
#         raise obj
# except BaseException as err:
#     print(err)

# def test():
#     try:
#         while True:
#             # if a > 4:
#             print('异常')
#             raise BaseException("抛出的异常")
#             print('抛出后')
#     except :
#         print('err')
# 
# test()
# 容易出错的，单独使用 try


答案：
class  defineErr(Exception):
    def __init__(self,line,msg):
        self.line = line
        self.msg  = msg

def  fun():
    a = input('请输入字符串T或者t:')
    #  用符号需要加括号，，使用单词不用加括号
    if  (a == 'T')|( a == 't'):
        try:
            obj = defineErr(3,'抛出异常')
            raise obj
        except BaseException as err:
            print(err)

fun()


'''

'''
187.
"文本文件中存储了多个文章标题、作者，标题和作者之间用若干空格（数量不定）隔开，每行一个，标题有的长有的短，
输出到控制台的时候最多标题长度10，如果超过10，则截取长度8的子串并且最后添加“...”，加一个竖线后输出作者的名字。"
with open('')as f:
     t= f.read()
     读取 split  if len()< 10 [0:8] else: 
'''

'''
字符串  查找 切片 index  运算  + *  分割    对齐  ljust   裁剪  strip    合并 join

utf-8  常用的unicode 编码   字符串  在 爬虫 和   web  开发中  用的 比较多  



补充：

# print( random.sample('zyxwvutsrqponmlkjihgfedcba',5) )  # # 多个字符中生成指定数量的随机字符
#
# a=[1,3,5,6,7]
# random.shuffle(a)
# print(a)

str = "12111，3"
print(str.find('4'))
print(str.find('4'))
print(str.count('1'))
# print(str.index('4'))
# 分割
print(str.split(','))

print('12\n33')

str2='123adf23545'
#  False  不包含换行符  True   包含换行符
['123\n', '23545']
print(str2.splitlines(True))
#  根据传进去的字符串 进行分块，，三部分  前 本 后
print(str2.partition('ad'))
print(str2.startswith('1'))
print(str2.endswith('5'))
print(str2.isalnum())
print(str2.isdigit())

str3 = '11'
print(str3.rjust(3))

str3 ='1234'
str4 = 'qwe'
q = ''.join((str4 ,str3))
print(q)
print(type(q))
str5 = str4.encode('utf-16')
print(str5)
print(str5.decode('utf-16'))
'''

'''
188.
接收用户输入的字符串，将其中的字符以与输入相反的顺序输出

while True:
    str = ''
    for i in range(3):
        a = input("请输入字符串：")

        # for i  in range(100):
        str += a
        # if a == 'p':
        1234
        [1,2,3,4]
        #     for i in range(3):
    print(str)
    for i in range(1,4):
        print(i)
        print(str[-i],end = ',')

'''
'''
189.
"从Email中提取出用户名和域名
1234@qq.com"
#  封装成了函数，方便以后调用
def Extrat(email):
    # email = "1234@qq.com"
    index = email.find('@')
    username = email[:index]
    yuming = email[index+1:]
    return ("您输入的内容为：%s\n用户名为：%s\n域名为：%s"%(email,username,yuming))
a = input("请输入要识别的email:")
print(Extrat(a))
'''

'''
190.
让用户输入一句话,找出所有ee和abc的位置  eeaee  abc  11abc11abc eeeee

#  第一次 ，  少了一次 
a = 'eeaee  abc  11abc11abc eeeee'
index = a.count('ee')
print('ee:',index)
index0 = 0
for i in range(index):
    if index0 ==0:
        print(0)
    index0 = a.index('ee',index0+2)
    print(index0)
'''
# a = input("请输入一句话：")


# index1 = a.index('abc')
# print(index)
# X=[1,2,3,4,5,1,2,3,4]
# print(enumerate(X))
# for i,x in enumerate(X):
#     print(i,X[i])
# l = len(X)
# zip_list = zip(*(range(l),X))
# print(zip_list)
# id1 = [z[0] for i,z in enumerate(zip_list) if z[1]==1]
# print(id1)

# for i  in range(len(X)):
#     if x[i] ==1 :
#         for i, x in enumerate(X):
#

    # id1 = [i for i,x in enumerate(X) if x ==1 ]
    #     print(i)


'''
191.
在需要的时候为字符串补足空格以达到字符串长度相同 格式整齐(PadLeft、PadRight )
str = '1234'
a = str.ljust(8,'#')
b = str.rjust(8,'#')

print(a,b)

'''

'''
192.
去掉字符串中的所有空格
str = '  df dfds   sf   '
# str1 =str.split(' ')
str1 = str.replace(' ','')
print(str1)

'''



'''
193.
"根据完整的路径从路径中分离文件路径、文件名及扩展名
例:""c:\dir1\1.txt""=>""c:\dir1"" ""1"" "".txt"""

#  不足： 没有利用 index  文件名带  .  , 会识别错误
c = "E:\Program Files\program\go\hell.1.go"
print(c)
#  分割路径
a = c.split('\\')
# 获取分割后的结果
b = a[0:-1]
#  获取文件和后缀
E = a[-1]
#  再分割  文件名  后缀
f= E.split('.')
d = '\\'.join(b)
print('E1:',E)
print(b)
print('文件名：',f[0])
print('后缀：',f[-1])
print('路径：',d)
完整版：



def identificatedfile(c):

    # c = "E:\Program Files\program\go\hell.1.go"

    index = c.rfind('\\')
    # 加1 带 斜杠
    path = c[:index]
    # print(path)
    file = c[index+1:]
    # print(file)
    index1 = file.rfind('.')
    filename = file[:index1]
    extend = file[index1+1:]
    # print('输入路径为：%s路径为：%s,文件名为：%s,后缀为：%s'%(c,path,filename,extend))
    return ('您输入路径为：%s \n路径为：%s\n文件名为：%s\n后缀为：%s'%(c,path,filename,extend))

c = input('请输入完整的路径名：')
print(identificatedfile(c))

'''
'''
194.
获取字符串中汉字的个数
#  封装好了方法  
#  不足，中文 符号，被视为 一个汉字 
def Geshu(a):
    ori = len(a)
    a= a.encode('utf-8')
    after=len(a)
    num = (after-ori)//2
    return num


a = input("你输入要查询的字符串：")
print(Geshu(a))
'''



'''
195.
对字符串进行加密与解密
str = 'hello python'
str1 = str.encode('utf-32')
str2 = str1.decode('utf-32')
print(str1,str2)
'''

'''
196.
将字母全部转换为大写或小写

str = 'abcdef'
str1 = str.upper()
str2 = str1.lower()
print(str1)
print(str2)
'''

'''
197.
   根据标点符号对字符串进行分行显示
   
#    还没看懂 
a = "k<n>v,ap.s?i!oe(f)\'lk;sadsfdk"

ls = [",", ".", "?", "!", "(", ")","<", ">", "\'",";", ":"]

for item in ls:
    a = a.replace(item, "\n")

print(a)

for i in range(len(a) - 1 , -1, -1):
    print(i)

'''
# str = 'guhijklsdsc,afgrgh,agrasf,asf.afg'
# str1 =str.splitlines(False)
# print(str1)

#  几率
# a = random.randrange(1,1000)
# print(a)
# if a <= 265:
#     print('26.5')
# else:
#     print('b')
'''
198.
去掉字符串列表中每个字符串的空格

# 根据单个字符串去 空格，扩招到 字符串列表去空格 
list = []

str1 = ['str ',' str','  df dfds   sf   ']

for str in str1:
    s = str.replace(' ','')
    print(s)
    list.append(s)

print(list)

str = '  df dfds   sf   '
# str1 =str.split(' ')
str = str.replace(' ','')
print(str)


'''

'''
199.
让用户输入一个日期格式如“2008/08/08”，将 输入的日期格式转换为“2008年-8月-8日”。


a = '2008/08/08'
index1 = a.index('/')
year = a[:index1]
# print(year)
b = a[index1+1:]
# print(b)
c = b.index('/')

month = b[:c]
# print(len(month))
if int(month)<10:
    month =month[1]
# print(month)

day = b[c+1:]
if int(day)<10:
    day =day[1]

# print(day)


print("%s年-%s月-%s日"%(year,month,day))
'''

'''
200.
接收用户输入的一句英文，将其中的单词以反序输出，“hello c sharp”→“sharp c hello”。


a = 'hello c sharp'

b = a.split(' ')
print(b[0])
print(len(b))
for i in range(1,len(b)+1):
    print(b[-i],end=' ')


'''

'''
201.
"从请求地址中提取出用户名和域名
http://www.163.com?userName=admin&pwd=123456"

a  = 'https://wwww.163.com?userName=admin&pwd=123456'
def Nm(a):
    index = a.index('=')
    b = a[index+1:]
    index2 = b.index('&')
    username = b[:index2]

    index3 = a.index(":")
    c = a[index3+3:]
    yuming = c.split("?")[0]
    return ('域名为：%s\n用户名为：%s'%(yuming,username))


print(Nm(a))
'''

'''
202.
让用户输入一句话,判断这句话中有没有邪恶,如果有邪恶就替换成这种形式然后输出,
如:“老牛很邪恶”,输出后变成”老牛很**”;

#  不足，自能替换一次，不能一次把全部敏感词都替换
a = '老牛很邪恶'
list = ['邪恶','恶心']
for i in range(len(list)):
    if list[i] in a:
        # print(list[i])
        # le = len(i)
        index = a.index(list[i])
        # print(index)
        b = a.replace(list[i],"*"*len(list[i]))
        # b = a[index:index+len[i]]
        set1 = set(b)
print(b)


'''
'''
203.
"如何判断一个字符串是否为另一个字符串的子串
如何验证一个字符串中的每一个字符均在另一个字符串中出现过"

# 有点投机呀  这是简单做了 
a = "abcde"
b = "abcdabcdabcdabcdabcdabcd"

atLeastOne = True
for ia in a:
    if b.find(ia) >= 0:
        pass
    else:
        atLeastOne = False
        break

if atLeastOne :
    print("a的所有字符均在b中出现了")
else:
    print("a中存在某些字符，在b中不存在")


str1 = '1234'
str2 = '1234567890'

def pan(a,b):
    if len(a) > len(b):
        big = a
        small= b
    else:
        big = b
        small = a
    if small in big:
        print('%s是%s的子串'%(small,big))
    else:
        print('%s 不 是%s的子串' % (small, big))

pan(str2,str1)


# 2

def  pan2(small,big):
    # print(big, small)
    flag = None
    for i in range(len(small)):
        if  not small[i] in big:
            # print(small[i])
            # print(type(small[i]))
            flag = False
            break
        else:
            flag = True
    return flag



str1 = '1123456'
str2 = '1234567890'

if len(str1) > len(str2):
    big = str1
    small = str2
else:
    big = str2
    small = str1

# print(pan2(str1, str2))


if pan2(str1, str2) :
    print('%s的每一个元素都出现在了%s 中'%(small,big))
else:
    print('%s的每一个元素  没有全部出现在 %s中' % (small, big))


'''

'''
204.
"如何随机生成带数字和字母的字符串
注意：如何判定一个字符串中既有数字又有字母"

通过 ASCII   

list = [x for x in range(47,58)]+[x for x in range(65,91)]+[x for x in range(97,123)]

str = random.choices(list,k=4)
list2 = []
for i in str:
    list2.append(chr(i))
list3 = ''.join(list2)
print(list3)

# 2  暂时无法完成判断 字母和数字


# print(ord('A'))
# print(type(ord('A')))
def pan4(a):
    list = []
    list1 = []
    # for i in range(len(a)):
    #     if ord(a[i])
    for i in range(0,10):
        flag1 = None
        if  i in a:
            list.append(i)
            flag = True
            break
        else:
    for i in range(65,91):
        if i in a:

    for i in range(97, 123):
        if i in a:
            flag = True
        else:
            flag = True
else:
    flag = True

    return  flag




# print(pan4('123s'))
#
# print(ord('a'))
# print(ord('z'))
# print(ord('A'))
# print(ord('Z'))
# print(ord('0'))
# print(ord('9'))

'''
'''
205.
"""
为一个既有数字又有大小写字母的字符串进行字符排序。
大小写字母排序时需要注意只比较字母的先后次序
例：1CaD =>1aCD

# 思路，，两个串，，一个 转大写 或者 小写，，另一个保持不变
两个串，，位置一样，变化一样，，换到 不区分 大小写的 串上，即可满足，，不区分大小写  排序 




要求使用选择排序
"""

str1 = "3519CeBdAf8"
str2 = str1.upper()

ls1 = list(str1) # 原始串儿
ls2 = list(str2) # 不区分大小写的串儿

for i in range(len(ls2)):
    for j in range(0, len(ls2) - 1 - i):
        if ls2[j] < ls2[j + 1]:
            ls2[j] , ls2[j + 1] = ls2[j + 1], ls2[j]
            ls1[j] , ls1[j + 1] = ls1[j + 1], ls1[j]

print(ls1)

# print(str1)
# print(str2)
#
# print(id(str1), id(str2))

成功：
str1 = 'ACwe'
str2 = str1.upper()
#


ls1 = list(str1) # 原始串儿
ls2 = list(str2) # 不区分大小写的串儿

for i in range(len(ls2)):
    for j in range(0, len(ls2) - 1 - i):
        if ls2[j] > ls2[j + 1]:
            ls2[j] , ls2[j + 1] = ls2[j + 1], ls2[j]
            # ls2[j], ls2[j + 1] = ls2[j + 1], ls2[j]
            ls1[j] , ls1[j + 1] = ls1[j + 1], ls1[j]

print(ls1)

'''
'''
206.接收用户输入的字符串，将其中的字符进行排序（升序），并以逆序的顺序输出，“cabed”→"abcde"→“edcba”。
#  思路：
#  转换成列表  ，利用sort  reverse   在遍历 拼接  即可

s = input("请输入字符串：")
ls = list(s)
#  升序就这么简单
ls.sort()
print(ls)
s1 = ""
for i in range(0,len(ls)):
    s1 += ls[i]
print(s1)

ls.reverse()
s = ""
for i in range(0,len(ls)):
    s += ls[i]
print(s)


'''






'''
212.
使用Array对两个列表进行合并操作

#  数组
import array
arr = array.array('i',[0,1,1,3])
print(arr)
print('arr的类型：')
print(type(arr))

print('\n 输出数组的元属个数：')
print(arr.itemsize)

import numpy as np
a = np.array([[1,2,3,6],[4,5,6,7]])
b = np.array([[1,2,3,1],[2,2,2,4]])

#  数组纵向合并
c = np.vstack((a,b))
print(c)
# 法二：row  行
D = np.r_[a,b]
print(D)

#  横向合并
e = np.hstack((a,b))
print(e)
for i in e:
    print(i)

# 法二：column  列
f = np.c_[a,b]
print(f)

numpy.array  强大，可以同时出列 多个列表，
横向 纵向的 都可以  这就是它 的 强大之处吧  
'''

'''
213.
向列表中追加数据对象，若位置不足，请扩容后追加

'''

'''
214.
如何将10对象随机存入列表中
objlist = [None,None,None]
list1 = []
T = 0
while T <=10:
    b = random.choice(objlist)
    if b not in list1:
        list1.append(b)
        T +=1
    else:
        break
'''
'''
218.
"如何用队列实现约瑟夫环
约瑟夫环：假设有n个人坐成一圈，从某个人开始报数，数到m的人出圈，
接着从出圈的下一个人开始重新报数，数到m的人再次出圈，如此反复，直到所有人都出圈，
请列出出圈顺序。"

'''

# def joseph(total, begins, count):
# 	queue = [range(1, total + 1)]
# 	death = (begins + count - 2) % len(queue)
# 	for times in range(total - 1):
# 		print ('out: ', queue[death])
# 		del queue[death]
# 		death = (death + count -1) % len(queue)
# 	print ('survivor: ', queue[0])
#
#
# print(joseph(5, 1, 2))


t = 0
s = 0



if t> 3:
    t = 1







