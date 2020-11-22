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

pn = 1
headers = {'User-Agent':'Dalvik/1.6.0 (Linux; U; Android 4.4.2; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10)'}
#url = 'http://gamehelper.gm825.com/wzry/hot/information?channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=13.0.1.0&version_code=13010&cuid=C8B595533A5E4F03B5B2A3839EFF8A1B&ovr=4.4.2&device=HUAWEI+_HUAWEI+MLA-AL10&net_type=1&client_id=9tcu5xhbpYYN6sxHKeVMcA%3D%3D&info_ms=5mYJrrjSbSut9IK6BQNriw%3D%3D&info_ma=3q8SJYmLxl%2Fiv0Am%2FAiHae0xlIUVwrhC3mS0zlXjskA%3D&mno=0&info_la=xIYTbOcOjEd%2FTFTutRfK8Q%3D%3D&info_ci=xIYTbOcOjEd%2FTFTutRfK8Q%3D%3D&mcc=0&clientversion=13.0.1.0&bssid=3q8SJYmLxl%2Fiv0Am%2FAiHae0xlIUVwrhC3mS0zlXjskA%3D&os_level=19&os_id=08d40ce27ef36489&resolution=720_1280&dpi=240&client_ip=192.168.10.148&pdunid=ce27ef3648908d40'

for pn in range(1,5):
    url = 'http://gamehelper.gm825.com/wzry/news/list?pn='+str(pn)+'&channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=13.0.1.0&version_code=13010&cuid=C8B595533A5E4F03B5B2A3839EFF8A1B&ovr=4.4.2&device=HUAWEI+_HUAWEI+MLA-AL10&net_type=1&client_id=9tcu5xhbpYYN6sxHKeVMcA%3D%3D&info_ms=5mYJrrjSbSut9IK6BQNriw%3D%3D&info_ma=3q8SJYmLxl%2Fiv0Am%2FAiHae0xlIUVwrhC3mS0zlXjskA%3D&mno=0&info_la=xIYTbOcOjEd%2FTFTutRfK8Q%3D%3D&info_ci=xIYTbOcOjEd%2FTFTutRfK8Q%3D%3D&mcc=0&clientversion=13.0.1.0&bssid=3q8SJYmLxl%2Fiv0Am%2FAiHae0xlIUVwrhC3mS0zlXjskA%3D&os_level=19&os_id=08d40ce27ef36489&resolution=720_1280&dpi=240&client_ip=192.168.10.148&pdunid=ce27ef3648908d40'
    response = requests.get(url, headers=headers)
    data = response.text
    data = json.loads(data)['list']
    print(data)
    count = len(data)
    for item in data:
        detail_id = item['detail_id']
        module_type = item['module_type']
        title = item['title']
        description = item['description']
        cover = item['cover']
        thumb_img = item['thumb_img']
        video_url = item['video_url']
        is_top = item['is_top']
        ctime = item['ctime']
        tags_id = item['tags_id']
        tags_name = item['tags_name']
        keyword_id = item['keyword_id']
        keyword_name = item['keyword_name']
        show_type = item['show_type']
        show_tags_type = item['show_tags_type']
        source = item['source']
        source_type = item['source_type']
        print('detail_id:',detail_id)
        print('module_type:',module_type )
        print('title:', title)
        print('description:',description)
        print('cover:', cover)
        print('thumb_img:',thumb_img)
        print('video_url:',video_url)
        print('is_top:',is_top)
        print('ctime:',ctime)
        print('tags_id:',tags_id)
        print('tags_name:',tags_name)
        print('keyword_id:',keyword_id)
        print('keyword_name:',keyword_name)
        print('show_type:',show_type)
        print('show_tags_type:',show_tags_type)
        print('source:',source)
        print('source_type:',source_type)
        print('='*60)







