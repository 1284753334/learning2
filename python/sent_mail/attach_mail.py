# coding=utf8
import smtplib
from email.mime.multipart import MIMEMultipart  # 支持附件的发送
from email.mime.text import MIMEText
from email.header import Header

# multi-user.target

# u1、创建一个SMTP对象
smtp = smtplib.SMTP()
# u设置邮件发送的日志信息
smtp.debuglevel = 1

# 2、连接到指定的邮件服务器
smtp.connect(host="smtp.qq.com")
# smtp.connect("smtp.126.com", port=25)

# 3、登录到邮件服务器
sender = '1284753334@qq.com'
# smtp.login("kundianhuo@126.com", "huokundian1211")
smtp.login(sender, "oiwtvumjgjndjcbb")

# 4、创建一个支持附件的message
message = MIMEMultipart()

# 5、设置消息体
# message["From"] = Header("kundianhuo@126.com", "utf-8")
# message["To"] = Header("472759903@qq.com", "utf-8")
message["From"] = Header("1285753334@qq.com", "utf-8")
message["To"] = Header("1475590219@qq.com", "utf-8")
message["Subject"] = Header("测试带有附件的邮件")

# 6、设置正文
text = MIMEText("这是一封带有附件功能的邮件", "plain", "utf-8")
message.attach(text)  # attach 以....为附件

# 7、设置附件
#   txt能打开 ，无乱码 为 文本文件，否则 二进制文件
# with open("CentOS7配置常用软件.docx", "rb") as f:
#   centos = MIMEText(f.read(), "base64", "utf-8")
#
#    centos["Content-Disposition"] = Header("attachment;filename=CentOS7.docx")
#    message.attach(centos)
with open("mail.py", "rb") as f:
    centos = MIMEText(f.read(), "base64", "utf-8")

    centos["Content-Disposition"] = Header("attachment;filename=mail.py")
    message.attach(centos)

# with open("https加密技术.docx", "rb") as f:
#    https = MIMEText(f.read(), "base64", "utf-8")
#    https["Content-Disposition"] = Header("attachment;filename=https.docx")
#    message.attach(https)
with open("../requirements.txt", "rb") as f:
    centos = MIMEText(f.read(), "base64", "utf-8")

    centos["Content-Disposition"] = Header("attachment;filename=requirements.txt")
    message.attach(centos)

# 发送邮件
# smtp.sendmail("kundianhuo@126.com", ("472759903@qq.com",), message.as_string())
smtp.sendmail(sender, ("18790579029@163.com", "18790579029@139.com"), message.as_string())

