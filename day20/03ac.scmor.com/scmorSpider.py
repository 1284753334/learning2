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
'''

执行本地 js 文件


google  把方法保存到本地，调用该方法 获取结果
'''
import requests
import execjs
import re


import os

#os.environ["EXECJS_RUNTIME"] = "PhantomJS"
node = execjs.get()
print(execjs.get().name)
file = './encrypt.js'
#  读取本地的js 文件
ctx = node.compile(open(file,'r',encoding='utf-8').read())

url = 'http://ac.scmor.com/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
}
response = requests.get(url=url, headers=headers)
html = response.content.decode(response.apparent_encoding)
#print(html)
pat_1 = re.compile(r'autourl.*?"(.*?)"')
ls = pat_1.findall(html)
print('len:',len(ls))
for item in ls:
    #print(item)
    #  直接调用解码函数即可
    href = ctx.call('strdecode',item)
    print(href)
