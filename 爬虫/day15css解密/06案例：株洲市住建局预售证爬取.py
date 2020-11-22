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

1.查看网页，查找相应的标签，发现和普通的不一样，它没有 url,
    前面有有个 Onview，点击搜索，发现这是一个函数，


    它前后台采用的是 Ajax  技术，即 查看请求头信息，，提交方式为 post,
    查看 response  相应信息为 一个字典
    {"total":4964,"rows":"[{\"bid\":\"20201318573\",\"cdno\":\"预许字(2020)第530号\",\"fpath\":\"/EIIMSWeb/CoreAttachUpload?nid=1037199789\",\"lname\":\"石峰区迎宾大道99号恒大誉苑9栋商业公寓\",\"pid\":\"100001088756\",\"pname\":\"恒大誉苑\"},{\"bid\":\"20201315760\",\"cdno\":\"预许字(2020)第529号\",\"fpath\":\"/EIIMSWeb/CoreAttachUpload?nid=1037198375\",\"lname\":\"芦淞区服饰大道99号锦湘悦16栋\",\"pid\":\"100001172307\",\"pname\":\"锦湘悦\"},{\"bid\":\"20201318585\",\"cdno\":\"预许字(2020)第528号\",\"fpath\":\"/EIIMSWeb/CoreAttachUpload?nid=1037198373\",\"lname\":\"天元区栗合路1515号恒大悦珑台16栋\",\"pid\":\"100000996039\",\"pname\":\"恒大悦珑台\"},{\"bid\":\"20201314629\",\"cdno\":\"预许字(2020)第527号\",\"fpath\":\"/EIIMSWeb/CoreAttachUpload?nid=1037195943\",\"lname\":\"芦淞区沿江南路688号世贸枫溪壹号B16栋\",\"pid\":\"100000995137\",\"pname\":\"世贸枫溪壹号\"},{\"bid\":\"20201315203\",\"cdno\":\"预许字(2020)第526号\",\"fpath\":\"/EIIMSWeb/CoreAttachUpload?nid=1037195939\",\"lname\":\"芦淞区沿江南路688号世贸枫溪壹号B10栋\",\"pid\":\"100000995137\",\"pname\":\"世贸枫溪壹号\"},{\"bid\":\"20201309872\",\"cdno\":\"预许字(2020)第525号\",\"fpath\":\"/EIIMSWeb/CoreAttachUpload?nid=1037192919\",\"lname\":\"天元区衡山西路480号圣桦锦悦府6栋\",\"pid\":\"100001292874\",\"pname\":\"圣桦锦悦府\"},{\"bid\":\"20201309501\",\"cdno\":\"预许字(2020)第524号\",\"fpath\":\"/EIIMSWeb/CoreAttachUpload?nid=1037192917\",\"lname\":\"天元区衡山西路480号圣桦锦悦府4栋\",\"pid\":\"100001292874\",\"pname\":\"圣桦锦悦府\"},{\"bid\":\"20201306176\",\"cdno\":\"预许字(2020)第523号\",\"fpath\":\"/EIIMSWeb/CoreAttachUpload?nid=1037191605\",\"lname\":\"石峰区藏龙路1129号时代馨园18栋\",\"pid\":\"100001339742\",\"pname\":\"时代馨园\"},{\"bid\":\"20201306254\",\"cdno\":\"预许字(2020)第522号\",\"fpath\":\"/EIIMSWeb/CoreAttachUpload?nid=1037191603\",\"lname\":\"石峰区藏龙路1129号时代馨园16栋\",\"pid\":\"100001339742\",\"pname\":\"时代馨园\"},{\"bid\":\"20201306165\",\"cdno\":\"预许字(2020)第521号\",\"fpath\":\"/EIIMSWeb/CoreAttachUpload?nid=1037191599\",\"lname\":\"石峰区藏龙路1129号时代馨园12栋\",\"pid\":\"100001339742\",\"pname\":\"时代馨园\"},{\"bid\":\"20201306155\",\"cdno\":\"预许字(2020)第520号\",\"fpath\":\"/EIIMSWeb/CoreAttachUpload?nid=1037191595\",\"lname\":\"石峰区藏龙路1129号时代馨园11栋\",\"pid\":\"100001339742\",\"pname\":\"时代馨园\"},{\"bid\":\"20201306154\",\"cdno\":\"预许字(2020)第519号\",\"fpath\":\"/EIIMSWeb/CoreAttachUpload?nid=1037191591\",\"lname\":\"石峰区藏龙路1129号时代馨园10栋\",\"pid\":\"100001339742\",\"pname\":\"时代馨园\"},{\"bid\":\"20201306249\",\"cdno\":\"预许字(2020)第518号\",\"fpath\":\"/EIIMSWeb/CoreAttachUpload?nid=1037191589\",\"lname\":\"石峰区藏龙路1129号时代馨园9栋\",\"pid\":\"100001339742\",\"pname\":\"时代馨园\"},{\"bid\":\"20201306242\",\"cdno\":\"预许字(2020)第517号\",\"fpath\":\"/EIIMSWeb/CoreAttachUpload?nid=1037191587\",\"lname\":\"石峰区藏龙路1129号时代馨园7栋\",\"pid\":\"100001339742\",\"pname\":\"时代馨园\"},{\"bid\":\"20201306239\",\"cdno\":\"预许字(2020)第516号\",\"fpath\":\"/EIIMSWeb/CoreAttachUpload?nid=1037191585\",\"lname\":\"石峰区藏龙路1129号时代馨园6栋\",\"pid\":\"100001339742\",\"pname\":\"时代馨园\"}]","success":true,"message":""}
    通过分析下面的  ajax  过程，

    通过断点 调试

    能够分析出 它的 url  等一些详细信息




'''
import requests
import json
import random
import time
#http://zjj.zhuzhou.gov.cn/c13948/
# url  信息 在 request 里面可以看到
url = 'http://zjj.zhuzhou.gov.cn/fcjadpater/select/WWW_YSXK_002'
head = {}
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
# 前缀怎么分析出来的
# PIC_SERVER_PREFIX = "http://218.75.204.3:5636"
# 通过分析 它是空，通过抓包 分析为 首页 地址，这可能是另一种反爬手段吧
PIC_SERVER_PREFIX = "http://zjj.zhuzhou.gov.cn"
# 抓包工具
# PIC_SERVER_PREFIX = ""

for page in range(1,10):
    print('page:',page)
    params = {
        'pageIndex': page,
        'pageSize': 15
    }
    response = requests.post(url,headers=head,params=params)
    data = json.loads(response.json()['rows'])
    print(len(data))

    for item in data:
        bid = item['bid']
        cdno = item['cdno']
        fpath = item['fpath']
        lname = item['lname']
        pid = item['pid']
        pname = item['pname']
        img_url = PIC_SERVER_PREFIX + fpath
        print('bid:',bid)
        print('cdno:', cdno)
        print('fpath:', fpath)
        print('lname:', lname)
        print('pid:', pid)
        print('pname:', pname)
        print('img_url:', img_url)
        print('='*60)

        img = requests.get(img_url,headers=head).content
        img_path = './images/ysz/' + cdno + '.jpg'
        with open(img_path,'ab+') as file:
            file.write(img)
    time.sleep(random.random())
