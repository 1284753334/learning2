"""
模拟简单的博客
1.账号注册，登陆验证


2.写文章，包含【标题，作者，时间，内容】
3.查询文章，列出所有文章及时间
4.可查看其中一篇文章
5.删除文章
6.修改文章
7.退出系统（sys.exit()）
"""
import os,json,time,sys

# #用户配置表结构
# userDictTable = {"users":[{"name":"admin","pwd":"123456"}]}
# print(userDictTable)
# print(userDictTable["users"])
# userDictTable["users"].append({"name":"张三","pwd":"654321"})
# print(userDictTable)

#读取用户配置表
def readAllUser(path="user.json"):
    if os.path.exists(path):
        #文件路径存在
        with open(path) as f_r:
            #  读出信息
            return json.load(f_r)
    else:
        with open(path,"w") as f_w:
            userDictTable = {"users": [{"name": "admin", "pwd": "123456"}]}
            json.dump(userDictTable,f_w)
            return userDictTable#返回默认用户信息

# readAllUser("user.json")

#更新用户数据表:覆盖写入
def updateUser(userDict,path="user.json"):
    with open(path,"w") as f_w:
        json.dump(userDict,f_w)
        print("用户数据更新成功！")

# updateUser({"users": [{"name": "admin", "pwd": "123456"}]},path="user.json")

#默认文章
def createDefaultArticle(name,path="Article"):
    if os.path.exists(path):
        with open(os.path.join(path,name+".json"),"w") as f_w:
            articleTable = {"article": [{
                "title": "default title",
                "author": name,
                "time": time.strftime("%Y-%m-%d"),
                "content": "default content"
            }]}
            json.dump(articleTable,f_w)
            print("创建默认文章成功！")
    else:
        #创建文件夹存储文章
        os.mkdir(path)
        with open(os.path.join(path,name+".json"),"w") as f_w:
            articleTable = {"article": [{
                "title": "default title",
                "author": name,
                "time": time.strftime("%Y-%m-%d"),
                "content": "default content"
            }]}
            json.dump(articleTable,f_w)
            print("创建默认文章成功！")

# createDefaultArticle("王二麻子","Article")

#注册 ：1.用户存在 --》失败 2.不存在：注册
def register(path="user.json"):
    while True:
        name = input("请输入用户名：")
        pwd = input("请输入密码：")
        temp = readAllUser(path)
        #print(temp)
        isFind = False#默认用户不存在
        for i in temp["users"]:
            if i["name"] == name:
                #用户存在
                print("用户存在，请重新注册！")
                isFind = True
                break
        if isFind == False:
            #注册
            curUser = {"name":name,"pwd":pwd}
            temp = readAllUser(path)
            print("***",temp)
            temp["users"].append(curUser)
            updateUser(temp,path)
            print("注册成功！")
            createDefaultArticle(name)
            return True

# register("user.json")

#登录：1.用户名和密码--》成功 2.失败
def login(path="user.json"):
    global currentUser
    while True:
        name = input("请输入账号：")
        pwd = input("请输入密码：")
        temp = readAllUser(path)
        isFind = False
        for i in temp["users"]:
            if i["name"] == name and i["pwd"] ==pwd:
                print("登陆成功！")
                currentUser = name
                isFind = True
                return isFind
        if isFind == False:
            print("用户名或密码输入有误，请重新输入！")

# login("user.json")

#2.写文章，包含【标题，作者，时间，内容】
# articleTable = {"article":[{
#     "title":"default title",
#     "author":"author",
#     "time":time.strftime("%Y-%m-%d"),
#     "content":"default content"
# }]}

#读文章
def readArticle(name,path="Article"):
    with open(os.path.join(path,name+".json")) as f_r:
        # 默认是读的模式   返回读取的内容
        return json.load(f_r)

# x= readArticle("王二麻子","Article")
# print(x)

#更新文章
def updateArticle(name,allArticle,path="Article"):
    """
    :param name:
    :param allArticle: 所有文章
    :param path:
    :return:
    """
    with open(os.path.join(path,name+".json"),"w") as f_w:
        json.dump(allArticle,f_w)
        print("更新文章成功！")


#写文章
def writeArticle(name,path="Article"):
    print("开始写文章了！！！")
    title = input("请输入文章标题：")
    content  = input("请输入文章内容：")
    articleDict = {
        "title": title,
        "author": name,
        "time": time.strftime("%Y-%m-%d"),
        "content": content
    }
    allArticle = readArticle(name,path)
    allArticle["article"].append(articleDict)

    #更新
    updateArticle(name,allArticle,path)


