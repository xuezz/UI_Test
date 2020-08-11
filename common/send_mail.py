"""
@author:xue
@time:2020/8/6
@desc:
"""
import yagmail
from common.read_ini import ReadConfig


class SendMail:
    def __init__(self):
        self._config = ReadConfig()
        self._user = self._config.get('email', 'USERNAME')
        self._password = self._config.get('email', 'PASSWORD')
        self._host = self._config.get('email', 'HOST')
        self._reciver = self._config.get('email', 'RECIVER')

    def send_email(self):
        yag = yagmail.SMTP(user=self._user, password=self._password, host=self._host)
        subject = '自动化测试报告'
        body = 'This is obviously the body'
        html = '<a href="https://pypi.python.org/pypi/sky/">Click me!</a>'
        yag.send(to=self._reciver, subject=subject, contents=[body, html])
