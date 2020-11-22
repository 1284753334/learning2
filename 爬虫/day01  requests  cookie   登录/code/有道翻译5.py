'''
F12  开发工具的使用:

 network  查看请求和响应的内容
     预览
     没有 刷新页面 会 显示 内容   使用的是  AJAX 技术






 element: 查看 网页源码

console:  输出信息


'''

#   表单的使用

# import  requests
#
# params = {
#
# }
#
# headers = {
#
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
# }
#
# response = requests.get('http://fanyi.youdao.com/',headers = headers)
'''
能翻译出来结果，一年后都不用维护都可以 
没啥，，稀松平常

post  请求

比着 pc网页多个参数 ：  "client":"fanyideskweb",
'''
#
import requests
if __name__ == "__main__":
    #对应上图的Request URL
    #Request_URL = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    Request_URL = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    #创建Form_Data字典，存储上图的Form Data
    #  不能再采用键值对的方式 往里面传值，会报错，意义不同吧
    Form_Data = {
      "i":"你好",
      "from": "AUTO",
      "to":"AUTO",
      "smartresult":"dict",
      "client":"fanyideskweb",
      "salt":"16034325943302",
      "sign":"6ffec6aa38a207188b9c2c0f6d867901",
      "ts":"1603432594330",
      "bv":"9ef72dd6d1b2c04a72be6b706029503a",
      "client":"fanyideskweb",
      'doctype': 'json',
      "version":"2.1",
      'keyfrom':'fanyi.web',
      'action': 'FY_BY_CLICKBUTTION',
      'typoResult':"false"

    }
    # Form_Data['i'] = 'tree'
    # Form_Data['from'] = 'AUTO'
    # Form_Data['to'] = 'AUTO'
    # Form_Data['smartresult'] = 'dict'
    # Form_Data['client'] = 'fanyideskweb'
    # Form_Data['salt'] = '1526796477689'
    # Form_Data['sign'] = 'd0a17aa2a8b0bb831769bd9ce27d28bd'
    # Form_Data['doctype'] = 'json'
    # Form_Data['version'] = '2.1'
    # Form_Data['keyfrom'] = 'fanyi.web'
    # Form_Data['action'] = 'FY_BY_REALTIME'
    # Form_Data['typoResult'] = 'false'
    head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    #写入User Agent信息
    # head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    #   post  请求
    response = requests.post(Request_URL, data=Form_Data,headers=head)
    print(Form_Data)
    print(response)
    # print(response.text)
    print(type(response))
    translate_results = response.json()
    # #找到翻译结果
    translate_results = translate_results['translateResult'][0][0]['tgt']
    # #打印翻译信息
    print("翻译的结果是：%s" % translate_results)

# import requests
# import json
# import pprint
# head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
#
# form_data={"i":"Computer",
#       "from":"AUTO",
#       "to":"AUTO",
#       "smartresult":"dict",
#       "client":"fanyideskweb",
#       "salt":"15674273328128",
#       "sign":"ea0289bbe84561c958aa9a6a4d9b9bdc",
#       "ts":"1567427332812",
#       "bv":"a4f4c82afd8bdba188e568d101be3f53",
#       "client":"fanyideskweb",
#       'doctype': 'json',
#       "version":"2.1",
#       'keyfrom':'fanyi.web',
#       'action': 'FY_BY_CLICKBUTTION',
#       'typoResult':"false"
#       }
#
# reponse=requests.post(url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule",data=form_data,timeout=0.5,headers=head)
# print(reponse.content.decode(reponse.apparent_encoding),type(reponse.content.decode(reponse.apparent_encoding)))
# dd=reponse.content.decode(reponse.apparent_encoding)
# gg=reponse.json()
# print(gg["translateResult"][0][0]["tgt"],gg)


