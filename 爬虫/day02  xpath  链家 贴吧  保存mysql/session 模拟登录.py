import  requests

#  1. 创建session 对象 ， 可以保存Cookie值
ssion = requests.session()

#  2. 处理 header

header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'

}


#  3. 用于登录的用户名和密码
#  账号： 17752558702
#密码： qikuedu9527
data = {'email':17752558702,'password':'qikuedu9527'}

#4. 发送带用户名和密码的请求，并获取登录后的cookie值，保存在ssion里
ssion.post('http://www.renren.com/PLogin.do',data=data,headers = header)

#  5  ssion  包含用户登录后的cookie值，可以直接访问首页

response = ssion.get('http://www.renren.com/966924492')
#  打印响应的内容
print(response.text)