# writeArticle("王二麻子")

#3.查询文章，列出所有文章及时间
def findAll(name,path="Article"):
    allArticle = readArticle(name,path)
    for i in range(len(allArticle["article"])):
        print(allArticle["article"])
        print(i+1,"标题是：%s,时间是：%s"%(allArticle["article"][i]["title"],allArticle["article"][i]["time"]))

# findAll("王二麻子")

#4.可查看其中一篇文章
def findOneArticle(name,path="Article"):
    allArticle = readArticle(name,path)
    for i in range(len(allArticle["article"])):
        #print(allArticle["article"])
        print(i+1,"标题是：%s,时间是：%s"%(allArticle["article"][i]["title"],allArticle["article"][i]["time"]))

    index  = int(input("请输入要查看的文章序号："))
    print("文章标题:%s"%(allArticle["article"][index-1]["title"]))
    print("文章作者:%s"%(allArticle["article"][index-1]["author"]))
    print("文章时间:%s"%(allArticle["article"][index-1]["time"]))
    print("文章内容:%s"%(allArticle["article"][index-1]["content"]))

# findOneArticle("王二麻子")

#5.删除文章
def deleteArticle(name,path="Article"):
    allArticle = readArticle(name,path)
    for i in range(len(allArticle["article"])):
        #print(allArticle["article"])
        print(i+1,"标题是：%s,时间是：%s"%(allArticle["article"][i]["title"],allArticle["article"][i]["time"]))
    if len(allArticle["article"])!=0:
        index  = int(input("请输入删除的文章序号："))
        print("文章标题:%s"%(allArticle["article"][index-1]["title"]))
        print("文章作者:%s"%(allArticle["article"][index-1]["author"]))
        print("文章时间:%s"%(allArticle["article"][index-1]["time"]))
        print("文章内容:%s"%(allArticle["article"][index-1]["content"]))

        allArticle["article"].pop(index-1)
        updateArticle(name,allArticle,path)
        print("该文章已删除！")
    else:
        print("文章不存在！")

# deleteArticle("王二麻子")

#6.修改文章
def editArticle(name,path="Article"):
    allArticle = readArticle(name, path)
    for i in range(len(allArticle["article"])):
        # print(allArticle["article"])
        print(i + 1, "标题是：%s,时间是：%s" % (allArticle["article"][i]["title"], allArticle["article"][i]["time"]))
    if len(allArticle["article"]) != 0:
        index = int(input("请输入修改的文章序号："))

        print("开始修改文章了！！！")
        title = input("请输入修改文章标题：")
        content = input("请输入修改文章内容：")
        articleDict = {
            "title": title,
            "author": name,
            "time": time.strftime("%Y-%m-%d"),
            "content": content
        }

        allArticle["article"][index-1] = articleDict
        #更新
        updateArticle(name, allArticle, path)
    else:
        print("文章不存在！！")

# editArticle("王二麻子")

#全局变量
currentUser = ""

def Main():
    #引入全局变量
    global currentUser
    print("欢迎来到功能薄弱的博客系统".center(50,"*"))
    while True:
        print("请选择：")
        selectA = input("1.注册   2.登录   3.退出\n")
        if selectA == "1":
            register()
        elif selectA == "2":
            if login():
                while True:
                    print("请选择：")
                    selectB = input("1.写文章 2.查询文章 3.查看其中一篇文章 4.删除文章 5.修改文章 6.返回登录页面\n")
                    if selectB == "1":
                        writeArticle(currentUser)
                    elif selectB =="2":
                        findAll(currentUser)
                    elif selectB =="3":
                        findOneArticle(currentUser)
                    elif selectB =="4":
                        deleteArticle(currentUser)
                    elif selectB =="5":
                        editArticle(currentUser)
                    elif selectB =="6":
                        currentUser = ""
                        break
                    else:
                        print("输入有误，重新输入！")

        else:
            print("你已经安全的退出了华丽的博客系统，不用再来了")
            sys.exit()


Main()

'''
json  

调用方法
拆分:

注册   登录

数据结构    确定  遍历  列表  下标

拆分

验证  

全局变量：  外面  所有人都能使用   golbal 


拆分为 模块  做自己的事情  

组合起来。，，项目经理   架构师 

接口 

项目需求   

blog 系统

面向对象：



'''



'''

函数


类 

实例


单例模式

工厂模式 


封装 继承  多态






'''


# 小结：




