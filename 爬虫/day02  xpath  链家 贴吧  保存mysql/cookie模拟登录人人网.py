
import  requests


headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
    # 'Cookie' :'anonymid=kezmeb8ly7gbny; _r01_=1; JSESSIONID=abcvRgEd1T_Tp7KrLmcsx; ick_login=3c3e85de-03d4-4983-9ca2-c78eaece58ea; taihe_bi_sdk_session=0f2cbd077d24f948e6f94542ecb9f716; taihe_bi_sdk_uid=c4d8d0ee8317cf647674e6e7921d4e89; depovince=GW; jebecookies=5e50e3ed-4648-47f1-8b0b-c6492dafb61e|||||; _de=32B20555AD3784A6BF2D3D01B72FE013; p=fb4174e0fe65b3f109d384d428f114952; ap=966924492; first_login_flag=1; ln_uact=17752558702; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=9f3b492932c41601e3742b29dc6b37ab2; societyguester=9f3b492932c41601e3742b29dc6b37ab2; id=966924492; xnsid=ab47b698; ver=7.0; loginfrom=null'

}
response = requests.get('http://www.renren.com/966924492/newsfeed/photo',headers=headers)

print(response.text)
print(response.status_code)

# #  获取 Cookie 对象
# cookie_obj = response.cookies
# print(cookie_obj)
# # 将cookie_obj 转换为 字典：
#
# cookies = requests.utils.dict_from_cookiejar(cookie_obj)
# print('dict',cookies)

#   人人：
#  账号： 17752558702
#密码： qikuedu9527