import os
import urllib
from os import mkdir

url2 =  'https://v.douyin.com/JQ35XFV/'


import requests

import  re
def get(url2):
    html = requests.get(url2,timeout = 10).url
    ht = re.findall(r'\d+',html)
    print(ht)
    url = 'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids='+ht[0]
    print('url：',url)
    # 'https://www.iesdouyin.com/share/video/6763218987665935624/?region=CN&mid=6763192848395045635&u_code=14kjed47i&titleType=title&did=69946580992&iid=3183825382289101&utm_source=copy_link&utm_campaign=client_share&utm_medium=android&app=aweme'



# def douyin(url):
#     mkdir('视频//')
#     html = requests.get(url, timeout=10).url
#     ht = re.findall(r'\d+', html)
#     #  拼接接口地址
#     url = 'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids='+ht[0]

    # headers = {
    #     'accept': 'application/json',
    #     'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
    # }
    headers = {
        'accept': 'application/json',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
    }

    html = requests.get(url)
    ht = html.json()
    print('ht:',ht)

    # url1 = 'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=' +ids[0]
    name = ht['item_list'][0]['author']['nickname']
    # post = ht['item_list'][0]['video']['play_addr']['uri']
    post = ht['item_list'][0]['video']['play_addr']['url_list'][0]
    print('p:',post)
#    拼接视频地址
#     'https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f600000bndsfbg7q8iaqr3l40og&ratio=720p&line=0'
#     url2 =  'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids='+ht[0]+ '$line0'
    'https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f600000bndsfbg7q8iaqr3l40og&ratio=720p&line=0'
    # url2 =  'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids='+post+ '$line0'
    url2 = post
    print('URL2:',url2)

#    获取视频文件
    html = requests.get(url2,headers = headers,timeout = 10).url
#     print('html:',html)
#
# #    下载
# #     name1 = 'video2'
#     if not os.path.exists('asd'):
#         # os.mkdir('同学们视频')
#         os.mkdir('asd')
#     urllib.request.urlretrieve(html,'asd\\'+name+'.mp4')
#
#     print('下载完成')
    print('html:', html)
    #    下载
    if not os.path.exists('同学们视频'):
        os.mkdir('同学们视频')
    urllib.request.urlretrieve(html, '同学们视频\\' + name + '.mp4')

    print('下载完成')

# html = ' http://v26-dy-cold.ixigua.com/4d6311fdb2f8feb4414296aa748df2ab/5fc3385d/video/tos/hxsy/tos-hxsy-ve-0015/7a2b1e4fb2b64cc18beb253b20503183/?a=1128&br=6519&bt=2173&cr=0&cs=0&cv=1&dr=0&ds=3&er=&l=2020112912572301019806213442D70C42&lr=aweme&mime_type=video_mp4&qs=0&rc=ajNvdWQ7OmV2cTMzM2kzM0ApaGRoNjk1Mzw5N2Y5ZTU1N2dsMTBuZm5kY2FfLS0zLS9zczNeMC40LmEvNmAxLTAzYS06Yw%3D%3D&vl=&vr='
#
#     print('html:',html)
#     #    下载
#     if not os.path.exists('同学们视频'):
#         os.mkdir('同学们视频')
#     urllib.request.urlretrieve(html, '同学们视频\\' + name + '.mp4')
#
#     print('下载完成')



'https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f600000bndsfbg7q8iaqr3l40og&ratio=720p&line=0"'



get(url2)




'http://v29-dy-cold.ixigua.com/b75becb645d523d9dacdb1be754932d4/5fc3229a/video/tos/hxsy/tos-hxsy-ve-0015/7a2b1e4fb2b64cc18beb253b20503183/?a=1128&br=6519&bt=2173&cr=0&cs=0&cv=1&dr=0&ds=3&er=&l=2020112911243201019808206716CA3C1D&lr=aweme&mime_type=video_mp4&qs=0&rc=ajNvdWQ7OmV2cTMzM2kzM0ApaGRoNjk1Mzw5N2Y5ZTU1N2dsMTBuZm5kY2FfLS0zLS9zczNeMC40LmEvNmAxLTAzYS06Yw%3D%3D&vl=&vr='


