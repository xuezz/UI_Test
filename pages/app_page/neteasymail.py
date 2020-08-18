"""
@author:xue
@time:2020/8/11
@desc:
"""
import allure
from selenium.webdriver.common.by import By

from base.app_base import AppBase


class NetEasyMail(AppBase):
    package_name = 'com.netease.mail'
    active_name = 'com.netease.mobimail.activity.AddAccountActivity'
    account_input = By.ID, 'com.netease.mail:id/editor_email'
    password_input = By.ID, 'com.netease.mail:id/editor_password'
    login_btn = By.ID, 'com.netease.mail:id/register_button_next'
    next_btn = By.ID, 'com.netease.mail:id/button_next'
    skip_btn = By.ID, 'com.netease.mail:id/skip'
    more_btn = By.ID, 'com.netease.mail:id/iv_mail_list_plus'
    to_write_btn = By.ID, 'com.netease.mail:id/tv_write_mail'
    address_input = By.ID, 'com.netease.mail:id/mailcompose_address_input'
    subject_input = By.ID, 'com.netease.mail:id/mailcompose_subject_textedit'
    content_input = By.XPATH, "//android.widget.LinearLayout[@resource-id='com.netease.mail:id/mailcompose_content']/android.widget.EditText"
    send_btn = By.ID, 'com.netease.mail:id/send'

    def open_app(self):
        print("open_app")
        self.activity(self.package_name, self.active_name)

    @allure.step(title="初始授权")
    def app_init(self):
        pass

    @allure.step(title="登录")
    def login(self):
        self.input_text(self.account_input, "xuezz1997@163.com")
        self.input_text(self.password_input, '11250520.')
        self.click(self.login_btn)
        self.click(self.next_btn)
        # self.click(self.skip_btn)

    @allure.step(title="发送邮件")
    def send_email(self):
        self.click(self.more_btn)
        self.click(self.to_write_btn)
        self.input_text(self.address_input, 'uoykiki@163.com')
        self.input_text(self.subject_input, '测试')
        self.input_text(self.content_input, '测试')
        self.click(self.send_btn)
