# 汉诺塔问题
#
#  把n-1个盘子看成一个整体 ，整体经c 移动到B，在将最后一个盘子移动到c,
# 在将n-1 个盘子 从 b，经a,移动到c
def hanoi (n,a,b,c):
    if  n > 0:
        hanoi(n-1,a,c,b)
        print('moving from %s to %s'%(a,c))
        hanoi(n-1,b,a,c)
hanoi(3,"A","B","C")




