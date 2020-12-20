# -*-coding:gb18030

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header

# 1、创建一个smtp对象
smtp = smtplib.SMTP()
# 2、连接smtp服务器
sender = '1284753334@qq.com'
smtp.connect("smtp.qq.com", 25)
# 3、登录账号
smtp.login(sender, "oiwtvumjgjndjcbb")

smtp.debuglevel = 1

# 4、创建消息体
message = MIMEMultipart()

# 5、添加正文
msg = """
        <a href='http://www.baidu.com'>百度</a>
        <a href='http://www.sina.com'>新浪</a>
        <a href='http://www.yahoo.com'>雅虎</a>
        <br/>
        <img src='cid:img1' width='200px' height='200px' />
    """
text = MIMEText(msg, "html", 'utf-8')

message.attach(text)

# 把 img src 的内容替换成真正的图片

with open("timg.jpg", "rb")as f:
    image = MIMEImage(f.read(), **{"_subtype": ".jpg"})
    # 替换msg中的 cid对应的内容
    image.add_header("Content-ID", "<img1>")
    message.attach(image)


# 开始指定message的头
message["From"] = Header(sender,charset="utf-8")

to_list = ["1475590219@qq.com", "18790579029@163.com"]

message["To"] = Header(";".join(to_list),charset="utf-8")

message["Subject"] = "正文中带有图片的邮件"

# 发送邮件
smtp.sendmail(sender, to_list, message.as_string())

# 关闭smtp
smtp.close()