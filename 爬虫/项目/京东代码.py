#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2020/11/11 8:00:32

@author: Json

        认真大胆      永无BUG
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/7 11:17
# @Author  : dddchongya
# @Site    :
# @File    : ComputerFromJD.py
# @Software: PyCharm
import requests
from bs4 import BeautifulSoup as bst
import json
import os
informationnumber=0
def GetComment(id):
    param = {
        'callback': 'fetchJSON_comment98',
        'productId': id,
        'score': 0,
        'sortType': 5,
        'page': 1,
        'pageSize': 10,
        'isShadowSku': 0,
        'rid': 0,
        'fold': 1,
    }
    url="https://club.jd.com/comment/productPageComments.action"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        # 标记了请求从什么设备，什么浏览器上发出
    }
    CommentLs={}
    bool=1
    label=[]
    comments=[]
    commentnumber={}
    for i in range(1,5):
        param["page"]=i
        res_songs = requests.get(url, params=param, headers=headers)
        jsondata = res_songs.text
        jsondata = json.loads(jsondata.replace("(", "").replace(")", "").replace("fetchJSON_comment98", "").replace(" ","").replace(";", ""))
        if bool ==1 :
            # 标签只用拿一次
            hotCommentTagStatistics=jsondata["hotCommentTagStatistics"]
            for j in hotCommentTagStatistics:
                label.append(j["name"]+":"+str(j["count"]))
            # 评论数量也只用拿一次
            productCommentSummary = jsondata["productCommentSummary"]
            commentnumber["commentCount"]=productCommentSummary["commentCount"]
            commentnumber["defaultGoodCount"] = productCommentSummary["defaultGoodCount"]
            commentnumber["goodCount"] = productCommentSummary["goodCount"]
            commentnumber["poorCount"] = productCommentSummary["poorCount"]
            commentnumber["generalCount"] = productCommentSummary["generalCount"]
            commentnumber["afterCountStr"] = productCommentSummary["afterCount"]
            commentnumber["showCount"] = productCommentSummary["showCount"]
            bool=bool+1

        comment=jsondata["comments"]
        for j in comment:
            comments.append(j["content"].replace("\n",""))
    CommentLs["commentnumber"]=commentnumber
    CommentLs["label"]=label
    CommentLs["comments"]=comments
    return CommentLs


def GetMoreInformation(id):
    url="https://item.jd.com/"+id+".html"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        # 标记了请求从什么设备，什么浏览器上发出
    }
    res= requests.get(url, headers=headers)
    html=bst(res.content)

def GetGoodResone(LsComputer):
        labells = []
        label = set()
        labellist = {}
        for i in LsComputer:
            if (i['comments']['commentnumber']['goodCount'] + i['comments']['commentnumber'][
                'defaultGoodCount']) / float(i['comments']['commentnumber']['commentCount']) > 0.7:
                labells.append(i['comments']["label"])
        for i in labells:
            for j in i:
                label.add(j.split(":")[0])
        for i in label:
            labellist[i] = 0
        for j in labells:
            for k in j:
                labellist[k.split(":")[0]] = labellist[k.split(":")[0]] + float(k.split(":")[1])
        result = sorted(labellist.items(), key=lambda x: x[1], reverse=False)
        with open(os.getcwd() + '\好评过七十的标签排行.txt', 'w', encoding="utf-8") as f:
            for i in result:
                f.write(str(i))
                f.write('\r\n')
        f.close()

def GetMaxSalesShop(LsComputer):
    shop=set()
    for i in LsComputer:
        shop.add(i["ShopName"])
    shopcount={}
    shopsalecount={}
    shopprice={}
    for i in shop:
        shopcount[i]=0
        shopsalecount[i]=0
        shopprice[i] = []
    for i in shop:
        for j in LsComputer:
            if j["ShopName"]==i:
                if j["Price"].__len__()>=5:
                    price=j["Price"][0:-3].replace("\n","").replace(" ","").replace("\t","")
                    # 销售额
                    shopcount[i]=shopcount[i]+j["comments"]["commentnumber"]["commentCount"]*float(price)
                    #价格总和，为了求平均数
                    shopprice[i].append(price)
                    # 销售量
                    shopsalecount[i]=shopsalecount[i]+j["comments"]["commentnumber"]["commentCount"]
    shopprice2={}
    for i in shopprice:
        sum=0
        if shopprice[i].__len__() != 0:
            for j in shopprice[i]:
                sum=sum+float(j)
            price=sum/(shopprice[i].__len__())
            shopprice2[i]=price

    print()
    print()
    result=sorted(shopcount.items(), key=lambda x: x[1], reverse=False)
    print("销售额排行::")
    for i in result:
        print(i)
    with open(os.getcwd() + '\销售额排行.txt', 'w', encoding="utf-8") as f:
        for i in result:
            f.write(str(i))
            f.write('\r\n')
    f.close()

    print()
    print()
    result = sorted(shopprice2.items(), key=lambda x: x[1], reverse=False)
    print("销售量排行::")
    for i in result:
        print(i)
    with open(os.getcwd() + '\销售量排行.txt', 'w', encoding="utf-8") as f:
        for i in result:
            f.write(str(i))
            f.write('\r\n')
    f.close()

    print()
    print()
    result = sorted(shopsalecount.items(), key=lambda x: x[1], reverse=False)
    print("平均价格排行::")
    for i in result:
        print(i)
    with open(os.getcwd() + '\平均价格排行.txt', 'w', encoding="utf-8") as f:
        for i in result:
            f.write(str(i))
            f.write('\r\n')
    f.close()

