'''

"如何用队列实现约瑟夫环
约瑟夫环：假设有n(n= 100)个人坐成一圈，从某(第一个人)个人开始报数，数到m的人出圈，
接着从出圈的下一个人开始重新报数，数到m的人再次出圈，如此反复，
直到所有人都出圈，请列出出圈顺序。"

# '''
# n = 100
# list = [x for x in range(n)]
# list[len(list)] = 0

'''
 30  15  1  9  出仓顺序 
'''
# people={}
# for x in range(1,31):
#     people[x]=1
# # print(people)
# #  零 表示在圈内
# check=0
# #  1 在圈外
# i=1
# # 出圈的人数  ，会 累加
# j=0
# while i<=31:
#     # 循环  31  之后是1
#     if i == 31:
#         i=1
#     #     计数 ：出圈人数  等于15  结束 游戏
#     elif j == 15:
#         break
#     else:
#         if people[i] == 0:
#             i+=1
#             continue
#         else:
#             check+=1
#             if check == 9:
#                 people[i]=0
#                 check = 0
#                 print("{}号下船了".format(i))
#                 j+=1
#             else:
#                 i+=1
#                 continue
#
'''
https://blog.csdn.net/jiangjiang_jian/article/details/81744435?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522160336088019724835821603%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=160336088019724835821603&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_v2~rank_blog_default-1-81744435.pc_v2_rank_blog_default&utm_term=%E7%BA%A6%E7%91%9F%E5%A4%AB%E9%97%AE%E9%A2%98+python&spm=1018.2118.3001.4187
1.首先我们把这n个人的序号编号从0~n-1
     m > n 
     m = n 
 一开始的时候，所有人的编号排成序列的模式即为：
0,1,2,3,4,5...n-2，n-1
#   注意  0  开始   
m < n  输出的是 编号 
那么第一次出列的人的 编号  则是(m-1)%n1  k1=m%n1

第一次：
1，2，3，4，5，6  .。。 m-1      m        m+1    m+2....           n
0  1  2 3   4  5        m-2      m-1       m     m+1 ...          n-1(n-2)
                                (m-1)%n1   m%n1
                                   k         k1   k1+1             k+n-2 
                        

比如：
n = 5
m = 3


第二次：
n-1人编号：
# 8   的 序号是 7 
k1，k1+1，k1+2，k1+3   ...          k1+n-2   0 
#  实际报号：
0,    1，    2,   3    ....          n-2

(k1+n-2)%n1
那么在这剩下的n-1个人中，我们也可以为了方便，将这n-1个人编号为：
n-1 人的编号
1 2 3 4 5 6    m   m+1  m+2      
0,1,2,3,4.    m-1  m   m+1   M+2  ..n-2
#  编号 出列(M-1)% N2
                  K2   K2+1  k2+2     k2+ n-3
                  0    1        2  




'''


# # 法二：
# class Solution:
#     #   n 个人  数到 m 出列
#     def LastRemaining_Solution(self, n, m):
#         if n < 1:
#             return -1
#         con = range(n)
#         final = -1
#         start = 0
#         while con:
#             k = (start + m - 1) % n
#             final = con.pop(k)
#             n -= 1
#             start = k
# 
#         return final






