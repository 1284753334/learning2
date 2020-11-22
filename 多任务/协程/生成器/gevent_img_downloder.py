# import urllib.request
#
#
# def main():
#     req =  urllib.request.urlopen('https://rpic.douyucdn.cn/live-cover/roomCover/2020/07/22/c27d0aa219f1f073dc1f239fffd5f927_big.jpg/webpdy1')
#     img_content = req.read()
#
#     with open('2.png','wb') as f:
#         f.write(img_content)
#
# if __name__ == '__main__':
#     main()
import gevent
import requests
# https://rpic.douyucdn.cn/live-cover/roomCover/2020/07/20/53a0ae3b49adbdc0c5bb0f1c792ee121_big.png/webpdy1
# https://pics4.baidu.com/feed/6609c93d70cf3bc7d1d87bb461dd85a6cf112af6.jpeg?token=97d5fb05990389b5022e87f0e397c734
#
# url = 'http://contentcms-bj.cdn.bcebos.com/cmspic/65c56c362615fdcbbbb521748aa97e28.jpeg?x-bce-process=image/crop,x_0,y_0,w_899,h_489'
# r = requests.get(url=url)
#
# with open('bd_logo3.png', 'wb') as f:
#     f.write(r.content)
#     print('OK')


def download(name,url):
    print('GET:%s' %url)
    resp = requests.get(url=url)
    data = resp.content
    print('%d bytes receieved from %s.'%(len(data),url))

    with open(name, 'wb') as f:
        f.write(data)
        print('OK')


def main():
    gevent.joinall([
        gevent.spawn(download,'1.jpg','http://contentcms-bj.cdn.bcebos.com/cmspic/65c56c362615fdcbbbb521748aa97e28.jpeg?x-bce-process=image/crop,x_0,y_0,w_899,h_489'),
        gevent.spawn(download,'2.jpg','https://pics4.baidu.com/feed/6609c93d70cf3bc7d1d87bb461dd85a6cf112af6.jpeg?token=97d5fb05990389b5022e87f0e397c734'),
    ])


if __name__ == '__main__':
    main()