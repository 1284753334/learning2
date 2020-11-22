#                    _ooOoo_
#                   o8888888o
#                   88" . "88
#                   (| -_- |)
#                   O\  =  /O
#                ____/`---'\____
#              .'  \\|     |//  `.
#             /  \\|||  :  |||//  \
#            /  _||||| -:- |||||-  \
#            |   | \\\  -  /// |   |
#            | \_|  ''\---/''  |   |
#            \  .-\__  `-`  ___/-. /
#          ___`. .'  /--.--\  `. . __
#       ."" '<  `.___\_<|>_/___.'  >'"".
#      | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#      \  \ `-.   \_ __\ /__ _/   .-` /  /
# ======`-.____`-.___\_____/___.-`____.-'======
#                    `=---='
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#             佛祖保佑       永无BUG

import requests
import json
import urllib3
from lxml import etree
#  避免ssl 警告
urllib3.disable_warnings()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    # 'Cookie': '_zap=e4c69db8-2dfb-4297-a38e-5b570f203604; _xsrf=FJOlMAJhAsqDK8NSTLApzEQeFlnhYBdX; d_c0="AFBjzCvo8Q6PTlbVQWyuddpyNqUM7BDSj9M=|1549532267"; tst=r; __gads=ID=75a1fdbc9f9167cc:T=1554123373:S=ALNI_MYQgwMeViwVE-Sf46R5QV8AeRreRw; __utmz=51854390.1559801941.10.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/signup; z_c0="2|1:0|10:1559802027|4:z_c0|92:Mi4xaUZvQ0N3QUFBQUFBVUdQTUstanhEaVlBQUFCZ0FsVk5xXzdsWFFBMFVzMDhrTXJNVzFsMndzUmE0cjMwVWswSjRn|1a920736708a3a7bf708f5268b86f3dfd7a480687613b43271809203dc9ae5dc"; __utmv=51854390.100--|2=registration_date=20180714=1^3=entry_date=20180714=1; __utma=51854390.1653671287.1549877340.1564109168.1564111474.12; q_c1=e7d0cd93220641f18e176549aedeb9dc|1567831387000|1549684664000',
    'Cookie': '_zap=edb3b5be-3191-4b42-ad56-4946e51664e7; d_c0="ALAY9fOPtRGPTgI_JX0RYun9Bg5iu8XKeX8=|1597022216"; _ga=GA1.2.154495460.1597022218; _xsrf=ecbd3356-07c5-44ff-b339-e04ac060fc8c; tst=f; capsion_ticket="2|1:0|10:1601564859|14:capsion_ticket|44:MjM3NDMyMjcxYmI3NDI1MDhjM2ExYjQzMjNlZjljZjg=|21a2849a50e7ec09d108563f6dc3a8fd0813a6a17ba5dfa5e9e45781ff496b80"; z_c0="2|1:0|10:1601564859|4:z_c0|92:Mi4xNDN1NURBQUFBQUFBc0JqMTg0LTFFU1lBQUFCZ0FsVk51ejVqWUFEX2xDS1FpTTR3czdoX2lBYUNrWVYzU0pEVC13|577d8a68e8abbf7b12b1306c61e3eed5cf0f4ff0cee9f232ad20e61ce8ac1210"; q_c1=6adf5998f86243daa38cb5a8f9bae90e|1601564859000|1597035262000; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1601295470,1601564773,1601567004,1601907107; _gid=GA1.2.1765030203.1601907108; SESSIONID=C6AgxuQvGxhea7dIGYneBMI6mRjO6acqpACBO2foNkU; JOID=Vl0WC0g51euiTS0sPzUzOXxytJ8pe-WhzjJZe0J5rIXMJx1JcJvxkPFLKiE_jWW1bdTMfVKHFSJF7hSg4aX0nkE=; osd=UFoQAE4_0u2pSysrOT41P3t0v5kvfOOqyDRefUl_qoLKLBtPd536lvdMLCo5i2KzZtLKelSMEyRC6B-m56LylUc=; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1601907946; KLBRSID=76ae5fb4fba0f519d97e594f1cef9fab|1601908380|1601907103',
    #'Referer': 'https://www.zhihu.com/signup?next=%2F',
    #'Accept-Encoding': 'gzip, deflate',
    #'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    #'Accept-Language': 'zh-CN,zh;q=0.9',
    #'Connection': 'keep-alive',
}
url = 'https://www.zhihu.com/'
response = requests.get(url, headers=headers, verify=False)
html = response.text
# print(html)
html = etree.HTML(html)
#print(etree.tostring(html, pretty_print=True).decode())
ls = html.xpath('//div[@class="Card TopstoryItem TopstoryItem-isRecommend"]')
# //*[@id="TopstoryContent"]/div/div/div/div[1]
# ls = html.xpath('//div[@class= "Topstory-follow"]/div/div[1]')
# ls = html.xpath('//*[@id="TopstoryContent"]/div/div/div/div')
# print(len(ls))
ls = html.xpath('//div[@class="Card TopstoryItem TopstoryItem--old TopstoryItem-isFollow"]')
for item in ls:
    title = item.xpath('.//h2//a/text()')[0]
    print(title)
    #url = item.xpath('.//h2//a/@href')[0]
    #print(url)
    brief = item.xpath('.//span[@class="RichText ztext CopyrightRichText-richText"]/text()')[0].strip()
    print(brief)
    print('=' * 60)

#  模拟ajax 下载数据   https://www.zhihu.com/api/v3/feed/topstory/recommend?limit=10&desktop=true
# https://www.zhihu.com/api/v3/feed/topstory/recommend?session_token=c6fce24a6cb75b9b9eb0256ba301405a&desktop=true&page_number=2&limit=6&action=down&after_id=5&ad_interval=-1
url = 'https://www.zhihu.com/api/v3/feed/topstory/recommend'
page_number = 2
limit = 6
after_id = 5
for page in range(2,15):
    params = {
        'session_token': 'fb76d600ecf59cb35c75250dad3bba6e',
        'desktop': 'true',
        'page_number': page_number,
        'limit': limit,
        'action': 'down',
        'after_id': after_id,
    }
    print('test...')
    data=requests.get(url=url,headers=headers,params=params,verify=False).text
    data = json.loads(data)['data']
    for item in data:
        #print(item)
        title = '无'
        if 'target' in item:
            if 'question' in item['target']:
                if 'title' in item['target']['question']:
                    title = item['target']['question']['title']
            elif 'title' in item['target']:
                title = item['target']['title']
        elif 'title' in item:
            title = item['title']
        print(title)
        brief = item['target']['excerpt']
        print(brief)
        print('=' * 60)
    page_number +=1
    after_id +=6
