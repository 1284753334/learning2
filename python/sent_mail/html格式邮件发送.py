import smtplib
from email.mime.text import MIMEText


sender = '1284753334@qq.com'
smtp  = smtplib.SMTP()

smtp.connect('smtp.qq.com',25)
smtp.login(sender,'')

text = """
    ��ӭ<b style ='color:red'> ����</b>
"""

message = MIMEText(text,'html','utf-8')




