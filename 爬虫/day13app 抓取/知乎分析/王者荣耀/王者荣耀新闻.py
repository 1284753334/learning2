
import requests,json

'''
热点
'''


url ='http://gamehelper.gm825.com/wzry/hot/information'
# url ='http://gamehelper.gm825.com/wzry/news/list'

page = 1
headers = {
'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; MI 6 Build/NMF26X)'
}

for page in range(1,10):
    params = {
        'pn':page,
        'channel_id':'90009a',
        'app_id':'h9044j',
        'game_id':7622,
        'game_name':'王者荣耀',
        'vcode':'13.0.1.0',
        'version_code':13010,
        'cuid':'44C3690762340774AF1D756FCF34D366',
        'ovr':'5.1.1',
        'device':'Xiaomi_MI 6',
        'net_type':1,
        'client_id':'qnBmQaRbJAMjU156zvFhGg==',
        'info_ms':'BoQNGP4oiZNOWbfiRN9Swg==',
        'info_ma':'9Sd6B3yFa6H+rHMXokRBPcq6E6VtiMQOSOlR1rkPfm0=',
        'mno':'0',
        'info_la':'FAsrk6drpuYLlcCG3Se3lQ==',
        'info_ci':'FAsrk6drpuYLlcCG3Se3lQ==',
        'mcc':0,
        'clientversion':'13.0.1.0',
        'bssid':'P8uGiTbIO5ybiSlLCZMYHypHQYJHAUvaqhJd6MFHkuM=',
        'os_level':22,
        'os_id':'3c970ee709c44800',
        'resolution':900_1600,
        'dpi':320,
        'client_ip':'192.168.43.253',
        '192.168.43.253':'ee709c448003c970',

    }
    page +=1

    data = requests.get(url,headers=headers,params=params,verify=False).text

    html = json.loads(data)['news_list']
    print(html)
    print(type(html))


    i = 0
    for each in html:
        # name = each
        name = each['title'].strip()
        print('name:',name)
        desc = each['description']
        print('desc:',desc)
        title = each['cover']
        print('cover:',title)
        i +=1
        print('count:',i)
    # cover = each['t']
    # key_word = html['keyword_name']
    # print('kw:',key_word)








