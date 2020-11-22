'''

视频下载

找到链接（复制到浏览器 可以打开 视频 那种  像 下载图片 一样  保存到  本地即可  ）

不足：  不带 进度条  不知道 什么时候结束



'''
import random
import time

'''
import  requests

headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
}

response = requests.get('https://vd3.bdstatic.com/mda-kihp0vhaysuduhi0/v1-cae/1080p/mda-kihp0vhaysuduhi0.mp4?auth_key=1603508800-0-0-ebda1693f0ba6c58ac0c50303d43feb4&bcevod_channel=searchbox_feed&pd=1&pt=3&abtest=8790_3',headers = headers)
with open('./viedo/老爸老妈.mp4', 'wb') as f:
    # content 里面为字节数据

    f.write(response.content)
    print('ok')


#  以流的形式下载，，stream =  True
# import  requests
# 
# 
# def  download(url,path):
#     # r = requests.get(url,stream =  True)
#     with requests.get(url,stream =  True) as r:
#         chunk_size = 1024
#         print('开始下载')
#         with open('path','wb') as f:
#             for chunk in r.iter_content(chunk_size= chunk_size):
#                 f.write(chunk)
#         print('下载结束')
# 
# if __name__ == '__main__':
#     url = ''
#     path = ''
#     download(url,path)


'''


# import  requests
#
#
# def  download(url,path):
#     # r = requests.get(url)
#     with requests.get(url) as r:
#         chunk_size = 1024
#         print('开始下载')
#         with open('path','wb') as f:
#             for chunk in r.iter_content(chunk_size= chunk_size):
#                 f.write(chunk)
#         print('下载结束')
#
# if __name__ == '__main__':
#     url = ''
#     path = ''
#     download(url,path)


''''
带进度 的 下载



需要知道 请求的 资源大小  以及 下载了 多少 
content_lenght


'''

import  requests


def  download(url,path,headers):
    # r = requests.get(url,stream =  True,headers = headers)
    with requests.get(url,stream =  True,headers = headers) as r:
        # time.sleep(random.random())
        chunk_size = 1024
        #  获取下载的 大小
        content_size = int(r.headers['content-length'])
        print('开始下载')
        #  是  path  不是 字符串 path
        with open(path,'wb') as f:
            n = 1
            for chunk in r.iter_content(chunk_size= chunk_size):
                loaded = n * 1024/ content_size
                f.write(chunk)
                n += 1
                loaded_rated = round(loaded*100,2)
                # print(f'已经下载{loaded_rated}%')
                # 避免同名   比如 f  （上文中 已经出现了，下文 不能使用 ）
                print('已经下载{0:}'.format(loaded_rated))
                # time.sleep(1)

        print('下载结束')

if __name__ == '__main__':
    headers = {

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
    }
    url = 'https://vd2.bdstatic.com/mda-kjfe7yg5i05ukxin/v1-cae/sc/mda-kjfe7yg5i05ukxin.mp4?auth_key=1603512026-0-0-d3a0433146f2dd9a25b07df724fa5ac9&bcevod_channel=searchbox_feed&pd=1&pt=3&abtest=8790_3'
    path = './viedo/酒醉的蝴蝶.mp4'
    download(url,path,headers)




