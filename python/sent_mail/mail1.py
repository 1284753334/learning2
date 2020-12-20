# coding=utf8

"""
    邮件：
        发送(smtp)
        接收(pop3)
    smtplib (邮件的发送)
    1、引入邮件操作的模块,
    2、获取smtp对象
    3、连接邮件服务器
    4、登录邮件服务器
    5、引入 from email.mime.text import MIMEText
    6、获取一个message (MIMEText)对象
    7、引入 Header 模块 from email.header import Header

"""
# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
#
# # 获取smtp对象
# smtp = smtplib.SMTP()
#
# # 连接邮件服务器
# smtp.connect(host="smtp.qq.com")
#
# fuser = "1475590219@qq.com"
#
# sender = '1284753334@qq.com'
#
# # 登录邮件,密码指的是邮件的登录密码/授权码(部分邮件运营商只支持授权码，例如QQ)
# smtp.login(sender, "oiwtvumjgjndjcbb")
# #smtp.login(sender, "soknkjhlhpmnbiid")
#
# # 准备开始进行邮件发送的准备工作
#
# """
#     content : 邮件的正文
#     subtype: 默认是plain，代表内容是一个字符串
#             html, 支持html网页格式
#     charset : 设置发送邮件的字符集编码格式，常用 UTF-8
# """
# message = MIMEText("这是一封测试邮件", "plain", "utf-8")
#
# # 设置发件人
# message["From"] = Header(", charset="utf-8")
# # 设置收件人，是一个列表或元组
#
# #tolist = ["kundianhuo@126.com", "kundianhuo@sina.com"]
# tolist = ["18790579029@139.com", "h18790579029@163.com"]
#
#
# message["To"] = Header(";".join(tolist), charset="utf-8")
#
# # 设置抄送
# #message["Cc"] = Header("1402607000@qq.com", charset="utf-8")
# message["Cc"] = Header("1475590219@qq.com", charset="utf-8")
#
# # 设置邮件标题
# message["Subject"] = Header("欢迎来到炬码", charset="utf-8")
#
# # 发送邮件
# tolist.append("1475590219@qq.com")
#
# smtp.sendmail(sender, tolist, message.as_string())


"""
    邮件：
        发送(smtp)
        接收(pop3)
    smtplib (邮件的发送)
    1、引入邮件操作的模块,
    2、获取smtp对象
    3、连接邮件服务器
    4、登录邮件服务器
    5、引入 from email.mime.text import MIMEText
    6、获取一个message (MIMEText)对象
    7、引入 Header 模块 from email.header import Header

"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 获取smtp对象
smtp = smtplib.SMTP()

# 连接邮件服务器
smtp.connect(host="smtp.qq.com")

fuser = "1475590219@qq.com"

sender = '1284753334@qq.com'

# 登录邮件,密码指的是邮件的登录密码/授权码(部分邮件运营商只支持授权码，例如QQ)
smtp.login(sender, "oiwtvumjgjndjcbb")
#smtp.login(sender, "soknkjhlhpmnbiid")

# 准备开始进行邮件发送的准备工作

"""
    content : 邮件的正文
    subtype: 默认是plain，代表内容是一个字符串
            html, 支持html网页格式
    charset : 设置发送邮件的字符集编码格式，常用 UTF-8
"""
# 邮件正文
message = MIMEText("这是一封测试邮件", "plain", "utf-8")

# 设置发件人
message["From"] = Header("1284753334@qq.com",charset="utf-8")
# 设置收件人，是一个列表或元组

#tolist = ["kundianhuo@126.com", "kundianhuo@sina.com"]
tolist = ["18790579029@139.com", "1475590219@qq.com"]


message["To"] = Header(",".join(tolist), charset="utf-8")

# 设置抄送
#message["Cc"] = Header("1402607000@qq.com", charset="utf-8")
message["Cc"] = Header("1284753334@qq.com", charset="utf-8")

# 设置邮件标题
message["Subject"] = Header("欢迎来到炬码", charset="utf-8")

# 发送邮件
#tolist.append("1475590219@qq.com")
tolist.append("18790579029@163.com")

smtp.sendmail(sender, tolist, message.as_string())

