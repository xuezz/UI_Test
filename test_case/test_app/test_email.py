"""
@author:xue
@time:2020/7/12
@desc:
"""
import allure

from base.get_driver import GetDriver
from pages.app_page.neteasymail import NetEasyMail
import pytest


class TestAppMail:
    def setup_method(self):
        self._driver = GetDriver.get_app_driver()
        self.mail_page = NetEasyMail(self._driver)
        self.mail_page.open_app()

    def teardown_method(self):
        print("teardown_method")
        # self._driver.close_app()
        # self._driver.reset()
        self._driver.terminate_app(self.mail_page.package_name)
        self._driver.quit()

    @allure.step(title="发送邮件")
    def test_sendmail(self):
        allure.attach("描述", "登录")
        self.mail_page.login()
        # allure.attach("描述", "发送")
        # self.mail_page.send_email()
        # self.mail_page.save_img("发送截图")
