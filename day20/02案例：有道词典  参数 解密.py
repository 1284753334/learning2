"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/8/9'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
'''

异步加载的 参数 ，需要 点击xhr,才能找到  相关的form data  参数  
通过在js文件中查找salt或者sign，可以找到
1.可以找到这个计算salt的公式
r = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10))
2.sign：n.md5("fanyideskweb" + t + r + "ebSeFb%=XZ%T[KZ)c(sy!");
md5 一共需要四个参数，第一个和第四个都是固定值得字符串，第三个是所谓的salt，
第二个参数是输入的需要翻译的单词

#   隐藏  动态生成的参数，一定都在js 里面，去 network 里面  查找，相关的键  即可 

调试 很 重要的  ，看清 数据的 走向，流程  
md5  加密 补充 
import hashlib
m = hashlib.md5()
m.update(b'123')
#  返回的是 MD5  对象
print(m)
# hexdigest()  转换成 十六进制的   字符串
print( m.hexdigest())
print(type( m.hexdigest()))
'''

import requests
import time
import random
import hashlib


def translate(content):
    #  比之前多了 参数 _o....
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    # 定义变量
    client = 'fanyideskweb'
    # js  时间戳和python  不太一样
    ctime = int(time.time() * 1000)
    salt = str(ctime + random.randint(1, 10))
    # key = 'rY0D^0\'nM0}g5Mm1z%1G4' 以前版本的秘钥
    key = 'n%A-rKaT5fb[Gy?;N5@Tj'
    sign = hashlib.md5((client + content + salt + key).encode('utf-8')).hexdigest()
    # 表单数据
    data = {}
    data['i'] = content
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = salt
    data['sign'] = sign
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_CL1CKBUTTON'
    data['typoResult'] = 'false'
    # 请求头
    head = {}
    head['Accept'] = 'application/json, text/javascript, */*; q=0.01'
    head['Accept-Encoding'] = 'gzip, deflate'
    head['Accept-Language'] = 'zh-CN,zh;q=0.9'
    head['Connection'] = 'keep-alive'
    head['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
    head['Cookie'] = 'OUTFOX_SEARCH_USER_ID_NCOO=484463584.8730025; OUTFOX_SEARCH_USER_ID="1241098497@10.168.11.144"; _ntes_nnid=bdb421e91d94536323866818f8c43d2c,1549875439929; P_INFO=jtbl_2000; JSESSIONID=aaaUAotyYk_2earuSp1Xw; ___rl__test__cookies=' + str(ctime)
    head['Host'] = 'fanyi.youdao.com'
    head['Origin'] = 'http://fanyi.youdao.com'
    head['Referer'] = 'http://fanyi.youdao.com/'
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    head['X-Requested-With'] = 'XMLHttpRequest'
    response = requests.post(url, data=data, headers=head)
    target = response.json()
    print(target)
    result = target['translateResult'][0][0]['tgt']

    return result


content = input('请输入需要翻译的内容：')
print('%s对应的中文为：'%content,translate(content))