# 可任意写搜索链接
url = 'https://search.jd.com/Search?keyword=%E7%94%B5%E8%84%91&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E7%94%B5%E8%84%91&page='
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
      # 标记了请求从什么设备，什么浏览器上发出
    }
# 伪装请求头
LsComputer=[]
#bool=1    # 每页开头第一个商品格式有误差，所以以此为判断符号跳过第一个
for k in range(1,10):
    url=url+str(k*2+1)
    res= requests.get(url, headers=headers)
    html=bst(res.content)
    list=html.findAll("li",{"class","gl-item gl-item-presell"})
    for html in list:
        ComputerInformation={}
        CustomUrl=html.find("div",{"class","p-img"}).find("a").get("href")
        if not str(CustomUrl).__contains__("https:"):
            CustomUrl="https:"+CustomUrl
      #  print(CustomUrl)
        id=html.find("div",{"class","p-price"}).find("strong").get("class")
        id=id[0].replace("J","").replace("_","")
        # 拿到评论信息
        Comments=GetComment(id)
        #print(Comment)

        #进入页面拿更详细的信息

        ImgUrl="https:"+str(html.find("div",{"class","p-img"}).find("img").get("source-data-lazy-img"))
      #  print(ImgUrl)

        Price=str(html.find("div",{"class","p-price"}).find("i"))[3:-4]
      #  print(Price[3:-4])

        Describe=str(html.find("div",{"class","p-name p-name-type-2"}).find("em").getText())
      #  print(Describe)

        #第一行一个会为空
        ShopName=html.find("div",{"class","p-shop"}).find("a")
        if ShopName != None:
            ShopName=str(ShopName.getText())

        # print(ShopName)
        # 店铺描述可能有多个
        Mode=html.find("div",{"class","p-icons"}).findAll("i")
        BusinessMode=[]
        for i in Mode:
            BusinessMode.append(i.getText())
      #  print(BusinessMode)

        ComputerInformation["CustomUrl"]=CustomUrl
        ComputerInformation["ImgUrl"] = ImgUrl
        ComputerInformation["Price"] = Price
        ComputerInformation["Describe"] = Describe
        ComputerInformation["ShopName"] = ShopName
        ComputerInformation["CustomUrl"] = CustomUrl
        ComputerInformation["BusinessMode"] = BusinessMode
        ComputerInformation["comments"]=Comments
        LsComputer.append(ComputerInformation)


for k in range(1,10):
    url=url+str(k*2+1)
    res= requests.get(url, headers=headers)
    html=bst(res.content)
    list=html.findAll("li",{"class","gl-item"})
    for html in list:
        ComputerInformation={}
        CustomUrl=html.find("div",{"class","p-img"}).find("a").get("href")
        if not str(CustomUrl).__contains__("https:"):
            CustomUrl="https:"+CustomUrl
      #  print(CustomUrl)
        id=html.find("div",{"class","p-price"}).find("strong").get("class")
        id=id[0].replace("J","").replace("_","")
        # 拿到评论信息
        Comments=GetComment(id)
        #print(Comment)

        #进入页面拿更详细的信息

        ImgUrl="https:"+str(html.find("div",{"class","p-img"}).find("img").get("source-data-lazy-img"))
      #  print(ImgUrl)

        Price=str(html.find("div",{"class","p-price"}).find("i"))[3:-4]
      #  print(Price[3:-4])

        Describe=str(html.find("div",{"class","p-name p-name-type-2"}).find("em").getText())
      #  print(Describe)

        #第一行一个会为空
        ShopName=html.find("div",{"class","p-shop"}).find("a")
        if ShopName != None:
            ShopName=str(ShopName.getText())
       # print(ShopName)
        # 店铺描述可能有多个
        Mode=html.find("div",{"class","p-icons"}).findAll("i")
        BusinessMode=[]
        for i in Mode:
            BusinessMode.append(i.getText())
      #  print(BusinessMode)

        ComputerInformation["CustomUrl"]=CustomUrl
        ComputerInformation["ImgUrl"] = ImgUrl
        ComputerInformation["Price"] = Price
        ComputerInformation["Describe"] = Describe
        ComputerInformation["ShopName"] = ShopName
        ComputerInformation["CustomUrl"] = CustomUrl
        ComputerInformation["BusinessMode"] = BusinessMode
        ComputerInformation["comments"]=Comments
        LsComputer.append(ComputerInformation)

#数据写入文件
with open(os.getcwd() + '\json.txt', 'w',encoding="utf-8") as f:
    for i in LsComputer:
        f.write(json.dumps(i,indent=4,ensure_ascii=False))
f.close()

GetMaxSalesShop(LsComputer)