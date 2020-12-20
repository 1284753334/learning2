#-*-coding:utf-8-*-
import base64
import logging
import traceback
from logging import handlers
import smtplib
from email.mime.multipart import MIMEMultipart  # 支持附件的发送
from email.mime.text import MIMEText
from email.header import Header

from retrying import retry

from TTADSpider.TTADSpider.utils.settings_utils import get_custom_settings
from log import Logger
from requests.exceptions import MissingSchema
# multi-user.target


class  Mail:
    def retry_if_missing_schema(exception):
        """Return True if we should retry (in this case when it's an MissingSchema), False otherwise"""
        return isinstance(exception, MissingSchema)
    smtp = smtplib.SMTP()
    # path = get_custom_settings('mail')

    def __init__(self):
        self.smtp.debuglevel = 1
        self.smtp.connect(host="smtp.qq.com")
        self.sender = '1284753334@qq.com'
        self.smtp.login(self.sender, "oiwtvumjgjndjcbb")
        self.logger = Logger()

        self.logger.info(f'正在登录 {self.sender} ...', if_print=True)
    def content(self,to_list):
        message = MIMEMultipart()
        message["From"] = Header("1284753334@qq.com", "utf-8")
        message["To"] = Header(','.join(to_list), "utf-8")
        message["Subject"] = Header("测试带有附件的邮件")
        text = MIMEText("这是一封带有附件功能的邮件", "plain", "utf-8")
        message.attach(text)  # attach 以....为附件

        with open("market_monitor_1.csv", "rb") as f:
            centos = MIMEText(f.read(), "base64", "utf-8")
            centos["Content-Disposition"] = Header("attachment;filename=mail你好.py")
            message.attach(centos)

        with open("market_monitor_2.csv", "rb") as f:
            centos = MIMEText(f.read(), "base64", "utf-8")

            centos['Content-Type'] = 'application/octet-stream'
            centos["Content-Disposition"] = Header("attachment;filename=requirements.txt")
            # centos["Content-Disposition"] = Header("attachment; filename*=UTF-8''{}".format('requirements你.txt'))
            # centos["Content-Disposition"] = Header("attachment; filename=" + base64.encode('requirements你.txt', "UTF-8"))

            message.attach(centos)
        to_list.append("18790579029@139.com")
        return message

    @retry(retry_on_exception=retry_if_missing_schema, wait_fixed=2000, stop_max_attempt_number=10)
    def sent(self,to_list):
        try:
            self.smtp.sendmail(self.sender, to_list, self.content(to_list).as_string())
            self.logger.error(f'账号 {self.sender}  邮件发送成功.')
        except:
            self.logger.error(f'账号 {self.sender}  邮件发送失败.')
            self.logger.error(traceback.format_exc())

if __name__ == '__main__':
    mail = Mail()
    to_list = ["1475590219@qq.com", "18790579029@163.com"]
    mail.content(to_list)

    mail.sent(to_list)



    # logging.basicConfig(level=logging.INFO,  # 控制台打印的日志级别
    #                     filename='sent_mail.log',
    #                     filemode='a',  ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
    #                     # a是追加模式，默认如果不写的话，就是追加模式
    #                     format=
    #                     '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
    #                     # 日志格式
    #                     )


