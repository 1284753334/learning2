"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/7/11'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
# 获取一个有登录信息的Cookie模拟登陆
import requests

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Cookie": '_zap=e4c69db8-2dfb-4297-a38e-5b570f203604; _xsrf=FJOlMAJhAsqDK8NSTLApzEQeFlnhYBdX; d_c0="AFBjzCvo8Q6PTlbVQWyuddpyNqUM7BDSj9M=|1549532267"; tst=r; __gads=ID=75a1fdbc9f9167cc:T=1554123373:S=ALNI_MYQgwMeViwVE-Sf46R5QV8AeRreRw; __utmz=51854390.1559801941.10.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/signup; z_c0="2|1:0|10:1559802027|4:z_c0|92:Mi4xaUZvQ0N3QUFBQUFBVUdQTUstanhEaVlBQUFCZ0FsVk5xXzdsWFFBMFVzMDhrTXJNVzFsMndzUmE0cjMwVWswSjRn|1a920736708a3a7bf708f5268b86f3dfd7a480687613b43271809203dc9ae5dc"; __utmv=51854390.100--|2=registration_date=20180714=1^3=entry_date=20180714=1; __utma=51854390.1653671287.1549877340.1564109168.1564111474.12; q_c1=e7d0cd93220641f18e176549aedeb9dc|1567831387000|1549684664000; tgw_l7_route=7bacb9af7224ed68945ce419f4dea76d',
}

response = requests.get("https://www.zhihu.com/", headers=headers)
html = response.text
print(html)


