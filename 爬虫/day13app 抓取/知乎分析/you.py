import requests
from lxml import etree
import time,random

import urllib3
#headers = {
#       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
#      "Cookie":'_zap=87dfa820-dc30-4b4b-9fb8-55b59f6746a4; d_c0="APAghnqdyw-PTrZvnknWN_9212Jb1mPp9QA=|1564142419"; capsion_ticket="2|1:0|10:1566305613|14:capsion_ticket|44:MGUwZjIyMmVlOTQ0NDQ5MWEzNTkwYTA1MTRhNTk0ODA=|90e91d1c132e64306e99197cae9119e74fccbcddf1b93fc618a1b6ac26952732"; z_c0="2|1:0|10:1566305632|4:z_c0|92:Mi4xdUxkU0J3QUFBQUFBOENDR2VwM0xEeVlBQUFCZ0FsVk5ZRHRKWGdBTHZraTRETVJBYTEwWXpIQkxTQUdQVWJIckxn|8ca193f22274ab1d9a429f83426705f6b55acf7b9ddf635bd754883932a01494"; tst=r; _xsrf=0c258e96-d95a-4feb-973b-53963a308776; tgw_l7_route=73af20938a97f63d9b695ad561c4c10c',
#
#   }

requests.packages.urllib3.disable_warnings()
headers = {
    'Cookie' :'_zap=edb3b5be-3191-4b42-ad56-4946e51664e7; d_c0="ALAY9fOPtRGPTgI_JX0RYun9Bg5iu8XKeX8=|1597022216"; _ga=GA1.2.154495460.1597022218; _xsrf=ecbd3356-07c5-44ff-b339-e04ac060fc8c; q_c1=6adf5998f86243daa38cb5a8f9bae90e|1601564859000|1597035262000; tst=r; capsion_ticket="2|1:0|10:1604800279|14:capsion_ticket|44:OGJlN2QzZmM3N2QyNGRkZWFmMGJiZjIyMmI2OGZjMTA=|cbc3a01bc4fa34711bec37184b369db53d32a311e1af6aac4a1138586d883a73"; z_c0="2|1:0|10:1604800353|4:z_c0|92:Mi4xNDN1NURBQUFBQUFBc0JqMTg0LTFFU2NBQUFDRUFsVk5ZZHpPWHdDQ1RlXzMtSEhCX2VOQ29zUkxIcFdMU01Ia3JB|d6da98b92e24f8a01ab48af8c8117ede9ca1d7f394b2d2dc27ef7a7a3467a802"; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1604720871,1604731085,1604747340,1604816984; SESSIONID=Spa7sulsO8mGHOwYtJ5DK4SVqqgpKhH4vOVpCrQvJ6p; JOID=U1AQC0oUyQ4TkKxjLB0g38CrMN85TrRiLePQAlJb-G5Z0eMdeEpZrUWZqGMoT5TN7zNuN0rA6lr9nykLFxvq48o=; osd=Wl8dB0IdxgMfmKVsIREo1s-mPNcwQbluJerfD15T8WFU3esUd0dVpUyWpW8gRpvA4ztnOEfM4lPykiUDHhTn78I=; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1604819280; KLBRSID=cdfcc1d45d024a211bb7144f66bda2cf|1604822273|1604816977',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
}



def down_firstweb(url):
    # 首先 爬取首页内容

    response = requests.get(url, headers=headers,verify=False)
    html = response.text
    html = etree.HTML(html)
    laoties = html.xpath('.//div[@class="Card TopstoryItem TopstoryItem-isRecommend"]')
    for temp in laoties:
        title = temp.xpath('.//h2//a/text()')[0]
        cont = temp.xpath('.//div[@class="RichContent-inner"]/span/text()')[0]
        cont_url = "https://www.zhihu.com/"+ temp.xpath('.//h2//a/@href')[0]
        favor = temp.xpath('.//div[@class="ContentItem-actions"]/span/button/text()')
        if len(favor):
            favor = favor[0]
        else:
            favor = "未知"
        print("标题：",title)
        print("简介：",cont)
        print("详情链接：", cont_url)
        print(favor)

        print("*" * 50, "华丽的分隔符", "*" * 50)
def ajax(url):
    try:
        response = requests.get(url, headers=headers,verify=False)
        laoties = response.json()['data']
        for temp in laoties:
            title = temp["target"]["question"]["title"]
            cont = temp["target"]["excerpt_new"]
            favor = temp["target"]["voteup_count"]

            print("标题：", title)
            print("简介：", cont)
            print("赞同数",favor)
            print("*" * 50, "华丽的分隔符", "*" * 50)

        next_url = response.json()['paging']['next']
        print("下一次异步请求路径：",next_url)
        time.sleep(random.random()*3)
        ajax(next_url)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    url = "https://www.zhihu.com/"
    down_firstweb(url)
    url = "https://www.zhihu.com/api/v3/feed/topstory/recommend?session_token=2e5f6496d2a96f92ef20d4d087fd584d&desktop=true&page_number=2&limit=6&action=down&after_id=5"
    ajax(url)






