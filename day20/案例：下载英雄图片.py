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

headers = {'User-Agent':'Dalvik/1.6.0 (Linux; U; Android 4.4.2; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10)'}
url = 'http://gamehelper.gm825.com/wzry/hero/list?channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=13.0.1.0&version_code=13010&cuid=C8B595533A5E4F03B5B2A3839EFF8A1B&ovr=4.4.2&device=HUAWEI+_HUAWEI+MLA-AL10&net_type=1&client_id=9tcu5xhbpYYN6sxHKeVMcA%3D%3D&info_ms=5mYJrrjSbSut9IK6BQNriw%3D%3D&info_ma=3q8SJYmLxl%2Fiv0Am%2FAiHae0xlIUVwrhC3mS0zlXjskA%3D&mno=0&info_la=xIYTbOcOjEd%2FTFTutRfK8Q%3D%3D&info_ci=xIYTbOcOjEd%2FTFTutRfK8Q%3D%3D&mcc=0&clientversion=13.0.1.0&bssid=3q8SJYmLxl%2Fiv0Am%2FAiHae0xlIUVwrhC3mS0zlXjskA%3D&os_level=19&os_id=08d40ce27ef36489&resolution=720_1280&dpi=240&client_ip=192.168.10.148&pdunid=ce27ef3648908d40'
response = requests.get(url,headers=headers)
data = response.text
print(data)
data = json.loads(data)['list']
for item in data:
    cover = item['cover']
    hero_id = item['hero_id']
    name = item['name']
    tags=item['tags']
    type = item['type']
    print('cover:',cover)
    print('hero_id:',hero_id)
    print('name:',name)
    print('tags:',tags)
    print('type:',type)
    print('='*60)
    #   保存图片
    content = requests.get(cover,headers=headers).content
    filename = cover.split('/')[-1]
    # filename = str(name).png
    with open('./images/12/'+filename,'wb') as file:
        file.write(content)
