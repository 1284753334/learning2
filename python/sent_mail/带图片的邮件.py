# -*-coding:gb18030

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header

# 1������һ��smtp����
smtp = smtplib.SMTP()
# 2������smtp������
sender = '1284753334@qq.com'
smtp.connect("smtp.qq.com", 25)
# 3����¼�˺�
smtp.login(sender, "oiwtvumjgjndjcbb")

smtp.debuglevel = 1

# 4��������Ϣ��
message = MIMEMultipart()

# 5���������
msg = """
        <a href='http://www.baidu.com'>�ٶ�</a>
        <a href='http://www.sina.com'>����</a>
        <a href='http://www.yahoo.com'>�Ż�</a>
        <br/>
        <img src='cid:img1' width='200px' height='200px' />
    """
text = MIMEText(msg, "html", 'utf-8')

message.attach(text)

# �� img src �������滻��������ͼƬ

with open("timg.jpg", "rb")as f:
    image = MIMEImage(f.read(), **{"_subtype": ".jpg"})
    # �滻msg�е� cid��Ӧ������
    image.add_header("Content-ID", "<img1>")
    message.attach(image)


# ��ʼָ��message��ͷ
message["From"] = Header(sender,charset="utf-8")

to_list = ["1475590219@qq.com", "18790579029@163.com"]

message["To"] = Header(";".join(to_list),charset="utf-8")

message["Subject"] = "�����д���ͼƬ���ʼ�"

# �����ʼ�
smtp.sendmail(sender, to_list, message.as_string())

# �ر�smtp
smtp.close()