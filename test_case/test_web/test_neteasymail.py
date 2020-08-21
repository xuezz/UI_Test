"""
@author:xue
@time:2020/8/10
@desc:
"""
from time import sleep

import allure

from base.get_driver import GetDriver
from common.read_data import read_yaml, join_path
from pages.web_page.neteasymail import NetEasyMail
import pytest

from pages.web_page.send_page import SendPage


class TestNetEasyMailLogin:
    def setup_method(self):
        self._driver = GetDriver.get_web_driver()
        self.login_page = NetEasyMail(self._driver)
        self.login_page.open_url()
        self.send_page = SendPage(self._driver)
        # print("setup_class")

    def teardown_method(self):
        self._driver.quit()
        # print("teardown_class")

    @allure.step(title="发送邮件")
    @pytest.mark.parametrize("uid,pw,subject,content,receiver", read_yaml(join_path('data/login.yml')))
    def test_email_login(self, uid, pw, subject, content, receiver):
        allure.attach("描述", "登录")
        self.login_page.login(uid, pw)
        self.login_page.implicitly_wait(3)
        assert self.login_page.is_login()

        allure.attach("描述", "发送")
        self.send_page.send_email(receiver, subject, content)
        self.login_page.implicitly_wait(3)
        assert self.send_page.is_send_success()

