'''
图片下载：

简单的来说：
获取的图片格式结尾的 网址的内容  比如  .jpg

response.content

权限 设置为  'wb'

然后 保存到指定的文件夹即可

换名字，，等其他操作
'''

import  requests

headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
}

response = requests.get('http://c1.haibao.cn/img/600_0_100_1/1549794487.7856/fa60e1e7264e6082569d729e4ee302dd.jpg',headers = headers)
with open('../img/3.jpg', 'wb') as f:
    # content 里面为字节数据

    f.write(response.content)
    print('ok')



# print(response.content.decode('utf-8'))
# # print(response.text)
# print(response.url)
# print(1+4)