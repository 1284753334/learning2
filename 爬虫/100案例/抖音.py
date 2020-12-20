#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2020/11/16 23:12:18

@author: Json

        认真大胆      永无BUG
"""

''''
抖音目前由分享的的单个视频url,复制粘贴到浏览器，会发生跳转，

开发者工具，查看请求头的url，，
# https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={item_id}"

点击会跳转到 一个  json  页面，格式化后，，找到 play_addr，url_list
点击第一个会发生跳转到播放页面，这时就可以下载了。

点击这个url，发生跳转，
'''
import os
import re
import urllib

import requests




'''
https://v.douyin.com/JQ35XFV/
'''
headers = {
    'accept': 'application/json',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
}


def get(share_url) -> dict:
    """
    author, title, audioName, audios, videoName, videos
    """
    data = {}
    headers = {
        'accept': 'application/json',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
    }
    api = "https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={item_id}"

    rep = requests.get(share_url, headers=headers, timeout=10)
    if rep.ok:
        # item_id
        print(rep.url)
        item_id = re.findall(r'video/(\d+)', rep.url)
        print(item_id[0])
        if item_id:
            item_id = item_id[0]
            # video info
            rep = requests.get(api.format(item_id=item_id), headers=headers, timeout=10)
            if rep.ok and rep.json()["status_code"] == 0:
                info = rep.json()["item_list"][0]

                data["author"] = info["author"]["nickname"]
                # name = ht['item_list'][0]['author']['nickname']
                data["title"] = data["videoName"] = info["desc"]
                print('author:',data["author"])
                if info.get('music'):
                    data["audioName"] = info["music"]["title"]
                    data["audios"] = [info["music"]["play_url"]["uri"]]
                # data["imgs"] = [info["video"]["origin_cover"]["url_list"][0]]

                # playwm_url -> play_url
                # play_url = info["video"]["play_addr"]["url_list"][0].replace('playwm', 'play')
                play_url = info["video"]["play_addr"]["url_list"][0]
                data["videos"] = [play_url]
                print('data:',data)
                return data
    return {'msg': '获取失败'}


if __name__ == "__main__":
    data = get(input('share url: '))
    url = data['videos'][0]
    # header = {}
    print('ss',data)
    print('url:',url)
    html = requests.get(url, headers=headers, timeout=10).url
    print('html:',html)

# html = 'http://v5-dy-j.ixigua.com/f54e32a6096ca72c5ac4e18c68ae1894/5fc336ff/video/tos/hxsy/tos-hxsy-ve-0015/7a2b1e4fb2b64cc18beb253b20503183/?a=1128&br=6519&bt=2173&cr=0&cs=0&cv=1&dr=0&ds=3&er=&l=2020112912513301019806013116D7009D&lr=aweme&mime_type=video_mp4&qs=0&rc=ajNvdWQ7OmV2cTMzM2kzM0ApaGRoNjk1Mzw5N2Y5ZTU1N2dsMTBuZm5kY2FfLS0zLS9zczNeMC40LmEvNmAxLTAzYS06Yw%3D%3D&vl=&vr='
   # 下载

    # html = 'http://v26-dy-cold.ixigua.com/a4d4f85baa48cf5f1d047c41dd44a369/5fc3370e/video/tos/hxsy/tos-hxsy-ve-0015/7a2b1e4fb2b64cc18beb253b20503183/?a=1128&br=6519&bt=2173&cr=0&cs=0&cv=1&dr=0&ds=3&er=&l=2020112912514801019808710251D4FF76&lr=aweme&mime_type=video_mp4&qs=0&rc=ajNvdWQ7OmV2cTMzM2kzM0ApaGRoNjk1Mzw5N2Y5ZTU1N2dsMTBuZm5kY2FfLS0zLS9zczNeMC40LmEvNmAxLTAzYS06Yw%3D%3D&vl=&vr='
    if not os.path.exists('同学们视频'):
        os.mkdir('同学们视频')
    # urllib.request.urlretrieve(html, '同学们视频\\' + data['author']+ '.mp4')
    urllib.request.urlretrieve(html, '同学们视频\\' + data['author']+ '.mp4')

    print('下载完成')
'''
url: url2 =  'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids='+post+ '$line0'
https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f600000bndsfbg7q8iaqr3l40og&ratio=720p&line=0
html: htt


url: https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f600000bndsfbg7q8iaqr3l40og&ratio=720p&line=0
html: http://v5-dy-g.ixigua.com/ad0c635416c143b965785607262dc0ab/5fc3342e/video/tos/hxsy/tos-hxsy-ve-0015/7a2b1e4fb2b64cc18beb253b20503183/?a=1128&br=6519&bt=2173&cr=0&cs=0&cv=1&dr=0&ds=3&er=&l=2020112912393201019806215512D56F99&lr=aweme&mime_type=video_mp4&qs=0&rc=ajNvdWQ7OmV2cTMzM2kzM0ApaGRoNjk1Mzw5N2Y5ZTU1N2dsMTBuZm5kY2FfLS0zLS9zczNeMC40LmEvNmAxLTAzYS06Yw%3D%3D&vl=&vr=
下载完成

      https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f600000bndsfbg7q8iaqr3l40og&ratio=720p&line=0
p:    https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f600000bndsfbg7q8iaqr3l40og&ratio=720p&line=0
URL2: https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f600000bndsfbg7q8iaqr3l40og&ratio=720p&line=0
html: http://v29-dy-cold.ixigua.com/41a44d146be293792e411ffb899f329e/5fc333ca/video/tos/hxsy/tos-hxsy-ve-0015/7a2b1e4fb2b64cc18beb253b20503183/?a=1128&br=6519&bt=2173&cr=0&cs=0&cv=1&dr=0&ds=3&er=&l=202011291237520101980650804CD44C33&lr=aweme&mime_type=video_mp4&qs=0&rc=ajNvdWQ7OmV2cTMzM2kzM0ApaGRoNjk1Mzw5N2Y5ZTU1N2dsMTBuZm5kY2FfLS0zLS9zczNeMC40LmEvNmAxLTAzYS06Yw%3D%3D&vl=&vr=
html: http://v5-dy-g.ixigua.com/ad0c635416c143b965785607262dc0ab/5fc3342e/video/tos/hxsy/tos-hxsy-ve-0015/7a2b1e4fb2b64cc18beb253b20503183/?a=1128&br=6519&bt=2173&cr=0&cs=0&cv=1&dr=0&ds=3&er=&l=2020112912393201019806215512D56F99&lr=aweme&mime_type=video_mp4&qs=0&rc=ajNvdWQ7OmV2cTMzM2kzM0ApaGRoNjk1Mzw5N2Y5ZTU1N2dsMTBuZm5kY2FfLS0zLS9zczNeMC40LmEvNmAxLTAzYS06Yw%3D%3D&vl=&vr=

下载完成

'''