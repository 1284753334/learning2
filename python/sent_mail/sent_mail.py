from html import HTML
from email.mime.text import MIMEText
# import mysql.connector
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import traceback
from html import HTML
import pdb

# 设置css样式
inline_css = {
    'black': 'color:#000000;',
    'red': 'color:#FF0000;',
    'green': 'color:#00FF00;',
}

b = HTML()

b1 = b.br("这是表格1:")

t1 = b.table(border='1', caption='table 1', width='800')
with open('market_monitor_1.csv') as f:
    lines = f.readlines()
    for line in lines:
        datas = line.split('\t')
        r1 = t1.tr()
        r1.td(datas[0], style=inline_css['black'])
        r1.td(datas[1], style=inline_css['black'])
        r1.td(datas[2], style=inline_css['black'])
        r1.td(datas[3], style=inline_css['black'])
        r1.td(datas[4], style=inline_css['black'])
        r1.td(datas[5], style=inline_css['black'])
        r1.td(datas[6], style=inline_css['black'])
        r1.td(datas[7], style=inline_css['black'])
        r1.td(datas[8], style=inline_css['black'])
        r1.td(datas[9], style=inline_css['black'])
        r1.td(datas[10], style=inline_css['black'])
        r1.td(datas[11], style=inline_css['black'])

b2 = b.br("这是表格2:")
t2 = b.table(border='1', width='600')
with open('market_monitor_2.csv') as f:
    lines = f.readlines()
    for line in lines:
        datas = line.split('\t')
        r2 = t2.tr()
        r2.td(datas[0], style=inline_css['black'])
        r2.td(datas[1], style=inline_css['black'])
        r2.td(datas[2], style=inline_css['black'])
        r2.td(datas[3], style=inline_css['black'])
        r2.td(datas[4], style=inline_css['black'])
        r2.td(datas[5], style=inline_css['black'])

b3 = b.br("各渠道当日累计转化数据详见附件：market_monitor_channel.xls")

# print(b)

# 发件人、发件邮箱服务器、收件人
mail_host = "smtp.email.qq.com"  # 设置服务器
mail_user = "1284753334@qq.com"  # 用户名
mail_pass = "oiwtvumjgjndjcbb"  # 口令

sender = '1284753334@qq.com'
receivers = ['18790579029@139.com']

# 邮件标题、发件人名称等
message = MIMEMultipart()
message['From'] = Header("发件人名称", 'utf-8')
message['To'] = Header(','.join(receivers), 'utf-8')
subject = '通知'
message['Subject'] = Header(subject, 'utf-8')

# 邮件正文内容为HTML
message.attach(MIMEText(str(b), 'html', 'utf-8'))

# 构造附件，传送当前目录下的 market_monitor_channel.xls 文件
att1 = MIMEText(open('market_monitor_channel.xls', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="market_monitor_channel.xls"'
message.attach(att1)

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print
    "邮件发送成功"
except smtplib.SMTPException:
    print
    "Error: 无法发送邮件"




