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
import base64
import zlib
import json
import datetime

'''

首先 token  经过了压缩和 编码 


'''
#解析token
def decode_token(token):
    # base64解码
    token_decode = base64.b64decode(token.encode())
    # 二进制解压
    token_string = zlib.decompress(token_decode)
    return token_string

# 生成token
def gen_token(page):
     ts = int(datetime.datetime.now().timestamp() * 1000)
     token_dict = {
        'rId': 100900,
        'ver': '1.0.6',
        'ts': ts,
        'cts': ts + 100 * 1000,
        'brVD': [1920, 524],
        'brR': [[1920, 1080], [1920, 1040], 24, 24],
        'bI': ['http://sz.meituan.com/meishi/c20004/', ''],
        'mT': [],
        'kT': [],
        'aT': [],
        'tT': [],
        'aM': '',
        # 'sign': 'eJwdjktOwzAQhu/ShXeJ4zYNKpIXqKtKFTsOMLUn6Yj4ofG4UjkM10CsOE3vgWH36df/2gAjnLwdlAPBBsYoR3J/hYD28f3z+PpUnmJEPqYa5UWEm0mlLBRqOSaP1qjEtFB849VeRXJ51nr56AOSVIi9S0E3LlfSzhitMix/mQwsrdWa7aTyCjInDk1mKu9nvOHauCQWq2rB/8laqd3cX+adv0zdzm3nbjTOdzCi69A/HQAHOOyHafMLmEtKXg=='
         'sign':gen_sign(page)
     }
     #二进制编码
     encode = str(token_dict).encode()
     # 二进制压缩
     compress = zlib.compress(encode)
     # base64编码
     b_encode = base64.b64encode(compress)
     # 转为字符串
     token = str(b_encode, encoding='utf-8')
     return token

#生成sign
def gen_sign(page):
    str1 = '"areaId=0&cateId=20004&cityName=深圳&dinnerCountAttrId=&optimusCode=10&originUrl=http://sz.meituan.com/meishi/c20004/&page={}&partner=126&platform=1&riskLevel=1&sort=&userId=&uuid=e2d479366fd240f98b32.1565785405.1.0.0"'
    str2 = '"areaId=0&cateId=20004&cityName=深圳&dinnerCountAttrId=&optimusCode=10&originUrl=http://sz.meituan.com/meishi/c20004/pn{}/&page={}&partner=126&platform=1&riskLevel=1&sort=&userId=&uuid=e2d479366fd240f98b32.1565785405.1.0.0"'

    if page == 1:
        s = str1.format(str(page))
    else:
        s = str2.format(str(page),str(page))
    # 二进制编码
    s = s.encode()
    # 二进制压缩
    s = zlib.compress(s)
    # base64编码
    s = base64.b64encode(s)
    # 转为字符串
    s = str(s, encoding='utf-8')
    return s

