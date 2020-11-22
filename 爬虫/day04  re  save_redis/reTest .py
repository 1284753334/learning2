#!/usr/bin/env python
# coding: utf-8

# In[6]:


import re


# In[7]:


# .匹配任意字符(除了\n)
ret = re.match(".","@b3=2@abc")
print(type(ret))
print(ret.group())


# In[8]:


#匹配列举的字符
ret = re.match("[hH]","hello Python")
print(ret.group())
ret = re.match("[a-zA-Z0-9]","Hello Python")
print(ret.group())


# In[6]:


#匹配数字
ret = re.match("嫦娥\d号","嫦娥3号发射成功")
print(ret.group())
ret = re.match("嫦娥\d号","嫦娥4号发射成功")
print(ret.group())
ret = re.match("嫦娥\d号","嫦娥5号发射成功")
print(ret.group())


# In[9]:


ret = re.match("[0-9]","687Hello Python")
print(ret.group())


# In[11]:


#匹配单词字符\w
ret = re.match('\w\w\w\w\w\w\w\w','Hello12_ world')
ret.group()


# In[14]:


#匹配非单词字符\W
ret = re.match('\W','#@Hello12_ world')
ret.group()


# In[15]:


#匹配空白字符\s
ret = re.match('\w\w\w\w\w\w\w\w\s\w\w\w\w\w','Hello12_ world')
ret.group()


# In[16]:


# * 匹配一个字符0到多次  
ret = re.match("[A-Z][a-z]a*","China")
print(ret.group())
ret = re.match("[A-Z][a-z]*?a*","Chinaaaaaaa")
print(ret.group())
ret = re.match("[A-Z][a-z]*?a","Chinaaaaaaa")
print(ret.group())
ret = re.match("[A-Z][a-z]*a","Chinaaaaaaa")
print(ret.group())


# In[17]:


# + 匹配前一个元字符1到多次
ret = re.match("[a-zA-Z_]+","__init__")
ret.group()


# In[10]:


#?匹配前一个元字符0到1次
ret = re.match("[1-9]?[0-9]","99")
ret.group()


# In[22]:


#匹配前一个元字符m到n次
ret = re.match("[a-zA-Z0-9_-]{8,20}","2018-07-01")
print(ret.group())
ret = re.match("[a-zA-Z0-9_-]{8,}","2018-07-01")
print(ret.group())
ret = re.match("[a-zA-Z0-9_-]{,20}","2018-")
print(ret.group())
#ret = re.match("[a-zA-Z0-9_-]{8,}","2018-")
#print(ret.group())


# In[25]:


# 通过$来确定末尾
ret = re.match("^\w{4,20}@163\.com$", "xiaoWang@163.com")
ret.group()


# In[26]:


ret = re.match("^[1-9]?[0-9]$","72")
ret.group()


# In[28]:


#引用分组num匹配到的字符串
ret = re.match(r"<(\w+)><(\w+)>.+</\2></\1>", "<html><h1>www.baidu.com</h1></html>")
ret.group()


# In[29]:


# 命名分组，引用别名为name的分组匹配到的字符串
ret = re.match("<(?P<name1>\w+)><(?P<name2>\w+)>.*</(?P=name2)></(?P=name1)>", "<html><h1>www.baidu.com</h1></html>")
ret.group()


# In[31]:


s = 'hello World!'
regex = re.compile("Hello world!", re.I)
print(regex.match(s).group())


# In[32]:


#匹配换行
s = '''first line
second line
third line'''
#
regex = re.compile(".+")
print(type(regex))
print(regex.findall(s))
print(regex.match(s).group())

# re.S
regex_dotall = re.compile(".+", re.S)
print(regex_dotall.findall(s))
print(regex_dotall.match(s).group())


# In[11]:


import re
pattern = re.compile(r'\d+') # 用于匹配至少一个数字
m = pattern.match('one12twothree34four') # 查找头部，没有匹配
print(m) 
m = pattern.match('one12twothree34four', 2, 10) # 从'e'的位置开始匹配，没有
# 匹配
print(m)


# In[15]:


import  re
pattern = re.compile(r'\d+') # 用于匹配至少一个数字
m = pattern.match('one12twothree34four', 3, 10) # 从'1'的位置开始匹配，正好
print(m) # 返回一个 Match 对象
print(m.group(0)) # 可省略 0
print(m.start(0)) # 可省略 0
print(m.end(0)) # 可省略 0
print(m.span(0)) # 可省略


# In[18]:


import re
pattern = re.compile('\d+')
m = pattern.search('one12twothree34four') # 这里如果使用 match 方法则不匹配
print(m.group()) 
m = pattern.search('one12twothree34four', 10, 30) # 指定字符串区间
print(m.group())
print(m.span())


# In[30]:


import re
pattern = re.compile(r'\d+') # 查找数字
result1 = pattern.findall('hello 123456 789')
result2 = pattern.findall('one1two2three3four4', 0, 10)
print(result1)
print(result2)


# In[20]:


import re
pattern = re.compile(r'\d+')
result_iter1 = pattern.finditer('hello 123456 789')
result_iter2 = pattern.finditer('one1two2three3four4', 0, 10)
print(type(result_iter1))
print(type(result_iter2))
print('result1...')
for m1 in result_iter1: # m1 是 Match 对象
 print('matching string: {}, position: {}'.format(m1.group(), m1.span()))
print('result2...')
for m2 in result_iter2:
 print('matching string: {}, position: {}'.format(m2.group(), m2.span()))


# In[33]:

#  sub
import re
p = re.compile(r'(\w+) (\w+)') # \w = [A-Za-z0-9]
# p = re.compile(r'\d+') # \w = [A-Za-z0-9]
s = 'hello 123, hello 456'
print(p.sub(r'hello world', s)) # 使用 'hello world' 替换 'hello 123' 和
'hello 456'
print(p.sub(r'\2 \1', s)) # 引用分组
def func(m):
    return 'hi' + ' ' + m.group(2)
print( p.sub(func, s))
print (p.sub(func, s, 1)) # 最多替换一次


# In[ ]:




