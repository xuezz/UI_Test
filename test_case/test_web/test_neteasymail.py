"""
@author:xue
@time:2020/8/10
@desc:
"""
from base.get_driver import GetDriver
from common.read_data import read_yaml, join_path
from pages.web_page.neteasymail import NetEasyMail
import pytest


class TestNetEasyMailLogin:
    def setup_method(self):
        self._driver = GetDriver.get_web_driver()
        self.login_page = NetEasyMail(self._driver)
        self.login_page.open_url()
        # print("setup_class")

    def teardown_method(self):
        self._driver.quit()
        # print("teardown_class")

    @pytest.mark.parametrize("uid,pw", read_yaml(join_path('data/login.yml')))
    def test_email_login(self, uid, pw):
        self.login_page.login(uid, pw)
        assert self.login_page.is_login()
