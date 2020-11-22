import re

text = """
    <ul>
    <li><a href="http://www.xbiquge.la/">首页</a></li>
    <li><a href="/modules/article/bookcase.php">我的书架</a></li>
    <li><a href="/xuanhuanxiaoshuo/">玄幻小说</a></li>
    <li><a href="/xiuzhenxiaoshuo/">修真小说</a></li>
    <li><a href="/dushixiaoshuo/">都市小说</a></li>
    <li><a href="/chuanyuexiaoshuo/">穿越小说</a></li>
    <li><a href="/wangyouxiaoshuo/">网游小说</a></li>
    <li><a href="/kehuanxiaoshuo/">科幻小说</a></li>
    <li><a href="/paihangbang/">排行榜单</a></li>
    <li><a href="/xiaoshuodaquan/">全部小说</a></li>
    </ul>
"""
# regex = 'href=".+?">.+?</a>'
# m = re.findall(regex, text)
# print(m)

# iter = re.finditer(regex , text)
# print(iter)

# full = re.fullmatch(regex, text)
#
# print(full)

s = "测试,abc 12456:32435 "
# #
regex = "(45|43)"
# #
# list = re.split(regex, s)
#
# print(list)
# #
# #
t = re.sub(regex, "哈哈", s)

print(t)