if __name__ == '__main__':
    #token ='eJxNjltvozAUhP+LX0GxIVzzFja0zRUIBXZZ9QEIAUNIwDZQqPa/r1dtpX2aOd+ZkeYDkO0FrCSETIREMOQErIC0QAsNiIBR/lE1VTdUVTUNZSmC7H+mybrOSykJN2D1WzJlJKqy8vaPnDn4JBIy0Jv47RXuZUX8TG15CJSMtSsI6bxocsz65L7IHg3knpYYZjJCSIF8C+CF5pUXuNZfmnwp+76PfDzPUlzcuct346UKpG6c116ZC34Zp350eL60e+tpSlqPUmqFz322OQT18f0RNsSt7S463LvCPKMw0gX3/VolOUoN25LJVBSIrt1ztx1qQ/hV9bpwJSbU2LqL7OtxlKb0uGXqvO+kH1SNi01fqEFMWs8ZXEzwgdTzy63Fjh/uILrtT+3PvVq3NBeCpIfs6fF6q1LqVH13udpTrOinGJOBQGz5guNH8dRZZ2Fg4W5MbAc68vySeZpcwma8mixZesuKnqjrepOGNKs0RhjjoMHgz1/Se5J6'
    token = 'eJxVUn+PojAQ/S5N9J/1hAIimJgLK7q66qn4K+dlcyltgSoCtgVPL/fdr+pu7jZpOq9vpi8zr/0N+IiADtR1V9cboKIcdABs6k0bNIAUKtOyHdd2TNeEhtUA+DNnOLABQr7xQecHdA29YcH2240JFPFgoO7ob40PbCmsdAzrVjVSRSCRshAdTRPX5pEyWaKsifOjprBImIYh1FQnH0WqPxZdPhVWhnamoRbTjHKU/ixQTL8iLFmedUXBiLqQERrRDNM6p6eSCtnLCe1SNUQbW2GkQ9dCkeuEJrSxSSLTsnUDt+pFimSU82MX1hFBhcx5F5Uyr4sS4x5K0xDhw5qn3XtrNdOrGQO18kKyYym+HKVg/7f5L6XQY4qAijKVNXOQcxazTGnVTP+hZrRueq2boto+O3OnHu7coXLoHoFy9LhSjqp4eI/oPcqP81S9rrJTsDhTiL6eyX4FT961v0ioxhan7YHtfqXfbL9Xeqc+8W2PP5vhAobLaZLvLD4/9MVusCqWeHSZbJ5M5mQ6jP3x01Ve8pfzwvLGxatT5bSvVVFbq+Zw7c/T/eRcTbCcJUM5SjfrXIZ5NTVP59O+R8aBazkBDWRofV8bjj1aHyZbTJerGbFHwfR5P+B+uaO2mAc7X3/ytwWOC2dcGPoVWmejKofLMsFbvqmG6gttkbZaMkKGLJnZ1nwxnoX7oqDP7RcUxGTmmQjxquVprd1y7XTBn79KX/KH'
    #   bs64解码
    token1 = json.loads(decode_token(token).decode())
    print(token1)
    print('=' * 600)
    sign = "eJwdjU1qwzAQhe+ShZbSWLGdpKBFyapQsssBVGucDLUkMxoVmrPkEqWLnqg9R0VW7+Pxfjae0b8EB2rygg0sAPRqIvk8+Yju7+fr9/6tAqWEfMw1ybMIt5zKq1Cs5ZgDug5UZrpQOvPiriLrkzHlpiOSVJ/0lKNpXK5kpse+Uau/tFoTljbsOjuqdfEyZ47NZirvr/iBS+OSWZyqBR+vtVJwaEO/O2zHcQ62h/mwf9ta3Q3jsNsPPQy606Bh8w/ZiUmi"
    sign = decode_token(sign).decode()
    print(sign)
    print('='*600)
    #
    # token = 'eJyNj0uPmzAUhf+Lt6DYODxMpC4gGQohBMJjSKlmAYECQZDwmgSq/vcazcyiu0pXOsffPT6yf4POSMGGQ0hGiAXvWQc2gFuhlQhYMPR0I4iCREQiSIjQwOVfxklrFiTd6w5sfnIyRiwm/NtCXAo+CEfvvbFfnqce83SWlEFDoBiG+wbCfl7VWTmMcbO63GpIfV+U8IIRQjy8NxjS9/xPFNDi2l+KJZ6wnEgWUC2Aavypw9fZor+lxX2ZN9Rl+0d69QdbmV8C91fmPdpXWEdV5Zmy0kbqaSxn5XoklTbaTnNn3Elrp23gq2WtpKHZjGYs2dgvtjKzV0u5eqadGotIt3Jfdg7lgcDzLK87RttNVaGfjwdoPS3opRPvqokTxs6Pg29oW75owloz10chaLsssnxl9gJBEHORw8OJEPvd6/ampqdqr2NjfE5WE7iR7jGRURTqLREhn2djE/a1Ory0Tt8O6km+wUSREjO9k3NymrAOh+7sXY82j3lmp7ehG47d0Xnk373R+Ab+/AXm559z'
    # token1 = json.loads(decode_token(token).decode())
    # print(token1)
    # print('=' * 60)
    # sign = "eJwdjTtOAzEURfeSwqV/mZkkSK9AqZBQuizAjN8kFuOPnp+RyFqyCUTBimAdWKnuKa7O2ThC9+JBi9kxdrBa60HMgT9PLiL8/Xz93r+FDykhHXNL/MxM/Sdy4RBbPWaPYLTIFC4hnWmFK3N5UqreZMTAzSU556g612tQ88OvSrJKFHdBsH2IuxyMnURZHS+ZIhhBob6/4geunWsmBtEqPsqtBQ9o/bA7bKdp8XbQy2H/trXSjNO424+DHqWRWurNPwgGSuI="
    # sign = decode_token(sign).decode()
    # print(sign)
    # print('=' * 60)
    #
    mystr = '"areaId=0&cateId=20004&cityName=深圳&dinnerCountAttrId=&optimusCode=10&originUrl=http://sz.meituan.com/meishi/c20004/pn2/&page=2&partner=126&platform=1&riskLevel=1&sort=&userId=&uuid=e2d479366fd240f98b32.1565785405.1.0.0"'
    print(mystr)

    # 二进制编码
    encode = mystr.encode()
    # 二进制压缩
    compress = zlib.compress(encode)
    # base64编码
    b_encode = base64.b64encode(compress)
    # 转为字符串
    mystr = str(b_encode, encoding='utf-8')
    print(mystr)
    print('=' * 60)
    #
    # token = 'eJyNj0tvozAUhf+Lt0GxeQWI1EXolAlBQADTJhl1QXhTINSYEKj63+uq7aK7ka50Pp97dHT9BoiZgDWPkIYQB64pAWvAL9FyBThAe7aRV7KiaitBZsCB+LenSBIHzuTxD1j/4zUBcYIqPX86PjO+HB6p6Jn7YYmxILH5TJksBApKuzWE/bxs0pIOUbuMLw1k3BcljAWEkAS7VoTsnv+LChCw8gazcqYv3xp9K/152+yjrLMv85ZRuhuTClPXmx88P0uD8TXUtGv/4h0sPSwfCrc45e0Q10avZlWc+mNNjrq1y/3zxiUGFg0jaxV9KlJoPt1c8+je8s1fOwwW+3Np0lfYrmA2C7DwUGd22hjs5x2GUh27tv+Etabig81UHByTKPh0LzpyaHWLySz1BtFpejR40qV5TWhWY+8SJuNJSe63gz1Qh9iXZmHzoeJHoVVdZ7EyyGHv3IwIlddkilTj7GyVeCsl8oGg0xGjVMyPlYb9/UK10VgGvL5plGysrGDw7sD7B7u5oTk='
    # token1 = json.loads(decode_token(token).decode())
    # print(token1)
    # print('=' * 60)
    # sign = "eJwdjTtOQzEQRfeSwqU99vskQXKBUiEhOhZgnuclFs8fjceRwlrYBKJgRbAOrFT3FFfn7Byhe/IWxOIYOxgAGMUS+PbiItq/n6/fz2/hQ0pIp9wSPzJT/4lcOMRWT9mj1SAyhXNIr7TZC3N5UKp+yIiBm0tyyVF1rpeglrtflTQoUdwZ7dCHuMutNrMom+M1U7RaUKjvz3jFrXPNxFa0ivdya8FbNH7cH4d5Xr0ZYT0e3gYj9TRP+8M0wiS1BAm7fwjKSuQ="
    # sign = decode_token(sign).decode()
    # print(sign)
    # print('=' * 60)
    #
    mystr = '"areaId=0&cateId=20004&cityName=深圳&dinnerCountAttrId=&optimusCode=10&originUrl=http://sz.meituan.com/meishi/c20004/pn3/&page=3&partner=126&platform=1&riskLevel=1&sort=&userId=&uuid=e2d479366fd240f98b32.1565785405.1.0.0"'
    print(mystr)
    #
    # 二进制编码
    encode = mystr.encode()
    # 二进制压缩
    compress = zlib.compress(encode)
    # base64编码
    b_encode = base64.b64encode(compress)
    # 转为字符串
    mystr = str(b_encode, encoding='utf-8')
    print(mystr)
    print('=' * 60)
    # print(gen_sign(3))
